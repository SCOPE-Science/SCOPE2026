#!/usr/bin/env python3
from itertools import product

def active_targets(R):
    return {v for (u, v) in R}

def update_by_truth(R, S):
    return {(u, v) for (u, v) in R if v in S}

# Exhaustive check of the combinatorial invariant on all one-agent
# relations and all possible target truth sets through four states.
for n in range(1, 5):
    pairs = [(u, v) for u in range(n) for v in range(n)]
    for mask in range(1 << len(pairs)):
        R = {e for k, e in enumerate(pairs) if (mask >> k) & 1}
        T = active_targets(R)
        for smask in range(1 << n):
            S = {v for v in range(n) if (smask >> v) & 1}
            R2 = update_by_truth(R, S)
            T2 = active_targets(R2)
            assert T2 <= T
            if R2 != R:
                assert T2 < T

def phi_truth_cycle(R, p_true, n):
    outgoing = {u: False for u in range(n)}
    for u, v in R:
        outgoing[u] = True
    # phi = p and not Box bottom; not Box bottom means at least one successor.
    return {u for u in range(n) if u in p_true and outgoing[u]}

# Sharpness family.
for n in range(1, 13):
    R = {(j, (j + 1) % n) for j in range(n)}
    p_true = set(range(n - 1))
    initial_targets = active_targets(R)
    assert len(initial_targets) == n

    strict = 0
    while True:
        S = phi_truth_cycle(R, p_true, n)
        R2 = update_by_truth(R, S)
        if R2 == R:
            break
        strict += 1
        assert len(active_targets(R2)) == n - strict
        R = R2

    assert strict == n
    assert len(R) == 0

print("VERIFY_OK")
