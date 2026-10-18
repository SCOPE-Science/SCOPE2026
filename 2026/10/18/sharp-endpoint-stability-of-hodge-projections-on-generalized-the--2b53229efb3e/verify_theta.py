"""Independent incidence-matrix checks for the generalized-theta Hodge bounds.

Usage: python verify_theta.py
Requires numpy and sympy. Universal statements are proved analytically,
not by these finite tests.
"""
from fractions import Fraction
from itertools import product
import random
import numpy as np
import sympy as sp


def incidence(lengths, symbolic=False):
    """Rows of oriented edge/vertex incidence; terminal vertices are 0 and 1."""
    edges=[]; next_v=2
    for m in lengths:
        prev=0
        for j in range(m):
            nxt=1 if j==m-1 else next_v
            if j<m-1: next_v+=1
            edges.append((prev,nxt)); prev=nxt
    if symbolic:
        B=sp.zeros(len(edges),next_v-1)
        for i,(u,v) in enumerate(edges):
            if u!=0:B[i,u-1]-=1
            if v!=0:B[i,v-1]+=1
    else:
        B=np.zeros((len(edges),next_v-1))
        for i,(u,v) in enumerate(edges):
            if u!=0:B[i,u-1]-=1
            if v!=0:B[i,v-1]+=1
    return B


def predicted(lengths):
    r=len(lengths)
    S=sum((Fraction(1,m) for m in lengths),Fraction(0))
    s=min(lengths)
    p=Fraction(2)-Fraction(2,s)+Fraction(r-2,s)/S+Fraction(2,s*s)/S
    q=Fraction(1)+Fraction(r-2,s)/S
    return p,q


def exact_check(lengths):
    B=incidence(lengths,True)
    P=B*(B.T*B).inv()*B.T
    Q=sp.eye(P.rows)-P
    pnorm=max(sum(abs(P[i,j]) for j in range(P.cols)) for i in range(P.rows))
    qnorm=max(sum(abs(Q[i,j]) for j in range(Q.cols)) for i in range(Q.rows))
    p,q=predicted(lengths)
    assert pnorm==sp.Rational(p.numerator,p.denominator), (lengths,pnorm,p)
    assert qnorm==sp.Rational(q.numerator,q.denominator), (lengths,qnorm,q)
    # A sign pattern of a maximizing row exactly attains the stated infinity norm.
    row=max(range(P.rows), key=lambda i:sum(abs(P[i,j]) for j in range(P.cols)))
    x=sp.Matrix([sp.sign(P[row,j]) for j in range(P.cols)])
    assert (P*x)[row]==pnorm


def float_check(lengths):
    B=incidence(lengths)
    P=B@np.linalg.solve(B.T@B,B.T)
    Q=np.eye(B.shape[0])-P
    p,q=predicted(lengths)
    assert abs(np.max(np.sum(np.abs(P),axis=1))-float(p))<2e-8,(lengths,p)
    assert abs(np.max(np.sum(np.abs(Q),axis=1))-float(q))<2e-8,(lengths,q)
    r=len(lengths); S=sum(1/m for m in lengths)
    f=lambda m:2-2/m+(r-2)/(m*S)+2/(m*m*S)
    assert max(f(m) for m in lengths)-f(min(lengths))<1e-12
    if r>=3 and len(set(lengths))>1:
        other=sorted(lengths)[1:-1]
        comparison=f(min(lengths))-f(max(lengths))
        criterion=(r-2)-2*sum(1/m for m in other)
        assert abs(comparison-(1/min(lengths)-1/max(lengths))*criterion/S)<1e-10
    assert (P@P-P).max()<2e-8 and np.max(abs(P@P-P))<2e-8
    assert np.max(abs(P-Q-np.eye(P.shape[0])+2*Q))<2e-8 # algebraic identity P+Q=I
    assert np.max(abs(P+Q-np.eye(P.shape[0])))<2e-8


def main():
    exact=[]
    for r in (2,3,4):
        for lengths in product(range(1,6),repeat=r):
            if lengths!=tuple(sorted(lengths)) or lengths.count(1)>1 or sum(lengths)>12:
                continue
            exact.append(lengths)
    # Select all small admissible tuples; exact inversion has rational output.
    for lengths in exact:exact_check(lengths)
    rng=random.Random(227104)
    for _ in range(150):
        r=rng.randint(2,8)
        lengths=[rng.randint(2,10) for _ in range(r)]
        if rng.randrange(3)==0:lengths[rng.randrange(r)]=1
        float_check(lengths)
    # Equal-arm and one-short-arm asymptotic formulas checked as rational identities.
    for r in range(2,30):
        for m in range(2,40):
            p,q=predicted([m]*r)
            assert p==Fraction(3)-Fraction(2,r)-Fraction(2*(r-1),r*m)
            assert q==Fraction(2)-Fraction(2,r)
        for m in (100,1000,100000):
            p,q=predicted([2]+[m]*(r-1))
            assert p<r and q<r-1 if r>=3 else p<r and q==1
    print(f'PASS {len(exact)} exact symbolic graph projections, 150 numerical graph projections, '
          '1,064 equal-arm identities and 84 asymptotic-bound checks')

if __name__=='__main__':main()
