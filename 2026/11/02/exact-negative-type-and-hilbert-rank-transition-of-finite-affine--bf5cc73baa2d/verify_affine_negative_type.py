#!/usr/bin/env python3
"""Independent finite incidence, shortest-path, and Gram-rank checks.

Requires only the Python 3 standard library. All incidence and graph distances
are constructed from finite-field arithmetic independently of spectral formulas.
The checks are illustrative finite tests; the mathematical proof covers all
finite affine planes, including those lacking field coordinates.
"""
from collections import deque
from math import log2, sqrt


def field(q):
    if q == 4:
        # F4=F2[u]/(u^2+u+1): elements 0,1,u,1+u as binary masks.
        add = lambda a, b: a ^ b
        def mul(a, b):
            z = 0
            for i in range(2):
                for j in range(2):
                    if ((a >> i) & 1) and ((b >> j) & 1):
                        z ^= (1 << (i + j))
            if z & 4:
                z ^= 7  # u^2=u+1, so u^2+u+1=0.
            return z
        return add, mul
    assert q in (2, 3, 5, 7), q
    return (lambda a, b: (a+b) % q,
            lambda a, b: (a*b) % q)


def incidence(q):
    add, mul = field(q)
    pts = [(x, y) for x in range(q) for y in range(q)]
    # Label parallel classes 0,...,q-1 (slopes) and q (vertical).
    lines = [(s, t) for s in range(q+1) for t in range(q)]
    P, L = len(pts), len(lines)
    B = [[0] * L for _ in range(P)]
    for i, (x, y) in enumerate(pts):
        for j, (s, t) in enumerate(lines):
            B[i][j] = int(x == t if s == q else y == add(mul(s, x), t))
    return pts, lines, B


def shortest_paths(B):
    P, L = len(B), len(B[0]); N=P+L
    adj = [[] for _ in range(N)]
    for i in range(P):
        for j in range(L):
            if B[i][j]:
                adj[i].append(P+j); adj[P+j].append(i)
    dist = [[-1]*N for _ in range(N)]
    for i in range(N):
        dist[i][i]=0; Q=deque([i])
        while Q:
            v=Q.popleft()
            for w in adj[v]:
                if dist[i][w] < 0:
                    dist[i][w]=dist[i][v]+1; Q.append(w)
    return dist


def eigenvalues_jacobi(M):
    # Symmetric Jacobi rotations, norm-based stopping criterion.
    n=len(M); A=[list(row) for row in M]
    for _ in range(60*n*n):
        i, j=max(((i,j) for i in range(n) for j in range(i+1,n)),
                 key=lambda t:abs(A[t[0]][t[1]]))
        if abs(A[i][j]) < 1.e-11:
            return sorted(A[i][i] for i in range(n))
        tau=(A[j][j]-A[i][i])/(2*A[i][j])
        u=(1. if tau >=0 else -1.)/(abs(tau)+sqrt(1+tau*tau))
        c=1/sqrt(1+u*u); s=u*c
        aii, ajj, aij=A[i][i],A[j][j],A[i][j]
        A[i][i]=aii-u*aij; A[j][j]=ajj+u*aij
        A[i][j]=A[j][i]=0.
        for k in range(n):
            if k==i or k==j: continue
            aki,akj=A[k][i], A[k][j]
            A[k][i]=A[i][k]=c*aki-s*akj
            A[k][j]=A[j][k]=s*aki+c*akj
    raise RuntimeError('Jacobi method failed to converge')


def gram_eigenvalues(dist, p):
    n=len(dist)
    a=n-1
    D=[[0. if not dist[i][j] else float(dist[i][j]**p)
        for j in range(n)] for i in range(n)]
    # The zero-sum basis e_i-e_a gives the exact centered quadratic form.
    G=[[-.5*(D[i][j]-D[i][a]-D[a][j]) for j in range(a)] for i in range(a)]
    return eigenvalues_jacobi(G)


def check(q):
    points,lines,B=incidence(q)
    P,L=len(points),len(lines)
    assert P==q*q and L==q*(q+1)
    for i in range(P):
        assert sum(B[i])==q+1
        for j in range(P):
            assert sum(B[i][k]*B[j][k] for k in range(L)) == (q+1 if i==j else 1)
    for j in range(L):
        assert sum(B[i][j] for i in range(P))==q
    dist=shortest_paths(B); N=P+L
    for i in range(N):
        for j in range(N):
            if i==j: expected=0
            elif i<P and j<P: expected=2
            elif i>=P and j>=P:
                expected=4 if lines[i-P][0]==lines[j-P][0] else 2
            else:
                pi,lj=(i,j-P) if i<P else (j,i-P)
                expected=1 if B[pi][lj] else 3
            assert dist[i][j]==expected, (q,i,j,dist[i][j],expected)
    p=log2(q/(q-1))
    tol=3e-7
    lower=gram_eigenvalues(dist, .8*p)
    edge=gram_eigenvalues(dist, p)
    upper=gram_eigenvalues(dist, 1.08*p)
    assert min(lower) > tol, (q,min(lower))
    zero=sum(abs(x)<tol for x in edge)
    expected_nullity=(5 if q==2 else q)
    assert zero==expected_nullity, (q,zero,expected_nullity,edge[:15])
    assert min(edge)>-tol, (q,min(edge))
    assert min(upper)<-tol, (q,min(upper))
    # Explicit endpoint equality supported on two parallel line classes.
    coeff=[0.]*N
    for j,(s,t) in enumerate(lines):
        if s==0: coeff[P+j]=1.
        if s==1: coeff[P+j]=-1.
    assert sum(coeff)==0
    quadratic=sum(coeff[i]*coeff[j]*(dist[i][j]**p)
                  for i in range(N) for j in range(N))
    assert abs(quadratic)<1e-7, (q,quadratic)
    print('AFFINE_OK', 'order',q,'vertices',N,'exponent',f'{p:.12f}',
          'endpoint_nullity',zero,'critical_Hilbert_rank',N-1-zero,
          'lower_strict',f'{min(lower):.4g}',
          'upper_indefinite',f'{min(upper):.4g}')

for q in (2,3,4,5,7):
    check(q)
print('ALL_AFFINE_NEGATIVE_TYPE_CHECKS_OK')
