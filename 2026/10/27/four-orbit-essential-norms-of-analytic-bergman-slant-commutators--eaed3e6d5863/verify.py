"""Supplementary checks for analytic slant Bergman commutators.
Run: python verify.py (NumPy required). The proof of infinite-dimensional claims is analytic.
"""
import cmath
import math
import random
import numpy as np


def multiplication_b(f, n, dimension):
    """Column n of B_f in the normalized Bergman monomial basis."""
    c = np.zeros(dimension, complex)
    for j, v in enumerate(f):
        if not v or (n + j) % 2:
            continue
        m = (n + j) // 2
        if m < dimension:
            c[m] += v * math.sqrt((n + 1) / (m + 1))
    return c


def B_matrix(f, dimension):
    return np.stack([multiplication_b(f, n, dimension) for n in range(dimension)], axis=1)


def conv(a, b):
    return np.convolve(a, b)


def P_coefficients(f, g):
    f2 = np.zeros(2 * len(f) - 1, complex)
    g2 = np.zeros(2 * len(g) - 1, complex)
    f2[::2] = f
    g2[::2] = g
    x = conv(g, f2)
    y = conv(f, g2)
    n = max(len(x), len(y))
    out = np.zeros(n, complex)
    out[:len(x)] += x
    out[:len(y)] -= y
    return out


def predicted_column(f, g, n, dimension):
    p = P_coefficients(f, g)
    x = np.zeros(dimension, complex)
    for t, v in enumerate(p):
        if (n + t) % 4:
            continue
        m = (n + t) // 4
        if m < dimension:
            x[m] += v * math.sqrt((n + 1) / (m + 1))
    return x


def phase_symbol(p, z):
    return np.array([sum(p[t] * z ** ((t + r) // 4) for t in range(len(p)) if (t + r) % 4 == 0)
                     for r in range(4)], complex)


def run():
    random.seed(3771)
    checked = 0
    for trial in range(80):
        flen = random.randint(1, 6)
        glen = random.randint(1, 6)
        f = np.array([complex(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(flen)])
        g = np.array([complex(random.randint(-3, 3), random.randint(-3, 3)) for _ in range(glen)])
        dim = 90
        bf = B_matrix(f, dim)
        bg = B_matrix(g, dim)
        comm = bf @ bg - bg @ bf
        for n in range(60):
            expected = predicted_column(f, g, n, dim)
            assert np.max(np.abs(comm[:,n] - expected)) < 1e-11, (trial, n)
            checked += 1
        p = P_coefficients(f, g)
        for n in (50, 60):
            v = np.zeros(dim, complex)
            for t, c in enumerate(p):
                if (n + t) % 4 == 0:
                    m = (n + t) // 4
                    v[m] += 2 * c * math.sqrt((n + 1) / (n + t + 4))
            assert np.max(np.abs(v - comm[:, n])) < 1e-11
            checked += 1
        for theta in (0.0, math.pi / 7, math.pi / 3):
            z = cmath.exp(1j * theta)
            q = phase_symbol(p, z)
            assert abs(sum(abs(v)**2 for v in q) - np.vdot(q,q).real) < 1e-9
            eta = cmath.exp(1j * theta / 4)
            four = sum(abs(np.polynomial.polynomial.polyval((1j)**k * eta,p))**2 for k in range(4))
            assert abs(4 * np.vdot(q,q).real - four) < 1e-7
            checked += 2
    for a, b in ((0, 1), (1, 3), (1, 5), (2, 6)):
        f = np.zeros(a+1);f[a]=1
        g = np.zeros(b+1);g[b]=1
        p = P_coefficients(f,g)
        largest = max(np.linalg.norm(phase_symbol(p, cmath.exp(2j * math.pi * k / 400))) for k in range(400))
        expected = 4 if ((a-b) % 4 == 0) else 2 * math.sqrt(2)
        assert abs(2 * largest - expected) < 1e-10
        checked += 1
    print(f'PASS: {checked} supplementary exact-entry and polyphase checks')

if __name__ == '__main__':
    run()
