#!/usr/bin/env python3
"""Exact checks of finite Boolean non-contingency types over KD45."""
from itertools import combinations
from random import Random


def supports(m):
    return [s for s in range(1, 1 << m)]


def signature(s, m):
    result = 0
    for a in range(1 << m):
        if s & a == s or s & a == 0:
            result |= 1 << a
    return result


def check_profiles(k):
    m = 1 << k
    sigs = {}
    for s in supports(m):
        sigs.setdefault(signature(s, m), []).append(s)
    assert len(sigs) == (1 << m) - m
    for group in sigs.values():
        if len(group) > 1:
            assert len(group) == m
            assert set(group) == {1 << b for b in range(m)}
        else:
            assert group[0].bit_count() >= 2 or m == 1
    print(f'k={k}, support_profiles={len(sigs)}, pointed_profiles={m*len(sigs)}')


def model(k, a, s, redundant=0):
    m = 1 << k
    vals = [b for b in range(m) if s >> b & 1]
    if redundant:
        vals += [vals[i % len(vals)] for i in range(redundant)]
    count = len(vals)
    succs = [list(range(count)) for _ in range(count)]
    if a in vals:
        root = vals.index(a)
    else:
        root = count
        vals.append(a)
        succs.append(list(range(count)))
    assert all(succs[u] == list(range(count)) for u in range(count))
    assert set(vals[j] for j in succs[root]) == set(b for b in range(m) if s >> b & 1)
    return vals, succs, root


def val(formula, vals, succs, w):
    op = formula[0]
    if op == 'atom':
        return bool(vals[w] >> formula[1] & 1)
    if op == 'const':
        return formula[1]
    if op == 'not':
        return not val(formula[1], vals, succs, w)
    if op == 'and':
        return val(formula[1], vals, succs, w) and val(formula[2], vals, succs, w)
    if op == 'delta':
        bits = [val(formula[1], vals, succs, v) for v in succs[w]]
        return all(x == bits[0] for x in bits)
    raise AssertionError(op)


def random_formula(rng, k, depth):
    if depth <= 0:
        return ('atom', rng.randrange(k))
    op = rng.choice(['atom', 'not', 'and', 'delta'])
    if op == 'atom':
        return ('atom', rng.randrange(k))
    if op == 'not':
        return ('not', random_formula(rng, k, depth - 1))
    if op == 'and':
        return ('and', random_formula(rng, k, depth - 1), random_formula(rng, k, depth - 1))
    return ('delta', random_formula(rng, k, depth - 1))


def check_nested(k):
    m = 1 << k
    rng = Random(0x45 + k)
    reps = []
    for a in range(m):
        for s in supports(m):
            base = model(k, a, s)
            duplicate = model(k, a, s, redundant=2)
            reps.append((base, duplicate))
    for j in range(300):
        f = random_formula(rng, k, 1 + (j % 5))
        for base, duplicate in reps:
            assert val(f, *base) == val(f, *duplicate)
        # Every singleton successor support has the same theory at fixed root.
        for a in range(m):
            answers = [val(f, *model(k, a, 1 << b)) for b in range(m)]
            assert len(set(answers)) == 1
    print(f'k={k}, nested_formulas=300, canonical_profiles={len(reps)}')


def check_sharp(k):
    m = 1 << k
    passing = []
    for s in supports(m):
        valid = all(not (s & a == s or s & a == 0) for a in range(1, (1 << m) - 1))
        if valid:
            passing.append(s)
    assert passing == [(1 << m) - 1]
    assert len(model(k, 0, passing[0])[0]) == m
    print(f'k={k}, full_support_detector_unique=True, minimal_worlds={m}')


if __name__ == '__main__':
    for k in range(4):
        check_profiles(k)
    for k in (1, 2):
        check_nested(k)
    for k in (1, 2, 3):
        check_sharp(k)
    print('ALL TESTS PASS')
