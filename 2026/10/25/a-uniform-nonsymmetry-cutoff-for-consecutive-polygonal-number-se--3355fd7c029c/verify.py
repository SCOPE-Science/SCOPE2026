"""Bounded arithmetic and Apéry checks for the nontriangular cutoff."""

from heapq import heappop, heappush
from math import gcd, inf


def polygonal(m, n):
    return n * ((m - 2) * n - m + 4) // 2


def apery_invariants(a, b, c):
    distances = [inf] * a
    distances[0] = 0
    queue = [(0, 0)]
    while queue:
        weight, residue = heappop(queue)
        if weight != distances[residue]:
            continue
        for step in (b, c):
            target = (residue + step) % a
            candidate = weight + step
            if candidate < distances[target]:
                distances[target] = candidate
                heappush(queue, (candidate, target))
    assert all(d != inf for d in distances)
    return max(distances) - a, sum((d - r) // a for r, d in enumerate(distances))


def main():
    checked = 0
    for m in range(4, 18):
        t = m - 2
        M = m * (3 * m - 8)
        for n in (*range(2, 45), 12 * M + 1, 12 * M + 2, 12 * M + 17):
            a, b, c = (polygonal(m, n + j) for j in range(3))
            u, e = b - a, c - a
            assert gcd(gcd(a, b), c) == 1 and gcd(u, e) == 1
            assert u == t * n + 1 and e == 2 * u + t
            assert 2 * t * a - (t - 1) == u * (t * n - t + 1)
            assert 8 * t * a - M == e * (2 * t * n - 3 * t + 2)
            assert (t - 1) % gcd(a, b) == (t - 1) % gcd(b, c) == 0
            assert M % gcd(a, c) == 0
            if n > 12 * M:
                assert a < b < c < 2 * a and e * M < a and e > M
            checked += 1
    assert checked == 644

    cases = {193: (17990103, 9011712), 194: (14677843, 7343724)}
    for n, expected in cases.items():
        assert n > 12 * 4 * (3 * 4 - 8)
        F, g = apery_invariants(*(polygonal(4, n + j) for j in range(3)))
        assert (F, g) == expected and 2 * g != F + 1
    print(f"VERIFY_OK: {checked} arithmetic cases, {len(cases)} above-cutoff Apéry checks")


if __name__ == "__main__":
    main()
