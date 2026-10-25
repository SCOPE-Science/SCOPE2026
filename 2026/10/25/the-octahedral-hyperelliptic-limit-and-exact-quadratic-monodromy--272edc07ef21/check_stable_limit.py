#!/usr/bin/env python3
"""Exact identities supporting the double-conic Ciani degeneration (SymPy)."""
import sympy as s
u,v,x,y,z,t,q,ss,w=s.symbols('u v x y z t q ss w')
X=2*u*v
Y=u*u-v*v
Z=s.I*(u*u+v*v)
Q=x*x+y*y+z*z
R=x*x*y*y+y*y*z*z+z*z*x*x
F=x**4+y**4+z**4+t*R
assert s.expand(F.subs(t,2+q)-(Q**2+q*R))==0
assert s.expand(Q.subs({x:X,y:Y,z:Z}))==0
B=u**8+14*u**4*v**4+v**8
assert s.expand(R.subs({x:X,y:Y,z:Z})+B)==0
assert s.discriminant(B.subs(v,1),u)==2**40*3**4
assert s.gcd(B.subs(v,1),s.diff(B.subs(v,1),u))==1
# The strict-transform substitution is an identity in the chart Q=ss*w:
A,Bsym=s.symbols('A B')
assert s.expand((ss*w)**2+ss**2*Bsym-ss**2*(w**2+Bsym))==0
# Partial derivatives of the original Ciani equation.
for vbl,other1,other2 in [(x,y,z),(y,x,z),(z,x,y)]:
    expected=2*vbl*(2*vbl**2+t*(other1**2+other2**2))
    assert s.expand(s.diff(F,vbl)-expected)==0
# Distinct singular exceptional parameter discriminants from derivative cases.
assert s.expand(s.resultant(2*A+t*Bsym,2*Bsym+t*A,A)+Bsym*(t**2-4))==0
print('PASS: quartic identity, conic normalization, octavic branch, discriminant, strict-transform identity, gradient equations.')
