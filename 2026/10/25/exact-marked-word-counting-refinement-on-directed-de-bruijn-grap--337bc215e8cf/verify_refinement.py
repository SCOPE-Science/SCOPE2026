#!/usr/bin/env python3
"""Exact finite checks for pointed directed de Bruijn color refinement.

Uses the edge set of the actual shift digraph and compares stable classes
against independently formed coordinate-alphabet classes and stabilizer orbits.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb


def stirling(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return k * stirling(n - 1, k) + stirling(n - 1, k - 1)


def verify(q, depth, root):
    words = tuple(product(range(q), repeat=depth))
    idx = {word: p for p, word in enumerate(words)}
    out = [tuple(idx[w[1:] + (a,)] for a in range(q)) for w in words]
    inc = [[] for _ in words]
    for i in range(len(words)):
        for j in out[i]:
            inc[j].append(i)
    colors = [int(w == root) for w in words]
    for iteration in range(len(words) + 1):
        features = [
            (colors[i],
             tuple(sorted(Counter(colors[j] for j in out[i]).items())),
             tuple(sorted(Counter(colors[j] for j in inc[i]).items())))
            for i in range(len(words))
        ]
        palette = {a: j for j, a in enumerate(sorted(set(features)))}
        new = [palette[a] for a in features]
        if len(set(new)) == len(set(colors)):
            colors = new
            break
        colors = new
    else:
        raise AssertionError('Nonterminating refinement')
    named = set(root)
    coarse = [tuple(a if a in named else q for a in w) for w in words]
    cclasses = defaultdict(set)
    for col, pattern in zip(colors, coarse):
        cclasses[col].add(pattern)
    assert all(len(pats) == 1 for pats in cclasses.values())
    assert len(cclasses) == len(set(coarse))
    t = len(named)
    u = q - t
    expected = (t + (u > 0)) ** depth
    assert len(cclasses) == expected

    def orbit_pattern(w):
        blocks = {}
        result = []
        for a in w:
            if a in named:
                result.append(('named', a))
            else:
                if a not in blocks:
                    blocks[a] = len(blocks)
                result.append(('other', blocks[a]))
        return tuple(result)

    orbits = set(map(orbit_pattern, words))
    theoretical_orbits = sum(
        comb(depth, h) * t ** (depth - h) *
        sum(stirling(h, b) for b in range(min(h, u) + 1))
        for h in range(depth + 1)
    )
    assert len(orbits) == theoretical_orbits
    assert len(cclasses) == len(orbits) if (u <= 1 or depth <= 1) else len(cclasses) < len(orbits)
    return len(words), iteration, len(cclasses), len(orbits)


def main():
    checked = 0
    visited = 0
    examples = []
    for q in range(1, 6):
        for depth in range(1, 6):
            if q ** depth > 256:
                continue
            for root in product(range(q), repeat=depth):
                n, steps, c, o = verify(q, depth, root)
                checked += 1
                visited += n
                if q == 3 and depth == 2 and root in ((0, 0), (0, 1)):
                    examples.append((q, depth, root, c, o))
            print(f'q={q}, length={depth}, roots={q ** depth}, vertices={q ** depth}: PASS')
    print(f'TOTAL checked_roots={checked}, checked_vertices={visited}')
    print('BASIC EXAMPLES', examples)
    print('VERIFY_REFINEMENT_OK')


if __name__ == '__main__':
    main()
