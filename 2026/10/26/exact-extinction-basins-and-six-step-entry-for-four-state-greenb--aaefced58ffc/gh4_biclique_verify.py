#!/usr/bin/env python3
"""Finite support certificate and independent site-level tests for four-state excitation."""
from collections import Counter, defaultdict
from pathlib import Path
import csv
from itertools import product
from math import comb

Q = 4
SUPPORTS = range(1, 1 << Q)


def support_step_one(s, opposite_excited):
    out = 0
    for c in range(Q):
        if s & (1 << c):
            nxt = (c + 1) % Q if c else int(opposite_excited)
            out |= 1 << nxt
    return out


def support_step(pair):
    a, b = pair
    return (support_step_one(a, bool(b & 2)),
            support_step_one(b, bool(a & 2)))


def canonical(cycle):
    return min(tuple(cycle[i:] + cycle[:i]) for i in range(len(cycle)))


def support_orbit(pair):
    seen = {}
    states = []
    while pair not in seen:
        seen[pair] = len(states)
        states.append(pair)
        pair = support_step(pair)
    return seen[pair], canonical(states[seen[pair]:])


def onto(j, n):
    return sum((-1) ** i * comb(j, i) * (j - i) ** n for i in range(j + 1))


def predicted_survivors(a, b):
    a2, a3, a4 = (onto(j, a) for j in (2, 3, 4))
    b2, b3, b4 = (onto(j, b) for j in (2, 3, 4))
    return (8*a2*b2 + 10*(a2*b3+a3*b2) + 3*(a2*b4+a4*b2)
            + 12*a3*b3 + 4*(a3*b4+a4*b3) + a4*b4)


def predicted_periodic(a, b):
    return 2*onto(2,a)*onto(2,b)+onto(4,a)*onto(4,b)


def direct_step(state, a):
    left, right = state[:a], state[a:]
    excit_left = 1 in left
    excit_right = 1 in right
    return tuple(((c + 1) % Q if c else int(excit_right)) for c in left) + tuple(
        ((c + 1) % Q if c else int(excit_left)) for c in right)


def direct_class(state, a):
    seen = {}
    history = []
    while state not in seen:
        seen[state] = len(history)
        history.append(state)
        state = direct_step(state, a)
        assert len(history) <= 13
    mu = seen[state]
    cycle = history[mu:]
    assert len(cycle) in (1, 4)
    if len(cycle) == 1:
        assert set(cycle[0]) == {0}
        return 'extinct', mu
    return 'period4', mu


def main():
    basins = defaultdict(list)
    for s in product(SUPPORTS, repeat=2):
        t, cycle = support_orbit(s)
        basins[cycle].append((s, t))

    extinct = ((1, 1),)
    dense = ((15, 15),)
    alternating = ((5, 10), (10, 5))
    assert set(basins) == {extinct, dense, alternating}
    assert {key: len(entries) for key, entries in basins.items()} == {
        extinct:170, dense:1, alternating:54}
    assert max(t for s,t in basins[extinct]) == 5
    assert max(t for s,t in basins[alternating]) == 6
    assert set(t for s,t in basins[dense]) == {0}

    # Read the complete published first-entry coefficient certificate.
    computed = Counter()
    for cyc, entries in basins.items():
        event = 'extinct' if cyc == extinct else 'period4'
        for (left,right), t in entries:
            computed[(event,t,left.bit_count(),right.bit_count())] += 1
    tabulated = Counter()
    with Path(__file__).with_name('gh4_biclique_depth_table.csv').open(
            encoding='utf-8', newline='') as inp:
        for row in csv.DictReader(inp):
            key = (row['eventual_type'], int(row['first_entry_time']),
                   int(row['left_support_size']), int(row['right_support_size']))
            assert key not in tabulated
            tabulated[key] = int(row['support_pair_count'])
    assert computed == tabulated

    # Exhaustive independent tabulation of the complete 225-state map.
    survival_hist = Counter((s[0].bit_count(), s[1].bit_count())
                            for cyc in (dense, alternating) for s,t in basins[cyc])
    assert survival_hist == {
        (2,2):8, (2,3):10, (3,2):10, (2,4):3, (4,2):3,
        (3,3):12, (3,4):4, (4,3):4, (4,4):1}

    direct_total = 0
    for a in range(1, 5):
        for b in range(1, 5):
            n_survive = n_periodic = 0
            mu_max_extinct = mu_max_survive = 0
            for state in product(range(Q), repeat=a+b):
                classification, mu = direct_class(state, a)
                if classification == 'period4':
                    n_survive += 1
                    mu_max_survive = max(mu_max_survive, mu)
                    if mu == 0:
                        n_periodic += 1
                else:
                    mu_max_extinct = max(mu_max_extinct, mu)
            assert n_survive == predicted_survivors(a,b), (a,b,n_survive)
            assert n_periodic == predicted_periodic(a,b), (a,b,n_periodic)
            direct_total += Q**(a+b)
            print('K(%d,%d): survival=%d, periodic=%d, last_extinction=%d, last_entry=%d' %
                  (a,b,n_survive,n_periodic,mu_max_extinct,mu_max_survive))

    # Independently enumerate surjective labelings on each chosen support.
    for a in range(1, 7):
        for b in range(1, 7):
            w = sum(onto(s[0].bit_count(),a)*onto(s[1].bit_count(),b)
                    for cyc in (dense,alternating) for s,t in basins[cyc])
            assert w == predicted_survivors(a,b)
    # Independent expansion of the balanced extinction formula.
    for n in range(1,31):
        extinction = 4**(2*n)-predicted_survivors(n,n)
        exact = (4*9**n+6*8**n-20*6**n+12*4**n
                 +16*3**n-28*2**n+12)
        assert extinction == exact
    print('GH4_BICLIQUE_CERTIFICATE_OK: 225 exact support pairs, '
          '%d independent full-site states, 36 weighted counts.' % direct_total)

if __name__ == '__main__':
    main()
