#!/usr/bin/env python3
"""Independent finite checks of singleton two-colour rainbow domination on paths and cycles.

Run with Python 3.9+; no external packages required.
"""
import itertools
from collections import Counter
from math import comb


def cycle_coefficients(n):
    assert n >= 3
    answer = {}
    for zeros in range((n - 1) // 2 + 1):
        count_positions = (n * comb(n - zeros, zeros)) // (n - zeros)
        answer[n - zeros] = count_positions * (2 ** (n - 2 * zeros))
    if n % 4 == 0:
        answer[n // 2] = 4
    return answer


def path_coefficients(n):
    assert n >= 1
    return {
        n - zeros: comb(n - zeros - 1, zeros) * (2 ** (n - 2 * zeros))
        for zeros in range((n - 1) // 2 + 1)
    }


def brute_force(n, cyclic):
    counts = Counter()
    for assignment in itertools.product((0, 1, 2), repeat=n):
        valid = True
        for i, symbol in enumerate(assignment):
            if symbol:
                continue
            if cyclic:
                neighbours = (assignment[(i - 1) % n], assignment[(i + 1) % n])
            else:
                neighbours = (assignment[i - 1:i] if i else ()) + assignment[i + 1:i + 2]
            if set(neighbours) != {1, 2}:
                valid = False
                break
        if valid:
            counts[sum(symbol != 0 for symbol in assignment)] += 1
    return dict(counts)


def add(first, second):
    keys = set(first) | set(second)
    return {key: first.get(key, 0) + second.get(key, 0) for key in keys if first.get(key, 0) + second.get(key, 0)}


def shift(first, amount, factor=1):
    return {key + amount: value * factor for key, value in first.items() if value * factor}


def check_algebra():
    # A(n) = alpha^n + beta^n for alpha,beta roots of u^2 - 2*z*u - z.
    # T(n) = (i*sqrt(z))^n + (-i*sqrt(z))^n.
    a_prev = {0: 2}
    a_now = {1: 2}
    for n in range(2, 101):
        a_next = add(shift(a_now, 1, 2), shift(a_prev, 1))
        if n >= 3:
            correction = {n // 2: 2 * (-1) ** (n // 2)} if n % 2 == 0 else {}
            assert add(a_next, correction) == cycle_coefficients(n), n
        a_prev, a_now = a_now, a_next
    previous = {1: 2}
    current = {2: 4}
    for n in range(3, 101):
        nxt = add(shift(current, 1, 2), shift(previous, 1))
        assert nxt == path_coefficients(n), n
        previous, current = current, nxt


def main():
    comparisons = 0
    for n in range(1, 12):
        assert brute_force(n, False) == path_coefficients(n), ('path', n)
        comparisons += 3 ** n
    for n in range(3, 12):
        assert brute_force(n, True) == cycle_coefficients(n), ('cycle', n)
        comparisons += 3 ** n
    check_algebra()
    print(f'VERIFY_OK direct_assignments={comparisons} paths=1..11 cycles=3..11 recurrence_lengths=3..100')


if __name__ == '__main__':
    main()
