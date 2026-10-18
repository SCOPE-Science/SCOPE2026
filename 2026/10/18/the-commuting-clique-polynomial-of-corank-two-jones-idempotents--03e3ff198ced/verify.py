#!/usr/bin/env python3
"""Independent diagram-composition and clique-census checks for planar pairings.

A Jones diagram has n top and n bottom vertices, each of degree one.
This program tests rank, multiplication, idempotence, commutation and
commuting-clique polynomials without using a semigroup presentation.
"""
from functools import lru_cache
from math import comb


def pairing(n, i, j):
    """The single-upper-cup/single-lower-cap diagram, 0-based cup starts."""
    p = [(i, i + 1), (n + j, n + j + 1)]
    top = [x for x in range(n) if x not in (i, i + 1)]
    bottom = [n + x for x in range(n) if x not in (j, j + 1)]
    p.extend(zip(top, bottom))
    return tuple(sorted(tuple(sorted(pair)) for pair in p))


def compose(left, right, n):
    """Stack pairings and forget internal closed loops."""
    parent = list(range(3*n))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def join(x, y):
        parent[root(x)] = root(y)
    for a, b in left:
        join(a, b)
    for a, b in right:
        join(a+n, b+n)
    blocks = {}
    for i in list(range(n)) + list(range(2*n, 3*n)):
        blocks.setdefault(root(i), []).append(i if i<n else i-n)
    assert all(len(v)==2 for v in blocks.values())
    return tuple(sorted(tuple(sorted(v)) for v in blocks.values()))


def rank(diagram, n):
    return sum(a < n <= b for a, b in diagram)


def noncrossing(points):
    """Recursively list all noncrossing matchings in polygon boundary order."""
    if not points:
        yield ()
        return
    a=points[0]
    for k in range(1, len(points), 2):
        b=points[k]
        for L in noncrossing(points[1:k]):
            for R in noncrossing(points[k+1:]):
                yield ((a,b),)+L+R


def all_jones(n):
    for m in noncrossing(tuple(range(2*n))):
        p=[(x if x<n else 3*n-1-x, y if y<n else 3*n-1-y) for x,y in m]
        yield tuple(sorted(tuple(sorted(e)) for e in p))


def poly_add(x,y):
    z=[0]*max(len(x),len(y))
    for i,a in enumerate(x): z[i]+=a
    for i,a in enumerate(y): z[i]+=a
    return tuple(z)


def predicted_polynomial(m):
    p=[(1,), (1,1), (1,4)]
    if m<=2:return p[m]
    for k in range(3,m+1):
        a=poly_add(p[-1],(0,)+p[-2])
        a=poly_add(a, (0,)+tuple(2*u for u in p[-3]))
        p.append(a)
    return p[m]


def actual_cliques(vertices, allowed):
    """Backtrack all cliques from an independently computed adjacency matrix."""
    counts={}
    def search(options,size):
        counts[size]=counts.get(size,0)+1
        for pos,v in enumerate(options):
            search([w for w in options[pos+1:] if allowed[v,w]],size+1)
    search(vertices,0)
    return tuple(counts.get(i,0) for i in range(max(counts)+1))


def check(n, exhaustive_all=False):
    diagrams={(i,j):pairing(n,i,j) for i in range(n-1) for j in range(n-1)}
    if exhaustive_all:
        actual=set(all_jones(n))
        assert len(actual)==comb(2*n,n)//(n+1)
        assert {x for x in actual if rank(x,n)==n-2}==set(diagrams.values())
    idems=[]
    for (i,j), d in diagrams.items():
        idem=(compose(d,d,n)==d)
        assert idem==(abs(i-j)<=1), (n,i,j)
        if idem:idems.append((i,j))
    assert len(idems)==3*n-5
    allowed={}
    ordered_commuting=0
    for i,x in enumerate(idems):
        for j,y in enumerate(idems):
            d1,d2=diagrams[x],diagrams[y]
            product=compose(d1,d2,n)
            backwards=compose(d2,d1,n)
            assert (rank(product,n)==n-2)==(abs(x[1]-y[0])<=1)
            direct=(product==backwards)
            criterion=(x==y or all(abs(a-b)>=2 for a in set(x) for b in set(y)))
            assert direct==criterion, (n,x,y)
            allowed[i,j]=(i!=j and direct)
            ordered_commuting+=direct
    actual=actual_cliques(list(range(len(idems))),allowed)
    prediction=predicted_polynomial(n-1)
    assert actual==prediction,(n,actual,prediction)
    expected=(1 if n==2 else 4 if n==3 else 9*n*n-66*n+129)
    assert ordered_commuting==expected==len(idems)+2*actual[2] if len(actual)>2 else ordered_commuting==expected
    cap=(n//2)
    assert len(actual)-1==cap
    top=(1 if n%2==0 else (3*n-1)//2)
    assert actual[-1]==top
    print('n',n,'idempotents',len(idems),'commuting_pairs',ordered_commuting,'clique_polynomial',actual)


if __name__=='__main__':
    for n in range(2,13):
        check(n,exhaustive_all=(n<=8))
    print('VERIFY_OK_JONES_CORANK_TWO')
