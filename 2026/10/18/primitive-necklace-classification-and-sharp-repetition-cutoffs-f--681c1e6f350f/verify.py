#!/usr/bin/env python3
"""Exhaustive bounded FO2 semantic-type tests for colored directed cycles.

Only Python 3 standard library is used.  This tests finite cases; it does not
replace the unrestricted two-pebble argument in RESULT.md.
"""
from collections import defaultdict
from itertools import product


def rotate_min(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def predicted_type(w):
    n = len(w)
    d = next(d for d in range(1, n + 1) if n % d == 0 and w == w[:d] * (n // d))
    k = n // d
    ceiling = 4 if d == 1 else 3 if d == 2 else 2
    return (rotate_min(w[:d]), min(k, ceiling))


def verify(colors, max_length, expected_models, expected_theories):
    models = []
    for n in range(1, max_length + 1):
        necklaces = {rotate_min(tuple(w)) for w in product(range(colors), repeat=n)}
        models.extend(sorted(necklaces))
    atoms, rebind_x, rebind_y, offsets = [], [], [], []
    for w in models:
        n = len(w)
        base = len(atoms)
        offsets.append(base)
        for x in range(n):
            for y in range(n):
                atoms.append((w[x], w[y], x == y, (x + 1) % n == y, (y + 1) % n == x))
                rebind_x.append(tuple(base + v*n + y for v in range(n)))
                rebind_y.append(tuple(base + x*n + v for v in range(n)))
    unique = {a: i for i, a in enumerate(sorted(set(atoms)))}
    types = [unique[a] for a in atoms]
    while True:
        signatures = [
            (types[i], tuple(sorted(set(types[j] for j in rebind_x[i]))),
             tuple(sorted(set(types[j] for j in rebind_y[i]))))
            for i in range(len(types))
        ]
        index = {a: i for i, a in enumerate(sorted(set(signatures)))}
        updated = [index[s] for s in signatures]
        if updated == types:
            break
        types = updated
    # Complete stable two-pebble types on all ordered pairs determine FO2.
    # On closed sentences, each structure is distinguished by the set of
    # unary (diagonal) types it realizes.
    predicted_to_actual = defaultdict(set)
    actual_to_predicted = defaultdict(set)
    for model, off in zip(models, offsets):
        n = len(model)
        t = tuple(sorted({types[off + x*n + x] for x in range(n)}))
        p = predicted_type(model)
        predicted_to_actual[p].add(t)
        actual_to_predicted[t].add(p)
    assert len(models) == expected_models, (len(models), expected_models)
    assert len(predicted_to_actual) == len(actual_to_predicted) == expected_theories, (
        len(predicted_to_actual), len(actual_to_predicted), expected_theories)
    assert all(len(s) == 1 for s in predicted_to_actual.values())
    assert all(len(s) == 1 for s in actual_to_predicted.values())
    return len(models), len(actual_to_predicted)


if __name__ == '__main__':
    assert verify(2, 9, 153, 140) == (153, 140)
    assert verify(3, 6, 225, 219) == (225, 219)
    print('FO2_CYCLE_VERIFY_OK binary=153/140 ternary=225/219')
