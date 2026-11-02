#!/usr/bin/env python3
"""Recompute the Hopf criticality for a two-strategy logit/resource-feedback ODE.

Uses only the Python standard library.  The general symbolic proof is in RESULT.md;
these checks independently contract the quadratic/cubic Taylor tensors using
complex eigenvectors and test exact parameter formulas numerically.
"""
import math
import random


def solve(parameters):
    theta, R, s0, T, P, epsilon = parameters
    assert 0 < theta < 1 and R > s0 > 0 and T > 0 and P > 0 and epsilon > 0
    a = P - R - s0 - T
    b = R + s0
    c = s0 - P
    D = R + T + theta * (P - s0)
    p = 1 / (1 + theta)
    q = p * (1 - p)
    h = 1 - 2 * p
    k = 1 - 6 * p + 6 * p * p
    beta = (D * (1 + theta) / theta + a * math.log(1 / theta)) / (R * P + s0 * T)
    n = (R - theta * s0 - (1 + theta) * math.log(1 / theta) / beta) / D
    assert 0 < n < 1 and beta > 0
    B = a * p + c
    m = epsilon * (1 + theta) * n * (1 - n)
    j12 = beta * q * B
    assert j12 < 0 and m > 0
    omega = math.sqrt(-j12 * m)
    assert math.isclose(beta * q * (a * n + b), 1, rel_tol=1e-12, abs_tol=1e-12)
    Fxx = h / q
    Fxn = beta * (h * B + q * a)
    Fnn = q * h * (beta * B) ** 2
    Fxxx = k / q ** 2
    Fxxn = k * beta * B / q + 2 * h * beta * a
    Fxnn = beta ** 2 * (k * B ** 2 + 2 * q * h * B * a)
    Fnnn = q * k * (beta * B) ** 3
    Gxn = epsilon * (1 + theta) * (1 - 2 * n)
    Gxnn = -2 * epsilon * (1 + theta)

    # Independent real planar Hopf-coefficient formula in canonical coordinates.
    alpha_inv = m / omega
    direct = (
        Fxxx + alpha_inv**2 * Fxnn
        + alpha_inv * Fxn * (Fxx + alpha_inv**2 * Fnn) / omega
    ) / 16

    # Exact algebraic closed form stated in the theorem (different computation).
    M = (1 - 3 * theta) * (P - s0) - (3 - theta) * (R + T)
    reduced = (
        -(1 + theta) * (R + T + P - s0) / (q * D)
        + epsilon * beta * n * (1 - n) * M
    ) / 16
    assert math.isclose(direct, reduced, rel_tol=1e-10, abs_tol=1e-10)

    # Independent Kuznetsov multilinear expression, using normalized complex
    # eigenvectors and the inverse of 2 i omega I - J.
    vec = (1.0 + 0j, 1j * omega / j12)
    adj = (0.5 + 0j, -0.5j * omega / m)
    def ip(u, v):
        return u[0].conjugate() * v[0] + u[1].conjugate() * v[1]
    assert abs(ip(adj, vec) - 1) < 1e-10
    def tensor2(u, v):
        mix = u[0]*v[1] + u[1]*v[0]
        return (Fxx*u[0]*v[0] + Fxn*mix + Fnn*u[1]*v[1], Gxn*mix)
    def tensor3(u, v, w):
        xxy = u[0]*v[0]*w[1] + u[0]*v[1]*w[0] + u[1]*v[0]*w[0]
        xyy = u[0]*v[1]*w[1] + u[1]*v[0]*w[1] + u[1]*v[1]*w[0]
        return (Fxxx*u[0]*v[0]*w[0] + Fxxn*xxy + Fxnn*xyy + Fnnn*u[1]*v[1]*w[1], Gxnn*xyy)
    conj = tuple(z.conjugate() for z in vec)
    u = tensor2(vec, conj)
    inv_u = (u[1] / m, u[0] / j12)
    v = tensor2(vec, vec)
    inv_v = ((2j*omega*v[0] + j12*v[1]) / (-3*omega**2),
             (m*v[0] + 2j*omega*v[1]) / (-3*omega**2))
    c3 = tensor3(vec, vec, conj)
    b1 = tensor2(vec, inv_u)
    b2 = tensor2(conj, inv_v)
    g21 = ip(adj, tuple(c3[j] - 2*b1[j] + b2[j] for j in (0, 1)))
    # With eigenvector first coordinate 1, Re(g21)=8*canonical coefficient.
    assert math.isclose(g21.real / 8, direct, rel_tol=1e-9, abs_tol=1e-9)
    return beta, n, M, reduced


def main():
    representative = [
        ('paper parameters', (0.8, 1.5, 0.5, 0.5, 0.25, 0.5)),
        ('switch slow resource', (0.1, 2, 0.5, 0.5, 50, 1)),
        ('switch fast resource', (0.1, 2, 0.5, 0.5, 50, 30)),
    ]
    for label, row in representative:
        beta, n, M, coefficient = solve(row)
        print('%s: beta_h=%.12f, n_h=%.12f, M=%.8f, L1=%.12f' %
              (label, beta, n, M, coefficient))
    assert solve(representative[0][1])[-1] < 0
    assert solve(representative[1][1])[-1] < 0
    assert solve(representative[2][1])[-1] > 0
    theta, R, s0, T, P, _ = representative[2][1]
    beta, n, M, _ = solve((theta, R, s0, T, P, 1))
    q = theta / (1 + theta) ** 2
    D = R + T + theta * (P - s0)
    epscrit = ((1 + theta) * (R + T + P - s0) /
               (q * D * beta * n * (1 - n) * M))
    assert 23.607 < epscrit < 23.608
    print('epsilon_c = %.12f' % epscrit)
    random.seed(20261026)
    for _ in range(100):
        theta = random.uniform(0.03, 0.97)
        s0 = random.uniform(0.03, 3)
        R = s0 + random.uniform(0.03, 5)
        T = random.uniform(0.03, 5)
        P = math.exp(random.uniform(-2, 5))
        epsilon = math.exp(random.uniform(-3, 4))
        solve((theta, R, s0, T, P, epsilon))
    print('PASS: 3 stated cases, 100 fixed-seed tests, two independent cubic-form contractions')


if __name__ == '__main__':
    main()
