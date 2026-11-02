"""Independent labelled triangle-free-graph orbit and distance certificate.

Run: python3 verify_triangle_orbits.py.  Standard library only.
Uses the forbidden-triangle condition rather than Petersen domination.
BFS is performed once per S5 orbit, not once per labelled state.
"""
from collections import Counter, deque
from itertools import combinations, permutations

edges = list(combinations(range(5), 2))
edge_index = {pair: j for j, pair in enumerate(edges)}
triangle_masks = [sum(1 << edge_index[e] for e in combinations(t, 2))
                  for t in combinations(range(5), 3)]


def admissible(mask):
    return mask.bit_count() >= 3 and all(mask & t != t for t in triangle_masks)

states = set(filter(admissible, range(1024)))
assert len(states) == 332
assert Counter(x.bit_count() for x in states) == {3:110, 4:140, 5:72, 6:10}
neighbor_map = {
    x: tuple(x ^ (1 << j) for j in range(10) if x ^ (1 << j) in states)
    for x in states
}
assert sum(len(ns) for ns in neighbor_map.values()) == 1960


def distances_from(source):
    dist = {source: 0}
    queue = deque([source])
    while queue:
        x = queue.popleft()
        for y in neighbor_map[x]:
            if y not in dist:
                dist[y] = dist[x] + 1
                queue.append(y)
    return dist

permutations_of_edges = []
for p in permutations(range(5)):
    permutations_of_edges.append(tuple(edge_index[tuple(sorted((p[u], p[v])))]
                                       for u, v in edges))


def permute(mask, mapping):
    result = 0
    for j in range(10):
        if mask & (1 << j):
            result |= (1 << mapping[j])
    return result

remaining = set(states)
orbits = []
while remaining:
    x = min(remaining)
    orbit = {permute(x, p) for p in permutations_of_edges}
    assert orbit <= remaining
    remaining -= orbit
    orbits.append(orbit)
assert len(orbits) == 10
assert Counter(len(o) for o in orbits) == {60: 4, 10:1, 12:1, 15:1, 5:1, 20:1, 30:1}

pair_dist_twice = Counter()
pair_defect_twice = Counter()
ecc = Counter()
diametral_directed = 0
orbit_rows = []
for orbit in sorted(orbits, key=lambda o:(min(s.bit_count() for s in o), len(o), min(o))):
    rep = min(orbit)
    dist = distances_from(rep)
    assert len(dist) == 332
    e = max(dist.values())
    size = len(orbit)
    if size == 12 and rep.bit_count() == 5:
        # This entire orbit comprises labelled five-cycles.
        assert all(distance == (rep ^ target).bit_count()
                   for target, distance in dist.items())
    ecc[e] += size
    for dest, d in dist.items():
        if dest != rep:
            pair_dist_twice[d] += size
            defect = d - (rep ^ dest).bit_count()
            assert defect in (0, 2)
            pair_defect_twice[defect] += size
            if d == 10:
                assert (rep ^ dest) == 1023
                assert rep.bit_count() == dest.bit_count() == 5
                diametral_directed += size
    shell = tuple(Counter(dist.values())[j] for j in range(e + 1))
    orbit_rows.append((rep, rep.bit_count(), size, len(neighbor_map[rep]), e, shell))

assert ecc == {8:100, 9:220, 10:12}
assert all(k % 2 == 0 for k in pair_dist_twice.values())
assert all(k % 2 == 0 for k in pair_defect_twice.values())
assert [pair_dist_twice[d] // 2 for d in range(1, 11)] == [
     980, 3210, 7070, 11585, 13170, 10970, 5810, 1875, 270, 6]
assert {k:v//2 for k,v in pair_defect_twice.items()} == {0:54211, 2:735}
assert diametral_directed == 12
print('ORBIT_COUNT 10 S5_SIZE=120')
for rep, ecount, size, degree, e, shell in orbit_rows:
    print('ORBIT', rep, 'edges', ecount, 'size', size, 'degree', degree,
          'ecc', e, 'shells', ','.join(map(str,shell)))
print('ORBIT_CERTIFICATE_PASS states=332 edges=980 radius=8 diameter=10')
print('DIAMETRAL_PAIRS_ARE_SIX_COMPLEMENTARY_C5_PAIRS')
print('TRIANGLE_ORBIT_CERTIFICATE_PASS')
