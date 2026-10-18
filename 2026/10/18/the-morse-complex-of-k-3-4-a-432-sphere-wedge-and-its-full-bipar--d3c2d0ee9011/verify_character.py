#!/usr/bin/env python3
"""Independent rooted-forest, incidence-rank and automorphism-character checks.

The input graph is K_{3,4}. All arithmetic is integral, with one
additional exact linear-rank computation over F_2. No packages required.
"""
from collections import Counter
from itertools import permutations, product
from math import factorial

A = range(3)
B = range(3, 7)
ARCS = [directed for i in A for j in B for directed in ((i, j), (j, i))]
ARC_TO_ID = {arc: i for i, arc in enumerate(ARCS)}
NEIGHBORS = [[v for v in range(7) if (u in A) != (v in A)] for u in range(7)]
CLASSES3 = [(1, 1, 1), (2, 1), (3,)]
CLASSES4 = [(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]
EXPECTED = [[432, -16, 4, 0, -2], [0, 0, 4, 0, -2], [-3, -1, 1, -3, 1]]
S3_CHAR = {(3,): [1, 1, 1], (2, 1): [2, 0, -1], (1, 1, 1): [1, -1, 1]}
S4_CHAR = {(4,): [1, 1, 1, 1, 1], (3, 1): [3, 1, -1, 0, -1],
           (2, 2): [2, 0, 2, -1, 0], (2, 1, 1): [3, -1, -1, 0, 1],
           (1, 1, 1, 1): [1, -1, 1, 1, -1]}
EXPECTED_MULT = [
    [2, 8, 7, 9, 4],
    [5, 17, 12, 19, 8],
    [2, 8, 6, 10, 3],
]


def independent_enumeration():
    valid = set()
    for targets in product(*([(-1, *NEIGHBORS[v]) for v in range(7)])):
        directed = [(v, targets[v]) for v in range(7) if targets[v] != -1]
        if len({tuple(sorted(edge)) for edge in directed}) != len(directed):
            continue
        cyclic = False
        for start in range(7):
            seen = set()
            v = start
            while v != -1:
                if v in seen:
                    cyclic = True
                    break
                seen.add(v)
                v = targets[v]
            if cyclic:
                break
        if cyclic:
            continue
        mask = sum(1 << ARC_TO_ID[edge] for edge in directed)
        valid.add(mask)
    return valid


def forest_polynomial():
    # Nonzero Laplacian eigenvalues of K_{3,4}: 7,4,4,3,3,3.
    # det(t I + L)/t enumerates rooted spanning forests by components.
    coefficients = [1]
    for eigen in (7, 4, 4, 3, 3, 3):
        next_coeff = [0] * (len(coefficients) + 1)
        for j, value in enumerate(coefficients):
            next_coeff[j] += eigen * value
            next_coeff[j + 1] += value
        coefficients = next_coeff
    assert coefficients == [3024, 4968, 3357, 1192, 234, 24, 1]
    return [coefficients[6 - k] for k in range(7)]


def rank_top_mod_two(faces):
    rows = {face: i for i, face in enumerate(sorted(f for f in faces if f.bit_count() == 5))}
    basis = {}
    rank = 0
    for high in sorted(f for f in faces if f.bit_count() == 6):
        vector = 0
        bits = high
        while bits:
            bit = bits & -bits
            bits -= bit
            vector ^= 1 << rows[high ^ bit]
        while vector:
            lead = vector.bit_length() - 1
            if lead not in basis:
                basis[lead] = vector
                rank += 1
                break
            vector ^= basis[lead]
    assert rank == 2592
    return rank


def cycle_type(permutation):
    seen, sizes = set(), []
    for i in range(len(permutation)):
        if i in seen:
            continue
        j, count = i, 0
        while j not in seen:
            seen.add(j)
            count += 1
            j = permutation[j]
        sizes.append(count)
    return tuple(sorted(sizes, reverse=True))


def class_character(faces):
    table = {}
    for left, right in product(permutations(range(3)), permutations(range(4))):
        vertex_image = list(left) + [3 + j for j in right]
        perm = [ARC_TO_ID[(vertex_image[u], vertex_image[v])] for u, v in ARCS]
        reduced_lefschetz = -1
        for f in faces:
            if f == 0:
                continue
            images = [perm[i] for i in range(24) if f & (1 << i)]
            if sum(1 << i for i in images) != f:
                continue
            inversions = sum(images[i] > images[j] for i in range(len(images))
                             for j in range(i + 1, len(images)))
            sign = -1 if inversions % 2 else 1
            # Ordinary chain sign (-1)^dimension, with dimension |f|-1.
            reduced_lefschetz += sign * (-1 if len(images) % 2 == 0 else 1)
        key = cycle_type(left), cycle_type(right)
        top_trace = -reduced_lefschetz  # unique reduced homology degree 5
        if key in table:
            assert table[key] == top_trace
        table[key] = top_trace
    actual = [[table[(x, y)] for y in CLASSES4] for x in CLASSES3]
    assert actual == EXPECTED, actual
    return actual


def z(mu):
    out = 1
    for i, multiplicity in Counter(mu).items():
        out *= i**multiplicity * factorial(multiplicity)
    return out


def multiplicities(table):
    terms3 = [(3,), (2, 1), (1, 1, 1)]
    terms4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    out = []
    for left_irrep in terms3:
        row = []
        for right_irrep in terms4:
            numerator = sum(table[i][j] * S3_CHAR[left_irrep][i] * S4_CHAR[right_irrep][j]
                            * (6 // z(x)) * (24 // z(y))
                            for i, x in enumerate(CLASSES3)
                            for j, y in enumerate(CLASSES4))
            assert numerator % 144 == 0
            row.append(numerator // 144)
        out.append(row)
    assert out == EXPECTED_MULT
    degrees3 = [S3_CHAR[ir][0] for ir in terms3]
    degrees4 = [S4_CHAR[ir][0] for ir in terms4]
    assert sum(out[i][j] * degrees3[i] * degrees4[j]
               for i in range(3) for j in range(5)) == 432
    return out


def main():
    faces = independent_enumeration()
    assert len(faces) == 12800
    counts = [sum(face.bit_count() == k for face in faces) for k in range(7)]
    assert counts == forest_polynomial()
    assert rank_top_mod_two(faces) == 2592
    characters = class_character(faces)
    irreducibles = multiplicities(characters)
    print("VERIFY_OK rooted_forests=12800 face_sizes=" + repr(counts))
    print("TOP_MOD2_BOUNDARY rank=2592 kernel=432")
    print("CHARACTER_ROWS " + repr(characters))
    print("SPECHT_MULTIPLICITY_ROWS " + repr(irreducibles))


if __name__ == "__main__":
    main()
