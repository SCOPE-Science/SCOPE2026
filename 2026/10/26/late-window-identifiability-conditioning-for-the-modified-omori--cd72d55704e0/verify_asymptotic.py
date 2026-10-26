#!/usr/bin/env python3
"""Symbolically check the late-window modified-Omori log-ratio expansion."""
import sympy as sp

p, x = sp.symbols("p x", positive=True)  # x = 1/u
j = sp.symbols("j", integer=True, nonnegative=True)

# Moments of t on the unit interval [j,j+1].
m1 = j + sp.Rational(1, 2)
m2 = j**2 + j + sp.Rational(1, 3)
m3 = j**3 + sp.Rational(3, 2) * j**2 + j + sp.Rational(1, 4)
A1 = -p * m1
A2 = p * (p + 1) * m2 / 2
A3 = -p * (p + 1) * (p + 2) * m3 / 6
L2 = sp.factor(A2 - A1**2 / 2)
L3 = sp.factor(A3 - A1 * A2 + A1**3 / 3)

def log_bin(j_value):
    mm1 = m1.subs(j, j_value)
    ll2 = L2.subs(j, j_value)
    ll3 = L3.subs(j, j_value)
    return sp.expand(-p * mm1 * x + ll2 * x**2 + ll3 * x**3)

s0 = sp.factor(log_bin(1) - log_bin(0))
s1 = sp.factor(log_bin(2) - log_bin(1))
expected0 = -p*x + p*x**2 - p*(p+14)*x**3/12
expected1 = -p*x + 2*p*x**2 - p*(p+50)*x**3/12
assert sp.simplify(s0 - expected0) == 0
assert sp.simplify(s1 - expected1) == 0

det_px = sp.factor(sp.diff(s0, p)*sp.diff(s1, x) - sp.diff(s0, x)*sp.diff(s1, p))
# Since x=1/u, d x/d u=-x^2. The limit is the leading coefficient in u.
det_pu = sp.factor(det_px * (-x**2))
assert sp.simplify(sp.limit(det_pu / x**4, x, 0) - p) == 0
print("PASS: log-ratio coefficients and leading Jacobian coefficient verified")
