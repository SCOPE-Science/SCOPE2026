"""Exact finite check of the two-outward-neighbour induction boundary.
This is a finite sanity check of the proof, not an infinite certificate.
"""
from itertools import combinations
from verify_zero_forcing import token_neighbours


def min_gap(v, n):
    s = sorted(v)
    return min(((s[(i + 1) % len(s)] - s[i]) % n) for i in range(len(s)))


def check(n, k):
    tested = 0
    for d in range(2, n // k + 1):
        for S0 in combinations(range(n), k - 2):
            S = set(S0)
            for t in range(n):
                A = S | {t, (t + d) % n}
                if len(A) != k or min_gap(A, n) < d:
                    continue
                B = S | {t, (t + d - 1) % n}
                assert len(B) == k and min_gap(B, n) < d, (n, k, d, S, t)
                expected = {tuple(sorted(A))}
                prev = S | {(t - 1) % n, (t + d - 1) % n}
                if len(prev) == k and min_gap(prev, n) >= d:
                    expected.add(tuple(sorted(prev)))
                actual = {v for v in token_neighbours(tuple(sorted(B)), n)
                          if min_gap(v, n) >= d}
                assert actual == expected, (n, k, d, S, t, actual, expected)
                tested += 1
    return tested


def main():
    total = 0
    for n in range(6, 17):
        for k in range(3, min(n + 1, 6)):
            count = check(n, k)
            total += count
            print(f'N={n} k={k} equations={count}')
    print(f'PASS: {total} local boundary equations')

if __name__ == '__main__':
    main()
