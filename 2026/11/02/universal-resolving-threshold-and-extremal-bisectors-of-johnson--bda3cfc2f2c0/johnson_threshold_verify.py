#!/usr/bin/env python3
"""Independent finite checks for Johnson-graph robust resolving thresholds.

No external packages. The exhaustive test uses original distances rather than
coefficient formulas; larger-parameter tests evaluate the separate formula.
"""
from itertools import combinations
from math import comb


def formula(n, k, r):
    return sum(comb(r, j)**2 * comb(n-2*r, k-2*j)
               for j in range(r+1) if 0 <= k-2*j <= n-2*r)


def predicted(n, k):
    if (n, k) == (8, 4):
        return (36, (4,), 35)
    b = comb(n-2, k) + comb(n-2, k-2)
    if (n, k) == (6, 3):
        return (b, (1, 2), 30)
    return (b, (1,), comb(n, 2))


def exhaustive(n, k):
    masks = [sum(1 << x for x in t) for t in combinations(range(n), k)]
    best = -1
    witness_dist = set()
    best_bisectors = set()
    for i, u in enumerate(masks):
        for v in masks[i+1:]:
            r = k - (u & v).bit_count()
            bisector = frozenset(w for w, x in enumerate(masks)
                                if (x & u).bit_count() == (x & v).bit_count())
            num = len(bisector)
            if num > best:
                best = num
                witness_dist.clear()
                best_bisectors.clear()
            if num == best:
                witness_dist.add(r)
                best_bisectors.add(bisector)
    assert (best, tuple(sorted(witness_dist)), len(best_bisectors)) == predicted(n, k), (
        n, k, best, witness_dist, len(best_bisectors), predicted(n, k))
    print('EXHAUSTIVE_OK', n, k, best, sorted(witness_dist), len(best_bisectors))


def arithmetic_check():
    cases = 0
    for n in range(6, 81):
        for k in range(3, n//2 + 1):
            b, rr, _ = predicted(n, k)
            data = [formula(n, k, r) for r in range(1, k+1)]
            got = max(data)
            assert got == b and tuple(i+1 for i, v in enumerate(data) if v == got) == rr, (n, k, data)
            cases += 1
    print('ARITHMETIC_OK', cases, 'parameter pairs up to n=80')


def ratio_check():
    for j in range(1, 26):
        lo = max(2*j, 6)
        for r in range(lo, 100):
            den = comb(2*r-2, 2*j) + comb(2*r-2, 2*j-2)
            assert comb(r, j)**2 < den, (j, r)
    print('RATIO_OK', 'strict finite base inequality tested')

if __name__ == '__main__':
    for n in range(6, 11):
        for k in range(3, n//2+1):
            exhaustive(n, k)
    arithmetic_check()
    ratio_check()
    print('VERIFY_OK')
