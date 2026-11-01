#!/usr/bin/env python3
"""Exact finite verification of topology and symmetry of the co-Heawood two-independence complex.

Only Python standard library is needed. The loops exhaust all 2^14 vertex masks
and all 7! point permutations; the signed Lefschetz sums use integral arithmetic.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations, permutations
from math import factorial

N = 14
FULL = (1 << N) - 1
LINES = tuple(frozenset((j + d) % 7 for d in (0, 1, 3)) for j in range(7))
assert len(set(LINES)) == 7
# Singer difference-set property: each pair of distinct points lies on one line.
assert all(sum(a in line and b in line for line in LINES) == 1
           for a in range(7) for b in range(a+1, 7))
line_index = {line: i for i, line in enumerate(LINES)}

# Vertices 0..6 represent points; 7..13 represent lines.
# Incidence is excluded, rather than included, in this graph.
adj = [0] * N
for p in range(7):
    for ell in range(7):
        if p not in LINES[ell]:
            adj[p] |= 1 << (7 + ell)
            adj[7 + ell] |= 1 << p
assert all(a.bit_count() == 4 for a in adj)
assert all((adj[u] >> v & 1) == (adj[v] >> u & 1)
           for u in range(N) for v in range(N))
assert all(not (adj[v] >> v & 1) for v in range(N))
assert sum(a.bit_count() for a in adj) == 56  # twice 28 edges
# The bipartite graph is connected; every pair of point vertices has two
# common nonincident lines, and each line has four neighboring points.
assert all((adj[a] & adj[b]).bit_count() == 2
           for a in range(7) for b in range(a+1, 7))

# Two separate predicates: induced degree and forbidden 3-vertex paths.
forbidden = set()
for v in range(N):
    neighbors = [u for u in range(N) if adj[v] >> u & 1]
    for u, w in combinations(neighbors, 2):
        forbidden.add((1 << u) | (1 << v) | (1 << w))

def by_degree(s):
    return all(not(s >> v & 1) or (adj[v] & s).bit_count() <= 1
               for v in range(N))

def by_forbidden_triples(s):
    return all((s & triple) != triple for triple in forbidden)

faces = set()
for s in range(1 << N):
    x = by_degree(s)
    assert x == by_forbidden_triples(s)
    if x:
        faces.add(s)
assert 0 in faces
counts = tuple(sum(s.bit_count() == k for s in faces) for k in range(8))
assert counts == (1, 14, 91, 280, 420, 266, 42, 2), counts
assert len(faces) == 1116
facets = [s for s in faces if all((s | (1<<v)) not in faces
                                  for v in range(N) if not (s >> v & 1))]
assert Counter(s.bit_count()-1 for s in facets) == {4:56, 5:28, 6:2}

# Element toggling in ascending vertex order, on the nonempty face poset.
# A pair is created only if both faces remain unmatched.
unmatched = faces - {0}
pairs = []
for v in range(N):
    b = 1 << v
    for lower in sorted(unmatched):
        upper = lower | b
        if not (lower & b) and upper in unmatched:
            unmatched.remove(lower)
            unmatched.remove(upper)
            pairs.append((lower, upper))
assert len(pairs) == 553, len(pairs)
assert len(unmatched) == 9, len(unmatched)
assert Counter(s.bit_count() - 1 for s in unmatched) == {0: 1, 4: 8}
assert len({s for pair in pairs for s in pair}) == 2 * len(pairs)
assert all(lower in faces and upper in faces
           and (upper ^ lower).bit_count() == 1
           and (upper & lower) == lower for lower, upper in pairs)

# FULL acyclicity check of the oriented Hasse graph.
# Reverse paired incidences (lower -> upper), orient all others upper -> lower.
paired_upper = {upper: lower for lower, upper in pairs}
vertices = sorted(faces - {0})
indegree = {s: 0 for s in vertices}
outgoing = defaultdict(list)
cover_edges = 0
for upper in vertices:
    t = upper
    while t:
        bit = t & -t
        t -= bit
        lower = upper ^ bit
        if not lower:
            continue  # empty face is not in the discrete Morse poset
        cover_edges += 1
        source, target = (lower, upper) if paired_upper.get(upper) == lower else (upper, lower)
        outgoing[source].append(target)
        indegree[target] += 1
queue = deque(s for s in vertices if indegree[s] == 0)
visited = 0
while queue:
    s = queue.popleft()
    visited += 1
    for target in outgoing[s]:
        indegree[target] -= 1
        if indegree[target] == 0:
            queue.append(target)
assert visited == len(vertices), (visited, len(vertices))
assert all(x == 0 for x in indegree.values())

# Independent mod-2 exact reduced chain-boundary check (augmented at dimension 0).
by_size = [[s for s in sorted(faces) if s.bit_count() == k] for k in range(8)]
boundary_ranks = {}
for k in range(1, 8):
    bottom = {s: i for i, s in enumerate(by_size[k-1])}
    pivots = {}
    for s in by_size[k]:
        col = 0
        t = s
        while t:
            bit = t & -t
            t ^= bit
            col ^= 1 << bottom[s ^ bit]
        while col:
            j = col.bit_length() - 1
            if j in pivots:
                col ^= pivots[j]
            else:
                pivots[j] = col
                break
    boundary_ranks[k] = len(pivots)
assert tuple(boundary_ranks[k] for k in range(1, 8)) == (1, 13, 78, 202, 218, 40, 2)
betti = [len(by_size[k]) - boundary_ranks[k] - boundary_ranks.get(k+1, 0)
         for k in range(1, 8)]
assert tuple(betti) == (0, 0, 0, 0, 8, 0, 0)

# Enumerate all bipartition-preserving automorphisms by all 7! point maps.
preserving = []
for point_map in permutations(range(7)):
    line_map = []
    for ell in range(7):
        image = frozenset(point_map[i] for i in LINES[ell])
        j = line_index.get(image)
        if j is None:
            break
        line_map.append(j)
    else:
        preserving.append(tuple(point_map) + tuple(7+j for j in line_map))
assert len(preserving) == 168
# This fixed bipartition-exchanging polarity preserves adjacency.
polarity = tuple(7 + (-i) % 7 for i in range(7)) + tuple((-j) % 7 for j in range(7))
autos = preserving + [tuple(polarity[x] for x in g) for g in preserving]
assert len(autos) == 336 and len(set(autos)) == 336
for g in autos:
    assert sorted(g) == list(range(14))
    for v in range(14):
        moved = 0
        for w in range(14):
            if adj[v] >> w & 1:
                moved |= 1 << g[w]
        assert moved == adj[g[v]]

# Reduced signed simplicial Lefschetz equals the trace in fourth homology:
# all other reduced rational homology groups vanish by the Morse certificate.
def image_and_orientation(s, g):
    image = 0
    permuted = []
    t = s
    while t:
        b = t & -t
        t ^= b
        i = b.bit_length() - 1
        a = g[i]
        image |= 1 << a
        permuted.append(a)
    parity = sum(a > b for i, a in enumerate(permuted) for b in permuted[i+1:]) & 1
    return image, -1 if parity else 1

def element_order(g):
    cur = tuple(range(14))
    k = 0
    while True:
        k += 1
        cur = tuple(g[i] for i in cur)
        if cur == tuple(range(14)):
            return k
        assert k <= 336

character = Counter()
traces = []
for index, g in enumerate(autos):
    signed_sum = -1  # empty face, in reduced simplicial Lefschetz formula
    for s in faces - {0}:
        image, orientation = image_and_orientation(s, g)
        if image == s:
            signed_sum += ((-1) if (s.bit_count()-1)%2 else 1) * orientation
    row = (int(index >= 168), element_order(g), signed_sum)
    character[row] += 1
    traces.append(signed_sum)
expected = {
    (0,1,8):1, (0,2,0):21, (0,3,-1):56, (0,4,0):42, (0,7,1):48,
    (1,2,-2):28, (1,6,1):56, (1,8,0):84,
}
assert dict(character) == expected, character
assert sum(traces) == 0
assert sum(x*x for x in traces) == 336

print('graph: 14 vertices, 28 edges, valency 4')
print('faces by size (including empty):', counts)
print('forbidden triples:', len(forbidden))
print('maximal-face dimensions and counts:', sorted(Counter(s.bit_count()-1 for s in facets).items()))
print('Morse pairs:', len(pairs), 'critical dimensions:', sorted(Counter(s.bit_count()-1 for s in unmatched).items()))
print('Hasse covering incidences:', cover_edges, 'acyclic topological sort:', visited, 'of', len(vertices))
print('mod-2 augmented boundary ranks:', tuple(boundary_ranks[k] for k in range(1,8)))
print('mod-2 reduced Betti numbers, dimensions 0..6:', betti)
print('automorphisms:', len(preserving), 'part-preserving +', len(autos)-len(preserving), 'part-swapping')
for (swap, order, tr), n in sorted(character.items()):
    print('character: swap=%d order=%d trace=%+d count=%d' % (swap, order, tr, n))
print('character inner product:', sum(x*x for x in traces), '/', len(traces), '=1')
print('character invariant average:', sum(traces), '/', len(traces), '=0')
print('ALL_CHECKS_PASS')
