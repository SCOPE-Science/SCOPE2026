"""Reproducible finite checks for Gaussian residual-screened sketched orthogonalization.

The theorem itself is proved analytically. Monte Carlo checks only test implementation,
scaling and finite diagnostics; they do not certify moment divergence.
"""
import math
import numpy as np


def analytic_moment_finite(k, m, trials, order):
    assert k >= 1 and m >= k + 1 and trials >= 1 and order > 0
    excess = m - k
    return order < min(excess + 1, trials * excess)


def simulate(k, m, trials, draws, seed):
    rng = np.random.default_rng(seed)
    G = rng.standard_normal((draws, trials, m, k))
    h = rng.standard_normal((draws, trials, m))
    GTG = np.einsum('ntmi,ntmj->ntij', G, G)
    GTh = np.einsum('ntmi,ntm->nti', G, h)
    coefficients = np.linalg.solve(GTG, GTh[..., None])[..., 0]
    residual_sq = np.einsum('ntm,ntm->nt', h, h) - np.einsum('nti,nti->nt', GTh, coefficients)
    assert np.min(residual_sq) > 0
    winning = np.argmax(residual_sq, axis=1)
    chosen_c = coefficients[np.arange(draws), winning]
    chosen_r = residual_sq[np.arange(draws), winning]
    c_sq = np.einsum('ni,ni->n', chosen_c, chosen_c)
    norm_sq = m * (1 + c_sq) / chosen_r
    angle_sq = c_sq / (1 + c_sq)
    return norm_sq, angle_sq, chosen_c, chosen_r, G, h, coefficients, residual_sq


def main():
    checks = 0
    for k in (1, 2, 5):
        for d in (1, 2, 3, 5):
            for trials in (1, 2, 4, 9):
                for p in (0.5, 1, 2, 3, 4, 5.5):
                    predicted = p < min(d + 1, trials * d)
                    assert analytic_moment_finite(k, k + d, trials, p) == predicted
                    checks += 1
    assert not analytic_moment_finite(1, 3, 1, 2)
    assert analytic_moment_finite(1, 3, 2, 2)
    assert not analytic_moment_finite(1, 2, 100, 2)
    checks += 3

    # The beta law gives exact expected squared Euclidean angular projection.
    for k, m, trials, N, seed in ((1, 3, 2, 220000, 438), (2, 4, 2, 150000, 7301)):
        norms, angles, c, rs, *_ = simulate(k, m, trials, N, seed)
        expected_norm = m * (k + 1) * math.log(2.0)
        expected_angle = k / (m + 1.0)
        batch_means = [float(np.mean(group)) for group in np.array_split(norms, 25)]
        robust_mean = float(np.median(batch_means))
        assert abs(robust_mean / expected_norm - 1) < 0.12, (k, robust_mean, expected_norm)
        assert abs(np.mean(angles) - expected_angle) < 0.015, (k, np.mean(angles), expected_angle)
        checks += 2
        # Selected coefficient's angle law does not change under residual screening.
        plain = simulate(k, m, 1, 35000, seed + 10)[1]
        screened = angles[:35000]
        assert abs(np.mean(plain) - np.mean(screened)) < 0.025
        checks += 1
        # The chosen coefficient is independent of the chosen residual in law.
        cov = float(np.mean((angles-angles.mean()) * (rs-rs.mean())))
        sd = float(np.std(angles) * np.std(rs))
        assert abs(cov / sd) < 0.02
        checks += 1
        print('k=', k, 'm=', m, 'two-sketch batch-median estimate for Euclidean norm^2=', round(robust_mean, 7),
              'target=', round(expected_norm, 7), 'angular mean=', round(float(angles.mean()), 7),
              'target=', expected_angle)

    # The Gaussian regression projection equals the small least-squares operation.
    for k, m in ((1, 3), (2, 4), (2, 5)):
        rng = np.random.default_rng(1700 + k + m)
        for _ in range(54):
            G = rng.standard_normal((m, k)) / math.sqrt(m)
            h = rng.standard_normal(m) / math.sqrt(m)
            c = np.linalg.lstsq(G, h, rcond=None)[0]
            residual = h - G @ c
            rho = np.linalg.norm(residual)
            q = np.r_[-c, 1.0] / rho
            assert np.allclose(G.T @ (residual / rho), 0, atol=1e-10)
            assert abs(np.linalg.norm(residual / rho) - 1) < 1e-10
            assert abs(np.dot(q, q) - (1 + np.dot(c, c)) / rho**2) < 1e-9
            assert abs(sum(q[:k]**2) / np.dot(q, q) - np.dot(c,c)/(1+np.dot(c,c))) < 1e-11
            checks += 4

    # Independent analytic quadrature of the exact two-candidate chi-square residual factor.
    z = np.geomspace(1e-10, 100.0, 200000)
    integrand = np.exp(-z/2) * (-np.expm1(-z/2)) / z
    integral = float(np.trapezoid(integrand, z))
    assert abs(integral - math.log(2)) < 1e-8, integral
    checks += 1
    print('analytic Frullani residual integral=', integral, 'target=', math.log(2))
    print('PASS:', checks, 'checks. Simulation is diagnostic only; the proof establishes all infinite-horizon moment claims.')


if __name__ == '__main__':
    main()
