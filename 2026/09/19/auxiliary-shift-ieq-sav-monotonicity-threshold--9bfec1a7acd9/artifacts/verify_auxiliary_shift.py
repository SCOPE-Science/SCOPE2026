#!/usr/bin/env python3
"""Deterministic checks for homogeneous IEQ/SAV Allen--Cahn shift laws."""

import math


def F(u):
    return 0.25 * (u * u - 1.0) ** 2


def f(u):
    return u ** 3 - u


def ieq_step(u, q, x, c):
    Q = math.sqrt(F(u) + c)
    H = f(u) / Q
    du = -x * H * q / (1.0 + 0.5 * x * H * H)
    return u + du, q + 0.5 * H * du


def sav_step(u, r, x, c0, eps, volume):
    S = math.sqrt(volume / (eps * eps) * F(u) + c0)
    g = f(u) / (eps * eps * S)
    # Homogeneous SAV equations after eliminating r^{n+1}.
    du = -x * f(u) * (r / S) / (1.0 + 0.5 * x * volume * f(u) ** 2 / (eps * eps * S * S))
    dr = volume * f(u) * du / (2.0 * eps * eps * S)
    return u + du, r + dr


def first_iterate(u, x, c):
    A = (1.0 - u * u) ** 2
    return u + x * u * (1.0 - u * u) * (A + 4.0 * c) / (
        A + 4.0 * c + 2.0 * x * u * u * A
    )


def threshold(u, eps, c):
    A = (1.0 - u * u) ** 2
    return eps * eps * (A + 4.0 * c) / (
        u * ((1.0 - u) * A + 4.0 * (1.0 + u) * c)
    )


def critical_shift(u, x):
    A = (1.0 - u * u) ** 2
    return A * (1.0 - x * u * (1.0 - u)) / (
        4.0 * (x * u * (1.0 + u) - 1.0)
    )


def main():
    u0 = 0.5
    eps = 1.0
    x = 2.0
    volume = 3.0
    ccrit = critical_shift(u0, x)

    print("threshold interval")
    print(f"lower_x = {1/(u0*(1+u0)):.15f}")
    print(f"chosen_x = {x:.15f}")
    print(f"upper_x = {1/(u0*(1-u0)):.15f}")
    print(f"critical_normalized_shift = {ccrit:.15f}")
    print()

    for c in (0.05, ccrit, 0.5):
        q = math.sqrt(F(u0) + c)
        u1, q1 = ieq_step(u0, q, x, c)
        u2, q2 = ieq_step(u1, q1, x, c)
        formula_u1 = first_iterate(u0, x, c)
        print(f"c = {c:.15f}")
        print(f"u1 = {u1:.15f}")
        print(f"u1_formula_error = {abs(u1-formula_u1):.3e}")
        print(f"u2 = {u2:.15f}")
        print(f"second_increment = {u2-u1:+.15f}")
        print(f"tau_star = {threshold(u0, eps, c):.15f}")
        print()

    print("IEQ/SAV homogeneous conjugacy")
    c = 0.2
    c0 = volume * c / (eps * eps)
    u_i = u0
    q_i = math.sqrt(F(u_i) + c)
    u_s = u0
    r_s = math.sqrt(volume / (eps * eps) * F(u_s) + c0)
    scale = math.sqrt(volume) / eps
    max_phase = 0.0
    max_aux = 0.0
    for n in range(6):
        max_phase = max(max_phase, abs(u_i - u_s))
        max_aux = max(max_aux, abs(q_i - r_s / scale))
        print(
            f"n={n} u_ieq={u_i:.15f} u_sav={u_s:.15f} "
            f"q_ieq={q_i:.15f} scaled_r_sav={r_s/scale:.15f}"
        )
        if n < 5:
            u_i, q_i = ieq_step(u_i, q_i, x, c)
            u_s, r_s = sav_step(u_s, r_s, x, c0, eps, volume)
    print(f"max_phase_discrepancy = {max_phase:.3e}")
    print(f"max_scaled_aux_discrepancy = {max_aux:.3e}")
    print()

    print("threshold monotonicity")
    vals = [threshold(u0, eps, c) for c in (1e-6, 1e-3, 0.01, 0.1, 1.0, 1000.0)]
    for c, val in zip((1e-6, 1e-3, 0.01, 0.1, 1.0, 1000.0), vals):
        print(f"c={c:g} tau_star={val:.15f}")
    assert all(vals[i] > vals[i + 1] for i in range(len(vals) - 1))
    print(f"small_shift_limit = {eps*eps/(u0*(1-u0)):.15f}")
    print(f"large_shift_limit = {eps*eps/(u0*(1+u0)):.15f}")


if __name__ == "__main__":
    main()
