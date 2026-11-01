#!/usr/bin/env python3
"""Finite exact verification for Desargues independence-complex homology characters.

No third-party modules are required. Executing this file independently constructs
all faces, the reduced boundary ranks over F_2, and all 240 Lefschetz traces.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

PAIR = list(combinations(range(5), 2))
PAIR_INDEX = {a: j for j, a in enumerate(PAIR)}
EDGE = [0] * 20
for i, a in enumerate(PAIR):
    for j, b in enumerate(PAIR):
        if not set(a).intersection(b):
            EDGE[i] |= 1 << (j + 10)
            EDGE[j + 10] |= 1 << i

faces = [[] for _ in range(10)]
def enumerate_independent(face, allowed, size):
    if size:
        faces[size - 1].append(face)
    while allowed:
        vbit = allowed & -allowed
        v = vbit.bit_length() - 1
        allowed ^= vbit
        enumerate_independent(face | vbit, allowed & ~EDGE[v], size + 1)
enumerate_independent(0, (1 << 20) - 1, 0)

f_vector = tuple(map(len, faces))
assert f_vector == (20, 160, 660, 1510, 1924, 1320, 480, 115, 20, 2)
assert sum(f_vector) == 6211

ranks = [1]  # augmented differential C_0 --> C_{-1}
for degree in range(1, len(faces)):
    row_index = {f: j for j, f in enumerate(faces[degree-1])}
    basis = {}
    for simplex in faces[degree]:
        column = 0
        bits = simplex
        while bits:
            atom = bits & -bits
            bits -= atom
            column ^= (1 << row_index[simplex ^ atom])
        while column:
            lead = column.bit_length() - 1
            if lead in basis:
                column ^= basis[lead]
            else:
                basis[lead] = column
                break
    ranks.append(len(basis))
assert tuple(ranks) == (1, 19, 141, 519, 991, 932, 383, 97, 18, 2)
mod2_betti = [len(faces[k]) - ranks[k] - (ranks[k+1] if k+1 < len(ranks) else 0) for k in range(10)]
assert mod2_betti == [0, 0, 0, 0, 1, 5, 0, 0, 0, 0]

def sign(values):
    parity = 0
    for j, v in enumerate(values):
        parity ^= (sum(v > w for w in values[j+1:]) & 1)
    return 1 - 2*parity

def cycle_type(p):
    seen = set()
    out = []
    for i in range(5):
        if i not in seen:
            j, length = i, 0
            while j not in seen:
                seen.add(j)
                j = p[j]
                length += 1
            out.append(length)
    return tuple(sorted(out, reverse=True))

def action_map(p, flip):
    out = [0] * 20
    for i, a in enumerate(PAIR):
        j = PAIR_INDEX[tuple(sorted(p[t] for t in a))]
        out[i] = j + 10 * flip
        out[10+i] = j + 10 * (1 - flip)
    return out

def lefschetz_reduced(mapping):
    # Signed permutation of oriented simplices in each cellular degree.
    total = -1  # augmentation correction (empty face).
    for degree, fs in enumerate(faces):
        tr = 0
        for face in fs:
            original = [i for i in range(20) if (face >> i) & 1]
            target = [mapping[i] for i in original]
            image_mask = sum(1 << i for i in target)
            if image_mask == face:
                tr += sign(target)
        total += (-1)**degree * tr
    return total

seen = set()
class_table = {}
for p in permutations(range(5)):
    for flip in (0, 1):
        mapping = action_map(p, flip)
        assert tuple(mapping) not in seen
        seen.add(tuple(mapping))
        for i in range(20):
            assert {mapping[j] for j in range(20) if EDGE[i] & (1 << j)} == {
                j for j in range(20) if EDGE[mapping[i]] & (1 << j)}
        observed = lefschetz_reduced(mapping)
        predicted = (-1)**flip * (sign(p) - sum(p[i] == i for i in range(5)))
        assert observed == predicted, (p, flip, observed, predicted)
        key = (cycle_type(p), flip)
        if key in class_table:
            assert class_table[key] == observed
        class_table[key] = observed
assert len(seen) == 240 and len(class_table) == 14

# The semisimple rational representation ring has a positive coefficient
# for the one-dimensional sign-on-both-factors representation in Ltilde.
# Since the F_2 bounds give dim_Q H~_4 <= 1 and dim_Q H~_5 <= 5,
# this forces H~_4 = sgn(S5)*sgn(C2) and H~_5 = Q^5*sgn(C2).
assert sum((-1)**k * mod2_betti[k] for k in range(10)) == -4
assert class_table[((1,)*5, 0)] == -4
assert class_table[((1,)*5, 1)] == 4
print('face vector:', ','.join(map(str, f_vector)))
print('augmented mod-2 boundary ranks:', ','.join(map(str, ranks)))
print('reduced mod-2 Betti:', ','.join(map(str, mod2_betti)))
print('conjugacy Lefschetz values (cycle type / no flip / flip):')
for typ in sorted({k[0] for k in class_table}, reverse=True):
    print(''.join(map(str,typ)), class_table[(typ,0)], class_table[(typ,1)])
print('automorphism actions checked:', len(seen))
print('complete rational representation: H4=sgn(S5)*sgn(C2), H5=permutation5*sgn(C2)')
print('VERIFY_OK')
