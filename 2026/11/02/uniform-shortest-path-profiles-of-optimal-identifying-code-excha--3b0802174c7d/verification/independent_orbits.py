#!/usr/bin/env python3
"""Independent sensor-signature census and symmetry-orbit shortest-path test for Q4.
Run: python3 verification/independent_orbits.py. Standard Python 3 only.
"""
from collections import Counter, deque
from itertools import combinations, permutations

V = tuple(range(16))

def sensor_works_on(sensor, place):
    return (sensor ^ place).bit_count() <= 1

def is_identifying(sensors):
    # Signatures are *index sets* in the ordered sensor tuple, not ball bitmasks.
    signatures = []
    for place in V:
        responding = tuple(i for i, sensor in enumerate(sensors)
                           if sensor_works_on(sensor, place))
        if not responding:
            return False
        signatures.append(responding)
    return len(set(signatures)) == 16

# The whole space of smaller configurations is exhaustively checked.
for size in range(0, 7):
    assert not any(is_identifying(t) for t in combinations(V, size))
states = set(combinations(V, 7))
states = {s for s in states if is_identifying(s)}
assert len(states) == 960
assert all(len(s) == 7 for s in states)

# Generate the full 16 x 24 automorphism group, with no graph-library calls.
automorphisms = []
for perm in permutations(range(4)):
    for translate in V:
        image = tuple(translate ^ sum(((v >> bit) & 1) << perm[bit]
                                       for bit in range(4)) for v in V)
        automorphisms.append(image)
assert len(set(automorphisms)) == 384

remaining = set(states)
orbits = []
while remaining:
    rep = min(remaining)
    orbit = {tuple(sorted(image[v] for v in rep)) for image in automorphisms}
    assert orbit <= states
    remaining -= orbit
    orbits.append((rep, orbit))
assert sorted(len(o) for _, o in orbits) == [192, 384, 384]

# Reconstruct the exchange adjacency directly using seven-common-point tests,
# rather than toggling bit masks; BFS only the orbit representatives.
states = sorted(states)
adj = {a: set() for a in states}
for a in states:
    a_set = set(a)
    for old in a:
        for new in V:
            if new not in a_set:
                b = tuple(sorted((a_set - {old}) | {new}))
                if b in adj:
                    adj[a].add(b)
assert all(len(v) == 9 for v in adj.values())
assert sum(map(len, adj.values())) // 2 == 4320
shell = (1, 9, 35, 132, 300, 338, 130, 15)
for rep, orbit in orbits:
    visited = {rep: 0}
    queue = deque([rep])
    while queue:
        a = queue.popleft()
        for b in adj[a]:
            if b not in visited:
                visited[b] = visited[a] + 1
                queue.append(b)
    assert len(visited) == 960
    counts = Counter(visited.values())
    assert tuple(counts[d] for d in range(8)) == shell
print('INDEPENDENT_ORBIT_CERTIFICATE_PASS')
print('orbit_sizes=', sorted(len(o) for _, o in orbits))
print('number_of_orbits=', len(orbits), 'shell=', shell)
