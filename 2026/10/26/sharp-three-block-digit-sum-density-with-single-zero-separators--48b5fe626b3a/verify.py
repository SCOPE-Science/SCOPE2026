"""Exact rational checks for a three-block binary digit-sum density theorem.
Run: python verify.py. Requires Python >=3.8; no third-party modules.
"""
from fractions import Fraction as Q
from itertools import product


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(2)), Q(0))
             for j in range(2)] for i in range(2)]


def H(X):
    X = Q(X)
    return [[1 / X, Q(2, 3) * (X - 1 / X)], [Q(0), X]]

S = [[Q(1), Q(0)], [Q(1, 2), Q(1)]]


def R2(X, Y, Z):
    T = H(X)
    for V in (S, H(Y), S, H(Z)):
        T = matmul(T, V)
    return T[0][1]


def poly(X, Y, Z):
    return (16*X*X*Y*Y*Z*Z - 4*X*X*Y*Y - X*X*Z*Z
            -2*X*X -4*Y*Y*Z*Z + Y*Y -2*Z*Z -4)


def formula(a, b, c):
    A, B, C = [Q(1, 4**j) for j in (a, b, c)]
    return (115+32*A+8*B+32*C+16*A*B-8*A*C
            +16*B*C+32*A*B*C)/216


def direct(a, b, c):
    t = int('1'*c + '0' + '1'*b + '0' + '1'*a, 2)
    length = a+b+c+2
    modulus = 1 << length
    total = Q(0)
    for low in range(modulus):
        out = low + t
        delta = (out % modulus).bit_count() - low.bit_count()
        if out < modulus:
            total += (delta >= 0)
        elif delta >= -1:
            # Upper bits receive +1, with 2^{-j-1} probability
            # of exactly j trailing 1 bits; then change is 1-j.
            total += 1-Q(1, 2**(delta+2))
    return total / modulus


# Both sides below are multiaffine in X^2, Y^2, Z^2.
# Equality on a Cartesian grid of 2^3 nodes proves universal equality.
for X, Y, Z in product((2,4), repeat=3):
    assert Q(27*X*Y*Z, 2)*R2(X,Y,Z) == poly(X,Y,Z), (X,Y,Z)

for a, b, c in product(range(1,7), repeat=3):
    X,Y,Z = 2**a,2**b,2**c
    assert formula(a,b,c) == Q(9,8)-R2(X,Y,Z)/2**(a+b+c+1)

for a, b, c in product(range(1,4), repeat=3):
    assert direct(a,b,c) == formula(a,b,c), (a,b,c)

assert formula(2,2,2) == Q(567,1024) < Q(5,9)
assert formula(1,1,1) == Q(5,8)
print('VERIFY_OK: 8 exact polynomial interpolation nodes; 216 transfer checks; 27 independent residue enumerations')
