#!/usr/bin/env python3
"""Independently enumerate eventual powers and check a component-size formula."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import gcd, lcm


def compose(f, g):
    return tuple(f[g[x]] for x in range(len(f)))


def power(f, e):
    result = tuple(range(len(f)))
    while e:
        if e & 1:
            result = compose(result, f)
        f = compose(f, f)
        e //= 2
    return result


def formula(e):
    n = len(e)
    roots = tuple(x for x in range(n) if e[x] == x)
    assert all(e[e[x]] == e[x] for x in range(n))
    sizes = tuple(sum(e[x] == r for x in range(n)) for r in roots)
    k = len(sizes)
    answer = Fraction(0)
    for p in permutations(range(k)):
        weight = Fraction(1)
        for i in range(k):
            weight *= sizes[p[i]] ** (sizes[i] - 1)
        done = set()
        for i in range(k):
            if i not in done:
                z, fraction = i, Fraction(1)
                while z not in done:
                    done.add(z)
                    fraction *= Fraction(sizes[z] - 1, sizes[z])
                    z = p[z]
                assert z == i
                weight *= (1 - fraction)
        answer += weight
    assert answer.denominator == 1
    return int(answer)


def verify(n):
    T = list(product(range(n), repeat=n))
    exponent = lcm(*range(1, n + 1))
    counts = Counter(power(f, exponent) for f in T)
    assert all(compose(e, e) == e for e in counts)
    for e, observed in counts.items():
        expected = formula(e)
        assert observed == expected, (n, e, observed, expected)
    assert sum(counts.values()) == n ** n
    if n == 3:
        assert sorted(counts.values()) == sorted([3]*3 + [2]*6 + [6])
    if n == 5:
        sizes_by_shape = defaultdict(set)
        for e, val in counts.items():
            roots = [i for i in range(n) if e[i] == i]
            shape = tuple(sorted([sum(e[x] == i for x in range(n)) for i in roots], reverse=True))
            sizes_by_shape[shape].add(val)
        assert sizes_by_shape[(4, 1)] == {17}
        assert sizes_by_shape[(3, 2)] == {11}
        assert sizes_by_shape[(3, 1, 1)] == {10}
        assert sizes_by_shape[(2, 2, 1)] == {10}
        assert sizes_by_shape[(5,)] == {125}
        assert sizes_by_shape[(1, 1, 1, 1, 1)] == {120}
        print('n=5 profiles:', {str(shape): (list(vals)[0], sum(1 for e in counts if tuple(sorted([sum(e[x] == i for x in range(n)) for i in range(n) if e[i]==i], reverse=True)) == shape)) for shape, vals in sizes_by_shape.items()})
    print(f'n={n}: {n ** n} maps, {len(counts)} idempotent components, formula agrees for every idempotent')


def graph_check(n):
    T = list(product(range(n), repeat=n))
    neighbors = {f: set() for f in T}
    for f in T:
        current = f
        seen_powers = {f}
        while True:
            current = compose(current, f)
            if current in seen_powers:
                break
            seen_powers.add(current)
            neighbors[f].add(current)
            neighbors[current].add(f)
    found = set()
    components = []
    for f in T:
        if f in found:
            continue
        todo = [f]
        found.add(f)
        s = set()
        while todo:
            u = todo.pop()
            s.add(u)
            for v in neighbors[u] - found:
                found.add(v)
                todo.append(v)
        components.append(s)
    exponent = lcm(*range(1, n + 1))
    assert all(len({power(f, exponent) for f in c}) == 1 for c in components)
    assert len(components) == len({power(f, exponent) for f in T})
    print(f'n={n}: power graph connectivity independently agrees')


if __name__ == '__main__':
    for n in range(1, 7):
        verify(n)
    for n in range(1, 6):
        graph_check(n)
    print('VERIFY_OK')
