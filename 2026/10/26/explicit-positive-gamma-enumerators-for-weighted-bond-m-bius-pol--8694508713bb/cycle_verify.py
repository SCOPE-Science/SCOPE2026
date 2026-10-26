#!/usr/bin/env python3
"""Exact finite checks for the gamma-enumerator of weighted bond Möbius polynomials on cycles.
No third-party dependencies; Python 3.9+."""
from fractions import Fraction
from math import factorial


def partitions(n):
    # Canonical restricted-growth strings: each set partition exactly once.
    word = [0] * n
    def go(i, maximum):
        if i == n:
            masks = [0] * (maximum + 1)
            for v, p in enumerate(word):
                masks[p] |= 1 << v
            yield masks
        else:
            for p in range(maximum + 2):
                word[i] = p
                yield from go(i + 1, max(maximum, p))
    yield from go(1, 0)


def connected(mask, adjacency):
    seen = mask & -mask
    while True:
        grow = seen
        for v, adj in enumerate(adjacency):
            if seen & (1 << v):
                grow |= adj & mask
        if grow == seen:
            return seen == mask
        seen = grow


def edges(n, cycle):
    adj = [0] * n
    for i in range(n - 1):
        adj[i] |= 1 << (i + 1)
        adj[i + 1] |= 1 << i
    if cycle:
        adj[0] |= 1 << (n - 1)
        adj[n - 1] |= 1
    return adj


def add(A, B):
    R = [0] * max(len(A), len(B))
    for i, a in enumerate(A):
        R[i] += a
    for i, b in enumerate(B):
        R[i] += b
    return R


def multiply(A, B):
    R = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            R[i + j] += a * b
    return R


def negate(A):
    return [-a for a in A]


def mobius_from_partitions(n, cycle, path_mu):
    graph = edges(n, cycle)
    value = [0]
    count = 0
    for blocks in partitions(n):
        if len(blocks) == 1 or not all(connected(B, graph) for B in blocks):
            continue
        product = [1]
        for block in blocks:
            product = multiply(product, path_mu[block.bit_count()])
        value = add(value, multiply(product, [1] * len(blocks)))
        count += 1
    return negate(value), count


def multinomial(n, p, q, r):
    if min(p, q, r) < 0 or p + q + r != n:
        return 0
    return factorial(n) // (factorial(p) * factorial(q) * factorial(r))


def gamma_formula(n, j):
    # Independent Lagrange inversion of the weighted unary--binary tree model.
    total = Fraction(0)
    for r in range(j + 1):
        total += Fraction(2*r + 2, n) * multinomial(n, j-r, n-2*j-2, j+r+2)
    for r in range(j):
        total += Fraction(2*r + 3, n) * multinomial(n, j-r-1, n-2*j-1, j+r+2)
    assert total.denominator == 1
    return total.numerator


def gamma_to_coeffs(n):
    result = [0] * n
    for j in range((n - 1)//2 + 1):
        gamma = gamma_formula(n, j)
        base = [1]
        for _ in range(n-1-2*j):
            base = multiply(base, [1, 1])
        for k, val in enumerate(base):
            result[j + k] += gamma * val
    return result


def main():
    path_mu = {1: [1]}
    # Independent literal bond-lattice recurrence using all set partitions.
    for n in range(2, 10):
        path_mu[n], _ = mobius_from_partitions(n, False, path_mu)
        # Do not truncate before division when evaluating Narayana numbers.
        expected_path = [(-1)**(n-1) * (factorial(n)//(factorial(j)*factorial(n-j))) * (factorial(n)//(factorial(j+1)*factorial(n-j-1))) // n for j in range(n)]
        assert path_mu[n] == expected_path, ('path', n, path_mu[n], expected_path)
    count = 0
    for n in range(3, 10):
        mu, checked = mobius_from_partitions(n, True, path_mu)
        count += checked
        c = [(-1)**(n-1) * c for c in mu]
        computed = gamma_to_coeffs(n)
        assert c == computed, (n, c, computed)
        gs = [gamma_formula(n, j) for j in range((n-1)//2 + 1)]
        print('cycle n=%d gamma=%s bond_partitions=%d' % (n, gs, checked))
    for n in range(3, 81):
        values = [gamma_formula(n, j) for j in range((n-1)//2+1)]
        assert all(x > 0 for x in values), n
        assert values[0] == n-1, n
    print('VERIFY_OK independent_bond_partition_orders=3..9 cyclic_orders=3..80 bond_partition_instances=%d' % count)

if __name__ == '__main__':
    main()
