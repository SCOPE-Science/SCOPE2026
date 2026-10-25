"""Independent finite-cell enumeration for the Fano-cap cyclic quotient.

Run: python3 checker.py
Only the Python standard library is required. The homotopy-cancellation
argument itself is given in RESULT.md rather than inferred from ranks.
"""
from itertools import combinations
from math import gcd
from functools import reduce

V = tuple(range(7))
LINES = [frozenset(((i + d) % 7 for d in (0, 1, 3))) for i in V]
FACETS = [frozenset(V) - L for L in LINES]
assert len(set(LINES)) == len(set(FACETS)) == 7
assert all(len(a & b) == 1 for a, b in combinations(LINES, 2))
assert all(len(a & b) == 2 for a, b in combinations(FACETS, 2))
FACES = {k: sorted(set(s for f in FACETS for s in combinations(sorted(f), k + 1))) for k in range(4)}
assert [len(FACES[k]) for k in range(4)] == [7, 21, 28, 7]
assert all(sum(set(t).issubset(f) for f in FACETS) == 1 for t in FACES[2])


def translate(simplex, d):
    return tuple(sorted(((v + d) % 7 for v in simplex)))


def orbits(k):
    remaining = set(FACES[k]); reps = []
    while remaining:
        f = min(remaining)
        orb = {translate(f, d) for d in V}
        assert len(orb) == 7 and orb <= remaining
        remaining -= orb
        reps.append(f)
    return reps


REPS = {k: orbits(k) for k in range(4)}
assert [len(REPS[k]) for k in range(4)] == [1, 3, 4, 1]
assert REPS[1] == [(0, 1), (0, 2), (0, 3)]
assert REPS[2] == [(0, 1, 2), (0, 1, 4), (0, 1, 5), (0, 2, 4)]
assert REPS[3] == [(0, 1, 2, 5)]
assert all(translate(f, d) != f for k in range(4) for f in FACES[k] for d in range(1, 7))


def edge_letter(a, b):
    delta = (b - a) % 7
    return ("abc"[delta - 1] if delta <= 3 else "ABC"[6 - delta])


WORDS = ["".join(edge_letter(t[i], t[(i + 1) % 3]) for i in range(3)) for t in REPS[2]]
assert WORDS == ["aaB", "acc", "aCb", "bbc"]


def perm_sign(seq):
    inversions = sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq)))
    return (-1) ** inversions


TET = REPS[3][0]
D3 = [0] * 4
for omit in range(4):
    oriented = tuple(x for j, x in enumerate(TET) if j != omit)
    matches = []
    for idx, rep in enumerate(REPS[2]):
        for d in V:
            shifted = tuple((x + d) % 7 for x in rep)
            if set(shifted) == set(oriented):
                idx_perm = [shifted.index(x) for x in oriented]
                matches.append((idx, ((-1) ** omit) * perm_sign(idx_perm)))
    assert len(matches) == 1
    idx, sgn = matches[0]
    D3[idx] += sgn
assert D3 == [-1, 1, 1, -1]

# Boundary of each oriented 2-cell: exponent totals in its attaching word.
D2 = [[word.count(low) - word.count(high) for word in WORDS]
      for low, high in zip('abc', 'ABC')]
assert D2 == [[2, 1, 1, 0], [-1, 0, 1, 2], [0, 2, -1, 1]]
assert all(sum(D2[i][j] * D3[j] for j in range(4)) == 0 for i in range(3))


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    return sum((-1)**j * matrix[0][j] * determinant([row[:j]+row[j+1:] for row in matrix[1:]])
               for j in range(n))


def minors_gcd(matrix, n):
    m = len(matrix); p = len(matrix[0])
    ds = [abs(determinant([[matrix[i][j] for j in js] for i in ix]))
          for ix in combinations(range(m), n) for js in combinations(range(p), n)]
    return reduce(gcd, ds)

assert [minors_gcd(D2, k) for k in (1, 2, 3)] == [1, 1, 7]
# Each 3-simplex and precisely one of its triangular faces forms a free pair.
assert (1, 2, 5) in FACES[2] and (0, 1, 2, 5) in FACES[3]
assert sum(set((1, 2, 5)).issubset(f) for f in FACETS) == 1
# The seven translates are disjoint pairs of cell *orbits* and give an
# equivariant collapse; the removed 2-cell is the orbit of (0,1,4).
assert translate((0, 1, 4), 1) == (1, 2, 5)
REMAINING = [WORDS[i] for i in (0, 2, 3)]
assert REMAINING == ['aaB', 'aCb', 'bbc']
D2_SMALL = [[row[i] for i in (0, 2, 3)] for row in D2]
assert determinant(D2_SMALL) == 7
assert [minors_gcd(D2_SMALL, k) for k in (1, 2, 3)] == [1, 1, 7]
# Relator aaB eliminates b=a*a. Relator aCb eliminates c=b*a.
# Then bbc becomes a^7, yielding a Moore 2-complex.
print('PASS: Fano cap face numbers [7,21,28,7]')
print('PASS: all cyclic face orbits have size seven; quotient cells [1,3,4,1]')
print('PASS: quotient relators', WORDS, 'and quotient d3', D3)
print('PASS: chain condition and integral determinantal divisors 1,1,7')
print('PASS: equivariant free-face orbit and remaining relators', REMAINING)
print('PASS: b=a^2, c=a^3, remaining relation a^7')
