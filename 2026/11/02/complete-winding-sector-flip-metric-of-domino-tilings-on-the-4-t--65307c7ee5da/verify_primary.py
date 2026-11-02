#!/usr/bin/env python3
"""Exhaustive toroidal 4-by-6 domino-flip graph verifier (standard library only).

State enumeration: recursively match the lowest-numbered uncovered cell.
Move enumeration: exchange parallel dimers on each of 24 elementary torus faces.
Shortest paths: breadth-first search from every state in each component.
"""
from collections import Counter, deque
import json

M, N = 4, 6
V = M * N

def vertex(r, c):
    return (r % M) * N + (c % N)

neighbors = [set() for _ in range(V)]
for r in range(M):
    for c in range(N):
        v = vertex(r, c)
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            neighbors[v].add(vertex(r + dr, c + dc))

edges = sorted((u, v) for u in range(V) for v in neighbors[u] if u < v)
assert len(edges) == 48
edge_id = {e: i for i, e in enumerate(edges)}

def eid(a, b):
    return edge_id[(min(a, b), max(a, b))]

faces = []
for r in range(M):
    for c in range(N):
        a, b = vertex(r, c), vertex(r, c + 1)
        d, e = vertex(r + 1, c), vertex(r + 1, c + 1)
        horizontal = (1 << eid(a, b)) | (1 << eid(d, e))
        vertical = (1 << eid(a, d)) | (1 << eid(b, e))
        assert horizontal & vertical == 0
        faces.append((horizontal, vertical))
assert len(faces) == 24 and len(set(faces)) == 24

states = []
def enumerate_matchings(uncovered, edge_mask):
    if not uncovered:
        states.append(edge_mask)
        return
    a = (uncovered & -uncovered).bit_length() - 1
    for b in sorted(neighbors[a]):
        if uncovered & (1 << b):
            enumerate_matchings(uncovered ^ (1 << a) ^ (1 << b), edge_mask | (1 << eid(a, b)))

enumerate_matchings((1 << V) - 1, 0)
assert len(states) == len(set(states)) == 3108
assert all(x.bit_count() == 12 for x in states)
lookup = {state: i for i, state in enumerate(states)}

adj = [set() for _ in states]
for i, matching in enumerate(states):
    for horizontal, vertical in faces:
        if matching & horizontal == horizontal:
            target = (matching ^ horizontal) | vertical
        elif matching & vertical == vertical:
            target = (matching ^ vertical) | horizontal
        else:
            continue
        assert target in lookup and target != matching
        adj[i].add(lookup[target])
assert all(i in adj[j] for i, ns in enumerate(adj) for j in ns)

# Signed seam flow relative to the horizontal base matching, which crosses neither seam.
horizontal_seam = [(eid(vertex(r, 5), vertex(r, 0)), (-1) ** (r + 5)) for r in range(M)]
vertical_seam = [(eid(vertex(3, c), vertex(0, c)), (-1) ** (3 + c)) for c in range(N)]
def flux(mask):
    return (sum(sign for edge, sign in horizontal_seam if mask >> edge & 1),
            sum(sign for edge, sign in vertical_seam if mask >> edge & 1))

components = []
unseen = set(range(len(states)))
while unseen:
    start = min(unseen)
    seen = {start}
    queue = deque([start])
    unseen.remove(start)
    while queue:
        current = queue.popleft()
        for j in adj[current]:
            if j not in seen:
                seen.add(j)
                unseen.remove(j)
                queue.append(j)
    components.append(sorted(seen))

records = []
for comp in components:
    sector = {flux(states[i]) for i in comp}
    assert len(sector) == 1, sector
    phi = next(iter(sector))
    degrees = Counter(len(adj[i]) for i in comp)
    distances = Counter()
    eccentricities = Counter()
    for origin in comp:
        distance = {origin: 0}
        queue = deque([origin])
        while queue:
            i = queue.popleft()
            for j in adj[i]:
                if j not in distance:
                    distance[j] = distance[i] + 1
                    queue.append(j)
        assert len(distance) == len(comp)
        distances.update(distance.values())
        eccentricities[max(distance.values())] += 1
    assert sum(distances.values()) == len(comp) ** 2
    weighted = sum(d * count for d, count in distances.items())
    assert weighted % 2 == 0
    records.append(dict(flux=list(phi), vertices=len(comp), edges=sum(len(adj[i]) for i in comp)//2,
                        radius=min(eccentricities), diameter=max(eccentricities), wiener=weighted//2,
                        degree_histogram={str(k): degrees[k] for k in sorted(degrees)},
                        distance_histogram={str(k): distances[k] for k in sorted(distances)},
                        eccentricity_histogram={str(k): eccentricities[k] for k in sorted(eccentricities)}))
records.sort(key=lambda r: r['flux'])
assert len(records) == 15 and len({tuple(r['flux']) for r in records}) == 15
assert [(r['flux'], r['vertices']) for r in records] == [
    ([-2,0],1), ([-1,-1],24), ([-1,0],152), ([-1,1],24),
    ([0,-3],1), ([0,-2],48), ([0,-1],576), ([0,0],1456),
    ([0,1],576), ([0,2],48), ([0,3],1), ([1,-1],24),
    ([1,0],152), ([1,1],24), ([2,0],1)]
assert sum(r['vertices'] for r in records) == 3108
assert sum(r['edges'] for r in records) == 9048
assert sum(r['wiener'] for r in records) == 10795608
assert sorted(Counter(r['vertices'] for r in records).items()) == [(1,4),(24,4),(48,2),(152,2),(576,2),(1456,1)]
assert max(r['diameter'] for r in records) == 20
result = dict(graph='C4 Cartesian C6: twenty-four elementary-face flips',
              vertices=3108, edges=9048, components=15,
              connected_pairs_wiener=10795608, sectors=records)
print(json.dumps(result, ensure_ascii=True, indent=2, sort_keys=True))
print('PRIMARY_CERTIFICATE_OK')
