#!/usr/bin/env python3
"""Reconstruct and verify the Clebsch 2-independence Morse certificate.

Usage: python3 verify.py (with certificate.json in the same directory).
Uses the Python standard library only.
"""
import json
from pathlib import Path
from collections import Counter, deque
from itertools import permutations

CERT = json.loads((Path(__file__).parent / 'certificate.json').read_text(encoding='utf-8'))
V = [v for v in range(32) if v.bit_count() % 2 == 0]
assert CERT['vertices_even_mask'] == V and len(V) == 16
E = [(i,j) for i in range(16) for j in range(i+1,16)
     if (V[i] ^ V[j]).bit_count() == 4]
assert CERT['edge_vertex_indices'] == [list(e) for e in E] and len(E) == 40
N = [0] * 16
for a,b in E:
    N[a] |= 1 << b
    N[b] |= 1 << a
faces = set()
for mask in range(1,1 << 16):
    if all((N[i] & mask).bit_count() <= 1
           for i in range(16) if mask & (1 << i)):
        faces.add(mask)
assert len(faces) == 2142
f_vector = [sum(s.bit_count() == d+1 for s in faces) for d in range(8)]
assert f_vector == [16,120,400,660,576,280,80,10], f_vector

order = CERT['order']
assert sorted(order) == list(range(16))
reconstructed = []
unpaired = set(faces)
for i in order:
    bit = 1 << i
    stage = [(low, low | bit) for low in sorted(unpaired)
             if not (low & bit) and (low | bit) in unpaired]
    for low, high in stage:
        unpaired.remove(low)
        unpaired.remove(high)
    reconstructed.extend(stage)
assert set(reconstructed) == set(map(tuple, CERT['pairs']))
assert sorted(unpaired) == CERT['critical'] == [1,61696]
assert len(reconstructed) == 1070

# Forman acyclicity: for every facet incidence, reverse just the matched edge.
matched = set(reconstructed)
out = {v: [] for v in faces}
indeg = {v: 0 for v in faces}
for high in faces:
    for i in range(16):
        if high & (1 << i):
            low = high ^ (1 << i)
            if low == 0:
                continue
            src, dst = (low, high) if (low, high) in matched else (high, low)
            out[src].append(dst)
            indeg[dst] += 1
q = deque(x for x in faces if indeg[x] == 0)
visited = 0
while q:
    src = q.popleft()
    visited += 1
    for dst in out[src]:
        indeg[dst] -= 1
        if indeg[dst] == 0:
            q.append(dst)
assert visited == len(faces), (visited, len(faces))
assert sum(len(v) for v in out.values()) == 9280

ix = {v:i for i,v in enumerate(V)}
def automorphism(translation, permutation):
    images = []
    for v in V:
        w = translation
        for i,j in enumerate(permutation):
            if v & (1 << i):
                w ^= 1 << j
        images.append(ix[w])
    assert len(set(images)) == 16
    for a,b in E:
        assert (V[images[a]] ^ V[images[b]]).bit_count() == 4
    return images

def induced_reduced_lefschetz(mapping):
    total = -1  # Subtract the trace on the augmented degree-zero constant chain.
    for face in faces:
        indices = [i for i in range(16) if face & (1 << i)]
        targets = [mapping[i] for i in indices]
        if sorted(targets) != indices:
            continue
        sign = (-1) ** sum(targets[i] > targets[j]
                           for i in range(len(targets))
                           for j in range(i+1,len(targets)))
        total += (-1) ** (len(indices)-1) * sign
    return total

sign_counts = Counter()
for t in V:
    for p in permutations(range(5)):
        sign = (-1) ** sum(p[i] > p[j] for i in range(5)
                            for j in range(i+1,5))
        got = induced_reduced_lefschetz(automorphism(t, p))
        assert got == sign, (t,p,got,sign)
        sign_counts[got] += 1
assert sign_counts == {1:960,-1:960}
print('PASS: 16 vertices, 40 edges, f =',f_vector)
print('PASS: 1070 unique Morse pairs, two critical cells (dimensions 0, 4)')
print('PASS: 9280 Hasse edges, oriented matching graph acyclic')
print('PASS: 1920 automorphism characters, each equals coordinate sign')
print('CONCLUSION: 2-independence complex is S^4; H4 action is sign of S5')
