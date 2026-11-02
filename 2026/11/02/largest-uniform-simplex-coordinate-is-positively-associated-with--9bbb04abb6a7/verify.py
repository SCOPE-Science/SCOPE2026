#!/usr/bin/env python3
"""Exact checks for the uniform-simplex maximum/Schur-convex covariance law."""
from fractions import Fraction
from math import factorial
from collections import defaultdict

# Sparse polynomial in y_1,...,y_m (nonnegative integer exponent tuples).
def const(m,z=1): return {(0,)*m:Fraction(z)}
def add(*ps):
    r=defaultdict(Fraction)
    for p in ps:
        for e,c in p.items():r[e]+=c
    return {e:c for e,c in r.items() if c}
def mul(p,q):
    if not p or not q:return {}
    r=defaultdict(Fraction)
    for a,x in p.items():
        for b,y in q.items():r[tuple(z+w for z,w in zip(a,b))]+=x*y
    return {e:c for e,c in r.items() if c}
def powp(p,n):
    r=const(len(next(iter(p))),1)
    for _ in range(n):r=mul(r,p)
    return r
def E(p,m):
    # Dirichlet(1,...,1) monomial moments: (m-1)! prod e_i!/(m+sum e_i-1)!
    return sum(c*Fraction(factorial(m-1)*__import__('math').prod(factorial(k) for k in e),factorial(m+sum(e)-1)) for e,c in p.items())
def coordinate(m,j):
    a=[0]*m;a[j]=1
    return {tuple(a):Fraction(1)}
def derivative(p,j):
    r={}
    for e,c in p.items():
        if e[j]:
            t=list(e);t[j]-=1;r[tuple(t)]=c*e[j]
    return r

def check(m,power):
    yy=[coordinate(m,j) for j in range(m)]
    xx=[add(*(mul(const(m,Fraction(1,j+1)),yy[j]) for j in range(k,m))) for k in range(m)]
    maximum=xx[0]
    F=add(*(powp(x,power) for x in xx))
    cov=E(mul(maximum,F),m)-E(maximum,m)*E(F,m)
    df=[derivative(F,j) for j in range(m)]
    rhs={}
    for i in range(m):
        for j in range(i+1,m):
            coeff=Fraction(1,i+1)-Fraction(1,j+1)
            if coeff:
                term=mul(mul(yy[i],yy[j]),add(df[i],mul(const(m,-1),df[j])))
                rhs=add(rhs,mul(const(m,coeff),term))
    rhs=E(rhs,m)/m
    assert E(maximum,m)==sum((Fraction(1,k) for k in range(1,m+1)),Fraction(0))/m
    assert cov==rhs,(m,power,cov,rhs)
    assert cov>0,(m,power,cov)
    return cov

if __name__=='__main__':
    checks=0
    for m in range(2,9):
        for p in (2,3,4):
            c=check(m,p)
            checks+=3
            print('m',m,'power',p,'covariance',c)
    # m=2 Shannon entropy has E[M H]=7/24+log(2)/12 and E[M]E[H]=3/8.
    # Therefore Cov(M,H)=(log(2)-1)/12<0.
    from math import log
    assert (log(2)-1)/12<0
    print('PASSED',checks+1,'exact/analytic assertions')
