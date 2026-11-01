#!/usr/bin/env python3
"""Exact, standard-library verification of an explicit D4 antichain-complex collapse.

Run: python verify_d4.py
All assertions use finite integer or rational arithmetic. The final wedge
identification follows topologically from the checked sphere-plus-graph model.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations

N = 4

def simple_coordinates(root):
    """Solve root=sum_i coefficient_i*simple_root_i over Q, without a formula table."""
    simple = [(1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,1,1)]
    A = [[Fraction(simple[j][i]) for j in range(N)] + [Fraction(root[i])]
         for i in range(N)]
    for k in range(N):
        pivot = next(i for i in range(k,N) if A[i][k])
        A[k], A[pivot] = A[pivot], A[k]
        d = A[k][k]
        A[k] = [x/d for x in A[k]]
        for i in range(N):
            if i != k:
                factor = A[i][k]
                A[i] = [x-factor*y for x,y in zip(A[i],A[k])]
    return tuple(row[N] for row in A)

roots = {}
for i,j in combinations(range(1,N+1),2):
    for sign in ('-','+'):
        v = [0]*N
        v[i-1] = 1
        v[j-1] = -1 if sign == '-' else 1
        name = f'{i}{sign}{j}'
        coord = simple_coordinates(v)
        assert all(x.denominator == 1 and x >= 0 for x in coord)
        roots[name] = coord
assert len(roots) == 12

# Distinct roots are comparable iff their coefficient vectors are ordered.
def incomparable(a,b):
    x,y=roots[a],roots[b]
    return not all(s <= t for s,t in zip(x,y)) and not all(t <= s for s,t in zip(x,y))

names = sorted(roots)
faces = {frozenset()}
for k in range(1,5):
    for subset in combinations(names,k):
        if all(incomparable(a,b) for a,b in combinations(subset,2)):
            faces.add(frozenset(subset))
assert Counter(map(len,faces)) == {0:1, 1:12, 2:24, 3:12, 4:1}

p,q,r,s,t,u,a,b,c,d,x,y = '1-2','1-3','1-4','1+4','2-3','2+3','2-4','2+4','3-4','3+4','1+2','1+3'

def F(*args): return frozenset(args)

# The following maximal faces can be read directly from the 12x12
# incomparability matrix; their list fixes the entire simplicial complex.
expected_facets = {
    F(x),F(y),
    F(p,u),F(q,u),F(r,b),F(r,d),F(s,a),F(s,c),
    F(p,a,b),F(p,a,d),F(p,b,c),
    F(q,a,b),F(q,a,d),F(q,b,c),F(q,c,d),
    F(r,s,u),F(p,t,c,d),
}
actual_facets = {face for face in faces if not any(face < other for other in faces)}
assert actual_facets == expected_facets

# Each pair (free face, unique codimension-one coface) is an actual
# elementary simplicial collapse in the current complex.
collapse_pairs = [
    (F(p,t,c), F(p,t,c,d)),
    (F(p,t),   F(p,t,d)),
    (F(r,s),   F(r,s,u)),
    (F(t,c),   F(t,c,d)),
    (F(t),     F(t,d)),
]
remaining = faces.copy()
for low,high in collapse_pairs:
    assert len(high) == len(low)+1 and low < high
    assert low in remaining and high in remaining
    assert {coface for coface in remaining if low < coface} == {high}
    remaining.remove(low)
    remaining.remove(high)

base_edges = [F(a,b),F(b,c),F(c,d),F(d,a)]
expected_sphere_triangles = {edge | {pole} for edge in base_edges for pole in [p,q]}
triangles = {f for f in remaining if len(f)==3}
assert triangles == expected_sphere_triangles and len(triangles)==8
assert not any(len(f)>=4 for f in remaining)

sphere_edges = set(base_edges)
for pole in (p,q):
    sphere_edges.update(F(pole,v) for v in (a,b,c,d))
assert len(sphere_edges)==12
extra_edges = {F(p,u),F(q,u),F(r,u),F(r,b),F(r,d),F(s,u),F(s,a),F(s,c)}
assert {f for f in remaining if len(f)==2} == sphere_edges | extra_edges
assert len(extra_edges)==8 and sphere_edges.isdisjoint(extra_edges)
assert {f for f in remaining if len(f)==1} == {F(z) for z in names if z!=t}
assert all(not any(x in f for f in remaining if len(f)>=2) for x in (x,y))

# A tree on the 9 vertices of the connected component meets the sphere in
# a spanning tree and has exactly three additional edges.
tree_sphere = {F(a,b),F(b,c),F(c,d),F(p,a),F(q,a)}
tree_new = {F(p,u),F(u,r),F(u,s)}
spanning_tree = tree_sphere | tree_new
connected_vertices = {p,q,r,s,u,a,b,c,d}
assert spanning_tree <= (sphere_edges|extra_edges)
assert len(spanning_tree)==len(connected_vertices)-1 == 8
adj = {v:set() for v in connected_vertices}
for edge in spanning_tree:
    v,w=tuple(edge)
    adj[v].add(w)
    adj[w].add(v)
seen={p};frontier=[p]
while frontier:
    v=frontier.pop()
    for w in adj[v]-seen:
        seen.add(w)
        frontier.append(w)
assert seen == connected_vertices
assert len(extra_edges-tree_new)==5

# Independent mod-2 chain ranks, checking the pre-collapse Betti profile.
def rank_f2(columns):
    basis={}
    for z in columns:
        while z:
            pivot=z.bit_length()-1
            if pivot not in basis:
                basis[pivot]=z
                break
            z ^= basis[pivot]
    return len(basis)

by_size = {k:sorted([tuple(sorted(f)) for f in faces if len(f)==k]) for k in range(1,5)}
rank={}
for k in (2,3,4):
    index={face:i for i,face in enumerate(by_size[k-1])}
    cols=[]
    for face in by_size[k]:
        z=0
        for j in range(k):
            boundary=face[:j]+face[j+1:]
            z ^= (1 << index[boundary])
        cols.append(z)
    rank[k]=rank_f2(cols)
assert (rank[2],rank[3],rank[4]) == (9,10,1)
assert (12-rank[2]-1,24-rank[2]-rank[3],12-rank[3]-rank[4]) == (2,5,1)

print('PASS: 12 positive roots, simplicial f-vector (12,24,12,1).')
print('PASS: all five elementary collapse pairs have unique cofaces.')
print('PASS: residue is an octahedral S^2 plus eight graph edges and two isolated vertices.')
print('PASS: a spanning tree leaves five attached independent circle edges.')
print('PASS: reduced integral homotopy type is (S^2 wedge 5 S^1) disjoint union {point} disjoint union {point}.')
print('PASS: independent mod-2 boundary ranks (9,10,1) yield reduced Betti ranks (2,5,1).')
