#!/usr/bin/env python3
"""Exact characteristic-zero checks for a two-conic, four-line octic."""
import sympy as s
from sympy.polys.matrices import DomainMatrix
from sympy.polys.domains import ZZ, QQ

X,Y,Z=s.symbols('X Y Z')
Q=X*Z-Y**2
R=4*X**2-8*X*Y+8*X*Z-4*Y*Z+Z**2
lines=[Z,X,X-2*Y+Z,4*X-4*Y+Z]
F=s.prod(lines+[Q,R])
assert s.det(s.hessian(R,(X,Y,Z)))==256
assert s.det(s.hessian(Q,(X,Y,Z)))!=0
assert s.expand(R-(4*X*(X-2*Y+Z)+Z*(4*X-4*Y+Z)))==0
T,U=s.symbols('T U')
assert s.expand(R.subs({X:T*T,Y:T*U,Z:U*U})-(2*T*T-2*T*U+U*U)**2)==0
# Every line is tangent to Q; its restriction to Q is the square of a linear form.
assert [s.factor(l.subs({X:T*T,Y:T*U,Z:U*U})) for l in lines]==[U**2,T**2,(T-U)**2,(2*T-U)**2]
# Each line meets R in exactly its two designated four-cycle vertices.
assert s.factor(R.subs(Z,0))==4*X*(X-2*Y)
assert s.expand(R.subs(X,0)-Z*(-4*Y+Z))==0
# All four crossings between the two opposite pairs of lines belong to R.
for pt in [(0,1,0),(2,1,0),(0,1,4),(2,3,4)]:
    assert R.subs(dict(zip((X,Y,Z),pt)))==0
# Quartic Jacobian relation gives the upper bound mdr(F)<=4.
A=-X*(32*X**2*Y+80*X**2*Z-176*X*Y**2-20*X*Y*Z-34*X*Z**2+140*Y**3-46*Y**2*Z+26*Y*Z**2-3*Z**3)
B=(-96*X**3*Z+80*X**2*Y**2+208*X**2*Y*Z-36*X**2*Z**2-160*X*Y**3-108*X*Y**2*Z+122*X*Y*Z**2-30*X*Z**3+84*Y**4-82*Y**3*Z+18*Y**2*Z**2+Y*Z**3)
C=Z*(2*Y-Z)*(70*X*Z-70*Y**2+Z**2)
assert s.expand(A*F.diff(X)+B*F.diff(Y)+C*F.diff(Z))==0
# Exact injectivity in degree 3; multiplication by a linear form then rules out all lower degrees.
r=3
mon=[X**i*Y**j*Z**(r-i-j) for i in range(r+1) for j in range(r-i+1)]
E=[(i,j,7+r-i-j) for i in range(8+r) for j in range(8+r-i)]
partials=[s.Poly(F.diff(v),X,Y,Z).as_dict() for v in (X,Y,Z)]
cols=[]
for p in partials:
    for m in mon:
        md=s.Poly(m,X,Y,Z).monoms()[0]
        cols.append({tuple(a+b for a,b in zip(k,md)):v for k,v in p.items()})
rows=[[int(c.get(e,0)) for c in cols] for e in E]
DM=DomainMatrix(rows,(len(rows),len(cols)),ZZ)
assert DM.convert_to(QQ).nullspace().shape[0]==0
print('EXACT_CONICS_QUARTIC_SYZYGY_AND_NO_CUBIC_SYZYGY_OK')
