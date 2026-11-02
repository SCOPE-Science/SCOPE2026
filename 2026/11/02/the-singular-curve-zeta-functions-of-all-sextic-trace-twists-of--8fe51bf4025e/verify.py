#!/usr/bin/env python3
"""Exact verification for the arithmetic singular curve of a trace Igusa quartic.
Uses only the Python standard library; no external files or network access.
"""
from collections import Counter
from itertools import combinations, permutations, product
from math import lcm

LABELS = tuple(range(6))
DUADS = tuple(combinations(LABELS, 2))

def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for b in vertices[1:]:
        rest = tuple(v for v in vertices if v != a and v != b)
        for m in matchings(rest):
            yield tuple(sorted(((a, b),) + m))

SYNTHEMES = tuple(sorted(set(matchings(LABELS))))
FLAGS = tuple((d, s) for d in DUADS for s in SYNTHEMES if d in s)
assert (len(DUADS), len(SYNTHEMES), len(FLAGS)) == (15, 15, 45)

def transform_duad(p, d):
    return tuple(sorted((p[d[0]], p[d[1]])))

def transform_syntheme(p, s):
    return tuple(sorted(transform_duad(p, d) for d in s))

def transform_flag(p, f):
    return (transform_duad(p, f[0]), transform_syntheme(p, f[1]))

DATA = (
    (DUADS, transform_duad),
    (SYNTHEMES, transform_syntheme),
    (FLAGS, transform_flag),
)

def cycle_type(p):
    seen = set()
    out = []
    for i in LABELS:
        if i in seen:
            continue
        j = i
        k = 0
        while j not in seen:
            seen.add(j)
            k += 1
            j = p[j]
        out.append(k)
    return tuple(sorted(out, reverse=True))

def cycle_counts(p, objects, action):
    remaining = set(objects)
    hist = Counter()
    while remaining:
        x = next(iter(remaining))
        y = x
        r = 0
        while y in remaining:
            remaining.remove(y)
            r += 1
            y = action(p, y)
        assert y == x
        hist[r] += 1
    return tuple(sorted(hist.items()))

def fixed_count(p, objects, action, exponent):
    total = 0
    for x in objects:
        y = x
        for _ in range(exponent):
            y = action(p, y)
        total += (y == x)
    return total

def from_hist(hist, n):
    return sum(d * c for d, c in hist if n % d == 0)

# Expected spectra on the 15 triple points, 15 singular lines, and 45 branches.
EXPECTED = {
    (1,1,1,1,1,1): (((1,15),),((1,15),),((1,45),)),
    (2,1,1,1,1): (((1,7),(2,4)),((1,3),(2,6)),((1,9),(2,18))),
    (2,2,1,1): (((1,3),(2,6)),((1,3),(2,6)),((1,5),(2,20))),
    (2,2,2): (((1,3),(2,6)),((1,7),(2,4)),((1,9),(2,18))),
    (3,1,1,1): (((1,3),(3,4)),((3,5),),((3,15),)),
    (3,2,1): (((1,1),(2,1),(3,2),(6,1)),((3,1),(6,2)),((3,3),(6,6))),
    (3,3): (((3,5),),((1,3),(3,4)),((3,15),)),
    (4,1,1): (((1,1),(2,1),(4,3)),((1,1),(2,1),(4,3)),((1,1),(2,2),(4,10))),
    (4,2): (((1,1),(2,1),(4,3)),((1,1),(2,1),(4,3)),((1,1),(2,2),(4,10))),
    (5,1): (((5,3),),((5,3),),((5,9),)),
    (6,): (((3,1),(6,2)),((1,1),(2,1),(3,2),(6,1)),((3,3),(6,6))),
}

partition_counts = Counter()
for perm in permutations(LABELS):
    typ = cycle_type(perm)
    partition_counts[typ] += 1
    spectra = tuple(cycle_counts(perm, *d) for d in DATA)
    assert spectra == EXPECTED[typ], (typ, spectra)
    for (objects, action), hist in zip(DATA, spectra):
        assert sum(d*c for d,c in hist) == len(objects)
        for n in range(1, 13):
            assert fixed_count(perm, objects, action, n) == from_hist(hist, n)
    assert lcm(*(d for d, _ in spectra[0] + spectra[1] + spectra[2])) == lcm(*typ)
assert sum(partition_counts.values()) == 720
assert len(partition_counts) == 11

# Check direct geometry of the split trace quartic in two odd characteristics.
def normalize_point(v, p):
    lead = next((x for x in v if x % p), None)
    if lead is None:
        return None
    inv = pow(lead, -1, p)
    return tuple((x * inv) % p for x in v)

def explicit_lines(q):
    lines = []
    for s in SYNTHEMES:
        pts = set()
        for u, v in product(range(q), repeat=2):
            w = (-u - v) % q
            x = [None] * 6
            for pair, val in zip(s, (u,v,w)):
                for i in pair:
                    x[i] = val
            pt = normalize_point(x, q)
            if pt is not None:
                pts.add(pt)
        assert len(pts) == q + 1
        lines.append(pts)
    return lines

def direct_singular_points(q):
    found = set()
    for free in product(range(q), repeat=5):
        x = tuple(free) + ((-sum(free)) % q,)
        x = normalize_point(x,q)
        if x is None or x in found:
            continue
        s2 = sum(a*a for a in x) % q
        s4 = sum(a**4 for a in x) % q
        if (s2*s2 - 4*s4) % q:
            continue
        grad = tuple((4*a*s2 - 16*a*a*a) % q for a in x)
        if len(set(grad)) == 1:
            found.add(x)
    return found

for q in (7, 11):
    lines = explicit_lines(q)
    assert len(set().union(*lines)) == 15*q - 15
    multiplicities = Counter(pt for line in lines for pt in line)
    assert Counter(multiplicities.values()) == {1:15*(q-2), 3:15}
    found = direct_singular_points(q)
    assert found == set().union(*lines)
    assert len(found) == 15*q-15
    print('DIRECT_GEOMETRY', q, 'points', len(found), 'components', 15, 'triple_points', 15)

print('FROBENIUS_ORBITS: all 720 permutations, 11 partitions, 12 extension tests each: OK')
for typ in sorted(EXPECTED, reverse=True):
    (pt, line, flag) = EXPECTED[typ]
    P, L, F = (from_hist(h, 1) for h in (pt, line, flag))
    # First-degree point count on the reduced singular curve:
    # (q+1)*L - F + P = L*q + (L-F+P).
    print('TYPE', typ, 'triple', pt, 'lines', line, 'branches', flag,
          'singular_curve_Fq_count', f'{L}*q+({L-F+P})')
print('VERIFY_OK')
