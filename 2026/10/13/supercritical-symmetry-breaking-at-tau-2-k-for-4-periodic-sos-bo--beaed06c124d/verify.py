#!/usr/bin/env python3
import math


def p(k, x):
    return (k - 1) * x ** (k + 1) - k * x ** (k - 1) + 1.0


def lower_root(k):
    lo = 0.0
    hi = math.sqrt(k / (k + 1.0))
    assert p(k, lo) > 0.0 and p(k, hi) < 0.0
    for _ in range(180):
        mid = (lo + hi) / 2.0
        if p(k, mid) > 0.0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def equations(k, tau, a, b):
    c = a + b - tau
    return c * a ** k + tau * a - 2.0, c * b ** k + tau * b - 2.0


def check(k):
    x = lower_root(k)
    tau2 = 2.0 * k / ((k - 1.0) * x)
    assert tau2 > 2.0 * (k + 1.0) / (k - 1.0)
    B = k - (k - 1.0) * x * x
    assert B > 0.0
    assert abs(x ** (k - 1) * B - 1.0) < 2e-11

    # Source equation (2.10), evaluated in a scaled form through its shared root.
    q = 2.0 * x ** (k + 1) - tau2 * x ** k + tau2 * x - 2.0
    assert abs(q) < 2e-11

    det = 2.0 * (k - 1.0) * (k - (k + 1.0) * x * x) / (x * B)
    C = (
        k * (3.0 * k * k - (3.0 * k * k - k + 2.0) * x * x)
        / (3.0 * x ** 3 * (k - 1.0) * (k - (k + 1.0) * x * x))
    )
    assert det > 0.0 and C > 0.0

    # First coefficient of s(u), obtained from the same linearized 2x2 system.
    s1 = -k * (k * x * x - k - 5.0 * x * x + 2.0) / (
        6.0 * x * (k * x * x - k + x * x)
    )

    delta = 1e-7
    u = delta / C
    d = math.sqrt(u)
    s = x + s1 * u
    a, b = s + d, s - d
    f1, f2 = equations(k, tau2 + delta, a, b)
    assert max(abs(f1), abs(f2)) < 2e-10
    ratio = abs(a - b) / (2.0 * math.sqrt(delta / C))
    assert abs(ratio - 1.0) < 2e-7
    return tau2, 2.0 / math.sqrt(C), max(abs(f1), abs(f2))


worst = 0.0
samples = []
for k in range(2, 41):
    tau2, amp, residual = check(k)
    worst = max(worst, residual)
    if k in (2, 3, 4, 10, 40):
        samples.append((k, tau2, amp))
print("VERIFY_OK degrees=2..40 worst_residual={:.3e} samples={}".format(worst, samples))
