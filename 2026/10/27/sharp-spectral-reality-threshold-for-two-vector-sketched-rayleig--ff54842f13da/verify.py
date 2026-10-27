"""Reproduce exact witness and stress-test the two sharp perturbation lemmas.
Universal quantified claims are established in RESULT.md, not by this finite checker.
Python 3 standard library only.
"""
from fractions import Fraction as F
from math import sqrt, isclose
from random import Random


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))]
            for i in range(len(A))]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def norm2_real_2x2(E):
    p, q = E[0]
    r, s = E[1]
    alpha, u, v, w = (p + s) / 2, (p - s) / 2, (q + r) / 2, (q - r) / 2
    return sqrt(alpha * alpha + w * w) + sqrt(u * u + v * v)


def imag_part_2x2(B):
    d = (B[0][0] - B[1][1]) ** 2 + 4 * B[0][1] * B[1][0]
    return sqrt(-d) / 2 if d < 0 else 0.0


# Exact rational four-dimensional positive-definite witness.
epsilon = F(3, 5)
a, b, c, d = F(2), F(3), F(1), F(2)
s, t, u = F(16, 25), F(12, 25), F(34, 25)
G = [[s, 0, 0, -t], [0, s, t, 0],
     [0, t, u, 0], [-t, 0, 0, u]]
A = [[a, 0, c, 0], [0, b, 0, c],
     [c, 0, d, 0], [0, c, 0, d]]
assert d > c * c / a and d > c * c / b  # Schur complement of diag(a,b).
M = sub(G, eye(4))
assert mul(M, M) == [[epsilon * epsilon * F(int(i == j)) for j in range(4)] for i in range(4)]
B = [[a, -c * t / s], [c * t / s, b]]
assert B == [[F(2), F(-3, 4)], [F(3, 4), F(3)]]
trace = B[0][0] + B[1][1]
det = B[0][0] * B[1][1] - B[0][1] * B[1][0]
assert trace == F(5) and det == F(105, 16)
assert trace * trace - 4 * det == F(-5, 4)
assert isclose(imag_part_2x2(B), sqrt(5) / 4, rel_tol=1e-13)

# The exact transition at epsilon=1/sqrt(5), and equal complex-radius envelope.
h, r = F(1, 2), F(1)
assert h * h / (h * h + r * r) == F(1, 5)
q = float(epsilon) / sqrt(1 - float(epsilon * epsilon))
assert isclose(q, 0.75, rel_tol=1e-14)
assert isclose(imag_part_2x2(B), sqrt((r * q) ** 2 - h * h), rel_tol=1e-13)

rng = Random(34019)
checks = 0
for _ in range(15000):
    h = 0.02 + 3 * rng.random()
    delta = 0.01 + 4 * rng.random()
    E = [[2*rng.random()-1, 2*rng.random()-1],
         [2*rng.random()-1, 2*rng.random()-1]]
    nrm = norm2_real_2x2(E)
    E = [[delta * z / nrm for z in row] for row in E]
    B = [[-h + E[0][0], E[0][1]], [E[1][0], h + E[1][1]]]
    observed = imag_part_2x2(B)
    max_imum = sqrt(max(0.0, delta * delta - h * h))
    assert observed <= max_imum + 1e-10, (h, delta, E, observed, max_imum)
    checks += 1

# Maximize the 2D metric block ratio under ||G-I|| <= epsilon.
for _ in range(5000):
    eps = .001 + .998 * rng.random()
    theta = 2 * 3.141592653589793 * rng.random()
    a11 = 1 + eps * __import__('math').cos(theta)
    off = eps * __import__('math').sin(theta)
    observed = abs(off / a11)
    bound = eps / sqrt(1 - eps * eps)
    assert observed <= bound + 1e-10
    checks += 1

print('VERIFICATION_OK; exact rational witness; 20,000 numeric lemma checks; nonreal threshold and sharp envelope')
