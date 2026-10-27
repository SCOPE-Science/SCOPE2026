#!/usr/bin/env python3
"""Independent finite checks of nilpotent partial-isometry rank enumerators.

The public mathematical certificate enumerates restrictions of dihedral
permutations and detects directed cycles directly. Python 3 standard library.
"""
from itertools import combinations
from math import comb, gcd


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def power(a, exponent):
    out = [1]
    for _ in range(exponent):
        out = poly_mul(out, a)
    return out


def euler_phi(m):
    return sum(gcd(j, m) == 1 for j in range(1, m+1))


def predicted(n):
    full = [0] * (n + 1)
    for order in range(1, n+1):
        if n % order:
            continue
        single = [comb(order, j) for j in range(order)]  # omit z^order
        block = power(single, n//order)
        for k, c in enumerate(block):
            full[k] += euler_phi(order) * c
    if n % 2:
        reflected = power([1, 2], (n-1)//2)
        for k, c in enumerate(reflected):
            full[k] += n*c
    else:
        for count, b in ((n//2, n//2-1), (n//2, n//2)):
            reflected = power([1,2], b)
            for k, c in enumerate(reflected):
                full[k] += count*c
    full[0] -= 2*n - 1
    full[1] -= n*(n-1)
    if n % 2 == 0:
        full[2] -= n*(n-2)//2
    return full


def is_nilpotent(partial):
    # Reject every directed cycle by following each chain.
    for x in partial:
        visited = set()
        while x in partial:
            if x in visited:
                return False
            visited.add(x)
            x = partial[x]
    return True


def observed(n):
    # Two lists: translations and reflections, each with n elements.
    permutations = []
    for c in range(n):
        permutations.append(tuple((x+c) % n for x in range(n)))
        permutations.append(tuple((c-x) % n for x in range(n)))
    maps = {}
    for perm in permutations:
        for size in range(n+1):
            for domain in combinations(range(n), size):
                restriction = tuple((x, perm[x]) for x in domain)
                maps[restriction] = None
    rank_count = [0]*(n+1)
    maximal_index = 0
    for restriction in maps:
        part = dict(restriction)
        if is_nilpotent(part):
            rank_count[len(restriction)] += 1
            if len(restriction) == n-1:
                maximal_index += 1
    return rank_count, len(maps), maximal_index


def main():
    for n in range(3, 11):
        actual, size, top = observed(n)
        expected = predicted(n)
        assert actual == expected, (n, actual, expected)
        assert top == n*euler_phi(n), (n, top)
        # Independently match the total cardinality in Fernandes--Paulista.
        if n % 2:
            expected_size = n*2**(n+1)-n*n-2*n+1
        else:
            expected_size = n*2**(n+1)-3*n*n//2-2*n+1
        assert size == expected_size, (n, size, expected_size)
        assert expected[-1] == 0
        print('n=', n, 'coefficients=', expected,
              'nilpotent_total=', sum(expected), 'monoid_size=', size,
              'maximal_index_count=', top)
    print('VERIFY_OK cycle partial-isometry nilpotent rank polynomial')


if __name__ == '__main__':
    main()
