#!/usr/bin/env python3
"""Finite-dimensional algebra checks for shift-based modulus-order perturbations.

The analytical infinite-dimensional theorem is proved separately. This code
checks exact dyadic Gaussian-rational matrix identities for finite sections;
finite checks cannot certify the infinite-dimensional norm asymptotics.
"""

def mm(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def plus(a, b):
    return [[x + y for x, y in zip(rowa, rowb)]
            for rowa, rowb in zip(a, b)]

def times(a, z):
    return [[z * v for v in row] for row in a]

def adj(a):
    n = len(a)
    return [[a[j][i].conjugate() for j in range(n)] for i in range(n)]

def comm(a, b):
    return plus(mm(a, b), times(mm(b, a), -1))

def check(n):
    I = [[complex(i == j) for j in range(n)] for i in range(n)]
    S = [[complex(i == j + 1) for j in range(n)] for i in range(n)]
    St = adj(S)
    A = plus(times(I, 2), times(plus(S, St), .5))
    Y = times(plus(S, times(St, -1)), 1/(2j))
    X = plus(I, times(Y, -1))
    B = plus(mm(A, X), mm(X, A))
    L = times(comm(A, X), 1j)
    expected = [[complex((-.5 if i == 0 else (.5 if i == n - 1 else 0)) if i == j else 0)
                 for j in range(n)] for i in range(n)]
    assert L == expected, (n, 'first-order derivative')
    assert A == adj(A) and X == adj(X) and B == adj(B)
    assert plus(mm(A, L), mm(L, A)) == times(comm(A, B), 1j), (n, 'Sylvester derivative')
    return n

if __name__ == '__main__':
    count = 0
    for n in range(2, 81):
        check(n)
        count += 1
    print('PASS: exact dyadic algebra for', count, 'finite shift sections (n=2,...,80).')
    print('FINITE CHECK ONLY: not a proof of the infinite-dimensional or asymptotic assertions.')
