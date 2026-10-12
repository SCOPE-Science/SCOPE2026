#!/usr/bin/env python3
"""Exact finite checks for permutation corner-process and inversion lemmas."""
from itertools import permutations
from collections import Counter
from fractions import Fraction as F
from math import factorial


def inv(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def corner_cells(n, r):
    return {(i, j) for i in range(1, n + 1) for j in range(1, n + 1)
            if abs(i - j) >= n - r}


def compatible_pairs(a):
    return sum(1 for x in a for y in a if x[0] != y[0] and x[1] != y[1])

permutations_checked = 0
factorial_moments_checked = 0
for n in range(2, 9):
    inv_sum = inv_sq_sum = 0
    max_identity = True
    cells = [corner_cells(n, r) for r in range(1, min(n, 4))]
    wm1 = [0] * len(cells)
    wm2 = [0] * len(cells)
    for p in permutations(range(1, n + 1)):
        permutations_checked += 1
        k = inv(p)
        inv_sum += k
        inv_sq_sum += k * k
        max_d = max(abs(i - v) for i, v in enumerate(p, start=1))
        min_corner_sum = min(min(i + (n + 1 - v), (n + 1 - i) + v)
                             for i, v in enumerate(p, start=1))
        assert n - max_d == min_corner_sum - 1
        points = {(i, v) for i, v in enumerate(p, start=1)}
        for j, a in enumerate(cells):
            w = len(points & a)
            wm1[j] += w
            wm2[j] += w * (w - 1)
    count = factorial(n)
    assert F(inv_sum, count) == F(n * (n - 1), 4)
    assert F(inv_sq_sum, count) - F(inv_sum, count) ** 2 == F(n * (n - 1) * (2 * n + 5), 72)
    for j, a in enumerate(cells):
        r = j + 1
        assert F(wm1[j], count) == F(len(a), n)
        assert F(wm2[j], count) == F(compatible_pairs(a), n * (n - 1))
        factorial_moments_checked += 2

conditional_checks = 0
for n in range(3, 8):
    for fixed in [
        {1: n}, {n: 1}, {1: n, n: 1},
        {1: n - 1, n: 1}, {2: n, n: 2},
    ]:
        if len(set(fixed.values())) != len(fixed):
            continue
        positions = [i for i in range(1, n + 1) if i not in fixed]
        values = sorted(set(range(1, n + 1)) - set(fixed.values()))
        actual = Counter()
        for values_perm in permutations(values):
            actual[inv(values_perm)] += 1
            p = [fixed.get(i) for i in range(1, n + 1)]
            for i, v in zip(positions, values_perm):
                p[i - 1] = v
            k = inv(p)
            rem = inv(values_perm)
            assert abs(k - rem) <= len(fixed) * n
        theoretical = Counter(inv(t) for t in permutations(range(1, n - len(fixed) + 1)))
        assert actual == theoretical
        conditional_checks += 1

print('VERIFY_OK permutations=%d factorial_moment_checks=%d conditional_remainder_checks=%d' %
      (permutations_checked, factorial_moments_checked, conditional_checks))
