"""Exact-rational verification of reciprocal-chord Kemeny network-design formulas.

Requires only Python 3.9+ standard library.  These are finite checks,
not a substitute for the all-dimensional determinant argument.
"""
from fractions import Fraction as Q
from itertools import combinations


def det(M):
    """Exact Gaussian elimination, independent of characteristic formulas."""
    A = [[Q(x) for x in row] for row in M]
    n = len(A)
    out = Q(1)
    for i in range(n):
        p = next((k for k in range(i, n) if A[k][i]), None)
        if p is None:
            return Q(0)
        if p != i:
            A[p], A[i] = A[i], A[p]
            out = -out
        pivot = A[i][i]
        out *= pivot
        for j in range(i + 1, n):
            f = A[j][i] / pivot
            if f:
                for k in range(i + 1, n):
                    A[j][k] -= f * A[i][k]
                A[j][i] = Q(0)
    return out


def matrix(n, k, a, b):
    L = [[Q(int(i == j)) - Q(int((i + 1) % n == j))
          for j in range(n)] for i in range(n)]
    L[0][0] += a
    L[0][k] -= a
    L[k][k] += b
    L[k][0] -= b
    return L


def minor(L, omit):
    keep = [i for i in range(len(L)) if i not in omit]
    return [[L[i][j] for j in keep] for i in keep]


def kemeny_from_independent_minors(L):
    n = len(L)
    c1 = sum((det(minor(L, (i,))) for i in range(n)), Q(0))
    c2 = sum((det(minor(L, pair)) for pair in combinations(range(n), 2)), Q(0))
    assert c1 > 0
    return c2 / c1


def formula(n, k, a, b):
    return Q(n - 1, 2) + (a * (n - k) * (k - 2)
        + b * k * (n - k - 2)) / (2 * (n + a * (n - k) + b * k))


def polynomial(n, k, a, b, z):
    d = 1 + z
    return (d ** n - 1 + a * (d ** (n - 1) - d ** (k - 1))
            + b * (d ** (n - 1) - d ** (n-k-1)))


def full_determinant(L, z):
    return det([[L[i][j] + (z if i == j else 0)
                 for j in range(len(L))] for i in range(len(L))])


def run():
    checks = 0
    pairs = [(Q(0), Q(0)), (Q(1), Q(0)), (Q(0), Q(1)),
             (Q(2, 3), Q(1, 4)), (Q(3, 2), Q(5, 7)),
             (Q(1, 5), Q(4)), (Q(4), Q(1, 5))]
    for n in range(4, 11):
        for k in range(2, n - 1):
            for a, b in pairs:
                L = matrix(n, k, a, b)
                assert kemeny_from_independent_minors(L) == formula(n, k, a, b)
                checks += 1
                for z in (Q(1, 3), Q(2)):
                    assert full_determinant(L, z) == polynomial(n, k, a, b, z)
                    checks += 1
                if n == 4:
                    assert formula(n, k, a, b) == Q(3, 2)
                    checks += 1
                elif a > 0 and b > 0:
                    assert formula(n, k, a, b) > Q(n - 1, 2)
                    checks += 1
            t = Q(9, 5)
            h_a = formula(n, k, t, Q(0))
            h_b = formula(n, k, Q(0), t)
            h_mid = formula(n, k, t / 2, t / 2)
            lo = min(h_a, h_b)
            hi = max(h_a, h_b)
            assert lo <= h_mid <= hi
            checks += 1
            if k < n / 2:
                assert h_a < h_b
                checks += 1
            elif k > n / 2:
                assert h_b < h_a
                checks += 1
            else:
                assert h_b == h_a == h_mid
                checks += 1
            for t in (Q(1, 7), Q(1), Q(13, 4)):
                assert formula(n, k, t, t) == Q(n - 1, 2) + t * (k*(n-k)-n) / (n*(1+t))
                checks += 1
    # Directional recovery after an already harmful reverse rate:
    # n=7, k=3, reversal threshold b=7/3.
    assert formula(7, 3, Q(0), Q(3)) > formula(7, 3, Q(1), Q(3)) > Q(3)
    checks += 1
    assert formula(7, 3, Q(0), Q(1)) < formula(7, 3, Q(1), Q(1))
    checks += 1
    print('PASS', checks, 'exact-rational checks')
    return checks


if __name__ == '__main__':
    run()
