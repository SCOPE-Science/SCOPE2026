#!/usr/bin/env python3
"""Finite exhaustive bipartiteness checks for random matching-glued cubes.

Requires Python 3.10+ standard library only. These finite checks do not prove
large-dimension asymptotics; those follow from the mathematical recurrence.
"""
from fractions import Fraction
from itertools import permutations
from math import comb, factorial, lgamma, log, pi


def glue(edges_left, edges_right, m, perm):
    assert sorted(perm) == list(range(m))
    return (list(edges_left) + [(a + m, b + m) for a, b in edges_right]
            + [(i, m + perm[i]) for i in range(m)])


def two_color(num_vertices, edges):
    neighbors = [[] for _ in range(num_vertices)]
    for a, b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    colors = [-1] * num_vertices
    for root in range(num_vertices):
        if colors[root] != -1:
            continue
        colors[root] = 0
        queue = [root]
        for vertex in queue:
            for v in neighbors[vertex]:
                if colors[v] == -1:
                    colors[v] = colors[vertex] ^ 1
                    queue.append(v)
                elif colors[v] == colors[vertex]:
                    return None
    return colors


def trial_probability(n):
    if n == 1:
        return Fraction(1)
    m = 2 ** (n - 1)
    return Fraction(2, comb(m, m // 2))


def exact_probabilities(max_n):
    ind = dup = Fraction(1)
    result = [(1, ind, dup)]
    for n in range(2, max_n + 1):
        p = trial_probability(n)
        ind = ind * ind * p
        dup = dup * p
        result.append((n, ind, dup))
    return result


def log_binomial(m):
    return lgamma(m + 1) - 2 * lgamma(m // 2 + 1)


def run():
    c4 = [(0, 1), (0, 2), (1, 3), (2, 3)]
    perms4 = list(permutations(range(4)))
    bip3 = []
    for q in perms4:
        edges = glue(c4, c4, 4, q)
        assert len(edges) == 12
        assert len(set(tuple(sorted(e)) for e in edges)) == 12
        assert (two_color(8, edges) is not None) == (
            all((i.bit_count() % 2) == (q[i].bit_count() % 2) for i in range(4)) or
            all((i.bit_count() % 2) != (q[i].bit_count() % 2) for i in range(4)))
        if two_color(8, edges) is not None:
            bip3.append((q, edges))
    assert len(bip3) == 8, len(bip3)
    assert Fraction(len(bip3), factorial(4)) == trial_probability(3)
    assert trial_probability(2) == 1
    assert trial_probability(4) == Fraction(1, 35)
    assert trial_probability(5) == Fraction(1, 6435)

    # Exhaust every matching of two equal but independently sampleable
    # bipartite eight-vertex child graphs. Exactly 2(4!)^2 matchings work.
    for el, er in [(bip3[0][1], bip3[1][1]),
                   (bip3[2][1], bip3[2][1])]:
        working = sum(two_color(16, glue(el, er, 8, p)) is not None
                      for p in permutations(range(8)))
        assert working == 2 * factorial(4)**2 == 1152
        assert Fraction(working, factorial(8)) == trial_probability(4)
    nonbip = next(glue(c4, c4, 4, q) for q in perms4
                  if two_color(8, glue(c4, c4, 4, q)) is None)
    assert two_color(16, glue(nonbip, bip3[0][1], 8, tuple(range(8)))) is None

    probs = exact_probabilities(6)
    assert probs[2][1] == probs[2][2] == Fraction(1, 3)
    assert probs[3][1] == Fraction(1, 315)
    assert probs[3][2] == Fraction(1, 105)
    for n, independent, duplicate in probs:
        p_product_ind = Fraction(1)
        p_product_dup = Fraction(1)
        for k in range(2, n + 1):
            p_product_ind *= trial_probability(k) ** (2**(n-k))
            p_product_dup *= trial_probability(k)
        assert independent == p_product_ind
        assert duplicate == p_product_dup

    # Compare exact factorial-log sums with the asymptotic scales.
    for n in range(6, 15):
        ell = {k: log_binomial(2 ** (k - 1)) - log(2)
               for k in range(2, n + 1)}
        Li = sum(2 ** (n-k) * ell[k] for k in ell)
        Ld = sum(ell.values())
        assert Li > 0 and Ld > 0
        # Duplication expansion has a uniformly bounded remainder.
        main_dup = ((2**n) * log(2)
                    - (n*n/4) * log(2)
                    - n*(log(2)/4 + log(pi)/2))
        assert abs(Ld - main_dup) < 2
        # A convergent numerical constant gives an O(n) independent remainder.
        gamma_n = sum(2 ** (-k) *
                      (ell[k] - 2**(k-1) * log(2)) for k in ell)
        assert abs(Li - 2**n*((n-1)*log(2)/2 + gamma_n)) < 1e-7
    print('PASS: 24 n=3 matchings, 80,640 n=4 matchings,')
    print('      exact rational recurrences n<=6 and logarithmic tests n<=14.')


if __name__ == '__main__':
    run()
