#!/usr/bin/env python3
import math


def direct(N):
    return sum(abs(1.0 + 2.0 * math.cos(2.0 * math.pi * k / N)) for k in range(N)) / N


def closed(N):
    alpha = math.pi / N
    m, r = divmod(N, 3)
    if r == 0:
        return 1.0 / 3.0 + (2.0 * math.sqrt(3.0) / N) / math.tan(alpha)
    if r == 1:
        return (m + 1.0 + 4.0 * math.sin(m * alpha) / math.sin(alpha)) / N
    return (m + 4.0 * math.sin((m + 1) * alpha) / math.sin(alpha)) / N


def negative_indices(N):
    return [k for k in range(N) if 1.0 + 2.0 * math.cos(2.0 * math.pi * k / N) < -1e-12]


def predicted_negative_indices(N):
    return [k for k in range(N) if N / 3.0 < k < 2.0 * N / 3.0]


max_error = 0.0
for N in range(3, 5001):
    a = direct(N)
    b = closed(N)
    err = abs(a - b)
    max_error = max(max_error, err)
    if err > 2e-12:
        raise AssertionError((N, a, b, err))
    if negative_indices(N) != predicted_negative_indices(N):
        raise AssertionError((N, negative_indices(N), predicted_negative_indices(N)))

limit = 1.0 / 3.0 + 2.0 * math.sqrt(3.0) / math.pi
if abs(closed(100000) - limit) > 1e-8:
    raise AssertionError((closed(100000), limit))

print(f"checked_N=3..5000 max_error={max_error:.3e}")
print(f"limit={limit:.15f} sample_100000={closed(100000):.15f}")
print("VERIFY_OK")
