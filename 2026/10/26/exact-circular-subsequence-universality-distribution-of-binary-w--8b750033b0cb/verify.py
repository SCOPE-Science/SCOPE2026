#!/usr/bin/env python3
"""Finite checks for an exact circular binary subsequence-universality law.

Requires only the Python 3 standard library. No result is inferred
from finite agreement: the accompanying proof handles arbitrary lengths.
"""
from collections import Counter
from math import comb


def linear_index(word):
    # Greedy complete-alphabet arches for the fixed alphabet {0,1}.
    present = 0
    arches = 0
    for bit in word:
        present |= 1 << bit
        if present == 3:
            arches += 1
            present = 0
    return arches


def rotation_index(word):
    length = len(word)
    return max(linear_index(word[cut:] + word[:cut])
               for cut in range(length))


def transition_matching_index(word):
    # Independent run-of-edges maximum matching, including the even cycle.
    length = len(word)
    transitions = [word[i] != word[(i + 1) % length]
                   for i in range(length)]
    if all(transitions):
        assert length % 2 == 0
        return length // 2
    if not any(transitions):
        return 0
    cut = transitions.index(False)
    linear_edges = transitions[cut + 1:] + transitions[:cut]
    matches = 0
    streak = 0
    for edge in linear_edges:
        if edge:
            streak += 1
        else:
            matches += (streak + 1) // 2
            streak = 0
    return matches + (streak + 1) // 2


def choose(top, bottom):
    return comb(top, bottom) if 0 <= bottom <= top else 0


def exact_count(n, k):
    if k < 0 or k > n // 2:
        return 0
    if k == 0:
        return 2
    return (1 << k) * (choose(n - k - 1, k) +
                       2 * choose(n - k - 1, k - 1)) - 2 * (n == 2 * k)


def coefficient_recurrence(max_n):
    # a_m(u)=[z^m](1-z-2u z^2)^(-1), so
    # a_m=a_{m-1}+2u a_{m-2}. This independently expands the rational form.
    p = [[1], [1]]
    for m in range(2, max_n):
        old, prev = p[m - 2], p[m - 1]
        row = [0] * max(len(prev), len(old) + 1)
        for j, coeff in enumerate(prev):
            row[j] += coeff
        for j, coeff in enumerate(old):
            row[j + 1] += 2 * coeff
        p.append(row)
    for n in range(1, max_n + 1):
        coeff = p[n - 1][:]
        if n >= 2:
            for k, value in enumerate(p[n - 2]):
                if len(coeff) <= k + 1:
                    coeff.extend([0] * (k + 2 - len(coeff)))
                coeff[k + 1] += 4 * value
        coeff[0] += 1
        if n % 2 == 0:
            coeff[n // 2] -= 2
        assert len(coeff) <= 1 + n // 2
        assert sum(coeff) == (1 << n)
        for k in range(n // 2 + 1):
            assert (coeff[k] if k < len(coeff) else 0) == exact_count(n, k), (n, k)


def exhaustive(max_n):
    checked = 0
    for n in range(1, max_n + 1):
        observations = Counter()
        for packed in range(1 << n):
            word = tuple((packed >> j) & 1 for j in range(n))
            by_rotation = rotation_index(word)
            by_matching = transition_matching_index(word)
            assert by_rotation == by_matching, (n, packed, by_rotation, by_matching)
            observations[by_rotation] += 1
            checked += 1
        for k in range(n // 2 + 1):
            assert observations[k] == exact_count(n, k), (n, k)
        assert sum(observations.values()) == (1 << n)
    return checked


if __name__ == '__main__':
    compared = exhaustive(17)
    coefficient_recurrence(256)
    print(f'CIRCULAR_BINARY_SUBSEQUENCE_CENSUS_PASS brute_words={compared}'
          ' brute_lengths=1..17 gf_coefficients=1..256')
