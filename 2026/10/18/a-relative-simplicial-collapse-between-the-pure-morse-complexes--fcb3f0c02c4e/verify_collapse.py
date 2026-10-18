#!/usr/bin/env python3
"""Finite certificate verifier for a relative simplicial collapse of pure Morse complexes.

Run: python verify_collapse.py collapse_certificate.json
Standard library only. Conventions: 0-based vertices of a tetrahedron; nonempty
faces indexed in increasing (cardinality, lexicographic) order; Hasse pairs
indexed lexicographically by the ordered pair (smaller-face index, larger-face index).
Each simplicial face is the bitmask of its Hasse pairs.
"""
import itertools
import json
import sys
from collections import Counter


def hasse(full):
    vertices = range(4)
    faces = [tuple(s) for k in range(1, 5 if full else 4)
             for s in itertools.combinations(vertices, k)]
    index = {face: i for i, face in enumerate(faces)}
    pairs = sorted((index[small], index[large])
                   for large in faces
                   for small in itertools.combinations(large, len(large)-1)
                   if len(small) and small in index)
    return faces, pairs


def acyclic(mask, size, pairs):
    # Downward Hasse orientation except on the matched cover relations.
    outgoing = [[] for _ in range(size)]
    indegree = [0] * size
    for j, (small, large) in enumerate(pairs):
        if mask & (1 << j):
            small, large = large, small
        outgoing[large].append(small)
        indegree[small] += 1
    stack = [i for i, count in enumerate(indegree) if count == 0]
    removed = 0
    while stack:
        u = stack.pop()
        removed += 1
        for v in outgoing[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)
    return removed == size


def pure_faces(full):
    faces, pairs = hasse(full)
    maximal_size = 7 if full else 6
    facets = []
    def rec(start, face_mask, used_cells, count):
        if count == maximal_size:
            facets.append(face_mask)
            return
        for i in range(start, len(pairs)):
            u, v = pairs[i]
            cell_bits = (1 << u) | (1 << v)
            if used_cells & cell_bits:
                continue
            new_mask = face_mask | (1 << i)
            if acyclic(new_mask, len(faces), pairs):
                rec(i + 1, new_mask, used_cells | cell_bits, count + 1)
    rec(0, 0, 0, 0)
    complex_faces = {0}
    for facet in facets:
        subface = facet
        while subface:
            complex_faces.add(subface)
            subface = (subface - 1) & facet
    return faces, pairs, facets, complex_faces


def face_vector(complex_faces, max_size):
    count = Counter(face.bit_count() for face in complex_faces)
    return [count[i] for i in range(1, max_size + 1)]


def main(path):
    small_cells, small_edges, small_facets, a = pure_faces(False)
    big_cells, big_edges, big_facets, b = pure_faces(True)
    assert small_edges == big_edges[:len(small_edges)] or set(small_edges).issubset(set(big_edges))
    # Convert boundary-pair masks to full-Hasse-pair masks; the two indexings differ.
    small_edge_lookup = [big_edges.index(pair) for pair in small_edges]
    mapped_a = set()
    for mask in a:
        translated = 0
        for i, j in enumerate(small_edge_lookup):
            if mask & (1 << i): translated |= 1 << j
        mapped_a.add(translated)
    assert mapped_a <= b, "Pure boundary does not embed as assumed"
    assert len(small_facets) == len(big_facets) == 256
    f_a = face_vector(a, 6)
    f_b = face_vector(b, 7)
    assert f_a == [24, 216, 896, 1680, 1152, 256]
    assert f_b == [28, 300, 1544, 3680, 3672, 1600, 256]
    apex_indices = [i for i, (low, high) in enumerate(big_edges)
                    if len(big_cells[high]) == 4]
    assert len(apex_indices) == 4
    assert all((mask & sum(1 << i for i in apex_indices)).bit_count() <= 1 for mask in b)
    for apex in apex_indices:
        link = {(face ^ (1 << apex)) for face in b if face & (1 << apex)}
        assert len(link) == 1714
        assert face_vector(link, 6) == [21, 162, 500, 630, 336, 64]
        assert link <= mapped_a
    with open(path, encoding='utf-8') as file:
        cert = json.load(file)
    assert cert['schema_version'] == 1
    assert cert['apex_indices'] == apex_indices
    pairs_to_remove = cert['collapse_pairs']
    assert len(pairs_to_remove) == 3428
    assert len({x for pair in pairs_to_remove for x in pair}) == 6856
    current = set(b)
    up = {m: 0 for m in current}
    for upper in current:
        for bit in _bits(upper):
            lower = upper ^ bit
            if lower in current:
                up[lower] += 1
    for index, (lower, upper) in enumerate(pairs_to_remove):
        assert lower in current and upper in current, (index, 'missing face')
        assert lower not in mapped_a and upper not in mapped_a, (index, 'boundary face removed')
        assert (lower & upper) == lower and (upper ^ lower).bit_count() == 1, (index, 'non-cover pair')
        assert up[lower] == 1 and up[upper] == 0, (index, 'not a free elementary collapse', up[lower], up[upper])
        for removed in (upper, lower):
            current.remove(removed)
            for bit in _bits(removed):
                f = removed ^ bit
                if f in current:
                    up[f] -= 1
                    assert up[f] >= 0
            del up[removed]
    assert current == mapped_a
    print('Source complex: full tetrahedron; 15 nonempty cells; 28 Hasse pairs')
    print('Target complex: tetrahedral boundary; 14 nonempty cells; 24 Hasse pairs')
    print('Maximal gradient matchings:',len(big_facets),len(small_facets))
    print('Full pure face vector:', f_b)
    print('Boundary pure face vector:', f_a)
    print('Link face vector:', [21, 162, 500, 630, 336, 64])
    print('Relative elementary collapse pairs verified:',len(pairs_to_remove))
    print('Preserved boundary faces:',len(mapped_a)-1)
    print('Result: PASS; full pure Morse complex simplicially collapses onto boundary pure Morse complex')


def _bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit

if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python verify_collapse.py collapse_certificate.json')
    main(sys.argv[1])
