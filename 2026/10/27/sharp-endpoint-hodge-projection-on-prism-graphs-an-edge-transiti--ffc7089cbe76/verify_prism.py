"""Exact-rational finite checks for edge-gradient projections on prism graphs.

Run with Python 3 and SymPy: python verify_prism.py
Finite checks supplement, but do not replace, the all-size arguments.
"""
from fractions import Fraction
import math
import sympy as sp

checks=0
for n in range(3, 13):
    verts=2*n
    edges=[(a*n+j,a*n+(j+1)%n) for a in range(2) for j in range(n)]
    edges += [(j,n+j) for j in range(n)]
    B=sp.zeros(3*n,verts)
    for k,(u,v) in enumerate(edges):B[k,u]=1;B[k,v]=-1
    L=B.T*B
    J=sp.ones(verts,verts)/verts
    Q=(L+J).inv()-J
    P=B*Q*B.T
    C=sp.zeros(n,n)
    for j in range(n):
        C[j,j]=4
        C[j,(j-1)%n]-=1
        C[j,(j+1)%n]-=1
    g=C.inv()[:,0]
    # Directly verify the Green-function recurrence and normalization.
    assert C*g==sp.eye(n)[:,0];checks+=1
    assert sum(g)==sp.Rational(1,2);checks+=1
    assert all(g[j]==g[(n-j)%n] for j in range(n));checks+=1
    assert all(g[j]>=g[j+1] for j in range(n//2));checks+=1
    delta=g[0]-g[n//2]
    H=1-sp.Rational(1,n)+sum(max(sp.Rational(1,n),2*g[j]) for j in range(1,n))+2*delta
    V=1+4*delta
    for k in range(3*n):
        row=sum(abs(P[k,j]) for j in range(3*n))
        assert row==(H if k<2*n else V), (n,k,row,H,V)
        checks+=1
        assert P[k,k]>=0 and P[k,k]<=1
        checks+=1
    assert P*P==P;checks+=1
    assert P.T==P;checks+=1
    if n==3:assert H==sp.Rational(26,15) and V==sp.Rational(9,5);checks+=1
    elif n==4:assert H==2 and V==2;checks+=1
    else:assert H>V;checks+=1
    assert H<3 and V<3;checks+=1
    print(f"n={n}: H={H}, V={V}")

r=2-math.sqrt(3)
q=1/r
L=math.log(q)
A=math.sqrt(3)-1
F=lambda f: 2+A*q**f-2*f-math.log(3)/L
fstar=math.log(2/(A*L))/L
assert 0<fstar<1;checks+=1
assert abs(F(1)-F(0))<1e-13;checks+=1
assert F(fstar)<F(0);checks+=1
for n in [31,100,1234,10000,50000,100000]:
    beta=math.log(n/math.sqrt(3))/L
    k=math.floor(beta)
    gmid=(r**(n//2)+r**(n-n//2))/(2*math.sqrt(3)*(1-r**n))
    tail=2*r**(k+1)*(1-r**(n-2*k-1))/(math.sqrt(3)*(1-r)*(1-r**n))
    H=3-(2*k+2)/n-2*gmid-tail
    discrepancy=n*(3-H)-2*math.log(n)/L
    assert abs(discrepancy-F(beta%1)) < 1e-6, (n,discrepancy,F(beta%1))
    checks+=1
print(f"PASS: {checks} assertions; asymptotic phase minimum {F(fstar):.12f}, maximum {F(0):.12f}")
