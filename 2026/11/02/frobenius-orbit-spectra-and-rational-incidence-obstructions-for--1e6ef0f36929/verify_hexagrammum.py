#!/usr/bin/env python3
"""Exact Frobenius and projective incidence checks for the Pascal--Kirkman flags.

Requires Python 3.9+ standard library. All projective calculations are exact
integer arithmetic or arithmetic modulo the indicated prime.
"""
from collections import Counter
from functools import reduce
from itertools import permutations
from math import gcd, lcm

V = tuple(range(6))
IDENTITY = V


def compose(a, b):
    return tuple(a[b[i]] for i in V)


def inverse(a):
    return tuple(a.index(i) for i in V)


def ppower(a, n):
    b = IDENTITY
    for _ in range(n):
        b = compose(a, b)
    return b


def cycles(a):
    seen = set()
    out = []
    for i in V:
        if i in seen:
            continue
        cyc = []
        j = i
        while j not in seen:
            seen.add(j)
            cyc.append(j)
            j = a[j]
        out.append(tuple(cyc))
    return out


def cycle_type(a):
    return tuple(sorted((len(c) for c in cycles(a)), reverse=True))


def canonical(a):
    return min(a, inverse(a))


def conjugate(g, h):
    return compose(compose(g, h), inverse(g))


ALL = tuple(permutations(V))
HEXAGONS = tuple(sorted({canonical(x) for x in ALL
                         if cycle_type(x) == (6,)}))
assert len(ALL) == 720 and len(HEXAGONS) == 60


def edges(h):
    # A hexagon is an unoriented Hamiltonian cycle on the six labels.
    return frozenset(frozenset((i, h[i])) for i in V)


EDGE_SETS = {h: edges(h) for h in HEXAGONS}
FLAGS = frozenset((h, k) for h in HEXAGONS for k in HEXAGONS
                  if EDGE_SETS[h].isdisjoint(EDGE_SETS[k]))
assert len(FLAGS) == 180
assert {sum((h, k) in FLAGS for k in HEXAGONS) for h in HEXAGONS} == {3}
assert {sum((h, k) in FLAGS for h in HEXAGONS) for k in HEXAGONS} == {3}


def on_hex(g, h):
    return canonical(conjugate(g, h))


def on_flag(g, x):
    return on_hex(g, x[0]), on_hex(g, x[1])


def orbit_spectrum(g, items, action):
    assert len(set(items)) == len(items)
    remaining = set(items)
    result = Counter()
    while remaining:
        x = min(remaining)
        y = x
        current = set()
        while y not in current:
            assert y in remaining
            current.add(y)
            y = action(g, y)
        assert y == x
        remaining.difference_update(current)
        result[len(current)] += 1
    return tuple(sorted(result.items()))


# Tuples (orbit length, number of such cycles), not merely fixed counts.
EXPECTED = {
    (6,): (((1, 1), (2, 1), (3, 5), (6, 7)), ((3, 8), (6, 26))),
    (5, 1): (((5, 12),), ((5, 36),)),
    (4, 2): (((2, 2), (4, 14)), ((2, 2), (4, 44))),
    (4, 1, 1): (((2, 2), (4, 14)), ((2, 2), (4, 44))),
    (3, 3): (((1, 3), (3, 19)), ((3, 60),)),
    (3, 2, 1): (((6, 10),), ((6, 30),)),
    (3, 1, 1, 1): (((3, 20),), ((3, 60),)),
    (2, 2, 2): (((1, 16), (2, 22)), ((1, 24), (2, 78))),
    (2, 2, 1, 1): (((1, 4), (2, 28)), ((1, 4), (2, 88))),
    (2, 1, 1, 1, 1): (((2, 30),), ((2, 90),)),
    (1, 1, 1, 1, 1, 1): (((1, 60),), ((1, 180),)),
}


def fixed(g, items, action):
    return sum(action(g, x) == x for x in items)


def check_orbit_classification():
    reps = {}
    for g in ALL:
        reps.setdefault(cycle_type(g), g)
    assert set(reps) == set(EXPECTED)
    for tp, g in reps.items():
        h_sp = orbit_spectrum(g, HEXAGONS, on_hex)
        f_sp = orbit_spectrum(g, FLAGS, on_flag)
        assert (h_sp, f_sp) == EXPECTED[tp], (tp, h_sp, f_sp)
        assert sum(d * count for d, count in h_sp) == 60
        assert sum(d * count for d, count in f_sp) == 180
        assert lcm(*(d for d, _ in f_sp)) == lcm(*tp)
        # Distinct original Pascal and Kirkman objects are separately fixed
        # in the two obstruction types, but no incident pair is fixed.
        if tp in {(6,), (3, 3)}:
            fs = [h for h in HEXAGONS if on_hex(g, h) == h]
            assert len(fs) == (1 if tp == (6,) else 3)
            assert all(EDGE_SETS[h] & EDGE_SETS[k]
                       for h in fs for k in fs)
            if tp == (3, 3):
                assert {len(EDGE_SETS[h] & EDGE_SETS[k])
                        for h in fs for k in fs if h != k} == {3}
            assert fixed(g, FLAGS, on_flag) == 0
        # Independent fixed-point check for every extension degree through
        # a full period, rather than trusting the orbit-walking algorithm.
        order = lcm(*tp)
        for n in range(1, order + 1):
            gn = ppower(g, n)
            assert fixed(gn, HEXAGONS, on_hex) == sum(
                d * count for d, count in h_sp if n % d == 0)
            assert fixed(gn, FLAGS, on_flag) == sum(
                d * count for d, count in f_sp if n % d == 0)
    # Exhaust all 720 permutations and check the identity class controls the
    # fixed-point character, and all incidences are relabeling-equivariant.
    for g in ALL:
        tp = cycle_type(g)
        hp, fp = EXPECTED[tp]
        assert fixed(g, HEXAGONS, on_hex) == next(
            (c for d, c in hp if d == 1), 0)
        assert fixed(g, FLAGS, on_flag) == next(
            (c for d, c in fp if d == 1), 0)
        assert all(on_flag(g, e) in FLAGS for e in FLAGS)
    assert [tp for tp, (hp, fp) in EXPECTED.items()
            if any(d == 1 for d, _ in hp)
            and not any(d == 1 for d, _ in fp)] == [(6,), (3, 3)]
    print('FROBENIUS_11_TYPES_AND_ALL_720_PERMUTATIONS_OK')
    for tp, (hp, fp) in EXPECTED.items():
        hfix = next((c for d, c in hp if d == 1), 0)
        ffix = next((c for d, c in fp if d == 1), 0)
        print('%s: hexagons=%s, flags=%s, rational=(%s,%s)'
              % (tp, hp, fp, hfix, ffix))


def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])


def primitive(v):
    g = reduce(gcd, v)
    assert g != 0
    w = tuple(x // g for x in v)
    return tuple(-x for x in w) if next(x for x in w if x) < 0 else w


def check_projective_realization(modulus=None):
    # Six exact points (1:t:t^2) of the nonsingular conic XZ=Y^2.
    ts = (0, 1, 3, 9, 25, 64)
    def normalize(v):
        if modulus is None:
            return primitive(v)
        w = tuple(x % modulus for x in v)
        lead = next(x for x in w if x != 0)
        return tuple((x * pow(lead, -1, modulus)) % modulus for x in w)
    def dot_zero(a, b):
        v = sum(x*y for x, y in zip(a, b))
        return v == 0 if modulus is None else v % modulus == 0
    points = [(1, t, t*t) for t in ts]
    secants = {(i, j): normalize(cross(points[i], points[j]))
               for i in V for j in V if i < j}
    def sec(i, j):
        return secants[tuple(sorted((i, j)))]
    pascals = {}
    for h in HEXAGONS:
        a, b, c, d, e, f = cycles(h)[0]
        x = normalize(cross(sec(a, b), sec(d, e)))
        y = normalize(cross(sec(b, c), sec(e, f)))
        z = normalize(cross(sec(c, d), sec(f, a)))
        line = normalize(cross(x, y))
        assert dot_zero(line, z)  # Pascal's collinearity.
        pascals[h] = line
    assert len(set(pascals.values())) == 60
    kirkmans = {}
    for k in HEXAGONS:
        neighboring = [h for h in HEXAGONS if (h, k) in FLAGS]
        assert len(neighboring) == 3
        point = normalize(cross(pascals[neighboring[0]],
                                pascals[neighboring[1]]))
        assert dot_zero(pascals[neighboring[2]], point)
        kirkmans[k] = point
    assert len(set(kirkmans.values())) == 60
    actual_flags = {(h, k) for h in HEXAGONS for k in HEXAGONS
                    if dot_zero(pascals[h], kirkmans[k])}
    assert actual_flags == FLAGS, (modulus, len(actual_flags))
    print('PROJECTIVE_CONFIGURATION_OK',
          ('Q' if modulus is None else 'F_%s' % modulus),
          '60_lines_60_points_180_flags')


if __name__ == '__main__':
    check_orbit_classification()
    check_projective_realization()
    check_projective_realization(10007)
    print('VERIFY_OK')
