#!/usr/bin/env python3
"""Exact rational cross-covariance check for Mallows records and descents."""
from collections import defaultdict
from fractions import Fraction
from itertools import permutations


def inversion_count(p):
    return sum(x > y for a, x in enumerate(p) for y in p[a + 1:])


def q_number(t, q):
    return sum((q**k for k in range(t)), Fraction(0))


def records(p):
    return tuple(j == 0 or p[j] > max(p[:j]) for j in range(len(p)))


def descents(p):
    return tuple(p[j] > p[j + 1] for j in range(len(p) - 1))


def claimed(n, q, i, j):
    # Position indices i,j are 1-based, with 1<=i<n and 1<=j<=n.
    if j == i:
        return ((q_number(i + 1, q) - 1 - q) /
                ((1 + q) * q_number(i, q) * q_number(i + 1, q)))
    if j == i + 1:
        return -q / ((1 + q) * q_number(i + 1, q))
    return Fraction(0)


def run_check(n, q):
    pairs = [(p, q**inversion_count(p)) for p in permutations(range(n))]
    total_weight = sum((w for _, w in pairs), Fraction(0))
    record_means = [Fraction(0) for _ in range(n)]
    descent_means = [Fraction(0) for _ in range(n - 1)]
    joint = [[Fraction(0) for _ in range(n)] for _ in range(n - 1)]
    for p, weight in pairs:
        rs = records(p)
        ds = descents(p)
        for j, flag in enumerate(rs):
            if flag:
                record_means[j] += weight
        for i, flag in enumerate(ds):
            if flag:
                descent_means[i] += weight
                for j, rec_flag in enumerate(rs):
                    if rec_flag:
                        joint[i][j] += weight
    record_means = [v / total_weight for v in record_means]
    descent_means = [v / total_weight for v in descent_means]
    total_from_matrix = Fraction(0)
    for i in range(n - 1):
        for j in range(n):
            observed = joint[i][j] / total_weight - descent_means[i] * record_means[j]
            expected = claimed(n, q, i + 1, j + 1)
            assert observed == expected, (n, q, i + 1, j + 1, observed, expected)
            total_from_matrix += observed
    total_expected = -(q / (1 + q)) * sum(
        (1 / (q_number(i, q) * q_number(i + 1, q)) for i in range(1, n)),
        Fraction(0))
    assert total_from_matrix == total_expected, (n, q, total_from_matrix, total_expected)
    assert total_expected < 0, (n, q, total_expected)
    if q == 1:
        assert total_expected == -Fraction(n - 1, 2 * n)


for n in range(2, 8):
    for q in (Fraction(1, 2), Fraction(1), Fraction(2)):
        run_check(n, q)
    print('EXACT_COVARIANCE_PASS', n)
print('ALL_RECORD_DESCENT_CHECKS_PASS')
