#!/usr/bin/env python3
"""Certified ML-DSA-44 witness for the equal-volume l1-ball vs box tradeoff."""
import math
N = 1024
GAMMA1 = 2**17
TAU = 39
ETA = 2
BETA = TAU * ETA  # 78, FIPS 204 ML-DSA-44

# Robbins bounds for log(N!)
stir = N*math.log(N)-N+0.5*math.log(2*math.pi*N)
lo = stir + 1.0/(12*N+1)
hi = stir + 1.0/(12*N)
log_fact = math.lgamma(N+1)
assert lo < log_fact < hi
M_lo, M_hi = math.exp(lo/N), math.exp(hi/N)
M = math.exp(log_fact/N)
R = GAMMA1*M
x = BETA/(2*GAMMA1)
u = BETA/(2*R)
delta_box = 1-x
delta_cross = (1-u)**N
D2_box = -math.log(delta_box)
D2_cross = -N*math.log1p(-u)
ratio = delta_cross/delta_box
print(f"M in [{M_lo:.12f}, {M_hi:.12f}], M={M:.12f}")
print(f"delta_box={delta_box:.16f}")
print(f"delta_cross={delta_cross:.16f}")
print(f"acceptance_ratio={ratio:.16f}")
print(f"D2_box={D2_box:.16f}")
print(f"D2_cross={D2_cross:.16f}")
print(f"D2_ratio={D2_cross/D2_box:.12f}")
assert ratio < 1.5
assert D2_cross > D2_box
# Analytic lower bound using M <= (N+1)/2.
lower = 2*N*(1-x)/(N+1)
print(f"analytic_D2_ratio_lower_bound={lower:.12f}")
assert lower > 1
