"""Reproduce exact finite checks for the Minkowski asymmetry of stellohedra.

Standard-library only. Finite examples supplement, not replace, the proof.
Run: python verify.py
"""
from fractions import Fraction
from itertools import permutations
from math import factorial


def simplices(k):
    return [tuple([k] + [i for i in range(k) if mask & (1 << i)])
            for mask in range(1, 1 << k)]


def subset_bounds(k, mask, tubes):
    subset = {i for i in range(k + 1) if (mask >> i) & 1}
    return (sum(set(t).issubset(subset) for t in tubes),
            sum(not set(t).isdisjoint(subset) for t in tubes))


def verify():
    total_vertices = 0
    total_subsets = 0
    for k in range(1, 7):
        n = k + 1
        tubes = simplices(k)
        count = (1 << k) - 1
        s = Fraction(k * 2 ** (k - 1), count)
        leaf = Fraction(2 ** (k - 1), 1) / (s + 1)
        center = [leaf] * k + [Fraction(count) - k * leaf]
        # Both sides of the necessary-and-sufficient containment inequalities.
        for mask in range(1 << n):
            low, high = subset_bounds(k, mask, tubes)
            cval = sum(center[i] for i in range(n) if (mask >> i) & 1)
            assert (s + 1) * cval >= s * low + high
            assert (s + 1) * cval <= s * high + low
            total_subsets += 1
        # Independent greedy-vertex check on the actually reflected vertices.
        for ordering in permutations(range(n)):
            position = {v: j for j, v in enumerate(ordering)}
            vertex = [0] * n
            for tube in tubes:
                vertex[min(tube, key=lambda v: position[v])] += 1
            assert sum(vertex) == count
            reflected = [((s + 1) * center[i] - vertex[i]) / s
                         for i in range(n)]
            for mask in range(1 << n):
                low, high = subset_bounds(k, mask, tubes)
                value = sum(reflected[i] for i in range(n)
                            if (mask >> i) & 1)
                assert low <= value <= high
            total_vertices += 1
        # The strict concavity of F(a)=2**k-2**(k-a) is checked exactly.
        ratios = [Fraction(2 ** k - 2 ** (k - a), a)
                  for a in range(1, k + 1)]
        assert all(ratios[i] > ratios[i + 1]
                   for i in range(k - 1))
        assert ratios[0] == 2 ** (k - 1)
        assert ratios[-1] == Fraction(count, k)
        print(f'k={k}: s={s}, leaf={leaf}, hub={center[-1]}, '
              f'greedy_orderings={factorial(n)}, subset_inequalities={1 << n}')
    print(f'PASS: {total_vertices} greedy orderings and '
          f'{total_subsets} center subset checks, with all reflected subset checks.')


if __name__ == '__main__':
    verify()
