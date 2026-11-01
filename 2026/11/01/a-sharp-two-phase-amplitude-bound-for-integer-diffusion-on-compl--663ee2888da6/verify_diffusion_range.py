#!/usr/bin/env python3
"""Finite independent checks for a sharp bipartite diffusion orbit-amplitude theorem.

All computations are integer exact. Finite checks support, but do not replace,
the all-size proof in RESULT.md.
"""
from itertools import combinations_with_replacement
from math import comb


def step(z, a, b):
    left, right = z[:a], z[a:]
    return tuple(u + sum((v > u) - (v < u) for v in right) for u in left) + tuple(
        v + sum((u > v) - (u < v) for u in left) for v in right
    )


def edge_reversal(x, y, a, b):
    def sgn(t):
        return (t > 0) - (t < 0)
    return all(sgn(x[i] - x[a+j]) + sgn(y[i] - y[a+j]) == 0
               for i in range(a) for j in range(b))


def maxwidth(a, b):
    return a + b + max(a, b) - 2


def extremizer(a, b):
    assert a >= 2 and b >= 2
    if a <= b:
        h = a + b - 1
        return (0,) * (a - 1) + (h - 1,) + (h,) * b
    # symmetric exchange: smaller shore gets the low values
    h = a + b - 1
    return (h,) * a + (0,) * (b - 1) + (h - 1,)


def test_extremizers():
    cases = 0
    for a in range(2, 15):
        for b in range(2, 15):
            x = extremizer(a, b)
            y = step(x, a, b)
            assert x != y and step(y, a, b) == x
            assert min(x + y) == 0
            assert max(x + y) == maxwidth(a, b)
            assert edge_reversal(x, y, a, b)
            cases += 1
    return cases


def exhaustive_local(a, b):
    t = maxwidth(a, b)
    tested = 0
    periodic = 0
    best = -1
    witness = None
    # Sorted shores are exhaustive up to independent within-shore relabelling.
    # Search a strictly larger range than the claimed cutoff.
    upper = t + 2
    lefts = list(combinations_with_replacement(range(upper + 1), a))
    rights = list(combinations_with_replacement(range(upper + 1), b))
    for l in lefts:
        for r in rights:
            if min(l[0], r[0]) != 0:
                continue
            tested += 1
            x = l + r
            y = step(x, a, b)
            if min(y) < 0 or x == y or step(y, a, b) != x:
                continue
            assert edge_reversal(x, y, a, b)
            periodic += 1
            width = max(x + y)
            assert width <= t, (a, b, x, y, width, t)
            if width > best:
                best = width
                witness = x
    assert best == t, (a, b, best, t)
    print(f'K_{{{a},{b}}}: search [0,{upper}], sorted states tested {tested}, '
          f'primitive two-phase representatives {periodic}, '
          f'maximal observed width {best}, exemplar {witness}')
    return tested, periodic


def main():
    print(f'Explicit sharp constructions verified for {test_extremizers()} size pairs.')
    total_tested = total_periodic = 0
    for a, b in [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4)]:
        u, v = exhaustive_local(a, b)
        total_tested += u
        total_periodic += v
    print(f'Sorted candidate states tested: {total_tested}')
    print(f'Qualifying primitive two-phase representatives: {total_periodic}')
    print('BIPARTITE_DIFFUSION_WIDTH_ALL_CHECKS_PASSED')


if __name__ == '__main__':
    main()
