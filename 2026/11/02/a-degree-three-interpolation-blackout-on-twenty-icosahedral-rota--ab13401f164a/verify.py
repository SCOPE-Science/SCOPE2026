"""Exact certificate for Wigner sampling at the 20 threefold rotations.
Run with Python 3; uses only the standard library.
"""
from itertools import permutations
from collections import Counter

N = 5
IDENTITY = tuple(range(N))

def compose(p, q):
    return tuple(p[q[i]] for i in range(N))

def inverse(p):
    return tuple(p.index(i) for i in range(N))

def parity_even(p):
    return sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N)) % 2 == 0

def cycle_type(p):
    seen, lengths = set(), []
    for i in range(N):
        if i not in seen:
            k, m = i, 0
            while k not in seen:
                seen.add(k)
                k = p[k]
                m += 1
            lengths.append(m)
    return tuple(sorted(lengths, reverse=True))

A5 = [p for p in permutations(range(N)) if parity_even(p)]
X = [p for p in A5 if cycle_type(p) == (3, 1, 1)]
FIVE = next(p for p in A5 if cycle_type(p) == (5,))
FIVE_SQUARED = compose(FIVE, FIVE)
FIVE_A = {compose(compose(h, FIVE), inverse(h)) for h in A5}
FIVE_B = {compose(compose(h, FIVE_SQUARED), inverse(h)) for h in A5}
assert (len(A5), len(X), len(FIVE_A), len(FIVE_B)) == (60, 20, 12, 12)
assert not FIVE_A.intersection(FIVE_B)

# Conjugacy labels: identity, half-turn, threefold, fivefold-A, fivefold-B.
def label(p):
    if p == IDENTITY:
        return 0
    typ = cycle_type(p)
    if typ == (2, 2, 1):
        return 1
    if typ == (3, 1, 1):
        return 2
    assert typ == (5,)
    return 3 if p in FIVE_A else 4

TYPES = [[label(compose(x, inverse(y))) for y in X] for x in X]
assert all(TYPES[i][j] == TYPES[j][i] for i in range(20) for j in range(20))
assert all(Counter(row) == {0: 1, 1: 6, 2: 7, 3: 3, 4: 3} for row in TYPES)

# Exact real quadratic ring Z[phi] with phi^2=phi+1.
# Each ordered pair (a,b) represents a+b*phi.
FIVE_CHARACTER = (
    ((1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)),
    ((1, 0), (1, -1), (0, 0), (-1, 1), (-1, 0)),
)

def character(l, typ):
    if typ == 0:
        return (2 * l + 1, 0)
    if typ == 1:
        return ((-1) ** l, 0)
    if typ == 2:
        return ((1, 0, -1)[l % 3], 0)
    return FIVE_CHARACTER[typ - 3][l % 5]

def zeros():
    return [[0] * 20 for _ in range(20)]

def identity():
    mat = zeros()
    for i in range(20):
        mat[i][i] = 1
    return mat

def pair_matrix(l):
    a, b = zeros(), zeros()
    for i in range(20):
        for j in range(20):
            a[i][j], b[i][j] = character(l, TYPES[i][j])
    return a, b

def multiply(P, Q):
    A, B = P
    C, D = Q
    E, F = zeros(), zeros()
    for i in range(20):
        for k in range(20):
            a, b = A[i][k], B[i][k]
            if not a and not b:
                continue
            for j in range(20):
                c, d = C[k][j], D[k][j]
                E[i][j] += a * c + b * d
                F[i][j] += a * d + b * c + b * d
    return E, F

def shift(P, value):
    A, B = P
    C = [row[:] for row in A]
    for i in range(20):
        C[i][i] -= value
    return C, B

# Distinct eigenvalues and exact multiplicities.
EXPECTED = {
    0: {0: 19, 20: 1},
    1: {0: 12, 6: 5, 10: 3},
    2: {2: 6, 4: 10, 12: 4},
    3: {0: 4, 5: 4, 7: 5, 10: 4, 15: 3},
    4: {5: 5, 7: 6, 9: 1, 12: 4, 14: 4},
    5: {4: 5, 12: 10, 16: 5},
    6: {7: 3, 11: 5, 12: 4, 14: 4, 17: 3, 29: 1},
    7: {9: 1, 12: 4, 14: 4, 17: 11},
    8: {9: 3, 13: 1, 15: 5, 18: 4, 19: 3, 24: 4},
    9: {12: 4, 14: 1, 18: 5, 22: 6, 24: 4},
}

for degree, spectrum in EXPECTED.items():
    G = pair_matrix(degree)
    assert sum(spectrum.values()) == 20
    assert all(v >= 0 for v in spectrum)
    # First show all possible eigenvalues are in the proposed list by
    # verifying an exact annihilating polynomial in Q(sqrt(5))[z].
    P = (identity(), zeros())
    for eigenvalue in spectrum:
        P = multiply(P, shift(G, eigenvalue))
    assert all(v == 0 for row in P[0] + P[1] for v in row)
    # Because G is real symmetric, use the first r power traces to
    # force the multiplicity of each of r distinct proposed roots.
    P = (identity(), zeros())
    for exponent in range(len(spectrum)):
        if exponent:
            P = multiply(P, G)
        tr_a = sum(P[0][i][i] for i in range(20))
        tr_b = sum(P[1][i][i] for i in range(20))
        assert (tr_a, tr_b) == (
            sum(count * root ** exponent for root, count in spectrum.items()), 0
        )
    rank = 20 - spectrum.get(0, 0)
    print('degree', degree, 'rank', rank, 'exact spectrum', spectrum)

# For every degree >= 10 the diagonal is >= 21. In each row
# the off-diagonal sum is bounded by 7+6+3*sqrt(5) < 21.
# The last inequality follows from 3*sqrt(5) < 8, i.e. 45<64.
assert 45 < 64
print('ALL_EXACT_CHECKS_PASSED')
