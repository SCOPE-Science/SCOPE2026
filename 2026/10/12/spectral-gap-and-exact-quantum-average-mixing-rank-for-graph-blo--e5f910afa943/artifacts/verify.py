#!/usr/bin/env python3
"""Exact and numerical tests for average-mixing spectra on independent-fibre graph blow-ups.
Requires sympy and numpy; no external files, network, or graph packages.
"""
from __future__ import annotations
import itertools
import random
import sympy as s
import numpy as np


def base_adjacency(n, edges):
    A=s.zeros(n)
    for u,v in edges:
        assert 0<=u<v<n
        A[u,v]=A[v,u]=1
    return A


def spectral_projectors(A):
    n=A.rows
    eigenvalues=list(A.eigenvals().keys())
    eye=s.eye(n)
    ans={}
    for lam in eigenvalues:
        E=eye
        for mu in eigenvalues:
            if lam!=mu:
                E=E*(A-mu*eye)/(lam-mu)
        E=E.applyfunc(s.simplify)
        assert (E*E-E).applyfunc(s.simplify)==s.zeros(n)
        ans[lam]=E
    assert (sum(ans.values(),s.zeros(n))-eye).applyfunc(s.simplify)==s.zeros(n)
    return ans


def average(A):
    Es=spectral_projectors(A)
    M=s.zeros(A.rows)
    for E in Es.values():
        M+=E.multiply_elementwise(E)
    return M.applyfunc(s.simplify), Es


def exact_check(A,m):
    n=A.rows
    B=s.kronecker_product(A,s.ones(m))
    Md, _=average(B)
    Mg, Es=average(A)
    E0=Es.get(s.Integer(0),s.zeros(n))
    P=s.ones(m)/m
    Q=s.eye(m)-P
    D=s.diag(*[E0[i,i] for i in range(n)])
    formula=(s.kronecker_product(Mg,s.ones(m))/m**2
        +s.Rational(2,m)*s.kronecker_product(D,Q)
        +s.kronecker_product(s.eye(n),s.Rational(m-2,m)*s.eye(m)+s.ones(m)/m**2))
    assert (Md-formula).applyfunc(s.simplify)==s.zeros(n*m)
    claimed=n+(m-1)*sum(bool(s.simplify(m-2+2*E0[i,i])>0) for i in range(n))
    assert Md.rank()==claimed, (n,m,Md.rank(),claimed)
    assert all(x>=0 for x in [s.simplify(E0[i,i]) for i in range(n)])
    # Matching complete eigenvalue multisets via the formula's invariant blocks
    factors=(Mg+(m-1)*s.eye(n))/m
    const_mult=factors.eigenvals()
    fibre=[s.simplify(s.Rational(m-2,m)+s.Rational(2,m)*E0[i,i]) for i in range(n)]
    pred={}
    for value,mult in const_mult.items():
        value=s.simplify(value)
        pred[value]=pred.get(value,0)+mult
    for value in fibre:
        pred[value]=pred.get(value,0)+m-1
    actual={}
    for value,mult in Md.eigenvals().items():
        value=s.simplify(value)
        actual[value]=actual.get(value,0)+mult
    assert pred==actual, (pred,actual)
    return claimed


cases=[
    ('isolated',base_adjacency(1,[])),
    ('edge',base_adjacency(2,[(0,1)])),
    ('P3',base_adjacency(3,[(0,1),(1,2)])),
    ('K3',base_adjacency(3,[(0,1),(0,2),(1,2)])),
    ('C4',base_adjacency(4,[(0,1),(1,2),(2,3),(0,3)])),
    ('star',base_adjacency(4,[(0,1),(0,2),(0,3)])),
    ('edge_plus_iso',base_adjacency(3,[(0,1)])),
]


def main():
    count=0
    examples={}
    for name,A in cases:
        for m in (2,3):
            rank=exact_check(A,m)
            examples[(name,m)]=rank
            count+=1
    assert examples['P3',2]==5
    assert examples['edge',2]==2
    assert examples['star',2]==7
    assert examples['edge',3]==6
    assert examples['isolated',2]==2
    # Independent floating point baseline over random graphs and larger fibres.
    rng=random.Random(51041)
    trials=0
    worst=0.0
    for n in range(2,8):
        for density in (0.20,0.52,0.84):
            edges=[(i,j) for i in range(n) for j in range(i+1,n) if rng.random()<density]
            A=np.array(base_adjacency(n,edges),dtype=float)
            Eg,Ug=np.linalg.eigh(A)
            Pg=[]
            for eig in Eg:
                if not any(abs(eig-v)<1e-8 for v in Pg): Pg.append(eig)
            E0=np.zeros((n,n))
            Mg=np.zeros((n,n))
            for eig in Pg:
                idx=np.where(abs(Eg-eig)<1e-8)[0]
                E=Ug[:,idx]@Ug[:,idx].T
                Mg+=E*E
                if abs(eig)<1e-8:E0=E
            for m in (2,3,4):
                B=np.kron(A,np.ones((m,m)))
                Eb,Ub=np.linalg.eigh(B)
                uniq=[]
                Md=np.zeros_like(B)
                for eig in Eb:
                    if any(abs(eig-v)<1e-8 for v in uniq):continue
                    uniq.append(eig)
                    idx=np.where(abs(Eb-eig)<1e-8)[0]
                    E=Ub[:,idx]@Ub[:,idx].T
                    Md+=E*E
                Q=np.eye(m)-np.ones((m,m))/m
                formula=np.kron(Mg,np.ones((m,m)))/m**2 + 2/m*np.kron(np.diag(np.diag(E0)),Q) + np.kron(np.eye(n),(m-2)/m*np.eye(m)+np.ones((m,m))/m**2)
                error=np.max(np.abs(Md-formula))
                assert error<1e-10,(n,m,error)
                worst=max(worst,error)
                evals=np.linalg.eigvalsh(Md)
                if m>=3:
                    assert min(evals)>(m-2)/m-1e-9
                trials+=1
    print(f'VERIFY_OK exact_matrices={count} numerical_matrices={trials} P3_two_clone_rank={examples["P3",2]}/6 star_two_clone_rank={examples["star",2]}/8 worst_formula_error={worst:.3g}')

if __name__=='__main__': main()
