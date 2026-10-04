#!/usr/bin/env python3
import math

TOL = 2e-10
min_slack = float("inf")
max_active = 0.0
max_obj = 0.0
cases = 0
samples = 0

for N in range(7, 2001):
    if N % 2 == 0:
        a = 0.0
        b = 0.5
        target = 2.0
        active = [N // 2]
    elif N % 3 == 0:
        C3 = math.cos(3.0 * math.pi / N)
        a = 0.0
        b = 1.0 / (2.0 * C3)
        target = 1.0 + 1.0 / C3
        active = [(N - 3) // 6, (N - 1) // 2]
    else:
        eps = 1 if N % 6 == 1 else -1
        A = math.cos(math.pi / 3.0 - eps * math.pi / (3.0 * N))
        C = math.cos(math.pi / N)
        D = math.cos(3.0 * math.pi / N)
        den = A * D + C * C
        a = (C - D) / (2.0 * den)
        b = (A + C) / (2.0 * den)
        target = 1.0 + (A + 2.0 * C - D) / den
        q = (N - eps) // 6
        h = (N - 1) // 2
        active = [q, h]

        R = C - A
        delta = math.pi / (3.0 * N)
        if eps == 1:
            B = math.cos(math.pi / 3.0 + 5.0 * delta)
            assert B < R < A
        else:
            B = math.cos(math.pi / 3.0 - 5.0 * delta)
            assert A < R < B

        for x in (-C, A, R, -0.71, 0.12, 0.83):
            lhs = 1.0 + 2.0 * a * x + 2.0 * b * (4.0 * x**3 - 3.0 * x)
            rhs = 8.0 * b * (x + C) * (x - A) * (x - R)
            assert abs(lhs - rhs) < 3e-10

    obj = 1.0 + 2.0 * a + 2.0 * b
    max_obj = max(max_obj, abs(obj - target))
    assert abs(obj - target) < TOL

    vals = []
    for k in range(N):
        v = 1.0 + 2.0 * a * math.cos(2.0 * math.pi * k / N) + 2.0 * b * math.cos(6.0 * math.pi * k / N)
        vals.append(v)
        min_slack = min(min_slack, v)
        samples += 1
    assert min(vals) >= -TOL
    for k in active:
        max_active = max(max_active, abs(vals[k]))
        assert abs(vals[k]) < 4e-10
    cases += 1

print(f"cases={cases}")
print(f"samples={samples}")
print(f"minimum_slack={min_slack:.3e}")
print(f"maximum_active_residual={max_active:.3e}")
print(f"maximum_objective_residual={max_obj:.3e}")
print("VERIFY_OK")
