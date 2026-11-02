"""Checks for the pure higher-order SIS model on complete multipartite hypergraphs.

All exact identities use rational arithmetic or SymPy. Bisection and
finite-dimensional eigenvalue checks are supplemental, not the proof.
"""
from fractions import Fraction as F
from itertools import combinations_with_replacement
from math import prod, sqrt
import numpy as np
import sympy as S


def flow(xs,sizes,beta):
    out=[]
    for i,x in enumerate(xs):
        q=prod(sizes[j]*xs[j] for j in range(len(xs)) if j!=i)
        out.append(-x + beta*(1-x)*q)
    return out


def jacobian(xs,sizes,beta):
    m=len(xs)
    J=S.zeros(m)
    for i,x in enumerate(xs):
        q=prod(sizes[j]*xs[j] for j in range(m) if j!=i)
        J[i,i]=-1-beta*q
        for j in range(m):
            if j!=i:
                J[i,j]=beta*(1-x)*sizes[j]*prod(sizes[k]*xs[k] for k in range(m) if k not in (i,j))
    return J


def x_of_h(h,n):
    return 2/(1+sqrt(1+4*n/h))

def phi(h, ns):
    return sum((1-x_of_h(h,n))/(2-x_of_h(h,n)) for n in ns)

def critical(ns):
    lo,hi=1e-12,1e12
    assert phi(lo,ns)>1 and phi(hi,ns)<1
    for _ in range(150):
        mid=sqrt(lo*hi)
        if phi(mid,ns)>1: lo=mid
        else: hi=mid
    h=sqrt(lo*hi)
    xs=[x_of_h(h,n) for n in ns]
    return h, h/prod(n*x for n,x in zip(ns,xs))


def check():
    # Exact critical and positive-branch equilibria, including all Jacobian signs.
    x=S.Rational(1,2)
    sizes=[2,2,2]
    beta=S.Rational(1)
    assert flow([x]*3,sizes,beta)==[0]*3
    J=jacobian([x]*3,sizes,beta)
    assert sorted(J.eigenvals())==[-3,0]
    assert J.eigenvals()[-3]==2 and J.eigenvals()[0]==1
    for x, expect in [(S.Rational(1,3),"lower"),(S.Rational(2,3),"upper")]:
        beta=S.Rational(9,8)
        assert flow([x]*3,sizes,beta)==[0]*3
        eigs=jacobian([x]*3,sizes,beta).eigenvals()
        assert (max(eigs)>0)==(expect=="lower")
        assert (min(eigs)<0)
        assert len([e for e in eigs for _ in range(eigs[e]) if e>0])==(1 if expect=="lower" else 0)
    # All-m version: exact symmetric folds for m=4,5,6.
    for m in (4,5,6):
        x=S.Rational(m-2,m-1)
        beta=S.Rational((m-1)**(m-1),(m-2)**(m-2))
        ns=[1]*m
        assert flow([x]*m,ns,beta)==[0]*m
        J=jacobian([x]*m,ns,beta)
        assert J.eigenvals()=={S.Integer(0):1,S.Integer(-m):m-1}
    # Full six-node Jacobian: 3 class modes and 3 negative transverse modes.
    for x, wanted in [(S.Rational(1,3),{S.Rational(1,2):1,S.Rational(-5,2):2,S.Rational(-3,2):3}),
                      (S.Rational(2,3),{S.Integer(-1):1,S.Integer(-4):2,S.Integer(-3):3})]:
        beta=S.Rational(9,8)
        Jfull=S.zeros(6)
        for a in range(6):
            ga=a//2
            Jfull[a,a]=-1/(1-x)
            for b in range(6):
                if b//2!=ga:
                    Jfull[a,b]=beta*(1-x)*(2*x)  # one other class has 2 nodes
        assert Jfull.eigenvals()==wanted
    # Heterogeneous rational stable endemic equilibrium.
    sizes=[72,27,16]
    xs=[S.Rational(1,2),S.Rational(2,3),S.Rational(3,4)]
    h=S.Rational(36)
    beta=S.Rational(1,216)
    assert all(s*x*x/(1-x)==h for s,x in zip(sizes,xs))
    assert flow(xs,sizes,beta)==[0]*3
    J=jacobian(xs,sizes,beta)
    assert J.trace()<0 and J.det()<0
    B=S.diag(*[1/xi for xi in xs])*J*S.diag(*xs)
    assert B==B.T
    assert all(B[i,j]==1 for i in range(3) for j in range(3) if i!=j)
    assert sum((1-x)/(2-x) for x in xs)==S.Rational(47,60)
    assert all(float(v)<0 for v in np.linalg.eigvalsh(np.array(B).astype(float)))
    # Nontrivial critical thresholds, and fixed-sum balancing.
    c=critical((3,3,3))[1]
    assert abs(c-4/9)<1e-13
    for ns in [(1,4,4),(2,3,4),(1,2,6),(1,1,7)]:
        assert critical(ns)[1]>c
    # For every positive integer partition of n<=18 into three group sizes,
    # test the balancing inequality in the precise finite set of cases.
    for n in range(3,19):
        parts=[p for p in combinations_with_replacement(range(1,n-1),3) if sum(p)==n]
        balanced=tuple(sorted([n//3+int(i<n%3) for i in range(3)]))
        b=critical(balanced)[1]
        for p in parts:
            c2=critical(p)[1]
            assert c2>=b-1e-10,(p,balanced,c2,b)
            if p!=balanced: assert c2>b+1e-10
    print('PASS: exact equilibrium/Jacobian identities; fold and branch inertia;')
    print('      heterogeneous exact certificate; balanced optimum numerical cross-check')
    print('      for all 3-group integer partitions of total size <=18.')
    print('example thresholds:',critical((3,3,3)),critical((2,3,4)),critical((1,4,4)))

if __name__=='__main__':check()
