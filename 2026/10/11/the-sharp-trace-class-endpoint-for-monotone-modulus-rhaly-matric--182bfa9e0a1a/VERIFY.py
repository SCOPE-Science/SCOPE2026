#!/usr/bin/env python3
"""Finite checks for the triangular-block identities in a Rhaly trace-norm theorem.

No dependencies beyond Python's standard library. These checks are finite only.
"""
import math
from fractions import Fraction


def product(a, b):
    rows, mid, cols = len(a), len(b), len(b[0])
    assert len(a[0]) == mid
    return [[sum(a[i][k] * b[k][j] for k in range(mid))
             for j in range(cols)] for i in range(rows)]


def transpose(a):
    return [list(z) for z in zip(*a)]


for n in range(1, 33):
    lower = [[int(j <= i) for j in range(n)] for i in range(n)]
    difference = [[int(i == j) - int(i == j + 1)
                   for j in range(n)] for i in range(n)]
    identity = [[int(i == j) for j in range(n)] for i in range(n)]
    assert product(difference, lower) == identity
    inverse_gram = product(difference, transpose(difference))
    expected = [[(1 if i == 0 else 2) if i == j
                 else (-1 if abs(i - j) == 1 else 0)
                 for j in range(n)] for i in range(n)]
    assert inverse_gram == expected
    singular_sum = 0.0
    for k in range(1, n + 1):
        theta = (2 * k - 1) * math.pi / (2 * n + 1)
        eigenvalue = 4 * math.sin(theta / 2) ** 2
        v = [math.cos((i + 0.5) * theta) for i in range(n)]
        for i in range(n):
            lhs = sum(inverse_gram[i][j] * v[j] for j in range(n))
            rhs = eigenvalue * v[i]
            assert abs(lhs - rhs) < 2e-12 * (1 + abs(rhs))
        singular_sum += 1 / math.sqrt(eigenvalue)
    harmonic_odd = sum(Fraction(1, 2 * k - 1) for k in range(1, n + 1))
    low = (2 * n + 1) * float(harmonic_odd) / math.pi
    high = (2 * n + 1) * float(harmonic_odd) / 2
    assert low - 1e-10 <= singular_sum <= high + 1e-10

# A finite matrix must equal its row-zero, dyadic internal, and rectangular pieces.
for size in (2, 4, 8, 16, 32):
    a = [Fraction(1, i + 2) for i in range(size)]
    matrix = [[a[i] if j <= i else Fraction(0)
               for j in range(size)] for i in range(size)]
    decomposition = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    decomposition[0][0] = a[0]
    start = 1
    while start < size:
        end = min(2 * start, size)
        for i in range(start, end):
            for j in range(start):
                decomposition[i][j] += a[i]
            for j in range(start, i + 1):
                decomposition[i][j] += a[i]
        start *= 2
    assert matrix == decomposition

print('RHALY_TRACE_ENDPOINT_FINITE_IDENTITIES_OK')
