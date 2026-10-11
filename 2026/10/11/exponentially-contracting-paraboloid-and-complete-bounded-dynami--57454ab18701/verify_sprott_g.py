#!/usr/bin/env python3
"""Exact symbolic checks for a quadratic dynamical-system reduction."""
import sympy as s

x,y,z,a,b,v,h,lam=s.symbols('x y z a b v h lam',real=True)
F=s.Matrix([a*x+b*z,x*z-y,-x+y])
H=y-x**2/(2*b)
V=-x/2+b*z
Dh=s.expand(sum(s.diff(H,q)*f for q,f in zip((x,y,z),F)))
assert s.factor(Dh+H+(a+s.Rational(1,2))*x**2/b)==0
trans={a:-s.Rational(1,2),y:h+x**2/(2*b),z:(v+x/2)/b}
Dx=s.expand(F[0].subs(trans))
Dv=s.expand(sum(s.diff(V,q)*f for q,f in zip((x,y,z),F)).subs(trans))
Dht=s.expand(Dh.subs(trans))
assert s.simplify(Dx-v)==0
assert s.simplify(Dv-(-v/2-b*x+x**2/2+b*h))==0
assert s.simplify(Dht+h)==0
J=s.Matrix([[s.diff(q,r) for r in (x,y,z)] for q in (x,V,H)])
assert s.simplify(J.det()+b)==0
U=b*x**2/2-x**3/6
Energy=v**2/2+U
Edot=s.diff(Energy,x)*Dx+s.diff(Energy,v)*Dv
assert s.factor(Edot+v**2/2-b*h*v)==0
for xs in (s.Integer(0),2*b):
    assert s.simplify((-b*x+x**2/2).subs(x,xs))==0
    Jac=s.Matrix([[0,1],[-b+xs,-s.Rational(1,2)]])
    assert s.factor((lam*s.eye(2)-Jac).det()-(lam**2+lam/2+b-xs))==0
assert s.simplify(U.subs(x,2*b)-U.subs(x,0)-2*b**3/3)==0
orig=s.Matrix([-x/2+b*z,x*z-y,-x+y])
for subs in ({x:0,y:0,z:0},{x:2*b,y:2*b,z:1}):
    assert all(s.simplify(w.subs(subs))==0 for w in orig)
print('PASS: exact polynomial identities, conjugacy, equilibria, linearization, and energy gap')
