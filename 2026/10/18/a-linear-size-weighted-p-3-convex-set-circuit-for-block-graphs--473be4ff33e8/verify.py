#!/usr/bin/env python3
"""Exact polynomial verification for P3-convex vertex sets of clique-block trees.
Only Python's standard library is required.
"""
from itertools import combinations, product
from random import Random


def add(p, q):
    r = [0] * max(len(p), len(q))
    for i, c in enumerate(p): r[i] += c
    for i, c in enumerate(q): r[i] += c
    return trim(r)


def mul(p, q):
    if not p or not q: return []
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q): r[i + j] += a * b
    return trim(r)


def trim(p):
    while p and p[-1] == 0: p.pop()
    return p


ONE = [1]
ZERO = []


def convex_polynomial_from_blocks(n, blocks):
    """DP for a connected block graph, given its maximal cliques as vertex tuples.
    No vertex occurs in multiple blocks except at shared cut vertices.
    """
    incident = [[] for _ in range(n)]
    for i, block in enumerate(blocks):
        for v in block: incident[v].append(i)

    def vertex(v, parent_block):
        selected = [0, 1]  # z
        unselected0, unselected1 = [1], []
        for bi in incident[v]:
            if bi == parent_block: continue
            yes, zero, one = block_message(bi, v)
            selected = mul(selected, yes)
            next1 = add(mul(unselected1, zero), mul(unselected0, one))
            unselected0 = mul(unselected0, zero)
            unselected1 = next1
        return selected, unselected0, unselected1

    def block_message(bi, parent_v):
        prod_unselected0 = [1]
        prod_selected = [1]
        zero = [1]
        one = []
        for u in blocks[bi]:
            if u == parent_v: continue
            a, b0, b1 = vertex(u, bi)
            one = add(mul(one, b0), mul(prod_unselected0, a))
            prod_unselected0 = mul(prod_unselected0, b0)
            prod_selected = mul(prod_selected, a)
            zero = mul(zero, add(b0, b1))
        return add(prod_unselected0, prod_selected), zero, one

    a, b0, b1 = vertex(0, -1)
    return add(add(a, b0), b1)


def edges_of_blocks(n, blocks):
    edges = set()
    for block in blocks:
        for x, y in combinations(block, 2): edges.add((min(x, y), max(x, y)))
    return sorted(edges)


def direct_polynomial(n, blocks):
    neighbours = [0] * n
    for u, v in edges_of_blocks(n, blocks):
        neighbours[u] |= 1 << v
        neighbours[v] |= 1 << u
    histogram = [0] * (n + 1)
    for mask in range(1 << n):
        good = True
        for v in range(n):
            if not (mask >> v & 1) and (neighbours[v] & mask).bit_count() > 1:
                good = False
                break
        if good: histogram[mask.bit_count()] += 1
    return trim(histogram)


def glued_cliques(rng, n):
    """Randomly glue new cliques to an existing vertex; returns a block graph."""
    if n == 1: return []
    blocks = []
    nxt = 1
    while nxt < n:
        u = rng.randrange(nxt)
        size = min(n - nxt, rng.randrange(1, 5))
        blocks.append(tuple([u] + list(range(nxt, nxt + size))))
        nxt += size
    return blocks


def run():
    cases = 0
    max_n = 0
    # Every rooted clique-chain with one articulation per consecutive pair,
    # all block sizes 2..5, total order at most 12.
    for count in range(1, 7):
        for increments in product((1, 2, 3), repeat=count):
            n = 1 + sum(increments)
            if n > 12: continue
            blocks = []
            next_v, attach = 1, 0
            for step in increments:
                blocks.append(tuple([attach] + list(range(next_v, next_v + step))))
                attach = next_v
                next_v += step
            got = convex_polynomial_from_blocks(n, blocks)
            expected = direct_polynomial(n, blocks)
            assert got == expected, (n, blocks, got, expected)
            cases += 1
            max_n = max(max_n, n)
    rng = Random(20260305)
    for n in range(1, 13):
        for _ in range(100):
            blocks = glued_cliques(rng, n)
            got = convex_polynomial_from_blocks(n, blocks)
            expected = direct_polynomial(n, blocks)
            assert got == expected, (n, blocks, got, expected)
            cases += 1
    for n in range(1, 12):
        blocks = [] if n == 1 else [tuple(range(n))]
        got = convex_polynomial_from_blocks(n, blocks)
        expected = direct_polynomial(n, blocks)
        assert got == expected, (n, blocks, got, expected)
        cases += 1
    print('PASS:', cases, 'connected clique-block-tree cases; maximum n =', max_n)
    for name, n, blocks in [
        ('triangle', 3, [(0, 1, 2)]),
        ('two triangles sharing a vertex', 5, [(0, 1, 2), (0, 3, 4)]),
        ('three triangles in a path', 7, [(0, 1, 2), (2, 3, 4), (4, 5, 6)]),
        ('clique with three pendant edges', 7, [(0, 1, 2, 3), (0, 4), (1, 5), (2, 6)])
    ]:
        print(name, convex_polynomial_from_blocks(n, blocks))


if __name__ == '__main__':
    run()
