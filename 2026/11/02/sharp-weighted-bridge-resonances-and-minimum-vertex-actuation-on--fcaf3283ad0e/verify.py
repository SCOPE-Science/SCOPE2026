"""Exact finite checks for the weighted two-hub tree controllability theorem.

Only Python's standard library is required. Tests are independent of any
precomputed eigenvalue or eigenvector tables. Run: python verify.py
"""
from fractions import Fraction as F
from itertools import combinations

assertions = 0


def check(condition, label):
    global assertions
    assertions += 1
    if not condition:
        raise AssertionError(label)


def laplacian(p, q, L, t):
    n = p + q + L + 1
    M = [[F(0) for _ in range(n)] for _ in range(n)]
    def edge(i, j, w):
        M[i][i] += w
        M[j][j] += w
        M[i][j] -= w
        M[j][i] -= w
    for i in range(L):
        edge(i, i + 1, t)
    for i in range(p):
        edge(0, L + 1 + i, F(1))
    for i in range(q):
        edge(L, L + 1 + p + i, F(1))
    return M


def rank_krylov(A, sensors):
    n = len(A)
    # Rational incremental column elimination. The Krylov span of input
    # columns up to power n-1 is the controllability subspace.
    pivots = {}
    def add(vec):
        for i in sorted(pivots):
            c = vec[i]
            if c:
                row = pivots[i]
                vec = [v - c * w for v, w in zip(vec, row)]
        for i, v in enumerate(vec):
            if v:
                pivots[i] = [w / v for w in vec]
                return
    for sensor in sensors:
        vector = [F(int(i == sensor)) for i in range(n)]
        for _ in range(n):
            add(vector)
            if len(pivots) == n:
                return n
            vector = [sum(a * b for a, b in zip(row, vector)) for row in A]
    return len(pivots)


def dirichlet_resonance(L, t):
    # The Dirichlet path block has L-1 internal vertices, diagonal 2t-1
    # and off-diagonal -t, evaluated at Laplacian eigenvalue one.
    if L == 1:
        return False
    prevprev, prev = F(1), 2 * t - 1
    for _ in range(2, L):
        prevprev, prev = prev, (2 * t - 1) * prev - t * t * prevprev
    return prev == 0


def expected_minimal(p, q, L, t):
    return p + q - 2 + int(dirichlet_resonance(L, t))


weights = [F(1, 3), F(1, 2), F(2, 3), F(1), F(4, 3), F(3, 2), F(2)]
for p in (2, 3):
    for q in (2, 3):
        for L in range(1, 8):
            left = list(range(L + 1, L + 1 + p))
            right = list(range(L + 1 + p, L + 1 + p + q))
            base = left[:-1] + right[:-1]
            for t in weights:
                A = laplacian(p, q, L, t)
                N = len(A)
                resonant = dirichlet_resonance(L, t)
                core_rank = rank_krylov(A, base)
                check(core_rank == N - int(resonant),
                      ('base rank', p, q, L, t, core_rank))
                if resonant:
                    check(rank_krylov(A, base + [left[-1]]) == N,
                          ('left leaf', p, q, L, t))
                    check(rank_krylov(A, base + [right[-1]]) == N,
                          ('right leaf', p, q, L, t))
                    check(rank_krylov(A, base + [0]) == N - 1,
                          ('left hub', p, q, L, t))
                    check(rank_krylov(A, base + [L]) == N - 1,
                          ('right hub', p, q, L, t))
                    # For rational t the corresponding sine mode has
                    # a rationally detectable zero pattern using
                    # its tridiagonal recurrence.
                    w0, w1 = F(0), F(1)
                    mode = {1: w1}
                    for i in range(2, L):
                        w0, w1 = w1, (2 - 1 / t) * w1 - w0
                        mode[i] = w1
                    for i in range(1, L):
                        predicted = N if mode[i] else N - 1
                        result = rank_krylov(A, base + [i])
                        check(result == predicted,
                              ('internal sensor', p, q, L, t, i, result, predicted))

# Exhaustively check all minimal-sized vertex sets in selected small
# graphs; no claim that this finite census proves the infinite theorem.
for p, q, L, t in [
    (2, 2, 1, F(1)),
    (2, 2, 2, F(1)),
    (2, 2, 2, F(1, 2)),
    (2, 2, 3, F(1)),
    (2, 2, 3, F(1, 3)),
    (2, 2, 4, F(1, 2)),
    (3, 2, 3, F(1)),
    (2, 3, 3, F(2)),
]:
    A = laplacian(p, q, L, t)
    N = len(A)
    m = expected_minimal(p, q, L, t)
    left = set(range(L + 1, L + 1 + p))
    right = set(range(L + 1 + p, N))
    resonance = dirichlet_resonance(L, t)
    for S in combinations(range(N), m):
        s = set(S)
        predicted = len(s & left) >= p - 1 and len(s & right) >= q - 1
        if resonance and predicted:
            if len(s & left) == p-1 and len(s & right) == q-1:
                interior = list(s & set(range(1, L)))
                if len(interior) != 1:
                    predicted = False
                else:
                    u = interior[0]
                    a, b = F(0), F(1)
                    for _ in range(2, u + 1):
                        a, b = b, (2 - 1 / t) * b - a
                    predicted = b != 0
        observed = rank_krylov(A, S) == N
        check(observed == predicted, ('all min sets', p, q, L, t, S))

# Exact arithmetic characterization at rational weights.
for L in range(1, 19):
    for t in weights:
        should = (t in (F(1), F(1, 3)) and L % 3 == 0) or (
            t == F(1, 2) and L % 2 == 0)
        check(dirichlet_resonance(L, t) == should, ('rational corollary', L, t))

print('PASS:', assertions, 'exact assertions')
