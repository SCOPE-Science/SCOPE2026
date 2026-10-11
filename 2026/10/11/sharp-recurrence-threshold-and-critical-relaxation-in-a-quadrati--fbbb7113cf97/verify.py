#!/usr/bin/env python3
"""Exact algebraic checks for the quadratic flow. Requires SymPy."""
import sympy as s
x,y,z,a,b,c,d,u,L=s.symbols('x y z a b c d u L', nonzero=True, real=True)
f=s.Matrix([a*y, x+z**2, b+c*x+d*z])
Delta=d*d+4*b*c
z_star=d/(2*c)
Q=z-c*y
assert s.expand(f[2]-c*f[1] - (b+d*z-c*z**2))==0
assert s.simplify((b+d*z-c*z**2) - (Delta/(4*c)-c*(z-z_star)**2))==0
for zz in ((d+s.sqrt(Delta))/(2*c),(d-s.sqrt(Delta))/(2*c)):
    rest=[s.simplify(expr.subs({x:-zz**2,y:0,z:zz})) for expr in f]
    assert rest==[0,0,0]
bcrit=-d**2/(4*c)
X=-z_star**2-(d/c)*u-u**2
Y=(d/a)*u**2
Z=z_star+u
v=[s.expand(expr.subs({x:X,y:Y,z:Z,b:bcrit},simultaneous=True)) for expr in f]
assert s.simplify(v[2]+c*u**2)==0
assert s.series(s.diff(X,u)*v[2]-v[0],u,0,3).removeO()==0
assert s.series(s.diff(Y,u)*v[2]-v[1],u,0,3).removeO()==0
J=f.jacobian([x,y,z]).subs(z,z_star)
assert s.simplify(s.det(L*s.eye(3)-J)-L*(L**2-d*L-a))==0
print('PASS: exact coboundary, roots, linearization, center-manifold residuals.')
