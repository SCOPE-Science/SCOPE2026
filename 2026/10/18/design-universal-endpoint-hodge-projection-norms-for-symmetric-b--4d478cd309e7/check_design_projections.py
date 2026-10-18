"""Exact independent small-design checks of incidence-graph projection formulas.

Run: python check_design_projections.py
Uses only the Python standard library, with rational Gaussian elimination.
"""
from fractions import Fraction as F
from itertools import product


def pg2(p):
    """Points and lines of the projective plane over a prime field."""
    representatives = {}
    for vec in product(range(p), repeat=3):
        if not any(vec):
            continue
        a = next(x for x in vec if x)
        representative = tuple((x * pow(a, -1, p)) % p for x in vec)
        representatives[representative] = 1
    vecs = sorted(representatives)
    return [tuple(i for i, x in enumerate(vecs)
                  if sum(a * b for a, b in zip(line, x)) % p == 0)
            for line in vecs]


def biplane11():
    residue = (1, 3, 4, 5, 9)
    return [tuple(sorted((i + x) % 11 for x in residue))
            for i in range(11)]


def crown(v):
    return [tuple(j for j in range(v) if j != i) for i in range(v)]


def inverse(M):
    n = len(M)
    A = [[F(M[i][j]) for j in range(n)]
         + [F(i == j) for j in range(n)] for i in range(n)]
    for i in range(n):
        pivot = next(r for r in range(i, n) if A[r][i])
        A[i], A[pivot] = A[pivot], A[i]
        z = A[i][i]
        A[i] = [x / z for x in A[i]]
        for r in range(n):
            if r == i:
                continue
            z = A[r][i]
            if z:
                A[r] = [a - z * b for a, b in zip(A[r], A[i])]
    return [row[n:] for row in A]


def audit(blocks):
    v = len(blocks)
    assert all(len(B) == len(blocks[0]) for B in blocks)
    k = len(blocks[0])
    lam = sum(0 in B and 1 in B for B in blocks)
    assert 1 <= lam < k < v
    assert all(sum(x in B for B in blocks) == k for x in range(v))
    assert all(sum(x in B and y in B for B in blocks) == lam
               for x in range(v) for y in range(x + 1, v))
    assert k * (k - 1) == lam * (v - 1)
    edges = sorted((x, j) for j, B in enumerate(blocks) for x in B)
    m = len(edges)
    L = [[0] * (2 * v) for _ in range(2 * v)]
    for x, j in edges:
        y = v + j
        L[x][x] += 1
        L[y][y] += 1
        L[x][y] -= 1
        L[y][x] -= 1
    # Ground the last vertex. Inverting this Laplacian is independent
    # of the proposed transfer-current formula.
    K = inverse([row[:-1] for row in L[:-1]])
    Q = [[F(0) for _ in edges] for _ in edges]
    for col, (p, B) in enumerate(edges):
        source = [F(0) for _ in range(2 * v - 1)]
        source[p] += 1
        if v + B < len(source):
            source[v + B] -= 1
        h = [sum(K[i][j] * source[j] for j in range(len(source)))
             for i in range(len(source))] + [F(0)]
        for row, (x, A) in enumerate(edges):
            Q[row][col] = h[x] - h[v + A]
            formula = F(1, k * v) + F(
                k * (x == p) - (x in blocks[B])
                - (p in blocks[A]) + k * (A == B), lam * v)
            assert Q[row][col] == formula
    assert all(Q[i][j] == Q[j][i] for i in range(m) for j in range(m))
    assert all(sum(Q[i][r] * Q[r][j] for r in range(m)) == Q[i][j]
               for i in range(m) for j in range(m))
    norm_Q = max(sum(abs(Q[row][col]) for row in range(m))
                 for col in range(m))
    norm_C = max(sum(abs(F(row == col) - Q[row][col])
                     for row in range(m)) for col in range(m))
    expected_Q = (F(1) + F(2 * (k - 1), lam * v)
                  * (2 * (k - lam) * (1 - F(lam, k))
                     + (lam - 1) * (2 - F(lam, k))))
    R = F(2 * v - 1, k * v)
    assert norm_Q == expected_Q
    assert norm_C == expected_Q + 1 - 2 * R
    assert all(Q[i][i] == R for i in range(m))
    if lam == 1:
        q = k - 1
        assert v == q * q + q + 1
        assert norm_Q == 1 + F(4 * q**3, k * v)
        for col in range(m):
            vals = [Q[row][col] for row in range(m)]
            assert vals.count(R) == 1
            assert vals.count(F(q * q, k * v)) == 2 * q
            assert vals.count(-F(q, k * v)) == 2 * q * q
            assert vals.count(F(1, k * v)) == q**3
    print(f"PASS symmetric ({v},{k},{lam}): "
          f"{m} columns; cut norm {norm_Q}; cycle norm {norm_C}; "
          "exact grounded inverse, all entries and idempotence")


if __name__ == '__main__':
    for blocks in (pg2(2), pg2(3), biplane11(), crown(5)):
        audit(blocks)
    print('ALL CHECKS PASSED')
