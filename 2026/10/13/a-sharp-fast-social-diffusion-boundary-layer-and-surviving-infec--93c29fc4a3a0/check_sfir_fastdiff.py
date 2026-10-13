#!/usr/bin/env python3
"""Numerical diagnostic for a published Gaussian epidemic ODE's fast-diffusion limit.

These numerical checks do not establish the infinite-parameter limit proved analytically.
"""
from math import exp, log, sqrt
from scipy.integrate import solve_ivp


def main():
    s0, i0, r0 = 0.8, 0.1, 0.1
    beta0, beta1, mu0, gamma, w0 = 0.2, 0.6, 0.4, 0.3, 0.5
    assert abs(s0 + i0 + r0 - 1.0) < 1e-14
    t_final = 0.6
    k = s0 + i0
    target_log = -2 * sqrt(beta1 * k) / gamma * (1 - exp(-gamma * t_final / 2))
    target_i = k * exp(-gamma * t_final)
    target_risk = sqrt(beta1 / target_i)
    limits = (target_log, target_i, target_risk)
    errors = []
    print('predicted: log(S/S0)/sqrt(D), I, (mean_beta-beta0)/sqrt(D) =', limits)

    for d in (100, 10_000, 1_000_000):
        def rhs(t, y):
            log_s, i, w = y
            infection = (beta0 + w) * exp(log_s) * i
            return [-(beta0 + w) * i,
                    infection - gamma * i,
                    2 * d * beta1 - 2 * mu0 * w - 2 * i * w * w]

        result = solve_ivp(rhs, (0, t_final),
                           (log(s0), i0, w0), method='Radau',
                           rtol=2e-9, atol=1e-11)
        assert result.success, result.message
        z, i, w = result.y[:, -1]
        observed = (z / sqrt(d), i, w / sqrt(d))
        error = tuple(abs(a - b) for a, b in zip(observed, limits))
        print('D=', d, 'observed=', observed, 'absolute_error=', error)
        errors.append(error)

    assert all(errors[j + 1][k] < errors[j][k] for j in range(2) for k in range(3))
    assert max(errors[-1]) < 2e-3
    print('VERIFY_OK: numerical diagnostic only')


if __name__ == '__main__':
    main()
