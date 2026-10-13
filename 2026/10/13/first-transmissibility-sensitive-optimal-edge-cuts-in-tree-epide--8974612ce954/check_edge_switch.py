#!/usr/bin/env python3
"""Exhaustive exact check of the first parameter-sensitive edge intervention trees.

Requires only Python 3 standard library. Prüfer words enumerate every labeled tree;
center-rooted canonical strings quotient by vertex relabeling.  All dominance
certificates use nonnegative integer coefficients in the basis
p^j (1-p)^(d-j), which is nonnegative on 0<=p<=1.
"""
from collections import deque, Counter
from itertools import product
from math import comb


def prufer_edges(word, n):
    deg = [1] * n
    for x in word: deg[x] += 1
    edges = []
    for x in word:
        y = min(i for i, d in enumerate(deg) if d == 1)
        edges.append((x,y))
        deg[x] -= 1
        deg[y] -= 1
    remaining = [i for i, d in enumerate(deg) if d == 1]
    assert len(remaining) == 2
    edges.append(tuple(remaining))
    return tuple(edges)


def adjacency(edges, n):
    g = [[] for _ in range(n)]
    for x, y in edges:
        g[x].append(y); g[y].append(x)
    return g


def canonical(g):
    """Unrooted-tree isomorphism string via leaf peeling and rooted AHU coding."""
    n = len(g)
    if n == 1: return '()'
    degree = list(map(len,g)); remaining = set(range(n))
    while len(remaining) > 2:
        leaves = [v for v in remaining if degree[v] <= 1]
        assert leaves
        for v in leaves: remaining.remove(v)
        for v in leaves:
            for w in g[v]: degree[w] -= 1
    def rooted(v,parent):
        return '(' + ''.join(sorted(rooted(w,v) for w in g[v] if w != parent)) + ')'
    if len(remaining) == 1:
        return 'U' + rooted(next(iter(remaining)),-1)
    a,b = sorted(remaining)
    left,right = sorted([rooted(a,b), rooted(b,a)])
    return 'V' + left + right


def distances(g,root,ban=None):
    out = {root:0}; queue = deque([root])
    while queue:
        x=queue.popleft()
        for y in g[x]:
            if ban is not None and ((x,y)==ban or (y,x)==ban):continue
            if y not in out:out[y]=out[x]+1;queue.append(y)
    return out


def edge_polys(g):
    """For each edge e, F_e(p)=sum_{u|v separated} p^(dist(u,v)-1)."""
    n = len(g)
    all_dist = [distances(g,v) for v in range(n)]
    assert all(len(r)==n for r in all_dist)
    out = {}
    for a in range(n):
        for b in g[a]:
            if b<a:continue
            aa=distances(g,a,(a,b)); bb=set(range(n))-set(aa)
            assert len(aa)+len(bb)==n and b in bb
            c=[0]*(n-1)
            for x in aa:
                for y in bb: c[all_dist[x][y]-1]+=1
            assert sum(c)==len(aa)*len(bb)
            # Independent convolution using endpoint-rooted distance histograms.
            ax=Counter(aa.values()); by=Counter(distances(g,b,(a,b)).values())
            conv=[0]*(n-1)
            for i,xi in ax.items():
                for j,yj in by.items(): conv[i+j]+=xi*yj
            assert c==conv
            out[(a,b)]=tuple(c)
    assert len(out)==n-1
    return out


def bernstein_diff(a,b):
    d=len(a)-1
    # p^k = sum_{j=k}^d binom(d-k,j-k) p^j(1-p)^(d-j)
    return tuple(sum((a[k]-b[k])*comb(d-k,j-k) for k in range(j+1)) for j in range(d+1))


def certificate(g):
    poly=edge_polys(g)
    return [e for e,a in poly.items() if all(min(bernstein_diff(a,b))>=0 for b in poly.values())]


def analyze():
    expected={2:1,3:1,4:2,5:3,6:6,7:11,8:23}
    exceptions={}
    for n in range(2,9):
        reps={}
        for word in product(range(n),repeat=n-2):
            g=adjacency(prufer_edges(word,n),n)
            key=canonical(g)
            reps.setdefault(key,g)
        assert len(reps)==expected[n],(n,len(reps))
        bad=[(key,g) for key,g in reps.items() if not certificate(g)]
        if n<=7:assert len(bad)==0,(n,[x[0] for x in bad])
        if n==8:
            assert len(bad)==2,(n,len(bad))
            exceptions={key:g for key,g in bad}
        print('order',n,'Prufer_codes',n**(n-2),'unlabeled_trees',len(reps),'switch_candidates',len(bad))
    return exceptions


def verify_witness(edges, n, center, alternative, root_poly, alt_poly, twin_alternative=()):
    g=adjacency(edges,n); p=edge_polys(g)
    ee=lambda u,v: tuple(sorted((u,v)))
    c,a=ee(*center),ee(*alternative)
    assert p[c]==root_poly,(c,p[c])
    assert p[a]==alt_poly,(a,p[a])
    twin={ee(*edge) for edge in twin_alternative}
    for e in twin:assert p[e]==alt_poly,(e,p[e])
    for e,v in p.items():
        if e not in ({c,a}|twin):assert all(x>=y for x,y in zip(p[c],v)), (e,v)
    return canonical(g)


def main():
    exceptions=analyze()
    # The first exceptional tree has one degree-three branch and a long tail.
    e1=((0,5),(1,0),(1,2),(2,3),(2,4),(5,6),(6,7))
    r1=(1,2,4,4,3,2,0);a1=(1,3,3,3,3,2,0)
    k1=verify_witness(e1,8,(1,0),(1,2),r1,a1)
    # The second exceptional tree has two degree-three branching vertices.
    e2=((0,5),(1,0),(1,2),(2,3),(2,4),(5,6),(5,7))
    r2=(1,2,5,4,4,0,0);a2=(1,3,3,4,4,0,0)
    k2=verify_witness(e2,8,(1,0),(1,2),r2,a2,twin_alternative=[(0,5)])
    p2=edge_polys(adjacency(e2,8))
    assert p2[(0,5)]==a2
    assert set(exceptions)=={k1,k2},(set(exceptions),{k1,k2})
    # Differences (alternative - center): p-p^2-p^3 and p-2p^2.
    assert tuple(x-y for x,y in zip(a1,r1))==(0,1,-1,-1,0,0,0)
    assert tuple(x-y for x,y in zip(a2,r2))==(0,1,-2,0,0,0,0)
    print('exception_canonical_codes', sorted(exceptions))
    print('thresholds', '(sqrt(5)-1)/2', '1/2')
    print('VERIFY_OK')

if __name__=='__main__':main()
