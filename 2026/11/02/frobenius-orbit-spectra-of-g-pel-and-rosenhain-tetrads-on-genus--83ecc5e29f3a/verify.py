#!/usr/bin/env python3
"""Exact Frobenius-orbit certificate for Kummer Göpel and Rosenhain tetrads.

Only Python's standard library is required. The mathematical input is the
six-point permutation model of the Jacobian's two-torsion; all finite cases
are exhausted, not randomly sampled.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial, lcm

OMEGA = frozenset(range(6))
ZERO = frozenset()
V = (ZERO,) + tuple(frozenset(c) for c in combinations(range(6), 2))
assert len(V) == 16 and len(set(V)) == 16


def plus(a, b):
    """Addition in the even-subset quotient, canonicalized to 0 or a pair."""
    s = a.symmetric_difference(b)
    return frozenset(s if len(s) <= 2 else OMEGA.difference(s))


def alternating(a, b):
    return len(a.intersection(b)) % 2


def permute(a, p):
    return frozenset(p[x] for x in a)


def cycle_type(p):
    seen, lengths = set(), []
    for i in range(6):
        if i in seen:
            continue
        j, size = i, 0
        while j not in seen:
            seen.add(j)
            size += 1
            j = p[j]
        lengths.append(size)
    return tuple(sorted(lengths, reverse=True))


def linear_planes():
    result = set()
    for a, b in combinations(V[1:], 2):
        result.add(frozenset((ZERO, a, b, plus(a, b))))
    assert len(result) == 35
    return frozenset(result)


def cosets(plane):
    return frozenset(frozenset(plus(v, u) for u in plane) for v in V)


def plane_type(plane):
    v = [x for x in plane if x != ZERO]
    assert len(v) == 3
    return 'G' if alternating(v[0], v[1]) == 0 else 'R'


def direct_orbit_profile(points, p):
    unseen = set(points)
    counts = Counter()
    while unseen:
        x = next(iter(unseen))
        y, count = x, 0
        while y in unseen:
            unseen.remove(y)
            count += 1
            y = frozenset(permute(z, p) for z in y)
        assert y == x
        counts[count] += 1
    return tuple(sorted(counts.items()))


def fixed_coset_formula(planes, p):
    """Independent fixed-point count using stable linear planes and quotient kernels."""
    count = 0
    for plane in planes:
        if frozenset(permute(z, p) for z in plane) != plane:
            continue
        num_vectors = sum(plus(v, permute(v, p)) in plane for v in V)
        assert num_vectors % 4 == 0
        count += num_vectors // 4
    return count


EXPECTED = {
    (1,1,1,1,1,1): (((1,60),), ((1,80),)),
    (2,1,1,1,1):   (((1,12),(2,24)), ((1,24),(2,28))),
    (2,2,1,1):     (((1,8),(2,26)), ((1,8),(2,36))),
    (2,2,2):       (((1,16),(2,22)), ((2,40),)),
    (3,1,1,1):     (((3,20),), ((1,5),(3,25))),
    (3,2,1):       (((3,4),(6,8)), ((1,3),(2,1),(3,7),(6,9))),
    (3,3):         (((1,3),(3,19)), ((1,2),(3,26))),
    (4,1,1):       (((1,2),(2,3),(4,13)), ((2,4),(4,18))),
    (4,2):         (((1,2),(2,3),(4,13)), ((2,4),(4,18))),
    (5,1):         (((5,12),), ((5,16),)),
    (6,):          (((1,1),(2,1),(3,5),(6,7)), ((2,1),(6,13))),
}


def class_size(partition):
    m = Counter(partition)
    d = 1
    for i, a in m.items():
        d *= (i ** a) * factorial(a)
    return factorial(6) // d


def main():
    # Basic linear and symplectic identities, exhausted over the 16-element space.
    for a in V:
        assert plus(a, a) == ZERO
        assert alternating(a, a) == 0
        for b in V:
            assert plus(a, b) in V
            assert alternating(a, b) == alternating(b, a)
            for c in V:
                assert plus(plus(a, b), c) == plus(a, plus(b, c))
                assert alternating(plus(a, b), c) == (alternating(a,c)+alternating(b,c))%2
    planes = linear_planes()
    g_linear = frozenset(p for p in planes if plane_type(p) == 'G')
    r_linear = planes.difference(g_linear)
    assert (len(g_linear), len(r_linear)) == (15, 20)
    g = frozenset(c for p in g_linear for c in cosets(p))
    r = frozenset(c for p in r_linear for c in cosets(p))
    assert (len(g), len(r), len(g.intersection(r))) == (60,80,0)
    assert all(len(c)==4 for c in g.union(r))
    # A second construction: all four-node affine parallelograms.
    direct = {frozenset((a,b,c,plus(plus(a,b),c)))
              for a,b,c in combinations(V, 3)}
    assert len(direct) == 140 and direct == g.union(r)

    rows = {}
    observed = Counter()
    for p in permutations(range(6)):
        typ = cycle_type(p)
        observed[typ] += 1
        gp = direct_orbit_profile(g, p)
        rp = direct_orbit_profile(r, p)
        assert sum(length*count for length,count in gp) == 60
        assert sum(length*count for length,count in rp) == 80
        assert gp == EXPECTED[typ][0] and rp == EXPECTED[typ][1]
        assert lcm(*(n for n, c in gp)) == lcm(*typ)
        assert lcm(*(n for n, c in rp)) == lcm(*typ)
        if typ in rows:
            assert rows[typ] == (gp,rp)
        else:
            rows[typ] = (gp,rp)
        assert dict(gp).get(1,0) == fixed_coset_formula(g_linear, p)
        assert dict(rp).get(1,0) == fixed_coset_formula(r_linear, p)
    assert len(observed) == 11 and sum(observed.values()) == 720
    assert all(observed[typ] == class_size(typ) for typ in observed)
    for typ in sorted(EXPECTED, reverse=True):
        gg, rr = rows[typ]
        print('type=%s G=%s R=%s rational=%s,%s' %
              (''.join(map(str,typ)),gg,rr,dict(gg).get(1,0),dict(rr).get(1,0)))
    print('LINEAR_PLANES=35 ISOTROPIC=15 NONISOTROPIC=20')
    print('AFFINE_TETRADS=140 GOEPEL=60 ROSENHAIN=80')
    print('SIX_POINT_PERMUTATIONS=720 CONJUGACY_TYPES=11')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
