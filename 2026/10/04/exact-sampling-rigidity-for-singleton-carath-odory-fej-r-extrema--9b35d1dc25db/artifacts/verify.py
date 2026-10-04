#!/usr/bin/env python3
import math

TOL = 2e-11
cases = 0
strict_cases = 0
contact_cases = 0
min_off_contact = float("inf")

for n in range(3, 41):
    alpha = math.pi / (2.0 * n)
    C = math.cos(alpha)
    lam = 1.0 / C
    c = ((-1.0) ** n) * math.tan(alpha) / n

    def phi(theta):
        return 1.0 + lam * math.cos(theta) + c * math.cos(n * theta)

    # The two analytic contacts.
    for theta in (math.pi - alpha, math.pi + alpha):
        assert abs(phi(theta)) < 2e-13
        assert abs(math.cos(n * theta)) < 2e-13
        assert abs(math.cos(theta) + C) < 2e-13

    # Corroborative dense circle scan; this is not the proof.
    dense_min = min(phi(2.0 * math.pi * k / 20000.0) for k in range(20000))
    assert dense_min > -TOL

    for m in range(3, 301):
        cases += 1
        vals = []
        for j in range(m):
            theta = 2.0 * math.pi * j / m
            vals.append((theta, phi(theta), math.cos(theta)))

        if m % (4 * n) == 0:
            contact_cases += 1
            j = m * (2 * n - 1) // (4 * n)
            theta = 2.0 * math.pi * j / m
            assert abs(phi(theta)) < 3e-12
            assert abs(math.cos(n * theta)) < 3e-12
            # The contact constraint is exactly 1 - lambda*C >= 0.
            assert abs(1.0 - lam * C) < 3e-14
        else:
            strict_cases += 1
            grid_min = min(v for _, v, _ in vals)
            min_off_contact = min(min_off_contact, grid_min)
            assert grid_min > 1e-10
            ratios = [v / (-co) for _, v, co in vals if co < -1e-14]
            assert ratios
            eps = 0.5 * min(ratios)
            assert eps > 0.0
            for theta, _, _ in vals:
                bumped = 1.0 + (lam + eps) * math.cos(theta) + c * math.cos(n * theta)
                assert bumped > -TOL

print(f"cases={cases} contact_cases={contact_cases} strict_cases={strict_cases}")
print(f"minimum_off_contact_margin={min_off_contact:.12e}")
print("VERIFY_OK")
