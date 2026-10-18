"""Exact finite checks for the Ferrers-block congruence-profile formula.

Usage: python verify_congruence.py
No external dependencies.
"""
from collections import Counter
from itertools import combinations_with_replacement, product
from math import comb


def endpoint_states(s, t):
    yield (0, 0, 1)
    for u in range(1, s + 1):
        for v in range(1, t + 1):
            yield (u, v, comb(u + v - 2, u - 1))


def formula_profile(lengths):
    k = len(lengths)
    choices = [list(endpoint_states(lengths[i], lengths[j]))
               for i in range(k) for j in range(k)]
    boundaries = [0]
    for n in lengths:
        boundaries.append(boundaries[-1] + n)
    result = Counter()
    for parameters in product(*choices):
        weight = 1
        supports = []
        outgoing = [0] * k
        incoming = [0] * k
        for index, (u, v, multiplicity) in enumerate(parameters):
            i, j = divmod(index, k)
            weight *= multiplicity
            outgoing[i] = max(outgoing[i], u)
            incoming[j] = max(incoming[j], v)
            if u:
                supports.append(set(range(boundaries[i], boundaries[i] + u))
                                | set(range(boundaries[j] + lengths[j] - v,
                                            boundaries[j] + lengths[j])))
        isolated = sum(max(0, n - outgoing[i] - incoming[i])
                       for i, n in enumerate(lengths))
        parent = list(range(len(supports)))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for i in range(len(supports)):
            for j in range(i):
                if supports[i] & supports[j]:
                    parent[find(i)] = find(j)
        blocks = len({find(i) for i in range(len(supports))})
        result[isolated + blocks] += weight
    return result


def direct_relation_profile(lengths):
    """Enumerate actual admissible relations, independently of endpoint weights."""
    k = len(lengths)
    boundaries = [0]
    for n in lengths:
        boundaries.append(boundaries[-1] + n)
    N = boundaries[-1]
    choices = []
    for i in range(k):
        for j in range(k):
            options = []
            for thresholds in combinations_with_replacement(range(lengths[j] + 1),
                                                             lengths[i]):
                edges = tuple((boundaries[i] + row, boundaries[j] + col)
                              for row, first in enumerate(thresholds)
                              for col in range(first, lengths[j]))
                options.append(edges)
            choices.append(options)
    result = Counter()
    for groups in product(*choices):
        parent = list(range(N))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for edges in groups:
            for x, y in edges:
                parent[find(x)] = find(y)
        result[len({find(x) for x in range(N)})] += 1
    return result


def raw_relation_profile(lengths):
    """Brute-force *all* binary relations and filter by the frame axioms."""
    N = sum(lengths)
    chain = []
    height = []
    for i, n in enumerate(lengths):
        chain.extend([i] * n)
        height.extend(range(n))
    less = [[chain[x] == chain[y] and height[x] <= height[y]
             for y in range(N)] for x in range(N)]
    implied = [(i, j, a, b) for i in range(N) for j in range(N)
               for a in range(N) for b in range(N)
               if less[a][i] and less[j][b]]
    profile = Counter()
    for mask in range(1 << (N * N)):
        if any((mask & (1 << (i * N + j))) and
               not (mask & (1 << (a * N + b)))
               for i, j, a, b in implied):
            continue
        parent = list(range(N))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        for i in range(N):
            for j in range(N):
                if mask & (1 << (i * N + j)):
                    parent[find(i)] = find(j)
        profile[len({find(i) for i in range(N)})] += 1
    return profile


def verify_axioms(lengths):
    """Independently evaluate the eight unary/binary WHB axiom schemes."""
    N = sum(lengths)
    chain = []
    height = []
    for i, n in enumerate(lengths):
        chain.extend([i] * n)
        height.extend(range(n))
    less = [[chain[x] == chain[y] and height[x] <= height[y]
             for y in range(N)] for x in range(N)]
    upsets = [u for u in range(1 << N)
              if all(not (u & (1 << x)) or not less[x][y] or (u & (1 << y))
                     for x in range(N) for y in range(N))]
    full = (1 << N) - 1
    options = []
    starts = [sum(lengths[:i]) for i in range(len(lengths))]
    for i, s in enumerate(lengths):
        for j, t in enumerate(lengths):
            options.append([tuple((starts[i] + row, starts[j] + col)
                                  for row, threshold in enumerate(ts)
                                  for col in range(threshold, t))
                            for ts in combinations_with_replacement(range(t + 1), s)])
    checked = 0
    for groups in product(*options):
        R = set().union(*(set(g) for g in groups))
        arrow = {}
        diff = {}
        for u in upsets:
            for v in upsets:
                a = sum((1 << x) for x in range(N)
                        if all(not ((x, y) in R and (u & (1 << y)) and not (v & (1 << y)))
                               for y in range(N)))
                d = sum((1 << x) for x in range(N)
                        if any((y, x) in R and (u & (1 << y)) and not (v & (1 << y))
                               for y in range(N)))
                assert a in upsets and d in upsets
                arrow[(u, v)] = a
                diff[(u, v)] = d
        for a in upsets:
            assert arrow[a, a] == full and diff[a, a] == 0
            for b in upsets:
                assert (a & diff[arrow[a, b], 0]) & ~b == 0
                assert a & ~(b | arrow[full, diff[a, b]]) == 0
                for c in upsets:
                    assert arrow[a, b & c] == (arrow[a, b] & arrow[a, c])
                    assert arrow[a | b, c] == (arrow[a, c] & arrow[b, c])
                    assert (arrow[a, b] & arrow[b, c]) & ~arrow[a, c] == 0
                    assert diff[a | b, c] == (diff[a, c] | diff[b, c])
                    assert diff[a, b & c] == (diff[a, b] | diff[a, c])
                    assert diff[a, c] & ~(diff[a, b] | diff[b, c]) == 0
        checked += 1
    return checked


def main():
    expected = {
        (1, 1): {1: 12, 2: 4},
        (1, 2): {1: 92, 2: 14, 3: 2},
        (2, 2): {1: 1213, 2: 70, 3: 12, 4: 1},
        (2, 3): {1: 11632, 2: 309, 3: 50, 4: 8, 5: 1},
        (3, 3): {1: 157938, 2: 1730, 3: 281, 4: 46, 5: 4, 6: 1},
    }
    for sizes, want in expected.items():
        got = formula_profile(sizes)
        assert dict(got) == want, (sizes, got)
        other = direct_relation_profile(sizes)
        assert got == other, (sizes, got, other)
        expected_total = 1
        for s in sizes:
            for t in sizes:
                expected_total *= comb(s + t, s)
        assert sum(got.values()) == expected_total
        print('PROFILE', sizes, sorted(got.items()), 'TOTAL', expected_total)
    for sizes in ((1, 1), (1, 2), (2, 2)):
        assert raw_relation_profile(sizes) == formula_profile(sizes)
        print('RAW_RELATIONS', sizes, 'OK')
    for sizes in ((1, 1), (1, 2)):
        count = verify_axioms(sizes)
        assert count == sum(formula_profile(sizes).values())
        print('AXIOMS', sizes, count, 'OK')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()
