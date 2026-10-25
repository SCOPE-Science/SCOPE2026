"""Recheck every five-bit insertion optimum and its reversal/complement orbit."""
import csv
from collections import Counter
from pathlib import Path

N = 5

def subseq(x, y, nx=5, ny=7):
    i = 0
    for j in range(ny - 1, -1, -1):
        if i < nx and (x >> (nx - 1 - i)) & 1 == (y >> j) & 1:
            i += 1
    return i == nx

def rev(x):
    z = 0
    for _ in range(N):
        z = (z << 1) | (x & 1)
        x >>= 1
    return z

def transform(mask, fun):
    return sum(1 << fun(x) for x in range(1 << N) if mask >> x & 1)

def orbit(mask):
    return {transform(mask, f) for f in (lambda x: x, rev, lambda x: 31 - x, lambda x: rev(31 - x))}

path = Path(__file__).resolve().parent / 'maxima_n5_ins.csv'
with path.open(newline='', encoding='utf-8') as f:
    rows = list(csv.DictReader(f))
assert len(rows) == 185
masks = [int(r['codebook_mask_hex'], 16) for r in rows]
assert len(set(masks)) == len(masks)
assert masks == sorted(masks)
incidence = [sum(1 << x for x in range(32) if subseq(x, y)) for y in range(128)]
classes = {}
for row, mask in zip(rows, masks):
    assert mask.bit_count() == 6
    assert all((mask & incidence_y).bit_count() <= 2 for incidence_y in incidence)
    orb = orbit(mask)
    assert orb <= set(masks)
    rep = min(orb)
    assert int(row['orbit_representative_mask_hex'], 16) == rep
    assert int(row['orbit_size']) == len(orb)
    classes[rep] = orb
assert len(classes) == 52
assert Counter(map(len, classes.values())) == {1: 1, 2: 10, 4: 41}
assert set().union(*classes.values()) == set(masks)
print('ORBIT_VERIFIED codebooks=185 orbits=52 sizes=1:1,2:10,4:41')
