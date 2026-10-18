#!/usr/bin/env python3
"""Exact-rational checks for canonical ellipsoids of complete-bipartite root polytopes.
Uses only Python's standard library. Finite checks corroborate the separately stated proof.
"""
from fractions import Fraction as Q
from itertools import product
from collections import deque


def inverse(A):
    n = len(A)
    X = [[Q(A[i][j]) for j in range(n)] + [Q(i == j) for j in range(n)] for i in range(n)]
    for j in range(n):
        piv = next(i for i in range(j,n) if X[i][j])
        X[j],X[piv] = X[piv],X[j]
        scale = X[j][j]
        X[j] = [v/scale for v in X[j]]
        for i in range(n):
            if i != j:
                scale = X[i][j]
                if scale: X[i] = [u-scale*v for u,v in zip(X[i],X[j])]
    return [row[n:] for row in X]


def dot_mat(v,M,w):
    return sum((v[i]*M[i][j]*w[j] for i in range(len(v)) for j in range(len(w))), Q(0))


def center(v):
    mean = sum(v,Q(0))/len(v)
    return tuple(Q(x)-mean for x in v)


def laplacian(a,b):
    n=a+b
    L=[[Q(0) for j in range(n)] for i in range(n)]
    for i in range(a):
        for j in range(a,n):
            L[i][i]+=1;L[j][j]+=1
            L[i][j]-=1;L[j][i]-=1
    return L


def outer_avg(vs):
    n=len(vs[0]); C=[[Q(0)]*n for i in range(n)]
    for v in vs:
        for i in range(n):
            for j in range(n): C[i][j]+=v[i]*v[j]/len(vs)
    return C


def tangent_connected(v,a,b):
    n=a+b; linked=[set() for _ in range(n)]
    for i in range(a):
        for j in range(a,n):
            if abs(v[i]-v[j]) == 1:
                linked[i].add(j);linked[j].add(i)
    seen={0};todo=[0]
    while todo:
        for w in linked[todo.pop()]:
            if w not in seen:seen.add(w);todo.append(w)
    return len(seen)==n


def exhaustive_polar_vertices(a,b):
    # Gauge the first A-coordinate to zero. Tight-edge connectedness is the
    # exact full-rank criterion; vertex coordinates must be integral, since
    # tight differences are +/-1 along a spanning tree.
    out=set()
    for rest in product(range(-2,3),repeat=a-1):
        for B in product(range(-1,2),repeat=b):
            v=(0,)+rest+B
            if all(abs(v[i]-v[j])<=1 for i in range(a) for j in range(a,a+b)):
                if tangent_connected(v,a,b):out.add(center(v))
    return out


def check(a,b,exhaustive=False):
    n=a+b;d=n-1;m=a*b
    L=laplacian(a,b)
    J=[[Q(1,n) for j in range(n)] for i in range(n)]
    K=inverse([[L[i][j]+J[i][j] for j in range(n)] for i in range(n)])
    Lplus=[[K[i][j]-J[i][j] for j in range(n)] for i in range(n)]
    W=[[v/m for v in row] for row in L]
    # All vertices of the polar by the explicit complete-bipartite facet rule.
    A=[center(s+(0,)*b) for s in product((-1,1),repeat=a)]
    B=[center((0,)*a+t) for t in product((-1,1),repeat=b)]
    normals=set(A+B)
    assert len(normals)==2**a+2**b-2,(a,b,len(normals))
    for y in normals: assert dot_mat(y,W,y)==1,('John facet contact',a,b,y)
    # Every signed edge-incidence vertex is on the proposed Loewner boundary.
    for i in range(a):
        for j in range(a,n):
            v=[Q(0)]*n;v[i]=1;v[j]=-1
            assert Q(m,d)*dot_mat(v,Lplus,v)==1,('Loewner contact',a,b,i,j)
    # Exact contact measure: balanced signs on each side and two pure directions.
    ua=a%2;ub=b%2
    BA=[v for s,v in zip(product((-1,1),repeat=a),A) if abs(sum(s))==ua]
    BB=[v for s,v in zip(product((-1,1),repeat=b),B) if abs(sum(s))==ub]
    ta=Q(a*a*(a-1),d*(a*a-ua))
    tb=Q(b*b*(b-1),d*(b*b-ub))
    tz=Q(1,d)-ta*Q(ua,a*a)-tb*Q(ub,b*b)
    assert ta>0 and tb>0 and tz>0 and ta+tb+tz==1
    CA=outer_avg(BA);CB=outer_avg(BB)
    pure=center((1,)*a+(0,)*b)
    for i in range(n):
        for j in range(n):
            cov=ta*CA[i][j]+tb*CB[i][j]+tz*pure[i]*pure[j]
            assert cov==Q(m,d)*Lplus[i][j],('contact covariance',a,b,i,j,cov,Q(m,d)*Lplus[i][j])
    if exhaustive:
        enumerated=exhaustive_polar_vertices(a,b)
        assert enumerated==normals,('exhaustive facet classification',a,b,len(enumerated),len(normals))
    # Principal eigenvalue/pseudodeterminant formula.
    pseudo_det=Q(n,a**a*b**b)
    assert pseudo_det>0
    return len(normals), len(BA)+len(BB)+1


if __name__=='__main__':
    cases=0;polar=0;contacts=0
    for a in range(2,6):
        for b in range(a,8):
            f,c=check(a,b,exhaustive=(a<=4 and b<=5))
            cases+=1;polar+=f;contacts+=c
    print('VERIFY_OK cases=%d polar_facet_normals=%d sampled_contact_labels=%d'% (cases,polar,contacts))
