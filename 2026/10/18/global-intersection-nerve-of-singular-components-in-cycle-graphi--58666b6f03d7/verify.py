#!/usr/bin/env python3
"""Exact combinatorial checks for the normal fan of a cycle graphical zonotope.

No external packages. This finite verification is a consistency check, not a
proof for unbounded cycle length. The general proof is in RESULT.md.
"""
from collections import Counter
from itertools import combinations, product
from math import comb


def signs(n):
    return [tuple(s) for s in product((-1, 0, 1), repeat=n)
            if 1 in s and -1 in s]


def support(s):
    return {i for i, a in enumerate(s) if a}


def is_face(smaller, larger):
    return all(a == 0 or a == b for a, b in zip(smaller, larger))


def join(x, y):
    z = []
    for a, b in zip(x, y):
        if a and b and a != b:
            return None
        z.append(a or b)
    return tuple(z)


def test(n):
    cs = signs(n)
    minimal = [s for s in cs if s.count(1) == 2 and s.count(-1) == 2]
    assert len(cs) == sum(comb(n, k) * (2**k - 2) for k in range(2, n+1))
    assert len(minimal) == 6*comb(n, 4)
    for s in cs:
        p, q = s.count(1), s.count(-1)
        singular = p >= 2 and q >= 2
        if singular:
            count = sum(is_face(t, s) for t in minimal)
            assert count == comb(p, 2)*comb(q, 2)
        else:
            assert not any(is_face(t, s) for t in minimal)
        # Each cone has pq extremal rays, in dimension p+q-1.
        assert p*q >= p+q-1
        assert (p*q == p+q-1) == (not singular)
    maxs = [s for s in cs if 0 not in s]
    assert len(maxs) == 2**n-2
    assert sum(s.count(1) in (1, n-1) for s in maxs) == 2*n
    assert sum(comb(s.count(1),2)*comb(s.count(-1),2) for s in maxs) == (6*comb(n,4)*2**(n-4))
    # Every minimal singular cone's star is a coordinate-orthant fan of rank n-4.
    for m in minimal:
        cofaces = [s for s in cs if is_face(m, s)]
        assert len(cofaces) == 3**(n-4)
        assert Counter(sum(a != 0 for a in s) - 4 for s in cofaces) == {
            j: comb(n-4,j)*2**j for j in range(n-3)
        }
    # Maximal simplices of the intersection nerve correspond to singular full signs.
    singular_full = [s for s in maxs if s.count(1) >= 2 and s.count(-1) >= 2]
    facet_sets = [frozenset(t for t in minimal if is_face(t,s)) for s in singular_full]
    assert len(set(facet_sets)) == len(singular_full)
    for fs in facet_sets:
        for t in minimal:
            if t not in fs:
                assert any(join(t,u) is None for u in fs)
    if n == 5:
        # Components are edges between weight-two and weight-three sign assignments.
        edges = set()
        for t in minimal:
            endpoints = [s for s in singular_full if is_face(t,s)]
            assert len(endpoints) == 2
            a,b = (frozenset(i for i,z in enumerate(s) if z==1) for s in endpoints)
            if len(a)>len(b):a,b=b,a
            assert len(a)==2 and len(b)==3 and a.issubset(b)
            edges.add((a,b))
        assert len(edges)==30
        assert all(sum(a==frozenset(x) for a,b in edges)==3 for x in combinations(range(n),2))
        assert {a for a,b in edges} == {frozenset(z) for z in combinations(range(n),2)}
        assert {b for a,b in edges} == {frozenset(z) for z in combinations(range(n),3)}
        assert len(edges)==sum(1 for a in combinations(range(n),2) for b in combinations(range(n),3) if set(a).issubset(b))
    if n >= 6:
        assert len({len(fs) for fs in facet_sets}) >= 2
    # For each pair, compatible signed prescriptions have a unique minimal join.
    for i, x in enumerate(minimal):
        for y in minimal[i+1:]:
            j = join(x,y)
            common = [s for s in cs if is_face(x,s) and is_face(y,s)]
            if j is None:
                assert not common
            else:
                assert j in common
                assert len(common) == 3**(n-len(support(j)))
                assert all(is_face(j,s) for s in common)
    print(f'n={n}: cones={len(cs)}, fixed={len(maxs)}, smooth_fixed={2*n}, '
          f'singular_components={len(minimal)}, pairwise_intersections_checked')


if __name__ == '__main__':
    for size in range(4, 8):
        test(size)
    print('VERIFY_OK')
