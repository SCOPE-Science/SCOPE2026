#!/usr/bin/env python3
"""Independent finite checks for the rank-resolved constant-composition identity."""
from collections import Counter
from itertools import product
from math import comb


def onto(N, k):
    if N < 0:
        return 0
    return sum((-1) ** j * comb(k, j) * (k + 1 - j) ** N
               for j in range(k + 1))


def pairs_by_formula(n):
    result = Counter()
    for r in range(n):
        for s in range(n):
            val = n * comb(n - 1, r) * comb(n - 1, s)
            val *= onto(n - s - 1, r) * onto(n - r - 1, s)
            if val:
                result[(r + 1, s + 1)] = val
    return result


def pairs_by_exhaustion(n):
    maps = list(product(range(n), repeat=n))
    result = Counter()
    for f in maps:
        for g in maps:
            fg = tuple(f[g[a]] for a in range(n))
            gf = tuple(g[f[a]] for a in range(n))
            if len(set(fg)) == 1 and fg == gf:
                result[(len(set(f)), len(set(g)))] += 1
    return result


def main():
    for n, expected in ((1, 1), (2, 6), (3, 63), (4, 976)):
        derived = pairs_by_formula(n)
        exhaustive = pairs_by_exhaustion(n)
        assert derived == exhaustive, (n, derived, exhaustive)
        assert sum(derived.values()) == expected
        assert all(i + j <= n + 1 for (i, j) in derived)
    for N in range(35):
        for k in range(N + 2):
            left = onto(N + 1, k)
            right = (k + 1) * onto(N, k) + (k * onto(N, k - 1) if k else 0)
            assert left == right, (N, k)
    for n in range(1, 16):
        tally = pairs_by_formula(n)
        for pair, count in tally.items():
            assert tally[pair[::-1]] == count
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
