#!/usr/bin/env python3
"""Exact six-voter neutral monotone voting-rule cross-check.

No external packages or network; run `python3 verify.py`.
This is an exhaustive finite verification, not a substitute for the proof.
"""
from collections import Counter
from itertools import combinations, permutations
from math import factorial

N = 6
FULL = (1 << N) - 1
ALL = tuple(range(1 << N))
LAYERS = tuple(tuple(s for s in ALL if s.bit_count() == k) for k in range(N + 1))
EDGES = LAYERS[2]
TRIPLE_COMPLEMENTS = tuple((s, FULL ^ s) for s in LAYERS[3] if s < (FULL ^ s))
assert len(TRIPLE_COMPLEMENTS) == 10


def rule_for_edges_and_orientation(edges, chosen):
    """Construct a neutral rule given winning pairs and chosen middle triples."""
    wins = set(LAYERS[5] + LAYERS[6])
    wins.update(edges)
    for pair in LAYERS[2]:
        if pair not in edges:
            wins.add(FULL ^ pair)
    wins.update(chosen)
    return frozenset(wins)


def monotone(wins):
    return all(s | (1 << i) in wins for s in wins for i in range(N))


def neutral(wins):
    return all((s in wins) != ((FULL ^ s) in wins) for s in ALL)


def powers(wins):
    sh = [0] * N
    bz = [0] * N
    for i in range(N):
        bit = 1 << i
        for s in ALL:
            if s & bit:
                continue
            if s not in wins and s | bit in wins:
                bz[i] += 1
                sh[i] += factorial(s.bit_count()) * factorial(N - 1 - s.bit_count())
    return tuple(sh), tuple(bz)


def three_counts(wins):
    return tuple(sum(1 for s in LAYERS[3] if s in wins and s & (1 << i)) for i in range(N))


def canonical_cycle_graph(wins):
    # Chosen triples containing distinguished voter 0 give a graph on voters 1,..,5.
    return frozenset(s & ~1 for s in LAYERS[3] if s in wins and s & 1)


def orbit_under_permutations(wins):
    out = set()
    for perm in permutations(range(N)):
        out.add(frozenset(sum(1 << perm[i] for i in range(N) if s & (1 << i)) for s in wins))
    return out


def main():
    fair_shapley = set()
    fair_banzhaf = set()
    examined_rules = 0
    edge_patterns = 0
    for pattern in range(1 << len(EDGES)):
        edges = frozenset(e for j, e in enumerate(EDGES) if pattern & (1 << j))
        # Winning pairs must intersect by neutrality and monotonicity.
        if any((e & f) == 0 for e, f in combinations(edges, 2)):
            continue
        edge_patterns += 1
        fixed = {}
        impossible = False
        for j, (a, b) in enumerate(TRIPLE_COMPLEMENTS):
            fa = any(a & e == e for e in edges)
            fb = any(b & e == e for e in edges)
            if fa and fb:
                impossible = True
                break
            if fa or fb:
                fixed[j] = a if fa else b
        if impossible:
            continue
        free = [j for j in range(10) if j not in fixed]
        for word in range(1 << len(free)):
            orient = dict(fixed)
            for k, j in enumerate(free):
                a, b = TRIPLE_COMPLEMENTS[j]
                orient[j] = a if (word >> k) & 1 else b
            wins = rule_for_edges_and_orientation(edges, orient.values())
            if not monotone(wins):
                continue
            assert neutral(wins)
            examined_rules += 1
            sh, bz = powers(wins)
            if len(set(sh)) == 1:
                fair_shapley.add(wins)
            if len(set(bz)) == 1:
                fair_banzhaf.add(wins)

    assert len(fair_shapley) == len(fair_banzhaf) == 12
    assert fair_shapley == fair_banzhaf
    assert all(sum(s in w for s in LAYERS[2]) == 0 for w in fair_shapley)
    assert all(three_counts(w) == (5,) * N for w in fair_shapley)

    cycle_graphs = {canonical_cycle_graph(w) for w in fair_shapley}
    assert len(cycle_graphs) == 12
    for graph in cycle_graphs:
        assert len(graph) == 5
        for i in range(1, 6):
            assert sum(bool(e & (1 << i)) for e in graph) == 2
    test = next(iter(fair_shapley))
    assert orbit_under_permutations(test) == fair_shapley
    stabilizer = factorial(N) // len(fair_shapley)
    assert stabilizer == 60
    for rule in fair_shapley:
        assert len({s for s in rule if s.bit_count() == 3}) == 10
        assert all(powers(rule)[0][i] == 120 for i in range(N))
        assert all(powers(rule)[1][i] == 10 for i in range(N))
    print('PASS: exhaustive neutral, monotone six-voter cases with no winning singleton')
    print('PASS: intersecting pair-patterns =', edge_patterns)
    print('PASS: admissible rules checked =', examined_rules)
    print('PASS: exactly 12 Shapley-Shubik-fair and exactly 12 Banzhaf-fair, identical sets')
    print('PASS: each fair rule has 10 winning triples and a distinguished 5-cycle')
    print('PASS: all 12 form one labeled orbit; automorphism group order =', stabilizer)


if __name__ == '__main__':
    main()
