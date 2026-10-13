"""Reproducible exact-arithmetic checks for a nonnegative-factorization landscape theorem.

Run with Python 3: python verify.py. No third-party libraries required.
Finite tests verify identities and witnesses, not the infinite-dimensional quantifiers.
"""
from fractions import Fraction as F
from random import Random


def tr(A):
    return list(map(list, zip(*A)))


def mm(A, B):
    return [[sum((a * b for a, b in zip(row, col)), F(0))
             for col in tr(B)] for row in A]


def norm2(A):
    return sum((v * v for row in A for v in row), F(0))


def sub(A, B):
    return [[a - b for a, b in zip(row, row_b)]
            for row, row_b in zip(A, B)]


def objective(Y, Z):
    m, k = len(Y), len(Z)
    r = len(Y[0])
    U = Y + Z
    target = [[F(1) if i < m and j < m else
               F(1) if i >= m and i == j else F(0)
               for j in range(m+k)] for i in range(m+k)]
    return norm2(sub(mm(U, tr(U)), target)) / 2


def split_difference(Y, Z):
    m, k = len(Y), len(Z)
    J = [[F(1)] * m for _ in range(m)]
    return (norm2(sub(mm(Y, tr(Y)), J)) / 2
            + norm2(mm(Y, tr(Z))) - norm2(Z)
            + norm2(mm(Z, tr(Z))) / 2)


def main():
    rng = Random(20260506)
    checks = 0
    for m in range(1, 8):
        for k in range(1, 4):
            for _ in range(20):
                Y = [[F(rng.randrange(1, 12), 12) for _ in range(3)]
                     for _ in range(m)]
                Z = [[F(rng.randrange(0, 5), 12) for _ in range(3)]
                     for _ in range(k)]
                assert objective(Y, Z) - F(k, 2) == split_difference(Y, Z)
                checks += 1
    # Exact perturbed candidate with balanced or unbalanced rational profile.
    profiles = [(F(3, 5), F(4, 5)), (F(5, 13), F(12, 13)),
                (F(8, 17), F(15, 17))]
    for a in profiles:
        for m in range(1, 21):
            k = 1
            Y = [list(a) for _ in range(m)]
            Z = [[F(0), F(0)]]
            assert objective(Y, Z) == F(1, 2)
            for j in (0, 1):
                t = F(1, 1000)
                Zt = [[t if h == j else F(0) for h in (0, 1)]]
                diff = objective(Y, Zt) - F(1, 2)
                assert diff == (m * a[j]**2 - 1) * t**2 + t**4 / 2
                checks += 1
    # Boundary m*min(a_j^2)=1: preserve unit norm while shifting mass.
    m = 4
    delta = F(1, 20)
    aj2 = F(1, 4)
    ah2 = F(3, 4)
    aj2new = aj2 - delta / m
    ah2new = ah2 + delta / m
    assert aj2new + ah2new == 1
    assert m * aj2new * delta - delta + delta**2 / 2 == -delta**2 / 2
    checks += 1
    # One-sided local certificate for positive upper block and Z >= 0.
    for _ in range(600):
        m, r, k = 6, 3, 2
        Y = [[F(rng.randrange(5, 9), 10) for _ in range(r)]
             for _ in range(m)]
        Z = [[F(rng.randrange(0, 6), 10) for _ in range(r)]
             for _ in range(k)]
        bmin = min(x for row in Y for x in row)
        assert norm2(mm(Y, tr(Z))) >= m * bmin**2 * norm2(Z)
        assert objective(Y, Z) - F(k, 2) >= (m*bmin*bmin-1)*norm2(Z)
        checks += 1
    print(f'VERIFY_OK {checks} exact-rational tests; boundary quartic escape identity')


if __name__ == '__main__':
    main()
