#!/usr/bin/env python3
"""Finite numerical diagnostics for geometric-gap constrained entropy.

This is not a proof of the infinite asymptotic or phase nonconstancy.
The published argument is analytic; computations inspect normalization,
endpoint periodicity, and decreasing asymptotic residuals.
"""
import math


def phase_constants(base, rho):
    psi = sum(math.expm1(-rho * base**j) for j in range(-180, 0))
    psi += sum(math.exp(-rho * base**j) for j in range(0, 35))
    a = sum(rho * base**j * math.exp(-rho * base**j)
            for j in range(-180, 35))
    xi = math.log(rho / a) / math.log(base) + psi + a
    return psi, a, xi


def direct_entropy(base, rho, K):
    lam = rho * base**(-K)
    z = 0.0
    lam_weighted_mean = 0.0
    for k in range(K + 35):
        x = lam * base**k
        w = math.exp(-x)
        z += w
        lam_weighted_mean += x * w
    t = lam * z / lam_weighted_mean
    H_over_t = math.log(z) + lam_weighted_mean / z
    L = math.log(1 / t) / math.log(base)
    _, _, xi = phase_constants(base, rho)
    prediction = math.log(L) + (math.log(L)/math.log(base) + xi) / L
    return t, H_over_t, prediction


def main():
    cases = [(2, 0.8), (3, 0.9), (5, 0.8)]
    tests = 0
    for b, rho in cases:
        xi_low = phase_constants(b, 1 / b)[2]
        xi_high = phase_constants(b, 1.0)[2]
        assert abs(xi_low - xi_high) < 3e-12, (b, xi_low, xi_high)
        tests += 1
        deltas = []
        for K in (20, 40, 80, 160):
            t, observed, predicted = direct_entropy(b, rho, K)
            assert 0 < t < 1 and math.isfinite(observed)
            deltas.append(abs(observed-predicted))
            tests += 1
        assert all(deltas[i+1] < deltas[i] for i in range(3)), (b,deltas)
        tests += 1
        print('b=%d phase=%.12f decreasing absolute errors=%s'
              % (b, phase_constants(b, rho)[2],
                 ' '.join('%.4g'%x for x in deltas)))
    # Checks a nontrivial phase difference at base 3; finite evidence only.
    assert abs(phase_constants(3, 0.5)[2] - phase_constants(3, 1.0)[2]) > 1e-4
    tests += 1
    print('DIAGNOSTICS_OK %d' % tests)


if __name__ == '__main__':
    main()
