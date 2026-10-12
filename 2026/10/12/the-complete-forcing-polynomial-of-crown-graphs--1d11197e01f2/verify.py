#!/usr/bin/env python3
"""Exact, standard-library check of the crown complete-forcing enumerator.

The exhaustive test derives forbidden edge sets only from pairs of
perfect matchings, without using the nice-cycle or star/triangle proof.
"""
from itertools import permutations
from math import comb


def addmul(dst, poly, scale=1, offset=0):
    for i, coeff in enumerate(poly):
        dst[i + offset] += scale * coeff


def multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i + j] += x * y
    return result


def power(a, k):
    result = [1]
    for _ in range(k):
        result = multiply(result, a)
    return result


def formula(n):
    assert n >= 3
    E = n * (n - 1)
    out = [0] * (E + 1)
    if n == 3:
        addmul(out, power([1, 1], 6))
        addmul(out, power([1, 1], 3), -2, 3)
        out[6] += 1
        return out
    h = [0, 2, 1]
    out[0] = 1
    addmul(out, h, comb(n, 2))
    for k in range(2, n):
        addmul(out, power(h, k), n * comb(n - 1, k))
    triangle = power(h, 3)
    if n >= 5:
        addmul(triangle, power([1, 1], 3), -2, 3)
        triangle[6] += 1
    addmul(out, triangle, comb(n, 3))
    return out


def exhaustive(n):
    """Test all complements against *ordered* distinct perfect matchings."""
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    bit = {e: k for k, e in enumerate(arcs)}
    perfect_matchings = []
    for p in permutations(range(n)):
        if all(p[i] != i for i in range(n)):
            perfect_matchings.append(sum(1 << bit[i, p[i]] for i in range(n)))
    forbidden = set()
    for M in perfect_matchings:
        for N in perfect_matchings:
            if M != N:
                forbidden.add(M & ~N)
    minimal = [f for f in sorted(forbidden) if not any(
        other != f and (other & f) == other for other in forbidden
    )]
    # Minimized forbidden matchings and all 2^E candidate complements.
    counts = [0] * (len(arcs) + 1)
    for T in range(1 << len(arcs)):
        if all((T & f) != f for f in minimal):
            counts[T.bit_count()] += 1
    predicted = formula(n)
    assert counts == predicted, (n, counts, predicted)
    print('n=%d derangements=%d minimal_forbidden=%d total=%d complement_profile=%s' %
          (n, len(perfect_matchings), len(minimal), sum(counts), counts))


def structural(n):
    """Independently enumerate star/triangle supports and compare formula."""
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    E = len(arcs)
    masks = {0}
    for c in range(n):
        positions = [q for q, (i, j) in enumerate(arcs) if i == c or j == c]
        for t in range(1 << len(positions)):
            masks.add(sum(1 << positions[k] for k in range(len(positions)) if (t >> k) & 1))
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                positions = [q for q, (i, j) in enumerate(arcs)
                             if i in (a, b, c) and j in (a, b, c)]
                for t in range(1 << len(positions)):
                    T = sum(1 << positions[k] for k in range(len(positions)) if (t >> k) & 1)
                    tri1 = {(a, b), (b, c), (c, a)}
                    tri2 = {(b, a), (c, b), (a, c)}
                    selected = {arcs[positions[k]] for k in range(len(positions)) if (t >> k) & 1}
                    if n == 4 or not (tri1 <= selected or tri2 <= selected):
                        masks.add(T)
    counts = [0] * (E + 1)
    for T in masks:
        counts[T.bit_count()] += 1
    assert counts == formula(n)
    print('n=%d structural_total=%d max_complement=%d max_count=%d' %
          (n, len(masks), max(i for i, c in enumerate(counts) if c),
           counts[max(i for i, c in enumerate(counts) if c)]))


if __name__ == '__main__':
    for n in (3, 4, 5):
        exhaustive(n)
    for n in (4, 5, 6, 7):
        structural(n)
    print('VERIFY_OK')
