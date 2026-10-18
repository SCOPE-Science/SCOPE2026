#!/usr/bin/env python3
"""Direct exhaustive checks of rooted-tree retraction rank polynomials.

Usage: python3 verify.py
The morphism census evaluates all local vertex functions and tests F(F(v))=F(v)
without using the subtree-retraction recurrence.
"""
from collections import Counter
from itertools import product
from math import comb


def shape_census(b, h):
    # Each tuple (size, all_morphisms_into_image, retracts_onto_image)
    # represents ONE labeled saturated rooted image subtree.
    shapes = [(1, 1, 1)]
    for _ in range(h):
        child_options = [None] + shapes
        new = []
        for items in product(child_options, repeat=b):
            kept = [item for item in items if item is not None]
            if not kept:
                continue
            size = 1 + sum(s for s, a, r in kept)
            target_sum = sum(a for s, a, r in kept)
            number_maps = target_sum ** b
            number_retracts = target_sum ** (b - len(kept))
            for s, a, r in kept:
                number_retracts *= r
            new.append((size, number_maps, number_retracts))
        shapes = new
    poly = Counter()
    for s, a, r in shapes:
        poly[s] += r
    return poly, len(shapes)


def brute_endomorphisms(b, h):
    vertices = [()]
    for depth in range(1, h + 1):
        vertices += list(product(range(b), repeat=depth))
    index = {v: i for i, v in enumerate(vertices)}
    parent = [-1] + [index[v[:-1]] for v in vertices[1:]]
    letter = [-1] + [v[-1] for v in vertices[1:]]
    children = [[index[v + (a,)] for a in range(b)] if len(v) < h else None
                for v in vertices]
    internals = [i for i, v in enumerate(vertices) if len(v) < h]
    choices = list(product(range(b), repeat=b))
    rows = Counter()
    checked = 0
    for labels in product(range(len(choices)), repeat=len(internals)):
        local = [None] * len(vertices)
        for internal_i, option_i in zip(internals, labels):
            local[internal_i] = choices[option_i]
        f = [0] * len(vertices)
        for i in range(1, len(vertices)):
            p = parent[i]
            f[i] = children[f[p]][local[p][letter[i]]]
        if all(f[f[i]] == f[i] for i in range(len(vertices))):
            rows[len(set(f))] += 1
        checked += 1
    return rows, checked


def edges(b, h):
    return (b ** (h + 1) - 1) // (b - 1)


def near_min_formula(b, h):
    exponent = b - 2 + (b - 1) * sum(b ** j for j in range(1, h))
    return b ** (h - 1) * comb(b, 2) * (2 ** exponent)


def run():
    cases = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2)]
    for b, h in cases:
        predicted, image_count = shape_census(b, h)
        actual, n_maps = brute_endomorphisms(b, h)
        assert actual == predicted, (b, h, actual, predicted)
        size = edges(b, h)
        assert set(predicted) == set(range(h + 1, size + 1))
        assert predicted[h + 1] == b ** h
        assert predicted[h + 2] == near_min_formula(b, h)
        assert predicted[size - 1] == (b ** h) * (b - 1)
        assert predicted[size] == 1
        print(f"b={b}, h={h}, all_morphisms_checked={n_maps}, "
              f"images={image_count}, idempotents={sum(actual.values())}, "
              f"rank_polynomial={dict(sorted(actual.items()))}")
    for b, h in [(2, 4), (3, 1), (4, 1)]:
        predicted, image_count = shape_census(b, h)
        assert predicted[h + 1] == b ** h
        assert predicted[h + 2] == near_min_formula(b, h)
        assert predicted[edges(b, h)-1] == b ** h * (b - 1)
        assert predicted[edges(b, h)] == 1
        print(f"recursion_only: b={b}, h={h}, images={image_count}, "
              f"idempotents={sum(predicted.values())}")
    print("ALL_EXACT_CHECKS_PASSED")


if __name__ == "__main__":
    run()
