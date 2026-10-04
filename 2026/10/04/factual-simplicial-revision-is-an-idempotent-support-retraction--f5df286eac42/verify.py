#!/usr/bin/env python3
from itertools import product

def overlap(f, g):
    return sum(x == y for x, y in zip(f, g))

def near_select(f, phi, a):
    candidates = [g for g in phi if g[a] == f[a]]
    if not candidates:
        return set()
    best = max(overlap(f, g) for g in candidates)
    return {g for g in candidates if overlap(f, g) == best}

def update_near(beliefs, phi):
    out = []
    for a, Sa in enumerate(beliefs):
        T = set()
        for f in Sa:
            T |= near_select(f, phi, a)
        out.append(frozenset(T))
    return tuple(out)

def update_grove(beliefs, phi):
    out = []
    for a, Sa in enumerate(beliefs):
        T = set()
        for f in Sa:
            internal = {g for g in Sa if g in phi and g[a] == f[a]}
            if internal:
                T |= internal
            else:
                T |= near_select(f, phi, a)
        out.append(frozenset(T))
    return tuple(out)

def fixed_criterion(beliefs, phi):
    return all(set(Sa) <= set(phi) for Sa in beliefs)

# Exhaustive two-agent binary-perspective universe.
facets2 = tuple(product(range(2), repeat=2))
subsets2 = [
    frozenset(f for i, f in enumerate(facets2) if (mask >> i) & 1)
    for mask in range(1 << len(facets2))
]

for phi in subsets2:
    for S0 in subsets2:
        for S1 in subsets2:
            beliefs = (S0, S1)
            for upd in (update_near, update_grove):
                once = upd(beliefs, phi)
                # Support success.
                assert all(set(Sa) <= set(phi) for Sa in once)
                # Exact fixed-point criterion.
                assert (once == beliefs) == fixed_criterion(beliefs, phi)
                # Idempotence.
                assert upd(once, phi) == once

# Exhaustive entailment absorption on the same universe.
for psi in subsets2:
    for phi in subsets2:
        if not set(psi) <= set(phi):
            continue
        for S0 in subsets2:
            for S1 in subsets2:
                beliefs = (S0, S1)
                for upd in (update_near, update_grove):
                    after_psi = upd(beliefs, psi)
                    assert upd(after_psi, phi) == after_psi

# Deterministic sampled three-agent checks.
facets3 = tuple(product(range(2), repeat=3))
samples = []
for mask in range(0, 1 << len(facets3), 17):
    samples.append(frozenset(f for i, f in enumerate(facets3) if (mask >> i) & 1))
samples.extend([frozenset(), frozenset(facets3)])
samples = tuple(dict.fromkeys(samples))

for phi in samples:
    for S0 in samples:
        for S1 in samples[:8]:
            for S2 in samples[:6]:
                beliefs = (S0, S1, S2)
                for upd in (update_near, update_grove):
                    once = upd(beliefs, phi)
                    assert all(set(Sa) <= set(phi) for Sa in once)
                    assert (once == beliefs) == fixed_criterion(beliefs, phi)
                    assert upd(once, phi) == once

print("VERIFY_OK")
