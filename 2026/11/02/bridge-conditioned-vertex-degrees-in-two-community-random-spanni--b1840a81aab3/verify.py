"""Independent exact checks for the two-block Gibbs spanning-tree theorem.

Run with Python 3.9 or later; standard library only.
"""
from fractions import Fraction
from itertools import product
from collections import defaultdict
from heapq import heapify, heappush, heappop
from math import comb

checks = 0

def check(condition, description):
    global checks
    if not condition:
        raise AssertionError(description)
    checks += 1


def prufer_edges(code, N):
    degrees = [1] * N
    for c in code:
        degrees[c] += 1
    leaves = [i for i in range(N) if degrees[i] == 1]
    heapify(leaves)
    edges = []
    for c in code:
        v = heappop(leaves)
        edges.append((v, c))
        degrees[v] -= 1
        degrees[c] -= 1
        if degrees[c] == 1:
            heappush(leaves, c)
    edges.append((heappop(leaves), heappop(leaves)))
    return edges


def enumerate_joint(m, n, alpha, beta):
    N = m + n
    poly = defaultdict(int)
    for code in product(range(N), repeat=N - 2):
        edges = prufer_edges(code, N)
        bridge = sum((u < m) != (v < m) for u, v in edges)
        degree = sum(u == 0 or v == 0 for u, v in edges)
        poly[(bridge, degree)] += alpha ** (N - 1 - bridge) * beta ** bridge
    return dict(poly)


def multiply(P, Q):
    R = defaultdict(int)
    for (k, d), a in P.items():
        for (h, e), b in Q.items():
            R[(k + h, d + e)] += a * b
    return {key: val for key, val in R.items() if val}


def exponentiate(P, e):
    R = {(0, 0): 1}
    for _ in range(e):
        R = multiply(R, P)
    return R


def formula_joint(m, n, alpha, beta):
    # beta*z*w * [alpha*(m-1+w)+beta*n*z]**(m-1)
    #            * [alpha*n+beta*z*(m-1+w)]**(n-1)
    U = {(0, 0): alpha * (m - 1), (0, 1): alpha, (1, 0): beta * n}
    V = {(0, 0): alpha * n, (1, 0): beta * (m - 1), (1, 1): beta}
    return multiply({(1, 1): beta}, multiply(exponentiate(U, m - 1), exponentiate(V, n - 1)))


def det_bareiss(A):
    A = [list(row) for row in A]
    N = len(A)
    if N == 0:
        return 1
    sign, previous = 1, 1
    for k in range(N - 1):
        if A[k][k] == 0:
            next_nonzero = next((i for i in range(k + 1, N) if A[i][k]), None)
            if next_nonzero is None:
                return 0
            A[k], A[next_nonzero] = A[next_nonzero], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k + 1, N):
            for j in range(k + 1, N):
                numerator = A[i][j] * pivot - A[i][k] * A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
        for i in range(k + 1, N):
            A[i][k] = 0
        previous = pivot
    return sign * A[-1][-1]


def reduced_laplacian_det(m, n, alpha, beta, w, z):
    N = m + n
    L = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(i + 1, N):
            b = (i < m) != (j < m)
            c = (beta * z if b else alpha) * (w if i == 0 else 1)
            L[i][i] += c
            L[j][j] += c
            L[i][j] -= c
            L[j][i] -= c
    return det_bareiss([row[1:] for row in L[1:]])


def coefficient_sum(P):
    return sum(P.values())


def covariance(P):
    Z = coefficient_sum(P)
    EX = Fraction(sum(k * v for (k, d), v in P.items()), Z)
    EY = Fraction(sum(d * v for (k, d), v in P.items()), Z)
    EXY = Fraction(sum(k * d * v for (k, d), v in P.items()), Z)
    return EXY - EX * EY


def covariance_formula(m, n, a, b):
    return a * b * n * (Fraction(n - 1, (a * n + b * m) ** 2)
                         - Fraction(m - 1, (a * m + b * n) ** 2))


def cross_pgf(m, n, a, b):
    # Shifted sum of two independent binomial count laws (unnormalized coefficients).
    P = defaultdict(int)
    for i in range(m):
        for j in range(n):
            P[1 + i + j] += (comb(m - 1, i) * (b * n) ** i * (a * m) ** (m - 1 - i)
                              * comb(n - 1, j) * (b * m) ** j * (a * n) ** (n - 1 - j))
    return dict(P)


for m, n in [(2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 2), (3, 4), (4, 3)]:
    for alpha, beta in [(1, 1), (2, 1), (1, 3)]:
        P = enumerate_joint(m, n, alpha, beta)
        F = formula_joint(m, n, alpha, beta)
        check(P == F, f'Prufer vs bivariate factorization: {(m,n,alpha,beta)}')
        normalizer = beta * (alpha * m + beta * n) ** (m - 1) * (alpha * n + beta * m) ** (n - 1)
        check(coefficient_sum(P) == normalizer, 'normalizer')
        check(covariance(P) == covariance_formula(m, n, alpha, beta), 'mixed moment')
        cross_marginal = defaultdict(int)
        for (k, d), value in P.items():
            cross_marginal[k] += value
        check(dict(cross_marginal) == {k: beta * v for k, v in cross_pgf(m, n, alpha, beta).items()},
              'bridge marginal Poisson-binomial')
        for w, z in [(1, 1), (2, 3), (3, 2)]:
            value = sum(v * (z ** k) * (w ** d) for (k, d), v in F.items())
            check(reduced_laplacian_det(m, n, alpha, beta, w, z) == value,
                  'independent weighted Laplacian determinant')
        if m == n:
            mean = Fraction(2 * m - 1, m)
            by_k = defaultdict(lambda: [0, 0])
            for (k, d), value in P.items():
                by_k[k][0] += d * value
                by_k[k][1] += value
            for k, (first, zeroth) in by_k.items():
                check(Fraction(first, zeroth) == mean, 'balanced conditional mean')

# Exact unbalanced sign reversal at a small crossing conductance.
for m, n, a, b, expected_sign in [(2, 3, 100, 1, -1), (2, 3, 1, 1, 1),
                                  (3, 2, 100, 1, 1), (3, 2, 1, 1, -1),
                                  (3, 4, 20, 1, -1), (3, 4, 1, 1, 1),
                                  (4, 3, 20, 1, 1), (4, 3, 1, 1, -1)]:
    c = covariance_formula(m, n, a, b)
    check((c > 0) - (c < 0) == expected_sign, 'finite sign transition')

# The conditional mean given exactly k cross-community edges is weight-independent.
# Its first increment has the opposite sign from the total endpoint difference
# exactly when the two community sizes differ.
for m, n in [(2, 2), (2, 3), (3, 2), (3, 3), (2, 4), (4, 2), (3, 4), (4, 3), (3, 5), (5, 3)]:
    P = formula_joint(m, n, 1, 1)
    by_k = defaultdict(lambda: [0, 0])
    for (k, d), val in P.items():
        by_k[k][0] += d * val
        by_k[k][1] += val
    means = {k: Fraction(total, denom) for k, (total, denom) in by_k.items()}
    N = m + n
    check(set(means) == set(range(1, N)), 'every cross-edge count feasible')
    check(means[1] == Fraction(2*m-1, m), 'one bridge conditional mean')
    check(means[N-1] == 1+Fraction(n-1, m), 'all bridges conditional mean')
    S = Fraction((m-1)*n, m) + Fraction((n-1)*m, n)
    increment = Fraction((m-n)*(m*n-m-n), m*m*n) / S
    check(means[2]-means[1] == increment, 'two bridges first increment')
    if m != n:
        check((means[2]-means[1])*(means[N-1]-means[1]) < 0,
              'strict opposite direction on short and full range')
    else:
        check(len(set(means.values())) == 1, 'balanced conditional flatness')

print('PASS', checks, 'exact assertions; direct Prufer enumeration, separate determinant, marginals and covariance')
