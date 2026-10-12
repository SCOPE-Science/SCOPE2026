#!/usr/bin/env python3
from fractions import Fraction
from math import gcd


def eye(n=3):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def mm(A, B):
    n, m, p = len(A), len(B), len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m)) for j in range(p)] for i in range(n)]


def sub_scalar(A, s):
    B = [row[:] for row in A]
    for i in range(len(B)):
        B[i][i] -= s
    return B


def scale(A, s):
    return [[s * x for x in row] for row in A]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def eq(A, B):
    return A == B


def projector(R, lam, vals):
    P = eye()
    for mu in vals:
        if mu != lam:
            P = mm(P, sub_scalar(R, Fraction(mu)))
            P = scale(P, Fraction(1, lam - mu))
    return P


def check_b(b):
    a = 2 * b - 1
    # Cell-value quotient on [root, child-level, leaf-level].
    R = [
        [Fraction(a), Fraction(-a), Fraction(0)],
        [Fraction(-1), Fraction(b + 1), Fraction(-b)],
        [Fraction(0), Fraction(-1), Fraction(1)],
    ]
    vals = [0, b, 2 * b + 1]
    Ps = [projector(R, lam, vals) for lam in vals]
    Z = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    S = Z
    for lam, P in zip(vals, Ps):
        assert eq(mm(P, P), P)
        assert eq(mm(R, P), scale(P, Fraction(lam)))
        S = add(S, P)
    assert eq(S, eye())
    e0 = Fraction(1, b * (2 * b + 1))
    eb = Fraction(b - 1, b * (b + 1))
    eh = Fraction(-2 * b, (b + 1) * (2 * b + 1))
    got = [Ps[0][1][0], Ps[1][1][0], Ps[2][1][0]]
    assert got == [e0, eb, eh]
    assert e0 > 0 and eb > 0 and eh < 0
    assert gcd(b, 2 * b + 1) == 1
    bound = abs(e0) + abs(eb) + abs(eh)
    assert bound == Fraction(4 * b, (b + 1) * (2 * b + 1))
    # At t = pi, integer eigenvalues contribute phases (-1)^lambda.
    amp_pi = e0 + ((-1) ** b) * eb + ((-1) ** (2 * b + 1)) * eh
    if b % 2 == 0:
        assert amp_pi == bound
    else:
        assert abs(amp_pi) < bound


for b in range(2, 25):
    check_b(b)
print('VERIFY_OK')
