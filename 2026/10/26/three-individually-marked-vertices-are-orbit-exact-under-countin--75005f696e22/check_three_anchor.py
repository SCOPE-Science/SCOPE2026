#!/usr/bin/env python3
"""Finite independent checks of the three-anchor Hamming refinement theorem.
Requires only the Python standard library. Vertex sets and all transformations are labelled.
"""
from collections import Counter, defaultdict
from itertools import combinations, product
from math import comb, factorial
from random import Random


def compact_labels(keys):
    lookup = {key: i for i, key in enumerate(sorted(set(keys)))}
    return [lookup[key] for key in keys]


def orbit_key(v, marks, q):
    types = []
    for i in range(len(v)):
        alphabet_blocks = {}
        for j, m in enumerate(marks):
            alphabet_blocks.setdefault(m[i], []).append(j)
        blocks = tuple(sorted(tuple(z) for z in alphabet_blocks.values()))
        block_id = next((k for k, block in enumerate(blocks)
                         if v[i] == marks[block[0]][i]), len(blocks))
        types.append((blocks, block_id))
    return tuple(sorted(Counter(types).items()))


def stable_colors(q, d, marks):
    vertices = list(product(range(q), repeat=d))
    ix = {v: i for i, v in enumerate(vertices)}
    adjacency = [[ix[v[:i] + (z,) + v[i + 1:]]
                  for i in range(d) for z in range(q) if z != v[i]]
                 for v in vertices]
    marked_ids = {ix[v]: j + 1 for j, v in enumerate(marks)}
    current = compact_labels([marked_ids.get(i, 0) for i in range(len(vertices))])
    histories = [len(set(current))]
    for round_no in range(1, d + 2):
        signatures = [(current[i], tuple(sorted(Counter(current[j]
                          for j in adjacency[i]).items())))
                      for i in range(len(vertices))]
        nxt = compact_labels(signatures)
        histories.append(len(set(nxt)))
        if len(set(nxt)) == len(set(current)):
            return vertices, nxt, round_no - 1, histories
        current = nxt
    raise AssertionError('refinement exceeded bound')


def direct_formula(marks, q):
    d = len(marks[0]); pi_counts = Counter()
    for i in range(d):
        groups = {}
        for j, m in enumerate(marks):
            groups.setdefault(m[i], []).append(j)
        key = tuple(sorted(tuple(group) for group in groups.values()))
        pi_counts[key] += 1
    expected = 1
    for p, n in pi_counts.items():
        assert len(p) < q
        expected *= comb(n + len(p), len(p))
    return expected, pi_counts


def reconstructed_type(v, marks, pi_counts, q):
    """Reconstruct orbit profile from distances and one-step displacement counts.
    Independent of the orbit_key routine and WL implementation.
    """
    d = len(v); dist = tuple(sum(v[i] != m[i] for i in range(d)) for m in marks)
    shifts = Counter()
    for i in range(d):
        old = v[i]
        for z in range(q):
            if z == old: continue
            y = v[:i] + (z,) + v[i+1:]
            D = tuple(sum(y[k] != m[k] for k in range(d)) for m in marks)
            shifts[tuple(b-a for a,b in zip(dist,D))] += 1
    by_type = Counter()
    all_labs = (0,1,2)
    discrete = ((0,), (1,), (2,))
    patterns = [tuple(sorted((singleton, complement))) for singleton,complement in
                [((0,),(1,2)),((1,),(0,2)),((2,),(0,1))]] + [discrete]
    for pi in patterns:
        if pi not in pi_counts: continue
        for block in pi:
            other = next(b for b in pi if b != block)
            step = tuple(int(i in block)-int(i in other) for i in all_labs)
            by_type[(pi,pi.index(block))] = shifts[step]
        by_type[(pi,len(pi))] = pi_counts[pi] - sum(by_type[(pi,s)] for s in range(len(pi)))
    mono = ((0,1,2),)
    if mono in pi_counts:
        other_count = dist[0] - sum(n for (pi,s),n in by_type.items()
                          if 0 not in (pi[s] if s < len(pi) else ()))
        by_type[(mono,1)] = other_count
        by_type[(mono,0)] = pi_counts[mono] - other_count
    assert all(n>=0 for n in by_type.values())
    return tuple(sorted((z,n) for z,n in by_type.items() if n>0))


def test(q, d, marks):
    vs, colors, rounds, history = stable_colors(q,d,marks)
    orbit = [orbit_key(v,marks,q) for v in vs]
    c2orbits = defaultdict(set); orbit2c = defaultdict(set)
    for c,o in zip(colors, orbit):
        c2orbits[c].add(o); orbit2c[o].add(c)
    assert all(len(s)==1 for s in c2orbits.values())
    assert all(len(s)==1 for s in orbit2c.values())
    formula, pi_counts = direct_formula(marks,q)
    assert len(orbit2c) == formula == len(c2orbits)
    # Check every individual orbit size against the multinomial formula.
    population = Counter(orbit)
    for key, actual_size in population.items():
        counts = dict(key)
        predicted = 1
        for pi, n_pi in pi_counts.items():
            denominator = 1
            for s in range(len(pi) + 1):
                denominator *= factorial(counts.get((pi, s), 0))
            unmatched = counts.get((pi, len(pi)), 0)
            predicted *= factorial(n_pi) // denominator * (q - len(pi)) ** unmatched
        assert actual_size == predicted
    if (q,d) in {(4,3),(5,3),(4,4)}:
        for v in vs:
            A=reconstructed_type(v, marks, pi_counts, q); B=orbit_key(v,marks,q)
            if A != B:
                print("MISMATCH",q,d,marks,v,pi_counts,A,B); raise AssertionError
    assert rounds <= d
    return rounds, len(orbit2c)


def main():
    rng = Random(20261018)
    cases = 0; witnesses = []
    for q,d in [(4,2),(5,2)]:
        space = list(product(range(q), repeat=d))
        for triple in combinations(space,3):
            result = test(q,d,triple)
            cases += 1
        print(f'EXHAUSTIVE q={q} d={d} triples={comb(q**d,3)} PASS',flush=True)
    for q,d,trials in [(4,3,160),(5,3,80),(6,3,30),(4,4,80),(5,4,25),(4,5,5)]:
        space = list(product(range(q), repeat=d))
        for _ in range(trials):
            triple = tuple(rng.sample(space,3))
            result = test(q,d,triple)
            if result[0] == d and len(witnesses) < 10:
                witnesses.append((q,d,triple,result))
            cases += 1
        print(f'SAMPLED q={q} d={d} triples={trials} PASS',flush=True)
    print(f'CASE_COUNT={cases}')
    print('DEPTH_D_WITNESSES',witnesses)
    print('ALL_TESTS_PASS')

if __name__=='__main__': main()
