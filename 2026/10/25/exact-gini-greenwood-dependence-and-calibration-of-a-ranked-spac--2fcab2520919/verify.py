#!/usr/bin/env python3
"""Exact checks for uniform-spacing Gini/Greenwood mixed moments.
Run: python3 verify.py. Uses only Python's standard library.
"""
from fractions import Fraction as F
from collections import Counter

checks=0

def ck(actual, expected, label):
    global checks
    assert actual==expected, (label,actual,expected)
    checks+=1

def falling_moment(idx,m):
    # Dirichlet(1,...,1), expectation of a product of coordinates.
    count=Counter(idx)
    factorial=1
    for n in count.values():
        for j in range(2,n+1):factorial*=j
    denom=1
    for j in range(len(idx)):denom*=m+j
    return F(factorial,denom)

for m in range(2,25):
    # Conditional on a coordinate ordering of a uniform Dirichlet vector,
    # its successive ranked gaps, weighted by their multiplicity, form a
    # NEW uniform Dirichlet vector Z. This representation is independent
    # of the unordered pair/conditional-Beta calculation in the proof.
    weights=[F(j,m) for j in range(m)]
    qcoeff=[[F(1,m-min(j,k)) for k in range(m)] for j in range(m)]
    eg=sum(weights,F(0))/m
    eq=sum(qcoeff[j][k]*falling_moment((j,k),m)
           for j in range(m) for k in range(m))
    eg2=sum(weights[j]*weights[k]*falling_moment((j,k),m)
           for j in range(m) for k in range(m))
    egq=sum(weights[i]*qcoeff[j][k]*falling_moment((i,j,k),m)
            for i in range(m) for j in range(m) for k in range(m))
    eq2=F(4*(m+5),(m+1)*(m+2)*(m+3))
    vg=eg2-eg*eg; vq=eq2-eq*eq; cov=egq-eg*eq
    ck(eg,F(m-1,2*m),'mean G')
    ck(eq,F(2,m+1),'mean Q')
    ck(vg,F(m-1,12*m*m),'variance G')
    ck(vq,F(4*(m-1),(m+1)**2*(m+2)*(m+3)),'variance Q')
    ck(cov,F(m-1,2*m*(m+1)*(m+2)),'covariance')
    ck(cov*cov,F(3*(m+3),4*(m+2))*vg*vq,'correlation squared')
    cst=F((m+1)*(4*m-1),6*m**3)
    et=eq-eg/m-cst
    vt=vq+vg/F(m*m)-2*cov/F(m)
    ck(et,F((m-1)*(5*m*m-2*m-1),6*m**3*(m+1)),'mean T')
    ck(vt,F((m-1)**2*(37*m**3-4*m*m-23*m-6),
           12*m**4*(m+1)**2*(m+2)*(m+3)),'variance T')
    z=[F(j+1,m*(m+1)//2) for j in range(m)]
    ordered=[sum((z[j]/(m-j) for j in range(i+1)),F(0)) for i in range(m)]
    g=sum((weights[j]*z[j] for j in range(m)),F(0))
    q=sum((v*v for v in ordered),F(0))
    t=sum(((ordered[i]-F(i+1,m*m))**2 for i in range(m)),F(0))
    ck(g,F(sum(abs(ordered[i]-ordered[j]) for i in range(m)
               for j in range(i+1,m)),m),'deterministic G')
    ck(t,q-g/m-cst,'deterministic T identity')

print('PASS:',checks,'exact-rational checks, m=2,...,24')
