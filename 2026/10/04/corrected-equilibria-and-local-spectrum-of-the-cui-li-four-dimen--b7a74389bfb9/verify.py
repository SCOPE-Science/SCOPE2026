#!/usr/bin/env python3
from fractions import Fraction
import sympy as sp

a,b,c,d,e,m,k,u,lam = sp.symbols('a b c d e m k u lam', nonzero=True)
r2 = 2*a*b/e

# Elimination of the equilibrium equations: p'=0 gives v=-u; w'=0 gives
# w=-u^2/b; then u'=0 factors into exactly the zero branch and the
# nonzero branch u^2=2ab/e.
v_elim = -u
w_elim = -u**2/b
f1_elim = sp.factor(a*(v_elim-u) + e*v_elim*w_elim)
assert sp.factor(f1_elim - u*(-2*a + e*u**2/b)) == 0

v = -u
w = -2*a/e
p = u*(d*e-c*e-2*a)/(e*m)

# Equilibrium equations after imposing the nonzero branch relation u^2=2ab/e.
f1 = a*(v-u) + e*v*w
f2 = c*u + d*v - u*w + m*p
f3 = -b*w + u*v
f4 = -k*(u+v)
for expr in (f1,f2,f3,f4):
    q = sp.factor(expr.subs(u**2, r2))
    assert q == 0, q

J = sp.Matrix([
    [-a, a+e*w, e*v, 0],
    [c-w, d, -u, m],
    [v, u, -b, 0],
    [-k, -k, 0, 0],
])
chi = sp.factor((lam*sp.eye(4)-J).det().subs(u**2, r2))
expected = (
    lam**4 + (a+b-d)*lam**3
    + (k*m-a*b+a*c-a*d-b*d+2*a*(a+b)/e)*lam**2
    + (b*(3*a*c+a*d+k*m)+10*a*a*b/e)*lam
    - 4*a*b*k*m
)
assert sp.simplify(chi-expected) == 0

params = {a:15,b:43,c:1,d:16,e:5,m:5,k:2}
baseline = sp.Poly(sp.expand(expected.subs(params)), lam)
assert baseline.as_expr() == lam**4 + 42*lam**3 - 1200*lam**2 + 32035*lam - 25800

# Exact Routh first column for the baseline quartic.
A1 = Fraction(42)
A2 = Fraction(-1200)
A3 = Fraction(32035)
A4 = Fraction(-25800)
B1 = (A1*A2-A3)/A1
C1 = (B1*A3-A1*A4)/B1
assert B1 == Fraction(-82435,42)
assert C1 == Fraction(519058805,16487)
signs = [1, 1, -1, 1, -1]
assert sum(signs[i] != signs[i-1] for i in range(1,len(signs))) == 3

# The source's printed baseline fourth coordinate has magnitude about 260.210,
# while the corrected equilibrium has fourth coordinate (9/5)*sqrt(258).
corrected_p2 = sp.Rational(81,25)*258
assert sp.simplify(corrected_p2 - sp.Rational(20898,25)) == 0

print('VERIFY_OK')
