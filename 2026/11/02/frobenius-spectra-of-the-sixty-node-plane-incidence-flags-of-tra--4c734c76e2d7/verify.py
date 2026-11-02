#!/usr/bin/env python3
"""Exact finite combinatorics for nodes, planes and incident flags of the Segre cubic.

No external dependencies. Python 3.9+.
"""
from collections import Counter
from itertools import combinations, permutations
from math import lcm, factorial

LABELS = tuple(range(6))
ALL = frozenset(LABELS)


def matchings(points):
    points = tuple(points)
    if not points:
        yield ()
        return
    a, rest = points[0], points[1:]
    for b in rest:
        for tail in matchings([c for c in rest if c != b]):
            yield tuple(sorted(((a, b),) + tail))


PLANES = tuple(sorted(set(matchings(LABELS))))
NODES = tuple(sorted({
    tuple(sorted([tuple(A), tuple(sorted(ALL - set(A)))]))
    for A in combinations(LABELS, 3)
}))
assert len(NODES) == 10 and len(PLANES) == 15


def incident(node, plane):
    return all(sum(v in node[0] for v in edge) == 1 for edge in plane)


FLAGS = tuple((n, m) for n in NODES for m in PLANES if incident(n, m))
assert len(FLAGS) == 60
assert {sum(incident(n, m) for n in NODES) for m in PLANES} == {4}
assert {sum(incident(n, m) for m in PLANES) for n in NODES} == {6}


def image_node(p, node):
    return tuple(sorted(tuple(sorted(p[v] for v in A)) for A in node))


def image_plane(p, plane):
    return tuple(sorted(tuple(sorted(p[v] for v in edge)) for edge in plane))


def image_flag(p, flag):
    return (image_node(p, flag[0]), image_plane(p, flag[1]))


def cycle_type(p):
    todo = set(LABELS)
    lengths = []
    while todo:
        start = min(todo)
        j = start
        c = 0
        while j in todo:
            todo.remove(j)
            c += 1
            j = p[j]
        assert j == start
        lengths.append(c)
    return tuple(sorted(lengths, reverse=True))


def cycle_spectrum(p, domain, image):
    todo = set(domain)
    out = Counter()
    while todo:
        start = min(todo)
        j = start
        d = 0
        while j in todo:
            todo.remove(j)
            d += 1
            j = image(p, j)
        assert j == start
        out[d] += 1
    return dict(sorted(out.items()))


def power(p, n):
    out = tuple(LABELS)
    for _ in range(n):
        out = tuple(p[out[j]] for j in LABELS)
    return out


def fixed_spectrum_check(p, domain, image, spectrum):
    order = lcm(*cycle_type(p))
    for e in range(1, order + 1):
        fp = sum(image(power(p, e), x) == x for x in domain)
        by_cycles = sum(d * mult for d, mult in spectrum.items() if e % d == 0)
        assert fp == by_cycles, (p, e, fp, by_cycles)


EXPECTED = {
    (6,): ({1: 1, 3: 1, 6: 1}, {1: 1, 2: 1, 3: 2, 6: 1}, {1: 1, 2: 1, 3: 5, 6: 7}),
    (5, 1): ({5: 2}, {5: 3}, {5: 12}),
    (4, 2): ({1: 2, 4: 2}, {1: 1, 2: 1, 4: 3}, {2: 2, 4: 14}),
    (4, 1, 1): ({2: 1, 4: 2}, {1: 1, 2: 1, 4: 3}, {2: 2, 4: 14}),
    (3, 3): ({1: 1, 3: 3}, {1: 3, 3: 4}, {1: 3, 3: 19}),
    (3, 2, 1): ({1: 1, 3: 1, 6: 1}, {3: 1, 6: 2}, {6: 10}),
    (3, 1, 1, 1): ({1: 1, 3: 3}, {3: 5}, {3: 20}),
    (2, 2, 2): ({1: 4, 2: 3}, {1: 7, 2: 4}, {1: 16, 2: 22}),
    (2, 2, 1, 1): ({1: 2, 2: 4}, {1: 3, 2: 6}, {1: 4, 2: 28}),
    (2, 1, 1, 1, 1): ({1: 4, 2: 3}, {1: 3, 2: 6}, {2: 30}),
    (1, 1, 1, 1, 1, 1): ({1: 10}, {1: 15}, {1: 60}),
}
assert len(EXPECTED) == 11

classes = Counter()
for p in permutations(LABELS):
    ty = cycle_type(p)
    classes[ty] += 1
    nodes = cycle_spectrum(p, NODES, image_node)
    planes = cycle_spectrum(p, PLANES, image_plane)
    flags = cycle_spectrum(p, FLAGS, image_flag)
    assert (nodes, planes, flags) == EXPECTED[ty], (p, ty, nodes, planes, flags)
    # Independent check of fixed point counts, rather than merely summing cycle lengths.
    for domain, action, spectrum in [(NODES, image_node, nodes),
                                     (PLANES, image_plane, planes),
                                     (FLAGS, image_flag, flags)]:
        fixed_spectrum_check(p, domain, action, spectrum)
    assert sum(a * b for a, b in nodes.items()) == 10
    assert sum(a * b for a, b in planes.items()) == 15
    assert sum(a * b for a, b in flags.items()) == 60
    assert lcm(*flags.keys()) == lcm(*ty)

assert sum(classes.values()) == factorial(6)
assert set(classes) == set(EXPECTED)
print('VERIFIED permutations:', sum(classes.values()))
print('lambda | classes | node spectra | plane spectra | flag spectra | rational nodes, planes, flags')
for ty in EXPECTED:
    n, m, f = EXPECTED[ty]
    print(f'{ty}: {classes[ty]}; {n}; {m}; {f}; {(n.get(1,0), m.get(1,0), f.get(1,0))}')

assert {ty for ty, (n, m, f) in EXPECTED.items()
        if n.get(1, 0) and m.get(1, 0) and not f.get(1, 0)} == {
            (4, 2), (2, 1, 1, 1, 1)}
print('Exceptional rational-node/rational-plane/no-rational-flag types:',
      '(4,2), (2,1,1,1,1)')
print('VERIFY_OK')
