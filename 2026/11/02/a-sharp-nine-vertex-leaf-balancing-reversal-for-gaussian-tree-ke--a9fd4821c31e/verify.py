#!/usr/bin/env python3
"""Exact rational interval certificate for a nine-vertex tree-metric comparison.

The sole requirements are Python 3 and the standard library. No floating-point
number participates in an assertion or a certificate. Run: python verify.py
"""
from fractions import Fraction

EXP_NUM = 137
EXP_DEN = 100
SCALE = 10 ** 12


class Interval:
    def __init__(self, lower, upper=None):
        self.lower = Fraction(lower)
        self.upper = Fraction(lower if upper is None else upper)
        assert self.lower <= self.upper

    def __add__(self, other):
        other = interval(other)
        return Interval(self.lower + other.lower, self.upper + other.upper)

    __radd__ = __add__

    def __neg__(self):
        return Interval(-self.upper, -self.lower)

    def __sub__(self, other):
        return self + (-interval(other))

    def __rsub__(self, other):
        return interval(other) - self

    def __mul__(self, other):
        other = interval(other)
        products = (self.lower * other.lower, self.lower * other.upper,
                    self.upper * other.lower, self.upper * other.upper)
        return Interval(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = interval(other)
        assert other.lower > 0, "LDL divisor is not certified positive"
        return self * Interval(1 / other.upper, 1 / other.lower)


def interval(value):
    return value if isinstance(value, Interval) else Interval(value)


def integer_nth_root_floor(value, power):
    """Return largest integer r with r**power <= value, by integer arithmetic."""
    low, high = 0, 1
    while high ** power <= value:
        high *= 2
    while high - low > 1:
        mid = (low + high) // 2
        if mid ** power <= value:
            low = mid
        else:
            high = mid
    assert low ** power <= value < (low + 1) ** power
    return low


def distance_power_intervals():
    result = {0: Interval(0), 1: Interval(1)}
    for distance in (2, 3, 4):
        target = (distance ** EXP_NUM) * (SCALE ** EXP_DEN)
        numerator = integer_nth_root_floor(target, EXP_DEN)
        assert numerator ** EXP_DEN <= target
        assert target < (numerator + 1) ** EXP_DEN
        result[distance] = Interval(Fraction(numerator, SCALE),
                                    Fraction(numerator + 1, SCALE))
    return result


def tree_distances(a, b, c):
    """The three hubs are vertices 0, 1, 2; pendant leaves follow by hub."""
    assert min(a, b, c) >= 1 and a + b + c == 6
    edges = [(0, 1), (1, 2)]
    next_vertex = 3
    for hub, multiplicity in enumerate((a, b, c)):
        for _ in range(multiplicity):
            edges.append((hub, next_vertex))
            next_vertex += 1
    assert next_vertex == 9
    d = [[99] * 9 for _ in range(9)]
    for i in range(9):
        d[i][i] = 0
    for u, v in edges:
        d[u][v] = d[v][u] = 1
    for k in range(9):
        for i in range(9):
            for j in range(9):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    assert max(max(row) for row in d) == 4
    return d


def gram_intervals(distances, powers):
    """Euclidean Schoenberg Gram with the last vertex as the base point."""
    last = 8
    return [[(powers[distances[i][last]] + powers[distances[j][last]]
              - powers[distances[i][j]]) / 2
             for j in range(8)] for i in range(8)]


def certified_ldlt_signs(matrix):
    """Interval LDL^T without pivoting, stopping at the first negative pivot.

    Every division is performed only after the preceding actual pivot has been
    certified strictly positive. The returned intervals contain true pivots.
    """
    n = len(matrix)
    L = [[Interval(int(i == j)) for j in range(n)] for i in range(n)]
    diagonal = []
    for k in range(n):
        pivot = matrix[k][k]
        for j in range(k):
            pivot = pivot - L[k][j] * L[k][j] * diagonal[j]
        diagonal.append(pivot)
        if pivot.upper < 0:
            return k, diagonal
        assert pivot.lower > 0, "Indeterminate pivot; raise precision"
        for i in range(k + 1, n):
            entry = matrix[i][k]
            for j in range(k):
                entry = entry - L[i][j] * L[k][j] * diagonal[j]
            L[i][k] = entry / pivot
    return n, diagonal


def run():
    powers = distance_power_intervals()
    representatives = sorted((a, b, 6 - a - b)
                             for a in range(1, 5)
                             for b in range(1, 6 - a)
                             if 1 <= 6 - a - b and a <= 6 - a - b)
    assert representatives == [
        (1, 1, 4), (1, 2, 3), (1, 3, 2), (1, 4, 1),
        (2, 1, 3), (2, 2, 2)
    ]
    expected = {
        (1, 1, 4): (7, Fraction(-7), Fraction(-6)),
        (1, 2, 3): (7, Fraction(-3), Fraction(-2)),
        (1, 3, 2): (6, Fraction(-4), Fraction(-3)),
        (1, 4, 1): (6, Fraction(-4), Fraction(-3)),
        (2, 1, 3): (8, Fraction(0), Fraction(1, 20)),
        (2, 2, 2): (7, Fraction(-1), Fraction(0))
    }
    for triple in representatives:
        distances = tree_distances(*triple)
        gram = gram_intervals(distances, powers)
        index, pivots = certified_ldlt_signs(gram)
        target_index, bound_low, bound_high = expected[triple]
        assert index == target_index
        assert len(pivots) == (index + 1 if index < 8 else 8)
        last = pivots[-1]
        assert bound_low < last.lower <= last.upper < bound_high
        if triple == (2, 1, 3):
            assert index == 8 and all(p.lower > 0 for p in pivots)
            outcome = "all eight pivots strictly positive"
        else:
            assert index < 8 and all(p.lower > 0 for p in pivots[:-1])
            assert last.upper < 0
            outcome = "negative pivot {} (zero-based)".format(index)
        print("{}: {} ; last pivot strictly between {} and {}".format(
            triple, outcome, bound_low, bound_high))
    all_triples = [(a, b, 6-a-b) for a in range(1, 5)
                   for b in range(1, 6 - a)]
    assert len(all_triples) == 10
    assert all(tuple(sorted((a, c))) == tuple(sorted((rep[0], rep[2])))
               and b == rep[1]
               for a, b, c in all_triples
               for rep in [(min(a, c), b, max(a, c))])
    assert {tuple((min(a, c), b, max(a, c))) for a, b, c in all_triples} == set(representatives)
    print("PASS: all 10 ordered positive triples covered by 6 reversal orbits")


if __name__ == "__main__":
    run()
