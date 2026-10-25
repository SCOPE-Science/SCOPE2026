#!/usr/bin/env python3
"""Exact finite verifier for folded-five-cube independence homology characters.

Uses only the Python standard library. No saved data or network access required.
"""
from collections import Counter, deque
from itertools import combinations, permutations

VERTICES = tuple(range(16))
GENERATORS = frozenset((1, 2, 4, 8, 15))
TOGGLE_ORDER = (14, 4, 9, 7, 3, 12, 6, 8, 13, 2, 0, 5, 10, 1, 11, 15)
FOURIER_MASKS = (14, 13, 11, 7, 15)  # sums over the four coordinates other than i

def parity(x):
    return x.bit_count() % 2

def sign_of_reordering(indices):
    return -1 if sum(indices[i] > indices[j]
                     for i in range(len(indices)) for j in range(i + 1, len(indices))) % 2 else 1

def graph_adj(x, y):
    return x != y and ((x ^ y) in GENERATORS)

def independent(face):
    return all(not graph_adj(x, y) for x, y in combinations(face, 2))

def quotient_coordinate_permutation(p, x):
    # In F_2^5/<11111>, normalize the fifth coordinate of x to zero.
    old = [(x >> i) & 1 for i in range(4)] + [0]
    new = [0] * 5
    for i in range(5):
        new[p[i]] = old[i]
    return sum((new[i] ^ new[4]) << i for i in range(4))

def lefschetz_top_character(image, faces):
    # Euler--Poincare trace: reduced Lefschetz number equals -trace(H_3).
    total = 1  # -(-1) for the empty simplex
    for dimension, simplex_list in enumerate(faces):
        for simplex in simplex_list:
            shifted = [image[x] for x in simplex]
            if tuple(sorted(shifted)) != simplex:
                continue
            orientation = sign_of_reordering([simplex.index(x) for x in shifted])
            total -= ((-1) ** dimension) * orientation
    return total

def verify_morse(faces):
    all_faces = sorted((f for layer in faces for f in layer), key=lambda f: (len(f), f))
    assert len(all_faces) == 392
    index = {f: i for i, f in enumerate(all_faces)}
    unmatched = set(range(len(all_faces)))
    matched = set()
    for v in TOGGLE_ORDER:
        for i in sorted(unmatched):
            f = all_faces[i]
            if v in f:
                continue
            bigger = tuple(sorted(f + (v,)))
            j = index.get(bigger)
            if j is not None and j in unmatched:
                unmatched.remove(i)
                unmatched.remove(j)
                matched.add((i, j))
    assert len(matched) == 191
    assert Counter(len(all_faces[i]) - 1 for i in unmatched) == {0: 1, 3: 9}
    assert len(unmatched) == 10
    edges = [[] for _ in all_faces]
    indegree = [0] * len(all_faces)
    hasse = 0
    for higher, face in enumerate(all_faces):
        if len(face) < 2:
            continue
        for j in range(len(face)):
            lower = index[face[:j] + face[j + 1:]]
            u, v = ((lower, higher) if (lower, higher) in matched
                    else (higher, lower))
            edges[u].append(v)
            indegree[v] += 1
            hasse += 1
    assert hasse == 1200
    ready = deque(i for i, degree in enumerate(indegree) if degree == 0)
    visited = 0
    while ready:
        u = ready.popleft()
        visited += 1
        for v in edges[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                ready.append(v)
    assert visited == len(all_faces)  # exhaustive acyclic-matching certificate
    print('MORSE_191_PAIRS_ONE_VERTEX_NINE_3CELLS_ACYCLIC', visited, hasse)

def main():
    faces = [tuple(f for f in combinations(VERTICES, d + 1) if independent(f))
             for d in range(5)]
    assert [len(layer) for layer in faces] == [16, 80, 160, 120, 16]
    assert all(not independent(f) for f in combinations(VERTICES, 6))
    assert sum(((-1) ** d) * len(layer) for d, layer in enumerate(faces)) == -8
    assert all(sum(graph_adj(x, z) and graph_adj(y, z) for z in VERTICES)
                   == (0 if graph_adj(x, y) else 2)
                   for x, y in combinations(VERTICES, 2))
    verify_morse(faces)

    seen = set()
    count = 0
    for p in permutations(range(5)):
        fixed_count = sum(i == p[i] for i in range(5))
        sgn = sign_of_reordering(p)
        linear = [quotient_coordinate_permutation(p, x) for x in VERTICES]
        assert sorted(linear) == list(VERTICES)
        assert frozenset(linear[v] for v in GENERATORS) == GENERATORS
        for t in VERTICES:
            image = tuple(linear[x] ^ t for x in VERTICES)
            assert image not in seen
            seen.add(image)
            # The sign twist of (standard_5 + five weight-four Fourier lines).
            predicted = sgn * (fixed_count - 1 + sum(
                1 - 2 * parity(FOURIER_MASKS[i] & t)
                for i in range(5) if p[i] == i))
            computed = lefschetz_top_character(image, faces)
            assert computed == predicted, (p, t, computed, predicted)
            count += 1
    assert count == len(seen) == 1920
    print('ALL_1920_FULL_AUTOMORPHISM_CHARACTERS_VERIFIED', count)

    # Independent Walsh--Fourier check of the translation restriction.
    zero = tuple(range(5))
    translations = [lefschetz_top_character(tuple(x ^ t for x in VERTICES), faces)
                    for t in VERTICES]
    assert translations[0] == 9
    multiplicities = [sum(translations[t] * (1 - 2 * parity(a & t))
                          for t in VERTICES) // 16 for a in VERTICES]
    assert all(sum(translations[t] * (1 - 2 * parity(a & t))
                   for t in VERTICES) % 16 == 0 for a in VERTICES)
    assert multiplicities[0] == 4
    assert {i for i, x in enumerate(multiplicities) if x == 1} == set(FOURIER_MASKS)
    assert sum(multiplicities) == 9
    print('TRANSLATION_MODULE_FOUR_TRIVIAL_PLUS_FIVE_DISTINCT_LINES_VERIFIED')
    print('CLEBSCH_FULL_RATIONAL_HOMOLOGY_MODULE_VERIFIED')

if __name__ == '__main__':
    main()
