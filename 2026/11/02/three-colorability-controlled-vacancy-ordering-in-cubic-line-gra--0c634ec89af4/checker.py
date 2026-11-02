#!/usr/bin/env python3
"""Exact independent ground-state enumerations for a spin-1 line-graph model.

Requires only Python 3; no downloaded data or third-party libraries.
"""
from collections import Counter
from itertools import permutations, product
from fractions import Fraction


def cube_edges():
    return [(u, v) for u in range(8) for v in range(u + 1, 8)
            if (u ^ v).bit_count() == 1]


def k33_edges():
    return [(u, v) for u in range(3) for v in range(3, 6)]


def build_incidence(edges, n):
    inc = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        inc[u].append(e)
        inc[v].append(e)
    assert len(edges) == 3 * n // 2
    assert all(len(row) == 3 for row in inc)
    return inc


def brute(edges, n):
    """Full 3^m enumeration, using twice the Hamiltonian, for J=1."""
    inc = build_incidence(edges, n)
    pvalues = (-2, 0, 1, 2, 4)  # p=2D/J: D/J=-1,0,1/2,1,2
    minima = {p: None for p in pvalues}
    ground = {p: Counter() for p in pvalues}
    nstates = 0
    for s in product((-1, 0, 1), repeat=len(edges)):
        nstates += 1
        k = sum(x * x for x in s)
        magnetization = sum(s)
        q = sum(sum(s[e] for e in row)**2 for row in inc)
        for p in pvalues:
            twice_energy = q + (p - 2) * k
            if minima[p] is None or twice_energy < minima[p]:
                minima[p] = twice_energy
                ground[p] = Counter()
            if twice_energy == minima[p]:
                ground[p][(k, magnetization)] += 1
    return nstates, minima, ground


# Independent transfer enumeration: the even sublattice of a cube partitions
# all twelve edge variables into four disjoint three-edge stars.
FULL = set(permutations((1, 1, -1))) | set(permutations((-1, -1, 1)))
COLOR = set(permutations((0, 1, -1)))
ZERO = {(0, 0, 0)}
STAR_CLASSES = {
    -2: FULL,
     0: FULL | COLOR,
     1: COLOR,
     2: ZERO | COLOR,
     4: ZERO,
}


def star_transfer_cube():
    edges = cube_edges()
    inc = build_incidence(edges, 8)
    even = [v for v in range(8) if v.bit_count() % 2 == 0]
    odd = [v for v in range(8) if v.bit_count() % 2 == 1]
    assert len(even) == len(odd) == 4
    result = {}
    for p, allowed in STAR_CLASSES.items():
        c = Counter()
        for stars in product(sorted(allowed), repeat=4):
            s = [None] * 12
            for v, triple in zip(even, stars):
                for edge_index, value in zip(inc[v], triple):
                    assert s[edge_index] is None
                    s[edge_index] = value
            if all(tuple(sorted(s[e] for e in inc[v]))
                   in {tuple(sorted(x)) for x in allowed} for v in odd):
                c[(sum(x*x for x in s), sum(s))] += 1
        result[p] = c
    return result


def total(counter):
    return sum(counter.values())


def moment2(counter):
    return sum(M*M*number for (_, M), number in counter.items())


def main():
    nstates, minima, ground = brute(cube_edges(), 8)
    assert nstates == 3**12 == 531441
    assert minima == {-2: -40, 0: -16, 1: -8, 2: 0, 4: 0}
    assert [total(ground[p]) for p in (-2, 0, 1, 2, 4)] == [450, 3054, 24, 69, 1]
    transfer = star_transfer_cube()
    for p in (-2, 0, 1, 2, 4):
        assert ground[p] == transfer[p], (p, ground[p], transfer[p])
    assert Counter({k: sum(num for (ki, M), num in ground[0].items() if ki == k)
                    for k in range(8, 13)}) == Counter({8: 24, 9: 288, 10: 1044, 11: 1248, 12: 450})
    assert {k: sum(num for (ki, M), num in ground[2].items() if ki == k)
            for k in (0, 4, 6, 8)} == {0: 1, 4: 12, 6: 32, 8: 24}
    assert moment2(ground[-2]) == 1152
    assert moment2(ground[0]) == 5280
    assert Fraction(moment2(ground[-2]), total(ground[-2])) == Fraction(64, 25)
    assert Fraction(moment2(ground[0]), total(ground[0])) == Fraction(880, 509)
    assert moment2(ground[1]) == moment2(ground[2]) == moment2(ground[4]) == 0
    nk, mk, gk = brute(k33_edges(), 6)
    assert nk == 3**9 == 19683
    assert mk == {-2: -30, 0: -12, 1: -6, 2: 0, 4: 0}
    for p in (-2, 0, 1, 2, 4):
        print(f"cube 2D/J={p:>2}: 2Emin={minima[p]:>3}, ground={total(ground[p])}")
    print(f"K3,3 state count: {nk}, minima: {mk}")
    print("Exact independent star-transfer and full-state checks: PASS")
    print("Cube zero-field low-T susceptibility/beta coefficients: 64/25, 880/509, then zero")


if __name__ == '__main__':
    main()
