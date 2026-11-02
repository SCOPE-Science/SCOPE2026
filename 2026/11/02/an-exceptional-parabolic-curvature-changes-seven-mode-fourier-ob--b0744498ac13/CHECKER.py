#!/usr/bin/env python3
"""Exact integer verification of the jet-determinant identities in RESULT.md.

Standalone, standard-library-only. Evaluating a polynomial identity at more
integer points than its degree certifies the identity over Q.
"""
from math import factorial
from itertools import combinations


def jet(k, n, w):
    return sum(
        factorial(k) // (factorial(j) * factorial(k-2*j))
        * (n*n)**(k-2*j) * (w*n)**j
        for j in range(k//2+1)
    )


def determinant(A):
    M = [list(map(int, row)) for row in A]
    d = len(M)
    if d == 1:
        return M[0][0]
    sign = 1
    prev = 1
    for k in range(d-1):
        if M[k][k] == 0:
            pivot = next((i for i in range(k+1, d) if M[i][k]), None)
            if pivot is None:
                return 0
            M[k], M[pivot] = M[pivot], M[k]
            sign = -sign
        p = M[k][k]
        for i in range(k+1, d):
            for j in range(k+1, d):
                numerator = p*M[i][j] - M[i][k]*M[k][j]
                assert numerator % prev == 0, 'nonexact Bareiss step'
                M[i][j] = numerator//prev
        for i in range(k+1, d):
            M[i][k] = 0
        prev = p
    return sign * M[d-1][d-1]


def det_rows(rows, ns, w):
    return determinant([[jet(k,n,w) for n in ns] for k in rows])


def main():
    # Degrees are bounded by the sum of floor(k/2) across rows.
    for w in range(-5, 6):
        assert det_rows(range(3), range(-1,2), w) == -4*w
        assert det_rows(range(5), range(-2,3), w) == 17280*w*w
        assert det_rows(range(7), range(-3,4), w) == 597196800*w**3*(57600*w**4-47320*w*w-22247)
        assert det_rows([0,1,2,3,4,5,7], range(-3,4), w) == 83607552000*w**3*(12600*w**4-7369*w*w-5272)
        assert det_rows(range(6), [-3,-2,-1,1,2,3], w) == 66355200*w**3*(90*w*w-143)
    print('PASS: all five exact jet polynomial identities certified at 11 integer points')
    print('Degree bounds: 1, 4, 9, 9, 6; 11 points exceed every bound.')

if __name__ == '__main__':
    main()
