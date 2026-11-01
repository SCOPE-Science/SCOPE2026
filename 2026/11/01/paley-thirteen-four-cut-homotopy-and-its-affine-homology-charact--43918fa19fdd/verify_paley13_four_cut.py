#!/usr/bin/env python3
"""Exhaustive finite certificate for the Paley(13) ordinary four-cut complex.
Uses only Python 3 standard library. No external inputs or packages.
"""
from itertools import combinations
from collections import Counter, deque
from math import comb

N = 13
FULL = (1 << N) - 1
RESIDUES = {pow(i, 2, N) for i in range(1, N)}
ADJ = [sum(1 << j for j in range(N) if j != i and (j-i) % N in RESIDUES)
       for i in range(N)]
PIVOTS = [2, 9, 7, 5, 3, 12, 6, 8, 0, 11, 4, 1, 10]


def components(mask):
    count = 0
    unseen = mask
    while unseen:
        count += 1
        frontier = unseen & -unseen
        unseen ^= frontier
        while frontier:
            vertex_bit = frontier & -frontier
            frontier ^= vertex_bit
            i = vertex_bit.bit_length() - 1
            neighbors = ADJ[i] & unseen
            frontier |= neighbors
            unseen ^= neighbors
    return count


def disconnected4():
    return {sum(1 << j for j in c) for c in combinations(range(N), 4)
            if components(sum(1 << j for j in c)) != 1}


def generate_by_facets(disconnected):
    faces = set()
    for complement in disconnected:
        facet = FULL ^ complement
        s = facet
        while s:
            faces.add(s)
            s = (s-1) & facet
    return faces


def generate_by_face_definition(disconnected):
    # Opposite direction: test each of the 2^13-1 possible nonempty faces.
    # Test the existence of a disconnected 4-subset in its complement.
    faces = set()
    for s in range(1, FULL + 1):
        if s.bit_count() > 9:
            continue
        remaining = FULL ^ s
        if any((d & remaining) == d for d in disconnected):
            faces.add(s)
    return faces


def matching(faces):
    unmatched = set(faces)
    pairs = []
    for vertex in PIVOTS:
        bit = 1 << vertex
        current_pairs = [(s, s | bit) for s in unmatched
                         if not (s & bit) and (s | bit) in unmatched]
        for low, high in current_pairs:
            assert low in unmatched and high in unmatched
            assert high.bit_count() == low.bit_count() + 1
            unmatched.remove(low)
            unmatched.remove(high)
        pairs.extend(current_pairs)
    return pairs, unmatched


def verify_complete_hasse_acyclic(faces, pairs):
    pair_by_low = {low: high for low, high in pairs}
    assert len(pair_by_low) == len(pairs)
    endpoints = [v for pair in pairs for v in pair]
    assert len(set(endpoints)) == len(endpoints)
    degrees = {face: 0 for face in faces}
    directed = {face: [] for face in faces}
    edge_count = 0
    for high in faces:
        b = high
        while b:
            bit = b & -b
            b ^= bit
            low = high ^ bit
            if low == 0:
                continue  # ordinary, nonaugmented face poset
            assert low in faces
            if pair_by_low.get(low) == high:
                start, end = low, high
            else:
                start, end = high, low
            directed[start].append(end)
            degrees[end] += 1
            edge_count += 1
    queue = deque(v for v, deg in degrees.items() if deg == 0)
    visited = 0
    while queue:
        face = queue.popleft()
        visited += 1
        for other in directed[face]:
            degrees[other] -= 1
            if degrees[other] == 0:
                queue.append(other)
    assert visited == len(faces), 'directed Hasse cycle'
    return edge_count


def orientation_sign(face, perm):
    source_vertices = [i for i in range(N) if face & (1 << i)]
    target_vertices = [perm[i] for i in source_vertices]
    if sorted(target_vertices) != source_vertices:
        return 0
    inversions = sum(target_vertices[i] > target_vertices[j]
                     for i in range(len(target_vertices))
                     for j in range(i + 1, len(target_vertices)))
    return (-1) ** inversions


def reduced_lefschetz(faces, perm):
    return -1 + sum(((-1) ** (face.bit_count()-1)) * orientation_sign(face, perm)
                    for face in faces)


def main():
    assert sorted(RESIDUES) == [1, 3, 4, 9, 10, 12]
    assert len(set(PIVOTS)) == N
    assert all(adj.bit_count() == 6 for adj in ADJ)
    disconnected = disconnected4()
    assert len(disconnected) == 260
    connected = comb(N, 4) - len(disconnected)
    assert connected == 455
    assert all(components(d) > 1 for d in disconnected)
    faces = generate_by_facets(disconnected)
    assert faces == generate_by_face_definition(disconnected)
    vector = [sum(f.bit_count() == i + 1 for f in faces) for i in range(9)]
    assert vector == [13, 78, 286, 715, 1287, 1716, 1664, 975, 260]
    assert len(faces) == 6994
    assert sum((-1) ** i * v for i, v in enumerate(vector)) - 1 == 25
    pairs, critical = matching(faces)
    critical_profile = dict(sorted(Counter(f.bit_count() - 1 for f in critical).items()))
    assert critical_profile == {0: 1, 6: 25}
    assert len(pairs) == 3484
    assert len(critical) + 2 * len(pairs) == len(faces)
    edge_count = verify_complete_hasse_acyclic(faces, pairs)
    assert edge_count == 42393
    assert not any(all(not ADJ[i] & (1 << j) for i, j in combinations(S, 2))
                   for S in combinations(range(N), 4))
    # A=F_13 semidirect F_13^{*2}; every affine transformation is a graph automorphism.
    characters = {}
    for a in sorted(RESIDUES):
        for b in range(N):
            perm = [(a * i + b) % N for i in range(N)]
            assert len(set(perm)) == N
            assert all(bool(ADJ[i] & (1 << j)) == bool(ADJ[perm[i]] & (1 << perm[j]))
                       for i in range(N) for j in range(N))
            trace = reduced_lefschetz(faces, perm)
            fixed_vertices = sum(perm[i] == i for i in range(N))
            assert trace == 2 * fixed_vertices - 1, (a, b, trace)
            characters[(a, b)] = trace
    assert len(characters) == 78
    assert characters[(1, 0)] == 25
    assert {characters[(1, b)] for b in range(1, N)} == {-1}
    assert {characters[(a, b)] for a in RESIDUES if a != 1 for b in range(N)} == {1}
    assert sum(characters.values()) == 78
    # Character is 1+2 times the 12-dimensional augmentation of the 13-point action.
    # Invariants of the 25-dimensional rational H_6 thus have dimension 1.
    print('PALEY13_FOUR_CUT_MORSE_AFFINE_VERIFIED')
    print('graph_vertices=13 graph_edges=39 disconnected_4_sets=260 connected_4_sets=455')
    print('nonempty_faces=6994 f_vector=' + ','.join(map(str,vector)))
    print('morse_pairs=3484 critical_cells=' + str(critical_profile))
    print('hasse_incidences=42393 acyclicity=PASS')
    print('integral_homotopy=wedge_25_S6 simplicial_dimension=8 nonshellable=YES')
    print('affine_automorphisms=78 character_identity=25 character_translations=-1 character_other=1')
    print('representation=trivial_plus_two_augmented_13point rational_invariants_dim=1')
    print('alternate_enumeration=PASS independent_set_size_4=0')


if __name__ == '__main__':
    main()
