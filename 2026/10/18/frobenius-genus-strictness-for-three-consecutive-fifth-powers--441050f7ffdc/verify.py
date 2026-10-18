#!/usr/bin/env python3
"""Finite independent checks for a fifth-power Frobenius/genus classification."""
from heapq import heappush, heappop

def apery_fg(n):
    gens = [(n - 1) ** 5, n ** 5, (n + 1) ** 5]
    m = gens[0]
    dist = [None] * m
    dist[0] = 0
    heap = [(0, 0)]
    while heap:
        d, r = heappop(heap)
        if dist[r] != d:
            continue
        for v in gens[1:]:
            nxt = (r + v) % m
            nd = d + v
            if dist[nxt] is None or nd < dist[nxt]:
                dist[nxt] = nd
                heappush(heap, (nd, nxt))
    assert all(v is not None for v in dist)
    F = max(dist) - m
    twice_g = (2 * sum(dist) - m * (m - 1)) // m
    assert (2 * sum(dist) - m * (m - 1)) % m == 0
    return F, twice_g

def odd_candidates(m):
    target = (2 * m + 1) ** 5
    right = (m + 1) ** 5
    return [B for B in range(target // right + 1)
            if (target - B * right) % (m ** 5) == 0]

def even_candidates(n):
    target = (n + 1) ** 5
    left = (n - 1) ** 5
    return [A for A in range(target // left + 1)
            if (target - A * left) % (n ** 5) == 0]

def main():
    assert odd_candidates(1)
    for m in range(2, 1025):
        assert odd_candidates(m) == [], (m, odd_candidates(m))
    for n in range(4, 1025, 2):
        assert even_candidates(n) == [], (n, even_candidates(n))
    assert ((11 ** 5 - 6 ** 5) % 5 ** 5) == 150
    assert ((9 ** 5 - 5 * 5 ** 5) % 4 ** 5) == 416
    assert [((7 ** 5 - b * 4 ** 5) % 3 ** 5) for b in (7, 16)] == [162, 180]
    assert [((5 ** 5 - a * 3 ** 5) % 4 ** 5) for a in (3, 7, 11)] == [348, 400, 452]
    assert ((7 ** 5 - 5 * 5 ** 5) % 6 ** 5) == 1182
    F, twice_g = apery_fg(3)
    assert (F, twice_g) == (7501, 7502)
    for n in range(4, 12):
        F, twice_g = apery_fg(n)
        assert twice_g > F + 1, (n, F, twice_g)
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
