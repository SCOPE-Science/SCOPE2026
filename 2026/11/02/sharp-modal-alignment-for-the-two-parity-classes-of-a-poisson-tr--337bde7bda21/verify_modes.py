#!/usr/bin/env python3
"""Exact integer-coefficient checks for two parity-conditional modal bounds.

This is a finite regression/stress checker. It is NOT a proof of the
universal mathematical statements; those follow from interlacing.
"""
from collections import Counter
from itertools import combinations_with_replacement
from random import Random


def product(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def check(factors, require_positive=False):
    a = [1]
    for triple in factors:
        assert sum(triple) > 0 and min(triple) >= 0
        if require_positive:
            assert min(triple) > 0
        a = product(a, triple)
    e, o = a[::2], a[1::2]
    if not e or not o or not max(e) or not max(o):
        return None
    E = [i for i, v in enumerate(e) if v == max(e)]
    O = [i for i, v in enumerate(o) if v == max(o)]
    gaps = [abs(2 * i - (2 * j + 1)) for i in E for j in O]
    bound = 1 if require_positive else 3
    assert max(gaps) <= bound, (factors, e, o, E, O, gaps, bound)
    return max(gaps)


def main():
    checks = 0
    tallies = Counter()
    for den, n in [(2, 7), (3, 6), (4, 5), (5, 4)]:
        triples = [(a, b, den - a - b)
                   for a in range(den + 1)
                   for b in range(den - a + 1)]
        for indices in combinations_with_replacement(range(len(triples)), n):
            gap = check([triples[i] for i in indices])
            if gap is not None:
                checks += 1
                tallies['boundary_' + str(gap)] += 1
    for den, n in [(3, 8), (4, 7), (5, 6), (6, 5), (8, 4), (10, 4)]:
        triples = [(a, b, den - a - b)
                   for a in range(1, den)
                   for b in range(1, den - a)]
        for indices in combinations_with_replacement(range(len(triples)), n):
            gap = check([triples[i] for i in indices], require_positive=True)
            checks += 1
            tallies['strict_' + str(gap)] += 1
    r = Random(20261026)
    for n in (10, 20, 40, 80):
        for _ in range(700):
            factors = [[r.randint(1, 1000) for k in range(3)] for i in range(n)]
            # Integer arithmetic preserves even exponentially small coefficients.
            gap = check(factors, require_positive=True)
            checks += 1
            tallies['strict_random_' + str(gap)] += 1
    # Universal bound is sharp: four equally likely lattice outcomes.
    assert check([(1, 1, 0), (1, 0, 1)]) == 3
    checks += 1
    # Full-support bound is sharp already with one summand.
    assert check([(1, 1, 1)], require_positive=True) == 1
    checks += 1
    assert sum(v for k, v in tallies.items() if k.startswith('boundary_3')) > 0
    print('All checks passed.')
    print('Checked admissible exact or random cases:', checks)
    print('Gap is measured in half-unit lattice steps: 1 means 1/2; 3 means 3/2.')
    for k in sorted(tallies):
        print(f'{k}: {tallies[k]}')
    print('Sharpness examples: boundary gap=3; strictly positive gap=1.')


if __name__ == '__main__':
    main()
