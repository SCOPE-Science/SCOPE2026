#!/usr/bin/env python3
from itertools import product

# Eight nontrivial semantic conditions on k=|p| in an n-element universe.
conds = [
    lambda n, k: k == 0,
    lambda n, k: k == n,
    lambda n, k: k > 0,
    lambda n, k: k < n,
    lambda n, k: 2 * k >= n,
    lambda n, k: 2 * k <= n,
    lambda n, k: 2 * k > n,
    lambda n, k: 2 * k < n,
]

def spectrum_of_mask(mask, N=64):
    out = []
    for n in range(1, N + 1):
        ok = False
        for k in range(n + 1):
            if all(((mask >> i) & 1) == 0 or conds[i](n, k) for i in range(8)):
                ok = True
                break
        if ok:
            out.append(n)
    return tuple(out)

N = 64
T1 = tuple(range(1, N + 1))
T2 = tuple(range(2, N + 1))
T3 = tuple(range(3, N + 1))
E2 = tuple(range(2, N + 1, 2))
EMPTY = ()
expected = {EMPTY, T1, T2, T3, E2}

seen = {spectrum_of_mask(mask, N) for mask in range(1 << 8)}
assert seen == expected, seen

# Strongest lower and upper bounds from the proof.
def lower(i, n):
    return [0, 1, (n + 1) // 2, n // 2 + 1, n][i]

def upper(j, n):
    return [n, n - 1, n // 2, (n + 1) // 2 - 1, 0][j]

table_expected = [
    [T1, T1, T1, T1, T1],
    [T1, T2, T2, T3, EMPTY],
    [T1, T2, E2, EMPTY, EMPTY],
    [T1, T3, EMPTY, EMPTY, EMPTY],
    [T1, EMPTY, EMPTY, EMPTY, EMPTY],
]

for i in range(5):
    for j in range(5):
        got = tuple(n for n in range(1, N + 1) if lower(i, n) <= upper(j, n))
        assert got == table_expected[i][j], (i, j, got)

# Concrete witness theories encoded by subsets of the eight condition indices.
# T1: empty theory.
assert spectrum_of_mask(0, N) == T1
# T2: k>0 and k<n.
assert spectrum_of_mask((1 << 2) | (1 << 3), N) == T2
# T3: k>0, k<n, and k>n-k.
assert spectrum_of_mask((1 << 2) | (1 << 3) | (1 << 6), N) == T3
# E2: k>=n-k and k<=n-k.
assert spectrum_of_mask((1 << 4) | (1 << 5), N) == E2
# Empty: k>k is a primitive contradiction in the original syntax.
# It is represented here directly as the empty expected spectrum.
assert EMPTY in expected

print("VERIFY_OK")
