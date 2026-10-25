#!/usr/bin/env python3
"""Exact finite cross-checks for the resolving number of Johnson graphs.

No external packages are required. The assertions here test the all-parameter
proof's binomial identities on finite ranges; they do not replace that proof.
"""
from itertools import combinations
from math import comb


def binom(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def equalizers(n, k, r):
    return sum(comb(r, j) ** 2 * binom(n - 2*r, k - 2*j)
               for j in range(r + 1))


def formula(n, k):
    k = min(k, n-k)
    if n == 4 and k == 2:
        return 5
    if n == 8 and k == 4:
        return 37
    return comb(n, k) - 2 * comb(n-2, k-1) + 1


def coefficient_lemma(r):
    # (1+z)^(2r-1)(1+z^2)-(1+z)sum_j C(r,j)^2 z^(2j)
    for h in range(2*r+2):
        lhs = binom(2*r-1, h) + binom(2*r-1, h-2)
        rhs = binom(r, h//2)**2 if h//2 <= r else 0
        assert lhs >= rhs, (r, h, lhs, rhs)


def exact_pairs(n, k):
    verts = [sum(1 << i for i in a) for a in combinations(range(n), k)]
    # Count via explicit distances to all vertices, without using the
    # binomial intersection formula.
    maximum = 0
    classes = {}
    for i, a in enumerate(verts):
        for b in verts[i+1:]:
            r = k - (a & b).bit_count()
            count = sum((a & x).bit_count() == (b & x).bit_count()
                        for x in verts)
            classes.setdefault(r, set()).add(count)
            maximum = max(maximum, count)
    assert all(len(v) == 1 for v in classes.values()), (n, k, classes)
    for r, counts in classes.items():
        assert next(iter(counts)) == equalizers(n, k, r), (n,k,r)
    assert maximum + 1 == formula(n,k), (n,k,maximum+1,formula(n,k))
    return len(verts), maximum + 1


def main():
    for r in range(1, 151):
        coefficient_lemma(r)
    print('COEFFICIENT_LEMMA_PASS r=1..150')
    pairs = 0
    for n in range(2, 81):
        for k in range(1, n//2 + 1):
            ours = formula(n,k)
            exact = max(equalizers(n,k,r) for r in range(1,k+1)) + 1
            assert ours == exact, (n,k,ours,exact)
            pairs += 1
    print('JOHNSON_CLASSIFICATION_PASS n=2..80, cases=',pairs)
    for n in range(2, 11):
        for k in range(1, n//2+1):
            if comb(n,k)>150:
                continue
            count, threshold=exact_pairs(n,k)
            print('EXHAUSTIVE_PASS',n,k,'vertices',count,'threshold',threshold)
    print('ALL_PASS')

if __name__ == '__main__':
    main()
