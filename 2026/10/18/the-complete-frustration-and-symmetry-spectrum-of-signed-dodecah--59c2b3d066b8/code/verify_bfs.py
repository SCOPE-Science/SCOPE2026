#!/usr/bin/env python3
"""Exact frustration profile of the signed dodecahedral graph.

This standalone checker uses breadth-first search on the even subsets of
vertices of the icosahedron, the planar dual of the dodecahedron.  No
nonstandard Python packages are required.
"""
from collections import Counter, deque
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]

def edges():
    n, s = 0, 11
    u = lambda i: 1 + i % 5
    l = lambda i: 6 + i % 5
    ed = set()
    def add(a, b):
        assert a != b
        ed.add(tuple(sorted((a, b))))
    for i in range(5):
        add(n, u(i))
        add(s, l(i))
        add(u(i), u(i + 1))
        add(l(i), l(i + 1))
        add(u(i), l(i))
        add(u(i), l(i - 1))
    return tuple(sorted(ed))

E = edges()
assert len(E) == 30
assert all(sum(v in e for e in E) == 5 for v in range(12))

D = [-1] * 4096
D[0] = 0
q = deque([0])
while q:
    mask = q.popleft()
    for a, b in E:
        new = mask ^ (1 << a) ^ (1 << b)
        if D[new] < 0:
            D[new] = D[mask] + 1
            q.append(new)
assert sum(x >= 0 for x in D) == 2048
assert all((D[m] >= 0) == (m.bit_count() % 2 == 0) for m in range(4096))
H = Counter(D[m] for m in range(4096) if D[m] >= 0)
assert H == {0: 1, 1: 30, 2: 315, 3: 1058, 4: 577, 5: 66, 6: 1}
assert [m for m in range(4096) if D[m] == 6] == [4095]

# Three explicit graph automorphisms; their closure has order 120.
generators = [
    (0,2,3,4,5,1,7,8,9,10,6,11),
    (0,1,5,4,3,2,10,9,8,7,6,11),
    (1,0,2,6,10,5,3,7,11,9,4,8),
]
for g in generators:
    assert sorted(g) == list(range(12))
    assert {tuple(sorted((g[a], g[b]))) for a, b in E} == set(E)
identity = tuple(range(12))
autos = {identity}
q = deque([identity])
while q:
    p = q.popleft()
    for g in generators:
        r = tuple(g[p[i]] for i in range(12))
        if r not in autos:
            autos.add(r)
            q.append(r)
assert len(autos) == 120

def image(mask, p):
    return sum(1 << p[v] for v in range(12) if mask & (1 << v))

remaining = {m for m in range(4096) if D[m] >= 0}
orbits = []
while remaining:
    seed = min(remaining)
    orb = {image(seed, g) for g in autos}
    assert orb <= remaining
    assert {D[m] for m in orb} == {D[seed]}
    remaining -= orb
    orbits.append((seed, len(orb), seed.bit_count(), D[seed]))
assert len(orbits) == 46
OH = Counter(row[3] for row in orbits)
assert OH == {0:1,1:1,2:7,3:20,4:13,5:3,6:1}

with (ROOT / 'data' / 'frustration_distances.csv').open('w', encoding='utf8', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['face_mask_decimal', 'negative_faces', 'minimum_negative_edges'])
    for mask in range(4096):
        if D[mask] >= 0:
            w.writerow([mask, mask.bit_count(), D[mask]])
with (ROOT / 'data' / 'icosahedron_orbits.csv').open('w', encoding='utf8', newline='') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['representative_mask_decimal', 'orbit_size', 'negative_faces', 'minimum_negative_edges'])
    w.writerows(orbits)

print('icosahedron vertices=12 edges=30 degree=5')
print('even-face switching classes=2048')
print('frustration histogram=', sorted(H.items()))
print('maximum frustration=6; unique face mask=4095')
print('icosahedral automorphism group order=', len(autos))
print('switching-isomorphism orbits=',len(orbits),'; orbit histogram=',sorted(OH.items()))
print('certificate rows=', 2048, 'orbit certificate rows=',len(orbits))
