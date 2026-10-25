"""Finite independent checks for Cartesian interval-box implications.
Usage: python verify.py (Python standard library only).
"""
from itertools import product, combinations
from math import comb, prod, ceil, log2
from collections import Counter
from random import Random


def instance(sizes):
    pts = list(product(*(range(q) for q in sizes)))
    n = len(pts)
    boxes = []
    for u in pts:
        row = []
        for v in pts:
            mask = 0
            for j, z in enumerate(pts):
                if all(min(u[i],v[i]) <= z[i] <= max(u[i],v[i]) for i in range(len(sizes))):
                    mask |= 1 << j
            row.append(mask)
        boxes.append(row)

    def box_closure(s):
        if not s:
            return 0
        selected = [pts[i] for i in range(n) if s >> i & 1]
        lo = tuple(min(x[j] for x in selected) for j in range(len(sizes)))
        hi = tuple(max(x[j] for x in selected) for j in range(len(sizes)))
        return sum(1 << i for i, x in enumerate(pts)
                   if all(lo[j] <= x[j] <= hi[j] for j in range(len(sizes))))

    rules = [(i, j, boxes[i][j]) for i in range(n)
             for j in range(i+1, n)
             if boxes[i][j] != (1 << i | 1 << j)]
    expected_count = comb(n, 2) - sum((q - 1) * (n // q) for q in sizes)
    assert len(rules) == expected_count

    def forward(s):
        val = s
        for i, j, target in rules:
            if (s >> i & 1) and (s >> j & 1):
                val |= target
        return val

    def finish(s):
        steps = 0
        while True:
            t = forward(s)
            if t == s:
                return steps, s
            s = t
            steps += 1
            assert steps <= 6

    return pts, rules, box_closure, finish


def exhaustive(sizes, check_pseudointents=False):
    pts, rules, close, finish = instance(sizes)
    n = len(pts)
    hist = Counter()
    for s in range(1 << n):
        count, got = finish(s)
        assert got == close(s), (sizes, s)
        hist[count] += 1
    expected_depth = 0 if (len(sizes) == 1 and sizes[0] == 2) else (1 if len(sizes) == 1 else ceil(log2(len(sizes))))
    assert max(hist) == expected_depth, (sizes, hist, expected_depth)

    if check_pseudointents:
        # Directly compute the recursive, cardinality-ordered definition.
        pseudo = []
        for s in sorted(range(1 << n), key=lambda m: (m.bit_count(), m)):
            if close(s) != s and all((q & s) != q or (close(q) & s) == close(q) for q in pseudo):
                pseudo.append(s)
        expected = sorted((1 << i | 1 << j) for i, j, _ in rules)
        assert sorted(pseudo) == expected, (sizes, sorted(pseudo), expected)

    print('EXHAUSTIVE', sizes, 'candidate_sets', 1 << n,
          'canonical_rules', len(rules), 'depth_histogram', dict(sorted(hist.items())),
          'pseudo_intents_checked', check_pseudointents, 'PASS')


def sampled(sizes, count):
    pts, rules, close, finish = instance(sizes)
    n = len(pts)
    rng = Random(20261018)
    for k in range(count):
        rate = (k % 9 + 1) / 10
        s = sum(1 << i for i in range(n) if rng.random() < rate)
        depth, got = finish(s)
        assert got == close(s)
        assert depth <= ceil(log2(len(sizes)))
    print('SAMPLED', sizes, 'candidate_sets', count, 'PASS')


def sharp_dimension(sizes):
    pts, _, close, finish = instance(sizes)
    d = len(sizes)
    if d < 2:
        return
    seeds = [tuple(1 if j == i else 0 for j in range(d)) for i in range(d)]
    mask = sum(1 << pts.index(v) for v in seeds)
    target = tuple(1 for j in range(d))
    depth, got = finish(mask)
    assert got == close(mask) and (got >> pts.index(target) & 1)
    assert depth == ceil(log2(d)), (sizes, depth)
    print('SHARPNESS', sizes, 'basis_vectors', d, 'depth', depth, 'PASS')


if __name__ == '__main__':
    exhaustive((2,), True)
    exhaustive((3,), True)
    exhaustive((2, 2), True)
    exhaustive((3, 2), True)
    exhaustive((2, 2, 2), True)
    exhaustive((3, 3), True)
    exhaustive((2, 2, 2, 2), False)
    sampled((3, 2, 2), 3000)
    sampled((2, 2, 2, 2, 2), 3000)
    for sizes in ((2, 2), (2, 2, 2), (2, 2, 2, 2), (2,) * 5, (2,) * 6):
        sharp_dimension(sizes)
    print('VERIFY_OK grid_closure=PASS pseudo_intent_characterization=PASS exact_minimal_rule_count=PASS exact_parallel_depth=PASS')
