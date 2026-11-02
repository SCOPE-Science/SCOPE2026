#!/usr/bin/env python3
"""Exact finite checks for spherical edge-sum cumulant identities.

This finite checker verifies examples using independent spherical tensor
integrals. The all-graph and all-order conclusions require the proof.
Requires Python 3 standard library only.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement, permutations, product
from math import comb, factorial

F = Fraction
ASSERTIONS = 0


def assert_eq(a, b, label):
    global ASSERTIONS
    ASSERTIONS += 1
    if a != b:
        raise AssertionError(f"{label}: {a} != {b}")


def pairings(positions):
    if not positions:
        yield []
        return
    first = positions[0]
    for j in range(1, len(positions)):
        for rest in pairings(positions[1:j] + positions[j + 1:]):
            yield [(first, positions[j])] + rest


def sphere_coordinate_moment(indices, dimension):
    if len(indices) % 2:
        return F(0)
    k = len(indices) // 2
    if k == 0:
        return F(1)
    numerator = sum(
        all(indices[i] == indices[j] for i, j in pairing)
        for pairing in pairings(tuple(range(len(indices))))
    )
    denominator = 1
    for j in range(k):
        denominator *= dimension + 2 * j
    return F(numerator, denominator)


def exact_edge_product(edge_multiset, dimension):
    if not edge_multiset:
        return F(1)
    vertices = sorted({v for a, b in edge_multiset for v in (a, b)})
    answer = F(0)
    for colors in product(range(dimension), repeat=len(edge_multiset)):
        incidence = {v: [] for v in vertices}
        for (a, b), color in zip(edge_multiset, colors):
            incidence[a].append(color)
            incidence[b].append(color)
        term = F(1)
        for v in vertices:
            term *= sphere_coordinate_moment(incidence[v], dimension)
            if term == 0:
                break
        answer += term
    return answer


def exact_cumulants(edges, dimension, order=5, weights=None):
    if weights is None:
        weights = [1] * len(edges)
    raw = [F(1)]
    cache = {}
    for r in range(1, order + 1):
        moment = F(0)
        for indices in combinations_with_replacement(range(len(edges)), r):
            multiplicity = factorial(r)
            for count in Counter(indices).values():
                multiplicity //= factorial(count)
            sample = tuple(edges[index] for index in indices)
            parity = Counter(v for a, b in sample for v in (a, b))
            if any(n % 2 for n in parity.values()):
                continue
            if sample not in cache:
                cache[sample] = exact_edge_product(sample, dimension)
            moment += multiplicity * cache[sample] * __import__("math").prod(weights[index] for index in indices)
        raw.append(moment)
    cumulative = [F(0)] * (order + 1)
    for r in range(1, order + 1):
        cumulative[r] = raw[r] - sum(
            comb(r - 1, j - 1) * cumulative[j] * raw[r - j]
            for j in range(1, r)
        )
    return cumulative


def cycles(edges, k):
    vset = sorted({x for e in edges for x in e})
    eset = {frozenset(e) for e in edges}
    canonical = set()
    for seq in permutations(vset, k):
        if all(frozenset((seq[i], seq[(i + 1) % k])) in eset for i in range(k)):
            shifted = [seq[i:] + seq[:i] for i in range(k)]
            reverse = seq[::-1]
            shifted += [reverse[i:] + reverse[:i] for i in range(k)]
            canonical.add(min(shifted))
    return len(canonical)


def circuit(k):
    return [(i, (i + 1) % k) for i in range(k)]


def predictions(edges, dimension):
    d = dimension
    m = len(edges)
    c3, c4, c5 = (cycles(edges, i) for i in (3, 4, 5))
    return [
        F(0), F(0), F(m, d), F(6 * c3, d**2),
        -F(6 * m, d**2 * (d + 2)) + F(24 * c4, d**3),
        -F(360 * c3, d**3 * (d + 2)) + F(120 * c5, d**4),
    ]


def main():
    graphs = {
        "one-edge": [(0, 1)],
        "path-four": [(0, 1), (1, 2), (2, 3), (3, 4)],
        "triangle": circuit(3),
        "square": circuit(4),
        "pentagon": circuit(5),
        "tetrahedron": [(a, b) for a in range(4) for b in range(a + 1, 4)],
        "bow-tie": circuit(3) + [(0, 3), (3, 4), (4, 0)],
        "house": circuit(4) + [(1, 4), (2, 4)],
    }
    for d in (2, 3, 4):
        for name, edges in graphs.items():
            observed = exact_cumulants(edges, d)
            expected = predictions(edges, d)
            for r in range(1, 6):
                assert_eq(observed[r], expected[r], f"dimension={d}, graph={name}, cumulant={r}")
            m = len(edges)
            assert_eq(observed[2], F(m, d), f"variance dimension={d}, graph={name}")
            if d == 3:
                assert_eq(observed[3] * F(3, 2), cycles(edges, 3), f"triangle readout {name}")
                assert_eq((observed[4] + F(2 * m, 15)) * F(9, 8), cycles(edges, 4), f"square readout {name}")
                assert_eq((observed[5] + F(8 * cycles(edges, 3), 3)) * F(27, 40), cycles(edges, 5), f"pentagon readout {name}")
        for length in range(3, 8):
            edges = circuit(length)
            expectation = exact_edge_product(tuple(edges), d)
            assert_eq(expectation, F(1, d**(length - 1)), f"cycle product dimension={d}, length={length}")
            assert_eq(cycles(edges, length), 1, f"cycle enumeration dimension={d}, length={length}")
    for d in (2, 3, 4):
        triangular_weights = [2, 3, 5]
        weighted_triangle = exact_cumulants(circuit(3), d, order=3, weights=triangular_weights)
        assert_eq(weighted_triangle[2], F(sum(w*w for w in triangular_weights), d), f"weighted variance {d}")
        assert_eq(weighted_triangle[3], F(6 * __import__("math").prod(triangular_weights), d*d), f"weighted third cycle cumulant {d}")
        mixed = circuit(3) + [(3,4),(4,5),(5,3)]
        cancelling_weights = [1,1,1,-1,1,1]
        assert_eq(exact_cumulants(mixed,d,order=3,weights=cancelling_weights)[3], F(0), f"signed cancellation {d}")
    for d in (2, 3, 4):
        edge = [(0, 1)]
        assert_eq(exact_edge_product(edge * 2, d), F(1, d), f"edge second moment {d}")
        assert_eq(exact_edge_product(edge * 4, d), F(3, d * (d + 2)), f"edge fourth moment {d}")
    print(f"PASS {ASSERTIONS} exact rational assertions; dimensions 2,3,4; eight graph families; cycle lengths 3..7")


if __name__ == "__main__":
    main()
