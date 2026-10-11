#!/usr/bin/env python3
import math


def exact_identity_lhs(M, t):
    return math.sin(t) * sum(m * math.sin(m*t) for m in range(1, M+1))


def exact_identity_rhs(M, t):
    return (-M * math.cos(t/2.0) * math.cos((M+0.5)*t)
            + 0.5 * (math.cos(t/2.0)/math.sin(t/2.0)) * math.sin(M*t))


def lambda_midpoint(M, n):
    h = math.pi / n
    total = 0.0
    for j in range(n):
        t = (j + 0.5) * h
        a = exact_identity_rhs(M, t)
        total += abs(a)
    return (2.0 / math.pi) * h * total

max_err = 0.0
cases = 0
for M in range(1, 81):
    for j in range(1, 201):
        t = math.pi * j / 202.0
        err = abs(exact_identity_lhs(M, t) - exact_identity_rhs(M, t))
        max_err = max(max_err, err)
        cases += 1
assert max_err < 2e-10, max_err

target = 8.0 / (math.pi * math.pi)
ratios = []
prev = None
for M in (16, 32, 64, 128, 256):
    n = max(80000, 1000*M)
    lam = lambda_midpoint(M, n)
    ratio = lam / M
    ratios.append((M, ratio))
    assert abs(ratio - target) < 0.02
    if prev is not None:
        assert abs(ratio-target) < abs(prev-target)
    prev = ratio

print("VERIFY_OK identity_cases=%d max_identity_err=%.3e target=%.12f ratios=%s" % (
    cases, max_err, target,
    ",".join("%d:%.12f" % x for x in ratios)
))
