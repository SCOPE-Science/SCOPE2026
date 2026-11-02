"""Finite exact tests for the model-space boundary quotient formulas.

The analytical infinite-rank and asymptotic claims require the proof, not this script.
Runs with the Python standard library alone: python check.py
"""
from fractions import Fraction as F


def mm(A, B):
    return [[sum((x * y for x, y in zip(row, col)), F(0))
             for col in zip(*B)] for row in A]


def transpose(A):
    return [list(col) for col in zip(*A)]


def ident(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse_shape(a, n):
    c = 1 + a
    return [[F(1, a) if i == j else
             ((-1) ** (i-j) * c / a**(i-j+1) if i > j else F(0))
             for j in range(n)] for i in range(n)]


def matrices(a, n):
    c = 1+a
    eta = a/c
    A = [[a if i == j else c if i > j else F(0)
          for j in range(n)] for i in range(n)]
    U = [[min(i, j)+eta for j in range(n)] for i in range(n)]
    P = [[(1/eta if n == 1 else 1+1/eta) if i == j == 0 else
          (1 if i == j == n-1 else 2 if i == j else
           -1 if abs(i-j) == 1 else 0)
          for j in range(n)] for i in range(n)]
    return A, U, P


def bj(a, j, z):
    return ((z-a)/(1-a*z))**j / (1-a*z)


def main():
    checks = 0
    for a in [F(1, 5), F(1, 2), F(3, 4)]:
        for n in range(1, 13):
            A, U, P = matrices(a, n)
            B = inverse_shape(a, n)
            I = ident(n)
            assert mm(U, P) == I
            checks += 1
            assert mm(P, U) == I
            checks += 1
            assert mm(A, B) == I
            checks += 1
            assert mm(B, A) == I
            checks += 1
            ATA = mm(A, transpose(A))
            assert all(ATA[i][j]+(a if i == j else 0) ==
                       (1+a)**2*U[i][j]
                       for i in range(n) for j in range(n))
            checks += n*n
            for z in [F(1, 7), F(2, 5), F(-1, 3)]:
                for j in range(n):
                    quotient = (bj(a, j, z)-bj(a, j, F(1))) / (z-1)
                    expansion = sum((A[j][i] * bj(a, i, z)/(1-a)
                                     for i in range(n)), F(0))
                    assert quotient == expansion
                    checks += 1
    print('PASS:', checks, 'exact rational assertions')


if __name__ == '__main__':
    main()
