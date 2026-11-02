#!/usr/bin/env python3
"""Exact arithmetic check of the incidence reductions of Klein's 28 bitangent forms.

Inputs are the 28 coefficient triples in Janasz--Pokora--Zielinski,
On arrangements of smooth plane quartics and their bitangents,
arXiv:2308.16514, Table 1 (2023), over Z[e]/(e^2+e+2).

No computer-algebra package, floating point arithmetic, or network access needed.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations, product

# The pair (a,b) denotes a+b*e, where e^2=-e-2.
Z = (0, 0)
I = (1, 0)
N = (-1, 0)
E = (0, 1)
NE = (0, -1)
B = (-1, 1)   # e-1
NB = (1, -1)  # 1-e

# Indexed in the printed order, from 1 to 28.
LINES = (
    (Z, I, E), (Z, I, NE), (E, N, Z), (Z, E, N),
    (NB, I, N), (I, N, B), (I, NB, I), (E, I, Z),
    (I, NE, Z), (I, N, NB), (I, I, B), (I, Z, E),
    (I, E, Z), (I, N, I), (I, B, I), (Z, E, I),
    (B, I, I), (E, Z, I), (I, I, N), (I, I, I),
    (I, Z, NE), (I, I, NB), (B, I, N), (I, NB, N),
    (I, B, N), (B, N, N), (I, N, N), (E, Z, N),
)
assert len(LINES) == 28


def radd(x, y):
    return x[0] + y[0], x[1] + y[1]


def rneg(x):
    return -x[0], -x[1]


def rsub(x, y):
    return radd(x, rneg(y))


def rmul(x, y):
    a, b = x
    c, d = y
    return a * c - 2 * b * d, a * d + b * c - b * d


def conjugate(x):
    a, b = x
    return a - b, -b


def norm(x):
    a, b = x
    return a * a - a * b + 2 * b * b


def cross(x, y, add, mul, neg):
    return tuple(add(mul(x[(i + 1) % 3], y[(i + 2) % 3]),
                     neg(mul(x[(i + 2) % 3], y[(i + 1) % 3])))
                 for i in range(3))


def det3(m):
    a, b, c = m
    return radd(rsub(rmul(a[0], rsub(rmul(b[1], c[2]), rmul(b[2], c[1]))),
                     rmul(a[1], rsub(rmul(b[0], c[2]), rmul(b[2], c[0])))),
                rmul(a[2], rsub(rmul(b[0], c[1]), rmul(b[1], c[0]))))


def generic_point_key(w):
    pivot = next(x for x in w if x != Z)
    den = norm(pivot)
    assert den > 0
    co = conjugate(pivot)
    return tuple(tuple(Fraction(u, den) for u in rmul(v, co)) for v in w)


def generic_profile():
    classes = Counter()
    for i, j in combinations(range(28), 2):
        w = cross(LINES[i], LINES[j], radd, rmul, rneg)
        assert w != (Z, Z, Z)
        classes[generic_point_key(w)] += 1
    # Each point incident to m distinct lines contributes C(m,2) pairs.
    assert set(classes.values()) == {1, 6}
    multiplicities = Counter({2: sum(v == 1 for v in classes.values()),
                              4: sum(v == 6 for v in classes.values())})
    assert multiplicities == Counter({2: 252, 4: 21})
    return multiplicities


class Field:
    """F_p, or F_p[e] when root=None and e^2+e+2 is irreducible."""
    def __init__(self, p, root):
        self.p = p
        self.root = root
        self.zero = 0 if root is not None else (0, 0)

    def scalar(self, x):
        a, b = x
        if self.root is not None:
            return (a + b * self.root) % self.p
        return (a % self.p, b % self.p)

    def add(self, a, b):
        if self.root is not None:
            return (a + b) % self.p
        return (a[0] + b[0]) % self.p, (a[1] + b[1]) % self.p

    def neg(self, a):
        if self.root is not None:
            return -a % self.p
        return -a[0] % self.p, -a[1] % self.p

    def mul(self, a, b):
        if self.root is not None:
            return a * b % self.p
        x, y = a
        u, v = b
        return (x * u - 2 * y * v) % self.p, (x * v + y * u - y * v) % self.p

    def inverse(self, a):
        if self.root is not None:
            return pow(a, -1, self.p)
        x, y = a
        d = (x * x - x * y + 2 * y * y) % self.p
        assert d != 0
        return self.mul(((x - y) % self.p, (-y) % self.p),
                        (pow(d, -1, self.p), 0))

    def normalize(self, values):
        pivot = next((x for x in values if x != self.zero), None)
        if pivot is None:
            return None
        inverse = self.inverse(pivot)
        return tuple(self.mul(x, inverse) for x in values)

    def reduced_lines(self):
        return tuple(self.normalize(tuple(self.scalar(x) for x in line))
                     for line in LINES)


def special_profile(p, root):
    f = Field(p, root)
    lines = f.reduced_lines()
    distinct = Counter(lines)
    points = {}
    equal_line_pairs = 0
    distinct_pair_counts = Counter()
    for i, j in combinations(range(28), 2):
        pt = f.normalize(cross(lines[i], lines[j], f.add, f.mul, f.neg))
        if pt is None:
            equal_line_pairs += 1
            continue
        points.setdefault(pt, set()).update((i, j))
        distinct_pair_counts[pt] += 1
    assert equal_line_pairs + sum(distinct_pair_counts.values()) == 378
    assert equal_line_pairs == sum(c * (c - 1) // 2 for c in distinct.values())
    profile = Counter(len(ids) for ids in points.values())
    return f, lines, distinct, points, profile


def main():
    expected_norms = {
        0: 84, 1: 48, 2: 276, 4: 368, 7: 36, 8: 696, 9: 24,
        11: 36, 14: 80, 16: 508, 18: 96, 22: 60, 28: 156,
        32: 420, 36: 24, 44: 60, 56: 28, 64: 204,
        72: 24, 88: 12, 112: 8, 128: 28,
    }
    norms = Counter(norm(det3([LINES[i], LINES[j], LINES[k]]))
                    for i, j, k in combinations(range(28), 3))
    assert norms == expected_norms
    assert sum(norms.values()) == 3276
    # The support of every nonzero norm is contained in {2,3,7,11}.
    support = set()
    for n in norms:
        if n == 0:
            continue
        for p in (2, 3, 7, 11):
            while n % p == 0:
                support.add(p)
                n //= p
        assert n == 1
    assert support == {2, 3, 7, 11}
    generic_profile()

    # Two primes above 2: the support divisor has distinct multiplicity patterns.
    f, lines, dist, points, pr = special_profile(2, 0)
    assert dist == Counter({(1, 0, 0): 4, (0, 1, 0): 4,
                            (0, 0, 1): 4, (1, 1, 1): 16})
    assert len(points) == 6 and pr == Counter({8: 3, 20: 3})
    f, lines, dist, points, pr = special_profile(2, 1)
    assert dist == Counter({(1, 1, 0): 8, (1, 0, 1): 8,
                            (0, 1, 1): 8, (1, 1, 1): 4})
    assert len(points) == 4 and pr == Counter({12: 3, 24: 1})

    f, lines, dist, points, pr = special_profile(3, None)  # F9
    assert len(dist) == 28 and len(points) == 63 and pr == Counter({4: 63})
    assert all(count == 1 for count in dist.values())

    f, lines, dist, points, pr = special_profile(7, 3)  # unique ramified prime
    assert len(dist) == 28 and len(points) == 57
    assert pr == Counter({3: 28, 4: 21, 7: 8})
    conic = sorted({f.normalize((x, y, z))
                    for x, y, z in product(range(7), repeat=3)
                    if (x, y, z) != (0, 0, 0) and (x*x+y*y+z*z) % 7 == 0})
    assert len(conic) == 8
    assert set(conic) == {pt for pt, ids in points.items() if len(ids) == 7}
    assert all(sum(sum(a*b for a,b in zip(line,pt)) % 7 == 0
                   for pt in conic) == 2 for line in lines)
    # All C(8,2) distinct secants occur.
    assert {f.normalize(cross(a,b,f.add,f.mul,f.neg))
            for a,b in combinations(conic,2)} == set(lines)

    for root in (4, 6):  # two primes above 11
        assert (root*root + root + 2) % 11 == 0
        f, lines, dist, points, pr = special_profile(11, root)
        assert len(dist) == 28 and len(points) == 105
        assert pr == Counter({3: 84, 4: 21})
        # Each line has exactly 9 triple points and 3 quadruple points.
        for i in range(28):
            assert Counter(len(ids) for ids in points.values() if i in ids) == \
                   Counter({3: 9, 4: 3})
    print('KLEIN28_EXACT_ALL_PRIMES_2_3_7_11_INCIDENTS_AND_CONIC_PASS')
    print('generic 252 double + 21 quadruple; determinant norms:',dict(sorted(norms.items())))
    print('p2: two nonreduced fibers; p3 63 quadruple; p7 secants of conic; p11 84 triple + 21 quadruple')

if __name__ == '__main__':
    main()
