#!/usr/bin/env python3
"""Exhaustive signed Lefschetz certificate for the Q4 independence complex.

Run: python3 verify.py    (Python 3.10+, standard library only).
Every group element and every invariant simplex is inspected.
"""
from collections import Counter
from itertools import permutations

N = 16
ADJ = [sum(1 << w for w in range(N) if (v ^ w).bit_count() == 1)
       for v in range(N)]
FACES = [[] for _ in range(8)]
for mask in range(1, 1 << N):
    if all(not (mask & (1 << v)) or not (mask & ADJ[v])
           for v in range(N)):
        FACES[mask.bit_count()-1].append(mask)
assert [len(v) for v in FACES] == [16, 88, 208, 228, 128, 56, 16, 2]
ALL = [x for layer in FACES for x in layer]


def rank_f2(columns):
    echelon = {}
    for col in columns:
        while col:
            lead = col.bit_length() - 1
            if lead not in echelon:
                echelon[lead] = col
                break
            col ^= echelon[lead]
    return len(echelon)


def binary_boundaries(k):
    rowpos = {mask: i for i, mask in enumerate(FACES[k-1])}
    for mask in FACES[k]:
        col = 0
        for v in range(N):
            if mask & (1 << v):
                col ^= 1 << rowpos[mask ^ (1 << v)]
        yield col

ranks = {k: rank_f2(binary_boundaries(k)) for k in range(1, 8)}
assert [ranks[k] for k in range(1, 8)] == [15, 73, 135, 86, 42, 14, 2]
betti = [len(FACES[k]) - ranks.get(k, 0) - ranks.get(k+1, 0)
         for k in range(8)]
assert betti == [1, 0, 0, 7, 0, 0, 0, 0]
reduced_euler = sum((-1)**k*len(FACES[k]) for k in range(8)) - 1
assert reduced_euler == -7
# Rank over Q is >= rank modulo 2; therefore Betti(Q)<=Betti(F2).
# These Betti bounds and the reduced Euler characteristic force
# H~_3(Q)=Q^7 and all other reduced rational homology to be zero.


def permutation_sign(entries):
    inversions = sum(entries[i] > entries[j]
                     for i in range(len(entries))
                     for j in range(i+1, len(entries)))
    return -1 if inversions % 2 else 1


def predicted_trace(pi, b):
    fixed_coordinates = [i for i in range(4) if pi[i] == i]
    return permutation_sign(pi) * (
        len(fixed_coordinates)-1
        + sum((-1)**((b & ~(1 << i)).bit_count()) for i in fixed_coordinates)
    )


def simplicial_trace(pi, b):
    image = [sum(((v >> i) & 1) << pi[i] for i in range(4)) ^ b
             for v in range(N)]
    # Ordinary Lefschetz trace on simplicial chains.
    chain_supertrace = 0
    for dimension, layer in enumerate(FACES):
        for mask in layer:
            source = [v for v in range(N) if mask & (1 << v)]
            target = [image[v] for v in source]
            if set(target) == set(source):
                chain_supertrace += (-1)**dimension*permutation_sign(target)
    # Augmentation contributes 1 to degree 0. The only nonzero
    # reduced rational homology is in odd degree 3.
    return 1 - chain_supertrace

traces = {}
for pi in permutations(range(4)):
    for b in range(16):
        actual = simplicial_trace(pi, b)
        expected = predicted_trace(pi, b)
        assert actual == expected, (pi, b, actual, expected)
        traces[(pi,b)] = actual
assert len(traces) == 384
identity = tuple(range(4))
translation = {b: traces[identity,b] for b in range(16)}
assert {w: {translation[b] for b in range(16) if b.bit_count() == w}
        for w in range(5)} == {0:{7},1:{1},2:{3},3:{5},4:{-1}}
# Exact Fourier inversion in the elementary abelian translation group.
multiplicity = {}
for a in range(16):
    signed_sum = sum(translation[b]*(-1)**((a&b).bit_count())
                     for b in range(16))
    assert signed_sum % 16 == 0
    multiplicity[a] = signed_sum // 16
assert multiplicity == {a: (3 if a == 0 else int(a.bit_count() == 3))
                        for a in range(16)}
assert sum(multiplicity.values()) == 7
# Averaging character gives zero invariants for the full group.
assert sum(traces.values()) == 0

print('INDEPENDENT_FACE_VECTOR', *map(len, FACES))
print('CHAIN_BOUNDARY_RANKS_F2', *(ranks[k] for k in range(1,8)))
print('MOD2_BETTI', *betti)
print('REDUCED_EULER', reduced_euler)
print('RATIONAL_REDUCED_H3_DIMENSION', 7)
print('AUTOMORPHISMS_TESTED', len(traces))
print('COMPLETE_SIGNED_TRACE_HISTOGRAM', sorted(Counter(traces.values()).items()))
print('TRANSLATION_TRACE_BY_HAMMING_WEIGHT', [translation[next(b for b in range(16) if b.bit_count()==w)] for w in range(5)])
print('TRANSLATION_CHARACTER_MULTIPLICITIES', sorted(multiplicity.items()))
print('FULL_SYMMETRY_INVARIANT_DIMENSION', sum(traces.values()) // 384)
print('VERIFY_OK_Q4_INDEPENDENCE_FULL_HYPEROCTAHEDRAL_CHARACTER')
