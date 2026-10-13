#!/usr/bin/env python3
"""Finite checks for a one-vector coordinate-sketched Ritz interval.

The proof in RESULT.md supplies the universal quantifiers; these checks do not.
Uses only the Python standard library.
"""
from fractions import Fraction as F
from itertools import combinations
import math
import random


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), F(0))


def matmul(A, B):
    return [[sum((A[i][k]*B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def projector(z):
    den = dot(z, z)
    assert den > 0
    return [[a*b/den for b in z] for a in z]


def ritz(A, v, J):
    den = sum((v[i]*v[i] for i in J), F(0))
    return sum((v[i]*dot(A[i], v) for i in J), F(0))/den


def fixed_q(v, J):
    den = sum((v[i]*v[i] for i in J), F(0))
    u = [v[i]/den if i in J else F(0) for i in range(len(v))]
    return [[(u[i]*v[j]+v[i]*u[j])/2 for j in range(len(v))]
            for i in range(len(v))]


def trace_square(Q):
    return sum((Q[i][j]*Q[j][i]
                for i in range(len(Q)) for j in range(len(Q))), F(0))


def diagonal_spectrum_witness(n, s, mu, L, upper=False):
    # n and s are perfect squares. Uniform v and a top-s subset
    # admit rational normalized vectors, yielding exact matrices.
    rn = math.isqrt(n)
    rs = math.isqrt(s)
    assert rn*rn == n and rs*rs == s
    v = [F(1, rn) for _ in range(n)]
    w = [F(1, rs) if i < s else F(0) for i in range(n)]
    z = [w[i]+v[i] if upper else w[i]-v[i] for i in range(n)]
    P = projector(z)
    assert matmul(P, P) == P
    A = [[(mu if i == j else F(0))+(L-mu)*P[i][j]
          for j in range(n)] for i in range(n)]
    actual = ritz(A, v, set(range(s)))
    c = (mu+L)/2
    delta = (L-mu)/2
    target = c + (delta*F(rn, rs) if upper else -delta*F(rn, rs))
    assert actual == target, (n, s, mu, L, upper, actual, target)
    assert matmul(P, P) == P  # spectrum of A exactly {mu, L}
    return actual


def float_endpoint_checks():
    rng = random.Random(140381)
    count = 0
    for n in (2, 3, 4, 6, 11):
        for s in range(1, n):
            for t in range(70):
                x = [rng.uniform(-1, 1) for _ in range(n)]
                xnorm = math.sqrt(sum(z*z for z in x))
                v = [z/xnorm for z in x]
                J = sorted(range(n), key=lambda j: -abs(v[j]))[:s]
                a = math.sqrt(sum(v[j]*v[j] for j in J))
                u = [v[i]/a if i in J else 0.0 for i in range(n)]
                # Orthogonal eigenvectors of Q are normalized u +/- v.
                for sign in (-1, 1):
                    z = [u[i]+sign*v[i] for i in range(n)]
                    znorm = math.sqrt(sum(k*k for k in z))
                    z = [k/znorm for k in z]
                    mu, L = 0.7, 4.1
                    Av = [mu*v[i]+(L-mu)*z[i]*sum(z[k]*v[k] for k in range(n))
                          for i in range(n)]
                    quotient = sum(v[j]*Av[j] for j in J)/(a*a)
                    target = (mu+L)/2 + (L-mu)/2/a*(1 if sign == 1 else -1)
                    if not math.isclose(quotient, target, abs_tol=3e-12, rel_tol=3e-12):
                        raise AssertionError((n, s, sign, quotient, target))
                    count += 1
    return count


def main():
    rng = random.Random(38492)
    qcount = 0
    for n in range(2, 11):
        for s in range(1, n+1):
            J = set(range(s))
            for _ in range(25):
                v = [F(rng.randrange(-7, 8)) for _ in range(n)]
                if dot(v, v) == 0 or sum(v[j]*v[j] for j in J) == 0:
                    continue
                Q = fixed_q(v, J)
                den = sum((v[j]*v[j] for j in J), F(0))
                norm = dot(v, v)
                assert sum((Q[i][i] for i in range(n)), F(0)) == 1
                assert trace_square(Q) == (1+norm/den)/2
                qcount += 1
    exact = 0
    for nn in range(2, 6):
        for ss in range(1, nn):
            for mu, L in ((F(1), F(4)), (F(1, 3), F(9, 2)),
                          (F(2), F(8)), (F(19, 11), F(20, 11))):
                for upper in (False, True):
                    diagonal_spectrum_witness(nn*nn, ss*ss, mu, L, upper)
                    exact += 1
    count = float_endpoint_checks()
    # For the exact n=4, s=1 case the sharp threshold is kappa=3.
    assert diagonal_spectrum_witness(4, 1, F(1), F(3)) == 0
    assert diagonal_spectrum_witness(4, 1, F(1), F(4)) == -F(1, 2)
    # For any fixed kappa>1 the critical sampled fraction is positive.
    for kappa in (1.01, 2, 3, 17):
        gamma = ((kappa-1)/(kappa+1))**2
        assert 0 < gamma < 1
        for frac in (gamma/2, (gamma+1)/2):
            q = 1/math.sqrt(frac)
            low = ((kappa+1)-(kappa-1)*q)/2
            assert (low > 0) == (frac > gamma)
    print('VERIFY_OK rational_Q_identities=', qcount,
          'exact_rational_endpoint_witnesses=', exact,
          'nonflat_endpoint_checks=', count,
          'phase_boundary_checks=8')


if __name__ == '__main__':
    main()
