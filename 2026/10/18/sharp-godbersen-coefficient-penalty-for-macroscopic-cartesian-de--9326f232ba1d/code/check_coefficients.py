#!/usr/bin/env python3
"""Exact arithmetic checks of hypergeometric collision and mixed-volume coefficients.

The analytic limit and convex-body coefficient inequality require mathematical proof;
finite checks here test the combinatorial identities and numerical behavior only.
"""
from math import comb, pi, sqrt
from fractions import Fraction


def convolve(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return c


def simplex_product_coefficients(dims):
    coefficients = [1]
    for d in dims:
        coefficients = convolve(coefficients, [comb(d, k) ** 2 for k in range(d + 1)])
    return coefficients


def collision_direct(dims, j):
    """Independent enumeration of multivariate hypergeometric outcomes."""
    n = sum(dims)
    denominator = comb(n, j)
    total = 0
    def search(i, left, numerator):
        nonlocal total
        if i == len(dims):
            if left == 0:
                total += numerator * numerator
            return
        for k in range(max(0, left - sum(dims[i+1:])), min(dims[i], left)+1):
            search(i+1, left-k, numerator * comb(dims[i], k))
    search(0, j, 1)
    return Fraction(total, denominator * denominator)


def sharp_asymptotic_constant(alphas, beta):
    return 1 / ((4*pi*beta*(1-beta)) ** ((len(alphas)-1)/2) * sqrt(__import__('math').prod(alphas)))


def test_all():
    tally = 0
    for dims in ([2, 3], [3, 4, 2], [1, 1, 3], [2, 2, 2, 2], [4, 1]):
        coeffs = simplex_product_coefficients(dims)
        n = sum(dims)
        assert len(coeffs) == n+1
        assert sum(coeffs) == __import__('math').prod(comb(2*d, d) for d in dims)
        for j in range(n+1):
            assert Fraction(coeffs[j], comb(n, j)**2) == collision_direct(dims, j)
            assert coeffs[j] <= comb(n, j)**2
            tally += 1
    print('Exact independent hypergeometric and polynomial identity checks:', tally)
    # Planar triangle has F_2=[1,4,1] and centrally symmetric rectangle
    # has F_2=[1,2,1]; their product coefficients are bounded by F_2^2.
    triangle = [1, 4, 1]
    rectangle = [1, 2, 1]
    for k, x in enumerate(convolve(triangle, rectangle)):
        assert x <= convolve(triangle, triangle)[k]
    print('Planar triangle/rectangle factor inequality: passed')
    for m in [2,3]:
        beta = .5
        alphas = [1/m]*m
        expected = sharp_asymptotic_constant(alphas, beta)
        print('Block count', m, 'expected scaled limit', round(expected, 10))
        seq = [60, 120, 240, 480] if m == 2 else [60, 120, 240]
        results=[]
        for n in seq:
            dims = [n//m]*m
            j = n//2
            exact = Fraction(simplex_product_coefficients(dims)[j], comb(n, j)**2)
            scaled = float(exact)*n**((m-1)/2)
            results.append(scaled)
            print('  n', n, 'scaled=', f'{scaled:.10f}', 'ratio to limit=', f'{scaled/expected:.8f}')
        assert abs(results[-1]/expected-1)<0.02
    print('All checks passed')

if __name__ == '__main__':
    test_all()
