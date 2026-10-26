#!/usr/bin/env python3
"""Exact finite checks for prime-power left-right orbit signatures."""
from itertools import permutations
from math import gcd


def reverse_digits(j, p, k):
    result = 0
    for _ in range(k):
        result = p * result + (j % p)
        j //= p
    return result


def signature(permutation):
    n = len(permutation)
    rows = []
    for x in range(n):
        y = x
        row = []
        for _ in range(1, n):
            y = permutation[y]
            row.append((y > x) - (y < x))
        rows.append(tuple(row))
    return tuple(rows)


def powering(permutation, u):
    n = len(permutation)
    output = []
    for x in range(n):
        y = x
        for _ in range(u):
            y = permutation[y]
        output.append(y)
    return output


def equal_signature_units(permutation):
    n = len(permutation)
    expected = signature(permutation)
    return [u for u in range(1, n) if gcd(u, n) == 1
            and signature(powering(permutation, u)) == expected]


def reversal_cycle(p, k):
    n = p ** k
    order = [reverse_digits(j, p, k) for j in range(n)]
    permutation = [0] * n
    for j in range(n):
        permutation[order[j]] = order[(j + 1) % n]
    return permutation


def every_cycle(n):
    for order in permutations(range(1, n)):
        cycle = (0,) + order
        permutation = [0] * n
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            permutation[a] = b
        yield permutation


def main():
    checks = 0
    for p, k in ((2, 2), (2, 3), (2, 4), (3, 2), (3, 3), (5, 2)):
        permutation = reversal_cycle(p, k)
        n = p ** k
        obtained = equal_signature_units(permutation)
        predicted = [u for u in range(1, n) if u % p == 1]
        assert obtained == predicted, (p, k, obtained, predicted)
        checks += 1
        print('digit reversal:', 'prime', p, 'exponent', k, 'multiplicity', len(obtained))
    for n, prime in ((4, 2), (8, 2), (9, 3)):
        maximum = 0
        number = 0
        for permutation in every_cycle(n):
            size = len(equal_signature_units(permutation))
            assert size <= n // prime, (n, permutation, size)
            maximum = max(maximum, size)
            number += 1
            checks += 1
        assert maximum == n // prime
        print('exhaustive cycles:', n, 'tested:', number, 'maximum:', maximum)
    print('PASS:', checks, 'independent finite cases')

if __name__ == '__main__':
    main()
