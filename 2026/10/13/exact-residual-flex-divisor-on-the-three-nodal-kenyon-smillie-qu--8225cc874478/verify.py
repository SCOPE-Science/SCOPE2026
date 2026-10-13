#!/usr/bin/env python3
"""Exact symbolic checks for the t=1 Kenyon--Smillie quartic flex divisor."""
import sympy as sp

x, y = sp.symbols('x y')
X, Y, Z = sp.symbols('X Y Z')

G = (
    X**4 - 3*X**3*Y + 6*X**3*Z - 3*X**2*Y**2 - 6*X**2*Y*Z
    + 6*X**2*Z**2 + 4*X*Y**3 - 6*X*Y**2*Z - 6*X*Y*Z**2
    + X*Z**3 + 3*Y**4 + 3*Y**3*Z
)
F = sp.expand(X**4 + G)
f = sp.expand(F.subs({X: x, Y: y, Z: 1}))

vars3 = (X, Y, Z)
H = sp.Matrix([[sp.diff(F, a, b) for b in vars3] for a in vars3]).det()
Hn = sp.expand(H / 162)
h = sp.expand(Hn.subs({X: x, Y: y, Z: 1}))

n = x**3 - 3*x + 1
q = 106*x**3 + 3*x**2 - 6*x - 2
expected_res = 729*x**3*n**6*q
res = sp.factor(sp.resultant(f, h, y))
assert sp.expand(res - expected_res) == 0

# There is no quartic--Hessian intersection at infinity.
F_inf = sp.expand(F.subs(Z, 0).subs(Y, 1))
H_inf = sp.expand(Hn.subs(Z, 0).subs(Y, 1))
assert sp.resultant(F_inf, H_inf, X) == 77274
assert F.subs({X: 1, Y: 0, Z: 0}) != 0

# The residual degree-three flex divisor has the claimed exact coordinates.
gb = sp.groebner([f, h, q], y, x, order='lex')
expected_gb = sp.groebner(
    [106*x**2 + 23*x + 19*y + 3, q], y, x, order='lex'
)
assert gb == expected_gb

# The known singular locus consists of the three roots of n, with y=1-x-x^2.
fx, fy = sp.diff(f, x), sp.diff(f, y)
gbs = sp.groebner([f, fx, fy], y, x, order='lex')
assert any(sp.expand(p.as_expr() - (x**2 + x + y - 1)) == 0 for p in gbs.polys)
assert sp.factor(sp.resultant(x**2 + x + y - 1, n, x)) != 0
assert sp.discriminant(n, x) != 0

# The two x=0 smooth flexes have tangent contact orders three and four.
assert fx.subs({x: 0, y: 0}) == 1 and fy.subs({x: 0, y: 0}) == 0
assert sp.factor(f.subs(x, 0)) == 3*y**3*(y + 1)
u = sp.symbols('u')
assert fx.subs({x: 0, y: -1}) == -3 and fy.subs({x: 0, y: -1}) == -3
assert sp.expand(f.subs({x: u, y: -1-u}) - u**4) == 0

# Arithmetic of the residual cubic.
fl = sp.Poly(q, x, modulus=5).factor_list()[1]
assert len(fl) == 1 and fl[0][0].degree() == 3 and fl[0][1] == 1
assert sp.discriminant(q, x) == -(1026**2)
assert sp.gcd(q, sp.diff(q, x)) == 1
assert sp.gcd(q, n) == 1
assert q.subs(x, 0) != 0

print('VERIFY_OK')
