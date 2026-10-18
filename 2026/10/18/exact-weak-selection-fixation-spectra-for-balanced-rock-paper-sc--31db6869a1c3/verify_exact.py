#!/usr/bin/env python3
"""Check a full finite-chain rational certificate without nonstandard dependencies.
Run: python3 verify_exact.py from any working directory.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from json import load
from pathlib import Path

BASE = Path(__file__).resolve().parent
STATES = list(product(range(3), repeat=6))
PAYOFF = ((0, 1, -1), (-1, 0, 1), (1, -1, 0))
EDGES = {
    'prism': ((0, 1), (1, 2), (2, 0), (3, 4), (4, 5), (5, 3), (0, 3), (1, 4), (2, 5)),
    'K33': tuple((u, v) for u in range(3) for v in range(3, 6)),
}
EXPECTED = {
    'prism': {Fraction(-22, 281): 6, Fraction(-65, 1686): 6,
              Fraction(-37, 1686): 12, Fraction(0): 42,
              Fraction(37, 1686): 12, Fraction(65, 1686): 6,
              Fraction(22, 281): 6},
    'K33': {Fraction(-1, 66): 18, Fraction(0): 54, Fraction(1, 66): 18},
}

def check():
    with (BASE / 'CERTIFICATES.json').open(encoding='utf-8') as fh:
        cert = load(fh)
    assert tuple(map(tuple, cert['payoff'])) == PAYOFF
    lookup = {v: i for i, v in enumerate(STATES)}
    balanced = [v for v in STATES if v.count(0) == v.count(1) == v.count(2) == 2]
    assert len(balanced) == 90
    for name, edges in EDGES.items():
        adjacent = [set() for _ in range(6)]
        for u, v in edges:
            adjacent[u].add(v)
            adjacent[v].add(u)
        assert all(len(s) == 3 for s in adjacent)
        dv = [Fraction(x) for x in cert[name]]
        assert len(dv) == len(STATES) == 729
        for state in STATES:
            i = lookup[state]
            if len(set(state)) == 1:
                assert dv[i] == 0, (name, state, 'boundary')
                continue
            score = [sum(PAYOFF[state[u]][state[j]] for j in adjacent[u])
                     for u in range(6)]
            drift = Fraction(0)
            avg = Fraction(0)
            for u in range(6):
                for v in adjacent[u]:
                    changed = list(state)
                    changed[v] = state[u]
                    avg += dv[lookup[tuple(changed)]] / 18
                    drift += Fraction(score[u] * ((state[u] == 0) - (state[v] == 0)), 108)
            assert dv[i] == avg + drift, (name, state, dv[i], avg + drift)
        distribution = dict(Counter(dv[lookup[state]] for state in balanced))
        assert distribution == EXPECTED[name], (name, distribution)
        print(name, '729 exact state residuals zero, 90 balanced cases',
              ', '.join(f'{v} ({n})' for v, n in sorted(distribution.items())))
    # Explicit antisymmetry under exchanging types 1 and 2.
    for name in EDGES:
        dv = [Fraction(x) for x in cert[name]]
        for st in STATES:
            switched = tuple(0 if x == 0 else 3 - x for x in st)
            assert dv[lookup[switched]] == -dv[lookup[st]], (name, st)
    print('Type-1/type-2 antisymmetry: 1458 exact identities verified.')

if __name__ == '__main__':
    check()
