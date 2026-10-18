"""Exhaustive restricted-growth enumeration for strict ternary synchronization gaps.

Run with Python 3.9+: python verify.py. Only standard-library dependencies.
"""
from functools import lru_cache
from fractions import Fraction
from itertools import permutations

WITNESS = '012010212021012102010212012'
COUNTS = [1, 1, 2, 3, 5, 7, 10, 13, 14, 18, 17, 17, 16, 15, 12,
          11, 10, 9, 9, 10, 11, 10, 9, 9, 10, 11, 1, 0]

@lru_cache(maxsize=None)
def lcs(a, b):
    row = [0] * (len(b) + 1)
    for x in a:
        diagonal = 0
        for j, y in enumerate(b, 1):
            previous = row[j]
            row[j] = max(previous, row[j - 1], diagonal + (x == y))
            diagonal = previous
    return row[-1]

def allowed_extension(word):
    """Check exactly those bad intervals whose right endpoint is the new end."""
    n = len(word)
    for middle in range(1, n):
        for left in range(middle):
            total = n - left
            if 16 * lcs(word[left:middle], word[middle:]) >= 7 * total:
                return False
    return True

def optimal_gap(word):
    best = Fraction(1, 1)
    minimizers = []
    for right in range(2, len(word) + 1):
        for middle in range(1, right):
            for left in range(middle):
                total = right - left
                score = Fraction(total - 2 * lcs(word[left:middle], word[middle:right]), total)
                if score < best:
                    best, minimizers = score, [(left, middle, right)]
                elif score == best:
                    minimizers.append((left, middle, right))
    return best, minimizers

def main():
    level = ['0']
    observed = [1]
    at_27 = None
    for n in range(2, 29):
        next_level = []
        for word in level:
            # Canonical alphabet relabeling by order of first appearance.
            for x in range(min(2, max(int(c) for c in word) + 1) + 1):
                candidate = word + str(x)
                if allowed_extension(candidate):
                    next_level.append(candidate)
        observed.append(len(next_level))
        level = next_level
        if n == 27:
            at_27 = level.copy()
    assert observed == COUNTS, (observed, COUNTS)
    assert at_27 == [WITNESS], at_27
    assert level == [], level
    gap, minimizers = optimal_gap(WITNESS)
    assert gap == Fraction(3, 23), gap
    assert set(minimizers) == {(0, 12, 23), (4, 15, 27)}, minimizers
    for rename in permutations('012'):
        renamed = ''.join(rename[int(ch)] for ch in WITNESS)
        assert optimal_gap(renamed)[0] == gap
        for letter in '012':
            assert not allowed_extension(renamed + letter)
    print('canonical_survivor_counts_n1_to_n28:', observed)
    print('unique_canonical_n27:', WITNESS)
    print('minimum_gap:', str(gap), 'minimizers:', minimizers)
    print('n28_canonical_survivors: 0; six labeled n27 survivors')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
