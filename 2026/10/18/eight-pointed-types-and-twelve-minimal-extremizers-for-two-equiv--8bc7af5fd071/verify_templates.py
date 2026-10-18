"""Enumerate the twelve minimal all-profile two-equivalence templates.

Each weighted edge is a nonempty intersection of an E-class and F-class.
The weight is its population. E and F class indices are independently named.
"""
from itertools import product


def templates():
    # Isolated intersections, one with weight one and one with weight two.
    isolated = [(0, 0, 1), (1, 1, 2)]

    # Two disjoint core intersections, with independent assignments of the
    # one- and two-element E-only and F-only leaf cells.
    for eperm, fperm in product(((2, 3), (3, 2)), repeat=2):
        yield isolated + [
            (2, 2, 1), (3, 3, 2),
            (eperm[0], 4, 1), (eperm[1], 5, 2),
            (4, fperm[0], 1), (5, fperm[1], 2),
        ]

    # Core intersections sharing their E-class. The two E-only leaf cells
    # either attach at the core or make a separate two-edge star.
    for outside, fperm in product((False, True), ((2, 3), (3, 2))):
        target = 3 if outside else 2
        yield isolated + [
            (2, 2, 1), (2, 3, 2),
            (target, 4, 1), (target, 5, 2),
            (4, fperm[0], 1), (5, fperm[1], 2),
        ]

    # Mirror case: core intersections sharing their F-class.
    for outside, eperm in product((False, True), ((2, 3), (3, 2))):
        target = 3 if outside else 2
        yield isolated + [
            (2, 2, 1), (3, 2, 2),
            (eperm[0], 4, 1), (eperm[1], 5, 2),
            (4, target, 1), (5, target, 2),
        ]


def signature(edges):
    # One signature per occupied cell, in (a,b,c,d) bit order.
    result = {}
    for i, (e, f, weight) in enumerate(edges):
        a = int(weight >= 2)
        b = int(any(u == e and v != f for u, v, m in edges))
        c = int(any(u != e and v == f for u, v, m in edges))
        d = int(any(u != e and v != f for u, v, m in edges))
        key = (a, b, c, d)
        assert key not in result, 'duplicate pointed type in minimal template'
        result[key] = (e, f)
    return result


def isomorphism_key(profiles):
    # Every profile occurs exactly once. It therefore canonically names a
    # weighted intersection cell. Equality of its left/right endpoints
    # reconstructs both equivalences without assigning class names.
    keys = sorted(profiles)
    return (
        tuple(profiles[x][0] == profiles[y][0] for x in keys for y in keys),
        tuple(profiles[x][1] == profiles[y][1] for x in keys for y in keys),
    )


def main():
    all_keys = set(product((0, 1), repeat=3))
    seen = set()
    examples = []
    for edges in templates():
        assert len(edges) == 8
        assert sum(m for _, _, m in edges) == 12
        assert sum(m == 2 for _, _, m in edges) == 4
        ps = signature(edges)
        assert set(ps) == {(*p, 1) for p in all_keys}
        key = isomorphism_key(ps)
        assert key not in seen, 'duplicate named-equivalence isomorphism type'
        seen.add(key)
        examples.append(edges)
    assert len(seen) == 12

    # Independently test the stated 12-point witness, specified by class
    # labels assigned to elements 1,...,12.
    E = 'abccddeeffff'
    F = 'abaaacddaaee'
    assert len(E) == len(F) == 12
    edges = []
    for e in sorted(set(E)):
        for f in sorted(set(F)):
            m = sum(E[i] == e and F[i] == f for i in range(12))
            if m:
                edges.append((e, f, m))
    assert len(edges) == 8
    assert set(signature(edges)) == {(*p, 1) for p in all_keys}
    assert isomorphism_key(signature(edges)) in seen
    print('TEMPLATES_OK distinct_minimal_isomorphism_types=12 '
          'required_pointed_types=8 minimum_elements=12')


if __name__ == '__main__':
    main()
