#!/usr/bin/env python3
"""Finite certificate for the ordinary independence complex of the Pappus graph."""
from collections import Counter, deque
import json

N = 18
LCF = [5, 7, -7, 7, -7, -5] * 3
ORDER = [9, 6, 12, 3, 4, 7, 13, 15, 1, 5, 14, 0, 2, 17, 16, 11, 8, 10]
# Explicit map to the incidence presentation used by verify_independent.py.
MAP = [0, 13, 7, 17, 6, 11, 4, 10, 5, 15, 8, 16, 2, 14, 3, 12, 1, 9]
LINES = [(0, 1, 2), (3, 4, 5), (0, 4, 6), (3, 1, 6),
         (0, 5, 7), (3, 2, 7), (1, 5, 8), (4, 2, 8), (6, 7, 8)]

def edges_lcf():
    e = set()
    for i in range(N):
        for j in ((i + 1) % N, (i + LCF[i]) % N):
            assert i != j
            e.add(tuple(sorted((i, j))))
    return e

def edges_incidence():
    return {tuple(sorted((p, 9 + k))) for k, line in enumerate(LINES) for p in line}

def faces_independent(edges):
    adj = [0] * N
    for i, j in edges:
        adj[i] |= 1 << j
        adj[j] |= 1 << i
    assert all(x.bit_count() == 3 for x in adj)
    return {s for s in range(1 << N) if all((s & (1 << i)) == 0 or (s & adj[i]) == 0 for i in range(N))}

def morse_match(faces):
    active = set(faces)
    pairs = set()
    for v in ORDER:
        bit = 1 << v
        candidates = [a for a in active if not (a & bit) and (a | bit) in active]
        for low in candidates:
            high = low | bit
            assert low in active and high in active
            active.remove(low)
            active.remove(high)
            pairs.add((low, high))
    return active, pairs

def check_acyclic_nonempty(faces, pairs):
    vertices = faces - {0}
    matched = {(a, b) for a, b in pairs if a != 0}
    assert len(matched) == len(pairs) - 1, 'Exactly one empty-face match needed'
    assert len({x for p in matched for x in p}) == 2 * len(matched)
    degree = {face: 0 for face in vertices}
    nexts = {face: [] for face in vertices}
    incidences = 0
    for high in vertices:
        for k in range(N):
            if not high & (1 << k):
                continue
            low = high & ~(1 << k)
            if not low:
                continue
            assert low in vertices
            source, target = (low, high) if (low, high) in matched else (high, low)
            degree[target] += 1
            nexts[source].append(target)
            incidences += 1
    ready = deque(v for v, d in degree.items() if d == 0)
    count = 0
    while ready:
        curr = ready.popleft()
        count += 1
        for target in nexts[curr]:
            degree[target] -= 1
            if degree[target] == 0:
                ready.append(target)
    assert count == len(vertices), 'Matching has a closed gradient path'
    return incidences, count

def main():
    edges = edges_lcf()
    assert len(edges) == 27
    assert sorted(MAP) == list(range(N))
    mapped = {tuple(sorted((MAP[i], MAP[j]))) for i, j in edges}
    assert mapped == edges_incidence(), 'LCF graph not isomorphic to Pappus incidence model'
    faces = faces_independent(edges)
    assert len(faces) == 2598
    fvec = [sum(face.bit_count() == k for face in faces) for k in range(1, 10)]
    assert fvec == [18, 126, 438, 801, 756, 348, 90, 18, 2]
    critical_augmented, pairs = morse_match(faces)
    assert len(pairs) == 1294
    expected_masks = [42113, 73873, 75040, 83985, 84004,
                      147748, 148516, 149776, 164996, 166148]
    assert sorted(critical_augmented) == expected_masks
    assert len(critical_augmented) == 10
    assert {s.bit_count() for s in critical_augmented} == {5}
    assert (0, 1 << ORDER[0]) in pairs
    ordinary_critical = critical_augmented | {1 << ORDER[0]}
    assert Counter(s.bit_count() - 1 for s in ordinary_critical) == {0: 1, 4: 10}
    incidence_count, sorted_count = check_acyclic_nonempty(faces, pairs)
    assert incidence_count == 11430, incidence_count
    assert sorted_count == len(faces) - 1
    print(json.dumps({'result': 'PASS', 'vertices': N, 'edges': len(edges),
                      'nonempty_faces': len(faces) - 1, 'f_vector': fvec,
                      'ordinary_matched_pairs': len(pairs) - 1,
                      'critical_cells': {'dim0': 1, 'dim4': 10},
                      'directed_incidences': incidence_count,
                      'acyclic_toposort_vertices': sorted_count,
                      'explicit_graph_isomorphism': MAP}, sort_keys=True))

if __name__ == '__main__':
    main()
