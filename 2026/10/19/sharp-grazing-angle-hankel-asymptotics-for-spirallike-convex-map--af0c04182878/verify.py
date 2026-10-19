#!/usr/bin/env python3
"""Exact-arithmetic checks of the algebraic identities in the accompanying proof.

This program tests finite algebraic reductions. The universal analytical
inequalities and the extremal argument are proved in RESULT.md.
"""
from fractions import Fraction as Q
from math import comb

# Bernstein coefficient identity for the single polynomial case inequality.
coefficients = [Q(2), Q(17,10), Q(61,45), Q(119,120), Q(67,105),
                Q(83,252), Q(11,105), Q(1,120), Q(4,45),
                Q(2,5), Q(1)]
assert all(c > 0 for c in coefficients)
# Convert the degree-10 Bernstein basis into monomial coefficients.
poly = [Q(0) for _ in range(11)]
for k, ck in enumerate(coefficients):
    for h in range(11-k):
        poly[k+h] += ck * comb(10,k) * comb(10-k,h) * (-1)**h
assert poly == [Q(2), Q(-3), Q(-2), Q(3), Q(1)] + [Q(0)]*6

# The first three Herglotz moments of the explicit two-point extremizer.
x2 = Q(1,8)
m2 = 2*x2-1
# m1*m3 = (4*x^2-3)*x^2, valid even though x is irrational.
m1m3 = (4*x2-3)*x2
phi = 3*m1m3-2*m2*m2
assert m2 == Q(-3,4)
assert phi == Q(-33,16)
assert abs(phi)/18 == Q(11,96)

# Critical transition polynomial at the maximizer t=1/8.
def low_branch(t):
    return Q(2)+t-4*t*t
assert low_branch(Q(1,8)) == Q(33,16)
assert Q(1,8) < Q(1,3)

# Expansion coefficient formula checked by finite exact rational specializations.
# f'(z)=exp(t*(c1*z+c2*z*z/2+c3*z*z*z/3+...)).
for t in [Q(-3,7), Q(1,3), Q(1)]:
    for c1 in [Q(-2), Q(1), Q(2)]:
        for c2 in [Q(-1), Q(2), Q(3)]:
            c3 = Q(1) + c1 - 2*c2
            a2 = t*c1/2
            a3 = t*c2/6+t*t*c1*c1/6
            a4 = t*c3/12+t*t*c1*c2/8+t**3*c1**3/24
            direct = a2*a4-a3*a3
            factored = t*t*(c1*c3/24-c2*c2/36+t*c1*c1*c2/144-t*t*c1**4/144)
            assert direct == factored
print('PASS: positive Bernstein certificate, extremal Herglotz moments, 27 exact coefficient identities.')
