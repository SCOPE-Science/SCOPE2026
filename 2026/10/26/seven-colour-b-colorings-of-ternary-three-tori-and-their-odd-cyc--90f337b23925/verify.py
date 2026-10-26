#!/usr/bin/env python3
"""Standalone finite verification of a seven-colour rainbow-square edge colouring.

Uses only Python standard library.  The proof that periodic pullbacks work at all
odd multiples of three is supplied in RESULT.md, not inferred from finite tests.
"""
import itertools
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TABLE = json.loads((HERE / 'certificate.json').read_text(encoding='utf-8'))['colors']
assert len(TABLE) == 3
assert all(len(slices) == 3 for slices in TABLE)
assert all(len(mat) == 3 and all(len(row) == 3 for row in mat)
           for slices in TABLE for mat in slices)
assert {v for slabs in TABLE for grid in slabs for row in grid for v in row} == set(range(7))


def edge(x, y):
    return (x, y) if x < y else (y, x)


def graph_and_colors(lengths):
    assert len(lengths) == 3 and all(n >= 3 and n % 3 == 0 for n in lengths)
    verts = list(itertools.product(*(range(n) for n in lengths)))
    graph = {v: set() for v in verts}
    col = {}
    for x in verts:
        for axis in range(3):
            y = list(x)
            y[axis] = (y[axis] + 1) % lengths[axis]
            y = tuple(y)
            e = edge(x, y)
            assert e not in col, ('edge repeated', lengths, e)
            z, u, v = (t % 3 for t in (x[2], x[0], x[1]))
            col[e] = TABLE[axis][z][u][v]
            graph[x].add(y)
            graph[y].add(x)
    assert len(col) == 3 * len(verts)
    return graph, col


def all_simple_four_cycles(graph):
    """Find all unlabelled 4-cycles using graph adjacency, no product assumptions."""
    found = set()
    for s, ns in graph.items():
        for a in ns:
            for b in ns:
                if a == b:
                    continue
                for t in (graph[a] & graph[b]) - {s, a, b}:
                    if len({s, a, t, b}) != 4:
                        continue
                    cyc = tuple(sorted((edge(s,a), edge(a,t), edge(t,b), edge(b,s))))
                    found.add(cyc)
    return found


def check(lengths):
    graph, colors = graph_and_colors(lengths)
    for v, neighbors in graph.items():
        assert len(neighbors) == 6, (lengths, v, len(neighbors))
        incident = [colors[edge(v,w)] for w in neighbors]
        assert len(set(incident)) == 6, (lengths, v, incident)
    squares = all_simple_four_cycles(graph)
    assert len(squares) == 3*len(graph), (lengths,len(squares),3*len(graph))
    for sq in squares:
        c = [colors[e] for e in sq]
        assert len(set(c)) == 4, (lengths, sq, c)
    assert set(colors.values()) == set(range(7))
    return dict(lengths=list(lengths), vertices=len(graph), edges=len(colors),
                four_cycles=len(squares), proper_vertices=len(graph),
                rainbow_four_cycles=len(squares), colors=7,
                color_counts=sorted(Counter(colors.values()).items()))


def main():
    cases = [(3,3,3),(9,3,3),(9,9,3),(15,9,3),(9,9,9),(15,9,9)]
    results = [check(ns) for ns in cases]
    report = {'certificate': '3 x 3 x 3 directed-axis edge-color table',
              'result': 'PASS', 'instances': results,
              'limit': 'The unrestricted statement follows from the separate covering argument, not from these finite checks.'}
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
