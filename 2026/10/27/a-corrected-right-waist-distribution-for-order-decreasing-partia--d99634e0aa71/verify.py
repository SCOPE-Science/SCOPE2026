#!/usr/bin/env python3
"""Independent finite checks for right-waist counts of decreasing partial injections."""
from collections import defaultdict
from itertools import combinations, permutations
from math import comb, factorial


def stirling(n, k):
    if k < 0 or k > n:
        return 0
    rows = [[1]]
    for m in range(1, n + 1):
        prev = rows[-1]
        rows.append([(prev[j - 1] if 1 <= j <= m else 0)
                     + (j * prev[j] if j < m else 0)
                     for j in range(m + 1)])
    return rows[n][k]


def fall(a, s):
    out = 1
    for i in range(s):
        out *= a-i
    return out


def formula(n, k):
    if k == 0:
        return 1
    if not 1 <= k <= n:
        return 0
    m = n - k
    return (m+1) * sum(
        stirling(k, k-r) * sum(
            comb(m, s) * fall(k-1-r, s)
            for s in range(min(m, k-1-r)+1))
        for r in range(k))


def exhaustive(n):
    counts = [0]*(n+1)
    counts[0] = 1
    for rank in range(1, n+1):
        for inputs in combinations(range(1, n+1), rank):
            for outputs in permutations(range(1, n+1), rank):
                if all(y <= x for x, y in zip(inputs, outputs)):
                    counts[max(outputs)] += 1
    return counts


def dynamic(n):
    # Independently sweep all possible inputs; state is exact used-image subset.
    states = {0: 1}
    for x in range(1, n+1):
        nxt = defaultdict(int)
        for used, ways in states.items():
            nxt[used] += ways  # omit input x
            for y in range(1, x+1):
                bit = 1 << (y-1)
                if not used & bit:
                    nxt[used | bit] += ways  # injective order-decreasing placement
        states = nxt
    counts = [0]*(n+1)
    for mask, ways in states.items():
        counts[mask.bit_length()] += ways
    return counts


def bell(n):
    return sum(stirling(n,j) for j in range(n+1))


def main():
    all_rows = {}
    for n in range(1, 8):
        actual = exhaustive(n)
        assert actual == [formula(n,k) for k in range(n+1)], (n, actual)
        assert actual == dynamic(n), (n, actual)
        assert sum(actual) == bell(n+1)
        all_rows[n] = actual
    assert all_rows[5] == [1,5,20,51,74,52]
    assert all_rows[4] == [1,4,12,20,15]
    assert formula(5,3) == 51 != comb(5,3)*bell(3)
    for n in range(3,101):
        assert formula(n,3) == (n-2)*(n*n-2*n+2)
    for n in range(8,17):
        assert dynamic(n) == [formula(n,k) for k in range(n+1)]
        assert sum(dynamic(n)) == bell(n+1)
    for n in range(1,5):
        for k in range(1,n+1):
            assert formula(n,k) == comb(n,k)*bell(k)
    for n in range(5,101):
        assert formula(n,3) - comb(n,3)*bell(3) == comb(n-2,3)
    print('EXHAUSTIVE_ROWS', all_rows)
    print('VERIFY_OK_UMAR_RIGHT_WAIST_CORRECTION')

if __name__ == '__main__':
    main()
