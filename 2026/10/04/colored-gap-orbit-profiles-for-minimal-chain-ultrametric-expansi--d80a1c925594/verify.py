#!/usr/bin/env python3
"""Finite replay for the chain-ultrametric orbit formulas."""
from functools import lru_cache
from itertools import permutations, product
from math import factorial


def unordered_partitions(items):
    """All set partitions, canonically encoded by restricted-growth strings."""
    items = tuple(items)
    n = len(items)
    if n == 0:
        yield ()
        return
    rgs = [0] * n

    def rec(i, max_seen):
        if i == n:
            blocks = [[] for _ in range(max_seen + 1)]
            for x, b in zip(items, rgs):
                blocks[b].append(x)
            yield tuple(tuple(block) for block in blocks)
            return
        for b in range(max_seen + 2):
            rgs[i] = b
            yield from rec(i + 1, max(max_seen, b))

    yield from rec(1, 0)


def ordered_partitions(items):
    for part in unordered_partitions(items):
        yield from permutations(part)


@lru_cache(None)
def hierarchies(items, depth):
    """Depth-d ordered nested partitions with singleton leaves."""
    items = tuple(items)
    if depth == 0:
        return frozenset([items[0]]) if len(items) == 1 else frozenset()
    out = set()
    for part in ordered_partitions(items):
        choices = [hierarchies(tuple(block), depth - 1) for block in part]
        if not all(choices):
            continue
        for children in product(*choices):
            out.add(tuple(children))
    return frozenset(out)


def encode(tree, depth):
    """Encode a hierarchy as (leaf permutation, adjacent gap levels)."""
    if depth == 0:
        return (tree,), ()
    orders = []
    gaps = []
    children = list(tree)
    for j, child in enumerate(children):
        order, child_gaps = encode(child, depth - 1)
        if j:
            gaps.append(depth)
        orders.extend(order)
        gaps.extend(child_gaps)
    return tuple(orders), tuple(gaps)


def decode(order, gaps, depth):
    """Inverse of encode: split at gaps carrying the current top level."""
    order = tuple(order)
    gaps = tuple(gaps)
    if depth == 0:
        assert len(order) == 1 and len(gaps) == 0
        return order[0]
    assert len(gaps) == len(order) - 1
    cuts = [i for i, c in enumerate(gaps) if c == depth]
    pieces = []
    start = 0
    for cut in cuts + [len(order) - 1]:
        stop = cut + 1
        suborder = order[start:stop]
        subgaps = gaps[start:stop - 1]
        pieces.append(decode(suborder, subgaps, depth - 1))
        start = stop
    return tuple(pieces)


def stirling2(n, k):
    table = [[0] * (k + 1) for _ in range(n + 1)]
    table[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            table[i][j] = table[i - 1][j - 1] + j * table[i - 1][j]
    return table[n][k]


def injective_formula(d, n):
    return factorial(n) * d ** (n - 1)


def all_tuple_formula(d, n):
    return sum(stirling2(n, k) * injective_formula(d, k) for k in range(1, n + 1))


def fubini_polynomial(n, x):
    return sum(factorial(k) * stirling2(n, k) * x ** k for k in range(1, n + 1))


def main():
    # Independent recursive enumeration of the finite structures.
    for d in range(1, 4):
        for n in range(1, 6):
            hs = hierarchies(tuple(range(n)), d)
            expected = injective_formula(d, n)
            assert len(hs) == expected, (d, n, len(hs), expected)

            codes = set()
            for h in hs:
                code = encode(h, d)
                order, gaps = code
                assert sorted(order) == list(range(n))
                assert len(gaps) == n - 1
                assert all(1 <= c <= d for c in gaps)
                assert decode(order, gaps, d) == h
                codes.add(code)
            assert len(codes) == expected
            # The target code space itself has n! d^(n-1) elements.
            all_codes = {
                (perm, word)
                for perm in permutations(range(n))
                for word in product(range(1, d + 1), repeat=n - 1)
            }
            assert codes == all_codes

    # Stirling transform and ordered-Bell/Fubini-polynomial identity.
    for d in range(1, 6):
        for n in range(1, 9):
            b = all_tuple_formula(d, n)
            assert d * b == fubini_polynomial(n, d)

    samples_injective = {
        d: [injective_formula(d, n) for n in range(1, 7)] for d in (1, 2, 3)
    }
    samples_all = {
        d: [all_tuple_formula(d, n) for n in range(1, 7)] for d in (1, 2, 3)
    }
    print("injective", samples_injective)
    print("all_tuples", samples_all)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
