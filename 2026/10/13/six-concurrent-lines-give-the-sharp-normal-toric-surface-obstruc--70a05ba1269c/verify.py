#!/usr/bin/env python3
"""Exact arithmetic witness that six projective directions impose six conic conditions."""
from fractions import Fraction

DIRECTIONS = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 1),
    (1, 2, 3),
    (1, 3, 2),
)


def conic_row(p):
    x, y, z = p
    return [Fraction(a) for a in (x*x, y*y, z*z, x*y, x*z, y*z)]


def determinant(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    det_sign = 1
    for i in range(n):
        pivot = next((r for r in range(i, n) if a[r][i] != 0), None)
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            a[pivot], a[i] = a[i], a[pivot]
            det_sign = -det_sign
        pivot_value = a[i][i]
        for r in range(i + 1, n):
            scale = a[r][i] / pivot_value
            for c in range(i + 1, n):
                a[r][c] -= scale * a[i][c]
            a[r][i] = Fraction(0)
    result = Fraction(det_sign)
    for i in range(n):
        result *= a[i][i]
    return result


if __name__ == "__main__":
    assert len(set(DIRECTIONS)) == 6
    matrix = [conic_row(p) for p in DIRECTIONS]
    result = determinant(matrix)
    assert result == 7, result
    print("CONIC_EVALUATION_DETERMINANT=7")
    print("CONIC_EVALUATION_RANK=6")
    print("VERIFY_OK")
