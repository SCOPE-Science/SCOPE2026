#!/usr/bin/env python3
import math

PI = math.pi
CRIT = 2.0 / PI

def gamma_c(N, mass_ratio):
    m = mass_ratio
    return (2.0 * (m + 1.0) / PI * math.asin(1.0 / (m + 1.0))
            - 2.0 * math.sqrt(m * (m + 2.0)) / (PI * (N - 1) * (m + 1.0)))

def lower_limit(N):
    return CRIT * (N - 2.0) / (N - 1.0)

def G(mass_ratio):
    r = 1.0 / (mass_ratio + 1.0)
    return CRIT * math.asin(r) / r

def bisect_decreasing(func, target, lo=1e-12, hi=1e8, steps=220):
    assert func(lo) > target and func(hi) < target
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        if func(mid) > target:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

# Representative strict mass monotonicity and particle-number monotonicity.
for N in (2, 3, 7, 30):
    ms = (0.02, 0.2, 1.0, 5.0, 40.0)
    vals = [gamma_c(N, m) for m in ms]
    assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))
for m in (0.1, 1.0, 10.0):
    vals = [gamma_c(N, m) for N in (2, 3, 5, 12)]
    assert all(vals[i] < vals[i+1] for i in range(len(vals)-1))

# Exact integer ceiling rule in representative subcritical couplings.
for gam in (0.10, 0.30, 0.50, 0.60):
    nmax = math.ceil(1.0 / (1.0 - PI * gam / 2.0))
    for N in range(2, nmax + 4):
        feasible = gam > lower_limit(N)
        assert feasible == (N <= nmax)

# Critical finite-N crossing and asymptotic ratio.
ratios = []
for N in (100, 1000, 10000, 100000):
    root = bisect_decreasing(lambda m: gamma_c(N, m), CRIT)
    ratios.append(root / math.sqrt((N - 1.0) / 6.0))
assert abs(ratios[-1] - 1.0) < abs(ratios[0] - 1.0)
assert ratios[-1] > 0.99

# Uniform-in-N critical mass as gamma approaches 2/pi from above.
ratios2 = []
for eps in (1e-2, 1e-3, 1e-4, 1e-5):
    gam = CRIT + eps
    root = bisect_decreasing(G, gam)
    prediction = 1.0 / math.sqrt(3.0 * PI * eps)
    ratios2.append(root / prediction)
assert abs(ratios2[-1] - 1.0) < abs(ratios2[0] - 1.0)
assert ratios2[-1] > 0.98

print('VERIFY_OK monotonicity=7 ceiling_cases=4 critical_ratio=%.9f uniform_ratio=%.9f' % (ratios[-1], ratios2[-1]))
