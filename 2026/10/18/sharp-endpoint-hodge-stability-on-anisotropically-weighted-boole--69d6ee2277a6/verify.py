#!/usr/bin/env python3
"""Exact-arithmetic matrix checks for weighted-cube gradient projections.

Run with Python 3; uses only the standard library. These finite checks supplement,
not replace, the analytical proof for all dimensions and positive weights.
"""
from fractions import Fraction as F
from math import isqrt


def invert(a):
    n = len(a)
    h = [[F(t) for t in a[i]] + [F(int(i==j)) for j in range(n)] for i in range(n)]
    for j in range(n):
        p = next(i for i in range(j, n) if h[i][j])
        h[j], h[p] = h[p], h[j]
        scale = h[j][j]
        h[j] = [z / scale for z in h[j]]
        for i in range(n):
            if i != j and h[i][j]:
                b = h[i][j]
                h[i] = [h[i][k] - b*h[j][k] for k in range(2*n)]
    return [row[n:] for row in h]


def check_dimension(weight_roots):
    # Positive conductances c_i = weight_roots[i]^2 make all projections rational.
    d = len(weight_roots)
    n = 1 << d
    c = [k*k for k in weight_roots]
    edges = [(i,x,x^(1<<i)) for i in range(d) for x in range(n) if not (x & (1<<i))]
    m = len(edges)
    # Ground last vertex: this computes B L^+ B^T without forming a pseudoinverse.
    L = [[F(0) for _ in range(n-1)] for _ in range(n-1)]
    for i,x,y in edges:
        if x < n-1: L[x][x] += c[i]
        if y < n-1: L[y][y] += c[i]
        if x < n-1 and y < n-1:
            L[x][y] -= c[i]; L[y][x] -= c[i]
    G = invert(L)
    diff = []
    for i,x,y in edges:
        v = [F(0) for _ in range(n-1)]
        if x < n-1: v[x] = -1
        if y < n-1: v[y] = 1
        diff.append(v)
    # Rows of grounded resolvent with edge incidence, never Walsh transform.
    X = [[sum(G[u][v]*diff[e][v] for v in range(n-1)) for u in range(n-1)] for e in range(m)]
    P = [[F(weight_roots[edges[e][0]]*weight_roots[edges[f][0]])*
         sum(diff[e][u]*X[f][u] for u in range(n-1)) for f in range(m)] for e in range(m)]
    checks = 0
    for e,(i,z,_) in enumerate(edges):
        pred = F(1)+sum(F(weight_roots[i]*weight_roots[j], c[i]+c[j]) for j in range(d) if i!=j)
        for j in range(d):
            want = F(1) if i==j else F(weight_roots[i]*weight_roots[j], c[i]+c[j])
            got = sum(abs(P[e][f]) for f,(j2,_,_) in enumerate(edges) if j2==j)
            assert got == want, ('directional row mass',d,weight_roots,e,j,got,want)
            checks += 1
        assert sum(abs(x) for x in P[e])==pred
        checks+=1
        for f,(j,x,_) in enumerate(edges):
            # Exact sign theorem: parallel entries strictly positive;
            # transverse signs depend only on coordinate halfspaces.
            expected = 1 if i==j or (((x>>i)+(z>>j))&1)==0 else -1
            assert P[e][f] * expected > 0, ('entry sign',d,weight_roots,e,f,P[e][f])
            assert P[e][f] == P[f][e],('symmetry',e,f)
            checks+=2
    # Orthogonal projection identity independently reconstructed from finite graphs.
    for e in range(m):
        for f in range(m):
            assert sum(P[e][k]*P[k][f] for k in range(m))==P[e][f]
            checks+=1
    return checks


def main():
    cases = [
        (1,), (2,),
        (1,1), (1,3), (2,7),
        (1,1,1), (1,2,5), (2,3,9),
        (1,1,1,1), (1,2,3,4), (1,4,9,16),
        (1,1,1,1,1),
    ]
    count = 0
    for c in cases:
        x = check_dimension(c)
        count += x
        print('PASS dimension',len(c),'roots',c,'assertions',x)
    print('PASS total',count,'exact-rational assertions over',len(cases),'graphs')

if __name__ == '__main__': main()
