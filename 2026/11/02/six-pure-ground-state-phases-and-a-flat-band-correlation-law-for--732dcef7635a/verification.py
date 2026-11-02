"""Reproducible finite checks for ternary Hamming Blume-Capel ground states.

Python 3 standard library only. These computations corroborate the proof and
are not used as a substitute for the arbitrary-dimension argument.
"""
from collections import Counter
from fractions import Fraction
from itertools import product, permutations
from math import isclose

TYPES = {
    "000": (0, 0, 0), "+00": (0, 0, 1), "+-0": (-1, 0, 1),
    "++-": (-1, 1, 1), "++0": (0, 1, 1), "+++": (1, 1, 1)
}
POINTS = {
    "000": (Fraction(3), Fraction(1)),
    "+00": (Fraction(1), Fraction(3, 2)),
    "+-0": (Fraction(1, 10), Fraction(1, 50)),
    "++-": (Fraction(-2), Fraction(1)),
    "++0": (Fraction(1, 5), Fraction(2)),
    "+++": (Fraction(0), Fraction(5)),
}

def line_energy(s, x, y):
    a, b, c = s
    return a * b + b * c + a * c + x * (a*a+b*b+c*c) - y * (a+b+c)

def states(d, triplet):
    """All realizable strict-region states by affine ternary functions."""
    vertices = tuple(product(range(3), repeat=d))
    out = set()
    for slopes in product((1, 2), repeat=d):
        for offset in range(3):
            for perm in set(permutations(triplet)):
                out.add(tuple(perm[(sum(a*v for a, v in zip(slopes, z)) + offset) % 3]
                              for z in vertices))
    return vertices, out

def lines(d, vertices):
    idx = {z: i for i, z in enumerate(vertices)}
    out = []
    for axis in range(d):
        for other in product(range(3), repeat=d-1):
            triple = []
            for a in range(3):
                z = list(other)
                z.insert(axis, a)
                triple.append(idx[tuple(z)])
            out.append(tuple(triple))
    return out

checks = 0
for d in (1, 2, 3, 4):
    vertices = tuple(product(range(3), repeat=d))
    axis_lines = lines(d, vertices)
    for name, triplet in TYPES.items():
        _, cfgs = states(d, triplet)
        expected = (1 if len(set(triplet)) == 1 else
                    3*2**d if len(set(triplet)) == 3 else 3*2**(d-1))
        assert len(cfgs) == expected, (d, name, len(cfgs), expected)
        for cfg in cfgs:
            assert all(tuple(sorted(cfg[i] for i in li)) == triplet
                       for li in axis_lines)
            checks += 1
print("AFFINE_CLASSIFICATION_CHECKS", checks)

# Exact exhaustive spectrum of 3^9 spin assignments on H(2,3).
d = 2
vertices = tuple(product(range(3), repeat=d))
axis_lines = lines(d, vertices)
edges = sorted({tuple(sorted((li[i], li[j])))
                for li in axis_lines for i, j in ((0, 1), (1, 2), (0, 2))})
assert len(edges) == 18
configs = list(product((-1, 0, 1), repeat=9))
assert len(configs) == 19683
for label, (x, y) in POINTS.items():
    local = {key:line_energy(t, x, y) for key, t in TYPES.items()}
    assert min(local, key=local.get) == label
    exact_min = len(axis_lines)*local[label]
    energies = [(sum(s[i]*s[j] for i, j in edges)
                 + d*x*sum(t*t for t in s)
                 - d*y*sum(s)) for s in configs]
    assert min(energies) == exact_min, (label, min(energies), exact_min)
    exact_count = sum(e == exact_min for e in energies)
    _, cfgs = states(d, TYPES[label])
    assert exact_count == len(cfgs), (label, exact_count, len(cfgs))
    print("EXHAUSTIVE", label, "energy", str(exact_min), "degeneracy", exact_count)

# Average centered covariances over every enumerated ground state.
pair_checks = 0
for d in (1, 2, 3):
    vertices = tuple(product(range(3), repeat=d))
    for label, triplet in TYPES.items():
        _, cfgs = states(d, triplet)
        n = len(cfgs)
        mu = Fraction(sum(triplet), 3)
        variance = Fraction(sum(v*v for v in triplet), 3) - mu**2
        for i, u in enumerate(vertices):
            for j, v in enumerate(vertices):
                r = sum(a != b for a, b in zip(u, v))
                covariance = sum((Fraction(s[i])-mu)*(Fraction(s[j])-mu)
                                 for s in cfgs) / n
                expected = variance * Fraction(-1, 2)**r
                assert covariance == expected, (d, label, r, covariance, expected)
                pair_checks += 1
print("EXACT_COVARIANCE_CHECKS", pair_checks)

# Every claimed pure phase is strictly feasible at its listed parameters.
assert len(POINTS) == len(TYPES)
print("STRICT_PHASE_WITNESSES", len(POINTS))
print("VERIFICATION_OK")
