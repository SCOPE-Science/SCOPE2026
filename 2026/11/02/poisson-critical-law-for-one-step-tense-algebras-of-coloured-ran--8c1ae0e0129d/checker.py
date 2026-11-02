#!/usr/bin/env python3
"""Finite exact tests of colour signatures and existential tense closure.

Only finite mathematical objects and independently reproducible checks occur here.
"""
from itertools import product
from fractions import Fraction


def partition_from_generators(n, generators):
    groups = {}
    for v in range(n):
        signature = tuple(int((g >> v) & 1) for g in generators)
        groups.setdefault(signature, 0)
        groups[signature] |= 1 << v
    return frozenset(groups.values())


def parts_to_algebra(parts):
    sets = {0}
    for atom in parts:
        sets |= {s | atom for s in list(sets)}
    return sets


def image(n, edges, subset, reverse):
    out = 0
    for v in range(n):
        for w in range(n):
            if (subset >> w) & 1 and (edges >> ((w * n + v) if reverse else (v * n + w))) & 1:
                out |= 1 << v
                break
    return out


def assess(n, colours, edges):
    q = 2
    bases = [sum(1 << v for v, a in enumerate(colours) if a == b) for b in range(q)]
    f = [image(n, edges, base, False) for base in bases]
    p = [image(n, edges, base, True) for base in bases]
    b0 = parts_to_algebra(partition_from_generators(n, bases))
    b1_parts = partition_from_generators(n, bases + f + p)
    b1 = parts_to_algebra(b1_parts)
    # Direct closure from generator subsets, independent of signature-fibre partition.
    full = (1 << n) - 1
    generated = {0, full, *(bases + f + p)}
    while True:
        old_size = len(generated)
        snapshot = list(generated)
        generated.update(full ^ a for a in snapshot)
        snapshot = list(generated)
        generated.update(a | b for a in snapshot for b in snapshot)
        if len(generated) == old_size:
            break
    assert generated == b1
    assert b0 <= b1
    # Full modal closure coincides with first-step closure at B0 exactly when B0 is stable.
    b0_closed = all(image(n, edges, subset, rev) in b0 for subset in b0 for rev in (False, True))
    assert b0_closed == (b0 == b1)
    missing = {}
    for a in range(q):
        for b in range(q):
            for s, outcome in (('+', f[b]), ('-', p[b])):
                missing[a, b, s] = sum(
                    1 for v in range(n)
                    if colours[v] == a and ((outcome >> v) & 1) == 0
                )
    # On the disjoint-defect and present-good-colour event, each flag gives one new atom.
    defect_count = []
    for v in range(n):
        defect_count.append(sum(1 for b in range(q) for modal_set in (f[b], p[b]) if not ((modal_set >> v) & 1)))
    if all(any(colours[v] == a and defect_count[v] == 0 for v in range(n)) for a in range(q)) and max(defect_count) <= 1:
        assert len(b1_parts) == q + sum(x > 0 for x in missing.values())
        assert (b0_closed == all(x == 0 for x in missing.values()))
    return missing


def main():
    census = 0
    for n in range(1, 4):
        for colours in product(range(2), repeat=n):
            n_edges = 1 << (n * n)
            totals = {(a, b, s): 0 for a in range(2) for b in range(2) for s in ('+', '-')}
            for edges in range(n_edges):
                defects = assess(n, colours, edges)
                for key, count in defects.items():
                    totals[key] += count
                census += 1
            for (a, b, s), total in totals.items():
                na = sum(v == a for v in colours)
                nb = sum(v == b for v in colours)
                observed_mean = Fraction(total, n_edges)
                exact_mean = Fraction(na, 2 ** nb)
                assert observed_mean == exact_mean, (n, colours, a, b, s, observed_mean, exact_mean)
    # Loop-free and full relations, among others, are present in every enumeration.
    assert census == sum((2 ** n) * (2 ** (n * n)) for n in range(1, 4))
    print('EXHAUSTIVE_CASES', census)
    print('ALL_CHECKS_OK')


if __name__ == '__main__':
    main()
