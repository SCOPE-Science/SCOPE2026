#!/usr/bin/env python3
"""Finite checks for the colour-profile canonical model of unary guarded equivalence logic.

No external libraries required. These finite tests supplement, but do not establish,
the all-cardinality bisimulation proof.
"""
from itertools import product


def partitions(n):
    if n == 0:
        yield ()
        return
    for p in partitions(n-1):
        for j in range(len(p)):
            q = list(map(list, p))
            q[j].append(n-1)
            yield tuple(tuple(b) for b in q)
        yield p + ((n-1,),)


def spectrum(blocks, colors, c):
    return frozenset(tuple(min(2, sum(colors[a] == t for a in block))
                           for t in range(c)) for block in blocks)


def canonical(s, c):
    colors, blocks = [], []
    for v in sorted(s):
        block = []
        for t, x in enumerate(v):
            for _ in range(x):
                block.append(len(colors))
                colors.append(t)
        blocks.append(tuple(block))
    return tuple(blocks), tuple(colors)


def guarded_positions(blocks):
    singles = [(a,) for block in blocks for a in block]
    pairs = [(a, b) for block in blocks for a in block for b in block if a != b]
    return singles + pairs


def overlap_compatible(old_a, old_b, new_a, new_b):
    old_map = dict(zip(old_a, old_b))
    new_map = dict(zip(new_a, new_b))
    return all(new_map[a] == old_map[a] for a in new_a if a in old_map)


def bisimilar(blocks_a, colors_a, blocks_b, colors_b):
    A = guarded_positions(blocks_a)
    B = guarded_positions(blocks_b)
    states = {(i, j) for i, a in enumerate(A) for j, b in enumerate(B)
              if tuple(colors_a[x] for x in a) == tuple(colors_b[y] for y in b)}
    while True:
        reduced = set()
        for i, j in states:
            a, b = A[i], B[j]
            if all(any((i2, j2) in states and overlap_compatible(a, b, A[i2], B[j2])
                       for j2 in range(len(B))) for i2 in range(len(A))) and \
               all(any((i2, j2) in states and overlap_compatible(b, a, B[j2], A[i2])
                       for i2 in range(len(A))) for j2 in range(len(B))):
                reduced.add((i, j))
        if reduced == states:
            break
        states = reduced
    return (all(any((i,j) in states for j in range(len(B))) for i in range(len(A)))
            and all(any((i,j) in states for i in range(len(A))) for j in range(len(B))))


def actual_profile_test(blocks, colors, x, v):
    """Evaluate concrete GF witnesses using only E-guarded quantification."""
    cx = next(b for b in blocks if x in b)
    for t, expected in enumerate(v):
        zero = all(colors[y] != t for y in cx)
        one = any(colors[y] == t and all(colors[z] != t or z == y for z in cx)
                  for y in cx)
        at_least_two = any(colors[y] == t and any(colors[z] == t and z != y for z in cx)
                           for y in cx)
        if not (zero if expected == 0 else one if expected == 1 else at_least_two):
            return False
    return True


def checks():
    total = 0
    bisim_checks = 0
    for n in range(1, 6):
        for blocks in partitions(n):
            for colors in product(range(2), repeat=n):
                s = spectrum(blocks, colors, 2)
                mb, mc = canonical(s, 2)
                assert len(mc) <= 18
                assert spectrum(mb, mc, 2) == s
                for x in range(n):
                    observed = tuple(min(2, sum(colors[y] == t for b in blocks if x in b
                                                 for y in b)) for t in range(2))
                    for v in product(range(3), repeat=2):
                        assert actual_profile_test(blocks, colors, x, v) == (v == observed)
                total += 1
                if n <= 4 or (n == 5 and total % 13 == 0):
                    assert bisimilar(blocks, colors, mb, mc), (blocks, colors, mb, mc)
                    bisim_checks += 1
    for c in (1, 2, 4):
        s = frozenset(v for v in product(range(3), repeat=c) if any(v))
        blocks, colors = canonical(s, c)
        assert len(colors) == c * 3**c
        for killed in range(len(colors)):
            kept = [z for z in range(len(colors)) if z != killed]
            b2 = tuple(tuple(x for x in b if x != killed) for b in blocks)
            b2 = tuple(b for b in b2 if b)
            assert spectrum(b2, colors, c) != s
        print('SHARP_PROFILE_BOUND_OK', c, len(s), len(colors))
    print('CANONICAL_GUARDED_EQUIVALENCE_OK', total, bisim_checks)


if __name__ == '__main__':
    checks()
