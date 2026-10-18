#!/usr/bin/env python3
"""Self-contained verification of reduced rational Betti numbers via mod-2 bounds."""
from collections import Counter

V = tuple(range(1, 8))
incidences = [(p, ell) for ell in V for p in V if ((p & ell).bit_count() & 1) == 0]
assert len(incidences) == 21
# A mask is a matching when each endpoint is used at most once.
by_size = [[0]]
for size in range(1, 8):
    new = []
    for mask in by_size[-1]:
        occupied_points = occupied_lines = 0
        for i, (p, ell) in enumerate(incidences):
            if mask & (1 << i):
                occupied_points |= 1 << p
                occupied_lines |= 1 << ell
        for i in range(mask.bit_length(), 21):
            p, ell = incidences[i]
            if not (occupied_points & (1 << p) or occupied_lines & (1 << ell)):
                new.append(mask | (1 << i))
    assert len(new) == len(set(new))
    by_size.append(new)
assert tuple(map(len, by_size)) == (1, 21, 168, 644, 1218, 1050, 336, 24)

# Exact reduction of columns over the field of two elements.
def rank(columns):
    pivot = {}
    for column in columns:
        while column:
            leading = column.bit_length() - 1
            if leading not in pivot:
                pivot[leading] = column
                break
            column ^= pivot[leading]
    return len(pivot)

ranks = [0]
for degree in range(1, 8):
    row_indices = {mask: j for j, mask in enumerate(by_size[degree - 1])}
    boundary_cols = []
    for mask in by_size[degree]:
        col = 0
        for i in range(21):
            if mask & (1 << i):
                col ^= 1 << row_indices[mask ^ (1 << i)]
        boundary_cols.append(col)
    ranks.append(rank(boundary_cols))
assert ranks[1:] == [1, 20, 148, 496, 722, 312, 24]
mod2_betti = [len(by_size[k]) - ranks[k] - (ranks[k + 1] if k < 7 else 0) for k in range(1, 8)]
assert mod2_betti == [0, 0, 0, 0, 16, 0, 0]
reduced_euler = sum((-1) ** (k - 1) * len(masks) for k, masks in enumerate(by_size))
assert reduced_euler == 16
print('OK: 3461 nonempty faces; exact mod-2 ranks and reduced Euler characteristic.')
print('The universal coefficient bound and Euler characteristic force rational H_4 = Q^16 only.')
