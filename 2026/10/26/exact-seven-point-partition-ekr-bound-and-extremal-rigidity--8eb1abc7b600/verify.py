#!/usr/bin/env python3
"""Exhaustive proof certificate for pair-intersecting four-block partitions of [7].

A partition p is represented by a restricted-growth word p[0],...,p[6].
Its atom mask has bit i exactly when the ith unordered vertex pair occurs
within one of the blocks. This script enumerates all 350 words and proves
all maximum clique claims with a complete, colour-bounded search.
"""
from itertools import combinations
from collections import Counter

N, BLOCKS, TARGET = 7, 4, 65
PAIRS = list(combinations(range(N), 2))


def partitions():
    word = [0] * N
    def rec(pos, largest):
        if pos == N:
            if largest + 1 == BLOCKS:
                yield tuple(word)
            return
        for value in range(min(largest + 2, BLOCKS)):
            word[pos] = value
            yield from rec(pos + 1, max(largest, value))
    yield from rec(1, 0)


P = list(partitions())
assert len(P) == 350 == len(set(P))
assert Counter(tuple(sorted(Counter(p).values(), reverse=True)) for p in P) == {
    (4, 1, 1, 1): 35, (3, 2, 1, 1): 210, (2, 2, 2, 1): 105
}
MASK = [sum(1 << j for j, (a, b) in enumerate(PAIRS) if p[a] == p[b]) for p in P]
V = len(P)
ADJ = [sum(1 << j for j in range(V) if i != j and (MASK[i] & MASK[j]))
       for i in range(V)]
ALL = (1 << V) - 1


def colour_order(candidates):
    """Proper greedy colouring, ordered by increasing positive colour."""
    vertices, colours = [], []
    colour = 0
    while candidates:
        colour += 1
        available = candidates
        while available:
            bit = available & -available
            v = bit.bit_length() - 1
            candidates ^= bit
            available ^= bit
            vertices.append(v)
            colours.append(colour)
            available &= ~ADJ[v]  # one colour class is independent
    return vertices, colours


def search_at_least(threshold):
    nodes = 0
    def rec(candidates, depth):
        nonlocal nodes
        nodes += 1
        if depth == threshold:
            return True
        vertices, colours = colour_order(candidates)
        for i in range(len(vertices) - 1, -1, -1):
            # A clique uses at most one vertex per remaining colour class.
            if depth + colours[i] < threshold:
                return False
            vertex = vertices[i]
            bit = 1 << vertex
            if candidates & bit:
                if rec(candidates & ADJ[vertex], depth + 1):
                    return True
                candidates ^= bit
        return False
    exists = rec(ALL, 0)
    return exists, nodes


def enumerate_size(target):
    nodes = 0
    found = []
    def rec(candidates, chosen):
        nonlocal nodes
        nodes += 1
        if len(chosen) == target:
            found.append(frozenset(chosen))
            return
        vertices, colours = colour_order(candidates)
        for i in range(len(vertices) - 1, -1, -1):
            if len(chosen) + colours[i] < target:
                return
            vertex = vertices[i]
            bit = 1 << vertex
            if candidates & bit:
                rec(candidates & ADJ[vertex], chosen + (vertex,))
                candidates ^= bit
    rec(ALL, ())
    return found, nodes


STARS = {frozenset(i for i, mask in enumerate(MASK) if mask & (1 << edge))
         for edge in range(len(PAIRS))}
assert len(STARS) == 21 and all(len(star) == TARGET for star in STARS)
# Verify compatibility without relying on the clique search.
for star in STARS:
    for a in star:
        assert all(a == b or (ADJ[a] >> b) & 1 for b in star)

exists_66, nodes_66 = search_at_least(66)
assert not exists_66, 'A clique of size at least 66 exists'
solutions_65, nodes_65 = enumerate_size(65)
assert len(solutions_65) == len(set(solutions_65)) == 21
assert set(solutions_65) == STARS

print('partitions=350 types=35,210,105')
print('star_size=65 labelled_stars=21')
print('clique_ge_66=False search_nodes='+str(nodes_66))
print('cliques_size_65=21 search_nodes='+str(nodes_65))
print('all_maximum_families_are_stars=True')
print('VERIFY_OK')
