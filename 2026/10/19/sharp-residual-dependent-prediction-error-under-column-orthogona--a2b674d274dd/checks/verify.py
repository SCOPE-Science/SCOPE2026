"""Reproducibility checks for the sharp orthogonal-column perturbation envelope.

Runs with the Python standard library only: python3 checks/verify.py.
The accompanying proof establishes the infinite family; these are finite tests.
"""
import math
import random


def envelope(rho, delta):
    if rho < 0 or delta < 0:
        raise ValueError("nonnegative parameters required")
    cap = math.inf if rho == 0 else (1 + math.hypot(1, rho)) / rho
    s = min(cap, delta)
    return (s * s + rho * s) / (1 + s * s)


def solve_spd(a, b):
    n = len(b)
    z = [list(map(float, a[i])) + [float(b[i])] for i in range(n)]
    for j in range(n):
        k = max(range(j, n), key=lambda i: abs(z[i][j]))
        z[j], z[k] = z[k], z[j]
        assert abs(z[j][j]) > 1e-12
        q = z[j][j]
        for h in range(j, n + 1):
            z[j][h] /= q
        for i in range(n):
            if i != j:
                q = z[i][j]
                for h in range(j, n + 1):
                    z[i][h] -= q * z[j][h]
    return [z[i][-1] for i in range(n)]


def norm(z):
    return math.sqrt(sum(x * x for x in z))


def matvec(a, x):
    return [sum(y * z for y, z in zip(row, x)) for row in a]


def tested_error(f, u, r):
    k, n = len(f), len(u)
    gram = [[(1.0 if i == j else 0.0) + sum(f[h][i] * f[h][j] for h in range(k))
             for j in range(n)] for i in range(n)]
    rhs = [u[i] + sum(f[h][i] * r[h] for h in range(k)) for i in range(n)]
    v = solve_spd(gram, rhs)
    return norm([v[i] - u[i] for i in range(n)]) / norm(u)


rng = random.Random(90234)
exact_cases = 0
for rho in [0.0, 0.001, 0.1, 1.0, 3.0, 30.0]:
    for delta in [0.0, 0.01, 0.5, 1.0, 2.0, 4.0, 30.0, 100.0]:
        optimum = math.inf if rho == 0 else (1 + math.hypot(1, rho)) / rho
        s = min(delta, optimum)
        # A=(1,0)^T, b=(1,rho)^T, E=(0,-s)^T, fixed original Ax prediction.
        error = tested_error([[-s]], [1.0], [rho])
        expected = envelope(rho, delta)
        assert abs(error - expected) < 1e-10 * (1 + expected), (rho, delta, error, expected)
        exact_cases += 1

random_cases = 0
for n in [1, 2, 3, 5]:
    for rho in [0.0, 0.01, 0.1, 1.0, 10.0]:
        for delta in [0.01, 0.5, 1.0, 3.0, 10.0]:
            for rep in range(12):
                u = [rng.gauss(0, 1) for _ in range(n)]
                normu = norm(u)
                u = [x / normu for x in u]
                r = [rng.gauss(0, 1) for _ in range(3)]
                normr = norm(r)
                r = [rho * x / normr for x in r]
                f = [[rng.gauss(0, 1) for _ in range(n)] for _ in range(3)]
                fro = math.sqrt(sum(x * x for row in f for x in row))
                # The operator norm is at most Frobenius norm, so F is feasible.
                f = [[delta * x / fro for x in row] for row in f]
                actual = tested_error(f, u, r)
                expected = envelope(rho, delta)
                assert actual <= expected + 2e-10, (n, rho, delta, actual, expected)
                random_cases += 1
print('PASS: %d sharp rank-one cases; %d randomized feasible matrices' % (exact_cases, random_cases))
