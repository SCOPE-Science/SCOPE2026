"""Independent exhaustive model using the Hamilton-cycle LCF encoding.

Usage: python verify_b.py > verify_b.json
Python standard library only. Exhaustive finite verification.
"""
from collections import Counter
import json

n = 20
lcf = [10, 7, 4, -4, -7, 10, -4, 7, -7, 4] * 2
edges = {tuple(sorted((v, (v + 1) % n))) for v in range(n)}
edges |= {tuple(sorted((v, (v + lcf[v]) % n))) for v in range(n)}
assert len(edges) == 30
adjbits = [0] * n
for a, b in edges:
    adjbits[a] |= 1 << b
    adjbits[b] |= 1 << a
assert all(bits.bit_count() == 3 for bits in adjbits)
# Explicit isomorphism of the independent Hamilton-cycle encoding to GP(10,2).
phi = [0, 1, 8, 7, 14, 15, 16, 17, 18, 19, 10, 2, 9, 6, 13, 5, 12, 4, 11, 3]
gp_edges = set()
for j in range(10):
    gp_edges.add(tuple(sorted((j, (j + 1) % 10))))
    gp_edges.add((j, j + 10))
    gp_edges.add(tuple(sorted((j + 10, 10 + (j + 2) % 10))))
assert {tuple(sorted((phi[a], phi[b]))) for a, b in gp_edges} == edges


def feasible(delete):
    alive = ((1 << n) - 1) ^ delete
    positive = 0
    negative = 0
    unseen = alive
    while unseen:
        root = unseen & -unseen
        positive |= root
        frontier = [root]
        unseen ^= root
        while frontier:
            bit = frontier.pop()
            v = bit.bit_length() - 1
            myside = bool(positive & bit)
            neighbors = adjbits[v] & alive
            if (neighbors & (positive if myside else negative)):
                return False
            new = neighbors & unseen
            if myside:
                negative |= new
            else:
                positive |= new
            unseen ^= new
            while new:
                low = new & -new
                frontier.append(low)
                new ^= low
    return True

counts = Counter()
states = []
for s in range(1 << n):
    k = s.bit_count()
    if k > 6:
        continue
    if feasible(s):
        counts[k] += 1
        if k == 6:
            states.append(s)
assert [counts[k] for k in range(7)] == [0, 0, 0, 0, 0, 0, 3240]
# Independently derive adjacency from unordered state pairs, not moves.
r = len(states)
neighbors = [[] for _ in range(r)]
for i in range(r):
    s = states[i]
    for j in range(i + 1, r):
        if (s ^ states[j]).bit_count() == 2:
            neighbors[i].append(j)
            neighbors[j].append(i)
metric = Counter()
ecc = Counter()
witness = None
for i, s in enumerate(states):
    dist = [-1] * r
    dist[i] = 0
    frontier = [i]
    for v in frontier:
        for w in neighbors[v]:
            if dist[w] < 0:
                dist[w] = dist[v] + 1
                frontier.append(w)
    assert len(frontier) == r
    ecc[max(dist)] += 1
    for j, t in enumerate(states):
        h = 6 - (s & t).bit_count()
        delta = dist[j]
        metric[(h, delta)] += 1
        if delta > h and witness is None:
            witness = [list(q for q in range(n) if (s >> q) & 1),
                       list(q for q in range(n) if (t >> q) & 1), h, delta]
assert max(delta - h for h, delta in metric) == 1
result = {
    'representation': 'LCF[10,7,4,-4,-7,10,-4,7,-7,4]^2',
    'order': n, 'size': len(edges),
    'excluded_sizes_0_through_5': [counts[k] for k in range(6)],
    'minimum_deletion_size': 6,
    'number_of_minimum_deletion_sets': r,
    'exchange_edges': sum(map(len, neighbors)) // 2,
    'exchange_degree_histogram': {str(d): count for d, count in sorted(Counter(map(len, neighbors)).items())},
    'exchange_eccentricities': {str(d): count for d, count in sorted(ecc.items())},
    'ordered_distance_by_johnson_histogram': {f'{h},{d}': count for (h, d), count in sorted(metric.items())},
    'excess_distance_ordered_pairs': sum(count for (h, d), count in metric.items() if d > h),
    'first_excess_witness': witness
}
print(json.dumps(result, sort_keys=True, separators=(',', ':')))
