#!/usr/bin/env python3
"""Finite checks for commuting pairs of Gödel-chain monadic roundings.
Run: python3 verify.py
Uses only the Python standard library.
"""

from itertools import product
from collections import Counter


def roundings(n, mask):
    retained = (0,) + tuple(i for i in range(1, n - 1)
                            if mask & (1 << (i - 1))) + (n - 1,)
    lower = tuple(max(t for t in retained if t <= x) for x in range(n))
    upper = tuple(min(t for t in retained if t >= x) for x in range(n))
    return retained, lower, upper


def commute(f, g):
    return all(f[g[x]] == g[f[x]] for x in range(len(f)))


def intersection_roundings(n, r, s):
    common = set(r) & set(s)
    return (tuple(max(t for t in common if t <= x) for x in range(n)),
            tuple(min(t for t in common if t >= x) for x in range(n)))


def gap_criterion(n, r, s):
    common = sorted(set(r) & set(s))
    for lo, hi in zip(common, common[1:]):
        seg_r = any(lo < t < hi and t not in s for t in r)
        seg_s = any(lo < t < hi and t not in r for t in s)
        if seg_r and seg_s:
            return False
    return True


def axioms(n, lower, upper):
    # The actual monadic Gödel equations M1--M4 of Castaño et al.
    # M5 is automatic on Gödel chains: x*x=x.
    top = n - 1
    def imp(x, y):
        return top if x <= y else y
    for x in range(n):
        if imp(lower[x], x) != top:  # M1
            return False
        for y in range(n):
            if lower[imp(x, lower[y])] != imp(upper[x], lower[y]):  # M2
                return False
            if lower[imp(lower[x], y)] != imp(lower[x], lower[y]):  # M3
                return False
            if lower[max(upper[x], y)] != max(upper[x], lower[y]):  # M4
                return False
    return True


def main():
    seq = [1, 4]
    for n in range(2, 13):
        k = n-2
        while len(seq) <= k:
            seq.append(4*seq[-1] - 2*seq[-2])
        all_ops = [roundings(n, mask) for mask in range(1 << k)]
        total = 0
        for r, f, e in all_ops:
            assert axioms(n, f, e), ('rounding-invalid',n,r)
            for s, g, h in all_ops:
                box_commutes = commute(f,g)
                diamond_commutes = commute(e,h)
                criterion = gap_criterion(n,r,s)
                assert box_commutes == diamond_commutes == criterion, (
                    'equivalence-failed', n, r, s)
                if criterion:
                    total += 1
                    fmeet, emeet = intersection_roundings(n,r,s)
                    assert tuple(f[g[x]] for x in range(n)) == fmeet
                    assert tuple(e[h[x]] for x in range(n)) == emeet
        assert total == seq[k], ('count-mismatch',n,total,seq[k])
        print('n =', n, 'compatible pairs =', total)

    # Exhaust all pairs of unary maps on chains up to four elements and
    # test the literal M1--M5 axioms, independently of subchain classification.
    for n in (2,3,4):
        all_maps = tuple(product(range(n), repeat=n))
        classified = set()
        for mask in range(1 << (n-2)):
            r, f, e = roundings(n,mask)
            classified.add((f,e))
        survivors = set()
        for f in all_maps:
            for e in all_maps:
                if axioms(n,f,e):
                    survivors.add((f,e))
        assert survivors == classified, ('monadic-classification', n,
                                         len(survivors), len(classified))
        print('direct unary-map check n =', n, 'survivors =', len(survivors))
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
