#!/usr/bin/env python3
"""Finite checks of a four-spine double-broom higher-independence theorem.

Uses only the standard library. Exact binary boundary ranks are corroboration,
not a replacement for the all-parameter homotopy argument.
"""
from itertools import combinations
from collections import defaultdict


def model(a, c):
    assert a >= 1 and c >= 1
    labels = ('u', 'v', 'w', 'z') + tuple('A%d' % j for j in range(a)) + tuple('C%d' % j for j in range(c))
    edges = [(0, 1), (1, 2), (2, 3)] + [(0, 4 + i) for i in range(a)] + [(3, 4 + a + j) for j in range(c)]
    neighbors = [set() for _ in labels]
    for p, q in edges:
        neighbors[p].add(q)
        neighbors[q].add(p)
    # For a forest, an induced component has >=3 vertices precisely when
    # it contains a three-vertex path. Enumerate those forbidden triples.
    forbidden = set()
    for center in range(len(labels)):
        for p, q in combinations(sorted(neighbors[center]), 2):
            forbidden.add((1 << p) | (1 << center) | (1 << q))
    return labels, sorted(forbidden)


def enumerate_faces(a, c):
    names, forbidden = model(a, c)
    n = len(names)
    faces = defaultdict(list)
    for mask in range(1 << n):
        if all(mask & triple != triple for triple in forbidden):
            faces[mask.bit_count() - 1].append(mask)
    return faces


def binary_rank(columns):
    pivots = {}
    for col in columns:
        while col:
            leading = col.bit_length() - 1
            if leading in pivots:
                col ^= pivots[leading]
            else:
                pivots[leading] = col
                break
    return len(pivots)


def reduced_betti(faces):
    keys = sorted(faces)
    ranks = {}
    for dimension in keys:
        if dimension < 0:
            continue
        row_position = {mask: i for i, mask in enumerate(faces[dimension - 1])}
        vectors = []
        for face in faces[dimension]:
            col = 0
            remaining = face
            while remaining:
                bit = remaining & -remaining
                remaining -= bit
                col ^= 1 << row_position[face ^ bit]
            vectors.append(col)
        ranks[dimension] = binary_rank(vectors)
    result = {k: len(faces[k]) - ranks.get(k, 0) - ranks.get(k + 1, 0)
              for k in keys if k >= 0}
    return {d: b for d, b in result.items() if b != 0}


def subcomplexes(a, c):
    faces = enumerate_faces(a, c)
    # v has index one. The link removes v from faces containing it.
    vbit = 1 << 1
    deletion = defaultdict(list)
    link = defaultdict(list)
    for dimension, masks in faces.items():
        for m in masks:
            if not (m & vbit):
                deletion[dimension].append(m)
            else:
                link[dimension - 1].append(m ^ vbit)
    return faces, deletion, link


def check(a, c):
    faces, deletion, link = subcomplexes(a, c)
    actual = reduced_betti(faces)
    d_actual = reduced_betti(deletion)
    l_actual = reduced_betti(link)
    expected = ({3: a * c - 1} if a * c > 1 else {})
    d_expected = ({3: (a - 1) * c} if a > 1 else {})
    l_expected = ({2: c - 1} if c > 1 else {})
    assert actual == expected, ('complex', a, c, actual, expected)
    assert d_actual == d_expected, ('deletion', a, c, d_actual, d_expected)
    assert l_actual == l_expected, ('link', a, c, l_actual, l_expected)
    # Independent reduced-Euler check against face counts, including empty face.
    reduced_euler = sum((-1) ** dimension * len(cells)
                        for dimension, cells in faces.items())
    assert reduced_euler == -(a * c - 1), ('Euler', a, c, reduced_euler)
    return sum(map(len, faces.values())), len(faces)


def main():
    checks = [(a, c) for a in range(1, 5) for c in range(1, 5)]
    checks += [(5, 3), (3, 5), (5, 5), (6, 2), (2, 6)]
    examined = 0
    for a, c in checks:
        face_count, _ = check(a, c)
        examined += face_count
    print('VERIFY_OK %d parameter pairs, %d faces, original/deletion/link GF(2) homology and Euler' %
          (len(checks), examined))

if __name__ == '__main__':
    main()
