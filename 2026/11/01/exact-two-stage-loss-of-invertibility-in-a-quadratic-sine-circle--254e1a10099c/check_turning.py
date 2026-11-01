"""Numerical checks for the critical-point phase diagram of a quadratic sine-circle lift.

Uses only the Python standard library. These finite tests supplement an analytic
proof; they do not certify the universal statement by themselves.
"""
import math

PI = math.pi


def thresholds(b, omega):
    B = abs(b)
    assert B > 0
    rho = abs(omega) / B
    delta = math.sqrt(rho * rho + 8)
    u_minus = (rho - delta) / 4
    hd = math.sqrt(1 - u_minus * u_minus) * (rho - u_minus)
    deep = 1 / (4 * PI * B * B * hd)
    shallow = None
    if rho < 1:
        u_plus = (rho + delta) / 4
        hs = math.sqrt(1 - u_plus * u_plus) * (u_plus - rho)
        shallow = 1 / (4 * PI * B * B * hs)
    return deep, shallow


def slope(theta, a, b, omega):
    return 1 + 4 * PI * a * b * math.cos(theta) * (omega - b * math.sin(theta))


def sampled_simple_roots(a, b, omega, divisions=16384):
    values = [slope((2 * PI / divisions) * j, a, b, omega)
              for j in range(divisions + 1)]
    return sum(values[j] * values[j + 1] < 0 for j in range(divisions))


n = 0
for b in (2.0, 4.0, 8.0):
    for ratio in (0.0, 0.15, 0.4, 0.8, 0.95, 1.0, 1.3):
        for sign in (-1, 1):
            omega = sign * b * ratio
            deep, shallow = thresholds(b, omega)
            tests = [(0.8 * deep, 0), (1.2 * deep, 4 if ratio == 0 else 2)]
            if ratio == 0:
                tests = [(0.8 * deep, 0), (1.2 * deep, 4)]
            elif ratio < 1:
                tests = [(0.8 * deep, 0), ((deep + shallow) / 2, 2),
                         (1.2 * shallow, 4)]
            for a, expected in tests:
                count = sampled_simple_roots(a, b, omega)
                assert count == expected, (b, omega, a, count, expected)
                n += 1

# Numeric minimum slope equals the analytic formula, away from equality.
for b, omega, a in ((3.0, 0.0, 0.03), (2.0, 0.7, 0.05),
                    (5.0, -1.1, 0.015), (-3.0, 0.9, 0.03),
                    (1.2, 1.5, 0.06)):
    deep, _ = thresholds(b, omega)
    predicted = 1 - a / deep
    measured = min(slope(2 * PI * j / 32768, a, b, omega)
                   for j in range(32768))
    assert abs(measured - predicted) < 5e-7, (b, omega, measured, predicted)
    n += 1

# The shallow threshold has a 3/2 blow-up as |omega| approaches |b|.
b = 4.0
constant = 3 * math.sqrt(3) / (8 * math.sqrt(2) * PI * b * b)
for gap in (0.01, 0.001, 0.0001):
    _, shallow = thresholds(b, b * (1 - gap))
    ratio = shallow * gap ** 1.5 / constant
    assert abs(ratio - 1) < 0.01, (gap, ratio)
    n += 1

# Splitting of the two critical points born at the deep threshold.
b = 3.0
rho = 0.4
omega = b * rho
threshold, _ = thresholds(b, omega)
Delta = math.sqrt(rho * rho + 8)
s = (rho - Delta) / 4
c = math.sqrt(1 - s * s)
theta0 = math.atan2(s, -c) % (2 * PI)
for eta in (1e-3, 1e-4):
    a = threshold + eta
    delta_expected = math.sqrt(eta / (2 * PI * threshold**2 * b*b * Delta*c))
    # Bisection for a derivative zero on either side of the minimum.
    offsets = []
    for sign in (-1, 1):
        lo, hi = 0.0, 2.0 * delta_expected
        assert slope(theta0, a, b, omega) < 0
        assert slope(theta0 + sign * hi, a, b, omega) > 0
        for _ in range(70):
            mid = (lo + hi) / 2
            if slope(theta0 + sign * mid, a, b, omega) < 0:
                lo = mid
            else:
                hi = mid
        offsets.append((lo + hi) / 2)
    assert all(abs(v / delta_expected - 1) < 0.08 for v in offsets), offsets
    n += 1

print(f"PASS: {n} deterministic parameter and asymptotic tests")
