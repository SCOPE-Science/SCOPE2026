"""Exact-rational checks for the two-patch switching benchmark.

The general mathematical argument is in RESULT.md; these tests independently
recompute the rational example and selected symbolic-identity instances.
Run: python3 check.py
"""
from fractions import Fraction as F


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def rowmul(u, A):
    return [sum(u[k] * A[k][j] for k in range(2)) for j in range(2)]


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def Iminus(A):
    return [[F(i == j) - A[i][j] for j in range(2)] for i in range(2)]


def matrices(a, b, m):
    P = [[1 - m, m], [m, 1 - m]]
    A = mul(P, [[a, F(0)], [F(0), b]])
    B = mul(P, [[b, F(0)], [F(0), a]])
    return A, B


def check_general_identity(a, b, m):
    A, B = matrices(a, b, m)
    C = a + b - 2 * a * b
    T = mul(B, A)
    assert det(Iminus(A)) == (1-a)*(1-b) + C*m
    assert det(Iminus(B)) == (1-a)*(1-b) + C*m
    assert det(Iminus(T)) == (1-a*b-C*m)*(1-a*b+m*(a+b+2*a*b))
    assert det(T) == (a*b)**2 * (1-2*m)**2


a = F(3)
b = F(1, 4)
m = F(9, 10)
q = F(3, 4)
A, B = matrices(a, b, m)
assert A == [[F(3, 10), F(9, 40)], [F(27, 10), F(1, 40)]]
assert B == [[F(1, 40), F(27, 10)], [F(9, 40), F(3, 10)]]
C = a + b - 2*a*b
assert C == F(7, 4)
assert (a-1)*(1-b)/C == F(6, 7)
assert (1-a*b)/C == F(1, 7)
assert m > F(6, 7) and m > F(1, 7)

uA, uB = [F(99), F(1)], [F(1), F(99)]
r, switch_factor = F(18, 55), F(27, 10)
assert rowmul(uA, A) == [F(162, 5), F(223, 10)]
assert rowmul(uB, B) == [F(223, 10), F(162, 5)]
assert rowmul(uA, B) == [F(27, 10), F(1338, 5)]
assert rowmul(uB, A) == [F(1338, 5), F(27, 10)]
for v, w, factor in ((rowmul(uA,A),uA,r),
                     (rowmul(uB,B),uB,r),
                     (rowmul(uA,B),uB,switch_factor),
                     (rowmul(uB,A),uA,switch_factor)):
    assert all(x >= factor*y for x,y in zip(v,w))
assert switch_factor**3*r == F(177147, 27500) > 1
assert a*b == F(3,4) < 1

n = 0
for a0 in (F(3, 2), F(2), F(3), F(5)):
    for b0 in (F(1, 9), F(1, 5), F(1, 7)):
        if a0*b0 >= 1:
            continue
        for m0 in (F(0),F(1,10),F(1,4),F(1,2),F(3,4),F(9,10),F(1)):
            check_general_identity(a0,b0,m0)
            n += 1
print('PASS: exact rational example and', n, 'determinant-identity instances')
print('Switch base:', switch_factor, 'non-switch base:', r)
print('Four-step certificate:', switch_factor**3*r, '> 1')
