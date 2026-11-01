"""Finite reproducibility checks for reflection-fixed pure cycle strong Morse complexes.

Standard-library only. All symbolic claims are established in RESULT.md;
this checker independently enumerates small cycle filtrations and verifies
orbit facets for a bounded range. Run: python verify.py
"""
from itertools import permutations


def rooted_path_facets(n):
    ans = set()
    for gap in range(n):
        path = [(gap + 1 + j) % n for j in range(n - 1)]
        for root_position in range(n - 1):
            arrows = set()
            for t in range(n - 2):
                # (edge index, matched endpoint): 0 = left, 1 = right.
                arrows.add((path[t], 0 if t < root_position else 1))
            ans.add(frozenset(arrows))
    return ans


def filtration_maximal(n):
    # For a one-dimensional simple cycle, a vertex is descending dominated
    # precisely when it has exactly one earlier neighbor (n >= 4).
    ans = set()
    for order in permutations(range(n)):
        preceding = set()
        matched = set()
        for v in order:
            earlier = [u for u in ((v - 1) % n, (v + 1) % n) if u in preceding]
            if len(earlier) == 1:
                u = earlier[0]
                edge = u if (u + 1) % n == v else v
                side = 0 if v == edge else 1
                matched.add((edge, side))
            preceding.add(v)
        if len(matched) == n - 2:
            ans.add(frozenset(matched))
    return ans


def reflection_orbits(n, a):
    perm = {(i, side): ((a - i - 1) % n, 1 - side)
            for i in range(n) for side in (0, 1)}
    out = set()
    for v in perm:
        out.add(frozenset((v, perm[v])))
    assert all(len(o) == 2 for o in out)
    assert len(out) == n
    return out


def actual_fixed_orbit_facets(n, a):
    orbits = reflection_orbits(n, a)
    induced = set()
    for facet in rooted_path_facets(n):
        selected = frozenset(orbit for orbit in orbits if orbit.issubset(facet))
        if selected:
            induced.add(selected)
    return {f for f in induced if not any(f < g for g in induced)}


def expected_orbit_facets(n, a):
    m = n // 2
    if a == 0:
        A, B = range(0, m - 1), range(1, m)
        mirror = lambda i: (n - 1 - i) % n
    else:
        assert n % 2 == 0 and a == 1
        A, B = range(1, m - 1), range(2, m)
        mirror = lambda i: (n - i) % n
    return {
        frozenset(frozenset(((i, 1), (mirror(i), 0))) for i in A),
        frozenset(frozenset(((i, 0), (mirror(i), 1))) for i in B),
    }


def all_nonempty_faces(facets):
    faces = set()
    for facet in facets:
        vec = list(facet)
        for mask in range(1, 1 << len(vec)):
            faces.add(frozenset(vec[j] for j in range(len(vec)) if mask >> j & 1))
    return faces


def main():
    filter_count = 0
    for n in (6, 7, 8):
        direct = filtration_maximal(n)
        model = rooted_path_facets(n)
        assert direct == model, (n, len(direct), len(model))
        assert len(model) == n * (n - 1)
        filter_count += len(direct)

    cases = 0
    orbit_face_count = 0
    for n in range(6, 65):
        for a in (0, 1) if n % 2 == 0 else (0,):
            actual = actual_fixed_orbit_facets(n, a)
            expected = expected_orbit_facets(n, a)
            assert actual == expected, (n, a, actual, expected)
            assert len(actual) == 2
            assert all(actual_facet.isdisjoint(other)
                       for actual_facet in actual for other in actual
                       if actual_facet is not other)
            cases += 1
            if n <= 18:
                allfaces = all_nonempty_faces(actual)
                orbit_face_count += len(allfaces)
                assert len(allfaces) == sum((1 << len(f)) - 1 for f in expected)
                # Each simplex has Euler characteristic 1 and the two
                # components are disjoint: total Euler characteristic 2.
                assert sum((-1)**(len(f)-1) for f in allfaces) == 2
    print('VERIFY_OK', 'filtration_facets', filter_count,
          'reflection_cases', cases, 'explicit_fixed_faces', orbit_face_count)


if __name__ == '__main__':
    main()
