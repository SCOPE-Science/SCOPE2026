#!/usr/bin/env python3
from fractions import Fraction as F
from math import sqrt

# Sparse exact polynomials in variables
# (a,b,c,p,q,t,r2,x,y,k), represented by exponent tuples.
NV = 10

def mon(var=None, coeff=1, power=1):
    e=[0]*NV
    if var is not None:
        e[var]=power
    return {tuple(e):F(coeff)}

def const(c): return mon(None,c)
def add(A,B):
    C=dict(A)
    for m,v in B.items():
        C[m]=C.get(m,F(0))+v
        if C[m]==0: del C[m]
    return C

def neg(A): return {m:-v for m,v in A.items()}
def sub(A,B): return add(A,neg(B))
def mul(A,B):
    C={}
    for ma,ca in A.items():
        for mb,cb in B.items():
            m=tuple(x+y for x,y in zip(ma,mb))
            C[m]=C.get(m,F(0))+ca*cb
    return {m:v for m,v in C.items() if v}
def scale(A,c): return {m:F(c)*v for m,v in A.items() if F(c)*v}
def power(A,n):
    R=const(1)
    Q=A
    while n:
        if n&1: R=mul(R,Q)
        Q=mul(Q,Q); n//=2
    return R

# Indices.
a,b,c,p,q,t,r2,x,y,k=range(NV)
A=mon(a); Bc=mon(b); Cc=mon(c); Pp=mon(p); Q=mon(q); T=mon(t)
R2=mon(r2); X=mon(x); Y=mon(y); K=mon(k)
X2=power(X,2); Y2=power(Y,2); XY=mul(X,Y)
s=add(X2,Y2)
alpha=add(add(mul(A,X2),scale(mul(Bc,XY),2)),mul(Cc,Y2))
beta=add(add(mul(Pp,X2),scale(mul(Q,XY),2)),mul(T,Y2))
D=sub(mul(A,Cc),power(Bc,2))
E=sub(mul(Pp,T),power(Q,2))

# Cross-multiplied chord equality.
left=mul(sub(alpha,mul(mul(R2,D),s)),power(beta,2))
right=mul(sub(beta,mul(mul(R2,E),s)),power(alpha,2))
Fpoly=sub(left,right)
Ppoly=add(mul(mul(alpha,beta),sub(beta,alpha)),
          mul(mul(R2,s),sub(mul(E,power(alpha,2)),mul(D,power(beta,2)))))
assert Fpoly==Ppoly

# The decisive proportional-case factorization beta=k alpha, E=k^2 D.
betak=mul(K,alpha)
Ek=mul(power(K,2),D)
Pk=add(mul(mul(alpha,betak),sub(betak,alpha)),
       mul(mul(R2,s),sub(mul(Ek,power(alpha,2)),mul(D,power(betak,2)))))
target=mul(mul(K,sub(K,const(1))),power(alpha,3))
assert Pk==target

# Direct regression checks for representative rational SPD matrices.
def chord(A11,A12,A22,rad,e1,e2):
    v1,v2=-e2,e1
    al=A11*v1*v1+2*A12*v1*v2+A22*v2*v2
    ga=A11*e1*e1+2*A12*e1*e2+A22*e2*e2
    et=A11*e1*v1+A12*(e1*v2+e2*v1)+A22*e2*v2
    det=A11*A22-A12*A12
    disc=4*(al-rad*rad*det)
    assert disc>0
    qdisc=(2*rad*et)**2-4*al*(rad*rad*ga-1)
    assert abs(qdisc-disc)<1e-11
    return sqrt(disc)/al

examples=[
    (0.16,0.00,0.25,1.0),
    (0.10,0.02,0.30,1.0),
    (0.04,-0.01,0.20,1.5),
]
for aa,bb,cc,rr in examples:
    assert aa*cc-bb*bb>0
    for e1,e2 in [(1.0,0.0),(0.0,1.0),(0.6,0.8),(-0.8,0.6)]:
        L=chord(aa,bb,cc,rr,e1,e2)
        assert L>0

print('VERIFY_OK')
print('cross_multiplied_sextic = exact')
print('proportional_factorization = exact')
print('quadratic_chord_regressions = passed')
