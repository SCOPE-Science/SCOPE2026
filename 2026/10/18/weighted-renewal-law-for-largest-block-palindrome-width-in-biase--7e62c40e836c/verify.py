"""Exact finite tests for weighted block-palindrome width laws.

Only standard-library arithmetic is used. Finite tests corroborate, not replace,
proofs of asymptotic assertions.
"""
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import product


def unbordered(word):
    return all(word[:j] != word[-j:] for j in range(1, len(word)))


def product_weight(word, probabilities):
    result = Fraction(1)
    for letter in word:
        result *= probabilities[letter]
    return result


def largest_width(word):
    width = 0
    while word:
        for j in range(1, len(word) // 2 + 1):
            if word[:j] == word[-j:]:
                width += 2
                word = word[j:-j]
                break
        else:
            return width + 1
    return width


def exact_kernel(probabilities, max_length):
    letters = range(len(probabilities))
    return {length: sum((product_weight(u, probabilities) ** 2
                         for u in product(letters, repeat=length)
                         if unbordered(u)), Fraction(0))
            for length in range(1, max_length + 1)}


@lru_cache(None)
def weighted_unbordered(length, weights):
    total = sum(weights)
    if length == 0:
        return Fraction(1)
    if length == 1:
        return total
    if length & 1:
        return total * weighted_unbordered(length - 1, weights)
    squared = tuple(w * w for w in weights)
    return (total * weighted_unbordered(length - 1, weights)
            - weighted_unbordered(length // 2, squared))


def recursive_distributions(max_length, b):
    distributions = [{0: Fraction(1)}]
    for n in range(1, max_length + 1):
        row = defaultdict(Fraction)
        row[1] = 1 - sum((b[j] for j in range(1, n // 2 + 1)), Fraction(0))
        for j in range(1, n // 2 + 1):
            for width, probability in distributions[n - 2 * j].items():
                row[width + 2] += b[j] * probability
        assert sum(row.values()) == 1
        distributions.append(dict(row))
    return distributions


def enumeration(n, probabilities):
    row = defaultdict(Fraction)
    for word in product(range(len(probabilities)), repeat=n):
        row[largest_width(word)] += product_weight(word, probabilities)
    return dict(row)


def check(probabilities, max_length):
    b = exact_kernel(probabilities, max_length // 2)
    weights = tuple(x * x for x in probabilities)
    for length, v in b.items():
        assert v == weighted_unbordered(length, weights)
    for length in range(1, max_length + 1):
        b_law = recursive_distributions(max_length, b)[length]
        positive = {width: mass for width, mass in b_law.items() if mass}
        assert positive == enumeration(length, probabilities), (length, positive)
    print('EXACT_WEIGHTED_LAWS', probabilities, 'THROUGH', max_length, 'PASS')


check((Fraction(1, 4), Fraction(3, 4)), 12)
check((Fraction(1, 3), Fraction(2, 3)), 12)
check((Fraction(1, 2), Fraction(1, 2)), 12)
check((Fraction(1, 3),) * 3, 8)

# A separate weighted recurrence check uses weights that are not probabilities.
for weights, cutoff in [((Fraction(2, 7), Fraction(3, 7)), 9),
                        ((Fraction(2, 9), Fraction(3, 9), Fraction(4, 9)), 8)]:
    for n in range(1, cutoff + 1):
        direct = sum((product_weight(word, weights)
                      for word in product(range(len(weights)), repeat=n)
                      if unbordered(word)), Fraction(0))
        assert direct == weighted_unbordered(n, weights)
print('WEIGHTED_UNBORDERED_RECURRENCE PASS')

p = (Fraction(1, 4), Fraction(3, 4))
s = sum(x * x for x in p)
weights = tuple(x * x for x in p)
h100 = sum((weighted_unbordered(n, weights) for n in range(1, 101)), Fraction(0))
assert s == Fraction(5, 8)
assert 0 < h100 < 1
assert s**101 / (1-s) < Fraction(1, 10**19)
assert abs(float(h100) - 0.8028150445695221) < 1e-15
assert abs(float((1+h100)/(1-h100)) - 9.142761630235764) < 1e-13
print('BIAS_EXAMPLE_CERTIFIED_INTERVAL', float(h100),
      'TAIL_BOUND', float(s**101/(1-s)))
print('ALL_CHECKS_PASSED')
