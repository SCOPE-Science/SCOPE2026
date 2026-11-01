#!/usr/bin/env python3
"""Independent direct-face enumeration and mod-2 simplicial homology cross-check."""
from itertools import combinations

N = 13
R = {i*i % N for i in range(1,N)}
EDGES = {(u,v) for u in range(N) for v in range(u+1,N) if (v-u)%N in R}

def connected(vertices):
    remaining = set(vertices)
    seen = {min(remaining)}
    while True:
        new = {v for v in remaining-seen
               if any((min(v,w),max(v,w)) in EDGES for w in seen)}
        if not new:
            break
        seen.update(new)
    return seen == remaining

# This enumeration tests each possible face directly against graph connectivity;
# it does not generate downward closure from any precomputed facet list.
groups = [[] for _ in range(9)]
for size in range(1,10):
    for vertices in combinations(range(N), size):
        comp = tuple(v for v in range(N) if v not in vertices)
        if any(not connected(four) for four in combinations(comp,4)):
            mask = sum(1<<v for v in vertices)
            groups[size-1].append(mask)
assert [len(g) for g in groups] == [13,78,286,715,1287,1716,1664,975,260]
ranks={}
for dim in range(1,9):
    row_index={f:i for i,f in enumerate(groups[dim-1])}
    pivots={}
    for face in groups[dim]:
        v=0
        bits=[i for i in range(N) if face & (1<<i)]
        for i in bits:
            v ^= 1 << row_index[face ^ (1<<i)]
        while v:
            p=v.bit_length()-1
            if p in pivots:
                v ^= pivots[p]
            else:
                pivots[p]=v
                break
    ranks[dim]=len(pivots)
assert [ranks[i] for i in range(1,9)] == [12,66,220,495,792,924,715,260]
betti=[len(groups[i])-ranks.get(i,0)-ranks.get(i+1,0) for i in range(9)]
assert betti == [1,0,0,0,0,0,25,0,0]
print('PALEY13_FOUR_CUT_MOD2_CROSSCHECK_OK')
print('faces=6994 graph_edges=39')
print('boundary_ranks_d1_to_d8=12,66,220,495,792,924,715,260')
print('ordinary_betti_d0_to_d8=1,0,0,0,0,0,25,0,0')
