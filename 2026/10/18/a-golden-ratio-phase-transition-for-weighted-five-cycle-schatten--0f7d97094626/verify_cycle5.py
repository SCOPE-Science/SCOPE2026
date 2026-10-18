"""Finite diagnostics for the weighted five-cycle Schatten-fourth identity.

Uses Python's standard library. Finite tests are not a proof of global
optimality, which is established analytically in the accompanying result.
"""
import cmath
import math
import random

N = 5
R = random.Random(521736)
GAMMA = math.sqrt(5.0) - 1.0


def mm(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(N)) for j in range(N)] for i in range(N)]


def adj(A):
    return [[A[j][i].conjugate() for j in range(N)] for i in range(N)]


def schatten_fourth(W, t, theta):
    Z = [[t * cmath.exp(1j * theta) * W[i][j] + (1 - t) * cmath.exp(-1j * theta) * W[j][i].conjugate() for j in range(N)] for i in range(N)]
    H = mm(adj(Z), Z)
    return sum(mm(H, H)[i][i] for i in range(N)).real


def F(x, q):
    return sum(xj * xj for xj in x) + q * sum(x[j] * x[(j+1) % N] for j in range(N))


def optimum(q):
    if q <= GAMMA:
        return (1.0 + q) / 5.0
    return (2.0 + q) / (6.0 + q)


def star(q):
    b = 2.0 / (6.0 + q)
    a = (2.0 + q) / (6.0 + q)
    return [a, 0.0, b, b, 0.0]


checks = 0
for _ in range(110):
    amplitudes = [R.random() + 0.08 for j in range(N)]
    phases = [2.0 * math.pi * R.random() for j in range(N)]
    weights = [r * cmath.exp(1j * phi) for r, phi in zip(amplitudes, phases)]
    W = [[0j for j in range(N)] for i in range(N)]
    for j, w in enumerate(weights):
        W[(j+1) % N][j] = w
    x = [abs(w) ** 2 for w in weights]
    t = R.random()
    A = t**4 + (1.0-t)**4
    B = 4.0 * t*t*(1.0-t)**2
    predicted = A * F(x, B / A)
    for theta in (0.0, 0.283, 1.17, 2.783):
        direct = schatten_fourth(W, t, theta)
        assert abs(direct - predicted) <= 2e-11 * (1 + predicted), (direct, predicted)
        checks += 1

for q in (0.0, 0.1, 0.4, 0.9, 1.0, 1.2, GAMMA, 1.3, 1.6, 1.95, 2.0):
    minimizer = [0.2] * N if q <= GAMMA else star(q)
    assert abs(F(minimizer, q) - optimum(q)) < 2e-14
    checks += 1
    for _ in range(600):
        xx = [R.expovariate(1) for j in range(N)]
        total = sum(xx)
        xx = [v / total for v in xx]
        assert F(xx, q) >= optimum(q) - 2e-11
        checks += 1

for r in (0.0, 0.08, 0.15, 0.2):
    x = [0.2 + r * math.cos(4 * math.pi * j / 5) for j in range(N)]
    if min(x) >= 0:
        assert abs(F(x, GAMMA) - optimum(GAMMA)) < 1e-13
        checks += 1
for b in (0.0, 0.1, 0.3, 0.5):
    x = [0.5, 0.0, b, 0.5-b, 0.0]
    assert abs(F(x, 2.0)-0.5) < 1e-13
    checks += 1

print('PASS:', checks, 'finite diagnostics')
