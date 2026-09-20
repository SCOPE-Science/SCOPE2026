#!/usr/bin/env python3
"""Numerical checks for the ELCD entropy-minimizer formulas."""
import math
import random

GAMMA = 1.4


def entropy(rho, p, c=0.0):
    return -rho / (GAMMA - 1.0) * math.log(p / rho**GAMMA) + c * rho


def rho_stationary(p, c=0.0):
    return math.exp(-1.0) * p ** (1.0 / GAMMA) * math.exp(-(GAMMA - 1.0) * c / GAMMA)


def rectangle_minimum(r1, r2, p1, p2, c=0.0):
    lo, hi = sorted((r1, r2))
    p = max(p1, p2)
    r = min(max(rho_stationary(p, c), lo), hi)
    return r, p, entropy(r, p, c)


def corner_minimum(r1, r2, p1, p2, c=0.0):
    pts = [(r1, p1), (r2, p2), (r1, p2), (r2, p1)]
    vals = [entropy(r, p, c) for r, p in pts]
    i = min(range(4), key=lambda j: vals[j])
    return pts[i][0], pts[i][1], vals[i]


# Configuration 3 state pair from arXiv:2609.19838v1.
r1, p1 = 0.5323, 0.3
r2, p2 = 0.138, 0.029
exact = rectangle_minimum(r1, r2, p1, p2)
corner = corner_minimum(r1, r2, p1, p2)
print("benchmark_exact", *exact)
print("benchmark_corner", *corner)
print("benchmark_entropy_excess", corner[2] - exact[2])
print("benchmark_sound_speed_corner", math.sqrt(GAMMA * corner[1] / corner[0]))
print("benchmark_sound_speed_exact", math.sqrt(GAMMA * exact[1] / exact[0]))

# Verify that an affine mass shift can place the stationary density at any target.
target = 0.4
base = rho_stationary(0.3)
c_target = -(GAMMA / (GAMMA - 1.0)) * math.log(target / base)
print("target_shift_c", c_target)
print("target_shift_stationary_density", rho_stationary(0.3, c_target))
print("corner_at_c_plus_20", *corner_minimum(r1, r2, p1, p2, 20.0)[:2])
print("corner_at_c_minus_20", *corner_minimum(r1, r2, p1, p2, -20.0)[:2])

# Deterministic random rectangles: compare the formula against a dense rho grid.
random.seed(260919838)
max_formula_minus_grid = 0.0
interior_count = 0
for _ in range(200):
    rr1 = 10 ** random.uniform(-2.0, 1.0)
    rr2 = 10 ** random.uniform(-2.0, 1.0)
    pp1 = 10 ** random.uniform(-2.0, 1.0)
    pp2 = 10 ** random.uniform(-2.0, 1.0)
    rho, p, value = rectangle_minimum(rr1, rr2, pp1, pp2)
    lo, hi = sorted((rr1, rr2))
    pmax = max(pp1, pp2)
    r0 = rho_stationary(pmax)
    if lo < r0 < hi:
        interior_count += 1
    grid_best = float("inf")
    for j in range(20001):
        r = lo + (hi - lo) * j / 20000.0
        grid_best = min(grid_best, entropy(r, pmax))
    max_formula_minus_grid = max(max_formula_minus_grid, value - grid_best)
print("random_interior_count", interior_count)
print("random_rectangle_count", 200)
print("max_formula_minus_grid", max_formula_minus_grid)

# Exact entropy-gap identity in the benchmark interior case.
rstar = rho_stationary(0.3)
r = 0.138
gap_formula = GAMMA / (GAMMA - 1.0) * (r * math.log(r / rstar) - r + rstar)
gap_direct = entropy(r, 0.3) - entropy(rstar, 0.3)
print("gap_formula", gap_formula)
print("gap_direct", gap_direct)
print("gap_abs_difference", abs(gap_formula - gap_direct))
