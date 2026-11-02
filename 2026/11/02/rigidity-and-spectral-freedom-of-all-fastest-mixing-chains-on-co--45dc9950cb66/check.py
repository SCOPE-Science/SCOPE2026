"""Exact and numerical checks for the complete-split optimal mixing theorem.
Usage: python check.py
Requires numpy, sympy.
Checks are corroborative; universal statements rely on the written proof.
"""
from fractions import Fraction
import random
import numpy as np
import sympy as sp


def optimum(p,q):
    if q <= 2*p:
        return Fraction(2,q+2*p), Fraction(q,q+2*p)
    return Fraction(1,q),Fraction(q-p,q)


def make_P(p,q,b,w):
    n=p+q
    A=sp.zeros(n,n)
    for i in range(p):
        for j in range(q):
            A[i,p+j]=A[p+j,i]=sp.Rational(b)
    for i in range(p):
        for j in range(i+1,p):
            A[i,j]=A[j,i]=sp.Rational(w[i][j])
    for i in range(n):
        A[i,i]=1-sum(A[i,j] for j in range(n) if i!=j)
    return A

n_exact=0
for p in range(2,9):
    for q in range(2,12):
        b,t=optimum(p,q)
        if q < p:
            a=Fraction(2*(p-q),p*(q+2*p))
        else:
            a=Fraction(0)
        if q < 2*p and p <= q:
            # A nonzero optional clique weight in this parameter range.
            a=Fraction(2*p-q,2*(p-1)*(q+2*p))
        w=[[a if i!=j else 0 for j in range(p)] for i in range(p)]
        P=make_P(p,q,b,w)
        assert all(x>=0 for x in P)
        assert P==P.T and P*sp.ones(p+q,1)==sp.ones(p+q,1)
        # Exact eigen-multiplicity certificate, not floating-point eigenvalues.
        vals=P.eigenvals()
        expected=[(sp.Rational(1),1), (sp.Rational(1-(p+q)*b),1),
                  (sp.Rational(1-p*b),q-1),(sp.Rational(1-q*b-p*a),p-1)]
        # Merge collisions, particularly at regime boundaries.
        e={}
        for k,m in expected:e[k]=e.get(k,0)+m
        assert vals==e,(p,q,vals,e)
        assert max(abs(v) for v in vals if v!=1)==t,(p,q,vals,t)
        n_exact+=1

# Nonuniform clique edge weights can genuinely remain optimal.
p,q=4,2
b,t=optimum(p,q)
w=[[Fraction(0) for _ in range(p)] for _ in range(p)]
for i in range(p):
    for j in range(i+1,p):
        w[i][j]=w[j][i]=Fraction(3,20)+Fraction(i+j-3,1000)
P=make_P(p,q,b,w)
eigs=np.linalg.eigvalsh(np.asarray(P.tolist(),dtype=float))
assert all(x>=0 for x in P)
assert abs(max(abs(v) for v in eigs[:-1])-float(t))<1e-12
assert len(set(w[i][j] for i in range(p) for j in range(i+1,p)))>1

# Random independently adjustable off-diagonal edges, normalized to feasible rows.
rng=random.Random(20261025)
count=0
for p in range(2,9):
    for q in range(2,11):
        b,t=optimum(p,q)
        for _ in range(25):
            n=p+q
            A=np.zeros((n,n))
            for i in range(p):
                for j in range(i+1,p):
                    A[i,j]=A[j,i]=rng.random()
                for j in range(q):
                    A[i,p+j]=A[p+j,i]=rng.random()
            row_max=A.sum(axis=1).max()
            A*=rng.random()/row_max
            np.fill_diagonal(A,1-A.sum(axis=1))
            ev=np.linalg.eigvalsh(A)
            mu=max(abs(v) for v in ev[:-1])
            assert mu+1e-10>=float(t),(p,q,mu,t)
            count+=1
print(f'PASS exact rational spectra: {n_exact}; nonuniform core witness: 1; independently adjustable feasible comparisons: {count}')
