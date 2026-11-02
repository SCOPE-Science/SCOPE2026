#!/usr/bin/env python3
"""Finite cross-checks for the first positive defect of the Kreisel-Putnam axiom.
Uses exact bit-mask downsets, two independent failure predicates, and a complete
natural-label enumeration. All universal claims require the accompanying proof.
"""
from itertools import combinations


def natural_posets(n):
    pairs = tuple(combinations(range(n), 2))
    for choice in range(1 << len(pairs)):
        down = [1 << j for j in range(n)]
        for t, (i, j) in enumerate(pairs):
            if choice >> t & 1:
                down[j] |= 1 << i
        if any((down[j] >> i & 1) and (down[i] & ~down[j])
               for j in range(n) for i in range(j)):
            continue
        yield tuple(down)


def downsets(pred):
    return tuple(I for I in range(1 << len(pred))
                 if all(not (I >> j & 1) or I & pred[j] == pred[j]
                        for j in range(len(pred))))


def direct_failures(pred, ideals=None):
    ideals = downsets(pred) if ideals is None else ideals
    impl = {(a, b): sum(1 << j for j, d in enumerate(pred)
                        if (d & a & ~b) == 0)
            for a in ideals for b in ideals}
    failures = []
    for a in ideals:
        not_a = impl[a, 0]
        for b in ideals:
            left_b = impl[not_a, b]
            for c in ideals:
                if impl[not_a, b | c] & ~(left_b | impl[not_a, c]):
                    failures.append((a, b, c))
    return failures


def structural_failures(pred):
    ideals = downsets(pred)
    failures = []
    for a in ideals:
        X = sum(1 << j for j, d in enumerate(pred) if d & a == 0)
        for b in ideals:
            for c in ideals:
                if any((X & d & ~(b | c)) == 0 and
                       (X & d & ~b) != 0 and (X & d & ~c) != 0
                       for d in pred):
                    failures.append((a, b, c))
    return failures


def extremal_poset(h):
    assert h >= 11
    # r < u, r < v, s isolated, and an upper chain above all four.
    # Vertex indices: r=0, u=1, v=2, s=3, c_0=4, ..., c_{h-11}.
    n = h - 6
    return (1, 3, 5, 8) + tuple((1 << (i + 1)) - 1
                               for i in range(4, n))


def explicit_extremal_downsets(p):
    n = len(p)
    base = tuple(I for I in range(16) if all(not(I >> j & 1) or I & p[j] == p[j] for j in range(4)))
    return base + tuple((1 << j) - 1 for j in range(5, n+1))

def run():
    total = 0
    positive = 0
    minimum = None
    cardinality_nine = []
    for n in range(1, 7):
        count = nonvalid = 0
        for p in natural_posets(n):
            count += 1
            f = direct_failures(p)
            if n <= 5:
                g = structural_failures(p)
                assert f == g, (n, p, f[:3], g[:3])
            if f:
                nonvalid += 1
                assert len(f) >= 8, (n, p, len(f))
                minimum = min(minimum or len(f), len(f))
                if len(downsets(p)) == 9:
                    cardinality_nine.append((n, p, len(f)))
        total += count
        positive += nonvalid
        print(f'NATURAL_POSETS_PASS n={n} count={count} nonvalid={nonvalid}',flush=True)
    assert total == 5231 and minimum == 8
    assert cardinality_nine == [(4, (1, 2, 4, 15), 24)]
    print('NINE_ELEMENT_UNIQUE_BOUNDARY_PASS defects=24',flush=True)
    for h in range(11, 31):
        p = extremal_poset(h)
        ideals = explicit_extremal_downsets(p)
        assert len(ideals) == h
        assert all(all(not(I >> j & 1) or (I & p[j]) == p[j] for j in range(len(p))) for I in ideals)
        f = direct_failures(p, ideals)
        assert len(f) == 8, (h, len(f))
    print('EVERY_SIZE_EXPLICIT_CONSTRUCTION_PASS h=11..30 defects=8',flush=True)
    print(f'ALL_KP_FIRST_DEFECT_CHECKS_PASS total_posets={total} positive={positive}',flush=True)


if __name__ == '__main__':
    run()
