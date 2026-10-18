#!/usr/bin/env python3
"""Finite checks for exact joint-tail and coincidence identities in overpartitions.

The limiting statements require the analytic argument in RESULT.md;
finite integer checks below are not proofs of asymptotic convergence.
"""
from collections import Counter
from itertools import product
from math import isqrt, pi, exp


def overpartition_numbers(N):
    p = [0] * (N + 1)
    p[0] = 1
    for m in range(1, N + 1):
        for j in range(m, N + 1):
            p[j] += p[j - m]
    for m in range(1, N + 1):
        for j in range(N, m - 1, -1):
            p[j] += p[j - m]
    return p


def partition_shapes(n, minimum=1):
    if n == 0:
        yield ()
    else:
        for j in range(minimum, n + 1):
            for rest in partition_shapes(n - j, j):
                yield (j,) + rest


def overpartition_profiles(n):
    for shape in partition_shapes(n):
        count = Counter(shape)
        keys = sorted(count)
        for overline_pattern in product((0, 1), repeat=len(keys)):
            yield {k: count[k] - b for k, b in zip(keys, overline_pattern)}


def minimum_gap(profile, r):
    j = 1
    while profile.get(j, 0) >= r:
        j += 1
    return j


def reduced_count(p, n, d):
    return p[n - d] if 0 <= d <= n else 0


def joint_count_formula(p, n, bounds):
    # Each (r,k) asserts the r-gap exceeds k.
    largest_r = max((r for r, k in bounds), default=0)
    d = 0
    for a in range(1, largest_r + 1):
        max_k = max((k for r, k in bounds if r >= a), default=0)
        d += max_k * (max_k + 1) // 2
    return reduced_count(p, n, d)


def tie_count_formula(p, n, r, s):
    count = 0
    j = 1
    while s * j * (j - 1) // 2 <= n:
        h = s * j * (j - 1) // 2
        count += reduced_count(p, n, h) - reduced_count(p, n, h + r * j)
        j += 1
    return count


def main():
    p = overpartition_numbers(1600)
    expected = (1, 2, 4, 8, 14, 24, 40, 64, 100, 154, 232)
    assert tuple(p[:len(expected)]) == expected
    enumeration_checks = 0
    joint_checks = 0
    tie_checks = 0
    for n in range(13):
        profiles = list(overpartition_profiles(n))
        assert len(profiles) == p[n]
        enumeration_checks += 1
        for r, s in ((1, 2), (1, 3), (2, 3)):
            direct = sum(minimum_gap(prof, r) == minimum_gap(prof, s) for prof in profiles)
            assert direct == tie_count_formula(p, n, r, s), (n, r, s, direct)
            tie_checks += 1
        for bounds in (((1, 0), (2, 1)), ((1, 1), (2, 2)),
                       ((2, 2), (3, 1)), ((1, 2), (2, 1), (3, 2)),
                       ((1, 0), (2, 0), (3, 3)), ((3, 1),)):
            direct = sum(all(minimum_gap(prof, r) > k for r, k in bounds) for prof in profiles)
            exact = joint_count_formula(p, n, bounds)
            assert direct == exact, (n, bounds, direct, exact)
            joint_checks += 1
    # Numerical asymptotic trend only: not a substitute for the limit proof.
    n1, n2 = 400, 1600
    for r, s in ((1, 2), (1, 3), (2, 3)):
        err1 = abs(tie_count_formula(p, n1, r, s) / p[n1] - r / s)
        err2 = abs(tie_count_formula(p, n2, r, s) / p[n2] - r / s)
        assert err2 < err1
    print(f'PASS: {enumeration_checks} full overpartition enumerations, '
          f'{joint_checks} joint-tail comparisons, {tie_checks} tie comparisons; '
          'three finite asymptotic trend checks')
    print('No finite test verifies the general limit theorem.')


if __name__ == '__main__':
    main()
