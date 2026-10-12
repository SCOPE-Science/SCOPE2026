"""Enumerate binary length-six (6,16,4) MDS symbol-pair codes.

Independent of the compatibility-clique enumerator, this script uses exact cover:
each word realizes one value for each cyclic adjacent two-coordinate erasure.
Requires only Python 3; it prints a compact checksum-free census and five orbit
representatives, with exhaustive assertions against the accompanying catalog.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path

N = 6
WORDS = range(1 << N)
KEEP = [tuple(k for k in range(N) if k not in (i, (i + 1) % N))
        for i in range(N)]
ROW = []
COL_ROWS = [[] for _ in range(96)]
for word in WORDS:
    cols = []
    for i, positions in enumerate(KEEP):
        value = sum(((word >> k) & 1) << j for j, k in enumerate(positions))
        cols.append(16 * i + value)
    row = sum(1 << c for c in cols)
    ROW.append(row)
    for c in cols:
        COL_ROWS[c].append(word)
FULL = (1 << 96) - 1
solutions = []
visits = 0

def exact_cover(used, selected):
    global visits
    visits += 1
    if used == FULL:
        assert len(selected) == 16
        solutions.append(tuple(sorted(selected)))
        return
    best = None
    for col in range(96):
        if (used >> col) & 1:
            continue
        possible = [v for v in COL_ROWS[col] if (ROW[v] & used) == 0]
        if not possible:
            return
        if best is None or len(possible) < len(best):
            best = possible
            if len(best) == 1:
                break
    for v in best:
        exact_cover(used | ROW[v], selected + [v])

def pair_distance(x, y):
    return sum(((x >> i) & 1, (x >> ((i + 1) % N)) & 1) !=
               ((y >> i) & 1, (y >> ((i + 1) % N)) & 1)
               for i in range(N))

def affine(code):
    base = code[0]
    members = set(code)
    return all((x ^ y ^ base) in members for x in code for y in code)

def transform(code, mask, step, start):
    # New bit i reads old bit at start+step*i, followed by a bitwise translation.
    mapped = []
    for word in code:
        t = sum(((word >> ((start + step * i) % N)) & 1) << i for i in range(N))
        mapped.append(t ^ mask)
    return tuple(sorted(mapped))

def orbit(code):
    return {transform(code, mask, step, start)
            for mask in WORDS for step in (1, -1) for start in range(N)}

exact_cover(0, [])
solutions.sort()
assert len(solutions) == len(set(solutions)) == 76
assert all(min(pair_distance(a, b) for a, b in combinations(code, 2)) == 4
           for code in solutions)
assert sum(affine(code) for code in solutions) == 44
assert sum(not affine(code) for code in solutions) == 32

# Reconstruct the five group orbits, under independent bit translations and
# dihedral permutations of the six cyclic positions.
all_codes = set(solutions)
remaining = set(solutions)
classes = []
while remaining:
    rep = min(remaining)
    images = orbit(rep)
    assert images <= all_codes
    remaining.difference_update(images)
    classes.append((len(images), affine(rep), rep))
classes.sort(key=lambda record: record[2])
assert sorted((size, aff) for size, aff, _ in classes) == sorted([
    (4, True), (32, False), (24, True), (12, True), (4, True)])

catalog_path = Path(__file__).with_name('pair6_codes.txt')
catalog = [tuple(map(int, line.split())) for line in catalog_path.read_text().splitlines()
           if line and not line.startswith('#')]
assert set(catalog) == all_codes, 'Catalog disagrees with exact-cover enumeration.'
assert len(catalog) == 76
print('EXACT_COVER_OK words=64 conditions=96 nodes=%s' % visits)
print('COUNT=76 AFFINE=44 NONAFFINE=32 ORBITS=5')
for size, is_affine, rep in classes:
    print('ORBIT size=%d affine=%s representative=%s' %
          (size, int(is_affine), ','.join(map(str, rep))))
