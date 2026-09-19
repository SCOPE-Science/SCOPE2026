#!/usr/bin/env python3
"""Verification checks for exact parity reduction in modular Laplacian dynamics."""

from itertools import product

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def laplacian(state, mask):
    keys = set(state)
    for p in list(state):
        for v in mask:
            keys.add((p[0] - v[0], p[1] - v[1]))
            keys.add(add(p, v))
    out = {}
    d = len(mask)
    for p in keys:
        x = sum(state.get(add(p, v), 0) for v in mask) - d * state.get(p, 0)
        if x:
            out[p] = x
    return out

def reduce_mod(state, k):
    return {p: x % k for p, x in state.items() if x % k}

def step(state, mask, k):
    return reduce_mod(laplacian(state, mask), k)

def binary(state, mask):
    return step(state, mask, 2)

def xor_states(a, b):
    keys = set(a) | set(b)
    return {p: 1 for p in keys if (a.get(p, 0) ^ b.get(p, 0)) & 1}

def boundary(state, mask):
    out = {}
    for p, val in state.items():
        if val & 1 and any((state.get(add(p, v), 0) & 1) == 0 for v in mask):
            out[p] = 1
    return out

def bpower(state, mask, r):
    cur = {p: v & 1 for p, v in state.items() if v & 1}
    for _ in range(r):
        cur = binary(cur, mask)
    return cur

def closed_backward_neighborhood(S, mask, r):
    cur = set(S)
    vectors = [(0, 0)] + [(-v[0], -v[1]) for v in mask]
    for _ in range(r):
        cur = {add(p, v) for p in cur for v in vectors}
    return cur

masks = [
    [(1, 0), (-1, 0)],
    [(1, 0), (0, 1), (-1, 0)],
    [(1, 0), (-1, 0), (0, 1), (0, -1)],
    [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1)],
]
binary_seeds = [
    {(0, 0): 1},
    {(0, 0): 1, (1, 0): 1, (0, 1): 1},
    {(x, y): 1 for x, y in product(range(-1, 2), repeat=2) if (x + 2*y) % 3 != 0},
]
integer_seeds = binary_seeds + [
    {(0, 0): 5, (1, 0): 2, (0, 1): 7, (-1, 1): 3},
]

even_scalar_checks = 0
for k in (2, 4, 6, 8, 10, 12):
    for x in range(-40, 41):
        assert ((x % k) & 1) == (x & 1)
        even_scalar_checks += 1

large_modulus_scalar_checks = 0
for d in range(1, 13):
    for k in range(d + 1, d + 9):
        eps = k & 1
        for x in range(-d, d + 1):
            lhs = (x % k) & 1
            rhs = ((x & 1) ^ (eps if x < 0 else 0))
            assert lhs == rhs
            large_modulus_scalar_checks += 1

even_erasure_checks = 0
for mask in masks:
    for u in integer_seeds:
        pure_two = binary(binary(u, mask), mask)
        for k in (2, 4, 6, 8, 10):
            assert binary(step(u, mask, k), mask) == pure_two
            even_erasure_checks += 1

boundary_formula_checks = 0
localization_checks = 0
for mask in masks:
    d = len(mask)
    for u in binary_seeds:
        Lu = laplacian(u, mask)
        neg = {p: 1 for p, x in Lu.items() if x < 0}
        bd = boundary(u, mask)
        assert neg == bd
        B2u = binary(binary(u, mask), mask)
        for k in range(d + 1, d + 7):
            eps = k & 1
            K = step(u, mask, k)
            first_binary = binary(K, mask)
            rhs = B2u if eps == 0 else xor_states(B2u, binary(bd, mask))
            assert first_binary == rhs
            assert set(K) == set(Lu)
            boundary_formula_checks += 1
        odd_k = next(k for k in range(d + 1, d + 10) if k & 1)
        even_k = next(k for k in range(d + 1, d + 10) if not (k & 1))
        for r in range(1, 5):
            odd = bpower(step(u, mask, odd_k), mask, r)
            even = bpower(step(u, mask, even_k), mask, r)
            diff = xor_states(odd, even)
            expected = bpower(bd, mask, r)
            assert diff == expected
            assert set(diff) <= closed_backward_neighborhood(set(bd), mask, r)
            localization_checks += 1

mask = [(1, 0), (-1, 0), (0, 1), (0, -1)]
u0 = binary_seeds[2]

def simulate_schedule(k, s, cycles):
    block = [2, k] + [2] * s
    state = dict(u0)
    states, mods = [], []
    for t in range(cycles * len(block)):
        mod = block[t % len(block)]
        state = step(state, mask, mod)
        states.append(state)
        mods.append(mod)
    return states, mods

schedule_checks = 0
for s in range(4):
    odd_runs = [simulate_schedule(k, s, 7) for k in (5, 7, 9)]
    even_runs = [simulate_schedule(k, s, 7) for k in (4, 6, 8)]
    for runs in (odd_runs,):
        for i in range(1, len(runs)):
            for t, mod in enumerate(runs[0][1]):
                assert set(runs[i][0][t]) == set(runs[0][0][t])
                if mod == 2:
                    assert runs[i][0][t] == runs[0][0][t]
                schedule_checks += 1
    pure = dict(u0)
    pure_states = []
    T = len(even_runs[0][0])
    for _ in range(T):
        pure = binary(pure, mask)
        pure_states.append(pure)
    for states, mods in even_runs:
        for t, mod in enumerate(mods):
            if mod == 2:
                assert states[t] == pure_states[t]
                schedule_checks += 1

print(f"even_scalar_checks={even_scalar_checks}")
print(f"large_modulus_scalar_checks={large_modulus_scalar_checks}")
print(f"even_erasure_checks={even_erasure_checks}")
print(f"boundary_formula_and_support_checks={boundary_formula_checks}")
print(f"boundary_localization_checks={localization_checks}")
print(f"periodic_schedule_checks={schedule_checks}")
print("all_checks_passed=True")
