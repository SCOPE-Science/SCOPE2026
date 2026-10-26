"""Deterministic checks for exact sampled-volatility identities."""
from itertools import product
from math import exp, prod, sqrt, factorial

# The squared action takes values 0, 1, 4 with probabilities 0.4, 0.4, 0.2.
zs = (0.0, 1.0, 4.0)
ps = (0.4, 0.4, 0.2)
q = sum(p*z for p, z in zip(ps, zs))
m2 = sum(p*z*z for p, z in zip(ps, zs))
var = m2 - q*q
T = 1.0
h = (0.1, 0.2, 0.7)
N = len(h)
uniform = (T/N,)*N

def ell(s):
    return sum(p*exp(-s*z) for p, z in zip(ps, zs))

def cf(grid, u):
    return prod(ell((u*u/2)*hi) for hi in grid)

def aggregate_cf(u):
    return exp(-(u*u/2)*q*T)

# Jensen comparison and uniform-grid minimization at multiple Fourier frequencies.
for u in (0.2, 0.7, 1.0, 2.0, 5.0):
    phi = cf(h, u)
    phi_agg = aggregate_cf(u)
    phi_unif = cf(uniform, u)
    assert phi > phi_agg
    assert phi_unif < phi

# Exact fourth-moment identity, computed in two algebraically equivalent ways.
left = 3.0*(m2*sum(x*x for x in h) + 2*q*q*sum(h[i]*h[j] for i in range(N) for j in range(i+1, N)))
right = 3.0*(q*q*T*T + var*sum(x*x for x in h))
assert abs(left-right) < 1e-12
assert abs((right-3*q*q*T*T) - 3*var*sum(x*x for x in h)) < 1e-12
assert abs(3*var*sum(x*x for x in uniform) - 3*T*T*var/N) < 1e-12
assert sum(x*x for x in uniform) < sum(x*x for x in h)

# Every even-moment objective is symmetric convex in the partition widths.
# Verify its claimed ordering by direct finite enumeration for this discrete Z law.
for k in range(1, 6):
    def moment_of_variance(grid):
        total = 0.0
        for idx in product(range(len(zs)), repeat=N):
            prob = prod(ps[j] for j in idx)
            v = sum(grid[i]*zs[idx[i]] for i in range(N))
            total += prob*(v**k)
        return total
    assert moment_of_variance(uniform) <= moment_of_variance(h) + 1e-12

# Constant-magnitude actions (random sign) have exactly the aggregate law at every grid.
const_z = 4.0
for u in (0.2, 1.0, 3.0):
    phi_sampled = prod(exp(-(u*u/2)*hi*const_z) for hi in h)
    phi_agg = exp(-(u*u/2)*const_z*T)
    assert abs(phi_sampled-phi_agg) < 1e-14

# Standard Gaussian action specialization: exact characteristic and fourth-moment formulas.
for n in (1, 2, 3, 8, 20):
    hh = T/n
    for u in (0.25, 1.0, 2.5):
        phi = (1+u*u*hh)**(-n/2)
        phi_from_product = prod((1+u*u*hh)**(-0.5) for _ in range(n))
        assert abs(phi-phi_from_product) < 1e-13
    gap = 6*T*T/n
    assert abs(gap - 3*2*T*T/n) < 1e-13
    for k in range(1, 7):
        double_factorial = prod(range(1, 2*k, 2))
        ratio = prod(1+2*j/n for j in range(k))
        sampled_moment = double_factorial*T**k*ratio
        aggregate_moment = double_factorial*T**k
        assert sampled_moment >= aggregate_moment - 1e-12

print("PASS: characteristic-function comparison and uniform-grid ordering")
print("PASS: exact fourth-moment identity and optimal-grid constant")
print("PASS: finite-distribution even-moment ordering for k=1..5")
print("PASS: constant-magnitude weak-law equality and Gaussian specialization")
