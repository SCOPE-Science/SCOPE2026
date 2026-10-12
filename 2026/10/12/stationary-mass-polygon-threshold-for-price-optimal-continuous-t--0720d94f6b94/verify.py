#!/usr/bin/env python3
"""Exact and numerical checks for the stationary-mass star spectral-gap formula.

No numerical test certifies the universally quantified theorem; the proof is in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random
from math import sqrt
import numpy as np


def determinant(A):
    """Fraction-free-ish rational elimination; zero if singular."""
    A=[list(x) for x in A]; n=len(A); s=F(1)
    for i in range(n):
        k=next((j for j in range(i,n) if A[j][i]),None)
        if k is None:return F(0)
        if k!=i:
            A[i],A[k]=A[k],A[i];s=-s
        v=A[i][i];s*=v
        for j in range(i+1,n):
            t=A[j][i]/v
            for q in range(i+1,n): A[j][q]-=t*A[i][q]
            A[j][i]=F(0)
    return s


def instance(pi,croots):
    m=len(croots)
    c=[z*z for z in croots]
    lengths=[pi[i]*croots[i] for i in range(m)]
    delta=max(F(0),2*max(lengths)-sum(lengths))
    S=sum(pi[i]*c[i] for i in range(m))
    T=S-delta*delta
    j=lengths.index(max(lengths)) if delta>0 else -1
    x=[pi[i]*(1+delta/croots[i] * (-1 if i==j else 1)) for i in range(m)]
    gamma=1/T
    w=[v/T for v in x]
    V=[[ (pi[i] if i==k else 0)-pi[i]*pi[k] for k in range(m)] for i in range(m)]
    Z=[[ (x[i] if i==k else 0)-V[i][k] for k in range(m)] for i in range(m)]
    assert sum(c[i]*w[i] for i in range(m))==1
    assert all(z>0 for z in w)
    assert determinant(Z)==0
    assert all(determinant([[Z[i][k] for k in inds] for i in inds])>=0
               for r in range(1,m+1) for inds in combinations(range(m),r))
    # Geometric dual, closed polygon or one-longest imbalance.
    if delta>0:
        z=[croots[i]*(1 if i==j else -1) for i in range(m)]
        assert sum(pi[i]*z[i] for i in range(m))==delta
        assert all(sum(Z[i][k]*z[k] for k in range(m))==0 for i in range(m))
    else:
        assert all(x[i]==pi[i] for i in range(m))
    p=np.array([float(z) for z in pi]); ff=np.array(V,dtype=float)
    ww=np.array([float(z) for z in w]); D=np.diag(ww)
    vals=np.linalg.eigvalsh(np.diag(1/np.sqrt(p))@D@np.diag(1/np.sqrt(p)) -
                            np.diag(1/np.sqrt(p))@(np.outer(p,p))@np.diag(1/np.sqrt(p)))
    # Better generalized eigen for D versus V using inv sqrt eigen V.
    v,s=np.linalg.eigh(ff)
    assert min(v)>0
    invsqrt=(s/np.sqrt(v))@s.T
    a=invsqrt@D@invsqrt
    eig=np.linalg.eigvalsh(a)
    assert abs(eig[0]-float(gamma))<2e-8*max(1,float(gamma))
    return delta>0


def main():
    r=Random(20261009)
    cases=0; unbalanced=0
    for m in range(3,7):
        for k in range(80):
            q=[r.randrange(1,15) for _ in range(m+1)]
            total=sum(q); pi=[F(z,total) for z in q[1:]]
            roots=[F(r.randrange(1,18)) for _ in range(m)]
            unbalanced+=instance(pi,roots)
            cases+=1
    assert instance([F(7,10),F(1,20),F(1,20)],[F(1)]*3)
    print(f'VERIFY_OK {cases+1} exact budget/PSD/duality cases, {unbalanced+1} imbalanced, numerical generalized eigenvalue checks')

if __name__=='__main__':main()
