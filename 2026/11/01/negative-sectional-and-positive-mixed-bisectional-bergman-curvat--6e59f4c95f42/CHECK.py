#!/usr/bin/env python3
"""Exact rational jet checks for Bergman curvature on intersected disk bundles.

This finite checker tests algebraic identities in sample rational dimensions and
parameters; the theorem for all positive parameters is proved separately.
"""
from fractions import Fraction as Q
from math import factorial
from itertools import product


def kernel_coefficient(alpha, weights):
    """Coefficient of the Bergman kernel, with its global pi^(-n) omitted."""
    n = len(alpha)
    t = Q(1) + sum(weights[j - 1] * (alpha[j] + 1) for j in range(1, n))
    out = Q(1)
    for j in range(1, n):
        out *= alpha[j] + 1
    for k in range(alpha[0] + 1):
        out *= t + k
    return out / factorial(alpha[0])


def basis(n, j, multiplicity=1):
    a = [0] * n
    a[j] = multiplicity
    return a


def check(weights):
    n = len(weights) + 1
    T = Q(1) + sum(weights)
    c0 = kernel_coefficient([0] * n, weights)
    assert c0 == T
    g = [kernel_coefficient(basis(n, j), weights) / c0 for j in range(n)]
    assert g[0] == T + 1
    for j in range(1, n):
        assert g[j] == 2 * (T + weights[j - 1]) / T

    R = [[Q(0)] * n for _ in range(n)]
    for j in range(n):
        for k in range(n):
            alpha = [0] * n
            alpha[j] += 1
            alpha[k] += 1
            c2 = kernel_coefficient(alpha, weights) / c0
            R[j][k] = -4 * (c2 - g[j] ** 2 / 2) if j == k else -(c2 - g[j] * g[k])
    assert R[0][0] == -2 * (T + 1)
    for j in range(1, n):
        u = weights[j - 1]
        assert R[0][j] == R[j][0] == -2 * u * (T + u) / T
        assert R[j][j] == -4 * (T * T + 2 * T * u - 2 * u * u) / (T * T)
        for k in range(j + 1, n):
            v = weights[k - 1]
            assert R[j][k] == R[k][j] == 4 * u * v / (T * T)
            assert R[j][k] / (g[j] * g[k]) == u * v / ((T + u) * (T + v))
            assert R[j][k] > 0

    # R is the coordinate-bisectional tensor; Kähler symmetry supplies four
    # equal mixed contributions in the sectional-curvature quartic form.
    for x in product([Q(0), Q(1, 3), Q(1), Q(3)], repeat=n):
        if not any(x):
            continue
        h = sum(R[j][j] * x[j] * x[j] for j in range(n))
        h += 4 * sum(R[j][k] * x[j] * x[k] for j in range(n) for k in range(j + 1, n))
        assert h < 0
    return 1


if __name__ == '__main__':
    cases = [
        [Q(1), Q(1)],
        [Q(1, 2), Q(2)],
        [Q(1, 7), Q(9, 2)],
        [Q(1, 2), Q(2), Q(3, 5)],
        [Q(1), Q(2), Q(3), Q(4)],
    ]
    count = sum(check(case) for case in cases)
    print(f'PASS: exact rational kernel-jet and curvature identities in {count} parameter cases')
