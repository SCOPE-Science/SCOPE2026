#!/usr/bin/env python3
"""Exact-rational checks of Hamming-graph edge-space projection constants.

Uses the reduced graph Laplacian, not the semigroup argument of the proof.
Only finite instances are checked; the theorem requires its separate proof.
Requires Python 3 standard library only.
"""
from fractions import Fraction as F
from itertools import product
from math import comb


def invert(a):
    n=len(a)
    aug=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if aug[i][j])
        aug[j],aug[pivot]=aug[pivot],aug[j]
        z=aug[j][j]
        aug[j]=[v/z for v in aug[j]]
        for i in range(n):
            if i!=j and aug[i][j]:
                z=aug[i][j]
                aug[i]=[a-z*b for a,b in zip(aug[i],aug[j])]
    return [row[n:] for row in aug]


def check(d,q):
    verts=list(product(range(q),repeat=d)); N=len(verts)
    edges=[(i,j) for i,x in enumerate(verts) for j,y in enumerate(verts)
           if i<j and sum(a!=b for a,b in zip(x,y))==1]
    E=len(edges)
    assert E == d*(q-1)*q**d//2
    lap=[[0]*N for _ in range(N)]
    for a,b in edges:
        lap[a][a]+=1;lap[b][b]+=1
        lap[a][b]-=1;lap[b][a]-=1
    R=invert([row[:-1] for row in lap[:-1]])
    # Orthogonal cut projection P = B^T L^+ B. Grounding fixes only potential gauge.
    pot=[]
    for a,b in edges:
        rhs=[F((i==b)-(i==a)) for i in range(N-1)]
        pot.append([sum(R[i][j]*rhs[j] for j in range(N-1)) for i in range(N-1)]+[F(0)])
    P=[[pot[j][b]-pot[j][a] for j in range(E)] for a,b in edges]
    Q=[[F(i==j)-P[i][j] for j in range(E)] for i in range(E)]
    pth=F((d+1)*(q-1),q)
    peeth=F(2*(q**d-1),d*q**d*(q-1))
    qth=1+pth-2*peeth
    count=0
    for j in range(E):
        assert sum(abs(P[i][j]) for i in range(E))==pth;count+=1
        assert sum(abs(Q[i][j]) for i in range(E))==qth;count+=1
        assert P[j][j]==peeth;count+=1
    for i in range(E):
        for j in range(E):
            assert P[i][j]==P[j][i];count+=1
            assert Q[i][j]==Q[j][i];count+=1
    # Every projected flow has zero divergence (the defining property of cycles).
    for j in range(E):
        out=[F(0) for i in range(N)]
        for e,(a,b) in enumerate(edges):
            out[a]-=Q[e][j];out[b]+=Q[e][j]
        for v in out:
            assert v==0;count+=1
    # Orthogonal decomposition via P^2=P and Q^2=Q.
    for i in range(E):
        for j in range(E):
            assert sum(P[i][k]*P[k][j] for k in range(E))==P[i][j];count+=1
            assert sum(Q[i][k]*Q[k][j] for k in range(E))==Q[i][j];count+=1
    return count,E,N,pth,qth


def main():
    count=0
    cases=[(1,3),(1,4),(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)]
    for d,q in cases:
        n,edges,verts,p,cycle=check(d,q)
        count+=n
        print('CASE',d,q,'vertices',verts,'edges',edges,'cut',p,'cycle',cycle,'checks',n)
    print('CHECK_OK',count,'exact-rational assertions across',len(cases),'finite cases')

if __name__=='__main__':
    main()
