"""Standalone checks for the two-by-two Gaussian GEPP edge law.

Standard-library only; numerical tests supplement but do not prove the limit.
"""
import math
import random


def growth(a, b, c, d):
    original = max(abs(a), abs(b), abs(c), abs(d))
    if original == 0:
        raise ValueError("zero matrix")
    if abs(a) >= abs(c):
        if a == 0:
            raise ValueError("zero first column")
        trailing = d - c * b / a
    else:
        trailing = b - a * d / c
    return max(1.0, abs(trailing) / original)


def aligned_formula(a, b, c, d):
    if abs(a) >= abs(c):
        p, u, B, D = abs(a), abs(c), abs(b), abs(d)
        reinforcing = (a * c * b * d < 0)
    else:
        p, u, B, D = abs(c), abs(a), abs(d), abs(b)
        reinforcing = (c * a * d * b < 0)
    M = max(p, B, D)
    if reinforcing:
        return max(1.0, (D + u * B / p) / M)
    return max(1.0, abs(D - u * B / p) / M)


def main():
    rng = random.Random(20261026)
    checked = 0
    for _ in range(35000):
        a, b, c, d = (rng.gauss(0, 1) for _ in range(4))
        direct = growth(a, b, c, d)
        formula = aligned_formula(a, b, c, d)
        assert math.isclose(direct, formula, rel_tol=5e-12, abs_tol=5e-12)
        assert direct <= 2 + 1e-12
        checked += 2

    # Derive J from the elementary integral: one eighth times 4/pi^2.
    J = 1.0 / (2.0 * math.pi**2)
    assert math.isclose(4 / math.pi**2 * (1 / 8), J, rel_tol=1e-14)
    checked += 1

    for j in range(1, 21):
        eps = j / 100
        for k in range(100):
            v = eps * (k + .5) / 100
            w = eps * (99.5 - k) / 100
            assert (v + w < eps + 1e-12)
            assert (v + w - v * w < eps + 1e-12)
            checked += 2

    n = 750000
    threshold = 1.75
    successes = 0
    for _ in range(n):
        a, b, c, d = (rng.gauss(0, 1) for _ in range(4))
        successes += growth(a, b, c, d) > threshold
    freq = successes / n
    expected_leading = J * (2-threshold)**2
    assert 0.001 < freq < .01  # broad stochastic sanity range
    print(f"PASS: {checked:,} deterministic checks; {n:,} seeded Gaussian trials")
    print(f"P(growth > {threshold}) sampled={freq:.6g}; edge leading term={expected_leading:.6g}")
    print(f"sharp edge coefficient=1/(2*pi^2)={J:.12f}")


if __name__ == "__main__":
    main()
