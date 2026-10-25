"""Exact finite verification of normal-cone measures for matching-deletion root polytopes.

Uses rank permutations and exact fractions. A forbidden extremal pair admits two
competitors. Reflection symmetry of order-statistic spacings gives probability
one half to either competitor, conditional on every rank permutation.
"""
from fractions import Fraction
from itertools import combinations, permutations
from math import comb, factorial


def verify_case(n, m):
    matching = {frozenset((2*j, 2*j+1)) for j in range(m)}
    edges = {frozenset(e) for e in combinations(range(n), 2) if frozenset(e) not in matching}
    seen = {e: Fraction(0) for e in edges}
    weight = Fraction(1, factorial(n))
    for order in permutations(range(n)):
        low, second_low = order[0], order[1]
        second_high, high = order[-2], order[-1]
        extreme = frozenset((low, high))
        if extreme in edges:
            seen[extreme] += weight
        else:
            pair_a = frozenset((high, second_low))
            pair_b = frozenset((low, second_high))
            assert pair_a in edges and pair_b in edges
            seen[pair_a] += weight / 2
            seen[pair_b] += weight / 2
    for e in edges:
        matched_count = sum(int(x < 2*m) for x in e)
        predicted = Fraction(2*(n-2)+matched_count, n*(n-1)*(n-2))
        assert seen[e] == predicted, (n, m, e, seen[e], predicted)
    assert sum(seen.values()) == 1
    return len(edges), factorial(n)


def verify_symbolic_counts():
    for n in range(4, 301):
        for m in range(n//2+1):
            counts = (comb(n-2*m,2), 2*m*(n-2*m), 2*m*(m-1))
            assert sum(counts) == comb(n,2)-m
            mass = sum(Fraction(counts[j]*(2*(n-2)+j), n*(n-1)*(n-2)) for j in range(3))
            assert mass == 1, (n,m)


if __name__ == '__main__':
    verify_symbolic_counts()
    total_cases = total_permutations = total_edges = 0
    for n in range(4, 9):
        for m in range(n//2+1):
            edge_count, perm_count = verify_case(n, m)
            total_cases += 1
            total_permutations += perm_count
            total_edges += edge_count
    print(f'EXACT_ANGLE_PASS cases={total_cases} permutations={total_permutations} '
          f'edge_checks={total_edges} symbolic_n_max=300')
