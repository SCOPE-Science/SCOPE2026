"""Exact verification of local permutation-pattern/inverse-descent covariance.

Uses independent direct enumeration, with integer arithmetic throughout.
"""
from collections import Counter
from itertools import permutations
from math import comb, factorial


def sign_vector(pattern):
    k = len(pattern)
    pos = [None] * (k + 1)
    for i, value in enumerate(pattern):
        pos[value] = i
    return tuple(1 if pos[r] > pos[r + 1] else -1 for r in range(1, k))


def kernel(n, k, j, r):
    return comb(j - 1, r - 1) * comb(n - j - 1, k - r - 1)


def theorem_numerator(n, k, pattern, j):
    return sum(s * kernel(n, k, j, r) for r, s in enumerate(sign_vector(pattern), 1))


assertions = 0
profiles = 0
for n in range(2, 9):
    cases = list(permutations(range(1, n + 1)))
    total = factorial(n)
    assert total == len(cases)
    assertions += 1
    for k in range(2, min(n, 5) + 1):
        pats = list(permutations(range(1, k + 1)))
        signature_set = {sign_vector(p) for p in pats}
        assert len(signature_set) == 2 ** (k - 1)
        assertions += 1
        # The square subkernel using j=1,...,k-1 has a nonzero diagonal.
        for r in range(1, k):
            assert kernel(n, k, r, r) > 0
            assertions += 1
            for j in range(1, r):
                assert kernel(n, k, j, r) == 0
                assertions += 1
        for start in range(n - k + 1):
            freq = Counter()
            joint = Counter()
            for p in cases:
                w = p[start:start + k]
                ordered = sorted(w)
                dictionary = {x: r + 1 for r, x in enumerate(ordered)}
                pattern = tuple(dictionary[x] for x in w)
                freq[pattern] += 1
                inverse = [0] * (n + 1)
                for idx, value in enumerate(p):
                    inverse[value] = idx
                for j in range(1, n):
                    if inverse[j] > inverse[j + 1]:
                        joint[pattern, j] += 1
            for pattern in pats:
                assert freq[pattern] == total // factorial(k)
                assertions += 1
                for j in range(1, n):
                    lhs = (2 * joint[pattern, j] - freq[pattern]) * (factorial(n) // factorial(n - k))
                    rhs = total * theorem_numerator(n, k, pattern, j)
                    assert lhs == rhs, (n, k, start, pattern, j, lhs, rhs)
                    assertions += 1
                    profiles += 1

# Distinct profile signatures have distinct profiles in the full matrix.
for k in range(2, 8):
    n = k + 3
    paths = {}
    for pattern in permutations(range(1, k + 1)):
        profile = tuple(theorem_numerator(n, k, pattern, j) for j in range(1, n))
        signature = sign_vector(pattern)
        if signature in paths:
            assert profile == paths[signature]
        else:
            assert profile not in paths.values()
            paths[signature] = profile
        assertions += 1
    assert len(paths) == 2 ** (k - 1)
    assertions += 1

# Peaks of length 3 have vanishing covariance with every inverse descent.
for n in range(3, 70):
    for j in range(1, n):
        assert theorem_numerator(n, 3, (1, 3, 2), j) + theorem_numerator(n, 3, (2, 3, 1), j) == 0
        assertions += 1

print(f'PASS: {assertions} exact assertions; {profiles} direct covariance comparisons; n=2..8, k<=5; all windows and inverse-descent positions.')
