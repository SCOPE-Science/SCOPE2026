"""Standalone exact finite checks for incidence-poset one-types."""
from itertools import combinations, product
from math import comb


def edges_universe(n):
    return list(combinations(range(n), 2))


def incidence_count(n, edges):
    e = [tuple(sorted(x)) for x in edges]
    deg = [sum(v in a for a in e) for v in range(n)]
    z = sum(2 ** sum(((a >> u) & 1) and ((a >> v) & 1)
                     for u, v in e) for a in range(1 << n))
    return 2 * z - 1 + sum(2 ** d - 1 for d in deg) + len(e)


def brute_types(n, edges):
    """Independent 3-state enumeration of all actual one-point extensions."""
    edges = list(edges)
    k = n + len(edges)
    comparabilities = [(v, n + i) for i, e in enumerate(edges) for v in e]
    total = 0
    # status is 0: parameter below new point; 1: incomparable; 2: above
    for relation in product(range(3), repeat=k):
        lower = [p for p in range(k) if relation[p] == 0]
        upper = [p for p in range(k) if relation[p] == 2]
        is_below = set(comparabilities)
        # Any two old points forced to compare by the insertion must
        # already have been comparable in the named induced parameter poset.
        if any((p, q) not in is_below for p in lower for q in upper):
            continue
        # Old order must be maintained by transitivity along either new relation.
        if any(relation[p] > relation[q] for p, q in comparabilities):
            continue
        total += 1
    return total


def higher_difference(n, E, F):
    """Alternating finite difference in the selected missing edges."""
    ans = 0
    for a in range(1 << len(F)):
        select = {F[j] for j in range(len(F)) if (a >> j) & 1}
        ans += (-1) ** (len(F) - len(select)) * incidence_count(n, E | select)
    return ans


def derivative_formula(n, E, F):
    degree = {u: sum(u in e for e in E) for u in range(n)}
    support = set(v for e in F for v in e)
    z = sum(2 ** sum(u in A and v in A for u, v in E)
            for s in range(1 << (n - len(support)))
            for A in [support | {v for j, v in enumerate(x for x in range(n) if x not in support) if (s >> j) & 1}])
    shared = sum(2 ** degree[v] for v in range(n) if all(v in f for f in F))
    return 2 * z + shared + (len(F) == 1)


def lucas_even(n):
    a, b = 2, 1
    for _ in range(2 * n):
        a, b = b, a + b
    return a


def run():
    configs = 0
    for n in range(5):
        U = edges_universe(n)
        for bits in range(1 << len(U)):
            E = {U[i] for i in range(len(U)) if (bits >> i) & 1}
            got = incidence_count(n, E)
            observed = brute_types(n, E)
            assert got == observed, (n, E, got, observed)
            configs += 1
    print('DIRECT_ONE_POINT_ENUMERATION', configs, 'graph configurations', 'PASS')

    checks = 0
    for n in range(2, 6):
        U = edges_universe(n)
        # Test all input graphs for small n; a representative collection for n=5.
        cases = range(1 << len(U)) if n < 5 else [0, 1, 3, 17, 75, 231, 512, 1023]
        for bits in cases:
            E = {U[i] for i in range(len(U)) if (bits >> i) & 1}
            missing = [e for e in U if e not in E]
            for r in range(1, min(3, len(missing)) + 1):
                for F in combinations(missing, r):
                    got = higher_difference(n, E, F)
                    expected = derivative_formula(n, E, F)
                    assert got == expected and got > 0, (n, E, F, got, expected)
                    checks += 1
    print('MIXED_FINITE_DIFFERENCES', checks, 'exact identities', 'PASS')
    for n in range(3, 13):
        E = {(i, (i + 1) % n) for i in range(n)}
        assert incidence_count(n, E) == 2 * lucas_even(n) + 4 * n - 1
    print('CROWN_LUCAS_LAW', 10, 'cycle lengths', 'PASS')
    print('ALL_TESTS_PASS')


if __name__ == '__main__':
    run()
