#!/usr/bin/env python3
import itertools
import math


def stirling2(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + j * dp[i - 1][j]
    return dp[n][k]


def predicted_gamma(m, n):
    assert 1 <= m <= n
    return min(n, 2 * m)


def predicted_count(m, n):
    assert 1 <= m <= n
    if n < 2 * m:
        return math.factorial(m) * stirling2(n, m)
    if n > 2 * m:
        return math.comb(n, 2) ** m
    return (math.factorial(m) * stirling2(2 * m, m)
            + math.comb(2 * m, 2) ** m
            - math.factorial(2 * m) // (2 ** m))


def is_2dom(m, n, chosen):
    chosen = set(chosen)
    for i in range(m):
        for j in range(n):
            if (i, j) in chosen:
                continue
            count = 0
            for jj in range(n):
                if jj != j and (i, jj) in chosen:
                    count += 1
            for ii in range(m):
                if ii != i and (ii, j) in chosen:
                    count += 1
            if count < 2:
                return False
    return True


def exhaustive_case(m, n):
    vertices = [(i, j) for i in range(m) for j in range(n)]
    tested = 0
    for size in range(len(vertices) + 1):
        count = 0
        for tup in itertools.combinations(vertices, size):
            tested += 1
            if is_2dom(m, n, tup):
                count += 1
        if count:
            return size, count, tested
    raise AssertionError('No dominating set found')


def construction(m, n):
    if (m, n) == (1, 1):
        return {(0, 0)}
    if n <= 2 * m:
        # One cell per column, with every row represented because n >= m.
        return {(j % m, j) for j in range(n)}
    # Two cells per row.
    return {(i, j) for i in range(m) for j in (0, 1)}


def main():
    subset_candidates = 0
    exhaustive_cases = 0
    for m in range(1, 5):
        for n in range(m, 5):
            got_gamma, got_count, tested = exhaustive_case(m, n)
            subset_candidates += tested
            exhaustive_cases += 1
            assert got_gamma == predicted_gamma(m, n), (m, n, got_gamma)
            assert got_count == predicted_count(m, n), (m, n, got_count, predicted_count(m, n))

    construction_cases = 0
    for m in range(1, 41):
        for n in range(m, 41):
            D = construction(m, n)
            assert len(D) == predicted_gamma(m, n), (m, n, len(D))
            assert is_2dom(m, n, D), (m, n)
            construction_cases += 1

    print('ALL CHECKS PASSED; '
          f'exhaustive_cases={exhaustive_cases}; '
          f'subset_candidates={subset_candidates}; '
          f'construction_cases={construction_cases}; '
          'exhaustive_range=1<=m<=n<=4; construction_range=1<=m<=n<=40')


if __name__ == '__main__':
    main()
