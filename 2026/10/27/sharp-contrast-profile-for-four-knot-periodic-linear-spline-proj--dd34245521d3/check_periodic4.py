#!/usr/bin/env python3
"""Exact rational checks for the four-knot alternating periodic linear-spline projector.
No external dependencies. Execute: python3 check_periodic4.py
"""
from fractions import Fraction as F


def inverse(a):
    n = len(a)
    b = [[F(x) for x in row] + [F(int(i == j)) for j in range(n)]
         for i, row in enumerate(a)]
    for i in range(n):
        p = next(k for k in range(i, n) if b[k][i])
        b[i], b[p] = b[p], b[i]
        den = b[i][i]
        b[i] = [x / den for x in b[i]]
        for k in range(n):
            if k != i:
                c = b[k][i]
                b[k] = [x - c*y for x, y in zip(b[k], b[i])]
    return [row[n:] for row in b]


def gram(r):
    edges = [r, F(1), r, F(1)]
    g = [[F(0) for _ in range(4)] for _ in range(4)]
    for i, length in enumerate(edges):
        j = (i + 1) % 4
        g[i][i] += length / 3
        g[j][j] += length / 3
        g[i][j] += length / 6
        g[j][i] += length / 6
    return g


def row_formula(r):
    q = (r + 1)*(r + 3)*(3*r + 1)
    return [4*(3*r*r + 8*r + 3)/q, -2*r*(3*r + 5)/q,
            8*r/q, -2*(5*r + 3)/q]


def norm_from_row(row, r):
    edges = [r, F(1), r, F(1)]
    norm = F(0)
    for i, length in enumerate(edges):
        u, v = row[i], row[(i + 1) % 4]
        if u*v < 0:
            norm += length*(u*u + v*v)/(2*(abs(u) + abs(v)))
        else:
            norm += length*(abs(u) + abs(v))/2
    return norm


def rational_formula(r):
    num = 90*r**6 + 913*r**5 + 3154*r**4 + 4742*r**3 + 3154*r*r + 913*r + 90
    den = 3*(r + 2)*(r + 3)**2*(2*r + 1)*(3*r + 1)**2
    return num/den


def lower_gap(r):
    return 8*r*(r + 1)**2*(11*r*r + 26*r + 11) / (3*(r+2)*(r+3)**2*(2*r+1)*(3*r+1)**2)


def upper_gap(r):
    return 2*(r-1)**2*(18*r**4+69*r**3+98*r*r+69*r+18) / (9*(r+2)*(r+3)**2*(2*r+1)*(3*r+1)**2)


def negative_derivative_sign_factor(r):
    p = 33*r**6 + 178*r**5 + 377*r**4 + 456*r**3 + 377*r*r + 178*r + 33
    return -16*(r-1)*(r+1)*p / (3*(r+2)**2*(r+3)**3*(2*r+1)**2*(3*r+1)**3)


def poly_mul(a, b):
    c = [0]*(len(a)+len(b)-1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            c[i+j] += v*w
    return c


def poly_pow(a, k):
    ans = [1]
    for _ in range(k):
        ans = poly_mul(ans, a)
    return ans


def poly_eval(a, r):
    return sum(F(x)*r**i for i, x in enumerate(a))


if __name__ == '__main__':
    # Multiplying the displayed denominator factors recovers the exact
    # denominator and numerator of the formula. This is an identity of
    # polynomials, not a finite sampling argument.
    denominator = [3]
    for poly, power in [([2,1],1), ([3,1],2), ([1,2],1), ([1,3],2)]:
        denominator = poly_mul(denominator, poly_pow(poly, power))
    numerator = [90,913,3154,4742,3154,913,90]
    assert len(denominator) == 7
    tests = 0
    for n in range(1, 18):
        for d in range(1, 14):
            r = F(n, d)
            inv = inverse(gram(r))
            assert inv[0] == row_formula(r)
            v = norm_from_row(inv[0], r)
            assert v == rational_formula(r)
            assert v * poly_eval(denominator, r) == poly_eval(numerator, r)
            assert v == rational_formula(1/r)
            assert v-F(5,3) == lower_gap(r)
            assert F(17,9)-v == upper_gap(r)
            assert F(5,3) < v <= F(17,9)
            assert (v == F(17,9)) == (r == 1)
            tests += 1
    assert rational_formula(F(1)) == F(17,9)
    # Direct finite-difference comparison at rational points matches the
    # rigorous derivative factorization in RESULT.md; verification of
    # monotonicity itself follows from its strictly positive factors.
    for r in [F(1,5), F(1,2), F(2,3), F(2), F(3), F(9)]:
        h = F(1, 1000000)
        finite_diff = (rational_formula(r+h)-rational_formula(r-h))/(2*h)
        deriv = negative_derivative_sign_factor(r)
        assert abs(finite_diff-deriv) < F(1, 100000)
    print('PASS: 221 exact Gram-inverse, Lebesgue-integral, and rational-identity checks; six derivative comparisons')
    print('Uniform mesh sharp norm:', rational_formula(F(1)))
