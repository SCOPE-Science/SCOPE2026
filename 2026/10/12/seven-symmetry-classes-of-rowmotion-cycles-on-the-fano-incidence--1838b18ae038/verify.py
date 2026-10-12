#!/usr/bin/env python3
"""Exact rowmotion and projective-symmetry classification for the Fano incidence poset.

No third-party dependencies. To replay: python3 verify.py
The seven representative masks index points 1,...,7 in bits 0,...,6 and
lines, in sorted triple order, in bits 7,...,13.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
import csv

POINTS = tuple(range(1, 8))
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b)))
                      for a in POINTS for b in POINTS if a < b}))
assert len(LINES) == 7 and all(len(s) == 3 for s in LINES)
P_MASK = (1 << 7) - 1
PREDS = tuple(sum(1 << (p - 1) for p in ln) for ln in LINES)

# Represent an ideal as (point mask S, chosen-line mask T); every chosen
# line must be fully contained in S.
def compatible_lines(S):
    return sum(1 << j for j, p in enumerate(PREDS) if S & p == p)

IDEALS = tuple(S | (T << 7)
               for S in range(128)
               for C in [compatible_lines(S)]
               for T in range(128) if T & ~C == 0)
assert len(IDEALS) == 458 == len(set(IDEALS))
IDEAL_SET = set(IDEALS)

# Explicit rank-two incidence formula: newly minimal absent lines are C(S)\T.
def advance(mask):
    S = mask & P_MASK
    T = mask >> 7
    N = compatible_lines(S) & ~T
    U = (P_MASK ^ S)
    for j in range(7):
        if (N >> j) & 1:
            U |= PREDS[j]
    return U | (N << 7)

NEXT = {x: advance(x) for x in IDEALS}
assert set(NEXT.values()) == IDEAL_SET  # bijection

cycles = []
cycle_id = {}
for x in IDEALS:
    if x in cycle_id:
        continue
    seq = []
    y = x
    while y not in cycle_id:
        cycle_id[y] = len(cycles)
        seq.append(y)
        y = NEXT[y]
    assert y == x
    cycles.append(tuple(seq))
assert len(cycles) == 92
LENGTHS = Counter(map(len, cycles))
assert LENGTHS == {3: 29, 5: 35, 7: 28}
assert sum(k*v for k,v in LENGTHS.items()) == 458

# All invertible linear transformations over F_2^3 are determined by the
# images of a basis, with the third image outside the first two's span.
line_lookup = {frozenset(line): j for j, line in enumerate(LINES)}
GROUP = []
for a in POINTS:
    for b in POINTS:
        if b == a:
            continue
        for c in POINTS:
            if c in (a, b, a ^ b):
                continue
            perm = tuple(((a if p & 1 else 0)
                           ^ (b if p & 2 else 0)
                           ^ (c if p & 4 else 0)) - 1 for p in POINTS)
            lineperm = tuple(7 + line_lookup[frozenset(perm[p-1] + 1 for p in L)]
                             for L in LINES)
            GROUP.append(perm + lineperm)
assert len(GROUP) == 168 == len(set(GROUP))

def transform(mask, permutation):
    y = 0
    for j in range(14):
        if mask & (1 << j):
            y |= 1 << permutation[j]
    return y

for g in GROUP:
    for x in IDEALS:
        assert transform(x, g) in IDEAL_SET
        assert transform(NEXT[x], g) == NEXT[transform(x, g)]

# The group maps whole rowmotion cycles to whole cycles. Compute its
# seven orbits on the set of 92 cycles, with one integer representative.
classes = []
visited_cycles = set()
for cid, cy in enumerate(cycles):
    if cid in visited_cycles:
        continue
    image_ids = {cycle_id[transform(cy[0], g)] for g in GROUP}
    assert cid in image_ids
    assert not (image_ids & visited_cycles)
    visited_cycles |= image_ids
    length = len(cy)
    assert all(len(cycles[t]) == length for t in image_ids)
    # Pick the lexicographically smallest state among *all* cycles in class.
    rep = min(x for t in image_ids for x in cycles[t])
    classes.append((length, len(image_ids), rep, sorted(cycles[cycle_id[rep]])))
assert len(classes) == 7 and len(visited_cycles) == len(cycles)
assert sorted((d, n, rep) for d, n, rep, _ in classes) == [
    (3, 1, 0x0000), (3, 14, 0x009f), (3, 14, 0x01bf),
    (5, 7, 0x0001), (5, 7, 0x0007), (5, 21, 0x0003),
    (7, 28, 0x000b)]
assert Counter((d, n) for d, n, _, _ in classes) == Counter({
    (3, 1): 1, (3, 14): 2, (5, 7): 2, (5, 21): 1, (7, 28): 1
})

# Small exhaustive certificate: the seven explicit (cycle, symmetry) families
# are pairwise disjoint, each has the stated size, and exhaust all 458 ideals.
certificate_states = set()
for d, number, rep, _ in classes:
    path = []
    y = rep
    for _ in range(d):
        path.append(y)
        y = NEXT[y]
    assert y == rep
    members = {transform(t, g) for t in path for g in GROUP}
    assert len(members) == d * number
    assert members.isdisjoint(certificate_states)
    certificate_states.update(members)
assert certificate_states == IDEAL_SET

# Additional independent checks on orbit representatives under symmetry.
for d, number, rep, sequence in classes:
    orbit_under_row = []
    q = rep
    for _ in range(d):
        orbit_under_row.append(q)
        q = NEXT[q]
    assert q == rep and len(set(orbit_under_row)) == d
    assert number * d == len({transform(t, g)
                              for t in orbit_under_row for g in GROUP})

DATA_PATH = Path(__file__).with_name('orbit_types.csv')
with DATA_PATH.open('w', newline='', encoding='utf-8') as fh:
    writer = csv.writer(fh)
    writer.writerow(('rowmotion_cycle_length', 'number_of_cycles_in_PGL_orbit',
                     'representative_ideal_mask_hex', 'number_of_ideals', 'rowmotion_cycle_hex'))
    for d, n, rep, _ in sorted(classes):
        seq = []
        y = rep
        for _ in range(d):
            seq.append(f'0x{y:04x}')
            y = NEXT[y]
        assert y == rep
        writer.writerow((d, n, f'0x{rep:04x}', d*n, ' '.join(seq)))

print('VERIFY_OK points=7 lines=7 ideals=458 rowmotion_bijection=true')
print('VERIFY_OK cycles=3:29,5:35,7:28 order=105 total_cycles=92')
print('VERIFY_OK incidence_automorphisms=168 cycle_orbit_classes=7')
print('VERIFY_OK cycle_classes=3x1,3x14,3x14,5x7,5x7,5x21,7x28')
print('VERIFY_OK equivariance=all_458_ideals_x_168_transformations')
print('VERIFY_OK seven_cycle_certificates_disjoint_and_cover_all_458_ideals=true')
print('VERIFY_OK orbit_types.csv=generated')
