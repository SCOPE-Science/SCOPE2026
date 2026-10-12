"""Checks for a Palm-Poisson conditional Voronoi-pair theorem.

Run: python verify.py
Only numpy and Python standard library required.
"""
import math
import numpy as np


def close(actual, target, atol, context):
    if not math.isfinite(actual) or abs(actual - target) > atol:
        raise AssertionError(f"{context}: {actual!r} versus {target!r}, tolerance {atol!r}")


def joint_laplace(s, t, lam):
    return (3 * lam / (3 * lam + s + t)
            * 2 * lam / (2 * lam + s)
            * 2 * lam / (2 * lam + t))


def diagonal_survival(u, lam):
    return 4 * math.exp(-3 * lam * u) - 3 * math.exp(-4 * lam * u)


def posterior_mutual(v, lam):
    return -math.expm1(-lam * v) / (lam * v)


def run():
    rng = np.random.default_rng(706188)
    N = 1_600_000
    for lam in (0.65, 1.0, 2.4):
        # Independent Poisson inter-arrival spacings under point Palm.
        a, b, c = rng.exponential(1 / lam, (3, N))
        v0, v1 = (a + b) / 2, (b + c) / 2
        mask = (b < a) & (b < c)
        q = mask.mean()
        close(float(q), 1 / 3, 0.0012, "mutual-pair probability")
        z0, z1 = v0[mask], v1[mask]
        close(float(np.mean(z0)), 5 / (6 * lam), 0.005 / lam, "conditional mean")
        close(float(np.var(z0)), 13 / (36 * lam ** 2), 0.01 / lam ** 2, "conditional variance")
        close(float(np.cov(z0, z1, bias=True)[0, 1]), 1 / (9 * lam ** 2), 0.008 / lam ** 2, "conditional covariance")
        close(float(np.corrcoef(z0, z1)[0, 1]), 4 / 13, 0.018, "conditional correlation")
        close(float(np.corrcoef(v0, v1)[0, 1]), 0.5, 0.008, "ordinary adjacent correlation")
        for s, t in ((0.1 * lam, 0.5 * lam), (0.9 * lam, 1.2 * lam), (2.0 * lam, 0.3 * lam)):
            emp = float(np.mean(np.exp(-s * z0 - t * z1)))
            close(emp, joint_laplace(s, t, lam), 0.0025, "joint Laplace transform")
        for u in (0.1 / lam, 0.6 / lam, 1.5 / lam):
            emp = float(np.mean((z0 > u) & (z1 > u)))
            close(emp, diagonal_survival(u, lam), 0.0025, "joint diagonal survival")
        # A point belongs to an MNN pair if either right or left
        # adjacent gap is strictly smaller than both neighboring gaps.
        left_out, right_out = rng.exponential(1 / lam, (2, N))
        # For a typical point, its left/right adjacent gaps are a,b;
        # outside gaps are left_out,c (independently exponential).
        belongs = ((a < left_out) & (a < b)) | ((b < a) & (b < c))
        close(float(np.mean(belongs)), 2 / 3, 0.0012, "Palm mutual membership")
        typical_length = (a + b) / 2
        for lo, hi in ((0.08 / lam, 0.25 / lam), (0.5 / lam, 0.7 / lam), (1.1 / lam, 1.5 / lam)):
            in_bin = (typical_length >= lo) & (typical_length < hi)
            # Unconditional bin-weighted posterior, integrated numerically.
            sample_p = float(np.mean(belongs[in_bin]))
            grid = np.linspace(lo, hi, 10001)
            density = 4 * lam ** 2 * grid * np.exp(-2 * lam * grid)
            expected = float(np.trapezoid(density * np.array([posterior_mutual(t, lam) for t in grid]), grid)
                             / np.trapezoid(density, grid))
            close(sample_p, expected, 0.013, "posterior mutual membership")
    for lam in (0.4, 1., 3.):
        for v in np.geomspace(0.001 / lam, 10 / lam, 40):
            p = posterior_mutual(v, lam)
            assert 0 < p < 1
        for u in np.linspace(0, 6 / lam, 70):
            assert diagonal_survival(u, lam) >= -1e-12
            assert diagonal_survival(u, lam) <= 1 + 1e-12
    print("PASS: independent Palm-spacing sampling, conditional moments, bivariate Laplace transform, joint survival, Palm posterior and scaling; N=1,600,000 per rate")


if __name__ == "__main__":
    run()
