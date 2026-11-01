#!/usr/bin/env python3
"""Exact finite checks of affine characters on the Paley-17 open-neighborhood complex.

Requires only Python 3 standard library; all enumeration is exhaustive for this graph.
"""
from collections import Counter
from itertools import combinations

P = 17
Q = {pow(a, 2, P) for a in range(1, P)}
assert Q == {1, 2, 4, 8, 9, 13, 15, 16}
assert {pow(2, j, P) for j in range(8)} == Q

neighborhoods = [sorted({(v+r) % P for r in Q}) for v in range(P)]
faces = [set() for _ in range(8)]
for neighbors in neighborhoods:
    for size in range(1, 9):
        faces[size-1].update(combinations(neighbors, size))
faces = [sorted(z) for z in faces]
f = tuple(map(len, faces))
assert f == (17, 136, 612, 1122, 952, 476, 136, 17)
assert sum((-1)**k * number for k, number in enumerate(f)) == -34

# Independent sparse boundary elimination over F_2; column vectors are Python integers.
indices = [{face: k for k, face in enumerate(lst)} for lst in faces]
ranks = []
for degree in range(1, len(faces)):
    basis = {}
    for simplex in faces[degree]:
        column = 0
        for j in range(degree + 1):
            facet = simplex[:j] + simplex[j+1:]
            column ^= 1 << indices[degree-1][facet]
        while column:
            pivot = column.bit_length()-1
            if pivot in basis:
                column ^= basis[pivot]
            else:
                basis[pivot] = column
                break
    ranks.append(len(basis))
assert tuple(ranks) == (16, 120, 492, 595, 357, 119, 17)
mod2_reduced_betti = tuple(f[k] - (ranks[k-1] if k else 1)
                           - (ranks[k] if k < 7 else 0)
                           for k in range(8))
assert mod2_reduced_betti == (0, 0, 0, 35, 0, 0, 0, 0)


def permutation_sign(values):
    return -1 if sum(values[i] > values[j]
                     for i in range(len(values))
                     for j in range(i+1, len(values))) % 2 else 1


def signed_fixed_face_traces(a, b):
    traces = [0]*8
    for degree, simplices in enumerate(faces):
        total = 0
        for simplex in simplices:
            image = [(a * v + b) % P for v in simplex]
            if tuple(sorted(image)) == simplex:
                total += permutation_sign(image)
        traces[degree] = total
    return tuple(traces)

# All 136 affine automorphisms, not one representative per abstract class.
character_table = {}
for j in range(8):
    a = pow(2, j, P)
    for b in range(P):
        traces = signed_fixed_face_traces(a, b)
        lefschetz = sum((-1)**k * tr for k, tr in enumerate(traces))
        homology_trace = 1 - lefschetz
        # Augmentation module U of the 17-point affine permutation module.
        fixed_vertices = sum((a*v+b) % P == v for v in range(P))
        u_trace = fixed_vertices - 1
        # W=sign_{C8} direct-sum Q(i), 2 acts on Q(i) as multiplication by i.
        w_trace = (-1)**j + (2, 0, -2, 0)[j % 4]
        assert homology_trace == 2*u_trace + w_trace, (j, b)
        character_table[(j, b)] = homology_trace
assert len(character_table) == 136
assert Counter(character_table.values()) == Counter({-1:102, 1:16, 3:17, 35:1})
assert tuple(character_table[(j, 0)] for j in range(8)) == (35, -1, -1, -1, 3, -1, -1, -1)
assert set(character_table[(0, b)] for b in range(1, 17)) == {1}

print('paley17 open-neighborhood face vector:', f)
print('mod2 boundary ranks:', tuple(ranks))
print('reduced mod2 Betti numbers:', mod2_reduced_betti)
print('signed Lefschetz traces by multiplier 2^j (b=0):')
for j in range(8):
    print(j, pow(2, j, P), signed_fixed_face_traces(pow(2, j, P), 0))
print('H3 rational trace for multiplier exponents j=0..7:',
      tuple(character_table[(j, 0)] for j in range(8)))
print('H3 rational character value counts across affine group:',
      sorted(Counter(character_table.values()).items()))
print('Representation equality verified for all 136 affine elements.')
print('VERIFY_OK')
