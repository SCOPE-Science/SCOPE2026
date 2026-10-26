#!/usr/bin/env python3
"""Exact independent finite checks of weighted rook-graph edge projection formulas.
Uses only Python standard library; finite checks supplement, not replace, the proof.
"""
from fractions import Fraction as F
from itertools import combinations


def inverse(mat):
    n = len(mat)
    a = [list(row) + [F(int(i == j)) for j in range(n)] for i, row in enumerate(mat)]
    for j in range(n):
        k = next((k for k in range(j, n) if a[k][j]), None)
        assert k is not None, "singular anchored Laplacian"
        a[j], a[k] = a[k], a[j]
        div = a[j][j]
        a[j] = [z / div for z in a[j]]
        for i in range(n):
            if i != j and a[i][j]:
                q = a[i][j]
                a[i] = [x - q * y for x, y in zip(a[i], a[j])]
    return [row[n:] for row in a]


def graph(a, b, root_c, root_d):
    vertices = [(i,j) for i in range(a) for j in range(b)]
    ix = {v: k for k, v in enumerate(vertices)}
    edges = []
    for j in range(b):
        for u, v in combinations(range(a), 2):
            edges.append((ix[(u,j)], ix[(v,j)], 'A', root_c))
    for i in range(a):
        for u, v in combinations(range(b), 2):
            edges.append((ix[(i,u)], ix[(i,v)], 'B', root_d))
    # Deliberate orientation reversals leave the asserted row norm invariant.
    edges = [(v,u,t,w) if e%3 == 1 else (u,v,t,w)
             for e,(u,v,t,w) in enumerate(edges)]
    n = a*b
    lap = [[F(0) for _ in range(n)] for _ in range(n)]
    for u,v,_,wroot in edges:
        w=F(wroot*wroot)
        lap[u][u] += w;lap[v][v] += w
        lap[u][v] -= w;lap[v][u] -= w
    t = inverse([[lap[i][j] + F(1,n) for j in range(n)] for i in range(n)])
    g = [[t[i][j] - F(1,n) for j in range(n)] for i in range(n)]
    p = []
    for u,v,typ,scale in edges:
        row=[]
        for x,y,_,s in edges:
            row.append(F(scale*s)*(g[u][x]-g[u][y]-g[v][x]+g[v][y]))
        p.append(row)
    return edges,p


def verify(a,b,sc,sd):
    edges,p=graph(a,b,sc,sd)
    c,d=F(sc*sc),F(sd*sd)
    kappa=F(sc*sd)/(a*c+b*d)
    sums={'A':(F(2*(a-1),a),F(2*(b-1))*kappa),
          'B':(F(2*(b-1),b),F(2*(a-1))*kappa)}
    cnt=0
    for i,e in enumerate(edges):
        own,cross=sums[e[2]]
        actual_own=sum(abs(p[i][j]) for j,z in enumerate(edges) if z[2]==e[2])
        actual_cross=sum(abs(p[i][j]) for j,z in enumerate(edges) if z[2]!=e[2])
        assert actual_own == own, (a,b,c,d,e,actual_own,own)
        assert actual_cross == cross,(a,b,c,d,e,actual_cross,cross)
        cnt+=2
        for j in range(len(edges)):
            assert p[i][j]==p[j][i]
            cnt+=1
    assert sum(p[i][i] for i in range(len(edges)))==a*b-1
    cnt+=1
    if a*b<=9:
        for i in range(len(edges)):
            for j in range(len(edges)):
                assert sum(p[i][k]*p[k][j] for k in range(len(edges)))==p[i][j]
                cnt+=1
    return cnt


def main():
    c=0; configurations=0
    for a,b in ((2,2),(2,3),(3,2),(2,4),(4,2),(3,3),(2,5),(3,4),(4,3),(4,4),(5,2)):
        for sc,sd in ((1,1),(1,2),(2,1),(2,3),(3,2)):
            c+=verify(a,b,sc,sd);configurations+=1
    print(f"PASS: {c} exact Fraction equalities across {configurations} independently constructed weighted rook graphs.")
    print("Universal formulas and optimizers require the algebraic proof in RESULT.md.")


if __name__=='__main__':
    main()
