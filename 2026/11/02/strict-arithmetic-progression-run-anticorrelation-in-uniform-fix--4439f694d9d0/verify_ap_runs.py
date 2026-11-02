#!/usr/bin/env python3
"""Exact checks of arithmetic-progression / occupied-run covariance.

This program uses two independent finite calculations: exhaustive fixed-size
subsets and hypergeometric overlap counting. The general positivity proof is
algebraic and is supplied separately; enumeration does not certify infinity.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def all_aps(n, ell):
    return [frozenset(a + j * d for j in range(ell))
            for d in range(1, (n - 1) // (ell - 1) + 1)
            for a in range(1, n - (ell - 1) * d + 1)]


def probability(n, k, s):
    if k < s or s > n:
        return Fraction(0)
    return Fraction(comb(n - s, k - s), comb(n, k))


def formula_overlap(n, ell, k):
    q = (n - 1) // (ell - 1)
    T = q * n - (ell - 1) * q * (q + 1) // 2
    N2 = (ell - 1) * (n - ell + 1)
    N1 = 2 * ell * T - 2 * q - 2 * N2
    N0 = (n - 1) * T - N1 - N2
    v = sum(Nj * probability(n, k, ell + 2 - j)
            for j, Nj in enumerate((N0, N1, N2)))
    v -= T * (n - 1) * probability(n, k, ell) * probability(n, k, 2)
    return v


def formula_endpoints(n, ell, k):
    if n == ell + 1:
        assert k == ell
        return Fraction(2 * (ell - 1), n * n)
    q = (n - 1) // (ell - 1)
    T = q * n - (ell - 1) * q * (q + 1) // 2
    D = n * (n - ell + 1) - ell * T
    E = ell * T - n * q
    alpha = Fraction((ell - 1) * D, n * (n - ell))
    beta = Fraction(2 * E, n * (n - ell))
    return (probability(n, k, ell) * Fraction(n - k, n - ell - 1)
            * ((n - 1 - k) * alpha + (k - ell) * beta))


def direct_covariance(n, ell, k, aps):
    sx = sy = sxy = 0
    count = 0
    for tup in combinations(range(1, n + 1), k):
        chosen = set(tup)
        X = sum(ap.issubset(chosen) for ap in aps)
        Y = sum(i in chosen and i + 1 in chosen for i in range(1, n))
        sx += X
        sy += Y
        sxy += X * Y
        count += 1
    assert count == comb(n, k)
    return Fraction(sxy, count) - Fraction(sx * sy, count * count)


def verify(max_n=12):
    checks = 0
    for n in range(4, max_n + 1):
        for ell in range(3, n):
            aps = all_aps(n, ell)
            q = (n - 1) // (ell - 1)
            T = q * n - (ell - 1) * q * (q + 1) // 2
            assert len(aps) == len(set(aps)) == T
            checks += 1
            N = [0, 0, 0]
            for ap in aps:
                for i in range(1, n):
                    N[len(ap.intersection((i, i + 1)))] += 1
            N2 = (ell - 1) * (n - ell + 1)
            N1 = 2 * ell * T - 2 * q - 2 * N2
            N0 = T * (n - 1) - N1 - N2
            assert N == [N0, N1, N2]
            checks += 1
            r = n - (ell - 1) * q
            D = n * (n - ell + 1) - ell * T
            E = ell * T - n * q
            assert D == ((ell - 2) * (q - 1) * ((ell - 1) * q + 2) // 2
                         + (r - 1) * (r + (ell - 2) * (q - 1)))
            assert 2 * E == (ell - 1) * q * ((ell - 2) * (q - 1) + 2 * (r - 1))
            assert D > 0 and E > 0
            checks += 4
            for k in range(ell, n):
                c1 = formula_overlap(n, ell, k)
                c2 = formula_endpoints(n, ell, k)
                c3 = direct_covariance(n, ell, k, aps)
                assert c1 == c2 == c3, (n, ell, k, c1, c2, c3)
                assert c1 > 0
                checks += 2
    # Verify the three-run counterpattern for k=3 by exhaustive counting.
    for n in range(5, max_n + 1):
        aps = all_aps(n, 3)
        group = defaultdict(lambda: [0, 0])
        for tup in combinations(range(1, n + 1), 3):
            chosen = set(tup)
            r = sum(i == 1 or i - 1 not in chosen for i in tup)
            x = sum(ap.issubset(chosen) for ap in aps)
            group[r][0] += x
            group[r][1] += 1
        q = (n - 1) // 2
        T = q * n - q * (q + 1)
        assert Fraction(*group[1]) == 1
        assert Fraction(*group[2]) == 0
        assert Fraction(*group[3]) == Fraction(T - (n - 2), comb(n - 2, 3))
        assert Fraction(*group[3]) > 0
        checks += 4
    return checks


if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('--max-n', type=int, default=12)
    args = p.parse_args()
    print(f'PASS: {verify(args.max_n)} exact assertions (n through {args.max_n}).')
