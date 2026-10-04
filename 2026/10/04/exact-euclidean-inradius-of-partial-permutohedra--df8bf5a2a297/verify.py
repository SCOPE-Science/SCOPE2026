#!/usr/bin/env python3
import math

def rhs(n, k):
    return k * (2 * n - k + 1) / 2.0

def crossing(n, k):
    return rhs(n, k) / (k + math.sqrt(k))

def formula(m, n):
    return min(
        n / 2.0,
        math.sqrt(m) * (2 * n - m + 1) / (2 * (math.sqrt(m) + 1)),
    )

cases = 0
for m in range(2, 201):
    for n in range(m - 1, m + 101):
        values = [crossing(n, k) for k in range(1, m + 1)]
        brute = min(values)
        radius = formula(m, n)
        tol = 1e-11 * max(1.0, abs(radius))
        if abs(brute - radius) > tol:
            raise SystemExit(("endpoint failure", m, n, brute, radius))
        center = radius
        for k in range(1, m + 1):
            distance = (rhs(n, k) - k * center) / math.sqrt(k)
            if distance + tol < radius:
                raise SystemExit(("halfspace failure", m, n, k, distance, radius))
        threshold = m + math.sqrt(m)
        if n < threshold - 1e-12:
            top_distance = (rhs(n, m) - m * center) / math.sqrt(m)
            if abs(top_distance - radius) > 1e-10 * max(1.0, radius):
                raise SystemExit(("top tangency failure", m, n))
        elif n > threshold + 1e-12:
            singleton_distance = n - center
            if abs(singleton_distance - radius) > 1e-10 * max(1.0, radius):
                raise SystemExit(("singleton tangency failure", m, n))
        cases += 1

triangle = formula(2, 1)
expected_triangle = 1.0 - 1.0 / math.sqrt(2.0)
if abs(triangle - expected_triangle) > 1e-14:
    raise SystemExit(("triangle boundary failure", triangle, expected_triangle))

print(
    "VERIFY_OK partial-permutohedron inradius "
    f"cases={cases} m=2..200 n=m-1..m+100"
)
