#!/usr/bin/env python3
"""Exact refutation of the cross-polytope vs box tradeoff claim (lane-1246).

Theory (proved in output/DRAFT.md):
  N = 256*l. Box S_box = [-g1,g1]^N. Cross-polytope C = {||y||_1 <= R},
  Vol(C) = (2R)^N/N!, so equal-volume calibration gives R = g1*(N!)^{1/N}.
  Single-spike shift v = beta*e_1 (inf-norm exactly beta, realizable as Sc):
    delta_box  = 1 - beta/(2*g1)                       (exact)
    delta_cross = (1 - beta/(2R))^N                    (exact, slice integration)
  Renyi-2 (accepted || ideal) = -log(delta) for both schemes, since the
  accepted law is uniform over the overlap region. So divergence comparison
  is equivalent to reversed acceptance comparison.

Instance: l=4 -> N=1024, g1=2^17, beta=240 (tau=60, eta=4), alpha=2.
Verifies with Robbins-certified (N!)^{1/N} bracket:
  ratio = delta_cross/delta_box < 1.5  (acceptance conjunct FAILS)
  R_cross > R_box                      (divergence conjunct FAILS)
Includes an independent Monte Carlo cross-check of delta_cross.
"""
import math
import random

N = 1024
G1 = 2**17
BETA = 240

# --- Robbins-certified bracket for M = (N!)^{1/N} ---
log_fact = math.fsum(math.log(k) for k in range(1, N + 1))
stir = N * math.log(N) - N + 0.5 * math.log(2 * math.pi * N)
r_lo, r_hi = 1.0 / (12 * N + 1), 1.0 / (12 * N)
assert stir + r_lo < log_fact < stir + r_hi, "Robbins bracket failed"
M_lo = math.exp((stir + r_lo) / N)
M_hi = math.exp((stir + r_hi) / N)
M = math.exp(log_fact / N)
print(f"M = (N!)^(1/N) in [{M_lo:.9f}, {M_hi:.9f}], width {M_hi - M_lo:.2e}")
R = G1 * M
print(f"R = {R:.6f}")

# --- exact acceptance + Renyi values ---
x = BETA / (2 * G1)                      # exact rational
delta_box = 1 - x
R_box = -math.log(delta_box)
u_hi = BETA / (2 * G1 * M_lo)            # certified upper bound on beta/(2R)
u = BETA / (2 * R)
delta_cross = (1 - u) ** N
R_cross = -N * math.log(1 - u)
ratio = delta_cross / delta_box
# certified bounds (monotone in u): ratio upper, R_cross lower
ratio_ub = (1 - (BETA / (2 * G1 * M_hi))) ** N / delta_box
R_cross_lb = -N * math.log(1 - (BETA / (2 * G1 * M_hi)))
print(f"\ndelta_box  = {delta_box:.12f}")
print(f"R_box (a=2) = {R_box:.12f}")
print(f"delta_cross = {delta_cross:.12f}  (certified <= {ratio_ub * delta_box:.12f})")
print(f"R_cross (a=2) >= {R_cross_lb:.12f}")
print(f"ratio delta_cross/delta_box = {ratio:.12f} (certified upper {(ratio_ub):.12f})")
assert ratio_ub < 1.0 < 1.5, "acceptance conjunct must fail"
assert R_cross_lb > R_box, "divergence conjunct must fail"
print("\nBOTH conjuncts REFUTED: ratio < 1 (need >=1.5); R_cross > R_box (need <=).")

# --- Monte Carlo cross-check of delta_cross ---
random.seed(1246)
T = 200000
acc = 0
for _ in range(T):
    E = [random.expovariate(1.0) for _ in range(N)]
    S = sum(E)
    r = R * (random.random() ** (1.0 / N))
    # only y_1 sign/magnitude and the l1-rest matter for the shift test
    y1 = (r * E[0] / S) * (1 if random.random() < 0.5 else -1)
    rest = r - r * E[0] / S
    if abs(y1 + BETA) + rest <= R:
        acc += 1
mc = acc / T
se = math.sqrt(mc * (1 - mc) / T)
print(f"\nMC delta_cross = {mc:.6f} +- {se:.6f}  vs exact {delta_cross:.6f}")
assert abs(mc - delta_cross) < 5 * se + 1e-9
print("MC cross-check PASSED.")
