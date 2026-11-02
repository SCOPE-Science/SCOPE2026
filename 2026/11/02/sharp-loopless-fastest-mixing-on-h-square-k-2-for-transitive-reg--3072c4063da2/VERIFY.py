#!/usr/bin/env python3
"""Reproduce exact spectral and optimal-weight checks for matched-clique and other two-layer graphs.

Only Python's standard library is required. This is supplementary finite verification;
the all-dimension theorem is proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from itertools import combinations, product

CHECKS = 0

def verify(condition, description):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description)

def build_graph(kind, size=None):
    if kind == 'complete':
        vertices = list(range(size))
        adjacent = lambda a, b: a != b
        lap = [(0, 1), (size, size - 1)]
    elif kind == 'johnson':
        vertices = list(combinations(range(size), 2))
        adjacent = lambda a, b: len(set(a) & set(b)) == 1
        lap = [(0, 1), (size, size - 1), (2 * (size - 1), size * (size - 3) // 2)]
    elif kind == 'petersen':
        vertices = list(combinations(range(5), 2))
        adjacent = lambda a, b: len(set(a) & set(b)) == 0
        lap = [(0, 1), (2, 5), (5, 4)]
    elif kind == 'cube3':
        vertices = list(product(range(2), repeat=3))
        adjacent = lambda a, b: sum(x != y for x, y in zip(a, b)) == 1
        lap = [(0, 1), (2, 3), (4, 3), (6, 1)]
    elif kind == 'cycle4':
        vertices = list(range(4))
        adjacent = lambda a, b: (a - b) % 4 in (1, 3)
        lap = [(0, 1), (2, 2), (4, 1)]
    elif kind == 'cycle6':
        vertices = list(range(6))
        adjacent = lambda a, b: (a - b) % 6 in (1, 5)
        lap = [(0, 1), (1, 2), (3, 2), (4, 1)]
    else:
        raise ValueError(kind)
    n = len(vertices)
    A = [[int(i != j and adjacent(vertices[i], vertices[j])) for j in range(n)] for i in range(n)]
    degrees = [sum(row) for row in A]
    verify(len(set(degrees)) == 1 and degrees[0] > 0, 'regularity')
    verify(sum(mult for _, mult in lap) == n, 'Laplacian multiplicities')
    verify(all(A[i][j] == A[j][i] for i in range(n) for j in range(n)), 'undirected')
    return A, degrees[0], lap

def product_integer_matrix(A, multiplier, rung):
    n = len(A)
    T = [[0 for _ in range(2 * n)] for __ in range(2 * n)]
    for i in range(n):
        for j in range(n):
            if A[i][j]:
                T[i][j] = multiplier
                T[n + i][n + j] = multiplier
        T[i][n + i] = rung
        T[n + i][i] = rung
    return T

def mult(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def exact_charpoly_certificate(T, eigenvalues):
    """Newton power-sum criterion: traces 1,...,N determine the full characteristic polynomial."""
    n = len(T)
    verify(len(eigenvalues) == n, 'expected spectrum size')
    P = [r[:] for r in T]
    for k in range(1, n + 1):
        measured = sum(P[i][i] for i in range(n))
        predicted = sum(lam ** k for lam in eigenvalues)
        verify(measured == predicted, 'spectrum power sum k=%s N=%s' % (k, n))
        if k < n:
            P = mult(P, T)

def run_case(kind, size=None, trace=True):
    A, d, lap = build_graph(kind, size)
    alpha = lap[1][0]
    beta = lap[-1][0]
    margin = min(alpha, 2 * d - beta)
    verify(0 <= margin <= 2 * d, 'spectral margin')
    denom = 2 * d + margin
    rung = margin
    T = product_integer_matrix(A, 2, rung)
    N = len(T)
    verify(all(sum(row) == denom for row in T), 'exact Markov row sums')
    verify(all(T[i][i] == 0 for i in range(N)), 'no holding')
    verify(all(T[i][j] == T[j][i] for i in range(N) for j in range(N)), 'symmetric transition')
    verify(all(T[i][j] >= 0 for i in range(N) for j in range(N)), 'nonnegative')
    eigs = []
    for base_lam, mult_base in lap:
        eigs.extend([denom - 2 * base_lam] * mult_base)
        eigs.extend([denom - 2 * base_lam - 2 * margin] * mult_base)
    verify(max(abs(z) for z in eigs if z != denom) <= denom, 'spectral modulus bound')
    # The nontrivial constant eigenvalue (when margin=0, there may be multiple 1-eigenvalues).
    vals = [denom - 2 * lam for lam, count in lap for _ in range(count)]
    vals += [denom - 2 * lam - 2 * margin for lam, count in lap for _ in range(count)]
    vals.remove(denom)  # remove exactly the all-ones eigenvalue
    verify(max(abs(z) for z in vals) == 2 * d - margin, 'sharp contraction')
    if trace:
        exact_charpoly_certificate(T, eigs)
    # Check a full rational mesh, independently using the unreduced spectral list.
    for q in [5, 11, 23]:
        for k in range(q + 1):
            x = F(k, q * d)
            y = 1 - d * x
            eigen = [1 - x * lam for lam, mult_base in lap for _ in range(mult_base)]
            eigen += [1 - x * lam - 2 * y for lam, mult_base in lap for _ in range(mult_base)]
            eigen.remove(1)
            slem = max(abs(z) for z in eigen)
            verify(slem >= F(2 * d - margin, 2 * d + margin), 'mesh lower bound')
    # Exact holding-allowed benchmark, including the sharp positivity-penalty boundary.
    full_denom = max(beta + 2 * alpha, 2 * d + alpha)
    holding_slem = F(full_denom - 2 * alpha, full_denom)
    loopless_slem = F(2 * d - margin, 2 * d + margin)
    verify(loopless_slem >= holding_slem, 'holding relaxation monotonicity')
    verify((loopless_slem == holding_slem) == (alpha + beta <= 2 * d), 'no-holding free iff spectral condition')
    if alpha + beta > 2 * d:
        exact_penalty = F(2 * beta * (alpha + beta - 2 * d), (4 * d - beta) * (beta + 2 * alpha))
        verify(loopless_slem - holding_slem == exact_penalty, 'sharp positive spectral penalty')
    print('%s(%s): n=%s degree=%s alpha=%s beta=%s margin=%s, mu0=%s, muH=%s' %
          (kind, size, len(A), d, alpha, beta, margin, loopless_slem, holding_slem))

for n in range(2, 10):
    run_case('complete', n, trace=n <= 8)
for n in range(4, 9):
    run_case('johnson', n, trace=n <= 7)
for kind in ('petersen', 'cube3', 'cycle4', 'cycle6'):
    run_case(kind)
print('PASS: %s exact assertions, including full characteristic-polynomial certificates' % CHECKS)
