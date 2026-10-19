"""Exact-rational checks of the upper-record/local-peak covariance theorem.

Run with Python 3 using only its standard library. Finite enumeration
checks small sizes; the unrestricted result is established by the proof.
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def expected_entry(i, j):
    """Covariance at upper-record position i and peak position j."""
    if j == i - 1:
        return -Fraction(1, 3 * i)
    if j == i:
        return Fraction(2 * i - 1, 3 * i * (i + 1))
    if j == i + 1:
        return -Fraction(i - 1, 3 * i * (i + 2))
    return Fraction(0)


def matrix_formula(n):
    return [[expected_entry(i, j) for j in range(2, n)]
            for i in range(2, n)]


def matrix_by_enumeration(n):
    entries = [[Fraction(0) for _ in range(n - 2)]
               for _ in range(n - 2)]
    for pi in permutations(range(n)):
        records = [int(pi[i-1] == max(pi[:i])) for i in range(2, n)]
        peaks = [int(pi[j-2] < pi[j-1] > pi[j]) for j in range(2, n)]
        for i, r in enumerate(records):
            if r:
                for j, p in enumerate(peaks):
                    entries[i][j] += p
    den = factorial(n)
    for row, i in enumerate(range(2, n)):
        for col in range(n - 2):
            entries[row][col] = entries[row][col] / den - Fraction(1, 3*i)
    return entries


def multiply(a, b):
    m = len(a)
    return [[sum((a[i][k] * b[k][j] for k in range(m)), Fraction(0))
             for j in range(m)] for i in range(m)]


def lu_factors(n):
    m = n - 2
    L = [[Fraction(int(i == j)) for j in range(m)] for i in range(m)]
    U = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for index in range(m):
        i = index + 2
        U[index][index] = Fraction(1, 3*i)
        if index:
            L[index][index-1] = -Fraction(i-1, i)
        if index+1 < m:
            U[index][index+1] = -Fraction(i-1, 3*i*(i+2))
    return L, U


def inverse_fraction(A):
    m=len(A)
    augmented = [row[:] + [Fraction(int(i == j)) for j in range(m)]
                 for i, row in enumerate(A)]
    for k in range(m):
        pivot = augmented[k][k]
        assert pivot != 0
        augmented[k] = [v / pivot for v in augmented[k]]
        for i in range(m):
            if i != k:
                f = augmented[i][k]
                augmented[i] = [a - f*b for a,b in zip(augmented[i],augmented[k])]
    return [row[m:] for row in augmented]


def main():
    checks=0
    for n in range(3,9):
        actual = matrix_by_enumeration(n)
        theory = matrix_formula(n)
        for i in range(n-2):
            for j in range(n-2):
                assert actual[i][j] == theory[i][j], (n, i, j)
                checks += 1
    for n in range(3,35):
        M=matrix_formula(n)
        L,U=lu_factors(n)
        assert multiply(L,U)==M, n
        checks+=1
        product=Fraction(1)
        for i in range(2,n):
            product *= U[i-2][i-2]
        assert product == Fraction(1, 3**(n-2)*factorial(n-1))
        checks+=1
    for n in range(3,14):
        M=matrix_formula(n)
        Q=inverse_fraction(M)
        assert all(x>0 for row in Q for x in row)
        checks+=sum(len(row) for row in Q)
        I=multiply(M,Q)
        assert all(I[i][j] == int(i==j)
                   for i in range(n-2) for j in range(n-2))
        checks+=(n-2)**2
    print('PASS: %d exact-rational assertions (enumeration n=3..8; '
          'LU n=3..34; inverse n=3..13)' % checks)


if __name__ == '__main__':
    main()
