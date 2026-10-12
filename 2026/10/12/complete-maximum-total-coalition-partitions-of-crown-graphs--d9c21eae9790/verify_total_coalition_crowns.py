"""Independent bounded verification of extremal total-coalition partitions of crown graphs.

Python 3 standard library only. Enumerates restricted growth strings (unlabeled set partitions)
and separately compares the total-domination criterion to graph adjacency.
"""
from collections import Counter
from itertools import combinations
from math import comb


def total_dominating(adj, selected):
    return all(adj[v] & selected for v in range(len(adj)))


def crown_adj(n):
    return [set(n + j for j in range(n) if j != i) for i in range(n)] + [
        set(j for j in range(n) if j != i) for i in range(n)
    ]


def tds_criterion(n, selected):
    a = sum(v < n for v in selected)
    b = len(selected) - a
    return a >= 2 and b >= 2


def partitions(N, K=None):
    """All set partitions, or precisely K-block partitions, via restricted growth strings."""
    codes = [0] * N

    def rec(i, k):
        if K is not None and (k > K or k + N - i < K):
            return
        if i == N:
            if K is None or k == K:
                yield tuple(codes)
            return
        for j in range(k + (K is None or k < K)):
            codes[i] = j
            yield from rec(i + 1, max(k, j + 1))

    yield from rec(1, 1)


def good_partition(n, codes):
    k = max(codes) + 1
    a = [0] * k
    b = [0] * k
    for i in range(n):
        a[codes[i]] += 1
    for i in range(n, 2 * n):
        b[codes[i]] += 1
    if any(a[i] >= 2 and b[i] >= 2 for i in range(k)):
        return False, ()
    if any(not any(j != i and a[i] + a[j] >= 2 and b[i] + b[j] >= 2
                   for j in range(k)) for i in range(k)):
        return False, ()
    return True, tuple(sorted(zip(a, b)))


def expected_shape(n):
    return tuple(sorted([(2, 1), (1, 2)] + [(1, 0)] * (n - 3) + [(0, 1)] * (n - 3)))


def expected_count(n):
    return comb(n, 2) * n * (n - 2) * comb(n - 1, 2)


def direct_total_domination_tests():
    tested = 0
    for n in range(3, 8):
        adj = crown_adj(n)
        for mask in range(1 << (2 * n)):
            selected = {v for v in range(2 * n) if (mask >> v) & 1}
            assert total_dominating(adj, selected) == tds_criterion(n, selected)
            tested += 1
    return tested


def all_partitions_for_five():
    n = 5
    tested = 0
    maximum = 0
    optimum_count = 0
    for p in partitions(2 * n):
        tested += 1
        good, shape = good_partition(n, p)
        if not good:
            continue
        k = max(p) + 1
        if k > maximum:
            maximum = k
            optimum_count = 1
        elif k == maximum:
            optimum_count += 1
    assert maximum == 2 * n - 4
    assert optimum_count == expected_count(n)
    return tested, maximum, optimum_count


def fixed_extremal_partition_tests(n):
    k = 2 * n - 4
    tested = count = 0
    for p in partitions(2 * n, k):
        tested += 1
        good, shape = good_partition(n, p)
        if not good:
            continue
        assert shape == expected_shape(n), (n, shape)
        a = [0] * k
        b = [0] * k
        for v, block in enumerate(p):
            if v < n:
                a[block] += 1
            else:
                b[block] += 1
        hubs = [i for i in range(k) if a[i] + b[i] == 3]
        assert len(hubs) == 2
        partners = [set() for _ in range(k)]
        for i in range(k):
            for j in range(i + 1, k):
                if a[i] + a[j] >= 2 and b[i] + b[j] >= 2:
                    partners[i].add(j)
                    partners[j].add(i)
        assert hubs[1] in partners[hubs[0]]
        assert all(len(partners[i]) == (n - 2 if i in hubs else 1)
                   for i in range(k))
        count += 1
    assert count == expected_count(n), (n, count, expected_count(n))
    return tested, count


if __name__ == '__main__':
    checked = direct_total_domination_tests()
    print('TOTAL_DOMINATION_GRAPH_ADJACENCY_SUBSETS:', checked)
    tested, maximum, count = all_partitions_for_five()
    print('N5_ALL_PARTITIONS:', tested, 'MAXIMUM:', maximum, 'COUNT:', count)
    for n in (5, 6, 7):
        tested, count = fixed_extremal_partition_tests(n)
        print('EXTREMAL_N:', n, 'PARTITIONS_TESTED:', tested,
              'MINIMAL_SHAPE_COUNT:', count, 'EXPECTED:', expected_count(n))
    print('VERIFICATION_OK')
