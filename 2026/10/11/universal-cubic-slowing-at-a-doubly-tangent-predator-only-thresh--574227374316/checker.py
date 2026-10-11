"""Independent algebraic identities for a doubly tangent Leslie--Gower critical point.

Reproduction: python checker.py (SymPy required).
"""
from fractions import Fraction
import sympy as S

x, a, n, k, b, d1, d2, s = S.symbols('x a n k b d1 d2 s', positive=True)
u = 1 + k*a
r = u*(d1 + a*b)
q = (n + (d2 + r*k*n/u**2)/b)/a
G = r/(u+k*n*x) - d1 - d2*x - b*(a+n*x)/(1+q*x)
P = d1*k*n*q + d2*(u*q + k*n) + b*k*n*n
Q = d2*k*n*q
assert S.cancel(G + x*x*(P+Q*x)/((u+k*n*x)*(1+q*x))) == 0
assert S.cancel(S.limit(G/x**2, x, 0) + P/u) == 0

# A completely rational strictly-positive realization.
parameters = {a:S.Integer(1), n:S.Integer(1), k:S.Integer(1),
              b:S.Integer(1), d1:S.Integer(1), d2:S.Integer(1),
              s:S.Integer(1)}
assert r.subs(parameters) == 4
assert q.subs(parameters) == 3
assert P.subs(parameters) == 11
assert Q.subs(parameters) == 3
assert S.cancel(G.subs(parameters) + x*x*(11+3*x)/((2+x)*(1+3*x))) == 0
assert S.simplify((u/(2*P)).subs(parameters)) == S.Rational(1, 11)
# Stable-fibre leading nonlinear balance: z'= -s z - n x', x'=-(P/u)x^3.
assert S.cancel((n*P/(s*u))*s - n*P/u) == 0
print('CHECK_OK: exact cubic, positive coefficients, rational witness, critical amplitude')
