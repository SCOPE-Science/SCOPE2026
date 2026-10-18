#!/usr/bin/env python3
"""Finite exact-integer cross-checks for the four-mode cubic Fourier moment theorem.

Only Python standard library is required. This is supplementary evidence,
not a substitute for the universal rank-and-multiplicity proof.
"""
from collections import defaultdict, Counter
from itertools import combinations, combinations_with_replacement
from math import factorial

WEIGHTS = {256: 0, 262: 6, 268: 12, 274: 18, 340: 84, 400: 144}
PATTERN_TO_ENERGY = {
    ((2, 1), (2, 1)): 274,
    ((2, 1), (3,)): 262,
    ((1, 1, 1), (3,)): 268,
    ((1, 1), (2,)): 340,
    ((1, 1), (1, 1)): 400,
}
EXAMPLES = {
    256: (0, 1, 2, 3),
    262: (-5, 1, 4, 6),
    268: (-18, 3, 10, 17),
    274: (1, 4, 9, 11),
    340: (-1, 0, 1, 2),
    400: (-2, -1, 1, 2),
}

def ordered_multiplicity(triple):
    counts = Counter(triple)
    value = factorial(3)
    for z in counts.values():
        value //= factorial(z)
    return value

def energy_and_defect(S):
    fibers = defaultdict(list)
    for T in combinations_with_replacement(S, 3):
        fibers[(sum(T), sum(t*t*t for t in T))].append(T)
    value = 0
    patterns = []
    for ts in fibers.values():
        value += sum(ordered_multiplicity(t) for t in ts)**2
        if len(ts) > 1:
            assert len(ts) == 2, (S, ts)
            u, v = ts
            plus = Counter(u)-Counter(v)
            minus = Counter(v)-Counter(u)
            key = tuple(sorted((tuple(sorted(plus.values(), reverse=True)),
                                tuple(sorted(minus.values(), reverse=True)))))
            patterns.append(key)
    return value, patterns

def main():
    for value, S in EXAMPLES.items():
        actual, patterns = energy_and_defect(S)
        assert actual == value, (S, actual, value, patterns)
        assert (not patterns) if value == 256 else (len(patterns) > 0)
    census = Counter()
    inspected = 0
    for S in combinations(range(-15, 16), 4):
        actual, patterns = energy_and_defect(S)
        assert actual in WEIGHTS, (S, actual)
        if actual == 256:
            assert len(patterns) == 0
        else:
            assert patterns
            target = actual
            for k in patterns:
                assert k in PATTERN_TO_ENERGY, (S, actual, k)
                assert PATTERN_TO_ENERGY[k] == target, (S, actual, k)
        if all(t > 0 for t in S):
            assert actual in (256, 274), (S, actual)
        census[actual] += 1
        inspected += 1
    assert set(census) | set(EXAMPLES) == set(WEIGHTS), census
    print('VERIFY_OK six attainable levels; 31 choose 4 = %d exact supports; counts=%s' %
          (inspected, ', '.join('%d:%d' % p for p in sorted(census.items()))))

if __name__ == '__main__':
    main()
