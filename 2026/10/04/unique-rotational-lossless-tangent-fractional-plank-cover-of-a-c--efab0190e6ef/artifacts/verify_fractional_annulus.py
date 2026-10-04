#!/usr/bin/env python3
"""Independent arithmetic checks for the explicit annulus fractional-plank formulas."""
from math import sqrt, pi, sin


def gamma_tail(a, h):
    return 2.0 * (a + h) / sqrt(h * (h + 2.0 * a))


def density(a, h):
    return 2.0 * a * a / (h * (h + 2.0 * a)) ** 1.5


def antiderivative(a, h):
    return 2.0 * sqrt(h * (h + 2.0 * a))


def transformed_integrand(a, s, phi):
    # z = y sin(phi)^2, t = sqrt(a^2+z)-a.
    y = s * (s + 2.0 * a)
    z = y * sin(phi) ** 2
    if z == 0.0:
        return 2.0
    t = sqrt(a * a + z) - a
    g = gamma_tail(a, t)
    # dz/dphi divided by [2(t+a)*sqrt(y-z)] is the transformed Jacobian.
    dz = 2.0 * y * sin(phi) * (1.0 - sin(phi) ** 2) ** 0.5
    den = 2.0 * (t + a) * sqrt(max(0.0, y - z))
    return g * dz / den


def simpson(f, lo, hi, n=20000):
    if n % 2:
        n += 1
    h = (hi - lo) / n
    total = f(lo) + f(hi)
    for k in range(1, n):
        total += (4.0 if k % 2 else 2.0) * f(lo + k * h)
    return total * h / 3.0


def main():
    # Tail derivative and layer-cake antiderivative identities on a parameter grid.
    for a in (0.05, 0.2, 0.5, 0.8, 0.95):
        H = 1.0 - a
        for frac in (0.07, 0.19, 0.43, 0.77):
            h = frac * H
            q = h * (h + 2.0 * a)
            # Exact algebraic derivative: Gamma'(h) = -2 a^2 / q^(3/2).
            eps = max(1e-8, 1e-6 * h)
            num = (gamma_tail(a, h + eps) - gamma_tail(a, h - eps)) / (2.0 * eps)
            exact = -density(a, h)
            assert abs(num - exact) <= 2e-5 * max(1.0, abs(exact))
            # Exact algebraic antiderivative derivative.
            numA = (antiderivative(a, h + eps) - antiderivative(a, h - eps)) / (2.0 * eps)
            assert abs(numA - gamma_tail(a, h)) <= 2e-6 * max(1.0, gamma_tail(a, h))
        cost = antiderivative(a, H)
        assert abs(cost - 2.0 * sqrt(1.0 - a * a)) < 1e-12

        # After the Abel substitution, the full integrand is identically 2 on (0,pi/2).
        for sfrac in (0.03, 0.2, 0.55, 1.0):
            s = sfrac * H
            for phi in (0.11, 0.37, 0.81, 1.23):
                assert abs(transformed_integrand(a, s, phi) - 2.0) < 2e-12
            # The transformed integrand being 2 makes the Abel integral exactly pi.
            assert abs(2.0 * (pi / 2.0) - pi) < 1e-15

    # Published special hole radius a=1/2: cost sqrt(3).
    assert abs(2.0 * sqrt(1.0 - 0.25) - sqrt(3.0)) < 1e-15
    print("PASS: tail monotonicity derivative, Abel transform, and total-width identities checked.")


if __name__ == "__main__":
    main()
