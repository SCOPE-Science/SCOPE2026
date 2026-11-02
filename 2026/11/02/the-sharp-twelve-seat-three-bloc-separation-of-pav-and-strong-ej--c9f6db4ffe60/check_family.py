#!/usr/bin/env python3
"""Exact arithmetic tests for the three-bloc committee theorem.

No scientific conclusion depends on floating-point arithmetic or a search cutoff.
The all-size conclusions are established in the accompanying proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product


def instance(r, s, p, h, q):
    assert min(r, s, p, h, q) >= 1
    k = r + s
    m = k + 1
    A = frozenset(range(r))
    C = frozenset(range(r, r + s))
    b = k
    types = (A | {b}, A, A | C)
    multiplicities = (p, h, q)
    W = A | C
    return m, k, types, multiplicities, W, b


def harmonic(t):
    return sum((Q(1, d) for d in range(1, t + 1)), Q(0))


def score(committee, types, mult):
    return sum((cnt * harmonic(len(committee & ballot))
                for ballot, cnt in zip(types, mult)), Q(0))


def pav_optima(m, k, types, mult):
    scores = {}
    for combo in combinations(range(m), k):
        w = frozenset(combo)
        scores[w] = score(w, types, mult)
    mx = max(scores.values())
    return [w for w, value in scores.items() if value == mx]


def full_strong_check(k, types, mult, W, b):
    """Enumerate every coalition *type-count* vector; same-type ballots are equal."""
    n = sum(mult)
    worst = None
    bad = []
    cases = 0
    for sizes in product(*(range(t + 1) for t in mult)):
        x, y, z = sizes
        if not x:  # The sole unselected candidate b has no supporter.
            continue
        chosen = [(ballot, count) for ballot, count in zip(types, sizes) if count]
        sc = sum(count for ballot, count in chosen if b in ballot)
        assert sc == x
        rho_c = Q(1, sc)
        payments = []
        for ballot, count in chosen:
            pay = rho_c if b in ballot else Q(0)
            for d in W:
                if d in ballot:
                    support = sum(cn for other, cn in chosen if d in other)
                    pay += min(Q(1, support), rho_c)
            payments.append(pay)
        cases += 1
        maxpay = max(payments)
        if maxpay <= Q(k, n):
            bad.append((sizes, maxpay))
        if worst is None or maxpay < worst[1]:
            worst = (sizes, maxpay)
    return (not bad), bad, cases, worst


def check(r, s, p, h, q, complete=True):
    m, k, types, mult, W, b = instance(r, s, p, h, q)
    P = W in pav_optima(m, k, types, mult)
    assert P == (Q(q, k) >= Q(p, r + 1))
    if complete:
        strong, bad, cases, worst = full_strong_check(k, types, mult, W, b)
        predicted = Q(r, p + h) + Q(1, p) > Q(k, p + h + q)
        assert strong == predicted, (r, s, p, h, q, bad, worst)
    return P


def main():
    samples = 0
    for r in range(1, 4):
        for s in range(1, 6):
            for p in range(1, 4):
                for h in range(1, 4):
                    for q in range(1, 7):
                        check(r, s, p, h, q)
                        samples += 1
    print('exact three-bloc formula comparisons:', samples)
    for k in range(2, 12):
        for r in range(1, k):
            lhs = Q(4*k*r)
            rhs = (Q(k+r) - Q(k, r+1))**2
            assert lhs > rhs, (k, r)
    print('exact rational below-12 necessary-inequality checks:', 55)
    for k in range(12, 25):
        r, s, p, h, q = 2, k - 2, 6, 10, 2*k + 1
        m, _, types, mult, W, b = instance(r,s,p,h,q)
        winners = pav_optima(m,k,types,mult)
        assert winners == [W]
        strong, bad, cases, worst = full_strong_check(k,types,mult,W,b)
        assert not strong
        assert (p,h,0) in [v[0] for v in bad]
        if k==12:
            actual = Q(7,24)
            target = Q(k,2*k+17)
            assert target - actual == Q(1,984)
            print('k=12: 41 voters; 13 candidates; unique PAV winner; all',cases,
                  'coalition-type profiles checked; witness margin',target-actual)
    print('family samples k=12..24:',13,'all passed')

if __name__=='__main__':
    main()
