#!/usr/bin/env python3
"""Independent finite exact checks for the public BST covariance identity."""
from fractions import Fraction
from itertools import permutations
from math import factorial


def harmonic(n, k=1):
    return sum((Fraction(1, j ** k) for j in range(1, n + 1)), Fraction())


def covariance_formula(n):
    return 3 * n + harmonic(n) - 2 * (n + 1) * harmonic(n, 2)


def insertion_path_length(order):
    if not order:
        return 0
    root = order[0]
    left, right = {}, {}
    total = 0
    for key in order[1:]:
        node = root
        depth = 0
        while True:
            depth += 1
            if key < node:
                if node not in left:
                    left[node] = key
                    break
                node = left[node]
            else:
                if node not in right:
                    right[node] = key
                    break
                node = right[node]
        total += depth
    return total


def upper_record_count(order):
    maximum, records = 0, 0
    for key in order:
        if key > maximum:
            maximum, records = key, records + 1
    return records


def run():
    tests = 0
    means_p = [Fraction()] * 101
    means_r = [Fraction()] * 101
    mixed = [Fraction()] * 101
    for n in range(1, 101):
        means_p[n] = 2 * (n + 1) * harmonic(n) - 4 * n
        means_r[n] = harmonic(n)
        mixed[n] = means_p[n] + sum(
            (mixed[j] + (means_p[n - 1 - j] + n - 1) * means_r[j]
             for j in range(n)), Fraction()) / n
        assert mixed[n] - means_p[n] * means_r[n] == covariance_formula(n)
        tests += 1
    for n in range(1, 9):
        sum_p = sum_r = sum_pr = 0
        for order in permutations(range(1, n + 1)):
            p = insertion_path_length(order)
            r = upper_record_count(order)
            sum_p += p
            sum_r += r
            sum_pr += p * r
            tests += 1
        f = factorial(n)
        assert Fraction(sum_p, f) == means_p[n]
        assert Fraction(sum_r, f) == means_r[n]
        assert Fraction(sum_pr, f) == mixed[n]
        assert Fraction(sum_pr, f) - Fraction(sum_p * sum_r, f * f) == covariance_formula(n)
        tests += 4
    assert covariance_formula(1) == 0 and covariance_formula(2) == 0
    for n in range(2, 101):
        delta = covariance_formula(n + 1) - covariance_formula(n)
        expected = 3 - 2 * harmonic(n, 2) - Fraction(n + 3, (n + 1) ** 2)
        assert delta == expected and delta < 0
        tests += 2
    print(f'VERIFY_OK {tests} exact checks')


if __name__ == '__main__':
    run()
