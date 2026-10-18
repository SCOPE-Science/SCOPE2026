#!/usr/bin/env python3
"""Reproduce finite checks of shortest Green-class representatives in free inverse monoids.

Run with: python3 artifacts/verify.py
Uses only the Python standard library. Enumerations are finite consistency checks;
the general space bound follows from the accompanying mathematical proof.
"""
from collections import defaultdict
from itertools import product


def reduce_word(word):
    stack = []
    for letter in word:
        if stack and stack[-1] == -letter:
            stack.pop()
        else:
            stack.append(letter)
    return tuple(stack)


def inverse(word):
    return tuple(-letter for letter in word[::-1])


def mul(a, b):
    return reduce_word(a + b)


def distance(a, b):
    return len(mul(inverse(a), b))


def munn(word):
    vertex = ()
    vertices = {vertex}
    for letter in word:
        vertex = mul(vertex, (letter,))
        vertices.add(vertex)
    return frozenset(vertices), vertex


def translate_to(vertex, vertices):
    return frozenset(mul(inverse(vertex), v) for v in vertices)


def d_invariant(vertices):
    return min(tuple(sorted(translate_to(v, vertices))) for v in vertices)


def checks(rank, length_limit):
    alphabet = tuple(i for a in range(1, rank + 1) for i in (a, -a))
    records = []
    for n in range(length_limit + 1):
        for word in product(alphabet, repeat=n):
            vertices, terminal = munn(word)
            edge_count = len(vertices) - 1
            origin_ecc = max(distance((), v) for v in vertices)
            terminal_ecc = max(distance(terminal, v) for v in vertices)
            diameter = max(distance(a, b) for a in vertices for b in vertices)
            formula = (
                2 * edge_count - distance((), terminal),
                2 * edge_count - origin_ecc,
                2 * edge_count - terminal_ecc,
                2 * edge_count - diameter,
            )
            keys = (
                (vertices, terminal),
                vertices,
                translate_to(terminal, vertices),
                d_invariant(vertices),
            )
            records.append((n, keys, formula, word))
    least = [dict() for _ in range(4)]
    for length, keys, _, _ in records:
        for j in range(4):
            least[j][keys[j]] = min(length, least[j].get(keys[j], length))
    geodesics = [0] * 4
    for length, keys, formula, word in records:
        for j in range(4):
            actual = least[j][keys[j]]
            assert actual == formula[j], (rank, word, j, actual, formula[j])
            if actual == length:
                geodesics[j] += 1
    return len(records), tuple(geodesics)


def main():
    total = 0
    for rank, max_length in ((1, 10), (2, 6), (3, 4)):
        count, counts = checks(rank, max_length)
        total += count
        print(f'rank={rank} maximum_length={max_length} words={count} total_geodesic_words_H_R_L_D={counts}')
    print(f'VERIFY_OK: {total} complete words; four Green-class distance formulae tested independently')


if __name__ == '__main__':
    main()
