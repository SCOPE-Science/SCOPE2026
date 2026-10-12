#!/usr/bin/env python3
"""Raw-vertex exhaustive maximum-code census for short mixed cycle channels.

This implementation constructs the entire 5*n-vertex confusability graph,
complements it, then enumerates maximal cliques using bitsets. It does not
use the cyclic-column state or compatibility transition in verify.py.
"""
from math import comb


def census(n):
    vertices = [(a, b) for a in range(5) for b in range(n)]
    count = len(vertices)
    allowed = [0] * count
    for i, (a, b) in enumerate(vertices):
        mask = 0
        for j, (c, d) in enumerate(vertices):
            if i == j:
                continue
            x = (a-c) % 5
            y = (b-d) % n
            confusable = x in (0, 1, 4) and y in (0, 1, n-1)
            if not confusable:
                mask |= 1 << j
        allowed[i] = mask

    largest, how_many = 0, 0

    def maximal_cliques(r, p, x):
        nonlocal largest, how_many
        size = r.bit_count()
        if size + p.bit_count() < largest:
            return
        if p == 0 and x == 0:
            if size > largest:
                largest, how_many = size, 1
            elif size == largest:
                how_many += 1
            return
        union = p | x
        pivot = -1
        max_neighbors = -1
        while union:
            bit = union & -union
            vertex = bit.bit_length() - 1
            degree = (p & allowed[vertex]).bit_count()
            if degree > max_neighbors:
                max_neighbors = degree
                pivot = vertex
            union -= bit
        candidates = p & ~allowed[pivot] if pivot >= 0 else p
        while candidates:
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            maximal_cliques(r | bit, p & allowed[v], x & allowed[v])
            p ^= bit
            x |= bit
            candidates ^= bit
    maximal_cliques(0, (1 << count)-1, 0)
    return largest, how_many


def predicted(n):
    walk = 5 * sum(comb(n, k) for k in range(n+1) if (2*k - n) % 5 == 0)
    return walk + (2*5**(n//2) if n%2 == 0 else 0)


def main():
    for n in range(6, 10):
        size, count = census(n)
        expected = predicted(n)
        assert (size, count) == (n, expected), (n, size, count, expected)
        print(f"n={n}: maximum_size={size}, optimal_codes={count}")
    print('GRAPH_VERIFY_OK')


if __name__ == '__main__':
    main()
