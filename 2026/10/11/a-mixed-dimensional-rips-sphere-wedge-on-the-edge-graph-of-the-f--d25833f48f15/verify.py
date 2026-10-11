#!/usr/bin/env python3
"""Verify exact acyclic Morse matching for scale-two Rips complex of the line graph of Q4."""
from collections import Counter, deque

# Cube vertices are binary 4-tuples encoded by integers 0...15.
# Cube edge labels are pairs (direction, base) with that direction's bit zero.
EDGE_LABELS = [(i, b) for i in range(4) for b in range(16) if not (b & (1 << i))]
assert len(EDGE_LABELS) == 32
ENDPOINTS = [(b, b ^ (1 << i)) for i,b in EDGE_LABELS]

# Two line-graph vertices are adjacent iff their underlying cube edges intersect.
N = len(ENDPOINTS)
GRAPH_NEIGHBORS = [0] * N
for a in range(N):
    for b in range(a):
        if set(ENDPOINTS[a]) & set(ENDPOINTS[b]):
            GRAPH_NEIGHBORS[a] |= 1 << b
            GRAPH_NEIGHBORS[b] |= 1 << a
assert all(z.bit_count() == 6 for z in GRAPH_NEIGHBORS)

# Breadth-first distances on the 32-vertex line graph.
DIST = [[-1] * N for _ in range(N)]
for u in range(N):
    DIST[u][u] = 0
    queue = deque([u])
    while queue:
        x = queue.popleft()
        for y in range(N):
            if GRAPH_NEIGHBORS[x] & (1 << y) and DIST[u][y] < 0:
                DIST[u][y] = DIST[u][x] + 1
                queue.append(y)
assert max(max(row) for row in DIST) == 4
for u in range(N):
    assert sum(DIST[u][v]==4 for v in range(N))==1
    for v in range(N):
        if u != v:
            min_endpoint_distance=min((a^b).bit_count() for a in ENDPOINTS[u] for b in ENDPOINTS[v])
            assert DIST[u][v] == 1 + min_endpoint_distance

# Rips radius two, every clique is generated once in increasing index order.
RIPS_NEIGHBORS = [sum(1 << j for j in range(N) if i != j and DIST[i][j] <= 2) for i in range(N)]
FACES = []
def enumerate_cliques(mask, candidates):
    while candidates:
        bit = candidates & -candidates
        candidates ^= bit
        j = bit.bit_length() - 1
        next_mask = mask | bit
        FACES.append(next_mask)
        enumerate_cliques(next_mask, candidates & RIPS_NEIGHBORS[j])
enumerate_cliques(0, (1 << N) - 1)
assert len(FACES) == len(set(FACES))
assert Counter(s.bit_count() - 1 for s in FACES) == {0:32,1:336,2:1568,3:3672,4:4512,5:2848,6:832,7:96}

# Staged vertex toggles produce a complete discrete-Morse matching.

def matching(order):
    remaining = set(FACES)
    pairs = []
    for j in order:
        bit = 1 << j
        stage = [(s, s | bit) for s in remaining if not (s & bit) and (s | bit) in remaining]
        for low,high in stage:
            remaining.remove(low)
            remaining.remove(high)
        pairs.extend(stage)
    return remaining,pairs

# Explicit and fixed Morse certificate order, independent of search or randomness.
ORDER=(16,25,18,31,29,20,0,4,10,7,14,17,22,28,15,12,13,27,1,24,6,19,8,9,21,23,5,26,11,30,2,3)
assert sorted(ORDER)==list(range(N))

critical,pairs=matching(ORDER)
crit_hist=Counter(s.bit_count()-1 for s in critical)
assert crit_hist == {0:1,3:1,5:8}
assert len(pairs)*2+len(critical) == len(FACES)

# Independently verify the matching is acyclic on the FULL Hasse diagram.
# Every incidence is normally oriented high -> low; matched incidences reverse.
index={s:i for i,s in enumerate(FACES)}
matched_pairs={(low,high) for low,high in pairs}
assert all((high.bit_count()-low.bit_count()==1 and low & high==low) for low,high in pairs)
out=[[] for _ in FACES]
indeg=[0]*len(FACES)
for high in FACES:
    x=high
    while x:
        bit=x&-x
        x-=bit
        low=high^bit
        if not low:
            continue  # do not introduce the empty simplex as a Morse 0-cell
        src,dst=(low,high) if (low,high) in matched_pairs else (high,low)
        si,di=index[src],index[dst]
        out[si].append(di)
        indeg[di]+=1
queue=deque(i for i,d in enumerate(indeg) if d==0)
visited=0
while queue:
    u=queue.popleft()
    visited+=1
    for v in out[u]:
        indeg[v]-=1
        if indeg[v]==0:queue.append(v)
assert visited==len(FACES), f'cyclic matching: {visited}/{len(FACES)} nodes'

# Morse rank tally; 3-dimensional and 5-dimensional reduced integral homology
# follow because the only Morse chain groups are C0=Z,C3=Z,C5=Z^8.
print('VERIFY_OK')
print('ORDER',' '.join(map(str,ORDER)))
print('FACES',len(FACES),'PAIRS',len(pairs),'CRITICAL',dict(sorted(crit_hist.items())))
print('HASSE_NODES',len(FACES),'HASSE_INCIDENCES',sum(map(len,out)),'TOPOLOGICAL_SORT',visited)
print('CRITICAL_FACES', sorted((s.bit_count()-1, format(s,'08x')) for s in critical))
