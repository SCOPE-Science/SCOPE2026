"""Exact finite checks for noun-union cardinality-spectrum partition axioms.

Each point is assigned to exactly one noun block, equivalently satisfying
all specified pairwise-disjointness and covering inclusion sentences.
The remaining axioms require equal block counts within each generator group.
"""
from collections import Counter
from itertools import product
from math import factorial


def bounded_additive_spectrum(generators, cap):
    feasible = [False] * (cap + 1)
    feasible[0] = True
    for n in range(1, cap + 1):
        feasible[n] = any(n >= a and feasible[n-a] for a in generators)
    return feasible


def direct_count(generators, n):
    block_to_group = [i for i, a in enumerate(generators) for _ in range(a)]
    count = 0
    for allocation in product(range(len(block_to_group)), repeat=n):
        counts = [0] * len(block_to_group)
        for block in allocation:
            counts[block] += 1
        offset = 0
        valid = True
        for a in generators:
            if len(set(counts[offset:offset+a])) != 1:
                valid = False
                break
            offset += a
        count += valid
    return count


def closed_count(generators, n):
    total = 0
    f_n = factorial(n)
    def recur(i, remaining, denominator):
        nonlocal total
        if i == len(generators):
            if remaining == 0:
                total += f_n // denominator
            return
        a = generators[i]
        for t in range(remaining // a + 1):
            recur(i+1, remaining-a*t, denominator * factorial(t)**a)
    recur(0, n, 1)
    return total


def main():
    comparisons = 0
    allocations = 0
    for generators, cap in [((2,3), 7), ((3,4), 6), ((4,7), 5), ((1,), 5)]:
        possible = bounded_additive_spectrum(generators, cap)
        for n in range(1, cap+1):
            brute = direct_count(generators, n)
            exact = closed_count(generators, n)
            assert brute == exact, (generators, n, brute, exact)
            assert (brute > 0) == possible[n], (generators, n, brute)
            comparisons += 1
            allocations += sum(generators)**n
    # Both inclusion sentences P subset not-P and not-P subset P
    # are incompatible on each nonempty finite universe.
    for n in range(1, 8):
        assert not any((s == 0 and s == (1 << n)-1) for s in range(1 << n))
    # Semigroup <4,7> has genuine intermediate finite gaps.
    possible = bounded_additive_spectrum((4,7), 50)
    for n in (1,2,3,5,6,9,10,13,17):
        assert not possible[n], n
    for n in (4,7,8,11,12,14,15,16,18,19,20,21,22,23,24,25):
        assert possible[n], n
    print('ALL_CHECKS_OK', comparisons, allocations)

if __name__ == '__main__':
    main()
