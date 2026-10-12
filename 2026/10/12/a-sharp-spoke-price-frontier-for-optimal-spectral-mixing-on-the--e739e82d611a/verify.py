#!/usr/bin/env python3
"""Supplementary arithmetic checks for the priced Petersen spectral-gap theorem.

Needs Python 3 standard library for exact checks. If NumPy is installed,
performs additional numerical spectrum and feasible-allocation comparisons.
The universal proof is analytical; finite checks cannot certify uniqueness.
"""
from fractions import Fraction as F
from random import Random
from math import sqrt

N=10
EDGE_OUTER=[(j,(j+1)%5) for j in range(5)]
EDGE_INNER=[(5+j,5+(j+2)%5) for j in range(5)]
EDGE_SPOKE=[(j,5+j) for j in range(5)]
EDGES=EDGE_OUTER+EDGE_INNER+EDGE_SPOKE

def exact_L(u,s):
    w=[u]*10+[s]*5
    L=[[F(0) for _ in range(N)] for _ in range(N)]
    for (i,j),e in zip(EDGES,w):
        L[i][i]+=e;L[j][j]+=e;L[i][j]-=e;L[j][i]-=e
    return L

def multiply(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def characteristic(A):
    # Faddeev--LeVerrier: exact rational characteristic polynomial coefficients.
    n=len(A)
    X=[[F(int(i==j)) for j in range(n)] for i in range(n)]
    coefficients=[F(1)]
    for k in range(1,n+1):
        Y=multiply(A,X)
        c=-sum(Y[i][i] for i in range(n))/k
        coefficients.append(c)
        X=[[Y[i][j]+(c if i==j else 0) for j in range(n)] for i in range(n)]
    return coefficients

def poly_mult(p,q):
    ans=[F(0)]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q): ans[i+j]+=a*b
    return ans

def exact_cases():
    cases=[(F(1,5),F(7,81),F(11,81),F(5,27)),
           (F(2,5),F(1,12),F(1,12),F(1,6)),
           (F(1),F(1,15),F(1,15),F(2,15)),
           (F(10),F(1,60),F(1,60),F(1,30))]
    for t,u,s,gap in cases:
        assert 10*u+5*t*s==1
        L=exact_L(u,s)
        assert all(sum(row)==0 for row in L)
        poly=[F(1)]
        for factor in ([F(1),F(0)],[F(1),-2*s]):poly=poly_mult(poly,factor)
        quad=[F(1),-(5*u+2*s),5*u*(u+s)]
        for _ in range(4):poly=poly_mult(poly,quad)
        assert characteristic(L)==poly, (t,characteristic(L),poly)
        # λ = 2s or the smaller of the two quadratic roots.
        discr=(5*u+2*s)**2-20*u*(u+s)
        low=(5*float(u)+2*float(s)-sqrt(float(discr)))/2
        assert abs(min(2*float(s),low)-float(gap)) < 1e-12
    return len(cases)

def numerical():
    try:
        import numpy as np
    except ImportError:
        return 'NumPy absent (optional numerical checks skipped)'
    rng=Random(20260525)
    checked=0
    for t in [0.0001,0.01,0.05,0.1,0.2,0.35,0.4,0.55,1,2,10,100]:
        if t<F(2,5):
            r=(2*sqrt(t)+(4-5*t)*sqrt(2-t))/((8-5*t)*sqrt(t))
        else:r=1.
        u=1/(5*(2+t*r));s=r*u
        Nval=2.5+r-sqrt(r*r+1.25)
        target=min(2*r,Nval)*u
        assert abs(10*u+5*t*s-1)<1e-12
        W=np.array([u]*10+[s]*5)
        def eigen_gap(weights):
            L=np.zeros((10,10))
            for (i,j),a in zip(EDGES,weights):
                L[i,i]+=a;L[j,j]+=a;L[i,j]-=a;L[j,i]-=a
            return np.linalg.eigvalsh(L)[1]
        got=eigen_gap(W)
        assert abs(got-target)<2e-12,(t,got,target)
        for k in range(60):
            test=np.array([0.02+rng.random() for _ in range(15)])
            test/=sum(test[:10])+t*sum(test[10:])
            assert eigen_gap(test)<=target+2e-12,(t,k,eigen_gap(test),target)
            checked+=1
    return f'{len([0.0001,0.01,0.05,0.1,0.2,0.35,0.4,0.55,1,2,10,100])} full spectra, {checked} arbitrary feasible allocations'

if __name__=='__main__':
    a=exact_cases();b=numerical()
    print(f'VERIFY_OK {a} exact rational 10-by-10 characteristic identities; {b}')
