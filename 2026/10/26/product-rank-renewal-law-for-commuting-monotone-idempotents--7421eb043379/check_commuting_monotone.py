"""Independent finite enumeration for the commuting retractions theorem.

Run with Python 3; no third-party packages are required.
"""
from itertools import combinations_with_replacement


def predicted(max_n):
    f = [0] * (max_n + 1)
    f[0] = 1
    if max_n: f[1] = 2
    for i in range(2, max_n + 1):
        f[i] = 3 * f[i - 1] - f[i - 2]
    d = [2 * a - 1 for a in f]
    block = [0] * (max_n + 1)
    for length in range(1, max_n + 1):
        block[length] = sum(d[a] * d[length - 1 - a] for a in range(length))
    rank = [[0] * (max_n + 1) for _ in range(max_n + 1)]
    rank[0][0] = 1
    for n in range(1, max_n + 1):
        for k in range(1, n + 1):
            rank[n][k] = sum(block[length] * rank[n - length][k - 1]
                             for length in range(1, n + 1))
    return rank, block


def check(max_n=9):
    target, block = predicted(max_n)
    pairs_total = 0
    for n in range(1, max_n + 1):
        maps = [f for f in combinations_with_replacement(range(n), n)
                if all(f[f[i]] == f[i] for i in range(n))]
        actual = [0] * (n + 1)
        for e in maps:
            for f in maps:
                if all(e[f[i]] == f[e[i]] for i in range(n)):
                    common = len({e[f[i]] for i in range(n)})
                    actual[common] += 1
        assert actual == target[n][:n + 1], (n, actual, target[n])
        pairs_total += len(maps) ** 2
        print('PASS', n, 'idempotents', len(maps), 'commuting', sum(actual),
              'product-rank-profile', actual[1:])
    print('ALL_MONOTONE_IDEMPOTENT_RANK_TESTS_PASSED', max_n, pairs_total)


if __name__ == '__main__':
    check()
