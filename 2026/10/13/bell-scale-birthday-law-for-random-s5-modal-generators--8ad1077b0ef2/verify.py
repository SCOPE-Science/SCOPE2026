#!/usr/bin/env python3
"""Reproduce finite S5 modal-generation counts and illustrative random tests.

This program uses only the Python standard library. It separates exhaustive
small-model enumeration from asymptotic Monte Carlo illustrations.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, exp, lgamma, log
import bisect
import random


def partitions(n):
    """All set partitions of {0,...,n-1}, once each."""
    if n == 0:
        yield ()
        return
    blocks = [[0]]
    def rec(j):
        if j == n:
            yield tuple(tuple(b) for b in blocks)
            return
        for b in blocks:
            b.append(j)
            yield from rec(j + 1)
            b.pop()
        blocks.append([j])
        yield from rec(j + 1)
        blocks.pop()
    yield from rec(1)


def bell(n):
    b = [1]
    for j in range(n):
        b.append(sum(comb(j, k) * b[k] for k in range(j + 1)))
    return b


def count_by_coefficient(n, q):
    # [z^n] product_s (1+z^s)^{binom(q,s)}, then multiply by n!.
    p = [1] + [0] * n
    for s in range(1, min(n, q) + 1):
        m = comb(q, s)
        factor = [comb(m, j) for j in range(min(m, n // s) + 1)]
        new = [0] * (n + 1)
        for k in range(n + 1):
            for j, v in enumerate(factor):
                if k + s * j <= n:
                    new[k + s * j] += p[k] * v
        p = new
    fact = 1
    for k in range(2, n + 1):
        fact *= k
    return fact * p[n]


def predicted_success(blocks, colors):
    palettes = defaultdict(list)
    for b in blocks:
        seq = tuple(colors[v] for v in b)
        if len(set(seq)) != len(seq):
            return False
        palettes[len(b)].append(frozenset(seq))
    return all(len(set(sets)) == len(sets) for sets in palettes.values())


def refined_success(blocks, colors):
    # Independent modal partition refinement, including diamond-of-color classes.
    n = len(colors)
    cid = list(colors)
    world_block = [None] * n
    for b in blocks:
        for v in b:
            world_block[v] = b
    for _ in range(n + 1):
        profiles = [
            (cid[v], tuple(sorted({cid[w] for w in world_block[v]})))
            for v in range(n)
        ]
        ren = {}
        nxt = [ren.setdefault(p, len(ren)) for p in profiles]
        if nxt == cid:
            return len(set(nxt)) == n
        cid = nxt
    raise AssertionError('Modal refinement failed to stabilize')


def direct_term_closure(blocks, colors, r):
    n = len(colors)
    top = (1 << n) - 1
    known = {0, top}
    for bit in range(r):
        known.add(sum(1 << v for v in range(n) if colors[v] & (1 << bit)))
    def dia(mask):
        return sum(sum(1 << u for u in b) for b in blocks
                   if any(mask & (1 << u) for u in b))
    for _ in range(2 ** n + 1):
        old = len(known)
        a = tuple(known)
        for x in a:
            known.add(top ^ x)
            known.add(dia(x))
        for x in a:
            for y in a:
                known.add(x & y)
                known.add(x | y)
        if len(known) == old:
            return len(known) == 2 ** n
    raise AssertionError('Term closure failed')


def exhaustive_small():
    b = bell(8)
    checked = 0
    direct = 0
    parameter_cases = 0
    for n in range(1, 7):
        cases = list(partitions(n))
        assert len(cases) == b[n]
        for q in (2, 3, 4):
            observed = 0
            for blocks in cases:
                for coloring in product(range(q), repeat=n):
                    a = predicted_success(blocks, coloring)
                    z = refined_success(blocks, coloring)
                    assert a == z, (n, q, blocks, coloring)
                    observed += a
                    checked += 1
            formula = count_by_coefficient(n, q)
            assert observed == formula, (n, q, observed, formula)
            parameter_cases += 1
    rng = random.Random(4175)
    for n in range(1, 7):
        parts = list(partitions(n))
        for r in (1, 2):
            for _ in range(15):
                blocks = rng.choice(parts)
                colors = tuple(rng.randrange(1 << r) for _ in range(n))
                assert direct_term_closure(blocks, colors, r) == predicted_success(blocks, colors)
                direct += 1
    # Exact Bell partition identities: ordered distinct edges always impose two merges.
    for n in range(3, 9):
        parts = list(partitions(n))
        H = [sum(comb(len(b), 2) for b in blocks) for blocks in parts]
        N = comb(n, 2)
        assert sum(H) == N * b[n-1]
        assert sum(h * (h - 1) for h in H) == N * (N - 1) * b[n-2]
    return checked, parameter_cases, direct


def w(n):
    v = log(n) - log(log(n)) if n > 4 else 1.0
    for _ in range(20):
        v -= (v + log(v) - log(n)) / (1 + 1/v)
    return v


def sample_partition_and_colors(n, q, rng, k_values, cdf):
    # Stam's exact distribution on K is proportional to K^n/K!, truncated
    # at 2*n; the omitted upper tail is astronomically small for n>=200.
    z = rng.random()
    k = k_values[bisect.bisect_left(cdf, z)]
    boxes = defaultdict(list)
    for _ in range(n):
        boxes[rng.randrange(k)].append(rng.randrange(q))
    within_pairs = sum(sum(v * (v - 1) // 2 for v in Counter(vals).values())
                       for vals in boxes.values())
    palettes = [(frozenset(vals), len(vals)) for vals in boxes.values()]
    full = within_pairs == 0 and len({frozenset(vals) for vals in boxes.values()}) == len(boxes)
    return within_pairs, full


def monte_carlo():
    rng = random.Random(20261009)
    out = []
    for n, q in ((400, 2048), (1000, 8192), (3000, 16384)):
        vals = [n * log(k) - lgamma(k + 1) for k in range(1, 2*n + 1)]
        mx = max(vals)
        weights = [exp(x - mx) for x in vals]
        total = sum(weights)
        cumulative = []
        s = 0.0
        for v in weights:
            s += v / total
            cumulative.append(s)
        cumulative[-1] = 1.0
        reps = 600
        pairs = 0
        successes = 0
        for _ in range(reps):
            t, success = sample_partition_and_colors(n, q, rng,
                          range(1, 2*n + 1), cumulative)
            pairs += t
            successes += success
        predicted = exp(-n * w(n) / (2 * q))
        out.append((n, q, reps, round(successes/reps, 4),
                    round(predicted, 4), round(pairs/reps, 4),
                    round(n*w(n)/(2*q), 4)))
    return out


if __name__ == '__main__':
    exhaustive, cases, direct = exhaustive_small()
    print('EXHAUSTIVE_OK', 'valuation_frame_pairs', exhaustive,
          'enumeration_cases', cases, 'direct_term_closures', direct)
    for row in monte_carlo():
        print('MONTE_CARLO n=%d q=%d samples=%d p_obs=%.4f p_theory=%.4f '
              'pairs_obs=%.4f pairs_theory=%.4f' % row)
    print('VERIFY_OK')
