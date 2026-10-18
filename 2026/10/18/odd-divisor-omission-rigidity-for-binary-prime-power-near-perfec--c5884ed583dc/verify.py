#!/usr/bin/env python3
"""Finite cross-check of an odd-divisor omission classification; not an infinite proof."""

def primes_upto(m):
    return [p for p in range(3, m + 1, 2)
            if all(p % d for d in range(3, int(p**0.5) + 1, 2))]

def check():
    trials = matches = supported = 0
    for k in range(1, 11):
        multiplier = (1 << (k + 1)) - 1
        for p in primes_upto(97):
            for e in range(2, 9):
                n = (1 << k) * p**e
                sigma = multiplier * sum(p**j for j in range(e + 1))
                excess = sigma - 2*n
                divisors = [p**j for j in range(e + 1)]
                matching_subsets = []
                for mask in range(1 << (e + 1)):
                    subset = tuple(divisors[j] for j in range(e + 1) if mask >> j & 1)
                    trials += 1
                    if sum(subset) == excess:
                        matching_subsets.append(subset)
                expected = [tuple(p**j for j in range(1, e))] if p == multiplier else []
                assert matching_subsets == expected, (k, p, e, matching_subsets, expected)
                supported += 1
                matches += len(matching_subsets)
    print(f'checked {supported} triples; {trials} subsets; {matches} matching cases')

if __name__ == '__main__':
    check()
