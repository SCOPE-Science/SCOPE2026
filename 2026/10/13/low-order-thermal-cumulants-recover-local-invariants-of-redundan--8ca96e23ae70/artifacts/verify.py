#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product
from collections import Counter


def sign_word(word, edges):
    parity = 0
    for a in range(len(word)):
        for b in range(a + 1, len(word)):
            if word[a] > word[b] and tuple(sorted((word[a], word[b]))) in edges:
                parity ^= 1
    return -1 if parity else 1


def direct_moment(couplings, edges, order):
    total = Fraction(0, 1)
    for word in product(range(len(couplings)), repeat=order):
        counts = Counter(word)
        if any(value % 2 for value in counts.values()):
            continue
        term = Fraction(sign_word(word, edges), 1)
        for index in word:
            term *= couplings[index]
        total += term
    return total


def closed_moments(couplings, edges):
    x = [value * value for value in couplings]
    n = len(x)
    p1 = sum(x)
    p2 = sum(value * value for value in x)
    p3 = sum(value * value * value for value in x)
    edge_mass = sum(x[i] * x[j] for i, j in edges)
    q = sum(x[i] * x[j] * (x[i] + x[j]) for i, j in edges)
    w = Fraction(0, 1)
    for i in range(n):
        neighbors = [j for j in range(n) if j != i and tuple(sorted((i, j))) in edges]
        for j, k in combinations(neighbors, 2):
            w += x[i] * x[j] * x[k]
    t = Fraction(0, 1)
    for i, j, k in combinations(range(n), 3):
        if {(i, j), (i, k), (j, k)} <= edges:
            t += x[i] * x[j] * x[k]
    m4 = 3 * p1 * p1 - 2 * p2 - 4 * edge_mass
    m6 = (15 * p1**3 - 30 * p1 * p2 + 16 * p3
          - 60 * p1 * edge_mass + 48 * q + 48 * w - 48 * t)
    return m4, m6


def main():
    vertices = range(4)
    all_edges = list(combinations(vertices, 2))
    couplings = [Fraction(1), Fraction(2), Fraction(3), Fraction(4)]
    for mask in range(1 << len(all_edges)):
        edges = {all_edges[k] for k in range(len(all_edges)) if (mask >> k) & 1}
        m4, m6 = closed_moments(couplings, edges)
        assert direct_moment(couplings, edges, 4) == m4
        assert direct_moment(couplings, edges, 6) == m6

        degrees = [sum(tuple(sorted((i, j))) in edges for j in vertices if j != i) for i in vertices]
        if len(set(degrees)) == 1:
            d = degrees[0]
            t = sum(1 for triple in combinations(vertices, 3)
                    if set(combinations(triple, 2)) <= edges)
            m = 4
            unit = [Fraction(1)] * m
            um4, um6 = closed_moments(unit, edges)
            c4 = Fraction(um4, 24) - Fraction(m * m, 8)
            c6 = Fraction(um6, 720) - Fraction(m * um4, 48) + Fraction(m**3, 24)
            assert c4 == -Fraction(m * (d + 1), 12)
            assert c6 == Fraction(m, 45) + Fraction(m * d * (d + 1), 30) - Fraction(t, 15)
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
