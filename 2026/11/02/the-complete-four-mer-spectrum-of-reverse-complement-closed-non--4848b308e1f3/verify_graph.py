#!/usr/bin/env python3
"""Exact integer enumeration of length-four Watson--Crick DNA codebooks.

No external libraries are needed. Optional input: adjacency.tsv, checked against
an independently reconstructed compatibility graph.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
import sys

ALPH = tuple(range(4))           # A C G T
LETTERS = 'ACGT'
EXPECTED = (1, 12, 88, 288, 584, 760, 688, 424, 160, 32)


def rc(w):
    return tuple(3 - w[3 - i] for i in range(4))


def internally_good(o):
    for x in o:
        for y in o:
            if any(x[:k] == y[4-k:] for k in (1, 2, 3)):
                return False
            if x != y and sum(a != b for a,b in zip(x, y)) < 2:
                return False
    return True


def compatible(o,p):
    for x in o:
        for y in p:
            if any(x[:k] == y[4-k:] or y[:k] == x[4-k:] for k in (1,2,3)):
                return False
            if sum(a != b for a,b in zip(x,y)) < 2:
                return False
    return True


def words(o):
    return ','.join(''.join(LETTERS[k] for k in w) for w in o)


def calculate():
    orbits = sorted({tuple(sorted({w, rc(w)})) for w in product(ALPH, repeat=4)})
    good = tuple(o for o in orbits if internally_good(o))
    assert len(orbits) == 136 and len(good) == 56
    assert sum(len(o) == 1 for o in good) == 12
    n = len(good)
    neighbours = []
    for i,o in enumerate(good):
        mask=0
        for j,p in enumerate(good):
            if i != j and compatible(o,p):
                mask |= 1 << j
        neighbours.append(mask)
    assert sum(m.bit_count() for m in neighbours) == 840
    for i in range(n):
        for j in range(n):
            assert bool(neighbours[i] & (1 << j)) == bool(neighbours[j] & (1 << i))
    rows = ['index\torbit\tneighbours_hex']
    rows += [f'{i}\t{words(good[i])}\t{neighbours[i]:014x}' for i in range(n)]
    graph_text = '\n'.join(rows) + '\n'
    if len(sys.argv) > 1:
        assert Path(sys.argv[1]).read_text(encoding='utf-8') == graph_text

    @lru_cache(maxsize=None)
    def polynomial(mask):
        if mask == 0:
            return (1,)
        # The vertex choice affects speed, not the recurrence or result.
        vertices = [i for i in range(n) if mask & (1 << i)]
        v = max(vertices, key=lambda i: (mask & neighbours[i]).bit_count())
        exclude = polynomial(mask ^ (1 << v))
        include = polynomial(mask & neighbours[v])
        size = len(good[v])
        ans = [0] * max(len(exclude), len(include)+size)
        for j, count in enumerate(exclude):
            ans[j] += count
        for j, count in enumerate(include):
            ans[j+size] += count
        return tuple(ans)

    distribution = polynomial((1 << n)-1)
    assert distribution == EXPECTED
    assert sum(distribution) == 3037
    print('GRAPH_VERIFY_OK', distribution, 'vertices', n, 'edges', 420,
          'recursion_states', polynomial.cache_info().currsize)
    return graph_text

if __name__ == '__main__':
    calculate()
