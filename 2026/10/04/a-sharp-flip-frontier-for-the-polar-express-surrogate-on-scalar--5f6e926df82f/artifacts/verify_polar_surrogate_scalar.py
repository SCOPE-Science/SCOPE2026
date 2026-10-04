import math

def T(u, tau):
    return u * (1.0 - tau / ((1.0 + abs(u)**4)**0.25))

def deriv(u, tau):
    return 1.0 - tau * (1.0 + abs(u)**4)**(-1.25)

# Representative strict magnitude contraction throughout the stable regime.
for tau in [0.1, 0.5, 1.0, 1.7, 2.0]:
    for u in [1e-2, 0.1, 1.0, 10.0, 1e3]:
        assert abs(T(u, tau)) < abs(u)

# Matched-step fifth-order coefficient: T(u)/u^5 -> 1/4.
for u in [1e-2, 5e-3, 2e-3]:
    ratio = T(u, 1.0) / (u**5)
    assert abs(ratio - 0.25) < 2e-5

# Exact postcritical symmetric two-cycle and multiplier.
for tau in [2.01, 2.2, 3.0, 5.0, 10.0]:
    us = ((tau/2.0)**4 - 1.0)**0.25
    assert abs(T(us, tau) + us) < 2e-12
    assert abs(T(-us, tau) - us) < 2e-12
    d = deriv(us, tau)
    expected = 1.0 - 32.0/(tau**4)
    assert abs(d - expected) < 2e-12
    assert d*d < 1.0

# Critical asymptotic: |u_k|*(2k)^(1/4) -> 1.
u = 1.0
samples = {}
for k in range(1, 400001):
    u = T(u, 2.0)
    if k in [50000, 100000, 200000, 400000]:
        samples[k] = abs(u) * (2.0*k)**0.25
for k, val in samples.items():
    assert abs(val - 1.0) < 0.02

# Critical signs alternate eventually.
u = 0.1
last = u
for k in range(100):
    nxt = T(last, 2.0)
    assert nxt * last < 0.0
    last = nxt

print("VERIFY_OK")
