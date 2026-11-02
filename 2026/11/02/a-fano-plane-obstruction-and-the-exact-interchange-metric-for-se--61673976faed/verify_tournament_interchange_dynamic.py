#!/usr/bin/env python3
"""Exhaustive verification of the order-seven regular-tournament triangle-interchange graph.
Uses row-score recursion and adjacency bit masks; does not use any catalogue.
Python 3, standard library only.
"""
from itertools import combinations
from collections import Counter

N = 7
PAIRS = list(combinations(range(N), 2))
EDGE_INDEX = {p: i for i, p in enumerate(PAIRS)}
TRIPLES = list(combinations(range(N), 3))
FULL = (1 << len(PAIRS)) - 1

# Bit i=1 means the earlier-labelled player beats the later player.
# All 2^21 orientations are partitioned by these binary decisions;
# prune as soon as a vertex can no longer finish with exactly three wins.
rem = [N-1] * N
wins = [0] * N
states = []

def visit(k, word):
    if k == len(PAIRS):
        if all(w == 3 for w in wins):
            states.append(word)
        return
    u, v = PAIRS[k]
    rem[u] -= 1
    rem[v] -= 1
    for winner, bit in ((u, 1), (v, 0)):
        wins[winner] += 1
        if all(wins[x] <= 3 <= wins[x] + rem[x] for x in (u,v)):
            visit(k+1, word | (bit << k))
        wins[winner] -= 1
    rem[u] += 1
    rem[v] += 1

visit(0, 0)
assert len(states) == len(set(states)) == 2640
ix = {w: i for i, w in enumerate(states)}

triangle_masks = []
triangle_cycles = []
for a, b, c in TRIPLES:
    xy = 1 << EDGE_INDEX[a,b]
    xz = 1 << EDGE_INDEX[a,c]
    yz = 1 << EDGE_INDEX[b,c]
    triangle_masks.append(xy | xz | yz)
    triangle_cycles.append((xy | yz, xz))

def is_cyclic(word, triple_id):
    mask = triangle_masks[triple_id]
    x, z = triangle_cycles[triple_id]
    return (word & mask) == x or (word & mask) == z

# The legal flip toggles the three orientations of a directed triangle.
adj = []
cyc_masks = []
for w in states:
    available = [j for j in range(len(TRIPLES)) if is_cyclic(w,j)]
    assert len(available) == 14
    cyc_masks.append(sum(1 << j for j in available))
    nbrs = []
    for j in available:
        dst = w ^ triangle_masks[j]
        assert dst in ix
        nbrs.append(ix[dst])
    assert len(set(nbrs)) == 14
    adj.append(tuple(nbrs))

assert len(adj) == 2640
assert sum(map(len, adj)) // 2 == 18480
assert all(i in adj[j] for i, nei in enumerate(adj) for j in nei)
assert all((states[i].bit_count() - states[j].bit_count()) % 2 == 1
           for i, nei in enumerate(adj) for j in nei)

# Enumerate all 2-(7,3,1) designs by exact cover of the 21 pairs.
block_masks = [sum(1 << EDGE_INDEX[e] for e in combinations(t,2)) for t in TRIPLES]
fano = []

def cover(uncovered, chosen):
    if uncovered == 0:
        fano.append(chosen)
        return
    first = uncovered & -uncovered
    for j,block in enumerate(block_masks):
        if block & first and (uncovered & block) == block:
            cover(uncovered ^ block, chosen | (1 << j))
cover(FULL, 0)
assert len(fano) == 30
fano_count = [sum((mask & c) == mask for mask in fano) for c in cyc_masks]
assert Counter(fano_count) == Counter({0: 720, 2: 1920})

# Complete all-source BFS: the exact ball count is an integer certificate.
def distances(source):
    dist = [-1] * len(states)
    dist[source] = 0
    todo = [source]
    for x in todo:
        for y in adj[x]:
            if dist[y] == -1:
                dist[y] = dist[x] + 1
                todo.append(y)
    assert len(todo) == len(states)
    return dist

profiles = Counter()
ecc = Counter()
converse = Counter()
far_pairs = 0
for i, word in enumerate(states):
    d = distances(i)
    profile = tuple(Counter(d)[x] for x in range(max(d)+1))
    profiles[profile] += 1
    ecc[max(d)] += 1
    # Opposite tournament reverses every single one of the 21 arcs.
    anti = ix[word ^ FULL]
    converse[(fano_count[i], d[anti])] += 1
    if max(d) == 9:
        far = [k for k, dist in enumerate(d) if dist == 9]
        assert len(far) == 1 and far[0] == anti
        far_pairs += 1

P_240 = (1,14,91,343,749,871,476,92,3)
P_1680 = (1,14,91,340,739,853,483,113,6)
P_720 = (1,14,91,336,721,822,485,147,22,1)
assert profiles == Counter({P_240:240,P_1680:1680,P_720:720})
assert ecc == Counter({8:1920,9:720})
assert converse == Counter({(2,7):1920,(0,9):720})
assert far_pairs//2 == 360
print('DYNAMIC_COMPLETE_REGULAR_TOURNAMENTS_2640_AND_EDGES_18480_PASS')
print('DYNAMIC_FANO_DECOMPOSITIONS_30_TWO_OR_ZERO_PASS')
print('DYNAMIC_ALL_ROOTS_PROFILES_240_1680_720_PASS')
print('DYNAMIC_CONVERSE_DISTANCES_7_9_AND_360_EXTREMAL_PAIRS_PASS')
