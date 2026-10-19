"""Standalone finite tests of Fourier-alias formulas for one-sided Poisson sampling.
Requires Python 3, numpy. Not a substitute for the analytic proof.
"""
import math
import numpy as np


def fiber(q, t, phi):
    z = np.exp(1j * (phi + 2 * np.pi * np.arange(q)) / q)
    w = np.exp(t * (z - 1))
    return w[None, :] ** np.arange(q)[:, None]


def lower(q, t, phi):
    s = np.linalg.svd(fiber(q, t, phi), compute_uv=False)
    return (s[-1] ** 2) / q


def collision_phase(q, d):
    z = 1 - np.exp(2j * np.pi * d / q)
    theta = np.pi / 2 - np.angle(z)
    return (q * theta) % (2 * np.pi)


def main():
    tests = 0
    # Vandermonde product and exact analytic collision phases.
    for q in range(2, 9):
        for d in range(1, q // 2 + 1):
            for m in (1, 2):
                t = math.pi * m / math.sin(math.pi * d / q)
                phi = collision_phase(q, d)
                V = fiber(q, t, phi)
                assert np.linalg.svd(V, compute_uv=False)[-1] < 2e-9, (q, d, m)
                tests += 1
        for phi in np.linspace(0.1, 6.0, 6):
            t = 0.3 + 0.17 * q
            V = fiber(q, t, phi)
            w = V[1, :]
            product = np.prod([w[j] - w[i] for i in range(q)
                               for j in range(i + 1, q)])
            assert abs(np.linalg.det(V) - product) < 2e-9
            tests += 1

    # Exact fiber/decimation identity, evaluated on independent finite-cycle FFTs.
    rng = np.random.default_rng(20261015)
    for q in range(2, 8):
        N = 60 * q
        M = N // q
        f = rng.normal(size=N) + 1j * rng.normal(size=N)
        F = np.fft.fft(f)
        theta = 2 * np.pi * np.arange(N) / N
        a = np.exp(0.73 * (np.exp(-1j * theta) - 1))
        for k in range(q):
            direct = np.fft.ifft(F * a ** k)[::q]
            G = np.sum((F * a ** k).reshape(q, M), axis=0) / q
            by_alias = np.fft.ifft(G)
            assert np.max(np.abs(direct - by_alias)) < 3e-12
            tests += 1

    # Small-time sharp frame lower-bound coefficient for several q.
    for q in range(2, 6):
        t = 0.002
        target = t ** (2 * (q - 1)) / math.comb(2 * q - 2, q - 1)
        vals = [lower(q, t, phi) / target for phi in np.linspace(0, 2*np.pi, 21)]
        assert all(abs(v - 1) < 0.03 for v in vals), (q, min(vals), max(vals))
        tests += len(vals)

    # The two-channel sharp leading constants at every tested positive resonance.
    for m in (1, 2, 3):
        t0 = m * math.pi
        expected = 1 / (1 + math.exp(2 * t0))
        for eps in (0.012, -0.012, 0.004, -0.004):
            t = t0 + eps
            a = lower(2, t, math.pi) / eps**2
            assert abs(a / expected - 1) < 0.07, (m, eps, a/expected)
            tests += 1

    print(f'PASS: {tests} independent finite comparisons of collision times, '
          'Vandermonde determinants, alias FFTs, and sharp asymptotic coefficients.')


if __name__ == '__main__':
    main()
