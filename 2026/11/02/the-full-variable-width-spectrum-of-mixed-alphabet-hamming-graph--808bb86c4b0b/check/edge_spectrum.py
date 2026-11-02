#!/usr/bin/env python3
"""Exhaustive clique-capacity and monochromatic-diameter checks.

Uses only Python's standard library. Edge colours are inferred from maximal
cliques and not read from the Cartesian coordinate construction.
"""
from itertools import product, combinations
from collections import Counter, deque
from math import comb


def make_graph(alph):
    vertices = list(product(*(range(q) for q in alph)))
    neighbors = {a:set() for a in vertices}
    for i,a in enumerate(vertices):
        for b in vertices[i+1:]:
            if sum(x!=y for x,y in zip(a,b)) == 1:
                neighbors[a].add(b)
                neighbors[b].add(a)
    return neighbors


def maximal_cliques(neighbors):
    def bk(R,P,X):
        if not P and not X:
            yield R
            return
        pivot = max(P|X, key=lambda u:len(P&neighbors[u]), default=None)
        candidates = P-(neighbors[pivot] if pivot is not None else set())
        for v in tuple(candidates):
            yield from bk(R|{v},P&neighbors[v],X&neighbors[v])
            P.remove(v)
            X.add(v)
    yield from bk(set(),set(neighbors),set())


def colored_diameters(neighbors,capacity,k,color):
    nodes=set(neighbors)
    colored = {u:set() for u in nodes}
    for (u,v),cap in capacity.items():
        if min(cap,k)==color:
            colored[u].add(v)
            colored[v].add(u)
    out=[]
    while nodes:
        seed=next(iter(nodes)); visited={seed}; queue=deque([seed])
        while queue:
            v=queue.popleft()
            for w in colored[v]-visited:
                visited.add(w);queue.append(w)
        nodes-=visited
        diam=0
        for root in visited:
            dist={root:0};queue=deque([root])
            while queue:
                v=queue.popleft()
                for w in colored[v]:
                    if w not in dist:
                        dist[w]=dist[v]+1;queue.append(w)
            assert set(dist)==visited
            diam=max(diam,max(dist.values()))
        out.append(diam)
    return set(out)


def check_case(alph,k):
    G=make_graph(alph)
    cap={(u,v):0 for u in G for v in G[u] if u<v}
    for clique in maximal_cliques(G):
        for u,v in combinations(sorted(clique),2):
            assert (u,v) in cap
            cap[(u,v)]=max(cap[(u,v)],len(clique))
    assert all(x>=2 for x in cap.values())
    actual=Counter(min(x,k) for x in cap.values())
    bins=Counter(min(q,k) for q in alph)
    n=len(G)
    expected=Counter()
    for q in alph: expected[min(q,k)]+=n*(q-1)//2
    assert actual==expected,(alph,k,actual,expected)
    diameters={}
    for color in range(2,k+1):
        Ds=colored_diameters(G,cap,k,color)
        assert Ds=={bins[color]},(alph,k,color,Ds,bins[color])
        diameters[color]=bins[color]
    print(f'PASS alph={alph} width={k} vertices={n} alphabet_bins={sorted(bins.items())} semantic_colored_diameters={diameters}')
    return 1

cases=[(3,),(4,),(5,),(2,2),(2,3),(2,4),(3,3),(3,4),(2,3,4),(2,2,3),(2,4,5),(2,3,3),(3,3,3)]
ncases=0
for alph in cases:
    for k in (3,4,5):
        ncases+=check_case(alph,k)
assert comb(3+4-2,4-2)==10
print(f'PASS {ncases} independent full-clique/coloured-component cases; four-variable 3-factor theory count = 10')
