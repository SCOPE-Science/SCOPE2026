#!/usr/bin/env python3
"""Finite checks of the rank enumerator for self-inverse cycle partial isometries.

Only Python standard-library components are used. This verifies finite cases,
not the statement for arbitrary cycle length; the latter is proved separately.
"""
from itertools import combinations, permutations
from math import comb


def multiply(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power(poly, exponent):
    out = [1]
    for _ in range(exponent):
        out = multiply(out, poly)
    return out


def add(*polynomials):
    out = [0] * max(map(len, polynomials))
    for poly in polynomials:
        for index, value in enumerate(poly):
            out[index] += value
    return out


def formula(n):
    assert n >= 4
    identity = power([1, 1], n)
    if n % 2:
        reflecting = multiply([1, 1], power([1, 0, 1], (n - 1) // 2))
        out = add(identity, [n * a for a in reflecting])
        out[0] -= n
        out[1] -= n
    else:
        m = n // 2
        vertex_reflection = multiply([1, 2, 1], power([1, 0, 1], m - 1))
        free_involution = power([1, 0, 1], m)
        out = add(identity, [m * a for a in vertex_reflection],
                  [(m + 1) * a for a in free_involution])
        out[0] -= n + 1
        out[1] -= n
        out[2] -= n
    return out


def brute_from_metric(n):
    """Enumerate domains and all involutive permutations; apply metric directly."""
    out = [0] * (n + 1)

    def dist(x, y):
        d = abs(x - y)
        return min(d, n - d)

    for rank in range(n + 1):
        for domain in combinations(range(n), rank):
            for targets in permutations(domain):
                map_xy = dict(zip(domain, targets))
                if not all(map_xy[map_xy[x]] == x for x in domain):
                    continue
                if not all(dist(x, y) == dist(map_xy[x], map_xy[y])
                           for x, y in combinations(domain, 2)):
                    continue
                out[rank] += 1
    return out


def all_dihedral_restrictions(n):
    """All distinct restrictions of rotations and reflections of the cycle."""
    all_maps = set()
    for shift in range(n):
        for sign in (+1, -1):
            images = [(sign * x + shift) % n for x in range(n)]
            for mask in range(1 << n):
                partial = tuple((x, images[x]) for x in range(n) if mask & (1 << x))
                all_maps.add(partial)
    return all_maps


def brute_from_all_dihedral_restrictions(n):
    """Deduplicate restrictions, then compare the maps with their inverses."""
    all_maps = all_dihedral_restrictions(n)
    out = [0] * (n + 1)
    for partial in all_maps:
        inverse = tuple(sorted((b, a) for a, b in partial))
        if inverse == partial:
            out[len(partial)] += 1
    return out


def all_metric_isometries(n):
    """Independently enumerate ALL metric partial injections (not only involutions)."""
    out = set()

    def dist(x, y):
        d = abs(x - y)
        return min(d, n - d)

    for rank in range(n + 1):
        for dom in combinations(range(n), rank):
            for targets in permutations(range(n), rank):
                mp = dict(zip(dom, targets))
                if all(dist(x, y) == dist(mp[x], mp[y])
                       for x, y in combinations(dom, 2)):
                    out.add(tuple(zip(dom, targets)))
    return out


def check():
    for n in range(4, 10):
        expected = formula(n)
        observed = brute_from_metric(n)
        assert observed == expected, (n, observed, expected)
        assert expected[0] == 1
        assert expected[1] == n
        assert expected[2] == 2 * comb(n, 2)
        print('METRIC_OK', n, observed)
    for n in range(4, 8):
        metric = all_metric_isometries(n)
        dihedral = all_dihedral_restrictions(n)
        assert metric == dihedral, (n, len(metric), len(dihedral))
        print('EXTENSION_OK', n, len(metric))
    for n in range(4, 13):
        expected = formula(n)
        observed = brute_from_all_dihedral_restrictions(n)
        assert observed == expected, (n, observed, expected)
        print('DIHEDRAL_OK', n, sum(observed))
    print('VERIFY_OK')


if __name__ == '__main__':
    check()
