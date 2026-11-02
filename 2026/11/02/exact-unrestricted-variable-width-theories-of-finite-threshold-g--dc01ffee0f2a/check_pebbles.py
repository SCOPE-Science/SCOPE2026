#!/usr/bin/env python3
"""Noncounting k-variable logical refinement, independently from the proof.

Uses all ordered k-tuples and greatest-back-and-forth color refinement.
Run: python3 check_pebbles.py. Standard library only.
"""
from itertools import product


def graph(word):
    n = 1 + len(word)
    adj = [[False for _ in range(n)] for _ in range(n)]
    for v, universal in enumerate(word, start=1):
        for u in range(v):
            adj[u][v] = adj[v][u] = bool(universal)
    return adj


def expected(adj, k):
    n = len(adj)
    # Distinct degree classes of a threshold graph are exactly twin blocks.
    bydegree = {}
    for x in range(n):
        bydegree.setdefault(sum(adj[x]), []).append(x)
    blocks = [bydegree[d] for d in sorted(bydegree)]
    witness_types = []
    for b in blocks:
        typ = None if len(b) == 1 else int(adj[b[0]][b[1]])
        witness_types.append((min(k, len(b)), typ))
        assert all(all(adj[u][v] == (typ == 1) for u in b for v in b if u != v)
                   for _ in (0,))
    edges = tuple(int(adj[blocks[i][0]][blocks[j][0]])
                  for i in range(len(blocks)) for j in range(i + 1, len(blocks)))
    return tuple(witness_types), edges


def theories(graphs, k):
    tuples = [list(product(range(len(g)), repeat=k)) for g in graphs]
    starts = []
    vals = []
    total = 0
    for a, tup in zip(graphs, tuples):
        starts.append(total)
        total += len(tup)
        for t in tup:
            vals.append(tuple((t[i] == t[j], a[t[i]][t[j]])
                              for i in range(k) for j in range(i + 1, k)))
    pool = {signature: index for index, signature in enumerate(sorted(set(vals)))}
    colors = [pool[v] for v in vals]
    reps = []
    for a, tuples_a, start in zip(graphs, tuples, starts):
        n = len(a)
        shifts = [n ** (k - 1 - i) for i in range(k)]
        for t in tuples_a:
            index = sum(v * shifts[i] for i, v in enumerate(t))
            assert tuples_a[index] == t
            reps.append(tuple(tuple(start + index + (replacement - t[i]) * shifts[i]
                                    for replacement in range(n))
                              for i in range(k)))
    for depth in range(100):
        old_count = len(pool)
        signatures = [
            (colors[j],) + tuple(tuple(sorted({colors[replacement]
                                                       for replacement in positions}))
                                  for positions in reps[j])
            for j in range(total)
        ]
        pool = {signature: index for index, signature in enumerate(sorted(set(signatures)))}
        colors = [pool[sig] for sig in signatures]
        if len(pool) == old_count:
            break
    else:
        raise AssertionError('refinement did not reach fixed point')
    return [frozenset(colors[start:start + len(tup)]) for start, tup in zip(starts, tuples)], depth + 1, len(pool)


def evaluate(k, maxvertices):
    words = [word for n in range(1, maxvertices + 1)
             for word in product((False, True), repeat=n - 1)]
    gs = [graph(w) for w in words]
    predicted = [expected(g, k) for g in gs]
    observed, depth, types = theories(gs, k)
    comparisons = 0
    for i in range(len(gs)):
        for j in range(i + 1, len(gs)):
            comparisons += 1
            a = predicted[i] == predicted[j]
            b = observed[i] == observed[j]
            assert a == b, ('disagreement', k, words[i], words[j], a, b)
    print('width', k, 'n<=', maxvertices, 'graphs', len(gs),
          'pairs', comparisons, 'rounds', depth, 'tuple colors', types,
          'theories', len(set(observed)), ': PASS')


if __name__ == '__main__':
    evaluate(3, 7)
    evaluate(4, 5)
