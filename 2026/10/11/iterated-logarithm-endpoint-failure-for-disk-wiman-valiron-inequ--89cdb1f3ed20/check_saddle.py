#!/usr/bin/env python3
"""Finite diagnostics for a concave coefficient saddle (not an asymptotic proof)."""
import math

def g(x):
    return x / math.log(math.log(x))

def gp(x):
    u = math.log(x)
    L = math.log(u)
    return 1 / L - 1 / (u * L**2)

def gpp(x):
    u = math.log(x)
    L = math.log(u)
    return -(1 - 1/u - 2/(u*L)) / (x*u*L*L)

for x in (5000, 20000, 100000, 1000000):
    u, L = math.log(x), math.log(math.log(x))
    s = gp(x)
    assert 0 < s < 1 and gpp(x) < 0
    H = g(x) - x*s
    assert math.isclose(H, x/(u*L*L), rel_tol=2e-14)
    q = math.sqrt(x*u)*L
    W = int(q/10)
    lo, hi = math.ceil(x-W), math.floor(x+W)
    assert hi-lo+1 >= q/10
    # Only a finite block of coefficients is tested, not the infinite series.
    deviations = [(g(k)-k*s)-H for k in range(lo,hi+1)]
    assert max(deviations) <= 1e-8
    assert min(deviations) > -0.01001
    r = math.exp(-s)
    log_mu_nearest = max(g(math.floor(x))-s*math.floor(x),
                         g(math.ceil(x))-s*math.ceil(x))
    assert H-1 < log_mu_nearest <= H + 1e-8
    log_A = log_mu_nearest - math.log1p(-r)
    block = sum(math.exp(t) for t in deviations)
    block_ratio = block*(1-r)/(math.sqrt(log_A)*math.log(log_A))
    print('saddle x={:<8d} block_terms={:<5d} block_endpoint_ratio={:.6f}'
          .format(x, hi-lo+1, block_ratio))
print('FINITE_DIAGNOSTICS_PASS; the theorem is proved analytically.')
