#!/usr/bin/env python3
"""Exact finite chain verification for the 12-vertex Möbius ladder.

No third-party libraries; all linear algebra is exact over F_2.
The finite enumeration is exhaustive and accompanies a mathematical proof.
"""
from itertools import combinations
from collections import defaultdict

N = 12
EDGES = {frozenset((j, (j + 1) % N)) for j in range(N)}
EDGES |= {frozenset((j, j + 6)) for j in range(6)}
assert len(EDGES) == 18


def independent(vs):
    return all(frozenset(pair) not in EDGES for pair in combinations(vs, 2))


FACES = defaultdict(list)
for mask in range(1, 1 << N):
    vs = tuple(j for j in range(N) if mask >> j & 1)
    if independent(vs):
        FACES[len(vs) - 1].append(vs)
assert [len(FACES[j]) for j in range(5)] == [12, 48, 76, 48, 12]
assert not FACES[5]


def xor_basis_add(x, pivots):
    while x:
        p = x.bit_length() - 1
        if p in pivots:
            x ^= pivots[p]
        else:
            pivots[p] = x
            return True
    return False


def boundary_columns(k):
    idx = {f: i for i, f in enumerate(FACES[k - 1])}
    return [sum(1 << idx[s] for s in combinations(f, k)) for f in FACES[k]]


def rank(columns):
    b = {}
    for c in columns:
        xor_basis_add(c, b)
    return len(b)


BRANKS = [rank(boundary_columns(j)) for j in range(1, 5)]
assert BRANKS == [11, 37, 36, 12], BRANKS
assert 76 - BRANKS[1] - BRANKS[2] == 3
assert 48 - BRANKS[0] - BRANKS[1] == 0
assert 48 - BRANKS[2] - BRANKS[3] == 0
assert 12 - BRANKS[3] == 0

# The three explicit induced octahedra, i.e. Ind(3K_2) = (S^0)^{*3}.
SUPPORTS = [
    (0, 1, 4, 5, 8, 9),
    (0, 2, 4, 6, 8, 10),
    (0, 3, 4, 7, 8, 11),
]
TRI = {t: i for i, t in enumerate(FACES[2])}
OCTAHEDRA = []
for vertices in SUPPORTS:
    internal = [e for e in EDGES if e <= set(vertices)]
    assert len(internal) == 3
    assert len(set().union(*internal)) == 6
    z = sum(1 << TRI[t] for t in combinations(vertices, 3) if t in TRI)
    assert z.bit_count() == 8
    OCTAHEDRA.append(z)

# Independently check that each fundamental sphere chain is a cycle.
D2 = boundary_columns(2)
for z in OCTAHEDRA:
    b = 0
    for j, col in enumerate(D2):
        if z >> j & 1:
            b ^= col
    assert b == 0

# Quotient C_2 / im(boundary_3) in characteristic 2; every class is
# calculated with an echelon basis carrying its three homology coordinates.
B = {}

def add_with_label(z, label, add_if_new):
    while z:
        j = z.bit_length() - 1
        if j in B:
            old, coord = B[j]
            z ^= old
            label ^= coord
        else:
            if add_if_new:
                B[j] = (z, label)
            return z, label
    return 0, label

for bdry in boundary_columns(3):
    add_with_label(bdry, 0, True)
assert len(B) == 36
for j, z in enumerate(OCTAHEDRA):
    residual, _ = add_with_label(z, 1 << j, True)
    assert residual != 0
assert len(B) == 39


def coords(z):
    residual, label = add_with_label(z, 0, False)
    assert residual == 0
    return label


def rotate(z):
    answer = 0
    for triangle, j in TRI.items():
        if z >> j & 1:
            rotated = tuple(sorted((u + 1) % N for u in triangle))
            answer ^= 1 << TRI[rotated]
    return answer


A = [coords(rotate(z)) for z in OCTAHEDRA]
assert A == [3, 5, 1], A  # 3 columns of the rotation matrix

def matmul_columns(U, V):
    out = []
    for col in V:
        x = 0
        for j in range(len(U)):
            if col >> j & 1:
                x ^= U[j]
        out.append(x)
    return out


I = [1, 2, 4]
assert matmul_columns(A, matmul_columns(A, matmul_columns(A, A))) == I
B0 = [A[j] ^ I[j] for j in range(3)]
B1 = matmul_columns(B0, B0)
B2 = matmul_columns(B1, B0)
assert [rank(m) for m in [B0, B1, B2]] == [2, 1, 0]

# Signed Lefschetz numbers over characteristic zero by exact fixed-face
# enumeration, independent of the characteristic-two boundary calculation.
def parity_inversions(seq):
    return sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i+1,len(seq))) % 2


def reduced_lefschetz_rotation(shift):
    z = -1  # augmented empty simplex in degree -1
    for d, all_faces in FACES.items():
        for f in all_faces:
            rotated = [((u + shift) % N) for u in f]
            if tuple(sorted(rotated)) == f:
                orient = -1 if parity_inversions(rotated) else 1
                z += (-1 if d & 1 else 1) * orient
    return z


TRACES = [reduced_lefschetz_rotation(j) for j in range(12)]
assert TRACES == [3 if j % 4 == 0 else -1 for j in range(12)], TRACES

print('VERIFY_OK')
print('f-vector [12,48,76,48,12]')
print('ranks (d1,d2,d3,d4) =', BRANKS)
print('mod2 H2 rank = 3')
print('octahedral support triples =', SUPPORTS)
print('rotation mod2 columns =', A)
print('ranks ((A-I)^1,(A-I)^2,(A-I)^3) = [2,1,0]')
print('characteristic-zero signed reduced Lefschetz traces =', TRACES)
