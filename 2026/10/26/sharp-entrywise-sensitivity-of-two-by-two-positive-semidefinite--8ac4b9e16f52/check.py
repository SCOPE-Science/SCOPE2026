#!/usr/bin/env python3
"""Exact arithmetic sanity checks for the 2-by-2 PSD projection stability theorem.

Only the Python standard library is required. This script checks algebraic
identities and sample rational spectral derivatives; the analytic proof in
RESULT.md supplies the universal quantifiers.
"""
from fractions import Fraction as F
from math import sqrt

checks=0

def ok(condition,label):
    global checks
    assert condition, label
    checks+=1

def add(a,b): return [a[i]+b[i] for i in range(max(len(a),len(b)))]  # unused

def polyadd(a,b):
    n=max(len(a),len(b));return [(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n)]

def polymul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):z[i+j]+=x*y
    return z

# Identity 3/2 - [1+t²(1-t²+2t)/(1+t²)²]
# = (t-1)²(3t²+2t+1)/(2(1+t²)²).
L=polyadd(polymul([3],polymul([1,0,1],[1,0,1])),
          polymul([-2],polyadd(polymul([1,0,1],[1,0,1]),polymul([0,0,1],[1,2,-1]))))
R=polymul([1,-2,1],[1,2,3])
ok(L==R,'diagonal T1 polynomial identity')

# Off-diagonal T1: 1+z-2z² <=9/8 from 2(z-1/4)².
z=F(1,4)
ok(F(9,8)-(1+z-2*z*z)==0,'off diagonal T1 max')

# Rank-one T0 diagonal maximum (3+2sqrt(2))/4<3/2.
ok((3+2*sqrt(2))/4<1.5,'T0 strict norm bound')

# Matrix action on symmetric inputs encoded by coefficient matrices in basis
# (E11, E12+E21, E22). Let p=t/sqrt(1+t²) and q=1/sqrt(1+t²).
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def plus(A,B):return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def minus(A,B):return [[A[i][j]-B[i][j] for j in range(2)] for i in range(2)]

def mul(c,A):return [[c*A[i][j] for j in range(2)] for i in range(2)]

def jac(A,Q,k):
    R=minus([[F(1),F(0)],[F(0),F(1)]],Q)
    return plus(mm(mm(R,A),R),mul(k,plus(mm(mm(R,A),Q),mm(mm(Q,A),R))))

BASIS=[[[F(1),F(0)],[F(0),F(0)]],[[F(0),F(1)],[F(1),F(0)]],[[F(0),F(0)],[F(0),F(1)]]]
for tnum in range(0,31):
    t=F(tnum,9);d=1+t*t
    Q=[[t*t/d,t/d],[t/d,F(1)/d]]
    for k in (F(0),F(1,10),F(1,2),F(9,10),F(1)):
        cols=[jac(A,Q,k) for A in BASIS]
        vals=[sum(abs(C[i][j]) for C in cols) for i,j in ((0,0),(0,1),(1,1))]
        for val in vals: ok(val<=F(3,2),'all sample derivative row sums')
        if k<F(1):
            for val in vals: ok(val<F(3,2),'strict sample derivative row sums')
        # Projector decomposition and symmetry check.
        P0=[mm(mm(minus([[F(1),F(0)],[F(0),F(1)]],Q),A),minus([[F(1),F(0)],[F(0),F(1)]],Q)) for A in BASIS]
        P1=[minus(A,mm(mm(Q,A),Q)) for A in BASIS]
        for idx in range(3):
            for i in range(2):
                for j in range(2):
                    ok(cols[idx][i][j]==(1-k)*P0[idx][i][j]+k*P1[idx][i][j],'convex decomposition')

# Demonstrate the limiting critical row at equal absolute eigenvector components.
Q=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
H=[[F(1),F(-1)],[F(-1),F(-1)]]
for n in (10,100,1000,10000):
    delta=F(1,n); k=1/(1+delta)
    direct=jac(H,Q,k)[0][0]
    ok(direct==F(1,2)+k,'critical Jacobian limit formula')
    ok(F(3,2)-direct==delta/(1+delta),'explicit sharpness gap')

# Floating-point checks of finite differences, not used as a proof.
def psdplus(a,b,c):
    mu=(a+c)/2; s=sqrt(((a-c)/2)**2+b*b)
    lo=mu-s; hi=mu+s
    if hi<=0:return (0.,0.,0.)
    if lo>=0:return (a,b,c)
    fac=hi/2
    return fac*(1+(a-c)/(2*s)), fac*b/s,fac*(1-(a-c)/(2*s))
for n in (10,100,1000):
    delta=1./n; h=delta*delta/10
    aa=(1-delta)/2; bb=-(1+delta)/2
    first=psdplus(aa+h,bb-h,aa-h)[0]
    old=psdplus(aa,bb,aa)[0]
    ratio=(first-old)/h
    ok(abs(ratio-(.5+1/(1+delta)))<3*h/delta+1e-4,'finite perturbation and derivative')
print(f'PASS: {checks} exact/algebraic and sample numerical assertions')
