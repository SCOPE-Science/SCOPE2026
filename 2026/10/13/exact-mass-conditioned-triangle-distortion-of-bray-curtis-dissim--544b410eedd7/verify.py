"""Exact finite tests for the prescribed-mass Bray--Curtis distortion theorem.

The theorem's proof is algebraic; these integer tests independently exercise its
case boundaries and explicit two-species attaining construction.
"""
from fractions import Fraction
from itertools import product


def parts(total, size):
    if size == 1:
        yield (total,)
    else:
        for q in range(total + 1):
            for tail in parts(total - q, size - 1):
                yield (q,) + tail


def distance(x, y):
    return Fraction(sum(abs(a - b) for a, b in zip(x, y)),
                    sum(x) + sum(y))


def bound(m, b, M):
    assert 0 < m <= M and b > 0
    if b <= m:
        return Fraction(m + b, 2 * m)
    if b <= m + M:
        return 1 / (Fraction(b - m, m + b) +
                    Fraction(M + 2 * m - b, M + b))
    return 1 / (Fraction(b - m, m + b) +
                Fraction(b - M, M + b))


def actual(x, y, z):
    denom = distance(x, y) + distance(y, z)
    return distance(x, z) / denom if denom else None


def check():
    count = witness_count = 0
    for m in range(1, 9):
        for M in range(m, 9):
            for b in range(1, 9):
                r = bound(m, b, M)
                x, z = (m, 0), (0, M)
                y = (min(m, b), max(0, b - m))
                assert sum(x) == m and sum(y) == b and sum(z) == M
                assert actual(x, y, z) == r
                witness_count += 1
                # All two-species integer profiles at the prescribed masses.
                for i, j, k in product(range(m + 1), range(b + 1), range(M + 1)):
                    a = (i, m - i)
                    mid = (j, b - j)
                    c = (k, M - k)
                    q = actual(a, mid, c)
                    if q is not None:
                        assert q <= r, (m, b, M, a, mid, c, q, r)
                    count += 1
    # Higher-dimensional independent enumeration for additional checks.
    count_three = 0
    for m in range(1, 5):
        for M in range(m, 5):
            for b in range(1, 5):
                r = bound(m, b, M)
                P, Q, S = (list(parts(v, 3)) for v in (m, b, M))
                for a, mid, c in product(P, Q, S):
                    q = actual(a, mid, c)
                    if q is not None:
                        assert q <= r, (m, b, M, a, mid, c)
                    count_three += 1
    print('VERIFY_OK mass_triples=%d 2d_profiles=%d 3d_profiles=%d exact_witnesses=%d' %
          (witness_count, count, count_three, witness_count))

if __name__ == '__main__':
    check()
