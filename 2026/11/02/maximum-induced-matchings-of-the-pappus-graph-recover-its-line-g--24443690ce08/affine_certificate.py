#!/usr/bin/env python3
"""Exact Pappus induced-matching classification and exchange certificate.
Only Python's standard library is needed. Run: python affine_certificate.py
"""
from itertools import combinations
from collections import Counter, deque

points = [(x,y) for x in range(3) for y in range(3)]
lines = [(s,b) for s in range(3) for b in range(3)]
flags = [(i,j+9) for i,(x,y) in enumerate(points)
         for j,(s,b) in enumerate(lines) if (y-s*x-b)%3 == 0]
assert len(flags) == 27
neigh = [set() for _ in range(18)]
for p,l in flags:
    neigh[p].add(l); neigh[l].add(p)

def induced_matching(items):
    for a,b in combinations(items,2):
        p,l = flags[a]; q,k = flags[b]
        if p==q or l==k or k in neigh[p] or l in neigh[q]:
            return False
    return True

maxima = [frozenset(c) for c in combinations(range(27),5) if induced_matching(c)]
assert len(maxima) == 27 and len(set(maxima)) == 27
# Upper bound: 2r incidences from r selected points into the 9-r
# unused lines, each holding at most three points: 2r<=3(9-r).
assert 2*6 > 3*(9-6)
exchange = [set() for _ in maxima]
for i,j in combinations(range(27),2):
    if len(maxima[i]&maxima[j]) == 3:
        exchange[i].add(j); exchange[j].add(i)
assert Counter(map(len, exchange)) == {4:27}
assert all(len(maxima[i]&maxima[j]) != 4 for i,j in combinations(range(27),2))

def distances(adj, source):
    d={source:0};todo=deque([source])
    while todo:
        v=todo.popleft()
        for w in adj[v]:
            if w not in d:d[w]=d[v]+1;todo.append(w)
    return d

distance_pairs=Counter(); overlap_distance=Counter(); profiles=set()
for i in range(27):
    di=distances(exchange,i)
    assert len(di)==27
    profiles.add(tuple(Counter(di.values())[k] for k in range(5)))
    for j in range(i):
        distance_pairs[di[j]]+=1
        overlap_distance[(len(maxima[i]&maxima[j]),di[j])]+=1
assert profiles=={(1,4,8,12,2)}
assert distance_pairs=={1:54,2:108,3:162,4:27}
assert overlap_distance=={(3,1):54,(1,2):108,(0,3):162,(0,4):27}

triangles=[frozenset(t) for t in combinations(range(27),3)
           if all(v in exchange[u] for u,v in combinations(t,2))]
assert len(triangles)==18 and len(set(triangles))==18
assert all(sum({i,j} <= t for t in triangles)==1
           for i,j in combinations(range(27),2) if j in exchange[i])
assert all(sum(i in t for t in triangles)==2 for i in range(27))
# The triangle incidence graph has one vertex for each of the 18 triangles;
# the 27 maximum matchings are the 27 edges between the two triangles containing them.
T=[set(t) for t in triangles]
tri_adj=[set() for _ in triangles]
for i,j in combinations(range(18),2):
    if T[i]&T[j]:tri_adj[i].add(j);tri_adj[j].add(i)
assert Counter(map(len,tri_adj))=={3:18}

# Backtracking isomorphism test against the original 18-vertex incidence graph.
# Both adjacency and nonadjacency are checked, so this is an exact isomorphism certificate.
orig=[set(v) for v in neigh]
def find_iso():
    mapping={};used=set()
    def search():
        if len(mapping)==18:return dict(mapping)
        left=[i for i in range(18) if i not in mapping]
        v=max(left,key=lambda v:(len(tri_adj[v]&mapping.keys()),-v))
        for w in range(18):
            if w in used or len(tri_adj[v])!=len(orig[w]):continue
            if any(((u in tri_adj[v]) != (mapping[u] in orig[w])) for u in mapping):continue
            mapping[v]=w;used.add(w)
            result=search()
            if result is not None:return result
            del mapping[v];used.remove(w)
        return None
    return search()

mapping=find_iso()
assert mapping is not None
# Explicitly map each exchange-vertex to an edge of the original Pappus graph.
induced_edges=[]
for v in range(27):
    a,b=[i for i,t in enumerate(triangles) if v in t]
    e=frozenset((mapping[a],mapping[b]))
    assert any(e==frozenset(f) for f in flags)
    induced_edges.append(e)
assert len(set(induced_edges))==27
assert all((j in exchange[i]) == bool(induced_edges[i]&induced_edges[j])
           for i,j in combinations(range(27),2))
print('AFFINE_EXHAUSTIVE_MATCHING_LINE_GRAPH_PASS')
print('max_size=5 max_count=27 2_replacement_edges=54 triangles=18')
print('distance_profile=(1,4,8,12,2) pair_distances=(54,108,162,27)')
print('intersection_distance=',sorted(overlap_distance.items()))
