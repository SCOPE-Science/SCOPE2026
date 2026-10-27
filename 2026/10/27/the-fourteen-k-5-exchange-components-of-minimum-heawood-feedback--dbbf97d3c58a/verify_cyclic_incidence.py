#!/usr/bin/env python3
"""Separate enumeration using a cyclic difference-set incidence model."""
from itertools import combinations
from collections import Counter

V=14
edge_list=[]
for line in range(7):
    for d in (0,1,3):
        edge_list.append(((line+d)%7,7+line))
assert len(edge_list)==21

def is_acyclic(complement_mask):
    parent=list(range(V))
    def find(x):
        while x!=parent[x]:
            x=parent[x]
        return x
    for u,v in edge_list:
        if complement_mask&(1<<u) and complement_mask&(1<<v):
            a,b=find(u),find(v)
            if a==b:return False
            parent[b]=a
    return True

counts={k:0 for k in range(5)}
valid=[]
for mask in range(1<<V):
    k=mask.bit_count()
    if k>4:continue
    if is_acyclic(((1<<V)-1)^mask):
        counts[k]+=1
        if k==4:valid.append(mask)
assert counts=={0:0,1:0,2:0,3:0,4:70},counts

index={mask:i for i,mask in enumerate(valid)}
neighbor_pairs=set()
for i,mask in enumerate(valid):
    selected=[b for b in range(V) if mask>>b&1]
    unselected=[b for b in range(V) if not (mask>>b&1)]
    for u in selected:
        for v in unselected:
            j=index.get(mask^(1<<u)^(1<<v))
            if j is not None:
                neighbor_pairs.add(tuple(sorted((i,j))))
assert len(neighbor_pairs)==140,len(neighbor_pairs)
parent=list(range(len(valid)))
def root(x):
    while x!=parent[x]:
        parent[x]=parent[parent[x]];x=parent[x]
    return x
for i,j in neighbor_pairs:
    a,b=root(i),root(j)
    if a!=b: parent[b]=a
sizes=Counter(root(i) for i in range(len(valid)))
assert len(sizes)==14 and set(sizes.values())=={5}

# Independently test the full geometric classification.
expected=set()
for line in range(7):
    unincident = {p for p in range(7) if (p-line)%7 not in (0,1,3)}
    U=unincident|{7+line}
    assert len(U)==5
    for sub in combinations(U,4): expected.add(sum(1<<v for v in sub))
for point in range(7):
    unincident = {7+line for line in range(7) if (point-line)%7 not in (0,1,3)}
    U=unincident|{point}
    assert len(U)==5
    for sub in combinations(U,4): expected.add(sum(1<<v for v in sub))
assert set(valid)==expected
print('CYCLIC_CHECK_OK')
print('counts_by_size=',counts)
print('number_minimum_feedback_vertex_sets=',len(valid))
print('exchange_edges=',len(neighbor_pairs))
print('components=',len(sizes))
print('component_size_histogram=',dict(Counter(sizes.values())))
print('geometric_classification_exact=',True)
