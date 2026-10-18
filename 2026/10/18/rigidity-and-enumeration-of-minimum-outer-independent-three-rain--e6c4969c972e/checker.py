"""Finite verification for outer-independent 3-rainbow labelings of Möbius ladders.

Uses only the Python standard library. Every subset of the fixed optimal
weight is visited in the exhaustive cases; these checks are not the proof
of the infinite statements.
"""
from itertools import combinations, product


def graph(m):
    assert m >= 3
    N = [set() for _ in range(2 * m)]
    def edge(a, b):
        N[a].add(b)
        N[b].add(a)
    for i in range(m):
        edge(2*i, 2*i+1)
        if i+1 < m:
            edge(2*i, 2*(i+1))
            edge(2*i+1, 2*(i+1)+1)
        else:
            edge(2*i, 1)
            edge(2*i+1, 0)
    return N


def count_at_weight(m, weight):
    """Count ALL legal labelings of exactly the given weight."""
    N = graph(m)
    V = range(2*m)
    total = 0
    for z in range(2*m + 1):
        surplus = weight - (2*m-z)
        if surplus not in (0, 1):
            continue  # Only the weight levels used in the listed cases.
        for zeros_tuple in combinations(V, z):
            zeros = set(zeros_tuple)
            if any(any(u in zeros for u in N[v]) for v in zeros):
                continue
            positive = [v for v in V if v not in zeros]
            choices_of_double = [None] if surplus == 0 else positive
            for doubled in choices_of_double:
                colors = [[3, 5, 6] if v == doubled else [1, 2, 4]
                          for v in positive]
                for labels in product(*colors):
                    f = dict(zip(positive, labels))
                    feasible = True
                    for v in zeros:
                        merged = 0
                        for u in N[v]:
                            merged |= f.get(u, 0)
                        if merged != 7:
                            feasible = False
                            break
                    total += feasible
    return total


def one_double_word_count(m):
    """Independent check for one fixed double location, m=5 or 11.

    With a zero in every rung, the other layer is a circular word.
    This tests every singleton word and every two-color mask at index 0.
    """
    count = 0
    for doubled in (3, 5, 6):
        for suffix in product((1, 2, 4), repeat=m-1):
            word = (doubled,) + suffix
            if all((word[(i-1) % m] | word[i] |
                    word[(i+1) % m]) == 7 for i in range(m)):
                count += 1
    return count


if __name__ == '__main__':
    for m, expected in [(3,12),(4,48),(5,60),(6,72),
                        (8,96),(9,12),(10,120)]:
        optimum = m if m % 6 == 3 else m+1
        got = count_at_weight(m, optimum)
        assert got == expected, (m,got,expected)
        print(m, got)
    assert one_double_word_count(5) == 6
    assert one_double_word_count(11) == 6
    print('Fixed-double cyclic-word checks: m=5 and m=11, six words each')
