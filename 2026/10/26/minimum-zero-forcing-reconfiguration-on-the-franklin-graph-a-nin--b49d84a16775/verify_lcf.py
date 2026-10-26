#!/usr/bin/env python3
"""Exact zero-forcing reconfiguration census for the Franklin graph; standard library only."""
import collections
import itertools
import json

N = 12
V = range(N)
offsets = [5, -5] * 6
neighbors = [set() for _ in V]
for u in V:
    for v in ((u-1)%N, (u+1)%N, (u+offsets[u])%N):
        neighbors[u].add(v)
        neighbors[v].add(u)
assert all(len(A)==3 for A in neighbors)
adj = [sum(1<<v for v in A) for A in neighbors]
full = (1<<N)-1

def forces(mask):
    """Parallel application of all legal forces; monotone fixed-point calculation."""
    while True:
        add = 0
        for u in V:
            if mask & (1<<u):
                white = adj[u] & ~mask
                if white and not (white & (white-1)):
                    add |= white
        new = mask | add
        if new == mask:
            return mask == full
        mask = new

mins4 = sum(forces(sum(1<<u for u in S)) for S in itertools.combinations(V, 4))
bases = [sum(1<<u for u in S) for S in itertools.combinations(V, 5)
         if forces(sum(1<<u for u in S))]
assert mins4 == 0 and len(bases) == 324
NBASE=len(bases)
TJ=[set() for _ in bases]
TS=[set() for _ in bases]
for i, j in itertools.combinations(range(NBASE), 2):
    removed = bases[i] & ~bases[j]
    added = bases[j] & ~bases[i]
    if removed.bit_count() == 1 and added.bit_count() == 1:
        TJ[i].add(j); TJ[j].add(i)
        u = removed.bit_length()-1
        if adj[u] & added:
            TS[i].add(j); TS[j].add(i)

def profile(g):
    edge_count = sum(map(len, g))//2
    degree_hist = dict(sorted(collections.Counter(map(len,g)).items()))
    dist_hist = collections.Counter()
    ecc_hist = collections.Counter()
    for root in range(NBASE):
        Q=collections.deque([root]); d={root:0}
        while Q:
            u=Q.popleft()
            for v in g[u]:
                if v not in d:
                    d[v]=d[u]+1;Q.append(v)
        assert len(d)==NBASE, 'disconnected graph'
        ecc_hist[max(d.values())]+=1
        dist_hist.update(d[j] for j in range(root+1,NBASE))
    return dict(edges=edge_count, degree_histogram=degree_hist,
                radius=min(ecc_hist),diameter=max(ecc_hist),
                eccentricities=dict(sorted(ecc_hist.items())),
                pair_distances=dict(sorted(dist_hist.items())))

tj=profile(TJ); ts=profile(TS)
assert tj['edges']==2910 and tj['diameter']==5
assert ts['edges']==534 and ts['diameter']==13
assert tj['eccentricities']=={5:324}
assert ts['eccentricities']=={9:24,10:144,11:60,12:48,13:48}
# Calculate maximal graph-metric distortion restricted to adjacent jump configurations.
max_stretch=0
witness=None
for root in range(NBASE):
    d={root:0};q=collections.deque([root])
    while q:
        u=q.popleft()
        for v in TS[u]:
            if v not in d: d[v]=d[u]+1;q.append(v)
    for j in TJ[root]:
        if root<j and d[j]>max_stretch:
            max_stretch=d[j]
            witness=(root,j)
assert max_stretch==9
claim_witness=[list(i for i in V if bases[x]>>i&1) for x in witness]
assert len(set(claim_witness[0])^set(claim_witness[1]))==2
print(json.dumps({'model':'LCF [5,-5]^6', 'four_element_forcing_sets':mins4,
  'five_element_forcing_sets':len(bases),'token_jump':tj,'token_slide':ts,
  'max_slide_distance_among_jump_neighbors':max_stretch,
  'example_jump_neighbor_pair_with_slide_distance_nine':claim_witness}, sort_keys=True))
