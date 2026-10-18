#!/usr/bin/env python3
"""Reproducible checks of a sharp trace-norm directional-derivative remainder.

Finite computations corroborate the proof, rather than replacing the all-dimension proof.
"""
from fractions import Fraction
import numpy as np


def nuclear(a):
    return float(np.linalg.svd(a, compute_uv=False).sum())


def remainder(A, t):
    m, n = A.shape
    P = np.zeros((m, n), dtype=float)
    P[0, 0] = 1.0
    D = A[0, 0] + nuclear(A[1:, 1:]) if min(m, n) > 1 else A[0, 0]
    return (nuclear(P + t * A) - 1.0) / t - D


def target(t, nonscalar=True):
    if nonscalar:
        return t / 2 if t <= 2 else 2 - 2 / t
    return 0 if t <= 1 else 2 - 2 / t


def exact_witnesses():
    count = 0
    # P + t A is a single-row rank-one tensor, and its squared trace norm is 1.
    for t, a, b in [(Fraction(6, 5), Fraction(-3, 5), Fraction(4, 5)),
                    (Fraction(8, 5), Fraction(-4, 5), Fraction(3, 5)),
                    (Fraction(2, 1), Fraction(-1, 1), Fraction(0, 1))]:
        assert a*a+b*b == 1
        assert a == -t/2
        assert (1+t*a)**2 + (t*b)**2 == 1
        assert (1-Fraction(1, 1))/t-a == t/2
        count += 4
    for t in [Fraction(2), Fraction(5, 2), Fraction(3), Fraction(7)]:
        # Choosing A=-P gives ||P+tA||=t-1 and D_P(A)=-1.
        assert (abs(1-t)-1)/t+1 == 2-Fraction(2)/t
        count += 1
    for t in [Fraction(1, 4), Fraction(1), Fraction(3, 2), Fraction(3)]:
        a = Fraction(-1)
        val = (abs(1+t*a)-1)/t-a
        assert val == (Fraction(0) if t <= 1 else 2-Fraction(2)/t)
        count += 1
    return count


def check_numeric():
    rng = np.random.default_rng(20261013)
    sizes = [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3), (4, 4)]
    ts = [0.01, 0.25, 0.5, 1.0, 1.75, 2.0, 2.2, 3.0, 5.0]
    count = 0
    for m, n in sizes:
        for t in ts:
            for _ in range(64):
                A = rng.normal(size=(m, n))
                A /= nuclear(A)
                got = remainder(A, t)
                assert got <= target(t, max(m,n)>1)+1e-9, (m,n,t,got)
                assert got >= -1e-9, (m,n,t,got)
                count += 1
    # Check two formula-attaining rectangular rank-one families.
    for m, n in [(1,2),(2,1),(2,2),(3,4)]:
        for t in [0.25,0.5,1.0,1.6,2.0,2.5,4.0]:
            P = np.zeros((m,n)); P[0,0] = 1.0
            if t <= 2:
                A = np.zeros((m,n)); A[0,0] = -t/2
                if n > 1: A[0,1] = (1-t*t/4)**0.5
                else: A[1,0] = (1-t*t/4)**0.5
            else:
                A = -P
            assert abs(nuclear(A)-1)<1e-10
            assert abs(remainder(A,t)-target(t))<1e-10,(m,n,t,remainder(A,t))
            count += 1
    return count


if __name__ == '__main__':
    exact=exact_witnesses()
    numerical=check_numeric()
    print(f'PASS: {exact} rational identities; {numerical} matrix tests')
