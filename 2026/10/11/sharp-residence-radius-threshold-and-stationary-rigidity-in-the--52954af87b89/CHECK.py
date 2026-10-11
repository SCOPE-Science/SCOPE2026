#!/usr/bin/env python3
"""Exact algebraic checks for the Sprott-N residence and stationary-moment theorem."""
import sympy as sp
x, y, z, a, b, R, T, K, L, D, C, v = sp.symbols('x y z a b R T K L D C v', real=True)
F = sp.Matrix([-a*y, x+z*z, 1+y-b*z])
H=z+x/a
assert sp.simplify(sp.Matrix([sp.diff(H,t) for t in (x,y,z)]).dot(F)-(1-b*z))==0
xe,ye,ze=-b**(-2),sp.Integer(0),b**(-1)
assert [sp.factor(t.subs({x:xe,y:ye,z:ze})) for t in F] == [0,0,0]
assert sp.factor(xe**2+ye**2+ze**2-(b**(-4)+b**(-2)))==0
assert sp.expand((L+v)**2+(L+v) -(L**2+L+(2*L+1)*v+v**2))==0
assert sp.factor((L**2-2*L*D/T)+(L-C/T) -(L**2+L-(2*L*D+C)/T))==0
print('PASS: exact flow identity, equilibrium, radial gap and residence-bound algebra')
