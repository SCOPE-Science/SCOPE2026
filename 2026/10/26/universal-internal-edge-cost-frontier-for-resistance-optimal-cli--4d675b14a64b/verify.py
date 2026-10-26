#!/usr/bin/env python3
"""Independent matrix and budget checks for the clique-bouquet resistance design theorem.

Pure Python 3 standard library; run: python3 verify.py
Finite tests corroborate, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from math import sqrt, isclose
from random import Random


def invert(A):
    n = len(A)
    M = [[A[i][j] for j in range(n)] + [Q(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if M[i][k])
        M[k], M[pivot] = M[pivot], M[k]
        factor = M[k][k]
        M[k] = [t / factor for t in M[k]]
        for i in range(n):
            if i == k:
                continue
            factor = M[i][k]
            M[i] = [u - factor * v for u, v in zip(M[i], M[k])]
    return [row[n:] for row in M]


def weighted_edges(sizes, spokes, rims):
    edges = []
    next_vertex = 1
    for s, a, b in zip(sizes, spokes, rims):
        vertices = list(range(next_vertex, next_vertex + s))
        edges.extend((0, v, a) for v in vertices)
        edges.extend((u, v, b) for k, u in enumerate(vertices) for v in vertices[k+1:])
        next_vertex += s
    return next_vertex, edges


def kirchhoff_matrix(sizes, spokes, rims):
    n, edges = weighted_edges(sizes, spokes, rims)
    H = [[Q(0) for _ in range(n-1)] for _ in range(n-1)]
    for u, v, w in edges:
        if u:
            H[u-1][u-1] += w
        if v:
            H[v-1][v-1] += w
        if u and v:
            H[u-1][v-1] -= w
            H[v-1][u-1] -= w
    R = invert(H)
    total = Q(0)
    for u in range(n):
        for v in range(u+1, n):
            if u == 0:
                total += R[v-1][v-1]
            else:
                total += R[u-1][u-1] + R[v-1][v-1] - 2*R[u-1][v-1]
    return total


def kirchhoff_formula(sizes, spokes, rims):
    N = 1+sum(sizes)
    return sum(Q(N*(s-1))/(a+s*b) + Q(N-s)/a
               for s,a,b in zip(sizes,spokes,rims))


def solution(sizes, spoke_costs, rim_costs, budget):
    N = 1+sum(sizes)
    U, V, classes, S = [], [], [], 0.0
    for s, c, d in zip(sizes, spoke_costs, rim_costs):
        if s == 1 or d*(N-1) >= 2*N*c:
            u = sqrt((N-1)/c)
            v = u
            S += s*sqrt((N-1)*c)
            classes.append('inactive')
        else:
            alpha = s*c-(s-1)*d/2
            beta = (s-1)*d/2
            assert alpha > 0 and beta > 0
            u = sqrt((N-s)/alpha)
            v = sqrt(2*N/d)
            assert v > u
            S += sqrt((N-s)*alpha)+sqrt(N*(s-1)*beta)
            classes.append('active')
        U.append(u)
        V.append(v)
    a = [budget*u/S for u in U]
    b = [(budget*(v-u)/(s*S)) if cl == 'active' else 0.0
         for s,u,v,cl in zip(sizes,U,V,classes)]
    return a,b,S*S/budget,classes,S


def float_inverse(A):
    n = len(A)
    M = [[float(A[i][j]) for j in range(n)] + [float(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        pivot=max(range(k,n), key=lambda i: abs(M[i][k]))
        M[k],M[pivot]=M[pivot],M[k]
        d=M[k][k]
        M[k]=[v/d for v in M[k]]
        for i in range(n):
            if i != k:
                d=M[i][k]
                M[i]=[u-d*v for u,v in zip(M[i],M[k])]
    return [r[n:] for r in M]


def kirchhoff_float_matrix(sizes, a, b):
    n, edges = weighted_edges(sizes,a,b)
    L = [[0.0 for _ in range(n-1)] for _ in range(n-1)]
    for u,v,w in edges:
        if u: L[u-1][u-1] += w
        if v: L[v-1][v-1] += w
        if u and v:
            L[u-1][v-1] -= w
            L[v-1][u-1] -= w
    G = float_inverse(L)
    return n*sum(G[i][i] for i in range(n-1))-sum(sum(row) for row in G)


def check():
    exact_cases = [[1,1],[2,2],[1,2,4],[3,1,2],[4,3],[1,1,1,2],[5,2,3],[4]]
    pairs=0
    for sizes in exact_cases:
        a=[Q(i+2,2*i+7) for i in range(len(sizes))]
        b=[Q(i+1,3*i+11) if s>1 else Q(0) for i,s in enumerate(sizes)]
        direct=kirchhoff_matrix(sizes,a,b)
        formula=kirchhoff_formula(sizes,a,b)
        assert direct==formula, (sizes,direct,formula)
        N=1+sum(sizes)
        pairs+=N*(N-1)//2
    tests=[
        ([1,2,4],[1,1,1],[0,1,1],1),
        ([1,2,4],[1,1,1],[0,3,1],1),
        ([1,2,4],[1,1,1],[0,16/7,1],1),
        ([2,2],[1,1],[3,3],1),
        ([2,2],[1,1],[2.5,2],1),
        ([1,1,1],[1,2,4],[0,0,0],2),
        ([2,2,3],[1,2,0.5],[1,4,3],2),
        ([4,3,2],[3,0.5,2],[8,1,6],3),
    ]
    rng=Random(341)
    for sizes,c,d,B in tests:
        a,b,k,cl,S=solution(sizes,c,d,B)
        cost=sum(s*ci*ai+s*(s-1)*di*bi/2
                 for s,ci,di,ai,bi in zip(sizes,c,d,a,b))
        assert isclose(cost,B,rel_tol=2e-12), (sizes,cost,B)
        calc=kirchhoff_float_matrix(sizes,a,b)
        assert isclose(calc,k,rel_tol=2e-11), (sizes,calc,k)
        for _ in range(32):
            aa=[ai*(.5+rng.random()) for ai in a]
            bb=[(bi*(.2+1.5*rng.random()) if bi else rng.random()*.05) for bi in b]
            co=sum(s*ci*ai+s*(s-1)*di*bi/2 for s,ci,di,ai,bi in zip(sizes,c,d,aa,bb))
            aa=[v*B/co for v in aa]
            bb=[v*B/co for v in bb]
            perturbed=kirchhoff_float_matrix(sizes,aa,bb)
            assert perturbed+1e-8 >= k, (sizes,k,perturbed)
    # Exact optimal homogeneous bow-tie value: 28 + 12 sqrt(5).
    a,b,k,cl,S=solution([2,2],[1,1],[1,1],1)
    assert isclose(k,28+12*sqrt(5),abs_tol=2e-12)
    assert all(cl0=='active' for cl0 in cl)
    # Exact threshold equality at N=8: d/c=16/7, hence rim weight zero.
    assert solution([1,2,4],[1,1,1],[0,16/7,1],1)[1][1]==0
    print('VERIFY_OK: {} exact grounded-matrix cases ({} pair resistances); '
          '{} weighted-cost regimes; {} full-matrix perturbations; '
          'bow-tie radical optimum; sharp mixed-cost threshold'.format(
              len(exact_cases),pairs,len(tests),32*len(tests)))

if __name__=='__main__':
    check()
