#!/usr/bin/env python3
"""Reproduce finite checks for exact strong-majority edge signings of Boolean cubes.

The all-dimensional classification relies on the mathematical Walsh proof;
this script independently verifies finite instances and the orbit laws.
"""
from itertools import product


def cube_edges(d):
    return [(x, x ^ (1 << i), i) for i in range(d)
            for x in range(1 << d) if not ((x >> i) & 1)]


def neighbors(edges):
    return [[j for j, (v, w, _) in enumerate(edges)
             if j != k and (v in (a, b) or w in (a, b))]
            for k, (a, b, _) in enumerate(edges)]


def parity_sign(x):
    return -1 if x.bit_count() % 2 else 1


def signature(d, epsilon):
    return tuple(epsilon[i] * parity_sign(a & ~(1 << i))
                 for a, _, i in cube_edges(d))


def balanced(signs, nbs):
    return all(sum(signs[j] for j in neigh) == 0 for neigh in nbs)


def brute_force(d):
    edges = cube_edges(d)
    nbs = neighbors(edges)
    predicted = {signature(d, eps) for eps in product((-1, 1), repeat=d)}
    if len(predicted) != 1 << d:
        raise AssertionError('the explicit edge patterns are not distinct')
    if not all(balanced(s, nbs) for s in predicted):
        raise AssertionError('an explicit coloring is not balanced')
    actual = {signs for signs in product((-1, 1), repeat=len(edges))
              if balanced(signs, nbs)}
    assert actual == predicted, (d, len(actual), len(predicted))
    print('exhaustive dimension', d, 'edges', len(edges),
          'balanced two-colorings', len(actual))


def theory_checks(d):
    edges = cube_edges(d)
    nbs = neighbors(edges)
    signs = {signature(d, eps) for eps in product((-1, 1), repeat=d)}
    assert len(signs) == 1 << d
    assert all(balanced(s, nbs) for s in signs)
    # A generator of the translation group changes epsilon_i by
    # (-1)^(sum of all translation bits except bit i).
    start = tuple([1] * d)
    orbit = {tuple(parity_sign(a & ~(1 << i)) for i in range(d))
             for a in range(1 << d)}
    if d % 2 == 0:
        assert len(orbit) == 1 << d
    else:
        assert len(orbit) == 1 << (d - 1)
        assert all(__import__('math').prod(t) == 1 for t in orbit)
    print('constructive dimension', d, 'edges', len(edges),
          'valid colorings', len(signs), 'translation orbit', len(orbit))


def main():
    for d in (2, 3):
        brute_force(d)
    for d in range(2, 9):
        theory_checks(d)
    print('ALL FINITE CHECKS PASSED; infinite-dimensional rigidity is in the proof.')


if __name__ == '__main__':
    main()
