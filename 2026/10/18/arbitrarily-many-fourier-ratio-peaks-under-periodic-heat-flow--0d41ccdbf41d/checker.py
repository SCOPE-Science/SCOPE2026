"""Deterministic numerical cross-checks for heat-flow Fourier-ratio constructions.

The proofs in RESULT.md are analytic; this program only checks finite cases.
"""
import math
from fractions import Fraction
import numpy as np

CHECKS = 0


def lse_ratio(logarithms):
    """Exact Fourier-coefficient formula evaluated after log rescaling."""
    x = np.asarray(logarithms, dtype=float)
    v = np.exp(x - np.max(x))
    return math.sqrt(2.0) * float(np.sum(v)) / math.sqrt(float(np.dot(v, v)))


def data(m, L, T=Fraction(1)):
    lam = [j * j * L * L for j in range(1, m + 1)]
    tau = {j: Fraction(m - j + 1, m) * T for j in range(2, m + 1)}
    loga = [Fraction(0)]
    for j in range(2, m + 1):
        loga.append(loga[-1] + (lam[j - 1] - lam[j - 2]) * tau[j])
    return lam, tau, loga


def spectrum(m, L, time, lam, loga):
    return [float(loga[j] - lam[j] * time) for j in range(m)]


def dft_ratio(m, L, logs):
    weights = np.exp(np.asarray(logs) - max(logs))
    N = 2 * m * L + 1
    theta = 2 * np.pi * np.arange(N) / N
    signal = 2 * np.sum([weights[j - 1] * np.cos(j * L * theta) for j in range(1, m + 1)], axis=0)
    coeff = np.fft.fft(signal) / N
    active = np.r_[[j * L for j in range(1, m + 1)], [N - j * L for j in range(1, m + 1)]]
    # Check that the spatial DFT recovers the independently built cosine-mode data.
    np.testing.assert_allclose(np.real(coeff[active]), np.r_[weights, weights], atol=5e-12, rtol=1e-10)
    residual = coeff.copy()
    residual[active] = 0
    assert max(abs(residual)) < 5e-12
    return float(sum(abs(coeff)) / math.sqrt(float(sum(abs(coeff) ** 2))))


def run():
    global CHECKS
    for m in range(2, 9):
        L = 12
        lam, tau, loga = data(m, L)
        eta = math.exp(-3 * L * L / (2 * m))
        assert eta <= 1 / (100 * m)
        CHECKS += 1
        for j in range(2, m + 1):
            # Rational identities before any floating-point evaluation.
            z0 = loga[j - 1] - lam[j - 1] * tau[j]
            z1 = loga[j - 2] - lam[j - 2] * tau[j]
            assert z0 == z1
            CHECKS += 1
            logs = spectrum(m, L, tau[j], lam, loga)
            value = lse_ratio(logs)
            assert value > 1.99
            dvalue = dft_ratio(m, L, logs)
            assert abs(value - dvalue) < 3e-10
            CHECKS += 2
        lows = [Fraction(0), Fraction(1)] + [(tau[j] + tau[j + 1]) / 2 for j in range(2, m)]
        for t in lows:
            logs = spectrum(m, L, t, lam, loga)
            value = lse_ratio(logs)
            assert value < 1.43
            dvalue = dft_ratio(m, L, logs)
            assert abs(value - dvalue) < 3e-10
            CHECKS += 2
        # Local ordering: each peak is strictly above its two neighboring valleys.
        peaks = [tau[j] for j in range(m, 1, -1)]
        valleys = [Fraction(0)] + [(tau[j + 1] + tau[j]) / 2 for j in range(m - 1, 1, -1)] + [Fraction(1)]
        assert len(valleys) == len(peaks) + 1
        for k, t in enumerate(peaks):
            hi = lse_ratio(spectrum(m, L, t, lam, loga))
            lo1 = lse_ratio(spectrum(m, L, valleys[k], lam, loga))
            lo2 = lse_ratio(spectrum(m, L, valleys[k + 1], lam, loga))
            assert hi > max(lo1, lo2)
            CHECKS += 1
    # Large-amplification construction: all m modes coincide at tau = 1/2.
    for m in (2, 5, 17, 50):
        L = 10
        lam = [j * j * L * L for j in range(1, m + 1)]
        loga = [Fraction(v, 2) for v in lam]
        at_half = lse_ratio(spectrum(m, L, Fraction(1, 2), lam, loga))
        initial = lse_ratio(spectrum(m, L, Fraction(0), lam, loga))
        assert abs(at_half - math.sqrt(2*m)) < 1e-10
        assert abs(initial - math.sqrt(2)) < 1e-10
        CHECKS += 2
    print(f'VERIFY_OK: {CHECKS} checks')


if __name__ == '__main__':
    run()
