#!/usr/bin/env python3
"""Exact finite certification of binary three-dimensional sampling optima.

Run using Python 3 standard library: python3 verify.py
"""
from fractions import Fraction
from itertools import combinations
from math import comb, lcm
from random import Random

NAMES = range(1, 8)
LINES = tuple(sorted({tuple(sorted((a, b, a ^ b))) for a in NAMES for b in NAMES if a < b}))
assert LINES == ((1,2,3),(1,4,5),(1,6,7),(2,4,6),(2,5,7),(3,4,7),(3,5,6))

EXPECTED = {
 8:(Fraction(422,105),7), 9:(Fraction(142,35),21),
 10:(Fraction(509,126),28), 11:(Fraction(1439,360),7),
 12:(Fraction(615,154),21), 13:(Fraction(7309,1848),7)
}

def compositions(total, places):
    if places == 1:
        yield (total,)
    else:
        for head in range(total + 1):
            for tail in compositions(total - head, places - 1):
                yield (head,) + tail

def rank_mask(mask):
    basis = []
    for b in NAMES:
        if (mask >> (b - 1)) & 1:
            v = b
            for w in basis:
                v = min(v, v ^ w)
            if v:
                basis.append(v)
                basis.sort(reverse=True)
    return len(basis)

def span_mask(a, b):
    # a denotes a subspace represented by its nonzero members
    todo = {0}
    for v in NAMES:
        if (a >> (v - 1)) & 1:
            todo.add(v)
    if b: todo.add(b)
    while True:
        nxt = todo | {u ^ v for u in todo for v in todo}
        if len(nxt) == len(todo): break
        todo = nxt
    return sum(1 << (v - 1) for v in todo if v)

FULL = (1 << 7) - 1
assert span_mask(FULL, 0) == FULL

def expectation_by_markov(counts):
    n = sum(counts)
    # Independently solve first-step recursion on all reachable subspaces.
    states = {0}
    for r in range(3):
        states |= {span_mask(S, v) for S in tuple(states) for v in NAMES}
    states.add(FULL)
    E = {FULL:Fraction(0)}
    for S in sorted(states - {FULL}, key=lambda s: (-rank_mask(s), s)):
        weight = sum(counts[v - 1] for v in NAMES if (S >> (v - 1)) & 1)
        if weight == n: return None
        future = sum((counts[v-1] * E[span_mask(S, v)] for v in NAMES
                      if not (S >> (v - 1)) & 1), Fraction(0))
        E[S] = Fraction(n, n-weight) + future/(n-weight)
    return E[0]

def integer_objective(counts, n, denominator):
    # Exclude rank-deficient collections (contained within a Fano line).
    line_term = 0
    for triple in LINES:
        outside = n - sum(counts[v-1] for v in triple)
        if outside <= 0:
            return None
        line_term += denominator // outside
    point_term = sum(denominator // (n-c) for c in counts)
    return line_term - 2 * point_term

def expected_patterns(n):
    r=n-7
    for chosen in combinations(NAMES, r):
        if r == 3 and any(set(chosen) == set(line) for line in LINES):
            continue
        if r == 4 and any(set(NAMES) - set(chosen) == set(line) for line in LINES) is False:
            continue
        yield tuple(2 if v in chosen else 1 for v in NAMES)

TOTAL_CHECKED = 0
for n, (target, target_count) in EXPECTED.items():
    denominator = lcm(*range(1, n+1))
    best = None
    attaining = set()
    valid = 0
    for counts in compositions(n, 7):
        obj = integer_objective(counts, n, denominator)
        if obj is None: continue
        valid += 1
        if best is None or obj < best:
            best = obj
            attaining = {counts}
        elif obj == best:
            attaining.add(counts)
    TOTAL_CHECKED += valid
    result = Fraction(8*denominator+n*best, denominator)
    patterns = set(expected_patterns(n))
    assert result == target, (n, result, target)
    assert attaining == patterns, (n, attaining ^ patterns)
    assert len(attaining) == target_count
    for a in attaining:
        assert expectation_by_markov(a) == target, (n,a)
    print('n=%d valid_profiles=%d exact_optimum=%s optimizing_profiles=%d structural_classification=PASS' %
        (n, valid, result, len(attaining)))

# Compare independently derived Markov recurrences with the lattice formula
# on 240 reproducibly selected unrestricted multiplicity vectors.
rng=Random(20261025)
for n in range(8,14):
    denominator = lcm(*range(1,n+1))
    valid_examples=0
    while valid_examples < 40:
        counts = [0]*7
        for j in range(n): counts[rng.randrange(7)] += 1
        obj = integer_objective(counts,n,denominator)
        if obj is None: continue
        lattice_value=Fraction(8*denominator+n*obj,denominator)
        markov_value=expectation_by_markov(counts)
        assert lattice_value == markov_value, (n, counts, lattice_value, markov_value)
        valid_examples += 1
print('RANK3_COVERAGE_EXACT_CERTIFICATE_OK', TOTAL_CHECKED, 'exhaustive valid profiles and 240 independent Markov cross-checks')
