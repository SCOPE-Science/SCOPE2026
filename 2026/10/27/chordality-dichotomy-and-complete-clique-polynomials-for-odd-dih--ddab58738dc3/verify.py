#!/usr/bin/env python3
"""Finite checks of the odd dihedral endomorphism commuting graph."""

from itertools import combinations, product


def quandle_endomorphisms(n):
    return {
        f
        for f in product(range(n), repeat=n)
        if all(f[(2*y-x) % n] == (2*f[y]-f[x]) % n
               for x, y in product(range(n), repeat=2))
    }


def affine_endomorphisms(n):
    return {tuple((a*x+b) % n for x in range(n))
            for a, b in product(range(n), repeat=2)}


def commute_by_composition(u, v, n):
    a, b = u[0]+1, u[1]
    c, d = v[0]+1, v[1]
    return (a*d+b) % n == (c*b+d) % n  # Both compositions have slope a*c.


def elimination_order(p, e):
    points = list(product(range(p**e), repeat=2))
    if e == 0:
        return points
    order = [v for v in points if v[0] % p or v[1] % p]
    if e == 1:
        return order + [(0, 0)]
    step = p**(e-2)
    for x, y in elimination_order(p, e-2):
        order.extend((p*(x+i*step), p*(y+j*step))
                     for i, j in product(range(p), repeat=2))
    return order


def check_order(p, e):
    n = p**e
    order = elimination_order(p, e)
    assert len(order) == n*n and set(order) == set(product(range(n), repeat=2))
    later = [set() for _ in order]
    for i, j in combinations(range(len(order)), 2):
        x, y = order[i]
        z, w = order[j]
        adjacent = commute_by_composition(order[i], order[j], n)
        assert adjacent == ((x*w-y*z) % n == 0)
        if adjacent:
            later[i].add(j)
    for neighbors in later:
        assert all(j in later[i] for i, j in combinations(sorted(neighbors), 2))
    assert max(map(len, later)) + 1 == n


def check_cycle(r, s):
    n = r*s
    er = (s*pow(s, -1, r)) % n
    es = (1-er) % n
    points = [(er, 0), (es, 0), (0, er), (0, es)]
    assert len(set(points)) == 4
    for i, j in combinations(range(4), 2):
        assert commute_by_composition(points[i], points[j], n) == ((j-i) in (1, 3))


if __name__ == '__main__':
    for n in (3, 5):
        assert quandle_endomorphisms(n) == affine_endomorphisms(n)
    for p, e in ((3, 1), (5, 1), (3, 2), (5, 2), (3, 3)):
        check_order(p, e)
    for r, s in ((3, 5), (3, 7), (9, 5)):
        check_cycle(r, s)
    print('VERIFY_OK affine=3,5 orders=3,5,9,25,27 cycles=15,21,45')
