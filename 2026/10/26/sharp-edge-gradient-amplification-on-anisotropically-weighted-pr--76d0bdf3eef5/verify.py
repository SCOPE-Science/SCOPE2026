#!/usr/bin/env python3
"""Standalone exact-rational finite checks for edge-gradient projection on clique products.

Python standard library only. These tests are checks, not a proof for every tuple size.
"""
from fractions import Fraction as F
from itertools import product
from math import prod, sqrt


def inverse(a):
    n=len(a)
    x=[[F(a[i][j]) for j in range(n)]+[F(int(i==j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        r=next((i for i in range(k,n) if x[i][k]),None)
        assert r is not None, 'singular gauge Laplacian'
        x[k],x[r]=x[r],x[k]
        z=x[k][k]
        for j in range(2*n): x[k][j]/=z
        for i in range(n):
            if i==k or not x[i][k]:continue
            t=x[i][k]
            for j in range(2*n):x[i][j]-=t*x[k][j]
    return [v[n:] for v in x]


def expected(q,s):
    return [F(2*(qi-1),qi)+sum(F(2*(qj-1)*s[i]*s[j],qi*s[i]**2+qj*s[j]**2)
                    for j,qj in enumerate(q) if j!=i) for i,qi in enumerate(q)]


def full_check(q,s):
    n=len(q); xs=list(product(*(range(v) for v in q)))
    N=len(xs); ix={v:i for i,v in enumerate(xs)}
    es=[]
    for u in xs:
        for j in range(n):
            for value in range(u[j]+1,q[j]):
                w=list(u);w[j]=value
                es.append((ix[u],ix[tuple(w)],j))
    M=len(es)
    L=[[F(1,N) for _ in range(N)] for _ in range(N)]
    for a,b,j in es:
        c=s[j]**2
        L[a][a]+=c; L[b][b]+=c
        L[a][b]-=c;L[b][a]-=c
    G=inverse(L)
    P=[[F(0) for _ in range(M)] for _ in range(M)]
    for i,(a,b,j) in enumerate(es):
        for k,(u,v,h) in enumerate(es):
            P[i][k]=s[j]*s[h]*(G[a][u]-G[a][v]-G[b][u]+G[b][v])
    norms=expected(q,s)
    for i,(a,b,j) in enumerate(es):
        assert sum(abs(v) for v in P[i])==norms[j], (q,s,i,norms[j])
        assert P[i][i]>=0
        assert sum(P[i][k]**2 for k in range(M))==P[i][i]
        for k in range(M):assert P[i][k]==P[k][i]
    assert max(sum(abs(v) for v in row) for row in P)==max(norms)
    return M+M*M


def optimal_check(q):
    r=F(0)
    for i,qi in enumerate(q):
        F_i=2*(qi-1)/qi+sum((qj-1)/(qi*qj)**.5 for j,qj in enumerate(q) if j!=i)
        if qi==min(q):assert F_i>=r-1e-11
        r=max(r,F_i)
    # When q_i differ, smaller alphabets give strictly greater globally optimal rows.
    a=[2*(qi-1)/qi+sum((qj-1)/(qi*qj)**.5 for j,qj in enumerate(q) if j!=i)
       for i,qi in enumerate(q)]
    for i in range(len(q)):
        for j in range(len(q)):
            if q[i]<q[j]:assert a[i]>a[j]
            elif q[i]==q[j]:assert abs(a[i]-a[j])<1e-10
    return len(q)**2


def run():
    cases=[([2,2],[1,2]),([2,3],[1,3]),([3,3],[2,1]),([2,4],[1,2]),
           ([2,2,2],[1,2,3]),([2,2,3],[1,2,2]),([2,3,3],[2,1,3]),
           ([2,2,2,2],[1,1,2,3]),([2,3,4],[1,2,2]),([3,2,2],[2,3,1])]
    tests=0
    for q,s in cases:
        tests+=full_check(q,s)
        tests+=optimal_check(q)
    # Homogeneous Hamming graph family and dimensional scaling, exact arithmetic.
    for d in range(2,18):
        for q in range(2,21):
            rr=expected([q]*d,[1]*d)
            assert len(set(rr))==1
            assert rr[0]==F((d+1)*(q-1),q)
            tests+=1
    for q in [(2,3,4),(2,2,2,4),(2,3,5,7),(5,6,7,8),(2,2,3,9)]:
        tests+=optimal_check(q)
    print('PASS: %d registered finite check units (exact-rational matrix checks and auxiliary numerical comparisons)' % tests)

if __name__=='__main__':run()
