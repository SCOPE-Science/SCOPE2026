"""Finite exact-rational checks for mutual Birkhoff--James orthogonality."""
from fractions import Fraction
from functools import reduce
from itertools import product
from math import gcd


def projective(v):
    g = reduce(gcd, (abs(a) for a in v))
    w = tuple(a // g for a in v)
    if next(t for t in w if t) < 0:
        return tuple(-t for t in w)
    return w


def support_criterion(x, y):
    lhs = abs(sum((1 if a > 0 else -1) * b
                  for a, b in zip(x, y) if a))
    rhs = sum(abs(b) for a, b in zip(x, y) if not a)
    return lhs <= rhs


def direct_piecewise_minimum(x, y):
    """A coercive sum of absolute affine functions minimizes at a knot."""
    knots = {Fraction(-a, b) for a, b in zip(x, y) if b}
    baseline = sum(map(abs, x))
    return min(sum(abs(a + t * b) for a, b in zip(x, y))
               for t in knots) >= baseline


def clique_search(vectors):
    n = len(vectors)
    near = [set() for _ in range(n)]
    for a in range(n):
        for b in range(a + 1, n):
            if support_criterion(vectors[a], vectors[b]) and \
               support_criterion(vectors[b], vectors[a]):
                near[a].add(b)
                near[b].add(a)
    maximum, extremizers, steps = 0, [], 0

    def expand(clique, candidates, excluded):
        nonlocal maximum, extremizers, steps
        steps += 1
        if not candidates and not excluded:
            size = len(clique)
            if size > maximum:
                maximum, extremizers = size, [clique]
            elif size == maximum:
                extremizers.append(clique)
            return
        if len(clique) + len(candidates) < maximum:
            return
        pivot = max(candidates | excluded,
                    key=lambda i: len(candidates & near[i])) \
                    if (candidates or excluded) else None
        remaining = tuple(candidates - (near[pivot] if pivot is not None else set()))
        for i in remaining:
            expand(clique + (i,), candidates & near[i], excluded & near[i])
            candidates.remove(i)
            excluded.add(i)

    expand((), set(range(n)), set())
    return maximum, [{vectors[i] for i in tup} for tup in extremizers], steps


checks = 0
for dimension, expected in ((1, 1), (2, 2), (3, 6)):
    vectors = sorted({projective(t) for t in product(range(-2, 3), repeat=dimension)
                      if any(t)})
    for x in vectors:
        for y in vectors:
            assert support_criterion(x, y) == direct_piecewise_minimum(x, y)
            checks += 1
    number, maxima, search_steps = clique_search(vectors)
    assert number == expected
    if dimension == 3:
        canonical_six = {projective(tuple(int(i == a) + s * int(i == b)
                                          for i in range(3)))
                         for a in range(3) for b in range(a + 1, 3)
                         for s in (-1, 1)}
        assert len(maxima) == 1 and maxima[0] == canonical_six
    print("dimension=%d vertices=%d clique=%d maximum_orbits_on_grid=%d search_nodes=%d"
          % (dimension, len(vectors), number, len(maxima), search_steps))
print("VERIFY_OK direct_piecewise_pairs=%d" % checks)
