"""Reproduce the two-state harmonic-switching fluctuation/response identities.

Requires numpy and scipy. The generator and Monte Carlo implementations are
independent numerical routes; neither replaces the analytic proof.
"""
import math
import numpy as np
from scipy.linalg import expm


def quantities(k1, k0, a, b, diffusion):
    s = a + b
    Q = np.array([[-a, b], [a, -b]], dtype=float)
    K = np.diag([k1, k0])
    A = Q - K
    p = np.array([b / s, a / s])
    u = np.linalg.solve(2 * K - Q, 2 * diffusion * p)
    gap = math.sqrt((k1 - k0 + a - b) ** 2 + 4 * a * b)
    lam_slow = (k1 + k0 + s - gap) / 2
    lam_fast = (k1 + k0 + s + gap) / 2
    z = a * k0 + b * k1 + 2 * k1 * k0
    y = a * k0 + b * k1 + k1 * k0
    slope = diffusion * a * b * (k1 - k0) ** 2 / (s * z)
    area = diffusion * a * b * (k1 - k0) ** 2 / (s * z * y)
    return A, p, u, gap, lam_slow, lam_fast, slope, area


def piecewise_update(x, state, duration, k1, k0, d, rng):
    k = k1 if state == 1 else k0
    if k == 0:
        return x + math.sqrt(2 * d * duration) * rng.normal()
    fade = math.exp(-k * duration)
    return x * fade + math.sqrt(d * (-math.expm1(-2 * k * duration)) / k) * rng.normal()


def evolve(x, state, t, k1, k0, a, b, d, rng, collect_response=False):
    remain = t
    attenuation = 1.0
    while remain > 0:
        rate = a if state == 1 else b
        dwell = rng.exponential(1 / rate)
        span = min(dwell, remain)
        k = k1 if state == 1 else k0
        if collect_response:
            attenuation *= math.exp(-k * span)
        x = piecewise_update(x, state, span, k1, k0, d, rng)
        remain -= span
        if dwell <= span and remain > 0:
            state = 1 - state
    return x, state, attenuation


def monte_carlo_check(k1, k0, a, b, d, t, seed, n=12000, burn=45):
    rng = np.random.default_rng(seed)
    state_prob = b / (a + b)
    xx, rr = [], []
    for _ in range(n):
        state = int(rng.random() < state_prob)
        x0, state, _ = evolve(0.0, state, burn, k1, k0, a, b, d, rng)
        xt, _, response = evolve(x0, state, t, k1, k0, a, b, d, rng, True)
        xx.append(x0 * xt)
        rr.append(response)
    A, p, u, *_ = quantities(k1, k0, a, b, d)
    E = expm(A * t)
    exact_c = sum(E @ u)
    exact_r = sum(E @ p)
    mc_c = float(np.mean(xx))
    mc_r = float(np.mean(rr))
    # Sampling error is O(n^{-1/2}); tolerances are diagnostic, not proof.
    assert abs(mc_c - exact_c) < 0.10 * max(1.0, abs(exact_c)), (mc_c, exact_c)
    assert abs(mc_r - exact_r) < 0.035 * max(1.0, abs(exact_r)), (mc_r, exact_r)
    return mc_c, exact_c, mc_r, exact_r


def main():
    rng = np.random.default_rng(202610)
    count = 0
    for j in range(160):
        k1 = float(rng.uniform(0.15, 5))
        k0 = 0.0 if j % 4 == 0 else float(rng.uniform(0, 5))
        a = float(rng.uniform(0.15, 3))
        b = float(rng.uniform(0.15, 3))
        d = float(rng.uniform(0.2, 3))
        A, p, u, gap, slow, fast, slope, area = quantities(k1, k0, a, b, d)
        s = a + b
        z = a * k0 + b * k1 + 2 * k1 * k0
        assert slow > 0 and fast > slow
        assert np.all(u > 0) and np.allclose(p, np.array([b / s, a / s]))
        assert np.allclose((2 * np.diag([k1, k0]) - (A + np.diag([k1, k0]))) @ u, 2 * d * p)
        assert np.isclose(np.dot(np.array([k1, k0]), u), d, rtol=1e-11)
        assert np.isclose(gap, fast - slow, rtol=1e-11)
        assert np.isclose(slow * fast, a * k0 + b * k1 + k1 * k0, rtol=1e-11)
        for t in (0.0, 0.015, 0.25, 0.8, 2.0, 5.0):
            E = expm(A * t)
            c = float(np.sum(E @ u))
            r = float(np.sum(E @ p))
            minus_derivative = float(np.array([k1, k0]) @ E @ u)
            measured_defect = minus_derivative - d * r
            predicted = slope / gap * (math.exp(-slow * t) - math.exp(-fast * t))
            assert np.isclose(measured_defect, predicted, atol=2e-11, rtol=3e-9), (
                k1, k0, a, b, t, measured_defect, predicted
            )
            assert c > 0 and r > 0
            if t > 0 and k1 != k0:
                assert predicted > 0
            count += 1
        chi = float(np.sum(np.linalg.solve(-A, p)))
        variance = float(np.sum(u))
        assert np.isclose(variance - d * chi, area, rtol=2e-10, atol=2e-11)
        # Independent definite integration of the difference of two exponentials.
        assert np.isclose(slope / (slow * fast), area, rtol=2e-10)
        tpeak = math.log(fast / slow) / gap
        fpeak = slope / gap * (math.exp(-slow * tpeak) - math.exp(-fast * tpeak))
        for f in (0.90, 0.99, 1.01, 1.1):
            trial = tpeak * f
            test = slope / gap * (math.exp(-slow * trial) - math.exp(-fast * trial))
            assert fpeak > test
        if k0 == 0:
            assert np.isclose(area, d * a / (b * (a + b)))
    assert count == 960
    # The following checks use sample trajectories, not matrix propagation.
    examples = [
        (2.0, 0.0, 0.9, 1.2, 0.6, 0.7, 11223),
        (1.6, 0.35, 0.6, 1.1, 1.3, 1.1, 44556),
    ]
    for e in examples:
        obs = monte_carlo_check(*e)
        print('Monte Carlo C, exact C, Monte Carlo R, exact R:', *[f'{z:.6f}' for z in obs])
    print('PASS: 960 response/covariance comparisons across 160 regimes,')
    print('160 integrated sum rules and peak tests, plus 2 independent simulations.')


if __name__ == '__main__':
    main()
