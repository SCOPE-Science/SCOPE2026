#!/usr/bin/env python3
from fractions import Fraction as F

one = (F(1), F(1), F(1))
P = (
    (F(2,3), F(-1,3), F(-1,3)),
    (F(-1,3), F(2,3), F(-1,3)),
    (F(-1,3), F(-1,3), F(2,3)),
)

def matvec(A, v):
    return tuple(sum(A[i][j]*v[j] for j in range(3)) for i in range(3))

def matmul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def norm2(a):
    return dot(a,a)

assert P == tuple(tuple(P[j][i] for j in range(3)) for i in range(3))
assert matmul(P,P) == P
assert matvec(P, one) == (0,0,0)
for col in range(3):
    assert sum(P[row][col] for row in range(3)) == 0

def sir(S,I,beta,gamma):
    return (-beta*S*I, beta*S*I-gamma*I, gamma*I)

states = [
    (F(9,10),F(1,10)),
    (F(3,5),F(1,4)),
    (F(7,20),F(2,5)),
]
pars = [
    (F(7,20),F(1,10),F(3,10),F(3,25)),
    (F(2,5),F(1,8),F(1,3),F(1,9)),
]
for S,I in states:
    for bt,gt,bd,gd in pars:
        r = sub(sir(S,I,bt,gt), sir(S,I,bd,gd))
        assert sum(r) == 0
        assert matvec(P,r) == r

targets = [
    (F(5,7),F(-2,9),F(4,11)),
    (F(-3,8),F(7,10),F(5,6)),
    (F(13,17),F(-9,19),F(2,23)),
]
residuals = [
    (F(1,5),F(-3,10),F(1,10)),
    (F(-2,7),F(5,14),F(-1,14)),
]
IminusP = (
    (F(1,3),F(1,3),F(1,3)),
    (F(1,3),F(1,3),F(1,3)),
    (F(1,3),F(1,3),F(1,3)),
)
for Y in targets:
    for r in residuals:
        assert sum(r) == 0
        PY = matvec(P,Y)
        normal = matvec(IminusP,Y)
        assert norm2(sub(Y,r)) == norm2(sub(PY,r)) + norm2(normal)
        assert norm2(sub(PY,r)) <= norm2(sub(Y,r))

print("VERIFY_OK")
