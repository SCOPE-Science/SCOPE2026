#!/usr/bin/env python3
BOUND = 200000

sigma = [0] * (BOUND + 1)
for d in range(1, BOUND + 1):
    for n in range(d, BOUND + 1, d):
        sigma[n] += d

def is_power_of_three(x):
    if x < 1:
        return False
    while x % 3 == 0:
        x //= 3
    return x == 1

hits = [(n, sigma[n]) for n in range(1, BOUND + 1) if is_power_of_three(sigma[n])]
assert hits == [(1, 1), (2, 3)], hits

ray = []
for a in range(1, 9):
    N = 3 ** a
    best = max(k for k in range(1, N + 1) if N % sigma[k] == 0)
    ray.append((a, best))
assert all(best == 2 for _, best in ray), ray

print(f"VERIFY_OK bound={BOUND} inverse_hits={hits} ternary_ray={ray}")
