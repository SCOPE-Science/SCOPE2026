#!/usr/bin/env python3
"""Standalone verification of an exact Černý subset rendezvous formula.

All states and alphabets are explicitly defined; checks are finite, not a
substitute for the universal proof.
"""
from collections import deque


def prediction(n, mask):
    xs = [i for i in range(n) if mask & (1 << i)]
    if len(xs) == 1:
        return 0
    cycle = [(xs[i] - xs[i - 1]) % n for i in range(len(xs))]
    return min((n - x) % n + n * (n - g - 1) + 1
               for x, g in zip(xs, cycle))


def distance_table(n):
    whole = (1 << n) - 1
    pre = [[] for _ in range(whole + 1)]
    for mask in range(1, whole + 1):
        aa = ((mask << 1) & whole) | (mask >> (n - 1))
        bb = (mask & ~1) | (2 if mask & 1 else 0)
        pre[aa].append(mask)
        pre[bb].append(mask)
    dist = [-1] * (whole + 1)
    queue = deque()
    for k in range(n):
        m = 1 << k
        dist[m] = 0
        queue.append(m)
    while queue:
        dst = queue.popleft()
        for src in pre[dst]:
            if dist[src] == -1:
                dist[src] = dist[dst] + 1
                queue.append(src)
    return dist


def run():
    total = 0
    for n in range(2, 16):
        d = distance_table(n)
        for mask in range(1, 1 << n):
            expected = prediction(n, mask)
            assert d[mask] == expected, (n, mask, d[mask], expected)
            total += 1
        assert d[(1 << n) - 1] == (n - 1) ** 2
    print(f'CERNY_SUBSET_GAP_PASS n=2..15 subsets={total}')


if __name__ == '__main__':
    run()
