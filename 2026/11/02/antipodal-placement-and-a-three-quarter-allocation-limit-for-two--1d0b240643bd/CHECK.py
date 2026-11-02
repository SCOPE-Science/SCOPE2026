#!/usr/bin/env python3
"""Reproduce the two-absorber cycle mean-time and optimal-allocation identities.

Python standard library only. This is a finite diagnostic checker; the proof of
all-parameter optimality is in RESULT.md.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def exact_linear_solve(M, b):
    n = len(b)
    A = [[F(z) for z in row] + [F(b[i])] for i, row in enumerate(M)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if A[i][j])
        A[j], A[pivot] = A[pivot], A[j]
        d = A[j][j]
        A[j] = [v / d for v in A[j]]
        for i in range(n):
            if i != j:
                t = A[i][j]
                if t:
                    A[i] = [v - t * w for v, w in zip(A[i], A[j])]
    return [row[-1] for row in A]


def exact_mean_from_generator(n, m, D, local, remote):
    M = [[F(0) for _ in range(n)] for __ in range(n)]
    for i in range(n):
        M[i][i] += 2 * D
        M[i][(i - 1) % n] -= D
        M[i][(i + 1) % n] -= D
    M[0][0] += local
    M[m][m] += remote
    return exact_linear_solve(M, [F(1) for _ in range(n)])[0]


def closed_mean(n, m, D, local, remote):
    C = D * n / F(m * (n - m))
    K = local + remote
    return F(n, 2) * (remote + 2*C) / (local*remote + C*K)


def optimum(n, D, K):
    z = (n*n)//4  # floor(n^2/4), maximizing m(n-m)
    C = float(D) * n / z
    s = sqrt(4.0 + float(K)/C)
    remote = float(K)/(2+s)
    return z, remote, n/float(K)*(0.5 + 1/s)


def run():
    n_cases = 0
    for n in range(3, 15):
        for m in range(1, n):
            for D, local, remote in [
                (F(1), F(2), F(1)),
                (F(2,3), F(3,5), F(1,2)),
                (F(5,4), F(1,7), F(9,11)),
            ]:
                direct = exact_mean_from_generator(n,m,D,local,remote)
                expression = closed_mean(n,m,D,local,remote)
                assert direct == expression, (n,m,D,local,remote,direct,expression)
                n_cases += 1
    rng = Random(17683)
    opt_cases = 0
    for n in range(3, 30):
        for rep in range(25):
            D = 10 ** rng.uniform(-2, 2)
            K = 10 ** rng.uniform(-2, 2)
            z, y, T = optimum(n,D,K)
            assert 0.0 < y < K/4
            m = n//2
            assert m*(n-m) == z
            C = D*n/z
            expression = n/2*(y+2*C)/((K-y)*y+C*K)
            assert isclose(T,expression,rel_tol=3e-13)
            assert T < n/K
            # Compare rates and locations independently against random alternatives.
            for _ in range(10):
                m2 = rng.randrange(1,n)
                y2 = K*rng.random()
                C2 = D*n/(m2*(n-m2))
                alt = n/2*(y2+2*C2)/((K-y2)*y2+C2*K)
                assert alt + 1e-10 * max(1.0,T) >= T, (n,D,K,m2,y2,alt,T)
                opt_cases += 1
    for n in [3,6,11,22]:
        D=F(2,3)
        K=F(7,5)
        for m in range(1,n):
            assert closed_mean(n,m,D,K,F(0)) == F(n)/K
            assert closed_mean(n,m,D,K/F(2),K/F(2)) == F(n)/K
    for n in [3,4,8,15]:
        D=1.0
        for K in [1e-8,1e-6,1e-4]:
            _, y, _=optimum(n,D,K)
            assert abs(y/K-.25) < .002
        for K in [1e6,1e8]:
            _, y, T=optimum(n,D,K)
            assert abs(T/(n/K)-.5) < .004
    print('PASS: %d exact rational generator comparisons, %d random global-optimality diagnostics, asymptotic and boundary tests' % (n_cases,opt_cases))


if __name__ == '__main__':
    run()
