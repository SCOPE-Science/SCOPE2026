#!/usr/bin/env python3
"""Exact finite checks for a poset/order-language comparison."""
from collections import Counter
from itertools import combinations


def boolean(n):
    E = [(mask.bit_count(), mask, 0) for mask in range(1 << n)]
    def le(x, y): return (x[1] & y[1]) == x[1]
    return E, le


def twisted_four():
    E = [(0, 0, 0)]
    E += [(1, 1 << j, 0) for j in range(4)]
    E += [(2, 3, j) for j in range(3)]
    E += [(2, 12, j) for j in range(3)]
    E += [(3, 15 ^ (1 << j), 0) for j in range(4)]
    E += [(4, 15, 0)]
    def le(x, y):
        return x == y or (x[0] < y[0] and (x[1] & y[1]) == x[1])
    return E, le


def twisted(n):
    assert n >= 4
    T, tle = twisted_four()
    B, ble = boolean(n - 4)
    E = [(a, b) for a in T for b in B]
    def le(x, y): return tle(x[0], y[0]) and ble(x[1], y[1])
    return E, le


def check_poset(E, le):
    assert len(E) == len(set(E))
    assert all(le(a, a) for a in E)
    assert all(not (le(a, b) and le(b, a)) for a in E for b in E if a != b)
    assert all(not (le(a, b) and le(b, c)) or le(a, c)
               for a in E for b in E for c in E)


def atomic(a, b, le):
    if a == b: return 0
    if le(a, b): return 1
    if le(b, a): return 2
    return 3


def compare_c2(A, leA, B, leB):
    # Canonical shared colour names, computed on a disjoint union.
    n = len(A)
    E = [(0, a) for a in A] + [(1, b) for b in B]
    typ = []
    for part_i, v in E:
        le = leA if part_i == 0 else leB
        typ.append([atomic(v, w, le) if part_i == part_j else -1 for part_j, w in E])
    colors = [0] * len(E)
    iterations = 0
    while True:
        signatures = []
        for i, c in enumerate(colors):
            cnt = Counter((colors[j], typ[i][j]) for j in range(len(E)) if typ[i][j] != -1)
            signatures.append((c, tuple(sorted(cnt.items()))))
        lookup = {sig: k for k, sig in enumerate(sorted(set(signatures)))}
        newer = [lookup[sig] for sig in signatures]
        iterations += 1
        if newer == colors: break
        if iterations > len(E) + 1: raise AssertionError('no stabilization')
        colors = newer
    return Counter(colors[:n]) == Counter(colors[n:]), iterations, len(set(colors))


def profile(P, le):
    return Counter((x[0], y[0], atomic(x, y, le)) for x in P for y in P)


def has_join(P, le, a, b):
    upper = [z for z in P if le(a, z) and le(b, z)]
    return any(all(le(z, u) for u in upper) for z in upper)


def check_three_by_three():
    # All possible bipartite rank-1/rank-2 incidences for the Boolean 3-cube.
    valid = []
    for bits in range(1 << 9):
        M = [[(bits >> (3*i + j)) & 1 for j in range(3)] for i in range(3)]
        if all(sum(row) == 2 for row in M) and all(sum(M[i][j] for i in range(3)) == 2 for j in range(3)):
            valid.append(M)
            assert all(sum(1-M[i][j] for i in range(3)) == 1 for j in range(3))
    assert len(valid) == 6
    print('B3: exactly six labelled 3-by-3 degree-two incidence matrices, all complements of matchings')


def main():
    check_three_by_three()
    B4, b4 = boolean(4)
    T4, t4 = twisted_four()
    check_poset(B4, b4)
    check_poset(T4, t4)
    assert profile(B4, b4) == profile(T4, t4)
    atoms = [v for v in T4 if v[0] == 1]
    assert not has_join(T4, t4, atoms[0], atoms[1])
    print('T4: 16 elements; reflexivity, antisymmetry, transitivity: PASS')
    print('T4: identical rank-pair ordered atomic profiles as B4: PASS')
    print('T4: two atoms lacking join: PASS')
    for n in range(4, 9):
        B, ble = boolean(n)
        T, tle = twisted(n)
        if n <= 5: check_poset(T, tle)
        ok, rounds, colors = compare_c2(B, ble, T, tle)
        assert ok
        print(f'n={n}, size={len(B)}, C2-colour-histogram-equal={ok}, rounds={rounds}, colours={colors}')
    print('ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
