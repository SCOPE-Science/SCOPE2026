#!/usr/bin/env python3
"""Exact checks for finite-tree outbreak-size variance asymptotics.

Requires Python 3 standard library. All calculations use integer counts and
fractions; no stochastic simulation is used. The general theorem is proved
separately, not by this bounded enumeration.
"""
from itertools import product
from math import comb
from fractions import Fraction


def edges_from_prufer(seq):
    n = len(seq) + 2
    degree = [1] * n
    for a in seq:
        degree[a] += 1
    edges = []
    for a in seq:
        leaf = next(i for i in range(n) if degree[i] == 1)
        edges.append((leaf, a))
        degree[leaf] -= 1
        degree[a] -= 1
    last = [i for i, d in enumerate(degree) if d == 1]
    edges.append(tuple(last))
    return edges


def component_sizes(n, open_edges):
    parent = list(range(n))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for a, b in open_edges:
        x, y = root(a), root(b)
        if x != y:
            parent[x] = y
    counts = [0] * n
    for i in range(n):
        counts[root(i)] += 1
    return [counts[root(i)] for i in range(n)]


def moments_by_open_count(n, edges):
    m = len(edges)
    h1, h2 = [0] * (m + 1), [0] * (m + 1)
    for state in product((0, 1), repeat=m):
        k = sum(state)
        sizes = component_sizes(n, [e for bit, e in zip(state, edges) if bit])
        h1[k] += sum(sizes)
        h2[k] += sum(s * s for s in sizes)
    return h1, h2


def polys(h, n, m):
    out = [Fraction(0)] * (m + 1)
    for k in range(m + 1):
        for j in range(m - k + 1):
            out[k + j] += Fraction(h[k] * (-1)**j * comb(m-k,j), n)
    return out


def multiply(a,b):
    z = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, u in enumerate(a):
        for j, v in enumerate(b):
            z[i+j] += u*v
    return z


def variance_poly(n, edges):
    h1,h2 = moments_by_open_count(n,edges)
    m=n-1
    a=polys(h1,n,m)
    b=polys(h2,n,m)
    aa=multiply(a,a)
    b.extend([Fraction(0)]*(len(aa)-len(b)))
    return [u-v for u,v in zip(b,aa)]


def w2(n, edges):
    d = [0]*n
    for a,b in edges:
        d[a]+=1;d[b]+=1
    return sum(comb(x,2) for x in d)


def wiener(n, edges):
    adj=[[] for _ in range(n)]
    for a,b in edges:
        adj[a].append(b);adj[b].append(a)
    val=0
    for source in range(n):
        dist=[-1]*n;dist[source]=0;stack=[source]
        for v in stack:
            for x in adj[v]:
                if dist[x]<0:
                    dist[x]=dist[v]+1;stack.append(x)
        val+=sum(dist)
    return val//2


def evalpoly(v,p):
    ans=Fraction(0)
    for coeff in reversed(v):
        ans=ans*p+coeff
    return ans


def run():
    count=0
    for n in range(4,7):
        m=n-1
        star=[(0,i) for i in range(1,n)]
        path=[(i,i+1) for i in range(m)]
        vstar=variance_poly(n,star)
        vpath=variance_poly(n,path)
        small=Fraction(1,100*n**6)
        large=1-small
        for seq in product(range(n),repeat=n-2):
            edges=edges_from_prufer(seq)
            poly=variance_poly(n,edges)
            deg_wedge=w2(n,edges)
            dis_wiener=wiener(n,edges)
            assert poly[0]==0
            assert poly[1]==Fraction(2*m,n)
            assert poly[2]==Fraction(8*deg_wedge,n)-Fraction(4*m*m,n*n)
            assert -sum(i*c for i,c in enumerate(poly)) == dis_wiener
            lo=evalpoly(poly,small)
            hi=evalpoly(poly,large)
            lo_star=evalpoly(vstar,small);lo_path=evalpoly(vpath,small)
            hi_star=evalpoly(vstar,large);hi_path=evalpoly(vpath,large)
            assert lo_path <= lo <= lo_star
            assert hi_star <= hi <= hi_path
            if deg_wedge!=w2(n,star): assert lo<lo_star
            if deg_wedge!=w2(n,path): assert lo>lo_path
            if dis_wiener!=wiener(n,star): assert hi>hi_star
            if dis_wiener!=wiener(n,path): assert hi<hi_path
            count+=1
    vs=variance_poly(4,[(0,1),(0,2),(0,3)])
    vp=variance_poly(4,[(0,1),(1,2),(2,3)])
    # Exact coefficient identity p^2 (1-p) (8-6p-5p^2-p^3)/4:
    required=[Fraction(0),Fraction(0),Fraction(2),Fraction(-14,4),Fraction(1,4),Fraction(1),Fraction(1,4)]
    # Direct expansion: 8 -14p + p^2 +4p^3 +p^4, times p^2 /4.
    assert [a-b for a,b in zip(vs,vp)] == required, ([a-b for a,b in zip(vs,vp)],required)
    assert evalpoly(vs,Fraction(1,2))>evalpoly(vp,Fraction(1,2))
    assert evalpoly(vs,Fraction(9,10))<evalpoly(vp,Fraction(9,10))
    print(f'VERIFY_OK labeled_trees={count} sizes=4..6 endpoint_order_and_both_taylor_coefficients=exact quartic_difference=exact')

if __name__=='__main__':
    run()
