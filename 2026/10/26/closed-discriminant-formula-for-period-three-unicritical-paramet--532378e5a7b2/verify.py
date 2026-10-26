#!/usr/bin/env python3
"""Exact finite checks for the period-three unicritical discriminant formula.

Uses only the Python standard library. The general theorem is proved in RESULT.md;
these checks compare exact Sylvester determinants for small degrees.
"""
from math import comb


def coefficients_g(d):
    """Ascending coefficients of G_d(c) = 1 + c^(d-1)(c^(d-1)+1)^d."""
    m = d - 1
    degree = d * d - 1
    coeffs = [0] * (degree + 1)
    coeffs[0] = 1
    for j in range(d + 1):
        coeffs[m * (j + 1)] += comb(d, j)
    return coeffs


def bareiss_det(matrix):
    """Exact determinant by fraction-free Bareiss elimination."""
    a = [list(map(int, row)) for row in matrix]
    n = len(a)
    if n == 0:
        return 1
    sign = 1
    previous_pivot = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            aik = a[i][k]
            for j in range(k + 1, n):
                numerator = a[i][j] * pivot - aik * a[k][j]
                if numerator % previous_pivot:
                    raise ArithmeticError("Bareiss division was not exact")
                a[i][j] = numerator // previous_pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        previous_pivot = pivot
    return sign * a[n - 1][n - 1]


def resultant_with_derivative(coeffs):
    """Resultant Res(G,G') as a Sylvester determinant."""
    degree = len(coeffs) - 1
    f_desc = list(reversed(coeffs))
    derivative_asc = [i * coeffs[i] for i in range(1, len(coeffs))]
    g_desc = list(reversed(derivative_asc))
    derivative_degree = degree - 1
    size = degree + derivative_degree
    matrix = []
    for shift in range(derivative_degree):
        matrix.append([0] * shift + f_desc + [0] * (derivative_degree - 1 - shift))
    for shift in range(degree):
        matrix.append([0] * shift + g_desc + [0] * (degree - 1 - shift))
    if len(matrix) != size or any(len(row) != size for row in matrix):
        raise AssertionError("incorrect Sylvester matrix dimensions")
    return bareiss_det(matrix)


def closed_formula(d):
    degree = d * d - 1
    r = (d + 1) ** (d + 1) - d**d
    return (-1) ** (d + 1) * (d - 1) ** degree * r ** (d - 1)


def main():
    for d in range(2, 8):
        coeffs = coefficients_g(d)
        resultant = resultant_with_derivative(coeffs)
        degree = d * d - 1
        discriminant = (-1) ** (degree * (degree - 1) // 2) * resultant
        expected = closed_formula(d)
        if discriminant != expected:
            raise SystemExit(f"FAILED at d={d}")
        print(f"d={d}: exact discriminant agrees")
    print("All exact finite checks passed; these checks do not replace the proof.")


if __name__ == "__main__":
    main()
