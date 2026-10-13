from __future__ import annotations


def build(N: int):
    chars = []
    vertices = []
    def rec(level: int, rem: int):
        p = len(chars)
        if rem == 0:
            chars.append('a')
            q = len(chars)
            vertices.append((p, q, level))
            return
        chars.append('x')
        rec(level + 1, rem - 1)
        rec(level + 1, rem - 1)
        chars.append('y')
        q = len(chars)
        vertices.append((p, q, level))
    rec(0, N)
    eta = [None] * (len(chars) + 1)
    for p, q, level in vertices:
        for g in (p, q):
            if eta[g] is None or level < eta[g]:
                eta[g] = level
    assert all(h is not None for h in eta)
    edges = [[] for _ in range(len(chars) + 1)]
    for i, c in enumerate(chars):
        if c in ('x', 'y'):
            edges[i].append(i + 1)
    for p, q, _ in vertices:
        edges[p].append(q)
    return eta, edges


def longest_crossing_free(N: int, n: int) -> int:
    eta, edges = build(N)
    grid_heights = sorted({h for h in eta if h % n == 0})
    best = 0
    # A crossing-free path either visits no grid gap, or all grid gaps it
    # visits have one fixed height. For each possibility, take a longest
    # path in the induced acyclic graph on allowed gaps.
    for mode in [None] + grid_heights:
        allowed = [h % n != 0 or (mode is not None and h == mode) for h in eta]
        neg = -10**9
        dp = [neg] * len(eta)
        for u in range(len(eta)):
            if not allowed[u]:
                continue
            if dp[u] < 0:
                dp[u] = 0
            for v in edges[u]:
                if allowed[v] and dp[u] + 1 > dp[v]:
                    dp[v] = dp[u] + 1
        best = max(best, max(dp))
    return best


def L(r: int) -> int:
    return 3 * (2 ** r) - 2


for n in range(1, 7):
    N = 2 * n
    got = longest_crossing_free(N, n)
    expected = 2 * L(2 * n - 2)
    threshold = expected + 1
    assert got == expected, (n, got, expected)
    assert threshold == 6 * (4 ** (n - 1)) - 3
    print(f"n={n} N={N} max_crossing_free={got} threshold={threshold}")

# Check stability at a taller multiple for moderate sizes.
for n in range(1, 5):
    N = 3 * n
    got = longest_crossing_free(N, n)
    expected = 2 * L(2 * n - 2)
    assert got == expected, (n, N, got, expected)
    print(f"n={n} N={N} taller_max={got}")

print('VERIFY_OK')
