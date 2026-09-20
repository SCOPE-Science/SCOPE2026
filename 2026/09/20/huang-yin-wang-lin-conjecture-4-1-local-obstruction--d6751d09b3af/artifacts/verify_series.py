#!/usr/bin/env python3
"""Symbolic check of the small-x coefficients in the published theorem."""
import sympy as sp

p, t = sp.symbols("p t", positive=True)
c1, c2, c3 = sp.symbols("c1 c2 c3")

a = 1 / (p * (p + 1))
b = (p + 1) / (2 * p**2 * (2 * p + 1))
c = (p + 1) * (2 * p + 1) / (6 * p**3 * (3 * p + 1))

w = 1 + c1*t + c2*t**2 + c3*t**3

def invert(sign):
    expr = sp.series(
        w + sign*a*t*w**(p+1) + b*t**2*w**(2*p+1)
          + sign*c*t**3*w**(3*p+1),
        t, 0, 4
    ).removeO().expand()
    s1 = sp.solve(sp.Eq(expr.coeff(t, 1), 0), c1)[0]
    s2 = sp.solve(sp.Eq(expr.coeff(t, 2).subs(c1, s1), 0), c2)[0]
    s3 = sp.solve(
        sp.Eq(expr.coeff(t, 3).subs({c1: s1, c2: s2}), 0), c3
    )[0]
    return tuple(map(sp.factor, (s1, s2, s3)))

s1, s2, s3 = invert(1)
h1, h2, h3 = invert(-1)

sin_ratio = 1 + s1*t + s2*t**2 + s3*t**3
sinh_ratio = 1 + h1*t + h2*t**2 + h3*t**3

N = sp.series(-sp.log(sin_ratio), t, 0, 4).removeO()
D = sp.series(
    sp.log((1 + t*sinh_ratio**p)**(1/p)), t, 0, 4
).removeO()
F = sp.series(N/D, t, 0, 3).removeO()

expected_c1 = (3*p**2 - 2*p - 2) / (2*(p+1)**2*(2*p+1))
expected_c2 = (
    (p-1)*(11*p**3 - 17*p**2 - 24*p - 6)
    / (12*(p+1)**3*(2*p+1)*(3*p+1))
)

assert sp.simplify(F.coeff(t, 0) - 1/(p+1)) == 0
assert sp.simplify(F.coeff(t, 1) - expected_c1) == 0
assert sp.simplify(F.coeff(t, 2) - expected_c2) == 0
assert sp.simplify(expected_c1.subs(p, sp.Rational(6, 5)) + sp.Rational(5, 2057)) == 0

p0 = (1 + sp.sqrt(7))/3
assert sp.simplify(expected_c1.subs(p, p0)) == 0
endpoint = sp.simplify(expected_c2.subs(p, p0))
assert sp.simplify(endpoint - (80*sp.sqrt(7) - 212)/81) == 0
assert endpoint.evalf() < 0

print("symbolic series identities verified")
print("p0 =", sp.N(p0, 16))
print("endpoint x^(2p0) coefficient =", sp.N(endpoint, 16))
