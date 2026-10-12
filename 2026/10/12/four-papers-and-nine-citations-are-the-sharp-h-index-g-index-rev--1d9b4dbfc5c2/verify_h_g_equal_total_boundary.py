#!/usr/bin/env python3
from itertools import combinations


def profiles(n, total, cap=None):
    if cap is None:
        cap = total
    if n == 0:
        if total == 0:
            yield ()
        return
    for x in range(min(cap, total), -1, -1):
        for tail in profiles(n - 1, total - x, x):
            yield (x,) + tail


def h_index(c):
    h = 0
    for r, x in enumerate(c, 1):
        if x >= r:
            h = r
    return h


def g_index(c):
    g = 0
    s = 0
    for r, x in enumerate(c, 1):
        s += x
        if s >= r * r:
            g = r
    return g


def reversals(ps):
    out = []
    for a, b in combinations(ps, 2):
        ha, ga = h_index(a), g_index(a)
        hb, gb = h_index(b), g_index(b)
        if (ha - hb) * (ga - gb) < 0:
            out.append((a, b, (ha, ga), (hb, gb)))
    return out

# The standard inequality h <= g, exhaustively replayed on a broad finite grid.
for n in range(1, 9):
    for total in range(0, 31):
        for c in profiles(n, total):
            assert h_index(c) <= g_index(c)

# No equal-total reversal below nine citations, for all profile lengths replayed here.
for n in range(1, 9):
    for total in range(0, 9):
        assert not reversals(list(profiles(n, total)))

# For at most three papers there is no reversal on a much larger citation window.
# The report supplies the symbolic all-total proof.
for n in range(1, 4):
    for total in range(0, 61):
        assert not reversals(list(profiles(n, total)))

# Sharp unrestricted first layer: four papers, nine citations.
p49 = list(profiles(4, 9))
r49 = reversals(p49)
assert len(r49) == 15
h1g3 = sorted([p for p in p49 if (h_index(p), g_index(p)) == (1, 3)], reverse=True)
h2g2 = sorted([p for p in p49 if (h_index(p), g_index(p)) == (2, 2)], reverse=True)
assert h1g3 == [(9,0,0,0), (8,1,0,0), (7,1,1,0)]
assert h2g2 == [(5,2,1,1), (4,3,1,1), (4,2,2,1), (3,3,2,1), (3,2,2,2)]
assert {(a,b) for a,b,_,_ in r49} == {(x,y) for x in h1g3 for y in h2g2}

# A simple displayed witness.
A = (3,2,2,2)
B = (7,1,1,0)
assert sum(A) == sum(B) == 9
assert (h_index(A), g_index(A)) == (2,2)
assert (h_index(B), g_index(B)) == (1,3)

# Strictly positive citation profiles: nine total citations still cannot reverse.
for n in range(1, 10):
    ps = [p for p in profiles(n, 9) if p and p[-1] >= 1]
    assert not reversals(ps)

# First positive layer: four papers, ten citations, exactly two pairs.
p410 = [p for p in profiles(4, 10) if p[-1] >= 1]
r410 = reversals(p410)
assert len(r410) == 2
assert {(a,b) for a,b,_,_ in r410} == {
    ((7,1,1,1),(4,2,2,2)),
    ((7,1,1,1),(3,3,2,2)),
}

# Zero-padding preserves the unrestricted witness for every paper count >= 4.
for n in range(4, 101):
    aa = A + (0,) * (n - 4)
    bb = B + (0,) * (n - 4)
    assert sum(aa) == sum(bb) == 9
    assert (h_index(aa), g_index(aa)) == (2,2)
    assert (h_index(bb), g_index(bb)) == (1,3)

print('VERIFY_OK')
print('unrestricted_first_boundary', {'papers':4,'total_citations':9,'reversal_pairs':len(r49)})
print('h1_g3_profiles', h1g3)
print('h2_g2_profiles', h2g2)
print('positive_first_boundary', {'papers':4,'total_citations':10,'reversal_pairs':len(r410)})
print('displayed_witness', A, B)
print('zero_padding_checked_through_papers', 100)
