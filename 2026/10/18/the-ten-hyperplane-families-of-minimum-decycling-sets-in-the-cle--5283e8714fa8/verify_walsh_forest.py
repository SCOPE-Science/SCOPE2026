#!/usr/bin/env python3
"""Exact finite verification of induced forests and their exchange graph."""
import hashlib
import json
from collections import Counter, deque
from itertools import combinations

N = 16
FULL = (1 << N) - 1
GEN = (1, 2, 4, 8, 15)
NEIGH = [sum(1 << (v ^ a) for a in GEN) for v in range(N)]
assert all(z.bit_count() == 5 for z in NEIGH)


def acyclic(mask):
    remaining = mask
    while remaining:
        leaves = 0
        for v in range(N):
            if remaining & (1 << v) and (NEIGH[v] & remaining).bit_count() <= 1:
                leaves |= 1 << v
        if not leaves:
            return False
        remaining &= ~leaves
    return True


def lam(i, v):
    return ((v & (15 ^ (1 << i))) if i < 4 else v).bit_count() % 2

halves = {}
for i in range(5):
    for b in range(2):
        H = sum(1 << v for v in range(N) if lam(i,v) == b)
        assert H.bit_count() == 8
        assert sum((H & NEIGH[v]).bit_count() for v in range(N) if H >> v & 1) == 8
        halves[(i,b)] = H

proposed = {H ^ (1 << v) for H in halves.values() for v in range(N) if H >> v & 1}
assert len(proposed) == 80

forest9 = set()
forest10 = 0
for mask in range(1 << N):
    size = mask.bit_count()
    if size == 9 and acyclic(mask):
        forest9.add(mask)
    if size == 10 and acyclic(mask):
        forest10 += 1
assert forest10 == 0
assert forest9 == {FULL ^ S for S in proposed}
assert len(forest9) == 80
seeds = sorted(proposed)

# Check complete pairwise minimum-replacement distances.
counts = Counter()
for j, a in enumerate(seeds):
    for b in seeds[:j]:
        counts[(a ^ b).bit_count() // 2] += 1
assert sum(counts.values()) == 3160


def exchange(t):
    adjacency = [[] for _ in seeds]
    for i,a in enumerate(seeds):
        for j in range(i):
            if (a ^ seeds[j]).bit_count() <= 2*t:
                adjacency[i].append(j)
                adjacency[j].append(i)
    comps = []
    seen = set()
    for root in range(len(seeds)):
        if root in seen:
            continue
        group = [root]
        seen.add(root)
        for vertex in group:
            for w in adjacency[vertex]:
                if w not in seen:
                    group.append(w)
                    seen.add(w)
        comps.append(group)
    return adjacency,comps

A1,C1=exchange(1)
A2,C2=exchange(2)
A3,C3=exchange(3)
assert len(C1)==len(C2)==10 and all(len(c)==8 for c in C1+C2)
assert len(C3)==1 and len(C3[0])==80
assert {len(a) for a in A1} == {7}
assert {len(a) for a in A3} == {23}
assert all(A1[i]==A2[i] for i in range(80))

profile = []
for root in range(80):
    dist = [-1] * 80
    dist[root] = 0
    q = deque([root])
    while q:
        v = q.popleft()
        for w in A3[v]:
            if dist[w] < 0:
                dist[w] = dist[v]+1
                q.append(w)
    assert -1 not in dist
    profile.append(tuple(Counter(dist)[i] for i in range(4)))
assert set(profile)=={(1,23,48,8)}

slide_edges = 0
for i,a in enumerate(seeds):
    for j in A1[i]:
        if j < i:
            delta=a ^ seeds[j]
            x=(a & delta).bit_length()-1
            y=(seeds[j] & delta).bit_length()-1
            if NEIGH[x] & (1 << y):
                slide_edges += 1
assert slide_edges==40

print(json.dumps({
    'graph':'five-regular Clebsch Cayley F2^4',
    'degree':5, 'forest9':len(forest9),'forest10':forest10,
    'minimum_fvs':7, 'minimum_fvs_count':len(seeds),
    'minimum_fvs_hex_sha256':hashlib.sha256(','.join(f'{s:04x}' for s in seeds).encode()).hexdigest(),
    'hyperplanes':len(halves),
    'exchange1_edges':sum(map(len,A1))//2,'exchange1_components':sorted(map(len,C1)),
    'exchange2_edges':sum(map(len,A2))//2,'exchange2_components':sorted(map(len,C2)),
    'exchange3_edges':sum(map(len,A3))//2,'exchange3_components':sorted(map(len,C3)),
    'exchange3_distance_profile':list(profile[0]),
    'slide_edges':slide_edges,
    'pair_cost_histogram':dict(sorted(counts.items())),
}, sort_keys=True))
