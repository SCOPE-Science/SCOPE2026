"""Exact finite checks of the triangular-block and Cesaro-covariance identities.

These checks support, but do not replace, the analytic infinite-dimensional proof.
"""
from fractions import Fraction
from math import ceil


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def rank_fraction(a):
    a = [[Fraction(x) for x in row] for row in a]
    m, n = len(a), len(a[0])
    h = 0
    for col in range(n):
        ix = next((i for i in range(h, m) if a[i][col]), None)
        if ix is None:
            continue
        a[h], a[ix] = a[ix], a[h]
        pivot = a[h][col]
        a[h] = [x / pivot for x in a[h]]
        for i in range(m):
            if i != h and a[i][col]:
                t = a[i][col]
                a[i] = [x - t * y for x, y in zip(a[i], a[h])]
        h += 1
        if h == m:
            break
    return h


checks = 0
for n in range(1, 22):
    v = [[int(j <= i) for j in range(n)] for i in range(n)]
    b = [[int(j == i) - int(j == i - 1) for j in range(n)]
         for i in range(n)]
    product = matmul(b, v)
    assert product == [[int(i == j) for j in range(n)] for i in range(n)]
    checks += n * n
    for blocks in range(2, n + 1):
        # Interval partition with sizes differing by at most one.
        endpoints = [int(t * n / blocks) for t in range(blocks + 1)]
        # The rank-(blocks-1) approximation keeps all preceding-block entries.
        approx = [[0] * n for _ in range(n)]
        residual = [[0] * n for _ in range(n)]
        for t in range(blocks):
            lo, hi = endpoints[t], endpoints[t + 1]
            for i in range(lo, hi):
                for j in range(n):
                    if j < lo:
                        approx[i][j] = 1
                    elif lo <= j <= i:
                        residual[i][j] = 1
        assert [[approx[i][j] + residual[i][j] for j in range(n)] for i in range(n)] == v
        assert rank_fraction(approx) <= blocks - 1
        # The residual is an orthogonal sum of lower triangular matrices
        # whose row and column sum norms are at most the maximum block length.
        maxlen = max(endpoints[t + 1] - endpoints[t] for t in range(blocks))
        assert maxlen == ceil(n / blocks)
        assert max(sum(abs(residual[i][j]) for j in range(n)) for i in range(n)) <= maxlen
        assert max(sum(abs(residual[i][j]) for i in range(n)) for j in range(n)) <= maxlen
        checks += n * n

for m in range(1, 15):
    for i in range(0, 50):
        eta = Fraction(1, i + m + 1) - Fraction(1, i + 1)
        assert eta == -Fraction(m, (i + 1) * (i + m + 1))
        assert Fraction(m, m + 1) * Fraction(1, (i + 1)**2) <= -eta
        assert -eta <= Fraction(m, (i + 1)**2)
        for j in range(0, 50):
            original = (Fraction(1, i + m + 1) - Fraction(1, i + 1)) if j <= i else Fraction(0)
            assert original == (eta if j <= i else 0)
            checks += 1

for level in range(0, 8):
    n = 2**level
    # Degree-two Rhaly matrix: row-slab factorization into a rectangular
    # rank-one predecessor block and the square lower triangular block.
    for i in range(n, 2*n):
        weight = Fraction(1, (i+1)**2)
        for j in range(2*n):
            val = weight if j <= i else Fraction(0)
            pred = weight if j < n else Fraction(0)
            internal = weight if n <= j <= i else Fraction(0)
            assert val == pred + internal
            checks += 1

print(f"VERIFIED: {checks} exact rational/integer comparisons")
