#!/usr/bin/env python3
"""Finite checks for shattering long-distance reachability queries on tree orientations.
Run with: python3 verify.py
No external dependencies.
"""
from itertools import combinations, product


def tree_edges_from_prufer(n, code):
    if n == 1:
        return ()
    deg = [1]*n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = min(i for i in range(n) if deg[i] == 1)
        edges.append((leaf,x))
        deg[leaf] -= 1
        deg[x] -= 1
    a,b = (i for i in range(n) if deg[i] == 1)
    edges.append((a,b))
    return tuple(tuple(sorted(e)) for e in edges)


def edge_paths(n, edges, d):
    adj = [[] for _ in range(n)]
    for idx,(a,b) in enumerate(edges):
        adj[a].append((b,idx)); adj[b].append((a,idx))
    paths = []
    for a in range(n):
        stack = [(a,-1,())]
        while stack:
            v, prev, es = stack.pop()
            if len(es) >= d:
                paths.append((a,v,es))
            for w,i in adj[v]:
                if w != prev:
                    direction = 0 if edges[i] == (v,w) else 1
                    stack.append((w,v,es + ((i,direction),)))
    return paths


def shadow(paths):
    out = []
    for p in paths:
        bits = 0
        for i,_ in p[2]: bits |= 1<<i
        out.append(bits)
    return out


def structural_fast(paths, shad, subset):
    direction = {}
    multiplicity = {}
    for j in subset:
        for e,b in paths[j][2]:
            if e in direction and direction[e] != b: return False
            direction[e] = b
            multiplicity[e] = multiplicity.get(e,0)+1
    return all(any(multiplicity[e]==1 for e,_ in paths[j][2]) for j in subset)


def literal_shattering(paths, subset, m):
    k = len(subset)
    if not k:return True
    patterns = set()
    for orientation in range(1<<m):
        pattern = 0
        for h,j in enumerate(subset):
            if all(((orientation>>e)&1)==b for e,b in paths[j][2]):
                pattern |= 1<<h
        patterns.add(pattern)
        if len(patterns)==1<<k:return True
    return False


case_count=0
# Exhaustive supports on every labeled path up to five edges at fixed path-length >=2;
# use all subsets when at most twelve ordered pairs, otherwise all size <=3.
for m in range(2,6):
    e = tuple((i,i+1) for i in range(m))
    for d in range(2,m+1):
        P = edge_paths(m+1,e,d)
        S = shadow(P)
        limit = len(P) if len(P)<=12 else min(3,len(P))
        for k in range(limit+1):
            for ix in combinations(range(len(P)),k):
                assert structural_fast(P,S,ix)==literal_shattering(P,ix,m),(m,d,ix)
                case_count+=1
# All labeled trees on 2..5 vertices, support sizes up to two.
for n in range(2,6):
    for code in product(range(n),repeat=max(0,n-2)):
        edges=tree_edges_from_prufer(n,code)
        for d in range(2,n):
            P=edge_paths(n,edges,d)
            S=shadow(P)
            for k in range(min(2,len(P))+1):
                for ix in combinations(range(len(P)),k):
                    assert structural_fast(P,S,ix)==literal_shattering(P,ix,n-1),(n,code,d,ix)
                    case_count+=1
print('DIRECT_SHATTERING_COMPARISONS_PASS',case_count)

# Independently maximize private-element systems of ordinary intervals through 8 edges.
interval_cases=0
for m in range(2,9):
    for d in range(2,m+1):
        ints = [(a,b) for a in range(m) for b in range(a+d-1,m)]
        q,r=divmod(m,d+1)
        predicted=2*q+(r>=d)
        assert predicted>=0
        masks = {(a,b):sum(1<<i for i in range(a,b+1)) for a,b in ints}
        def private(sub):
            ms = [masks[c] for c in sub]
            for i,mask in enumerate(ms):
                others = 0
                for j,mj in enumerate(ms):
                    if i != j: others |= mj
                if not (mask & ~others):return False
            return True
        assert any(private(c) for c in combinations(ints,predicted)),(m,d,'no witness')
        if predicted<len(ints):
            assert not any(private(c) for c in combinations(ints,predicted+1)),(m,d,'upper fail')
        interval_cases+=1
print('INTERVAL_EXTREMAL_CASES_PASS',interval_cases)
print('ALL_TREE_REACHABILITY_CHECKS_PASS')
