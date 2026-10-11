#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import factorial


def det(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    total = 0
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in matrix[1:]]
        total += (-1) ** j * matrix[0][j] * det(minor)
    return total


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
checked = 0
for idx in product(range(3), repeat=6):
    a1, a2, b1, b2, c1, c2 = [basis[i] for i in idx]
    cols = [a1, a2, b1, b2, (0, 0, 0), (0, 0, 0)]
    low = [a1, a2, (0, 0, 0), (0, 0, 0), c1, c2]
    matrix = [[cols[j][i] for j in range(6)] for i in range(3)] + [[low[j][i] for j in range(6)] for i in range(3)]
    lhs = det(matrix)
    rhs = dot(cross(a1, a2), cross(cross(b1, b2), cross(c1, c2)))
    if lhs != rhs:
        raise AssertionError((idx, lhs, rhs))
    checked += 1

if checked != 3 ** 6:
    raise AssertionError(checked)

if Fraction(4 ** 6, factorial(6) * 512) != Fraction(1, 90):
    raise AssertionError('ball coefficient')
if Fraction(1, 90) / Fraction(16, 9) != Fraction(1, 160):
    raise AssertionError('normalized ellipsoid coefficient')
if Fraction(1, 160) / Fraction(3, 10) != Fraction(1, 48):
    raise AssertionError('Janson ratio')

print('VERIFY_OK')
