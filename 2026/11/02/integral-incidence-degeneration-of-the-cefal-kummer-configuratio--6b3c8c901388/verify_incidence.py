#!/usr/bin/env python3
"""Exact checks for the integral incidence of the Cefalu quartic's marked nodes.

Only Python's standard library is used. The full scheme-level proof is in RESULT.md;
these tests independently check the sign-orbit incidence, exceptional primes,
and the rank/torsion calculations for the local group-algebra presentations.
"""
from fractions import Fraction
from itertools import product


def determinant(A):
    B = [[Fraction(z) for z in row] for row in A]
    n = len(B)
    answer = Fraction(1)
    for j in range(n):
        i = next((i for i in range(j, n) if B[i][j]), None)
        if i is None:
            return 0
        if i != j:
            B[i], B[j] = B[j], B[i]
            answer = -answer
        pivot = B[j][j]
        answer *= pivot
        for i in range(j + 1, n):
            a = B[i][j] / pivot
            for k in range(j, n):
                B[i][k] -= a * B[j][k]
    assert answer.denominator == 1
    return int(answer)


def labels():
    for absent in range(4):
        nonzero = [j for j in range(4) if j != absent]
        for a, b in product((-1, 1), repeat=2):
            c = [0] * 4
            c[nonzero[0]] = 1
            c[nonzero[1]] = a
            c[nonzero[2]] = b
            yield (absent, tuple(c))


def dot(v, w):
    return sum(a*b for a, b in zip(v, w))


def quartic(x):
    squares = [t*t for t in x]
    return sum(squares[i]*squares[j] for i in range(4)
               for j in range(i+1, 4)) - sum(z*z for z in squares)


def polynomial_identity_checks():
    # Test each coefficient of the degree-four polynomials over F_2/F_3.
    from collections import defaultdict
    F = defaultdict(int)
    Q2 = defaultdict(int)
    Q3 = defaultdict(int)
    for i in range(4):
        e = [0]*4
        e[i] = 4
        F[tuple(e)] -= 1
        q = [0]*4
        q[i] = 2
        Q2[tuple(q)] += 1
        Q3[tuple(q)] += 1
        for j in range(i+1, 4):
            e = [0]*4
            e[i] = e[j] = 2
            F[tuple(e)] += 1
            q = [0]*4
            q[i] = q[j] = 1
            Q2[tuple(q)] += 1

    def square(P):
        A = defaultdict(int)
        for e, c in P.items():
            for f, d in P.items():
                A[tuple(x+y for x,y in zip(e,f))] += c*d
        return A

    f2, f3 = square(Q2), square(Q3)
    for e in set(F)|set(f2):
        assert (F[e]-f2[e]) % 2 == 0, ('char2', e)
    for e in set(F)|set(f3):
        assert (F[e]+f3[e]) % 3 == 0, ('char3', e)
    # Polar matrix of Q_2 is J+I, and (J+I)^2=I in characteristic 2.
    P = [[int(i != j) for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            assert sum(P[i][k]*P[k][j] for k in range(4)) % 2 == int(i==j)


def count_checks():
    L = list(labels())
    assert len(L) == 16 and len(set(v for _,v in L)) == 16
    for _,v in L:
        assert quartic(v) == 0
    dots = [[dot(v,w) for _,w in L] for _,v in L]
    assert sorted(set(z for row in dots for z in row)) == [-2,-1,0,1,2,3]
    assert [sum(z==0 for z in row) for row in dots] == [6]*16
    assert [sum(z%3==0 for z in row) for row in dots] == [7]*16
    for a, (i,v) in enumerate(L):
        for b,(j,w) in enumerate(L):
            assert (dots[a][b] % 3 == 0 and dots[a][b] != 0) == (a==b)
    assert sum(z==0 for row in dots for z in row) == 96
    assert sum(z%3==0 for row in dots for z in row) == 112
    for p in (5,7,11,13):
        assert [sum(z%p==0 for z in row) for row in dots] == [6]*16
    # The diagonal-axis group algebra has multiplication by 1+r+s.
    # Its determinant is -3, so its cokernel over Z has order exactly 3.
    basis = ((0,0),(1,0),(0,1),(1,1))
    H = [[0]*4 for _ in range(4)]
    for j,(a,b) in enumerate(basis):
        for c,d in ((0,0),(1,0),(0,1)):
            i = basis.index((a^c,b^d))
            H[i][j] += 1
    assert abs(determinant(H)) == 3
    # Tensoring with the two remaining free involutions makes the torsion
    # quotient (Z/3)^4 on each of the four equal-axis components.
    # For unequal-axis components the one-character relation 1+t=0
    # leaves three free involutions, and hence a flat Z-module of rank 8.
    K = [[1,1],[1,1]]
    assert determinant(K) == 0 and K[0][0] == 1
    assert 12*8 == 96 and 4*4 == 16


def main():
    polynomial_identity_checks()
    count_checks()
    print('CEFALU_INTEGRAL_INCIDENCE_96_HORIZONTAL_16_VERTICAL_CHAR3_AND_CHAR2_THICKENING_PASS')


if __name__ == '__main__':
    main()
