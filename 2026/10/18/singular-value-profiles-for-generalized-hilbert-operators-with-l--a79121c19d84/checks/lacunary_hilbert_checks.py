#!/usr/bin/env python3
"""Exact finite sanity checks for an analytic Cauchy-kernel factorization."""
from fractions import Fraction
from math import isqrt

def positive_leading_pivots(matrix):
    data = [[Fraction(x) for x in row] for row in matrix]
    count = len(data)
    for i in range(count):
        pivot = data[i][i]
        assert pivot > 0
        for j in range(i + 1, count):
            multiplier = data[j][i] / pivot
            for k in range(i, count):
                data[j][k] -= multiplier * data[i][k]
    return True

def main():
    degrees = (1, 4, 16, 64)
    coefficients = [Fraction(1, j + 2) for j in range(len(degrees))]
    cutoff = 32
    for j, degree in enumerate(degrees):
        root = isqrt(degree)
        assert root * root == degree
        for k in range(cutoff):
            from_integral = Fraction(degree, degree + k) * coefficients[j]
            diagonal_times_analysis = (root * coefficients[j]) * Fraction(root, degree + k)
            assert from_integral == diagonal_times_analysis
    gram = [[sum((Fraction(isqrt(n) * isqrt(m), (n+k)*(m+k)) for k in range(cutoff)), Fraction(0))
             for m in degrees] for n in degrees]
    assert all(gram[i][j] == gram[j][i] for i in range(4) for j in range(4))
    assert positive_leading_pivots(gram)
    print("LACUNARY_HILBERT_SINGULAR_PROFILE_FINITE_IDENTITIES_OK")

if __name__ == "__main__":
    main()
