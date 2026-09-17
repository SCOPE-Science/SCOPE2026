#!/usr/bin/env python3
from math import comb

def binom_tail(n, k, x):
    return sum(comb(n, j) * x**j * (1-x)**(n-j) for j in range(k, n+1))

def binom_tail_prime(n, k, x):
    return n * comb(n-1, k-1) * x**(k-1) * (1-x)**(n-k)

_tau_cache = {}
def tangent_tau(n, k):
    key = (n, k)
    if key in _tau_cache:
        return _tau_cache[key]
    assert 2 <= k <= n-1
    lo = (k-1)/(n-1)
    hi = 1.0
    for _ in range(90):
        mid = (lo + hi)/2
        h = mid*binom_tail_prime(n,k,mid) - binom_tail(n,k,mid)
        if h > 0:
            lo = mid
        else:
            hi = mid
    ans = (lo + hi)/2
    _tau_cache[key] = ans
    return ans

def upper(n, k, p):
    if k == 1:
        return 1 - (1-p)**n
    if k == n:
        return p
    t = tangent_tau(n,k)
    gt = binom_tail(n,k,t)
    return p*gt/t if p <= t else binom_tail(n,k,p)

def lower(n, k, p):
    return 1 - upper(n, n-k+1, 1-p)

def finite_exchangeable_bounds(n,k,p):
    return max((n*p-k+1)/(n-k+1), 0.0), min(n*p/k, 1.0)

examples = [(10,6,.3),(10,6,.5),(20,12,.3),(3,2,.5)]
for n,k,p in examples:
    t = tangent_tau(n,k) if 1 < k < n else float("nan")
    lo,hi = finite_exchangeable_bounds(n,k,p)
    print(f"n={n} k={k} p={p:.3f} tau={t:.12f} "
          f"L={lower(n,k,p):.12f} U={upper(n,k,p):.12f} "
          f"finite=[{lo:.12f},{hi:.12f}] iid={binom_tail(n,k,p):.12f}")
    if 1 < k < n:
        residual = t*binom_tail_prime(n,k,t)-binom_tail(n,k,t)
        print(f"  tangent residual={residual:.3e}")

max_majorant_violation = 0.0
max_concavity_violation = 0.0
case_count = 0
grid = [i/400 for i in range(401)]
for n in range(2,21):
    for k in range(1,n+1):
        vals = [upper(n,k,x) for x in grid]
        for x,c in zip(grid,vals):
            max_majorant_violation = max(
                max_majorant_violation, binom_tail(n,k,x)-c)
        for i in range(1,len(vals)-1):
            max_concavity_violation = max(
                max_concavity_violation,
                vals[i-1]+vals[i+1]-2*vals[i])
        case_count += 1
print(f"grid cases={case_count}, points/case={len(grid)}")
print(f"max(g-C)={max_majorant_violation:.3e}")
print(f"max discrete concavity violation={max_concavity_violation:.3e}")
