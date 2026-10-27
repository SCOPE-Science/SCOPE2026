#!/usr/bin/env python3
"""Independent check of the optimum metric-basis census of KG(7,3).

The distance to any fixed triple is uniquely determined by its
intersection cardinality: intersections 3, 0, 2, 1 give distances
0, 1, 2, 3 respectively. No graph-distance routines are needed.
"""
from itertools import combinations
from collections import Counter

triples = [v for v in range(1 << 7) if v.bit_count() == 3]
assert len(triples) == 35

def resolves(chosen):
    seen = set()
    for t in triples:
        signature = tuple((t & c).bit_count() for c in chosen)
        if signature in seen:
            return False
        seen.add(signature)
    return True

bases = []
for k in (4, 5):
    count = 0
    for inds in combinations(range(35), k):
        if resolves(tuple(triples[i] for i in inds)):
            count += 1
            if k == 5:
                bases.append(sum(1 << i for i in inds))
    print(f'minimum_test_k={k} successful={count}')

assert len(bases) == 149184
index = {bits: i for i, bits in enumerate(bases)}
parent = list(range(len(bases)))
size = [1] * len(bases)

def root(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def unite(a, b):
    a, b = root(a), root(b)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]

edges = 0
deg_hist = Counter()
for i, base in enumerate(bases):
    selected = [j for j in range(35) if base & (1 << j)]
    missing = [j for j in range(35) if not (base & (1 << j))]
    degree = 0
    for outgoing in selected:
        without = base ^ (1 << outgoing)
        for incoming in missing:
            neighbor = index.get(without | (1 << incoming))
            if neighbor is not None:
                degree += 1
                if neighbor > i:
                    edges += 1
                    unite(i, neighbor)
    deg_hist[degree] += 1

comps = Counter(root(i) for i in range(len(bases)))
print(f'minimum_bases={len(bases)} exchange_edges={edges}')
print(f'exchange_components={len(comps)} component_sizes={sorted(comps.values())}')
print(f'degree_sum={sum(k*v for k, v in deg_hist.items())} min_degree={min(deg_hist)} max_degree={max(deg_hist)}')
assert len(comps) == 1
assert edges == 6331500
assert sum(k*v for k, v in deg_hist.items()) == 2 * edges

# Two explicit six-step witnesses, independently checked using exchanges
# generated directly from bitsets (without stored exchange-graph edges).
from collections import deque
for start_triples, goal_triples in (
    ((7, 11, 21, 73, 112), (38, 42, 52, 81, 104)),
    ((7, 11, 37, 73, 97), (22, 26, 52, 88, 112)),
):
    initial = sum(1 << triples.index(v) for v in start_triples)
    terminal = sum(1 << triples.index(v) for v in goal_triples)
    assert initial in index and terminal in index
    q = deque([initial])
    dist = {initial: 0}
    while q and terminal not in dist:
        bits = q.popleft()
        for j in range(35):
            if not (bits & (1 << j)):
                continue
            fewer = bits ^ (1 << j)
            for k in range(35):
                if bits & (1 << k):
                    continue
                nxt = fewer | (1 << k)
                if nxt in index and nxt not in dist:
                    dist[nxt] = dist[bits] + 1
                    q.append(nxt)
    assert dist[terminal] == 6
    print(f'certified_pair_distance={dist[terminal]} from={start_triples} to={goal_triples}')

# Independent check of the complete S_7 orbit partition using six adjacent
# transpositions, separate from the C++ orbit machinery.
orbit_parent = list(range(len(bases)))
orbit_size = [1] * len(bases)
def orbit_root(x):
    while orbit_parent[x] != x:
        orbit_parent[x] = orbit_parent[orbit_parent[x]]
        x = orbit_parent[x]
    return x
def orbit_join(a, b):
    a, b = orbit_root(a), orbit_root(b)
    if a == b:
        return
    if orbit_size[a] < orbit_size[b]:
        a, b = b, a
    orbit_parent[b] = a
    orbit_size[a] += orbit_size[b]
for pivot in range(6):
    pmap = []
    for trip in triples:
        x, y = (trip >> pivot) & 1, (trip >> (pivot+1)) & 1
        image = trip ^ ((1 << pivot) | (1 << (pivot+1))) if x != y else trip
        pmap.append(triples.index(image))
    for i, basis in enumerate(bases):
        image = 0
        for j in range(35):
            if basis & (1 << j):
                image |= 1 << pmap[j]
        orbit_join(i, index[image])
orbit_counts = Counter(orbit_root(i) for i in range(len(bases)))
size_hist = Counter(orbit_counts.values())
print(f'ground_symbol_symmetry_orbits={len(orbit_counts)} sizes={sorted(size_hist.items())}')
assert len(orbit_counts) == 48
assert size_hist == Counter({420: 1, 504: 1, 840: 1, 1260: 5, 2520: 24, 5040: 16})
