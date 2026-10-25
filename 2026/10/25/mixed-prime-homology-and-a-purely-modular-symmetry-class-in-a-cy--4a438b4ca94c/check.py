"""Self-contained exact integral chain calculation for the five-by-five cyclic chessboard quotient.

Requires Python 3, numpy and sympy (only for exact integer Smith form).
Run: python3 check.py
"""
from itertools import combinations, permutations
from collections import Counter
import hashlib
import json
import numpy as np
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

P = 5


def normalize(face):
    """Orient by increasing row and shift the first column to zero."""
    face = tuple(sorted(face))
    assert face and len({a for a, _ in face}) == len(face)
    assert len({b for _, b in face}) == len(face)
    shift = face[0][1]
    return tuple((a, (b - shift) % P) for a, b in face)


def all_faces(k):
    """Generate EVERY nonempty matching of k rooks, with no quotient."""
    for rows in combinations(range(P), k):
        for cols in permutations(range(P), k):
            yield tuple(zip(rows, cols))


def rank_mod_p(mat, p):
    """Independent finite-field Gaussian elimination, not based on Smith form."""
    a = (np.array(mat, dtype=np.int64) % p).copy()
    m, n = a.shape
    rank = 0
    for col in range(n):
        ix = next((i for i in range(rank, m) if a[i, col] != 0), None)
        if ix is None:
            continue
        if ix != rank:
            a[[rank, ix]] = a[[ix, rank]]
        a[rank, col:] = (a[rank, col:] * pow(int(a[rank, col]), -1, p)) % p
        for i in range(rank + 1, m):
            z = int(a[i, col])
            if z:
                a[i, col:] = (a[i, col:] - z * a[rank, col:]) % p
        rank += 1
        if rank == m:
            break
    return rank


raw_f = []
cells = []
for k in range(1, 6):
    raw = list(all_faces(k))
    raw_f.append(len(raw))
    # Every face orbit under column shifts has length exactly five.
    for face in raw:
        orbit = {tuple((r, (c + a) % P) for r, c in face) for a in range(P)}
        assert len(orbit) == P
        assert len({normalize(elem) for elem in orbit}) == 1
    canonical = sorted({normalize(face) for face in raw})
    cells.append(canonical)
    assert len(raw) == P * len(canonical)

assert raw_f == [25, 200, 600, 600, 120], raw_f
assert [len(z) for z in cells] == [5, 40, 120, 120, 24]

boundaries = []
for degree in range(1, 5):
    index = {c: i for i, c in enumerate(cells[degree - 1])}
    d = np.zeros((len(cells[degree - 1]), len(cells[degree])), dtype=np.int64)
    for j, face in enumerate(cells[degree]):
        for omit in range(degree + 1):
            facet = normalize(face[:omit] + face[omit + 1:])
            d[index[facet], j] += (-1) ** omit
    assert np.max(np.abs(d)) <= 2
    boundaries.append(d)

for a, b in zip(boundaries, boundaries[1:]):
    assert np.count_nonzero(a @ b) == 0, 'boundary squared must be zero'

invariants = []
for mat in boundaries:
    diagonal = smith_normal_form(Matrix(mat.tolist()), domain=ZZ)
    inv = [abs(int(diagonal[i, i])) for i in range(min(diagonal.shape))
           if diagonal[i, i] != 0]
    assert all(inv[i + 1] % inv[i] == 0 for i in range(len(inv) - 1))
    invariants.append(inv)

expected = [Counter({1: 4}), Counter({1: 35, 5: 1}),
            Counter({1: 83, 3: 1}), Counter({1: 24})]
assert [Counter(v) for v in invariants] == expected, invariants
ranks = [len(v) for v in invariants]
assert ranks == [4, 36, 84, 24]

for prime, expected_ranks in [(2, [4,36,84,24]), (3, [4,36,83,24]),
                              (5, [4,35,84,24]), (7, [4,36,84,24]),
                              (11, [4,36,84,24])]:
    actual = [rank_mod_p(mat, prime) for mat in boundaries]
    assert actual == expected_ranks, (prime, actual)

# Topological Euler characteristic agrees with rational homology.
chi = sum((-1)**i * len(cells[i]) for i in range(5))
assert chi == -11
free_ranks = [len(cells[i]) - (ranks[i - 1] if i else 0)
              - (ranks[i] if i < 4 else 0) for i in range(5)]
assert free_ranks == [1, 0, 0, 12, 0], free_ranks

print('PASS: all 1,545 original nonempty faces, free five-element face orbits')
print('PASS: quotient-cell counts', [len(z) for z in cells])
print('PASS: every boundary composition is zero')
for j, s in enumerate(invariants, start=1):
    print('Smith(d_%d) =' % j, dict(sorted(Counter(s).items())))
print('PASS: independent modular rank checks at 2,3,5,7,11')
print('PASS: integral homology H_0=Z, H_1=Z/5, H_2=Z/3, H_3=Z^12, H_4=0')

# An integral Bockstein cup product on the quotient.
def u(edge):
    return normalize(edge)[1][1]


def beta(triangle):
    face = normalize(triangle)
    numerator = (u(face[1:]) - u((face[0], face[2])) + u(face[:2]))
    assert numerator % P == 0
    return numerator // P

betas = np.array([beta(triangle) for triangle in cells[2]], dtype=np.int64)
assert np.count_nonzero(boundaries[2].T @ betas) == 0
w = np.array([u(face[:2]) * beta(face[1:]) for face in cells[3]],
             dtype=np.int64)
assert np.count_nonzero((boundaries[3].T @ w) % P) == 0

def parity(values):
    return (-1) ** sum(values[i] > values[j] for i in range(len(values))
                       for j in range(i + 1, len(values)))

z = np.zeros(len(cells[3]), dtype=np.int64)
for i, face in enumerate(cells[3]):
    if tuple(r for r, _ in face) == (0, 1, 2, 3):
        cols = tuple(c for _, c in face)
        unused = next(c for c in range(P) if c not in cols)
        z[i] = parity(cols + (unused,))
assert np.count_nonzero(z) == 24
assert np.count_nonzero(boundaries[2] @ z) == 0
assert int(w @ z) % P == 2
print('PASS: explicit 24-cell integral three-cycle pairs to 2 mod 5 with u cup Bockstein(u)')

# Character of the row-permutation action on H_3 over characteristic zero.
def cycle_type(permutation):
    seen, sizes = set(), []
    for r in range(P):
        if r in seen:
            continue
        x, size = r, 0
        while x not in seen:
            seen.add(x)
            size += 1
            x = permutation[x]
        sizes.append(size)
    return tuple(sorted(sizes, reverse=True))

classes = {}
for perm in permutations(range(P)):
    trace_chain = []
    for faces in cells:
        trace = 0
        for face in faces:
            changed = [(perm[r], c) for r, c in face]
            rows_changed = [r for r, _ in changed]
            if normalize(changed) == face:
                trace += parity(rows_changed)
        trace_chain.append(trace)
    character = 1 - sum((-1) ** d * val for d, val in enumerate(trace_chain))
    typ = cycle_type(perm)
    classes.setdefault(typ, []).append(character)
expected_chars = {
    (1,1,1,1,1): (1,12),
    (2,1,1,1): (10,-2),
    (2,2,1): (15,0),
    (3,1,1): (20,3),
    (3,2): (20,1),
    (4,1): (30,0),
    (5,): (24,-3),
}
for key, (size, char) in expected_chars.items():
    assert len(classes[key]) == size
    assert set(classes[key]) == {char}
assert sum(sum(values) for values in classes.values()) == 0
print('PASS: complete seven-class S5 character on rational H_3 and zero invariant multiplicity')
print('PASS: nonzero canonical S5-invariant mod-five cohomology class in degree three')
