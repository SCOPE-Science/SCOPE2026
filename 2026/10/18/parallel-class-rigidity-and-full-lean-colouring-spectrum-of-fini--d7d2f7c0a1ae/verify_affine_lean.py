"""Finite independent checks for affine-plane lean-colouring formulas.

This tests the claimed classification exhaustively at orders 2 and 3,
and tests every predicted partition at the prime orders 5 and 7 and at
order 4 (using F_4). It does not prove the statement for all planes.
Run: python verify_affine_lean.py
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def field(q):
    if q == 4:
        # Encode 0,1,a,a+1 as 0,1,2,3, with a^2=a+1.
        add = lambda a, b: a ^ b
        def multiply(a, b):
            table = ((0, 0, 0, 0),
                     (0, 1, 2, 3),
                     (0, 2, 3, 1),
                     (0, 3, 1, 2))
            return table[a][b]
        return add, multiply
    assert all(q % p for p in range(2, int(q ** 0.5) + 1))
    return lambda a, b: (a + b) % q, lambda a, b: (a * b) % q


def affine_plane(q):
    add, mul = field(q)
    points = [(a, b) for a in range(q) for b in range(q)]
    point_id = {p: i for i, p in enumerate(points)}
    parallel_classes = []
    for slope in range(q):
        parallel_classes.append(tuple(
            frozenset(point_id[(x, add(mul(slope, x), intercept))]
                      for x in range(q))
            for intercept in range(q)))
    parallel_classes.append(tuple(
        frozenset(point_id[(x, y)] for y in range(q))
        for x in range(q)))
    lines = [L for par in parallel_classes for L in par]
    assert len(lines) == q * (q + 1)
    assert len(set(lines)) == len(lines)
    assert all(len(L) == q for L in lines)
    assert all(sum(u in L and v in L for L in lines) == 1
               for u, v in combinations(range(q * q), 2))
    return lines, parallel_classes


def canon(labels):
    mapping = {}
    return tuple(mapping.setdefault(c, len(mapping)) for c in labels)


def candidate_partitions(q, parallel_classes):
    all_partitions = set()
    size = q * q
    all_partitions.add(tuple(range(size)))
    for par in parallel_classes:
        for k in range(1, q + 1):
            for chosen in combinations(par, k):
                blocks = list(chosen) + [frozenset((v,)) for v in range(size)
                                         if all(v not in L for L in chosen)]
                part = [None] * size
                for label, block in enumerate(blocks):
                    for v in block:
                        part[v] = label
                all_partitions.add(canon(part))
    return all_partitions


def rgs_partitions(n):
    p = [0] * n
    def rec(i, largest):
        if i == n:
            yield tuple(p)
            return
        for new in range(largest + 2):
            p[i] = new
            yield from rec(i + 1, max(new, largest))
    yield from rec(1, 0)


def lean(partition, lines):
    return len(set(partition)) >= 2 and all(
        len({partition[v] for v in L}) in (1, len(L)) for L in lines)


def check(q):
    lines, parallels = affine_plane(q)
    predicted = candidate_partitions(q, parallels)
    if q >= 3:
        assert len(predicted) == 1 + (q + 1) * (2 ** q - 1)
        assert all(lean(p, lines) for p in predicted)
        spectrum = Counter(len(set(p)) for p in predicted)
        assert spectrum == Counter({q*q: 1, **{
            q*q-k*(q-1): (q+1)*comb(q, k) for k in range(1, q+1)}})
        print('order', q, 'predicted partition count', len(predicted),
              'valid constructions and spectrum', sorted(spectrum.items()))
    else:
        print('order 2: separate all-nonconstant-colorings rule')
    if q <= 3:
        actual = set(p for p in rgs_partitions(q*q) if lean(p, lines))
        assert len(actual) == (14 if q == 2 else 29)
        if q == 3:
            assert actual == predicted
        else:
            assert len(actual - predicted) == 4
            assert len(predicted - actual) == 0
        print('order', q, 'exhaustive partition check', len(actual),
              'spectrum', sorted(Counter(len(set(p)) for p in actual).items()))


if __name__ == '__main__':
    for q in (2, 3, 4, 5, 7):
        check(q)
    print('PASS: exhaustive checks for orders 2/3; all predicted patterns for 4/5/7')
