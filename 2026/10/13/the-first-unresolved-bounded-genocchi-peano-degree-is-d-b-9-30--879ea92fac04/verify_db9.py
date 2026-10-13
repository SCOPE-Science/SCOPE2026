#!/usr/bin/env python3
from itertools import combinations
from math import lcm
from fractions import Fraction

N = 9
M = 14
L = lcm(*range(1, M + 1))
assert L == 360360

total = 0
baseline_impossible = 0
residual_checked = 0
feasible = []

for ds in combinations(range(1, M + 1), N):
    total += 1
    weights = [L // d for d in ds]
    target = 2 * L - sum(weights)  # x_i = alpha_i - 1
    if target < 0:
        baseline_impossible += 1
        continue

    residual_checked += 1
    # Exact bounded-subset-sum bitset.  For each d, x ranges over 0,...,2d-2.
    bits = 1  # bit s is 1 iff sum s is reachable
    for d, w in zip(ds, weights):
        old = bits
        new = 0
        for x in range(2 * d - 1):
            new |= old << (x * w)
        bits = new & ((1 << (target + 1)) - 1)
    if (bits >> target) & 1:
        feasible.append(ds)

assert total == 2002
assert baseline_impossible == 1228
assert residual_checked == 774
assert feasible == []

# Explicit degree-30 witness.
ds = (2, 3, 4, 6, 7, 10, 12, 14, 15)
alphas = (1, 1, 1, 1, 1, 1, 1, 5, 1)
betas = tuple(2 * d for d in ds)
assert len(set(betas)) == N
assert max(betas) == 30
assert sum(Fraction(a, b) for a, b in zip(alphas, betas)) == 1
assert all(b % 2 == 0 for b in betas)
assert all(a > 0 for a in alphas)

print("VERIFY_OK")
print(f"L={L}")
print(f"denominator_sets={total}")
print(f"baseline_impossible={baseline_impossible}")
print(f"residual_checked={residual_checked}")
print("feasible_degree_le_28=0")
print("witness_betas=" + ",".join(map(str, betas)))
print("witness_alphas=" + ",".join(map(str, alphas)))
