#!/usr/bin/env python3
"""Independent finite-dimensional diagnostic for a rank-one Schatten stability theorem.
The analytic proof, not this finite test, establishes the continuum statement.
"""
import cmath
import math
import random

rng = random.Random(261013271)


def moment_gram(M, p):
    # Squared singular values of a 2-by-2 matrix: trace and determinant.
    t = sum(abs(M[i][j]) ** 2 for i in range(2) for j in range(2))
    det = M[0][0] * M[1][1] - M[0][1] * M[1][0]
    discr = max(0.0, t * t - 4.0 * abs(det) ** 2)
    z1 = max(0.0, (t + math.sqrt(discr)) / 2)
    z2 = max(0.0, (t - math.sqrt(discr)) / 2)
    return z1 ** (p / 2) + z2 ** (p / 2)


def vec(c, phase):
    return [c * cmath.exp(1j * phase), math.sqrt(max(0.0, 1 - c * c))]


def outer(x, y, amp):
    return [[amp * x[i] * y[j].conjugate() for j in range(2)] for i in range(2)]


def eval_pair(p, a, b, c, d, phase1, phase2):
    u = [1 + 0j, 0j]
    v = [1 + 0j, 0j]
    x = vec(c, phase1)
    y = vec(d, phase2)
    A = outer(u, v, a)
    B = outer(x, y, b)
    out = []
    for sign in (-1, 1):
        C = [[A[i][j] + sign * B[i][j] for j in range(2)] for i in range(2)]
        out.append(moment_gram(C, p))
    return max(out)


def F(p, a, b, Q):
    root = math.sqrt(max(0.0, (a - b) ** 2 + 2 * a * b * Q))
    return ((a + b + root) / 2) ** p + (max(0.0, a + b - root) / 2) ** p


def K(p, a, b):
    if a == b:
        return p * (1 - p) * a ** p / 2
    return (p * a * b / 2) * (a ** (p - 1) - b ** (p - 1)) / (b - a)


count = 0
for p in (0.12, 0.35, 0.66, 0.94):
    for a, b in ((1.0, 1.0), (0.4, 2.3), (2.0, 1.0)):
        k = K(p, a, b)
        for _ in range(120):
            c = 0.025 + 0.95 * rng.random()
            d = 0.025 + 0.95 * rng.random()
            phase1 = (2 * rng.random() - 1) * math.pi
            phase2 = (2 * rng.random() - 1) * math.pi
            Q = c * c + d * d
            obs = eval_pair(p, a, b, c, d, phase1, phase2)
            env = F(p, a, b, Q)
            assert obs <= env + 2e-7, (p, a, b, Q, obs, env)
            assert a ** p + b ** p - obs >= k * Q - 2e-7
            count += 1
        for Q in (0.025, 0.18, 0.66, 1.27, 1.89):
            # Aligned positive rank-one projections realize exact equality.
            c = math.sqrt(Q / 2)
            obs = eval_pair(p, a, b, c, c, 0.0, 0.0)
            assert abs(obs - F(p, a, b, Q)) < 1e-8
            count += 1
        Q = 0.0001
        c = math.sqrt(Q / 2)
        obs = eval_pair(p, a, b, c, c, 0, 0)
        secant = (a ** p + b ** p - obs) / Q
        assert abs(secant - k) <= 0.0005 * max(k, 0.05)
        count += 1
print('PASS: checked', count, 'complex rank-one configurations and sharpness/slope diagnostics')
