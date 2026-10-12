"""Exact finite-projective-plane stopping-set and erasure-decoding verifier.

Variables are the thirteen projective lines; checks are the thirteen points.
All arithmetic is exact in the prime field of three elements.
"""
import itertools
from collections import Counter
from math import comb
import csv
from pathlib import Path

Q = 3

def canonical(v):
    k = next(x for x in v if x)
    inv = pow(k, -1, Q)
    return tuple(x * inv % Q for x in v)

P = sorted({canonical(v) for v in itertools.product(range(Q), repeat=3) if any(v)})
assert len(P) == 13
# A coordinate vector labels a projective line when interpreted as a covector.
CHECK = [sum(1 << j for j, v in enumerate(P) if sum(x*y for x, y in zip(u, v)) % Q == 0) for u in P]
assert len(set(CHECK)) == 13 and all(r.bit_count() == 4 for r in CHECK)
assert all(sum(bool(r & (1 << j)) for r in CHECK) == 4 for j in range(13))
UNIVERSE = (1 << 13) - 1

# The dual point set is the set of projective line labels.
def is_stopping(mask):
    return all((mask & r).bit_count() != 1 for r in CHECK)


def peeling_fails(mask):
    rem = mask
    while rem:
        for row in CHECK:
            overlap = rem & row
            if overlap and not (overlap & (overlap - 1)):
                rem ^= overlap
                break
        else:
            return True
    return False


def class_name(selected):
    t = UNIVERSE ^ selected
    size = t.bit_count()
    complete = [row for row in CHECK if row & t == row]
    if size == 13:
        return 'dual_plane'
    if complete:
        if size == 7 and len(complete) == 2:
            return 'two_lines'
        if size == 5 and len(complete) == 1:
            return 'line_plus_point'
        if size == 4 and len(complete) == 1:
            return 'line'
        raise AssertionError(('unexpected complete-line case', size, len(complete)))
    if any((t & row).bit_count() >= 3 for row in CHECK):
        raise AssertionError('a dual complement with no complete line contains a collinear triple')
    return {0:'empty', 1:'point', 2:'two_points', 3:'triangle', 4:'quadrangle'}[size]

stop = {m for m in range(1 << 13) if is_stopping(m)}
scount = Counter(m.bit_count() for m in stop)
expected_stopping = {0:1, 6:78, 8:117, 9:247, 10:234, 11:78, 12:13, 13:1}
assert dict(scount) == expected_stopping
classes = Counter(class_name(m) for m in stop)
assert classes == Counter({'dual_plane':1, 'two_lines':78, 'line_plus_point':117,
                           'line':13, 'quadrangle':234, 'triangle':234,
                           'two_points':78, 'point':13, 'empty':1})

pair_unions = {r | s for r, s in itertools.combinations(CHECK, 2)}
assert len(pair_unions) == 78 and all(m.bit_count() == 7 for m in pair_unions)
minimum = {UNIVERSE ^ m for m in pair_unions}
assert minimum == {m for m in stop if m.bit_count() == 6}
assert all(any(m & b == b for b in minimum) for m in stop if m)

fails = set()
for mask in range(1 << 13):
    direct = peeling_fails(mask)
    covering = any(((UNIVERSE ^ mask) & union) == (UNIVERSE ^ mask) for union in pair_unions)
    assert direct == covering, ('failure theorem disagrees with peeling', mask)
    if direct:
        fails.add(mask)
expected_failures = {6:78, 7:546, 8:1287, 9:715, 10:286, 11:78, 12:13, 13:1}
assert dict(Counter(m.bit_count() for m in fails)) == expected_failures

# Enumerate every projective linear transformation, modulo scalar matrices.
perms = set()
for inds in itertools.product(range(13), repeat=3):
    abc = [P[i] for i in inds]
    a, b, c = abc
    determinant = (a[0]*(b[1]*c[2]-b[2]*c[1])
                   - a[1]*(b[0]*c[2]-b[2]*c[0])
                   + a[2]*(b[0]*c[1]-b[1]*c[0])) % 3
    if not determinant:
        continue
    for e, f in itertools.product((1,2), repeat=2):
        cols = (a, tuple(e*x % 3 for x in b), tuple(f*x % 3 for x in c))
        image = tuple(P.index(canonical(tuple(sum(cols[k][j]*v[k] for k in range(3)) % 3 for j in range(3)))) for v in P)
        perms.add(image)
assert len(perms) == 5616 and all(len(set(p)) == 13 for p in perms)
seen = set()
orbit_sizes = Counter()
for s in sorted(stop):
    if s in seen:
        continue
    orbit = {sum(1 << p[i] for i in range(13) if s & (1 << i)) for p in perms}
    assert orbit <= stop and not (orbit & seen)
    seen |= orbit
    orbit_sizes[(class_name(s), len(orbit))] += 1
assert seen == stop and len(orbit_sizes) == 9
with (Path(__file__).parent / 'orbits.csv').open(newline='', encoding='utf-8') as fh:
    reps = list(csv.DictReader(fh))
assert len(reps) == 9
listed = set()
for rec in reps:
    representative = int(rec['stopping_mask_hex'], 16)
    orbit = {sum(1 << p[i] for i in range(13) if representative & (1 << i)) for p in perms}
    assert representative in stop and len(orbit) == int(rec['orbit_size'])
    assert representative.bit_count() == int(rec['stopping_cardinality'])
    indices = ';'.join(str(i) for i in range(13) if not representative & (1 << i))
    assert indices == rec['complement_point_indices']
    assert not (listed & orbit)
    listed |= orbit
assert listed == stop

assert sorted(size for _,size in orbit_sizes) == [1,1,13,13,78,78,117,234,234]
print('VERIFY_OK plane=PG(2,3) 13_points 13_lines 4_each PGL=5616')
print('VERIFY_OK tested=8192 stopping=769 classes=9 full_polynomial='+','.join(f'{k}:{v}' for k,v in sorted(scount.items())))
print('VERIFY_OK nonempty_stopping_minimum=6 minimum_count=78 every_nonempty_contains_a_minimum=true')
print('VERIFY_OK all_peeling_patterns=8192 failure=3004 failure_polynomial='+','.join(f'{k}:{v}' for k,v in sorted(expected_failures.items())))
print('VERIFY_OK projective_classes='+','.join(f'{k}:{classes[k]}' for k in sorted(classes)))
