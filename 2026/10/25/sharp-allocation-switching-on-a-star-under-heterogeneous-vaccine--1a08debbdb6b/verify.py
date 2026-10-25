#!/usr/bin/env python3
"""Independent full-matrix checks for a star mobility allocation theorem.
Run with Python 3 standard library: python3 verify.py
The universal theorem is proved analytically in RESULT.md; finite tests are corroborative.
"""
import math
import random
from fractions import Fraction as F

COUNT = 0

def check(flag, explanation):
    global COUNT
    COUNT += 1
    if not flag:
        raise AssertionError(explanation)


def predicted(m, k, mu, B):
    D = (math.sqrt(k) - 1) * (m + 1 / math.sqrt(k))
    x0 = (B + m * mu * D) / (k * m + 1)
    x = min(B, max(0., x0))
    leaves = (B - x) / m
    return x, leaves


def formula(m, k, mu, B, x):
    y = (B - x) / m
    A = -y - mu
    C = -k * x - m * mu
    return (A + C + math.sqrt((A - C) ** 2 + 4 * m * mu ** 2)) / 2


def star_matrix(m, k, mu, allocations):
    n = m + 1
    mat = [[0.0] * n for _ in range(n)]
    mat[0][0] = -k * allocations[0] - m * mu
    for i in range(1, n):
        mat[i][i] = -allocations[i] - mu
        mat[0][i] = mat[i][0] = mu
    return mat


def jacobi_max(matrix):
    """Full matrix symmetric Jacobi eigensolver, independent of 2x2 reduction."""
    a = [row[:] for row in matrix]
    n = len(a)
    for iteration in range(200 * n * n):
        p, q = 0, 1
        ab = abs(a[p][q])
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > ab:
                    ab, p, q = abs(a[i][j]), i, j
        if ab < 3e-15:
            break
        theta = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        cs, sn = math.cos(theta), math.sin(theta)
        # A' = R^T A R with R columns (c,-s), (s,c), using the matching sign convention.
        app, aqq, apq = a[p][p], a[q][q], a[p][q]
        a[p][p] = cs * cs * app - 2 * cs * sn * apq + sn * sn * aqq
        a[q][q] = sn * sn * app + 2 * cs * sn * apq + cs * cs * aqq
        a[p][q] = a[q][p] = 0.0
        for t in range(n):
            if t == p or t == q:
                continue
            apt, aqt = a[p][t], a[q][t]
            a[p][t] = a[t][p] = cs * apt - sn * aqt
            a[q][t] = a[t][q] = sn * apt + cs * aqt
    else:
        raise AssertionError('symmetric Jacobi solver did not converge')
    return max(a[i][i] for i in range(n))


def exact_examples():
    m, k, mu, B = 3, F(4), F(1, 5), F(1, 5)
    D = F(7, 2)
    x = (B + m * mu * D) / (k * m + 1)
    y = (B - x) / m
    check((x, y) == (F(23, 130), F(1, 130)), 'exact center / leaves allocation')
    Delta = -y + k * x + (m - 1) * mu
    rad = Delta ** 2 + 4 * m * mu ** 2
    sqrt_rad = mu * (k * m + 1) / 2  # sqrt(k) = 2
    check(rad == sqrt_rad ** 2, 'rational eigenvalue discriminant')
    A, C = -y - mu, -k * x - m * mu
    eig = (A + C + sqrt_rad) / 2
    check(eig == -F(7, 65), 'exact minimized eigenvalue')
    check(F(1, 5) > mu * D / k, 'interior regime')
    m, k, mu, B = 2, F(1, 4), F(1, 10), F(1, 2)
    D = F(-2)
    x = (B + m * mu * D) / (k * m + 1)
    y = (B - x) / m
    check((x, y) == (F(1, 15), F(13, 60)), 'leaf-superior efficiency interior allocation')
    check(-(k * B + mu * m * F(1, 4)) / (k * m + 1) == -F(7, 60), 'exact eigenvalue leaf-superior')


def randomized_checks():
    rng = random.Random(240617)
    for m in range(2, 10):
        for k in [0.16, 0.25, 0.49, 0.8, 1.0, 1.3, 2.25, 4, 9]:
            for mu in [0.005, 0.025, 0.1, 0.3]:
                B = rng.uniform(0.02, 0.9) / max(1, k)
                x, y = predicted(m, k, mu, B)
                check(-1e-13 <= x <= B + 1e-13 and y >= -1e-13, 'feasible')
                opt = formula(m, k, mu, B, x)
                full = jacobi_max(star_matrix(m, k, mu, [x] + [y] * m))
                check(abs(full - opt) < 2e-11, 'full matrix formula')
                if 0 < x < B:
                    val = -(k * B + mu * m * (math.sqrt(k) - 1) ** 2) / (k * m + 1)
                    check(abs(val - opt) < 2e-11, 'interior optimum eigenvalue')
                for ix in range(61):
                    X = B * ix / 60
                    check(formula(m, k, mu, B, X) >= opt - 1e-12, 'global symmetric minimizer')
                for sample in range(7):
                    weights = [-math.log(max(1e-10, rng.random())) for i in range(m + 1)]
                    S = sum(weights)
                    v = [B * w / S for w in weights]
                    raw = jacobi_max(star_matrix(m, k, mu, v))
                    check(raw >= opt - 2e-11, 'asymmetric budget candidate')
                    if sample == 0:
                        sym = [v[0]] + [sum(v[1:])/m] * m
                        check(jacobi_max(star_matrix(m, k, mu, sym)) <= raw + 2e-11, 'leaf symmetrization')
    for k in [0.25, 0.49, 1.0, 4.0, 9.0]:
        for m in [2, 3, 5, 8]:
            for B in [0.01, 0.05, 0.2, 0.5]:
                mu=0.025
                D=(math.sqrt(k)-1)*(m+1/math.sqrt(k))
                x,y=predicted(m,k,mu,B)
                if k > 1:
                    check(abs(x-B)<1e-12 if B <= mu*D/k+1e-12 else x<B, 'center threshold')
                elif k < 1:
                    check(abs(x)<1e-12 if B <= -m*mu*D+1e-12 else x>0, 'leaf threshold')
                else:
                    check(abs(x-B/(m+1))<1e-12, 'uniform limit')

if __name__ == '__main__':
    exact_examples()
    randomized_checks()
    print(f'VERIFY_OK {COUNT} assertions; full-matrix Jacobi comparisons and exact-rational examples')
