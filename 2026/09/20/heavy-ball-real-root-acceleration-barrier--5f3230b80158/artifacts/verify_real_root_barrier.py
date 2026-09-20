#!/usr/bin/env python3
"""Deterministic numerical checks for the heavy-ball spectral-interval formulas."""

import cmath
import math


def roots(alpha, beta, lam):
    s = 1.0 + beta - alpha * lam
    disc = s * s - 4.0 * beta
    z = cmath.sqrt(disc)
    return (0.5 * (s + z), 0.5 * (s - z), disc)


def rho_grid(alpha, beta, mu, L, n=20001):
    rho = 0.0
    min_disc = float("inf")
    max_disc = -float("inf")
    for j in range(n):
        lam = mu + (L - mu) * j / (n - 1)
        r1, r2, disc = roots(alpha, beta, lam)
        rho = max(rho, abs(r1), abs(r2))
        min_disc = min(min_disc, disc)
        max_disc = max(max_disc, disc)
    return rho, min_disc, max_disc


def positive_frontier(t, c):
    s = 1.0 + t * t - c * (1.0 - t) ** 2
    return 0.5 * (s + math.sqrt(max(0.0, s * s - 4.0 * t * t)))


def check_case(kappa):
    L = 1.0
    mu = 1.0 / kappa
    q_gd = (L - mu) / (L + mu)
    alpha_gd = 2.0 / (L + mu)
    rho_gd, _, _ = rho_grid(alpha_gd, 0.0, mu, L)

    sqL, sqmu = math.sqrt(L), math.sqrt(mu)
    q_hb = (sqL - sqmu) / (sqL + sqmu)
    alpha_hb = 4.0 / (sqL + sqmu) ** 2
    beta_hb = q_hb * q_hb
    rho_hb, min_disc_hb, _ = rho_grid(alpha_hb, beta_hb, mu, L)

    endpoint_lo = roots(alpha_hb, beta_hb, mu)
    endpoint_hi = roots(alpha_hb, beta_hb, L)
    mid = roots(alpha_hb, beta_hb, 0.5 * (mu + L))

    print(f"kappa={kappa:g}")
    print(f"  GD: alpha={alpha_gd:.12g}, q={q_gd:.12g}, grid_rho={rho_gd:.12g}")
    print(f"  HB: alpha={alpha_hb:.12g}, beta={beta_hb:.12g}, q={q_hb:.12g}, grid_rho={rho_hb:.12g}")
    print(f"      endpoint roots mu=({endpoint_lo[0].real:.12g},{endpoint_lo[1].real:.12g})")
    print(f"      endpoint roots L =({endpoint_hi[0].real:.12g},{endpoint_hi[1].real:.12g})")
    print(f"      midpoint discriminant={mid[2]:.12g}, min_grid_discriminant={min_disc_hb:.12g}")

    assert abs(rho_gd - q_gd) < 2e-12
    assert abs(rho_hb - q_hb) < 2e-8
    assert abs(endpoint_lo[0].real - q_hb) < 2e-8
    assert abs(endpoint_lo[1].real - q_hb) < 2e-8
    assert abs(endpoint_hi[0].real + q_hb) < 2e-8
    assert abs(endpoint_hi[1].real + q_hb) < 2e-8
    assert mid[2] < 0.0
    assert q_hb < q_gd

    c = mu / L
    base = 1.0 - c
    for t in (0.05, 0.10, 0.30, 0.60):
        if t >= 1.0:
            continue
        alpha = (1.0 - t) ** 2 / L
        beta = t * t
        rho, min_disc, _ = rho_grid(alpha, beta, mu, L)
        frontier = positive_frontier(t, c)
        print(f"      positive-root frontier t={t:.2f}: rho={rho:.12g}, formula={frontier:.12g}, GD-positive-base={base:.12g}, min_disc={min_disc:.12g}")
        assert min_disc > -2e-12
        assert abs(rho - frontier) < 2e-10
        assert frontier > base


if __name__ == "__main__":
    for kappa in (1.2, 2.0, 10.0, 100.0):
        check_case(kappa)
    print("All deterministic checks passed.")
