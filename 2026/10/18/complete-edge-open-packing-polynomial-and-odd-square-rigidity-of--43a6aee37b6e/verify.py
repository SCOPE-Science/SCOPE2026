"""Reproduce the edge-open-packing enumerator checks for rook graphs.

Only Python 3 standard-library modules are required.
"""
from collections import Counter
from itertools import combinations
from math import factorial


def enumerator_formula(m, n):
    """Coefficients from the three component species."""
    counts = Counter()
    for h in range(m + 1):
        for v in range(n + 1):
            for e in range(min(m, n) // 2 + 1):
                rows, cols = h + 2 * v + 2 * e, 2 * h + v + 2 * e
                if rows > m or cols > n:
                    continue
                numerator = factorial(m) // factorial(m - rows)
                numerator *= factorial(n) // factorial(n - cols)
                denominator = factorial(h) * factorial(v) * factorial(e) * (2 ** (h + v))
                assert numerator % denominator == 0
                counts[h + v + 2 * e] += numerator // denominator
    return dict(sorted(counts.items()))


def enumerator_direct(m, n):
    """Enumerate feasible edge subsets using only the graph adjacency rule.

    Construct the incompatibility relation by testing for a third edge
    joining the endpoints of each pair of selected edges. Then enumerate
    every clique of the compatibility graph, including the empty set.
    """
    vertices = [(i, j) for i in range(m) for j in range(n)]
    edges = [(u, v) for u, v in combinations(vertices, 2)
             if u[0] == v[0] or u[1] == v[1]]
    compatibility = [0] * len(edges)
    for i, (a, b) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            c, d = edges[j]
            selected = {frozenset((a, b)), frozenset((c, d))}
            forbidden = any(
                (x[0] == y[0] or x[1] == y[1])
                and x != y and frozenset((x, y)) not in selected
                for x in (a, b) for y in (c, d)
            )
            if not forbidden:
                compatibility[i] |= 1 << j
    counts = Counter({0: 1})
    def search(available, size):
        while available:
            bit = available & -available
            index = bit.bit_length() - 1
            available ^= bit
            counts[size + 1] += 1
            search(available & compatibility[index], size + 1)
    search((1 << len(edges)) - 1, 0)
    return dict(sorted(counts.items()))


def extremal_formula(m, n):
    """Return sharp packing size and number of maximum sets, m<=n."""
    if m == n:
        if m % 2 == 0:
            return (m, factorial(m) ** 2 // factorial(m // 2))
        top = (m + 7) * factorial(m) ** 2
        bottom = 8 * factorial((m - 1) // 2)
        assert top % bottom == 0
        return (m - 1, top // bottom)
    count = 0
    for h in range(m % 2, min(m, n - m) + 1, 2):
        e = (m - h) // 2
        numerator = factorial(m) * factorial(n) // factorial(n - m - h)
        denominator = factorial(h) * factorial(e) * (2 ** h)
        assert numerator % denominator == 0
        count += numerator // denominator
    return (m, count)


def main():
    boards = [(2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
              (3, 3), (3, 4), (3, 5), (3, 6),
              (4, 4), (4, 5), (4, 6), (5, 5)]
    total_sets = 0
    for m, n in boards:
        direct = enumerator_direct(m, n)
        formula = enumerator_formula(m, n)
        assert direct == formula, (m, n, direct, formula)
        total_sets += sum(direct.values())
        print(f'board={m}x{n} coefficients={list(formula.items())} OK')
    print(f'direct_checked_boards={len(boards)} total_edge_open_packing_sets={total_sets}')
    param_count = 0
    for m in range(2, 21):
        for n in range(m, 21):
            polynomial = enumerator_formula(m, n)
            degree, leading_coefficient = extremal_formula(m, n)
            assert max(polynomial) == degree
            assert polynomial[degree] == leading_coefficient
            param_count += 1
    print(f'extremal_formula_checked_boards={param_count} OK')
    print('VERIFICATION_OK')

if __name__ == '__main__':
    main()
