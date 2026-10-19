#!/usr/bin/env python3
"""Exhaustive small-case verification of the exact PAL3 descendant formula."""
from itertools import product
from fractions import Fraction


def dup3(word, i):
    assert 0 <= i <= len(word) - 3
    return word[:i+3] + word[i:i+3][::-1] + word[i+3:]


def equal_length_runs(word, start, count):
    return len(set(word[start:start+count])) == 1


def motif_count(word, distance):
    assert distance in (3, 4, 5)
    n = len(word)
    total = 0
    for i in range(max(0, n-distance-2)):
        chunk = word[i:i+distance+3]
        a, b = chunk[0], chunk[1]
        if distance == 3:
            # abaaba, with a != b
            wanted = (a, b, a, a, b, a)
        elif distance == 4:
            # baaaaba, with a != b; set b = first symbol
            b, a = chunk[0], chunk[1]
            wanted = (b, a, a, a, a, b, a)
        else:
            # bbaabbab, with a != b; set b = first symbol
            b, a = chunk[0], chunk[2]
            wanted = (b, b, a, a, b, b, a, b)
        total += (a != b and tuple(chunk) == wanted)
    return total


def formula(word):
    n = len(word)
    if n < 3:
        return 0
    constant4 = sum(equal_length_runs(word, i, 4) for i in range(n-3))
    return (n-2) - constant4 - sum(motif_count(word, d) for d in (3, 4, 5))


def expectation(q, n):
    z = Fraction(n-2) - Fraction(n-3, q**3)
    for d in (3, 4, 5):
        z -= Fraction(max(0, n-d-2)*(q-1), q**(d+2))
    return z


def run():
    tested = 0
    for q, maximum_n in [(2, 14), (3, 11), (4, 9), (5, 7)]:
        for n in range(3, maximum_n+1):
            sum_size = 0
            for word in product(range(q), repeat=n):
                desc = [dup3(word, i) for i in range(n-2)]
                actual = len(set(desc))
                predicted = formula(word)
                if predicted != actual:
                    raise AssertionError(('sphere', q, n, word, actual, predicted))
                # Independent check: only the stated local edges link consecutive
                # indices in each equivalence class.
                classes = {}
                for i, result in enumerate(desc):
                    classes.setdefault(result, []).append(i)
                expected_edges = []
                for positions in classes.values():
                    for i, j in zip(positions, positions[1:]):
                        expected_edges.append((i, j))
                actual_edges = []
                for i in range(n-2):
                    if i+1 < n-2 and equal_length_runs(word, i, 4):
                        actual_edges.append((i, i+1))
                    for d in (3, 4, 5):
                        if i+d < n-2 and motif_count(word[i:i+d+3], d):
                            actual_edges.append((i, i+d))
                if sorted(expected_edges) != sorted(actual_edges):
                    raise AssertionError(('edges', q, n, word, expected_edges, actual_edges))
                sum_size += actual
                tested += 1
            if Fraction(sum_size, q**n) != expectation(q, n):
                raise AssertionError(('mean', q, n, sum_size, expectation(q, n)))
    print(f'PALINDROMIC_LENGTH3_FORMULA_PASS words={tested} q=2..5 ranges=(14,11,9,7)')

if __name__ == '__main__':
    run()
