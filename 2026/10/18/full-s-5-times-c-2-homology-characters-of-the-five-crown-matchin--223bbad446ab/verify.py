#!/usr/bin/env python3
"""Exact finite checks for the five-crown matching-complex character.

Uses only Python 3 and NumPy. All computations are finite integer or prime-field
computations; the proof explains separately the characteristic-zero inputs.
"""
import itertools
import math
import json
from pathlib import Path
from collections import Counter
import numpy as np

N = 5
V = tuple((i, j) for i in range(N) for j in range(N) if i != j)
vid = {v: a for a, v in enumerate(V)}
F = []
for k in range(N + 1):
    faces = []
    for rows in itertools.combinations(range(N), k):
        for cols in itertools.permutations(range(N), k):
            if all(i != j for i, j in zip(rows, cols)):
                faces.append(tuple(sorted(vid[i, j] for i, j in zip(rows, cols))))
    F.append(tuple(sorted(faces)))
assert tuple(map(len, F)) == (1, 20, 130, 320, 265, 44)
ix = [{face: a for a, face in enumerate(faces)} for faces in F]

def boundary(k):
    A = np.zeros((len(F[k - 1]), len(F[k])), dtype=np.int64)
    for c, f in enumerate(F[k]):
        for j in range(k):
            A[ix[k - 1][f[:j] + f[j + 1:]], c] = -1 if j % 2 else 1
    return A

B = {k: boundary(k) for k in range(2, N + 1)}
for k in range(3, N + 1):
    assert not np.any(B[k - 1] @ B[k])

def rank_mod(M, p):
    A = np.remainder(M.copy(), p).astype(np.int64)
    rank = 0
    for col in range(A.shape[1]):
        nz = np.flatnonzero(A[rank:, col])
        if not len(nz):
            continue
        i = rank + int(nz[0])
        if i != rank:
            A[[rank, i]] = A[[i, rank]]
        A[rank, col:] = A[rank, col:] * pow(int(A[rank, col]), -1, p) % p
        nonzero = np.flatnonzero(A[rank + 1:, col]) + rank + 1
        if len(nonzero):
            A[nonzero, col:] = (A[nonzero, col:] - A[nonzero, col, None] * A[rank, col:]) % p
        rank += 1
        if rank == A.shape[0]:
            break
    return rank

for p in (3, 101):
    assert tuple(rank_mod(B[k], p) for k in range(2, 6)) == (19, 111, 208, 44)

# A geometric crosscheck: three disjoint attacking pairs form an octahedral 2-cycle.
pairs = (((0, 1), (0, 2)), ((1, 3), (1, 4)), ((2, 0), (3, 0)))
z = np.zeros(len(F[3]), dtype=np.int64)

def parity_of_word(seq):
    return -1 if sum(x > y for i, x in enumerate(seq) for y in seq[i + 1:]) % 2 else 1

for choices in itertools.product((0, 1), repeat=3):
    word = [vid[pairs[a][choices[a]]] for a in range(3)]
    s = (-1) ** sum(choices) * parity_of_word(word)
    z[ix[3][tuple(sorted(word))]] += s
assert np.count_nonzero(z) == 8
assert not np.any(B[3] @ z)
assert rank_mod(np.column_stack((B[4], z)), 101) == 209

# An explicit integral 2-cocycle makes the nonzero rational H2 class
# independently checkable: an integral boundary pairs to zero with it.
entries = json.loads(Path(__file__).with_name('cocycle.json').read_text(encoding='utf-8'))
phi = np.zeros(len(F[3]), dtype=np.int64)
for j, coeff in entries:
    assert 0 <= j < len(phi) and coeff in (-1, 1) and phi[j] == 0
    phi[j] = coeff
assert len(entries) == 120
assert not np.any(B[4].T @ phi)
assert int(phi @ z) == 2

def cycle_type(p):
    visited = set()
    result = []
    for v in range(N):
        if v in visited:
            continue
        t, k = v, 0
        while t not in visited:
            visited.add(t)
            t = p[t]
            k += 1
        result.append(k)
    return tuple(sorted(result, reverse=True))

def trace_chains(p, transpose):
    vertex_action = [vid[p[j], p[i]] if transpose else vid[p[i], p[j]] for i, j in V]
    ans = []
    for faces in F[1:]:
        t = 0
        for f in faces:
            image = tuple(vertex_action[v] for v in f)
            if tuple(sorted(image)) == f:
                t += parity_of_word(image)
        ans.append(t)
    return tuple(ans)

classes = {}
for p in itertools.permutations(range(N)):
    classes.setdefault(cycle_type(p), p)
assert len(classes) == 7

# Verify that signed trace depends only on the class, for all 240 automorphisms.
expected_trace = {}
for c, p in classes.items():
    for t in (0, 1):
        tr = trace_chains(p, t)
        expected_trace[(c, t)] = sum((-1) ** j * val for j, val in enumerate(tr)) - 1

for p in itertools.permutations(range(N)):
    c = cycle_type(p)
    for t in (0, 1):
        tr = trace_chains(p, t)
        reduced_lefschetz = sum((-1) ** j * val for j, val in enumerate(tr)) - 1
        assert reduced_lefschetz == expected_trace[(c, t)]

# Rational irreducible characters for S5, ordered by partitions:
# (5), (4,1), (3,2), (3,1,1), (2,2,1), (2,1,1,1), (1^5).
parts = ((5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1))

def s5_irr(c):
    fixed = c.count(1)
    pairs_fixed = math.comb(fixed, 2) + c.count(2)
    std = fixed - 1
    g2std = fixed + 2 * c.count(2) - 1
    wedge2std = (std * std - g2std) // 2
    sgn = (-1) ** (N - len(c))
    return (1, std, pairs_fixed - fixed, wedge2std,
            sgn * (pairs_fixed - fixed), sgn * std, sgn)

weights = {c: math.factorial(N) // math.prod(k ** m * math.factorial(m)
            for k, m in Counter(c).items()) for c in classes}
assert sum(weights.values()) == 120
assert [s5_irr((1, 1, 1, 1, 1))[i] for i in range(7)] == [1, 4, 5, 6, 5, 4, 1]
for i in range(7):
    for j in range(7):
        v = sum(weights[c] * s5_irr(c)[i] * s5_irr(c)[j] for c in classes)
        assert v == (120 if i == j else 0)

# From the established rational Betti numbers (1,0,1,13,0), H2 is a line.
# Test its four possible 1-dimensional characters using virtual-character
# identity L = chi(H2) - chi(H3) and nonnegative integral multiplicities.
candidates = {}
for sign_s5 in (0, 1):
    for sign_transpose in (0, 1):
        h2 = lambda c, t: (-1) ** (sign_s5 * (N - len(c)) + sign_transpose * t)
        multiplicities = {}
        for i in range(7):
            for eps in (0, 1):
                numerator = sum(weights[c] * (h2(c, t) - expected_trace[(c, t)])
                                * s5_irr(c)[i] * (-1) ** (eps * t)
                                for c in classes for t in (0, 1))
                assert numerator % 240 == 0
                multiplicities[(i, eps)] = numerator // 240
        candidates[(sign_s5, sign_transpose)] = multiplicities

valid = [(key, multiplicities) for key, multiplicities in candidates.items()
         if all(v >= 0 for v in multiplicities.values())]
assert len(valid) == 1 and valid[0][0] == (0, 1)
assert {parts[i]: mult for (i, eps), mult in valid[0][1].items() if mult and eps == 0} == {
    (4, 1): 1, (3, 2): 1}
assert {parts[i]: mult for (i, eps), mult in valid[0][1].items() if mult and eps == 1} == {
    (2, 1, 1, 1): 1}
assert sum(s5_irr((1, 1, 1, 1, 1))[i] * mult for (i, _), mult in valid[0][1].items()) == 13

for c in classes:
    for t in (0, 1):
        h2 = (-1) ** t
        h3 = s5_irr(c)[1] + s5_irr(c)[2] + (-1) ** t * s5_irr(c)[5]
        assert h2 - h3 == expected_trace[(c, t)]

print('VERIFY_OK CROWN_5 F_VECTOR_20_130_320_265_44 RANKS_19_111_208_44')
print('GROUP_ORDER_240 H2_TRIVIAL_TIMES_TRANSPOSE_SIGN H3_4_PLUS_5_PLUS_4')
