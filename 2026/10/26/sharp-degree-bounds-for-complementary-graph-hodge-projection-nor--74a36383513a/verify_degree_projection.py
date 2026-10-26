"""Exact-rational finite checks for sharp degree bounds on graph Hodge projections.

Run with Python 3: python verify_degree_projection.py
The infinite-graph assertion is established by the accompanying proof, not this test.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def inverse(a):
    n = len(a)
    t = [[F(a[i][j]) for j in range(n)] + [F(i == j) for j in range(n)] for i in range(n)]
    for k in range(n):
        r = next((r for r in range(k, n) if t[r][k]), None)
        assert r is not None, 'disconnected graph'
        t[k], t[r] = t[r], t[k]
        p = t[k][k]
        t[k] = [v / p for v in t[k]]
        for i in range(n):
            if i != k:
                c = t[i][k]
                if c:
                    t[i] = [t[i][j] - c * t[k][j] for j in range(2 * n)]
    return [row[n:] for row in t]


def test_graph(n, edges):
    edges = sorted({tuple(sorted(e)) for e in edges})
    assert all(0 <= u < v < n for u, v in edges)
    assert edges
    deg = [sum(u == v or w == v for u, w in edges) for v in range(n)]
    delta = max(deg)
    m = len(edges)
    B = [[F((u == i) - (v == i)) for u, v in edges] for i in range(n-1)]
    L = [[sum(B[i][k] * B[j][k] for k in range(m)) for j in range(n-1)] for i in range(n-1)]
    invL = inverse(L)
    Q = [[sum(B[i][e] * invL[i][j] * B[j][f] for i in range(n-1) for j in range(n-1)) for f in range(m)] for e in range(m)]
    assert all(Q[i][j] == Q[j][i] for i in range(m) for j in range(m))
    assert all(sum(Q[i][k] * Q[k][j] for k in range(m)) == Q[i][j] for i in range(m) for j in range(m))
    cq = []
    cc = []
    for e, (u, v) in enumerate(edges):
        r = Q[e][e]
        assert F(0) < r <= F(1)
        qe = sum(abs(Q[j][e]) for j in range(m))
        ce = sum(abs(F(j == e) - Q[j][e]) for j in range(m))
        assert qe - ce == 2 * r - 1
        a, b = deg[u] - 1, deg[v] - 1
        if a + b > 0:
            # Sharp lower bound obtained by fixing both edge-endpoint potentials.
            bound = F(a + b, a + b + a * b)
        else:
            bound = F(1)
        assert r >= bound
        if a and b:
            twins = a == b and {w for w in range(n) if w != v and (min(u,w),max(u,w)) in edges and w != u} == {w for w in range(n) if w != u and (min(v,w),max(v,w)) in edges and w != v}
            assert (r == bound) == twins
        else:
            assert r == F(1)
        cq.append(qe)
        cc.append(ce)
    gap = max(cq) - max(cc)
    assert gap >= F(3-delta, delta+1), (n,edges,gap,delta)
    return gap, max(cq), max(cc), delta, m


def kgraph(n):
    return n, list(combinations(range(n), 2))


def cycle(n):
    return n, [(i, (i+1)%n) for i in range(n)]


def path(n):
    return n, [(i, i+1) for i in range(n-1)]


def star(n):
    return n, [(0, i) for i in range(1,n)]


def book(m):
    return m+2, [(0,1)] + [(u, v) for u in (0,1) for v in range(2,m+2)]


def gp(n,k=2):
    return 2*n, ([(i,(i+1)%n) for i in range(n)]
                 + [(n+i, n+(i+k)%n) for i in range(n)]
                 + [(i,n+i) for i in range(n)])


def is_connected(n, edges):
    s={0}
    while True:
        ns=s|{v for u,v in edges if u in s}|{u for u,v in edges if v in s}
        if ns==s:break
        s=ns
    return len(s)==n


def main():
    fixtures=[]
    fixtures += [kgraph(n) for n in range(2,10)]
    fixtures += [cycle(n) for n in range(3,11)]
    fixtures += [path(n) for n in range(2,11)]
    fixtures += [star(n) for n in range(3,11)]
    fixtures += [book(m) for m in range(2,9)]
    fixtures += [gp(n) for n in range(5,10)]
    rng=Random(230512582)
    for n in range(4,10):
        for t in range(12):
            e=[(i,j) for i in range(n) for j in range(i+1,n) if rng.random()<0.42]
            if not e or not is_connected(n,e):continue
            if max(sum(i==x or j==x for i,j in e) for x in range(n))>4:continue
            fixtures.append((n,e))
    count=0; totalcols=0
    for n,es in fixtures:
        gap,q,c,degree,cols=test_graph(n,es)
        count+=1; totalcols+=cols
        if len(es)==n*(n-1)//2:
            assert gap==F(3-degree,degree+1)
        if len(es)==1+2*(n-2) and (0,1) in es and all((u,j) in es for u in (0,1) for j in range(2,n)):
            assert gap==F(3-degree,degree+1)
    assert test_graph(*kgraph(4))[0] == 0
    assert test_graph(*kgraph(5))[0] == F(-1,5)
    print('PASS exact rational graphs=',count,'columns=',totalcols)
    print('PASS K4 equality and K5 sharp reversal, local twin resistance equality')


if __name__=='__main__':
    main()
