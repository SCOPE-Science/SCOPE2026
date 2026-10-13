"""Exact finite tests for the planar enclosure-width merge theorem.

The proof is analytic; these exhaustive and randomized tests check implementation,
tie cases, empty enclosures, and witness validity without replacing the proof.
"""
from fractions import Fraction
from itertools import combinations
import random


def minimal_front(points):
    ordered = sorted(points)
    front = []
    best = None
    for x, y in ordered:
        if best is None or y < best:
            front.append((x, y))
            best = y
    return front


def maximal_front(points):
    ordered = sorted(points, reverse=True)
    front = []
    best = None
    for x, y in ordered:
        if best is None or y > best:
            front.append((x, y))
            best = y
    return front[::-1]


def width_sorted_fronts(l_front, u_front):
    """Linear-time merge; input fronts must be antichains sorted by first coordinate."""
    if not l_front or not u_front:
        return None, None
    j = 0
    value = None
    witness = None
    for a, b in l_front:
        while j < len(u_front) and u_front[j][0] - u_front[j][1] < a - b:
            j += 1
        for k in (j - 1, j):
            if 0 <= k < len(u_front):
                x, y = u_front[k]
                score = min(x - a, y - b)
                if value is None or score > value:
                    value, witness = score, ((a, b), (x, y))
    if value is None or value < 0:
        return None, None
    return value, witness


def width_merge(lower, upper):
    """Sorting-plus-linear exact width algorithm on arbitrary finite point sets."""
    if not lower or not upper:
        return None, None
    return width_sorted_fronts(minimal_front(lower), maximal_front(upper))


def width_brute(lower, upper):
    if not lower or not upper:
        return None
    value = max(min(x - a, y - b) for a, b in lower for x, y in upper)
    return value if value >= 0 else None


def check(lower, upper):
    value, witness = width_merge(lower, upper)
    front_value, front_witness = width_sorted_fronts(minimal_front(lower), maximal_front(upper))
    assert (front_value, front_witness) == (value, witness)
    expected = width_brute(lower, upper)
    assert value == expected, (lower, upper, value, expected)
    if witness is None:
        assert value is None
        return
    lo, up = witness
    assert lo in lower and up in upper
    assert lo[0] <= up[0] and lo[1] <= up[1]
    assert value == min(up[0] - lo[0], up[1] - lo[1])


def main():
    domain = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1)]
    small = [tuple(s) for k in range(4) for s in combinations(domain, k)]
    for lower in small:
        for upper in small:
            check(lower, upper)
    rng = random.Random(20261008)
    for n in range(1, 9):
        for m in range(1, 9):
            for _ in range(1500):
                lower = [(rng.randint(-20, 20), rng.randint(-20, 20)) for _ in range(n)]
                upper = [(rng.randint(-20, 20), rng.randint(-20, 20)) for _ in range(m)]
                check(lower, upper)
    for _ in range(1500):
        lower = [(Fraction(rng.randint(-12, 12), rng.randint(1, 7)),
                  Fraction(rng.randint(-12, 12), rng.randint(1, 7)))
                 for _ in range(rng.randint(1, 6))]
        upper = [(Fraction(rng.randint(-12, 12), rng.randint(1, 7)),
                  Fraction(rng.randint(-12, 12), rng.randint(1, 7)))
                 for _ in range(rng.randint(1, 6))]
        check(lower, upper)
    check([], [(1, 1)])
    check([(0, 0)], [])
    check([(0, 10), (4, 6), (8, 1)], [(5, 18), (11, 9), (16, 3)])
    assert width_merge([(0, 10), (4, 6), (8, 1)],
                       [(5, 18), (11, 9), (16, 3)])[0] == 5
    print('VERIFY_OK', len(small)**2, 'exhaustive subset pairs,',
          96000, 'random integer pairs,', 1500, 'rational pairs')


if __name__ == '__main__':
    main()
