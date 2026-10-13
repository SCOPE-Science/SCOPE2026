"""Independent finite checks for the zero-forcing polynomial of crown graphs.

Run: python3 verify.py
This is finite corroboration, not a proof of the statement for every n.
"""
from collections import Counter
from math import comb
from itertools import combinations


def neighbor_masks(n):
    return [sum(1 << (n + j) for j in range(n) if j != i)
            for i in range(n)] + [sum(1 << j for j in range(n) if j != i)
                                   for i in range(n)]


def forcing_serial(n, blue, neighbors):
    white = ((1 << (2 * n)) - 1) ^ blue
    while white:
        progress = False
        for vertex, mask in enumerate(neighbors):
            if white & (1 << vertex):
                continue
            candidates = mask & white
            if candidates != 0 and candidates & (candidates - 1) == 0:
                white ^= candidates
                progress = True
                break
        if not progress:
            return False
    return True


def forcing_parallel(n, blue):
    blue_vertices = {v for v in range(2 * n) if blue & (1 << v)}
    white_vertices = set(range(2 * n)) - blue_vertices
    while white_vertices:
        new_vertices = set()
        for vertex in blue_vertices:
            if vertex < n:
                possible = {n + j for j in range(n) if j != vertex}
            else:
                possible = {j for j in range(n) if j != vertex - n}
            remaining = possible & white_vertices
            if len(remaining) == 1:
                new_vertices.update(remaining)
        if not new_vertices:
            return False
        blue_vertices.update(new_vertices)
        white_vertices.difference_update(new_vertices)
    return True


def structural_test(n, blue):
    white_a = {i for i in range(n) if not blue & (1 << i)}
    white_b = {i for i in range(n) if not blue & (1 << (n + i))}
    return len(white_a) <= 2 and len(white_b) <= 2 and not (
        len(white_a) == len(white_b) == 2 and white_a == white_b)


def predicted_coefficients(n):
    c = comb(n, 2)
    return {2 * n - 4: c * (c - 1),
            2 * n - 3: n * n * (n - 1),
            2 * n - 2: comb(2 * n, 2),
            2 * n - 1: 2 * n,
            2 * n: 1}


def all_minimum_extensions(n, blue):
    # Test only sets known to be zero-forcing; the enumeration is independent
    # of the proof that all such sets admit a minimum-size subset.
    white_a = {i for i in range(n) if not blue & (1 << i)}
    white_b = {i for i in range(n) if not blue & (1 << (n + i))}
    for a_pair in combinations(range(n), 2):
        if not white_a.issubset(a_pair):
            continue
        for b_pair in combinations(range(n), 2):
            if not white_b.issubset(b_pair) or a_pair == b_pair:
                continue
            return True
    return False


def algebra_coefficients(n):
    # Explicit multiplication of polynomial Q(y-n/2), with exact integer
    # arithmetic after multiplication by 16, confirms the shift identity.
    # 16*Q(y-n/2) has nonzero degrees only 4,2,0.
    from fractions import Fraction
    from math import comb as choose
    c = choose(n, 2)
    q = [c * (c - 1), n * n * (n - 1), n * (2 * n - 1), 2 * n, 1]
    shift = Fraction(-n, 2)
    translated = [Fraction(0) for _ in range(5)]
    for degree, coefficient in enumerate(q):
        for power in range(degree + 1):
            translated[power] += coefficient * choose(degree, power) * shift ** (degree-power)
    expected = [Fraction(n * (n**3 - 4*n*n - 4*n + 8), 16),
                Fraction(0), Fraction(n*(n-2), 2), Fraction(0), Fraction(1)]
    return translated == expected


def main():
    total = 0
    parallel_count = 0
    minimum_count = 0
    for n in range(3, 11):
        neighbor = neighbor_masks(n)
        counts = Counter()
        for blue in range(1 << (2 * n)):
            predicted = structural_test(n, blue)
            actual = forcing_serial(n, blue, neighbor)
            assert actual == predicted, (n, blue, actual, predicted)
            if n <= 7:
                assert forcing_parallel(n, blue) == actual, (n, blue)
                parallel_count += 1
            if actual:
                counts[blue.bit_count()] += 1
                if n <= 7:
                    assert all_minimum_extensions(n, blue), (n, blue)
                    minimum_count += 1
            total += 1
        assert dict(counts) == predicted_coefficients(n), (n, counts)
        assert algebra_coefficients(n)
        print('n=%d: subsets=%d, forcing-coefficients=%s, classification PASS' %
              (n, 1 << (2*n), dict(sorted(counts.items()))))
    print('PASS all: %d serial subsets; %d parallel corroborations;'
          ' %d finite minimum-extension tests; 8 exact shift identities.' %
          (total, parallel_count, minimum_count))


if __name__ == '__main__':
    main()
