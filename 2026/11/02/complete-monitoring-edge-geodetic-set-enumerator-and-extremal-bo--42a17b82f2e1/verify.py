"""Independent finite checks for monitoring edge-geodetic sets on cycles.

Usage: python3 verify.py [maximum_cycle_order]
Standard-library only. All checks use the original distance-after-edge-deletion
condition rather than the circular-gap criterion used in the proof.
"""
from collections import deque
from math import comb
import sys


def all_distances(n, deleted_edge=None):
    adj = [[] for _ in range(n)]
    for i in range(n):
        if i == deleted_edge:
            continue
        j = (i + 1) % n
        adj[i].append(j)
        adj[j].append(i)
    distance = []
    for s in range(n):
        ds = [n + 1] * n
        ds[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if ds[v] > ds[u] + 1:
                    ds[v] = ds[u] + 1
                    q.append(v)
        distance.append(ds)
    return distance


def exact_sets(n):
    base = all_distances(n)
    monitors = []
    for e in range(n):
        disrupted = all_distances(n, e)
        monitors.append([
            (1 << u) | (1 << v)
            for u in range(n) for v in range(u + 1, n)
            if disrupted[u][v] > base[u][v]
        ])
    return [all(any((s & p) == p for p in per_edge) for per_edge in monitors)
            for s in range(1 << n)]


def expected_count(n, k):
    if not k:
        return 0
    m = n // 2
    return comb(n, k) - n * (comb(m, k - 1) if 0 <= k - 1 <= m else 0) + (n // 2 if n % 2 == 0 and k == 2 else 0)


def run(max_n=13):
    assert max_n >= 4
    for n in range(3, max_n + 1):
        good = exact_sets(n)
        counts = [sum(good[s] for s in range(1 << n) if s.bit_count() == k)
                  for k in range(n + 1)]
        expect = [expected_count(n, k) for k in range(n + 1)]
        assert counts == expect, (n, counts, expect)
        minimal = [s for s in range(1 << n) if good[s] and all(
            not good[s & ~(1 << v)] for v in range(n) if s & (1 << v))]
        maximal_bad = [s for s in range(1 << n) if not good[s] and all(
            good[s | (1 << v)] for v in range(n) if not s & (1 << v))]
        m = n // 2
        expected_min3 = ((n * m * (m + 1)) // 6 if n % 2 else
                         (m * (m - 1) * (m - 2)) // 3)
        expected_min4 = (comb(m, 2) if n % 2 == 0 else 0)
        assert len([s for s in minimal if s.bit_count() == 3]) == expected_min3
        assert len([s for s in minimal if s.bit_count() == 4]) == expected_min4
        assert all(s.bit_count() in (3, 4) for s in minimal)
        if n % 2 == 0:
            for s in minimal:
                if s.bit_count() == 4:
                    assert all((s >> ((v + m) % n)) & 1 for v in range(n) if (s >> v) & 1)
        expected_bad = {
            sum(1 << ((i + j) % n) for j in range(m + 1))
            for i in range(n)
        }
        assert set(maximal_bad) == expected_bad, (n, maximal_bad, expected_bad)
        assert max(s.bit_count() for s, ok in enumerate(good) if not ok) == m + 1
        print(f"n={n} coefficients={counts} minimal={len(minimal)} maximal_nonMEG={len(maximal_bad)}")
    print("VERIFY_OK")


if __name__ == "__main__":
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 13)
