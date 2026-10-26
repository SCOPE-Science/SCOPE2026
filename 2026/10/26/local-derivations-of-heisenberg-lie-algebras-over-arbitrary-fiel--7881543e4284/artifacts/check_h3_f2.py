"""Exhaustive small-case check for the 3D Heisenberg Lie algebra over F_2.

This finite check corroborates, but does not replace, the symbolic proof for
all dimensions and all fields in RESULT.md.
"""
from itertools import product

VECTORS = list(product((0, 1), repeat=3))
ZERO = (0, 0, 0)

def add(u, v):
    return tuple(a ^ b for a, b in zip(u, v))

def bracket(u, v):
    return (0, 0, (u[0] & v[1]) ^ (u[1] & v[0]))

def apply_map(columns, v):
    out = ZERO
    for i, bit in enumerate(v):
        if bit:
            out = add(out, columns[i])
    return out

basis = [tuple(1 if i == j else 0 for i in range(3)) for j in range(3)]
all_maps = product(VECTORS, repeat=3)
derivations = []
for columns in all_maps:
    valid = True
    for e_i in basis:
        for e_j in basis:
            lhs = apply_map(columns, bracket(e_i, e_j))
            rhs = add(bracket(apply_map(columns, e_i), e_j),
                      bracket(e_i, apply_map(columns, e_j)))
            if lhs != rhs:
                valid = False
                break
        if not valid:
            break
    if valid:
        derivations.append(columns)

all_maps = product(VECTORS, repeat=3)
local_maps = []
for columns in all_maps:
    if all(any(apply_map(d, x) == apply_map(columns, x) for d in derivations)
           for x in VECTORS):
        local_maps.append(columns)

center_preserving = [columns for columns in product(VECTORS, repeat=3)
                     if columns[2][0] == 0 and columns[2][1] == 0]
assert len(derivations) == 64
assert len(local_maps) == 128
assert len(center_preserving) == 128
assert set(local_maps) == set(center_preserving)
print("PASS: derivations=64; local_derivations=128; center_preserving=128; sets_equal=True")
