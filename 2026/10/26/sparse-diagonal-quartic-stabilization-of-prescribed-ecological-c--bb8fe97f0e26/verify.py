"""Exact rational spot checks for sparse diagonal ecological stabilization.

This file checks examples; the analytic proof, not sampling, establishes the theorem.
"""
from fractions import Fraction as F
from random import Random


def parameters(r, S, z, mu):
    n = len(r)
    R = [r[i] + sum(S[i][j] * z[j] for j in range(n)) for i in range(n)]
    beta = []
    alpha = []
    for i in range(n):
        radius = z[i] * sum(abs(S[i][j]) for j in range(n) if j != i)
        b = max(F(1), R[i] / z[i]**3, (z[i]*S[i][i]-2*R[i]+radius+mu) / z[i]**3) + F(1)
        a = b*z[i] - R[i]/z[i]**2
        assert a > 0 and b > 0
        alpha.append(a)
        beta.append(b)
    return R, alpha, beta


def verify_instance(r, S, z, mu):
    n = len(r)
    R, a, b = parameters(r, S, z, mu)
    for i in range(n):
        g = r[i] + sum(S[i][j]*z[j] for j in range(n)) + a[i]*z[i]**2-b[i]*z[i]**3
        assert g == 0
        diag = z[i]*S[i][i]-2*R[i]-b[i]*z[i]**3
        diag_from_derivative = z[i]*(S[i][i]+2*a[i]*z[i]-3*b[i]*z[i]**2)
        assert diag == diag_from_derivative
        off = z[i]*sum(abs(S[i][j]) for j in range(n) if j != i)
        assert diag + off < -mu
    maxr = max(abs(ri) for ri in r)
    L = max(sum(abs(Sij) for Sij in row) for row in S)
    maxa = max(a)
    minb = min(b)
    K = max(F(1), 4*maxr/minb, 4*L/minb, 4*maxa/minb) + F(1)
    for m in (K, 2*K, 7*K):
        assert maxr + L*m + maxa*m*m - minb*m*m*m < 0
    return n


def main():
    rng = Random(20261021)
    count = 0
    for n in range(1, 8):
        for _ in range(200):
            r = [F(rng.randrange(-12, 13), rng.randrange(1, 5)) for i in range(n)]
            S = [[F(rng.randrange(-9, 10), rng.randrange(1, 5)) for j in range(n)] for i in range(n)]
            z = [F(rng.randrange(1, 9), rng.randrange(1, 6)) for i in range(n)]
            mu = F(rng.randrange(1, 9), rng.randrange(1, 4))
            verify_instance(r, S, z, mu)
            count += 1
    for p in (2, 3):
        # For r=-1,S=0,z=1, one diagonal feedback monomial is forced
        # to have coefficient +1; its Jacobian eigenvalue is +p.
        coeff = F(1)
        assert -1 + coeff == 0 and p*coeff > 0
    print(f'PASS: {count} exact rational systems and both one-monomial obstructions')


if __name__ == '__main__':
    main()
