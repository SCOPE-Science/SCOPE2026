#!/usr/bin/env python3
"""Exact integer cellular verification for a free antipodal quotient of a simplicial double."""
from itertools import combinations, product
from collections import Counter
from math import comb

N = 6
base_edges = list(combinations(range(N), 2))
signed_edges = []
for a,b in base_edges:
    for sa,sb in product((0,1), repeat=2):
        signed_edges.append((a,b,sa,sb))
edge_to_index = {edge: k for k,edge in enumerate(signed_edges)}
flip = {i: edge_to_index[(a,b,sa^1,sb^1)] for i,(a,b,sa,sb) in enumerate(signed_edges)}
assert len(signed_edges) == 60 and all(flip[flip[i]] == i and flip[i] != i for i in flip)

# Independently create all faces by checking distinct underlying coordinates.
faces = {1: [(i,) for i in range(len(signed_edges))]}
for k in (2,3):
    faces[k] = []
    for face in combinations(range(len(signed_edges)), k):
        coordinates = [z for i in face for z in signed_edges[i][:2]]
        if len(set(coordinates)) == 2*k:
            faces[k].append(face)
assert [len(faces[k]) for k in (1,2,3)] == [60,720,960]

# A different count uses the number of matchings of K_6 and 4 independent
# signed choices per matching edge.
assert [len(faces[k]) for k in (1,2,3)] == [15*4,45*16,15*64]

def opposite(face):
    return tuple(sorted(flip[i] for i in face))

def orbit(face):
    return min(face, opposite(face))

orbits = {k: sorted(set(orbit(face) for face in faces[k])) for k in (1,2,3)}
assert all(opposite(face) != face for k in (1,2,3) for face in faces[k])
assert [len(orbits[k]) for k in (1,2,3)] == [30,360,480]

indices = {k: {face:i for i,face in enumerate(orbits[k])} for k in (1,2,3)}
boundary = {}
for k in (2,3):
    boundary[k] = []
    for face in orbits[k]:
        column = {}
        for position in range(k):
            subface = orbit(face[:position]+face[position+1:])
            j = indices[k-1][subface]
            column[j] = column.get(j,0)+(-1)**position
        column = {i:a for i,a in column.items() if a}
        boundary[k].append(column)
assert sum(len(x) for x in boundary[2]) == 720
assert sum(len(x) for x in boundary[3]) == 1440
print('QUOTIENT_OK signed_faces=(60,720,960) quotient_cells=(30,360,480)')

# Verify the complete integer chain identity d1*d2=0, including all signs.
for col in boundary[3]:
    squared = {}
    for j,a in col.items():
        for i,b in boundary[2][j].items():
            squared[i] = squared.get(i,0)+a*b
    assert all(a == 0 for a in squared.values())
for col in boundary[2]:
    assert sum(col.values()) == 0
print('CHAIN_OK 720_plus_1440_integer_incidence_entries d1_d2_zero')

# Determine rank(d1)=29 by connectivity of the complete quotient one-skeleton.
adj = {i:set() for i in range(len(orbits[1]))}
for col in boundary[2]:
    assert len(col)==2 and sorted(col.values())==[-1,1]
    x,y=col
    adj[x].add(y);adj[y].add(x)
seen={0};stack=[0]
while stack:
    i=stack.pop()
    for j in adj[i]-seen:
        seen.add(j);stack.append(j)
assert len(seen)==30
print('GRAPH_OK quotient_one_skeleton_connected rank_d1=29')

# Full integer unit-pivot elimination: each entry ±1 allows unimodular
# elimination of its row and column. Sparse Schur-complement updates are exact.
# This computes Smith factors of 1 and leaves a presentation matrix for the
# nonunit factors, without using floating point or a modular surrogate.
def reduce_unit_columns(columns, nrows):
    rows={i:{} for i in range(nrows)}
    cols={j:dict(c) for j,c in enumerate(columns)}
    for j,c in cols.items():
        for i,a in c.items():
            assert a != 0 and i in rows
            rows[i][j] = a
    pivot_count=0
    while True:
        best=None
        for j,col in cols.items():
            for i,a in col.items():
                if abs(a) == 1:
                    score=(len(col)-1)*(len(rows[i])-1)
                    if best is None or score < best[0]:
                        best=(score,i,j)
                    if score == 0: break
            if best is not None and best[0]==0:break
        if best is None:break
        _,i,j=best
        pivot=rows[i][j]
        source=tuple(rows[i].items())
        target=tuple(cols[j].items())
        for k,x in target:
            if k==i:continue
            for l,y in source:
                if l==j:continue
                new=rows[k].get(l,0)-x*y*pivot
                if new:
                    rows[k][l]=new;cols[l][k]=new
                else:
                    rows[k].pop(l,None);cols[l].pop(k,None)
        for k,_ in target:
            if k != i: rows[k].pop(j,None)
        for l,_ in source:
            if l != j: cols[l].pop(i,None)
        del rows[i];del cols[j]
        pivot_count+=1
        # Confirm transpose bookkeeping, including complete zero-column cases.
        if pivot_count in (1, 90, 180, 270):
            assert all(cols[l].get(k,0)==a for k,r in rows.items() for l,a in r.items())
            assert all(rows[k].get(l,0)==a for l,c in cols.items() for k,a in c.items())
    return pivot_count, rows, cols

p1,rows1,cols1=reduce_unit_columns(boundary[3],360)
remaining_values=Counter(abs(a) for c in cols1.values() for a in c.values())
assert p1 == 270
assert len(rows1)==90 and len(cols1)==210
assert remaining_values == {2:240}, remaining_values

# The residual is 2*A. A second exact unimodular reduction of A finds 15
# unit pivots and zero remaining matrix. Scaling those same unimodular
# operations by 2 shows Smith factors 2^15, not just a mod-2 obstruction.
row_ids={key:i for i,key in enumerate(rows1)}
half_columns = [{row_ids[i]:a//2 for i,a in c.items()} for c in cols1.values()]
p2,rows2,cols2=reduce_unit_columns(half_columns,len(rows1))
assert p2 == 15 and len(rows2)==75 and len(cols2)==195
assert all(not c for c in cols2.values())
assert all(not r for r in rows2.values())
print('SMITH_OK d2=(1^270,2^15,0^195) after exact_270_unit_pivots_plus_15_double_pivots')

rank1=29;rank2=p1+p2
h1_free=360-rank1-rank2
h2_free=480-rank2
assert (h1_free,h2_free)==(46,195)
assert (30-360+480)==(1-h1_free+h2_free)
print('HOMOLOGY_OK reduced_H1=Z^46_plus_(Z/2)^15 reduced_H2=Z^195')
print('ALL_VERIFY_OK')
