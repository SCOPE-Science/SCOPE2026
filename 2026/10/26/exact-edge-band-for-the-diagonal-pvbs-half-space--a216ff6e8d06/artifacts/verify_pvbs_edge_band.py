#!/usr/bin/env python3
"""Finite consistency checks for the diagonal PVBS edge-band formulas."""
from math import cos, pi, sin


def check(lam: float, k: float) -> None:
    c = cos(k / 2.0)
    r = lam * c
    a = 2.0 * lam * lam / (1.0 + lam * lam)
    b = 2.0 * lam * c / (1.0 + lam * lam)
    energy = 2.0 * lam * lam * sin(k / 2.0) ** 2 / (1.0 + lam * lam)

    # Boundary equation for v_0 = 1, v_s = r**s.
    assert abs((a - energy) - b * r) < 2e-12

    # Bulk recurrence; values beyond the checked range are supplied by r**s,
    # so this checks the infinite geometric ansatz rather than a truncated box.
    for s in range(1, 20):
        v_prev = r ** (s - 1)
        v_now = r ** s
        v_next = r ** (s + 1)
        residual = 2.0 * v_now - b * (v_prev + v_next) - energy * v_now
        assert abs(residual) < 2e-11

    bulk_min = 2.0 - 2.0 * b
    exact_gap = 2.0 * (1.0 - lam * c) ** 2 / (1.0 + lam * lam)
    assert abs((bulk_min - energy) - exact_gap) < 2e-12
    assert exact_gap > 0.0
    assert 0.0 <= r < 1.0


def main() -> None:
    lambdas = (0.1, 0.25, 0.5, 0.9, 0.999)
    momenta = (-pi, -2.4, -1.1, -0.2, 0.0, 0.37, 1.8, 2.9, pi)
    count = 0
    for lam in lambdas:
        for k in momenta:
            check(lam, k)
            count += 1
    print(f"PASS: {count} parameter pairs; recurrence and bulk-separation identities checked")


if __name__ == "__main__":
    main()
