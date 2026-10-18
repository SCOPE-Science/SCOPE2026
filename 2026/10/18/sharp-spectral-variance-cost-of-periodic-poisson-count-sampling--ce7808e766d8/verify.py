"""Independent numerical quadrature tests for a periodic Poisson window-count formula.

No external data or resources. Requires NumPy.
"""
import math
import numpy as np


def claimed(lambda_, amplitude, harmonic):
    return (4 * lambda_ ** 3 + (4 / 3) * lambda_ ** 2
            + lambda_ ** 2 * amplitude ** 2 / (math.pi ** 2 * harmonic ** 2))


def overlapping_mass_grid(amplitude, harmonic, n=1200):
    # Independent direct integration of the overlap intensity,
    # with period coordinates t and overlap length L.
    t = np.arange(n)[:, None] / n
    L = np.arange(n)[None, :] / n
    c = amplitude / (2 * math.pi * harmonic)
    A = L + c * (np.sin(2 * math.pi * harmonic * t)
                 - np.sin(2 * math.pi * harmonic * (t - L)))
    return float(np.mean(A * A))


def check():
    assertions = 0
    for lam in (0.25, 0.75, 1.5, 4.0):
        lower = 4 * lam ** 3 + (4 / 3) * lam ** 2
        upper = 4 * lam ** 3 + 2 * lam ** 2
        for amp, k in ((0., 1), (0.2, 1), (0.65, 2), (0.85, 5)):
            # Analytically independent check of the scalar Fourier term:
            # the only nonzero nonconstant coefficients are a/2 at +/-k.
            spectral = sum((amp / 2) ** 2 / (j * j)
                           for j in (k, -k))
            v = lower + (2 * lam ** 2 / math.pi ** 2) * spectral
            assert abs(v - claimed(lam, amp, k)) < 1e-12
            assertions += 1
            assert lower - 1e-12 <= v < upper
            assertions += 1
            I = overlapping_mass_grid(amp, k)
            # Left-endpoint quadrature has ~1/(2n) bias from L^2.
            expected = (1 / 3) + amp ** 2 / (4 * math.pi ** 2 * k ** 2)
            assert abs(I - expected) < 0.00043
            assertions += 1
        # The L^2 Fourier penalty of increasingly concentrated periodic
        # wrapped Gaussian profiles tends to the analytic supremum.
        x = np.arange(8192) / 8192
        for width in (0.10, 0.04, 0.015):
            dist = np.minimum(x, 1 - x)
            pulse = np.exp(-0.5 * (dist / width) ** 2) + 1e-4
            pulse /= pulse.mean()
            f = np.fft.fft(pulse) / pulse.size
            inds = np.fft.fftfreq(len(f), d=1 / len(f))
            k2 = inds[1:] ** 2
            spectral = np.sum(abs(f[1:]) ** 2 / k2).real
            v_pulse = lower + (2 * lam ** 2 / math.pi ** 2) * spectral
            assert lower < v_pulse < upper
            assertions += 1
        # An independently discretized periodic rate has mean exactly one;
        # every window of length one therefore has Poisson mean lam.
        grid = np.arange(8192) / 8192
        mean_rate = np.mean(1.0 + 0.85 * np.cos(6 * math.pi * grid))
        assert abs(mean_rate - 1.0) < 1e-12
        assertions += 1
    print(f"PASS: {assertions} deterministic assertions; not a substitute for the proof.")


if __name__ == '__main__':
    check()
