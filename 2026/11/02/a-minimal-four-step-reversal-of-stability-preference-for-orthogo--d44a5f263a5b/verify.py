#!/usr/bin/env python3
"""Exact, dependency-free checks for the two balanced four-step shear schedules."""
from fractions import Fraction as F
from itertools import permutations


def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def prod(matrices):
    result = ((F(1), F(0)), (F(0), F(1)))
    for matrix in matrices:
        result = mm(result, matrix)
    return result


def trace(A):
    return A[0][0] + A[1][1]


def determinant(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def strictly_stable(t, d):
    return 1-d > 0 and 1+t+d > 0 and 1-t+d > 0


def calc(a, k):
    q, x = a*a, k*k
    U = ((a, k), (F(0), a))
    L = ((a, F(0)), (-k, a))
    G = prod([U,U,L,L])
    A = prod([U,L,U,L])
    assert trace(G) == 2*q*q - 4*q*x
    assert trace(A) == 2*q*q - 4*q*x + x*x
    assert determinant(G) == q**4 == determinant(A)
    assert strictly_stable(trace(G),determinant(G)) == (x < (1+q*q)**2/(4*q))
    assert strictly_stable(trace(A),determinant(A)) == (x < (1+q)**2)
    assert trace(A) - trace(G) == k**4
    for word in set(permutations(('U','U','L','L'))):
        M = prod([U if letter == 'U' else L for letter in word])
        assert determinant(M) == q**4
        transitions = sum(word[i] != word[(i+1)%4] for i in range(4))
        assert transitions in (2,4)
        target = trace(G) if transitions == 2 else trace(A)
        assert trace(M) == target
    return trace(G), trace(A), q**4


def polynomial(q):
    return q**4 - 4*q**3 - 6*q**2 - 4*q + 1


def main():
    num = 0
    for d in (2,3,4,5,7,9,11,13,19):
        for i in range(1,d):
            a=F(i,d)
            for k in (F(0), F(1,5), F(2,3), F(7,6), F(3,2), F(9,4), F(4,1)):
                calc(a,k)
                num+=1
    tG,tA,d=calc(F(1,4),F(3,2))
    assert (tG,tA,d) == (F(-71,128), F(577,128), F(1,65536))
    assert strictly_stable(tG,d) and not strictly_stable(tA,d)
    tG,tA,d=calc(F(1,2),F(7,6))
    assert (tG,tA,d) == (F(-89,72), F(799,1296), F(1,256))
    assert not strictly_stable(tG,d) and strictly_stable(tA,d)
    assert polynomial(F(18959,100000)) > 0
    assert polynomial(F(18960,100000)) < 0
    # Both threshold exits have the claimed unit-circle multipliers.
    for q in (F(1,16), F(1,4), F(4,9), F(9,16)):
        xG=(1+q*q)**2/(4*q)
        xA=(1+q)**2
        assert 2*q*q-4*q*xG == -(1+q**4)
        assert 2*q*q-4*q*xA+xA*xA == 1+q**4
    print('EXACT_CHECKS_OK', num, 'rational parameter pairs; six balanced words each; two reversal witnesses')


if __name__=='__main__':
    main()
