"""Exact finite certificate for total-domination reconfiguration on KG(5,2).

Run: python3 verify_petersen_direct.py.  Standard library only.
All 2^10 candidate subsets are tested directly against open neighborhoods.
"""
from collections import Counter, deque
from itertools import combinations

vertices = list(combinations(range(5), 2))
neighbor_masks = []
for i, e in enumerate(vertices):
    neighbor_masks.append(sum(1 << j for j, f in enumerate(vertices)
                              if set(e).isdisjoint(f)))
assert all(x.bit_count() == 3 for x in neighbor_masks)


def total_dominates(mask):
    return all(mask & neighbors for neighbors in neighbor_masks)


def build(cap):
    states = [mask for mask in range(1 << 10)
              if mask.bit_count() <= cap and total_dominates(mask)]
    state_set = set(states)
    adjacency = {s: [s ^ (1 << j) for j in range(10)
                     if (s ^ (1 << j)) in state_set] for s in states}
    assert all(s in adjacency[t] for s, adj in adjacency.items() for t in adj)
    return states, adjacency


def bfs(start, adjacency):
    dist = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


minimal = [s for s in range(1 << 10) if total_dominates(s)
           and all(not total_dominates(s & ~(1 << j))
                   for j in range(10) if s & (1 << j))]
assert Counter(s.bit_count() for s in minimal) == {4: 10, 5: 12, 6: 5}
assert min(x.bit_count() for x in minimal) == 4
print('MINIMAL_TDS 4:10 5:12 6:5')

expected_components = {4: [1] * 10, 5: [7] * 10 + [1] * 12,
                       6: [217] + [1] * 5, 7: [332]}
for cap in range(4, 8):
    states, adj = build(cap)
    remaining = set(states)
    components = []
    while remaining:
        root = next(iter(remaining))
        component = set(bfs(root, adj))
        components.append(len(component))
        remaining -= component
    assert sorted(components, reverse=True) == sorted(expected_components[cap], reverse=True)
    print(f'CAP_{cap} states={len(states)} components={len(components)} largest={max(components)}')

states, adj = build(7)
assert len(states) == 332
assert sum(len(adj[s]) for s in states) // 2 == 980
assert Counter(s.bit_count() for s in states) == {4: 10, 5: 72, 6: 140, 7: 110}
assert Counter(len(adj[s]) for s in states) == {4: 25, 5: 72, 6: 160, 7: 60, 8: 15}

pair_counts = Counter()
stretch = Counter()
eccentricities = Counter()
diametral_pairs = []
for a in states:
    distances = bfs(a, adj)
    assert len(distances) == 332
    eccentricities[max(distances.values())] += 1
    for b, distance in distances.items():
        if a < b:
            pair_counts[distance] += 1
            defect = distance - (a ^ b).bit_count()
            stretch[defect] += 1
            assert defect in (0, 2)
            if distance == 10:
                diametral_pairs.append((a, b))

assert eccentricities == {8: 100, 9: 220, 10: 12}
assert pair_counts == {1:980, 2:3210, 3:7070, 4:11585, 5:13170,
                       6:10970, 7:5810, 8:1875, 9:270, 10:6}
assert stretch == {0: 54211, 2: 735}
assert len(diametral_pairs) == 6
assert all(a.bit_count() == b.bit_count() == 5 and (a ^ b) == 1023
           for a, b in diametral_pairs)
print('DIRECT_DISTANCE_PASS states=332 edges=980 radius=8 diameter=10')
print('ECC 8:100 9:220 10:12')
print('UNORDERED_DISTANCE_HISTOGRAM', *[pair_counts[i] for i in range(1, 11)])
print('HAMMING_DEFECT 0:54211 2:735')
print('COMPLEMENTARY_C5_DIAMETRAL_PAIRS', len(diametral_pairs))
print('DIRECT_PETERSEN_TDS_CERTIFICATE_PASS')
