"""Symbolic verification of the scalar critical expansion for u' = sin(u) - u."""
import sympy as sp

u = sp.symbols("u")
r = sp.sin(u) - u
r_series = sp.series(r, u, 0, 10)
wprime_series = sp.series(-2 * r / u**3, u, 0, 8)

print("sin(u)-u =", r_series)
print("d(u^-2)/dt =", wprime_series)

expected_r = -u**3/sp.Integer(6) + u**5/sp.Integer(120) - u**7/sp.Integer(5040) + u**9/sp.Integer(362880)
expected_w = sp.Rational(1, 3) - u**2/sp.Integer(60) + u**4/sp.Integer(2520) - u**6/sp.Integer(181440)

assert sp.expand(r_series.removeO() - expected_r) == 0
assert sp.expand(wprime_series.removeO() - expected_w) == 0
print("verified: all displayed coefficients have zero symbolic residual")
