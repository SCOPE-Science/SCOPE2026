"""Deterministic verification of the two-site Beta report phase formulas."""

from math import exp


def solve_a(alpha, iterations=100):
    lo, hi = 0.0, 50.0
    for _ in range(iterations):
        mid = (lo + hi) / 2.0
        cdf = 1.0 - exp(-mid) * (1.0 + mid)
        if cdf < alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def a_low(lam, tau, h):
    x = lam * tau * h
    return 1.0 - exp(-x) * (1.0 + x)


def a_high(lam, tau, h):
    return (
        1.0
        - 2.0 * exp(-lam * h)
        + exp(-lam * tau * h) * (1.0 - lam * h * (2.0 - tau))
    )


def exact_deficit(alpha, theta, m, rho):
    L = m - 1
    h = solve_a(alpha) / (L - 1.0 + rho)
    r = exp(-h)

    n0 = (
        (L - 1) * r ** (L - 2) * a_high(1.0, 1.0 + rho, h)
        + L * r ** (L - 1) * a_low(1.0, rho, h)
    )
    f0a = (L - 1) * r ** (L - 2) * (1.0 - r) ** 2
    f0b = L * r ** (L - 1) * (1.0 - r) ** 2

    n1 = (
        (L - 1) * r ** (theta * (L - 2)) * a_high(theta, 1.0 + rho, h)
        + L * r ** (theta * (L - 1)) * a_low(theta, rho, h)
    )
    f1a = (L - 1) * r ** (theta * (L - 2)) * (1.0 - r**theta) ** 2
    f1b = L * r ** (theta * (L - 1)) * (1.0 - r**theta) ** 2

    if n0 <= f0a:
        fraction = n0 / f0a
        deficit = n1 - fraction * f1a
        boundary = "A"
    else:
        fraction = (n0 - f0a) / f0b
        deficit = n1 - f1a - fraction * f1b
        boundary = "B"
    return deficit, boundary, fraction


def phase_function(rho):
    s = min(rho, 1.0 - rho)
    return (1.0 - 3.0 * s * s) / 6.0


def limiting_constant(alpha, theta, rho):
    a = solve_a(alpha)
    q = exp(-a)
    return theta**2 * (theta - 1.0) * q**theta * a**3 * phase_function(rho)


def main():
    alpha, theta = 0.05, 2.0
    a = solve_a(alpha)
    oracle = 1.0 - exp(-theta * a) * (1.0 + theta * a)
    print(f"a={a:.15f}")
    print(f"oracle_power={oracle:.15f}")
    print(f"half_phase_limit={limiting_constant(alpha, theta, 0.5):.15f}")

    for m in (8, 16, 64, 256, 512):
        deficit, boundary, fraction = exact_deficit(alpha, theta, m, 0.5)
        print(
            f"m={m:3d} deficit={deficit:.15g} "
            f"relative={deficit / oracle:.9g} m2d={m*m*deficit:.12g} "
            f"boundary={boundary} fraction={fraction:.9g}"
        )

    q = exp(-a)
    base = theta**2 * (theta - 1.0) * q**theta * a**3
    print("phase_check_m=512")
    for rho in (0.05, 0.10, 0.25, 0.40, 0.50, 0.60, 0.75, 0.90, 0.95):
        deficit, _, _ = exact_deficit(alpha, theta, 512, rho)
        observed = 512 * 512 * deficit / base
        print(
            f"rho={rho:.2f} observed={observed:.9f} "
            f"limit={phase_function(rho):.9f}"
        )


if __name__ == "__main__":
    main()
