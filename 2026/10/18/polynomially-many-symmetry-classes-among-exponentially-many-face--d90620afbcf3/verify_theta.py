#!/usr/bin/env python3
"""Exact facet/orbit checks for theta graphs with one two-edge arm and m three-edge arms.

Only Python's standard library is needed. Enumerates every integral Lipschitz
potential using a fixed spanning tree whose increments are in {-1,0,1}.
It independently compares computed symmetry orbits with multiset formulae.
"""
from itertools import product
from collections import Counter
from math import factorial, comb


def graph(m):
    a, b, w = 0, 1, 2
    edges = [(a, w), (w, b)]
    for i in range(m):
        u, v = 3 + 2*i, 4 + 2*i
        edges += [(a, u), (u, v), (v, b)]
    # This is a spanning tree; it is not assumed tight at any facet.
    tree = [(a, w), (a, 3), (3, 4), (4, b)]
    for i in range(1, m):
        tree += [(a, 3+2*i), (3+2*i, 4+2*i)]
    assert len(tree) == 2*m + 2
    return 2*m+3, edges, tree


def connected(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    frontier = [0]
    while frontier:
        for v in adj[frontier.pop()]:
            if v not in seen:
                seen.add(v)
                frontier.append(v)
    return len(seen) == n


def all_facets(m):
    n, edges, tree = graph(m)
    out = {}
    for steps in product((-1,0,1), repeat=n-1):
        f = {0: 0}
        for (u, v), s in zip(tree, steps):
            assert u in f and v not in f
            f[v] = f[u] + s
        F = tuple(f[i] for i in range(n))
        if any(abs(F[u]-F[v]) > 1 for u, v in edges):
            continue
        tight = [(u,v) for u,v in edges if abs(F[u]-F[v]) == 1]
        if connected(n, tight):
            out[F] = len(tight)
    return out


def transformations(m, f):
    n, _, _ = graph(m)
    # First: sign reversal; second: pole interchange plus path reversal;
    # third and subsequent: adjacent arm transpositions.
    yield tuple(-x for x in f)
    perm = list(range(n))
    perm[0], perm[1] = 1, 0
    for i in range(m):
        perm[3+2*i], perm[4+2*i] = 4+2*i, 3+2*i
    # g[perm[old_vertex]] = f[old_vertex], then normalize at vertex 0.
    g = [0]*n
    for i, x in enumerate(f): g[perm[i]] = x
    off = g[0]
    yield tuple(x-off for x in g)
    for i in range(m-1):
        g = list(f)
        for k in (0,1):
            g[3+2*i+k],g[3+2*(i+1)+k] = g[3+2*(i+1)+k],g[3+2*i+k]
        yield tuple(g)


def actual_orbits(m, facets):
    unseen = set(facets)
    orbit_info = []
    while unseen:
        seed = next(iter(unseen))
        reached = {seed}
        todo = [seed]
        while todo:
            for g in transformations(m, todo.pop()):
                assert g in facets
                if g not in reached:
                    reached.add(g)
                    todo.append(g)
        unseen.difference_update(reached)
        d = seed[1]
        category = ('zero' if d==0 else 'two' if abs(d)==2 else 'one')
        assert {('zero' if f[1]==0 else 'two' if abs(f[1])==2 else 'one') for f in reached} == {category}
        orbit_info.append((category, len(reached)))
    return sorted(orbit_info)


def compositions(length, n):
    if length==1:
        yield (n,)
    else:
        for k in range(n+1):
            for rest in compositions(length-1, n-k):
                yield (k,) + rest


def multiset_size(c):
    z = factorial(sum(c))
    for v in c:z //= factorial(v) # division step-wise works: factorial ratios integer successively
    return z


def predicted_orbits(m):
    result=[]
    # Δ=0: short path orientation is normalized using sign reversal.
    # The remaining pole interchange acts on six long-arm states by two
    # fixed letters and two transposed pairs. 0,1 fixed; 2<->3,4<->5.
    invol0 = (0,1,3,2,5,4)
    seen=set()
    for c in compositions(6,m):
        mate=tuple(c[invol0[i]] for i in range(6))
        if c in seen:continue
        seen.add(c);seen.add(mate)
        M=multiset_size(c)
        result.append(('zero',2*M if mate==c else 4*M))
    # Δ=±2: three positions for a zero on each long arm;
    # reversal swaps the outer positions.
    seen=set()
    for c in compositions(3,m):
        mate=(c[2],c[1],c[0])
        if c in seen: continue
        seen.add(c);seen.add(mate)
        M=multiset_size(c)
        result.append(('two',2*M if mate==c else 4*M))
    # Δ=±1: short-path slack position is flipped by pole reversal;
    # this means no identification between distinct three-color multisets.
    for c in compositions(3,m):
        result.append(('one',4*multiset_size(c)))
    return sorted(result)


def formula(m):
    H=sum((s+1)*(m-2*s+1) for s in range(m//2+1))
    return (comb(m+5,5)+H+3*comb(m+2,2)+(m//2)+1)//2


def test(m, check_orbits=True):
    n, edges, tree = graph(m)
    found = all_facets(m)
    expected = 2*6**m + 6*3**m
    assert len(found) == expected, (m,len(found),expected)
    bytight = Counter(found.values())
    if m>=2:
        assert bytight == Counter({2+2*m:2*6**m+2*3**m,
                                   1+3*m:4*3**m}), (m,bytight)
    if check_orbits:
        actual=actual_orbits(m,found)
        predicted=predicted_orbits(m)
        assert actual==predicted,(m,Counter(actual)-Counter(predicted),Counter(predicted)-Counter(actual))
        assert len(actual)==formula(m)
        assert sum(size for _,size in actual)==expected
        print(f'm={m}; potentials={expected}; actual_orbits={len(actual)}; edge_histogram={dict(bytight)}; orbit_types={dict(Counter(t for t,_ in actual))}')
    else:
        print(f'm={m}; potentials={expected}; edge_histogram={dict(bytight)}')

if __name__=='__main__':
    for m in (2,3,4):test(m)
    test(5, False)
    print('ALL EXACT MIXED-THETA CHECKS PASSED')
