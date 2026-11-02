#!/usr/bin/env python3
"""Exact modular Krylov-rank checks for the two-leaf capture theorem.

The proof is algebraic; this script independently constructs adjacency dynamics
and compares modular Krylov ranks with the totient expressions at sample sizes.
"""
from math import gcd

PRIMES = (1000003, 1000033)


def full_tree(branching, depth):
    graph = [[]]
    levels = [[0]]
    for _ in range(depth):
        current = []
        for parent in levels[-1]:
            for _ in range(branching):
                child = len(graph)
                graph.append([parent])
                graph[parent].append(child)
                current.append(child)
        levels.append(current)
    return graph, levels


def euler_phi(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))


def distinct_count(depth):
    # Number of distinct adjacency eigenvalues of a complete branching tree
    # of height 'depth'. This is also independently derived in RESULT.md.
    return sum(euler_phi(q) for q in range(2, depth + 3))


def krylov_rank_mod(graph, traps, prime):
    n = len(graph)
    basis = {}
    vectors = []
    for trap in traps:
        vector = [0] * n
        vector[trap] = 1
        vectors.append(vector)

    for _ in range(n):
        for vector in vectors:
            remainder = vector.copy()
            while True:
                pivot = next((j for j, x in enumerate(remainder) if x), None)
                if pivot is None:
                    break
                if pivot not in basis:
                    inverse = pow(remainder[pivot], -1, prime)
                    basis[pivot] = [(x * inverse) % prime for x in remainder]
                    break
                subtract = remainder[pivot]
                other = basis[pivot]
                remainder = [(x - subtract * y) % prime
                             for x, y in zip(remainder, other)]
        if len(basis) == n:
            break
        vectors = [
            [sum(vector[j] for j in neighbors) % prime for neighbors in graph]
            for vector in vectors
        ]
    return len(basis)


def check_case(b, depth):
    graph, levels = full_tree(b, depth)
    leaves = levels[-1]
    n = len(graph)
    assert n == (b ** (depth + 1) - 1) // (b - 1)
    one = distinct_count(depth)
    expected = [one + distinct_count(h - 1) for h in range(1, depth + 1)]
    for prime in PRIMES:
        result_one = krylov_rank_mod(graph, [leaves[0]], prime)
        assert result_one == one, (b, depth, prime, result_one, one)
        for h in range(1, depth + 1):
            # Their lowest common ancestor is exactly depth-h.
            pair = (leaves[0], leaves[b ** (h - 1)])
            result = krylov_rank_mod(graph, pair, prime)
            target = expected[h - 1]
            assert result == target, (b, depth, h, prime, result, target)
    print('PASS b=%d depth=%d N=%d one=%d pair=%s' %
          (b, depth, n, one, expected))


def main():
    # Includes a 121-site, depth-four example and multiple branch factors.
    for b, depths in [(3, range(1, 5)), (4, range(1, 4)),
                      (5, range(1, 3)), (6, range(1, 3))]:
        for depth in depths:
            check_case(b, depth)
    # Test invariance across different representatives at each distance.
    g, levels = full_tree(3, 3)
    for index_a, index_b in [(0, 1), (4, 5), (0, 3), (6, 8),
                             (0, 9), (9, 18), (3, 21)]:
        a, b = levels[-1][index_a], levels[-1][index_b]
        assert a != b
        parents = {0: None}
        for v, neighbors in enumerate(g):
            for w in neighbors:
                if w > v:
                    parents[w] = v
        d = 0
        ancestors = set()
        t = a
        while t is not None:
            ancestors.add(t)
            t = parents[t]
        t = b
        while t not in ancestors:
            t = parents[t]
        lca = t
        while lca != 0:
            d += 1
            lca = parents[lca]
        h = 3 - d
        actual = krylov_rank_mod(g, [a, b], PRIMES[0])
        expected = distinct_count(3) + distinct_count(h - 1)
        assert actual == expected, (index_a, index_b, h, actual, expected)
    print('PASS all additional leaf-placement checks')
    # The branching threshold is essential. On the binary depth-two tree,
    # opposite-principal-branch leaves do not have the required third branch.
    boundary_graph, boundary_levels = full_tree(2, 2)
    boundary_rank = krylov_rank_mod(
        boundary_graph, [boundary_levels[-1][0], boundary_levels[-1][2]],
        PRIMES[0])
    assert boundary_rank == 6, boundary_rank
    assert distinct_count(2) + distinct_count(1) == 8
    print('PASS binary-boundary counterexample: actual rank=6 vs formal extension=8')


if __name__ == '__main__':
    main()
