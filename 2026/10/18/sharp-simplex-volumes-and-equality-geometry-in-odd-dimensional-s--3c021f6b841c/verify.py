#!/usr/bin/env python3
"""Reproduce exact rational identities for odd-dimensional spherical slabs.

Standard library only. These finite cases supplement (and do not replace) the
all-dimensional analytic proof in RESULT.md.
"""
from fractions import Fraction as Q
from math import factorial, comb


def determinant(matrix):
    a = [list(row) for row in matrix]
    n = len(a)
    result = Q(1)
    for col in range(n):
        pivot = next((i for i in range(col, n) if a[i][col]), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            result = -result
        v = a[col][col]
        result *= v
        for i in range(col + 1, n):
            m = a[i][col] / v
            for j in range(col + 1, n):
                a[i][j] -= m * a[col][j]
            a[i][col] = Q(0)
    return result


def volume_primitive(k, t):
    return sum(((-1) ** j) * comb(k, j) * t ** (2 * j + 1) / (2 * j + 1)
               for j in range(k + 1))


def check(d, t):
    assert d >= 3 and d % 2 == 1 and Q(0) < t * t < Q(1, d)
    k = (d - 1) // 2
    a2 = Q(d, d - 1) * (1 - t * t)
    b2 = d * t * t
    assert a2 - 1 == Q(1, d - 1) * (1 - d * t * t)
    assert Q(1) - a2 / b2 == -(1 - d * t * t) / ((d - 1) * t * t)
    assert (1 - t * t) / a2 == Q(d - 1, d)
    assert t * t / b2 == Q(1, d)
    n = d + 1
    signs = [1] * (k + 1) + [-1] * (k + 1)
    assert len(signs) == n
    r2 = 1 - t * t

    def dot(i, j):
        if i == j:
            return Q(1)
        if signs[i] != signs[j]:
            return -(t * t)
        return -r2 / k + t * t

    for i in range(n):
        for j in range(n):
            horizontal = (Q(0) if signs[i] != signs[j]
                          else (r2 if i == j else -r2 / k))
            value = horizontal / a2 + signs[i] * signs[j] * t * t / b2
            assert value == (Q(1) if i == j else -Q(1, d))
    gram = [[dot(i + 1, j + 1) - dot(i + 1, 0) - dot(0, j + 1) + 1
             for j in range(d)] for i in range(d)]
    volume_squared = Q((d + 1) ** (d + 1),
                       factorial(d) ** 2 * (d - 1) ** (d - 1))
    volume_squared *= t * t * (1 - t * t) ** (d - 1)
    assert determinant(gram) == factorial(d) ** 2 * volume_squared
    return 1


count = 0
for d in (3, 5, 7, 9):
    for denom in (d + 1, 2 * (d + 1), 3 * (d + 1)):
        count += check(d, Q(1, denom))

for d in (3, 5, 7, 9, 11, 13):
    t2 = Q(1, d)
    assert Q(d, d - 1) * (1 - t2) == 1
    assert d * t2 == 1

# Exact rational sample checks of the strictly decreasing volume-ratio factor
# t (1-t^2)^k / integral_0^t (1-s^2)^k ds before the transition.
for d in (3, 5, 7, 9):
    k = (d - 1) // 2
    ts = [Q(j, 24 * d) for j in range(1, 12)]
    vals = [t * (1 - t * t) ** k / volume_primitive(k, t) for t in ts]
    assert all(x > y for x, y in zip(vals, vals[1:]))

print('VERIFY_OK exact_odd_dimension_cases=12 transition_identities=6 monotonicity_samples=4')
