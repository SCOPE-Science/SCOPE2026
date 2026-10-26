#!/usr/bin/env python3
"""Finite, reproducible checks for orbit-exact 1-WL on marked ternary Hamming graphs."""
from collections import Counter, defaultdict
from itertools import combinations, product
import random


def canon(items):
    palette = {a: i for i, a in enumerate(sorted(set(items)))}
    return tuple(palette[a] for a in items)


def graph(d):
    V = tuple(product(range(3), repeat=d))
    index = {v: i for i, v in enumerate(V)}
    N = tuple(tuple(index[v[:j] + (b,) + v[j+1:]]
                    for j in range(d) for b in range(3) if b != v[j]) for v in V)
    return V, N


def refinement(V, N, marks):
    singleton = {v: i + 1 for i, v in enumerate(marks)}
    colors = tuple(singleton.get(v, 0) for v in V)
    for rnd in range(len(V) + 1):
        signatures = tuple((colors[u], tuple(sorted(Counter(colors[v] for v in N[u]).items())))
                           for u in range(len(V)))
        nxt = canon(signatures)
        if len(set(nxt)) == len(set(colors)):
            return colors, rnd
        colors = nxt
    raise AssertionError('refinement did not stabilize')


def profile(v, marks):
    counts = defaultdict(Counter)
    for j, x in enumerate(v):
        blocks = tuple(sorted(tuple(i for i, a in enumerate(marks) if a[j] == symbol)
                              for symbol in {a[j] for a in marks}))
        current = tuple(i for i, a in enumerate(marks) if a[j] == x)
        counts[blocks][current] += 1
    return tuple(sorted((blocks, tuple(sorted(c.items()))) for blocks, c in counts.items()))


def verify_one(V, N, marks, d):
    colors, rounds = refinement(V, N, marks)
    profiles = tuple(profile(v, marks) for v in V)
    cp, pc = {}, {}
    for c, p in zip(colors, profiles):
        if c in cp: assert cp[c] == p
        else: cp[c] = p
        if p in pc: assert pc[p] == c
        else: pc[p] = c
    assert rounds <= d + 1
    # Independently check the exact one-step distance-displacement polynomial.
    for v, adj in zip(V, N):
        Ds = tuple(sum(x != y for x,y in zip(v, a)) for a in marks)
        transitions = Counter(tuple(sum(x != y for x,y in zip(V[w], a)) - z
                                    for a,z in zip(marks, Ds)) for w in adj)
        pp = dict(profiles[V.index(v)])
        all_expected = Counter()
        for blocks, counts_tuple in pp.items():
            c = dict(counts_tuple)
            expected = Counter()
            for status, multiplicity in c.items():
                for B in blocks:
                    if B == status:
                        continue
                    increment = tuple((1 if i in status else 0) - (1 if i in B else 0)
                                      for i in range(len(marks)))
                    expected[increment] += multiplicity
                other = 3 - len(blocks) - (status == ())
                increment = tuple(1 if i in status else 0 for i in range(len(marks)))
                expected[increment] += multiplicity * other
            # Each pattern's transitions contribute additively across coordinates.
            if 'all_expected' not in locals():
                all_expected = Counter()
            all_expected.update(expected)
            if len(blocks) == 1:
                B = blocks[0]
                assert transitions[tuple(+1 for _ in marks)] >= 2*c.get(B,0)
                assert transitions[tuple(-1 for _ in marks)] >= c.get((),0)
            elif len(blocks) == 2:
                for B in blocks:
                    assert transitions[tuple(1 if i in B else 0 for i in range(len(marks)))] >= c.get(B,0)
                    assert transitions[tuple(-1 if i in B else 0 for i in range(len(marks)))] >= c.get((),0)
            else:
                for B in blocks:
                    for C in blocks:
                        if B!=C:
                            assert transitions[tuple(1 if i in B else -1 if i in C else 0
                                                     for i in range(len(marks)))] >= c.get(B,0)
        assert transitions == +all_expected, (d, marks, v, transitions, all_expected)
    return rounds, len(cp)


def main():
    overall = 0
    for d in range(1, 5):
        V, N = graph(d)
        for r in range(1, min(len(V), 4) + 1):
            family = list(combinations(V[1:], r-1))
            random.Random(31+d*7+r).shuffle(family)
            if d <= 2:
                selection = family
            elif d == 3:
                selection = family[:min(len(family), 300)]
            else:
                selection = family[:min(len(family), 90)]
            max_round = 0
            max_classes = 0
            for tail in selection:
                rr, nc = verify_one(V, N, (V[0],) + tail, d)
                max_round = max(max_round, rr)
                max_classes = max(max_classes, nc)
            overall += len(selection)
            print('d=%d markers=%d configurations=%d max_round=%d max_classes=%d'
                  % (d, r, len(selection), max_round, max_classes))
    print('PASS configurations=%d' % overall)

if __name__ == '__main__': main()
