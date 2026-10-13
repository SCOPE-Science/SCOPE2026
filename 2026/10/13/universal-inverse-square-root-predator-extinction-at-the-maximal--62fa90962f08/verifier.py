#!/usr/bin/env python3
"""Exact algebraic checks for the Holling-IV critical extinction theorem.

Dependency: SymPy. These checks validate symbolic premises and a witness;
the convergence and asymptotic arguments are proved in RESULT.md.
"""
import sympy as s

x, b, c, xi, beta, gamma, y, u = s.symbols(
    'x b c xi beta gamma y u', positive=True)
Q = 1 + b * x**2
f = x / (c * Q + x)
g = (x + xi * Q) / (c * Q + x)
r = s.sqrt(b)
K = 1 / r
m = (1 + 2 * xi * r) / (1 + 2 * c * r)
F = 1 / (1 + 2 * c * r)
G = 2 * (c - xi) * b**s.Rational(3, 2) / (1 + 2 * c * r)**2
agap = beta * (m - g)
closed_gap = beta * (c - xi) * b * (x - K)**2 / (
    (1 + 2 * c * r) * (c * Q + x))

assert s.simplify(agap - closed_gap) == 0
assert s.simplify(f.subs(x, K) - F) == 0
assert s.simplify(g.subs(x, K) - m) == 0
assert s.simplify(s.diff(g, x).subs(x, K)) == 0
assert s.simplify(s.diff(g, x, 2).subs(x, K) + G) == 0
assert s.simplify(s.limit(agap / (x - K)**2, x, K) - beta*G/2) == 0

# The exact quotient evolution after setting u=x-K and w=u/y.
xpr = x*(1-x/K) - f*y
ypr = -agap*y
wpr = s.diff((x-K)/y, x)*xpr + s.diff((x-K)/y, y)*ypr
predicted = -(1+(x-K)/K-agap)*(x-K)/y-f
assert s.simplify(wpr-predicted) == 0

# An admissible exact-rational parameter witness.
v = {b:s.Integer(1), c:s.Integer(2), xi:s.Integer(1), beta:s.Integer(5)}
assert s.simplify(m.subs(v)-s.Rational(3,5)) == 0
assert s.simplify(F.subs(v)-s.Rational(1,5)) == 0
assert s.simplify(G.subs(v)-s.Rational(2,25)) == 0
assert s.simplify(1/(F*s.sqrt(beta*G)).subs(v)-25/s.sqrt(10)) == 0
assert s.simplify(1/s.sqrt(beta*G).subs(v)-5/s.sqrt(10)) == 0

print('VERIFY_OK')
