#!/usr/bin/env python3
"""Standalone finite checks for three-patch spectral-capacity sampling."""
from itertools import product, combinations, permutations
from collections import Counter
from math import comb, sqrt


def prufer_tree(n, code):
    degree = [1] * n
    for v in code:
        degree[v] += 1
    edges = set()
    for v in code:
        leaf = min(i for i in range(n) if degree[i] == 1)
        edges.add(tuple(sorted((leaf, v))))
        degree[leaf] -= 1
        degree[v] -= 1
    a, b = [i for i, d in enumerate(degree) if d == 1]
    edges.add(tuple(sorted((a, b))))
    return edges


def determinant_coefficients_of_xI_minus_A(vertices, edges):
    """A symbolic polynomial determinant, coefficients constant through cubic."""
    m = len(vertices)
    coeffs = [0] * (m + 1)
    for perm in permutations(range(m)):
        inv = sum(perm[i] > perm[j] for i in range(m) for j in range(i + 1, m))
        poly = [1]
        for i, j in enumerate(perm):
            a = int(tuple(sorted((vertices[i], vertices[j]))) in edges and i != j)
            factor = [0, 1] if i == j else [-a]
            nxt = [0] * (len(poly) + len(factor) - 1)
            for p, xp in enumerate(poly):
                for q, yq in enumerate(factor):
                    nxt[p + q] += xp * yq
            poly = nxt
        for p, val in enumerate(poly):
            coeffs[p] += (-1 if inv % 2 else 1) * val
    return tuple(coeffs)


def main():
    trees = 0
    triples = 0
    spectral_determinants = 0
    for n in range(3, 8):
        scores = {}
        for code in product(range(n), repeat=n - 2):
            E = prufer_tree(n, code)
            deg = [0] * n
            for a, b in E:
                deg[a] += 1
                deg[b] += 1
            W = sum(comb(d, 2) for d in deg)
            actual = Counter()
            for V in combinations(range(n), 3):
                e = sum(a in V and b in V for a, b in E)
                assert e in (0, 1, 2)
                actual[e] += 1
                triples += 1
                if trees < 100 or (trees + triples) % 337 == 0:
                    assert determinant_coefficients_of_xI_minus_A(V, E) == (0, -e, 0, 1)
                    spectral_determinants += 1
            assert actual[2] == W
            assert actual[1] == (n - 1) * (n - 2) - 2 * W
            assert actual[0] == comb(n, 3) - (n - 1) * (n - 2) + W
            assert sum(actual.values()) == comb(n, 3)
            # Every tree has exactly n-1 edges; two-site capacity is
            # topology-independent and equals one with probability 2/n.
            pair_capacities = sum(tuple(sorted(pair)) in E for pair in combinations(range(n), 2))
            assert pair_capacities == n - 1
            if n >= 4:
                assert n - 2 <= W <= comb(n - 1, 2)
                if W == n - 2:
                    assert max(deg) == 2
                if W == comb(n - 1, 2):
                    assert max(deg) == n - 1
                if n not in scores:
                    scores[n] = [99999, -1]
                scores[n][0] = min(scores[n][0], W)
                scores[n][1] = max(scores[n][1], W)
            trees += 1
        if n >= 4:
            assert scores[n] == [n - 2, comb(n - 1, 2)]
        C = comb(n, 3)
        low_p = lambda w: ((n - 1) * (n - 2) - w) / C
        high_p = lambda w: w / C
        if n >= 4:
            assert low_p(n - 2) > low_p(comb(n - 1, 2))
            assert high_p(n - 2) < high_p(comb(n - 1, 2))
    assert trees == sum(n**(n-2) for n in range(3, 8))
    print('VERIFY_OK', 'labeled_trees=' + str(trees), 'three_patch_samples=' + str(triples),
          'symbolic_charpoly_checks=' + str(spectral_determinants))


if __name__ == '__main__':
    main()
