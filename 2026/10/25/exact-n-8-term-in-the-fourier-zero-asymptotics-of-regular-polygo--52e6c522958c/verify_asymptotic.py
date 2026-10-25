#!/usr/bin/env python3
"""Exact rational checks for the radial-moment coefficients in RESULT.md.
Uses only the Python standard library; no numerical quadrature is involved.
"""
from fractions import Fraction as F


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def integrate_minus1_1(poly):
    total = F(0)
    for k, coefficient in enumerate(poly):
        if k % 2 == 0:
            total += coefficient * F(2, k + 1)
    return total


# g0 = (3*x^2 - 1)/24 and g1 = (25*x^4 - 10*x^2 - 3)/1920.
g0 = [F(-1, 24), F(0), F(3, 24)]
g1 = [F(-3, 1920), F(0), F(-10, 1920), F(0), F(25, 1920)]

moment3_leading = integrate_minus1_1(mul(mul(g0, g0), g0))
moment3_next = 3 * integrate_minus1_1(mul(mul(g0, g0), g1))
moment4_leading = integrate_minus1_1(mul(mul(mul(g0, g0), g0), g0))
coefficient_n6 = moment3_leading / 12
coefficient_n8 = moment3_next / 12 + moment4_leading / 24

assert moment3_leading == F(1, 15120), moment3_leading
assert moment3_next == F(13, 1209600), moment3_next
assert moment4_leading == F(1, 120960), moment4_leading
assert coefficient_n6 == F(1, 181440), coefficient_n6
assert coefficient_n8 == F(1, 806400), coefficient_n8

print("integral G0^3:", moment3_leading)
print("3 integral G0^2 G1:", moment3_next)
print("integral G0^4:", moment4_leading)
print("coefficient of j^3*pi^6/n^6:", coefficient_n6)
print("coefficient of j^3*pi^8/n^8:", coefficient_n8)
print("EXACT_RATIONAL_CHECKS_OK")
