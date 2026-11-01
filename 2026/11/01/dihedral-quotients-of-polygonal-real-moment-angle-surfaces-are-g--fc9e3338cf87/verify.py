#!/usr/bin/env python3
"""Finite independent orbit and mirror-circuit checks for polygon surfaces.

All enumerations are finite sanity checks. The accompanying written proof
establishes the statements for every polygon size in its stated domain.
"""
from collections import defaultdict
from math import gcd


def apply(mask, permutation):
    out = 0
    for index, target in enumerate(permutation):
        if mask & (1 << index):
            out |= 1 << target
    return out


def dihedral(n):
    return [tuple((sign * j + shift) % n for j in range(n))
            for sign in (1, -1) for shift in range(n)]


def orbit_euler(n):
    masks = range(1 << n)
    vertices = set((v,) for v in masks)
    edges = set()
    triangles = set()
    for low in masks:
        for i in range(n):
            a = 1 << i
            if not (low & a):
                edges.add((low, low | a))
            j = (i + 1) % n
            b = 1 << j
            ab = a | b
            if low & ab:
                continue
            high = low | ab
            edges.add(tuple(sorted((low, high))))
            triangles.add(tuple(sorted((low, low | a, high))))
            triangles.add(tuple(sorted((low, low | b, high))))
    group = dihedral(n)
    action = [tuple(apply(v, p) for v in masks) for p in group]

    def count_orbits(cells):
        pending = set(cells)
        result = 0
        while pending:
            c = pending.pop()
            result += 1
            for transformation in action:
                image = tuple(sorted(transformation[v] for v in c))
                pending.discard(image)
        return result

    ov, oe, of = (count_orbits(cells) for cells in (vertices, edges, triangles))
    return (ov, oe, of, ov - oe + of)


def mirror_components(n):
    group = dihedral(n)
    actions = [tuple(apply(v, p) for v in range(1 << n)) for p in group]
    orbit = {v: min(a[v] for a in actions) for v in range(1 << n)}
    mirror_edges = set()
    for center in range(n):
        reflection = tuple((center - j) % n for j in range(n))
        active = [(i,) for i in range(n) if reflection[i] == i]
        active += [(i, j) for i in range(n) for j in range(i + 1, n)
                   if reflection[i] == j and ((j - i) % n in (1, n - 1))]
        for indices in active:
            bits = sum(1 << i for i in indices)
            for low in range(1 << n):
                if low & bits:
                    continue
                if any((bool(low & (1 << i)) != bool(low & (1 << reflection[i])))
                       for i in range(n) if i not in indices):
                    continue
                mirror_edges.add(tuple(sorted((orbit[low], orbit[low | bits]))))
    neighbors = defaultdict(set)
    for a, b in mirror_edges:
        neighbors[a].add(b)
        neighbors[b].add(a)
    if not all(len(adj) == 2 for adj in neighbors.values()):
        raise AssertionError('Mirror quotient is not a union of circuits')
    remaining = set(neighbors)
    count = 0
    while remaining:
        count += 1
        root = remaining.pop()
        stack = [root]
        while stack:
            for other in neighbors[stack.pop()]:
                if other in remaining:
                    remaining.remove(other)
                    stack.append(other)
    return count, len(neighbors), len(mirror_edges)


def formula(n):
    base = (4 - n) * 2 ** (n - 2)
    fixed_rotation_sum = sum(2 ** gcd(n, j) for j in range(1, n))
    if (base + fixed_rotation_sum) % (2 * n):
        raise AssertionError('Nonintegral quotient Euler characteristic')
    quotient_chi = (base + fixed_rotation_sum) // (2 * n)
    rank = 1 - quotient_chi
    return quotient_chi, rank


def main():
    print('n  orbit_cells(V,E,F)  chi_quotient  free_rank  mirror_components')
    for n in range(5, 11):
        v, e, f, direct_chi = orbit_euler(n)
        chi, rank = formula(n)
        components, mv, me = mirror_components(n)
        assert direct_chi == chi
        assert mv == me
        if n % 2:
            assert components == 2 ** ((n - 3) // 2)
        print(f'{n:2}  ({v:4},{e:4},{f:4})  {direct_chi:6}  {rank:7}  {components:7}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
