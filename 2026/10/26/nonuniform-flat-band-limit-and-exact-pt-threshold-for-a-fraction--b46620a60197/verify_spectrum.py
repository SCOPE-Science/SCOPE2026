#!/usr/bin/env python3
"""Reproducible numerical sanity checks for the exact Bloch-spectrum formulas.
The analytic proof is in RESULT.md; this script checks representative boundary cases.
Uses only the Python standard library.
"""
import math

V = 1.0
TOL = 2e-10

def q_of(kx, ky):
    return 4.0 - 2.0 * math.cos(kx) - 2.0 * math.cos(ky)

def radicand(q, s, gamma, V=V):
    return V * V * (4.0 - q ** s) ** 2 - gamma * gamma

def gamma_threshold(s, V=V):
    if not (0.0 < s < 2.0 / 3.0):
        return 0.0
    return V * (4.0 - 8.0 ** s)

def main():
    # Below the critical exponent, all sampled Bloch fibers are real at threshold.
    exponents = [0.05, 0.1, 0.25, 0.4, 0.5, 0.6, 2.0/3.0 - 1e-6]
    qgrid = [8.0 * j / 400 for j in range(401)]
    for s in exponents:
        gc = gamma_threshold(s)
        assert gc > 0.0
        assert min(radicand(q, s, gc) for q in qgrid) >= -TOL, (s, gc)
        assert radicand(8.0, s, gc + 1e-5) < 0.0, (s, gc)

    # At and above 2/3, q*=4^(1/s) lies in [0,8], forcing the Bloch factor to zero.
    for s in [2.0/3.0, 0.7, 0.8, 0.95, 0.999]:
        qstar = 4.0 ** (1.0 / s)
        assert qstar <= 8.0 + 1e-10, (s, qstar)
        assert abs(4.0 - qstar ** s) < 1e-9, (s, qstar)
        assert radicand(qstar, s, 0.2) < 0.0

    # Nonuniform s -> 0 limit: fixed q>0 gives q^s -> 1, while q=0 remains 0.
    eps = 1e-6
    for q in [0.125, 1.0, 2.0, 8.0]:
        assert abs(q ** eps - 1.0) < 3e-6, (q, q ** eps)
        assert abs((4.0 - q ** eps) - 3.0) < 3e-6
    assert 4.0 - 0.0 ** eps == 4.0
    assert abs((4.0 - 8.0 ** eps) - 3.0) < 3e-6
    print('PASS: 7 subcritical threshold grids; 5 supercritical witness wavevectors; nonuniform s->0 limit.')
    print('Analytic proof, not the finite grid, establishes the all-wavevector statements.')

if __name__ == '__main__':
    main()
