#!/usr/bin/env python3
"""Exact rational checks for robust spanning-tree design on book graphs.

Requires only the Python standard library. These are finite checks, not a proof
of the formulas for arbitrary graph size or real parameters.
"""
from fractions import Fraction as F
from math import factorial
from itertools import product


def determinant(M):
    n=len(M)
    A=[list(row) for row in M]
    det=F(1)
    for k in range(n):
        pivot=next((i for i in range(k,n) if A[i][k]),None)
        if pivot is None: return F(0)
        if pivot!=k:
            A[k], A[pivot]=A[pivot], A[k]
            det=-det
        p=A[k][k]
        det*=p
        for i in range(k+1,n):
            ratio=A[i][k]/p
            for j in range(k+1,n):
                A[i][j]-=ratio*A[k][j]
            A[i][k]=0
    return det


def graph(m,a,b):
    # Two hubs 0,1; pages 2..m+1. The bridge is indexed last.
    return [(0,v,a) for v in range(2,m+2)]+[(1,v,a) for v in range(2,m+2)]+[(0,1,b)]


def tau(m,edges,drop=None):
    n=m+2
    L=[[F(0) for _ in range(n-1)] for _ in range(n-1)]
    for k,(u,v,w) in enumerate(edges):
        if k==drop: continue
        if u<n-1: L[u][u]+=w
        if v<n-1: L[v][v]+=w
        if u<n-1 and v<n-1:
            L[u][v]-=w
            L[v][u]-=w
    return determinant(L)


def branch(m,t):
    t=F(t)
    lo=F(4*m,2*m*m+m-1)
    hi=F(4*m,m*m-1)
    if t<=lo: return F(m+1,2)
    if t>=hi: return F(0)
    return F(4*m-(m*m-1)*t,2*m*t)


def symmetric_objective(m,t,B,r):
    a=F(B)/(2*m+F(t)*r)
    b=r*a
    direct=min(tau(m,graph(m,a,b),k) for k in range(2*m+1))
    closed=F(2)**(m-2)*a**(m+1)*min(F(m-1)+2*r,F(2*m))
    assert direct==closed
    return direct


def check():
    count=0
    for m in range(2,9):
        # Rational determinant checks for original, bridge-deleted and side-deleted graphs.
        for a,b in [(F(1),F(0)),(F(2,3),F(4,5)),(F(7,4),F(2,11))]:
            e=graph(m,a,b)
            assert tau(m,e)==F(2)**(m-1)*a**m*(m*a+2*b); count+=1
            assert tau(m,e,2*m)==F(2)**(m-1)*m*a**(m+1); count+=1
            for k in range(2*m):
                assert tau(m,e,k)==F(2)**(m-2)*a**m*((m-1)*a+2*b);count+=1
        lo=F(4*m,2*m*m+m-1)
        hi=F(4*m,m*m-1)
        assert F(0)<lo<hi
        count+=1
        tvals=(lo/2,lo,(lo+hi)/2,hi,hi*2)
        for t in tvals:
            r=branch(m,t)
            B=F(11,3)
            assert r>=0
            v=symmetric_objective(m,t,B,r)
            count+=1
            # Brute rational competitors, including both phase boundary sides.
            for rr in [F(0),F(1,10),F(1,2),F(1),F(m+1,2),F(3),F(9),F(20)]:
                assert v>=symmetric_objective(m,t,B,rr)
                count+=1
            # Cost accounting and bound from analytic stationarity.
            a=B/(2*m+t*r);b=r*a
            assert 2*m*a+t*b==B;count+=1
        # Asymmetric perturbations of the FULL independently weighted graph.
        t=(lo+hi)/2
        r=branch(m,t)
        a=F(11,3)/(2*m+t*r);b=r*a
        best=symmetric_objective(m,t,F(11,3),r)
        for k in range(2*m):
            eps=F(1,17)*a
            edges=graph(m,a,b)
            # Exchange equal-price edges; preserve budget, retain nonnegative weights.
            u,v,w=edges[k];edges[k]=(u,v,w+eps)
            j=(k+1)%(2*m)
            u,v,w=edges[j];edges[j]=(u,v,w-eps)
            worst=min(tau(m,edges,drop=i) for i in range(len(edges)))
            assert worst<best
            count+=1
    print(f'PASS {count} exact determinant/budget/competitor assertions')

if __name__=='__main__':
    check()
