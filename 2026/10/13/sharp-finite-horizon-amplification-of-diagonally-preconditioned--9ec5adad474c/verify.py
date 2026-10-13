"""Exact checks of the sharp normalized oblique-write product theorem.

Run with Python >=3.9: python verify.py. Standard library only.
The universal upper bound is proved in the accompanying paper, not by this test.
"""
from fractions import Fraction as Q
from math import sqrt
import random


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def transpose(A):
    return [[A[j][i] for j in range(2)] for i in range(2)]


def trace(A):
    return A[0][0] + A[1][1]


def norm2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    tr = a*a+b*b+c*c+d*d
    det = a*d-b*c
    return sqrt((tr+sqrt(max(0.0, tr*tr-4*det*det)))/2)


def det(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]


# For parameter kappa=t*t, P1 and P2=P1^T are rational, although
# the normalized key coordinates contain sqrt(1+t*t).
identities = 0
for t in range(2, 17):
    u = Q(t)
    P = [[Q(1,2), -1/(2*u)], [-u/2, Q(1,2)]]
    T = transpose(P)
    C2 = Q((t*t+1)**2, 4*t*t)
    assert matmul(P,P) == P
    assert matmul(T,T) == T
    assert det(P) == 0
    assert trace(matmul(P,T)) == C2
    # Kill own key, while the transpose is induced by the reciprocal key.
    assert P[0][0]+t*P[0][1] == P[1][0]+t*P[1][1] == 0
    assert t*T[0][0]+T[0][1] == t*T[1][0]+T[1][1] == 0
    identities += 6
    M = [[Q(1),Q(0)],[Q(0),Q(1)]]
    for n in range(1, 19):
        M = matmul(M, P if n%2 else T)
        assert det(M) == 0
        assert trace(matmul(M,transpose(M))) == C2**n
        identities += 2

# Two distinct allowed preconditioners in the practical [0.5, 2] box:
# kappa=2, D1=diag(2,1), D2=diag(1,2), gate=3/4.
t=sqrt(2.0)
P=[[0.5,-1/(2*t)],[-t/2,0.5]]
T=transpose(P)
assert 0.0 < 0.75 < 1.0
assert abs(norm2(matmul(P,T))-9/8) < 2e-14
assert abs(norm2(P)-3/(2*t)) < 2e-14

# Random finite checks of the product upper bound (not a proof).
rng=random.Random(19340513)
tests=0
for kappa in (1.0, 1.001, 1.2, 1.5, 2.0, 4.0, 10.0, 100.0):
    C=(kappa+1)/(2*sqrt(kappa))
    for trial in range(500):
        M=[[1.0,0.0],[0.0,1.0]]
        for n in range(1, 13):
            a,b=rng.gauss(0,1),rng.gauss(0,1)
            r=sqrt(a*a+b*b)
            a/=r; b/=r
            d1=1+(kappa-1)*rng.random()
            d2=1+(kappa-1)*rng.random()
            mu=d1*a*a+d2*b*b
            Qp=[[1-d1*a*a/mu,-a*d2*b/mu],[-b*d1*a/mu,1-d2*b*b/mu]]
            M=matmul(M,Qp)
            assert norm2(M) <= C**n*(1+2e-11)
            tests+=1

print('VERIFY_OK exact_fraction_identities=',identities,
      'random_product_norm_checks=',tests,
      'two_step_growth_kappa2=',format(9/8,'.12g'))
