"""Exact verification of paired-population Hamilton apportionment formulas.

Run with Python 3 using only the standard library.
"""
from itertools import combinations
from math import gcd


def allocations(a, b, h):
    population = (a, a, b, b)
    total = 2 * (a + b)
    base = [h * p // total for p in population]
    rest = [h * p % total for p in population]
    slots = h - sum(base)
    result = []
    for selected in combinations(range(4), slots):
        if all(rest[i] >= rest[j]
               for i in selected for j in range(4) if j not in selected):
            result.append(tuple(base[i] + int(i in selected) for i in range(4)))
    return result


def compulsory_loss(a, b, h):
    first = allocations(a, b, h)
    second = allocations(a, b, h + 1)
    return all(any(x[i] > y[i] for i in range(4))
               for x in first for y in second)


def predicted_loss(a, b, h):
    assert 0 < a < b
    modulus = 2 * (a + b)
    residue = (h * a) % modulus
    if h % 2 == 0:
        return 2 * (a + b) < 2 * residue < a + 3 * b
    return a + b < 2 * residue < 2 * b


def count_even(lower, upper):
    return max(0, upper // 2 - (lower - 1) // 2)


def count_odd(lower, upper):
    return max(0, (upper + 1) // 2 - lower // 2)


def period_count(a, b):
    assert 0 < a < b and gcd(a, b) == 1
    low_even, high_even = a + b + 1, (a + 3 * b - 1) // 2
    low_odd, high_odd = (a + b) // 2 + 1, b - 1
    second = (count_odd(low_odd, high_odd)
              if a % 2 else count_even(low_odd, high_odd))
    return count_even(low_even, high_even) + second


def main():
    comparisons = 0
    for a in range(1, 41):
        for b in range(a + 1, 41):
            if gcd(a, b) > 1:
                continue
            total = 2 * (a + b)
            for h in range(1, total + 1):
                assert compulsory_loss(a, b, h) == predicted_loss(a, b, h), (a, b, h)
                comparisons += 1
    counts = 0
    for a in range(1, 80):
        for b in range(a + 1, 80):
            if gcd(a, b) > 1:
                continue
            expected = period_count(a, b)
            actual = sum(predicted_loss(a, b, h)
                         for h in range(1, 2 * (a + b) + 1))
            assert expected == actual, (a, b, expected, actual)
            counts += 1
    smallest = [(a, b) for s in range(2, 6)
                for a in range(1, s)
                for b in (s - a,)
                if a < b and gcd(a, b) == 1 and period_count(a, b) > 0]
    assert smallest == [(1, 4)], smallest
    assert not any(predicted_loss(a, b, h)
                   for a in range(1, 30) for b in range(a + 1, 31)
                   for h in (1, 2))
    assert allocations(1, 4, 3) == [(1, 0, 1, 1), (0, 1, 1, 1)]
    assert allocations(1, 4, 4) == [(0, 0, 2, 2)]
    print(f'VERIFIED comparisons={comparisons} count_pairs={counts} minimum=(1,4) first_house=3')


if __name__ == '__main__':
    main()
