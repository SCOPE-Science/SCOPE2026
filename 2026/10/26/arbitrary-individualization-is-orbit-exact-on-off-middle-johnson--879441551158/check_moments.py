#!/usr/bin/env python3
"""Exact independent checks for the odd neighbour-displacement moment lemma."""
from itertools import combinations
from random import Random


def poly(delta, subset):
    if len(subset) % 2:
        value = 1
        for i in subset:
            value *= delta[i]
        return value
    j = subset[0]
    value = delta[j] * delta[j]
    for i in subset[1:]:
        value *= delta[i]
    return value


def moment_coefficient(n, markers, subset, target):
    # Extract multilinear coefficient of product of a_i for i in target.
    value = 0
    for bits in range(1 << len(target)):
        a = [0] * len(markers)
        for j, i in enumerate(target):
            a[i] = (bits >> j) & 1
        total = 0
        for b in range(n):
            t = [int(b in marker) for marker in markers]
            total += poly([t[i] - a[i] for i in range(len(markers))], subset)
        value += (-1 if (len(target) - bits.bit_count()) % 2 else 1) * total
    return value


def check(n, k, marks):
    r = len(marks)
    allx = list(combinations(range(n), k))
    subsets = [tuple(i for i in range(r) if mask & (1 << i))
               for mask in range(1, 1 << r)]
    for subset in subsets:
        coefficient = moment_coefficient(n, marks, subset, subset)
        expected = -n if len(subset) % 2 else -(n - 2*k)
        assert coefficient == expected, (n, k, subset, coefficient, expected)
    # Direct pairwise comparison of the two expressions of odd swap moment.
    for xx in allx[:min(30, len(allx))]:
        X = set(xx)
        for subset in subsets:
            left, right = 0, 0
            for a in X:
                for b in range(n):
                    delta = [int(b in marker)-int(a in marker) for marker in marks]
                    term = poly(delta, subset)
                    right += term
                    if b not in X:
                        left += term
            assert left == right, (n, k, subset, left, right)
    return len(subsets), min(30, len(allx)) * len(subsets)


def main():
    rng = Random(30812026)
    total_coeff = 0
    total_moments = 0
    total_sets = 0
    for n, k in [(7, 3), (9, 4), (11, 5)]:
        base = list(combinations(range(n), k))
        for r in range(1, 7):
            for _ in range(3):
                indexes = rng.sample(range(len(base)), r)
                markers = [set(base[i]) for i in indexes]
                coeff, moments = check(n, k, markers)
                total_coeff += coeff
                total_moments += moments
                total_sets += 1
        print('PASS moment family n=%d k=%d' % (n, k))
    print('ALL_TESTS_PASS marked_sets=%d leading_coefficients=%d exact_swap_moments=%d' %
          (total_sets, total_coeff, total_moments))


if __name__ == '__main__':
    main()
