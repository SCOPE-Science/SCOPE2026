"""Self-contained numerical and normalization checks for a periodic two-particle Langevin theorem.

Requires numpy. Stochastic tests are diagnostic and not substitutes for the proof.
"""
import numpy as np


def h(lam, t):
    return t / lam - (-np.expm1(-lam * t)) / lam**2


def check():
    D1, D2, L = 0.7, 1.3, 2 * np.pi
    d = D1 + D2
    c = 1 / D1 + 1 / D2
    a, b, phi = 1.0, 0.4, 0.37
    t = 1.5
    coeff = np.array([a * a / 2, 2 * b * b])  # pair weights for |V'_n|^2
    lam = np.array([d, 4 * d])
    C = 2 * sum(w * h(x, t) for w, x in zip(coeff, lam))
    sigma = c * sum(coeff)
    # Direct spatial quadrature of the force autocorrelation.
    z = (np.arange(32768) + 0.5) * (L / 32768)
    f = a * np.sin(z) + 2 * b * np.sin(2 * z + phi)
    assert abs(np.mean(f) - 0) < 2e-13
    assert abs(np.mean(f * f) - sigma / c) < 2e-13
    times = np.linspace(0, t, 10001)
    k = np.array([sum(w * np.exp(-x * s) for w, x in zip(coeff, lam)) for s in times])
    quad = 2 * np.trapezoid((t - times) * k, times)
    assert abs(quad - C) < 5e-8, (quad, C)
    assert C < 2 * sigma / c * h(d, t)
    # Pure fundamental is an exact equality witness for all t.
    Afund = np.sqrt(2 * sigma / c)
    assert abs(0.5 * Afund**2 - sigma / c) < 1e-12
    for T in (0.2, 1.5, 4.0):
        lhs = 2 * (sigma / c) * h(d, T)
        rhs = (2 * sigma / c) * h(d, T)
        assert abs(lhs - rhs) < 1e-13
    # The limiting diffusion gain equals the Haar variance of V divided by d.
    expected_gain = (a * a + b * b) / (2 * d)
    assert abs(sum(w / x for w, x in zip(coeff, lam)) - expected_gain) < 1e-14
    assert expected_gain < sigma / (c * d)
    # From ideal exact C''(t), the leading spectral atom and its residual are reconstructible.
    for s in (0.8, 3.0):
        dd = 2 * sum(w * np.exp(-x * s) for w, x in zip(coeff, lam))
        residue = dd - 2 * coeff[0] * np.exp(-lam[0] * s)
        assert np.isclose(residue, 2 * coeff[1] * np.exp(-lam[1] * s), rtol=1e-6, atol=1e-15)
    # Independent direct stochastic simulation of the original SDE, including correlated R noise.
    rng = np.random.default_rng(8141)
    paths = 30000
    steps = 900
    dt = t / steps
    R = rng.uniform(0, L, paths)
    dx = np.zeros(paths)
    dy = np.zeros(paths)
    for _ in range(steps):
        force = a * np.sin(R) + 2 * b * np.sin(2 * R + phi)
        dn1 = np.sqrt(2 * D1 * dt) * rng.standard_normal(paths)
        dn2 = np.sqrt(2 * D2 * dt) * rng.standard_normal(paths)
        dx += force * dt + dn1
        dy += force * dt + dn2
        R += dn1 - dn2
    observed = np.cov(dx, dy)[0, 1]
    assert abs(observed - C) < 0.045, (observed, C)
    assert abs(np.var(dx, ddof=1) - (2 * D1 * t + C)) < 0.07
    assert abs(np.var(dy, ddof=1) - (2 * D2 * t + C)) < 0.07
    print("PASS: periodic Fourier, entropy, sharp optimum, inverse, direct SDE")
    print(f"predicted cross-covariance={C:.12g}; simulated={observed:.12g}; entropy={sigma:.12g}")


if __name__ == '__main__':
    check()
