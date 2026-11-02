#!/usr/bin/env python3
"""Finite-transition certificate and independent short-word tests.

The infinite statement follows from the finite closure and the proof in RESULT.md;
short-word enumeration is an independent diagnostic, not an infinite proof.
"""
from collections import deque
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parent
R = (1, 2, 0)
T = (0, 2, 0)
Z = (0, 0, 0)


def action(table, state, word):
    for symbol in word:
        state = table[int(symbol)][state]
    return state


def pair_certificate(A):
    machines = ((T, R), (R, T))
    a_actions = [tuple(action(machine, q, A) for q in range(3))
                 for machine in machines]
    start = tuple(z for j in range(2) for z in (a_actions[j][0], 0))

    def transition(state, symbol):
        out = []
        for j, machine in enumerate(machines):
            f = machine[int(symbol)]
            out.extend((f[state[2*j]], f[state[2*j+1]]))
        return tuple(out)

    # phase 0: expect A[0]; phase 1: expect A[1]; phase 2: dead
    def phase_next(phase, letter):
        if phase == 2:
            return 2
        return (phase + 1) % 2 if letter == A[phase] else 2

    states = [(start, 0)]
    indices = {states[0]: 0}
    q = deque(states)
    while q:
        st, ph = q.popleft()
        for letter in '01':
            nxt = (transition(st, letter), phase_next(ph, letter))
            if nxt not in indices:
                indices[nxt] = len(states)
                states.append(nxt)
                q.append(nxt)
    assert len(states) == 31, (A, len(states))
    assert sum(ph == 0 for _, ph in states) == 2
    assert sum(ph == 1 for _, ph in states) == 2
    assert sum(ph == 2 for _, ph in states) == 27

    rows = []
    for st, ph in states:
        equal = all(st[2*j] == a_actions[j][st[2*j+1]] for j in range(2))
        assert equal == (ph == 0), (A, st, ph, equal)
        successors = [indices[(transition(st, c), phase_next(ph, c))] for c in '01']
        rows.append((A, indices[(st,ph)], *st, ph, int(equal), *successors))
    return rows


def shift_two(w):
    return w[2:] + w[:2]


def sep_two_criterion(w):
    v = shift_two(w)
    if w == v:
        return 0
    if w[-1] != v[-1]:
        return 2
    def suffix_run(s):
        j = len(s) - 1
        while j >= 0 and s[j] == s[-1]:
            j -= 1
        return len(s) - j - 1
    return 2 if (suffix_run(w) - suffix_run(v)) % 2 else 3


def expected_three_count(n):
    assert n >= 3
    return (5 * (1 << (n-2)) - (8 if n % 2 == 0 else 10)) // 3


def all_two_state_tables():
    tables = []
    maps = list(product((0, 1), repeat=2))
    for x in maps:
        for y in maps:
            tables.append((x,y))
    return tables


def four_three_state_tables():
    return ((T,R), (R,T), (Z,R), (R,Z))


def independent_small_check(max_n=14):
    # The 16 possible binary two-state transition tables are all checked directly.
    # Four explicit three-state tables are tested, without using the 31-state lemma.
    two = all_two_state_tables()
    three = four_three_state_tables()
    counts = {}
    checks = 0
    for n in range(3, max_n + 1):
        count_three = 0
        for bits in product('01', repeat=n):
            w = ''.join(bits)
            v = shift_two(w)
            if w == v:
                assert sep_two_criterion(w) == 0
                continue
            two_sep = any(action(t, 0, w) != action(t, 0, v) for t in two)
            pred = sep_two_criterion(w)
            assert (pred == 2) == two_sep, (n, w, pred)
            if not two_sep:
                assert any(action(t,0,w)!=action(t,0,v) for t in three), (n,w)
                count_three += 1
            checks += 1
        assert count_three == expected_three_count(n), (n, count_three)
        counts[n] = count_three
    return counts, checks


def main():
    header = 'A\tid\tp1\tq1\tp2\tq2\tphase\tequality\ton0\ton1\n'
    rows = pair_certificate('01') + pair_certificate('10')
    body = ''.join('\t'.join(map(str, row)) + '\n' for row in rows)
    certpath = ROOT / 'certificate.tsv'
    actual = certpath.read_text(encoding='utf-8')
    assert actual == header + body, 'certificate mismatch'
    counts, checks = independent_small_check(14)
    print('FINITE_COMMUTATION_CLOSURE_OK: 31 states for A=01, 31 for A=10')
    print('CLASS_TRANSITIONS_OK: accepted state iff B belongs to A*')
    print('TWO_STATE_ENUMERATION_OK: 16 complete tables over lengths 3..14')
    print('THREE_STATE_WITNESSES_OK: four explicit 3-state tables over lengths 3..14')
    print('NONIDENTICAL_PAIRS_CHECKED:', checks)
    print('THREE_STATE_COUNTS:', ' '.join('%d:%d' % t for t in counts.items()))
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()
