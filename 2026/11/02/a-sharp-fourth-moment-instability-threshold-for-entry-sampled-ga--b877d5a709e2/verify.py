#!/usr/bin/env python3
"""Exact arithmetic checks for fourth-moment threshold of entry-sampled Gauss-Seidel."""
from fractions import Fraction
from itertools import product
import sympy as sp

r=sp.symbols('r', positive=True)
x,y=sp.symbols('x y')
a=sp.Rational(1,2)
A=sp.Matrix([[1,r],[r,-1]])
P=x**4+y**4
Q=x**3*y-x*y**3
R=x*x*y*y
B=[P,Q,R]
M=[]
L=sp.eye(2)
for i,j in product(range(2),repeat=2):
    E=sp.eye(2)[:,j]*A[i,:]
    U=sp.simplify(sp.eye(2)-a*E/A[i,j]); p=sp.factor(A[i,j]**2/(2*(1+r*r)))
    M.append((U,p))

def operator(F):
    out=sp.Integer(0)
    for U,p in M:
        v=U*sp.Matrix([x,y])
        out+=p*F.subs({x:v[0],y:v[1]},simultaneous=True)
    return sp.factor(sp.expand(out))

C=sp.Matrix([
    [(r**4+16*r*r+1)/(32*r*r),(1-r*r)/(16*r),sp.Rational(1,8)],
    [(r*r-1)/(8*r),sp.Rational(1,8),0],
    [sp.Rational(3,8),0,sp.Rational(1,4)]
])
for j in range(3):
    assert sp.simplify(operator(B[j])-sum(C[i,j]*B[i] for i in range(3)))==0

assert sp.simplify((sp.eye(3)-C).det()+3*(5*r**4-94*r*r+5)/(1024*r*r))==0
assert sp.factor(C.charpoly().as_expr().subs(r,1)) == sp.factor((sp.Symbol('lambda')-sp.Rational(1,8))*(sp.Symbol('lambda')**2-sp.Rational(13,16)*sp.Symbol('lambda')+sp.Rational(3,32)))

for q in [sp.Rational(1,5), sp.Rational(1,2), sp.Rational(3,4)]:
    AA=A.subs(r,q)
    ps=[sp.factor(p.subs(r,q)) for U,p in M]
    Us=[U.subs(r,q) for U,p in M]
    v0=sp.Matrix([1,2]); cur=[(v0,sp.Integer(1))]
    c=C.subs(r,q)
    for k in range(6):
        exact=sum(weight*(v[0]**4+v[1]**4) for v,weight in cur)
        col=c**k*sp.Matrix([1,0,0]); predict=col[0]*(v0[0]**4+v0[1]**4)+col[1]*(v0[0]**3*v0[1]-v0[0]*v0[1]**3)+col[2]*v0[0]**2*v0[1]**2
        assert exact==sp.factor(predict)
        s2=sum(weight*(v[0]**2+v[1]**2) for v,weight in cur)
        assert s2==sp.Rational(3,4)**k*(v0[0]**2+v0[1]**2)
        cur=[(U*v,weight*p) for v,weight in cur for U,p in zip(Us,ps)]

# Diagonalized benchmark and sharp critical interval.
tcrit=(sp.Integer(47)-2*sp.sqrt(546))/5
rcrit=sp.sqrt(tcrit)
assert sp.simplify(5*tcrit**2-94*tcrit+5)==0
assert sp.Rational(1,5)<rcrit<sp.Rational(1,4)
import numpy as np
for rr,expect in [(0.1,True),(0.2,True),(0.3,False),(1,False)]:
    eig=np.linalg.eigvals(np.array(C.subs(r,rr).evalf(),dtype=float))
    assert (max(abs(eig))>1)==expect
print('VERIFY_OK: exact quartic operator, determinant, r=1 eigensystem, 36 exhaustive finite-path moment identities, sharp crossing samples')
