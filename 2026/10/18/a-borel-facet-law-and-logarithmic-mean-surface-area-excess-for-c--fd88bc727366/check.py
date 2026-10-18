"""Reproducible finite checks for Cayley-tree graphical-zonotope surface area.

No third-party packages are needed. Finite tests support, but do not replace,
analytical arguments for arbitrary order and asymptotic estimates.
"""
import heapq
import itertools
import math
from collections import deque


def edges_from_prufer(code, n):
    deg = [1] * n
    for x in code:
        deg[x] += 1
    leaves = [v for v in range(n) if deg[v] == 1]
    heapq.heapify(leaves)
    out = []
    for x in code:
        u = heapq.heappop(leaves)
        out.append((u, x))
        deg[u] -= 1
        deg[x] -= 1
        if deg[x] == 1:
            heapq.heappush(leaves, x)
    a = heapq.heappop(leaves)
    b = heapq.heappop(leaves)
    out.append((a, b))
    return out


def edge_cuts(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    out = []
    for a, b in edges:
        seen = {a}
        q = deque([a])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if (u == a and v == b) or (u == b and v == a):
                    continue
                if v not in seen:
                    seen.add(v)
                    q.append(v)
        assert len(seen) < n
        out.append(min(len(seen), n - len(seen)))
    return out


def det_bareiss(A):
    M = [list(map(int, row)) for row in A]
    n = len(M)
    if n == 0:
        return 1
    s = 1
    denom = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            i = next(i for i in range(k + 1, n) if M[i][k] != 0)
            M[k], M[i] = M[i], M[k]
            s = -s
        pivot = M[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = M[i][j] * pivot - M[i][k] * M[k][j]
                assert num % denom == 0
                M[i][j] = num // denom
        for i in range(k + 1, n):
            M[i][k] = 0
        denom = pivot
    return s * M[-1][-1]


def gram(n, edges):
    vectors = []
    for a, b in edges:
        x = [0] * n
        x[a] = 1
        x[b] = -1
        vectors.append(x)
    return [[sum(x * y for x, y in zip(u, v)) for v in vectors] for u in vectors]


def area_from_cuts(n, cuts):
    return 2 * sum(math.sqrt(k * (n - k)) for k in cuts)


def expected_cut_counts(n):
    denominator = n ** (n - 2)
    ans = {}
    for k in range(1, n // 2 + 1):
        numerator = math.comb(n, k) * (k ** (k - 1)) * ((n - k) ** (n - k - 1))
        if 2 * k == n:
            assert numerator % 2 == 0
            numerator //= 2
        ans[k] = numerator / denominator
    return ans


def exact_expected_area(n):
    return 2 * sum(count * math.sqrt(k * (n - k))
                   for k, count in expected_cut_counts(n).items())


def log_expected_area(n):
    # Avoid huge integers when checking large dimensions.
    total = 0.0
    for k in range(1, n // 2 + 1):
        log_count = (math.lgamma(n + 1) - math.lgamma(k + 1)
                     - math.lgamma(n - k + 1)
                     + (k - 1) * math.log(k)
                     + (n - k - 1) * math.log(n - k)
                     - (n - 2) * math.log(n))
        weight = 0.5 if 2 * k == n else 1.0
        total += weight * math.exp(log_count) * math.sqrt(k * (n - k))
    return 2 * total


def main():
    checked = 0
    for n in range(3, 7):
        total = 0.0
        counts = {k: 0 for k in range(1, n // 2 + 1)}
        best_min = 2 * (n - 1) * math.sqrt(n - 1)
        best_max = 2 * sum(math.sqrt(j * (n - j)) for j in range(1, n))
        for code in itertools.product(range(n), repeat=n - 2):
            edges = edges_from_prufer(code, n)
            cuts = edge_cuts(n, edges)
            area = area_from_cuts(n, cuts)
            total += area
            assert best_min - 1e-10 <= area <= best_max + 1e-10
            for k in cuts:
                counts[k] += 1
            degrees = [0] * n
            for a, b in edges:
                degrees[a] += 1
                degrees[b] += 1
            if n >= 4:
                if abs(area - best_min) < 1e-10:
                    assert sorted(degrees) == [1] * (n - 1) + [n - 1]
                if abs(area - best_max) < 1e-10:
                    assert sorted(degrees) == [1, 1] + [2] * (n - 2)
            G = gram(n, edges)
            assert det_bareiss(G) == n
            area_gram = 0.0
            for j, k in enumerate(cuts):
                Gj = [[G[a][b] for b in range(n - 1) if b != j]
                      for a in range(n - 1) if a != j]
                det = det_bareiss(Gj)
                assert det == k * (n - k)
                area_gram += 2 * math.sqrt(det)
            assert math.isclose(area, area_gram, rel_tol=1e-12)
            checked += 1
        N = n ** (n - 2)
        assert math.isclose(total / N, exact_expected_area(n), rel_tol=1e-11)
        for k, expected in expected_cut_counts(n).items():
            assert math.isclose(counts[k] / N, expected, rel_tol=1e-12)
        assert math.isclose(sum(expected_cut_counts(n).values()), n - 1,
                            rel_tol=1e-12)
    # Only numerical corroboration of the analytical leading constant.
    asympt_ratios = []
    for n in (100, 1000, 10000):
        exact = log_expected_area(n)
        predicted = math.sqrt(2 / math.pi) * n ** 1.5 * math.log(n)
        asympt_ratios.append(exact / predicted)
    assert 1.0 < asympt_ratios[-1] < asympt_ratios[0] < 1.2
    print(f"PASS: {checked} labeled trees, Gram minors, complete finite Cayley expectations, extremizers, and large-n asymptotic consistency")
    print("Asymptotic normalized ratios at n=100,1000,10000:", asympt_ratios)


if __name__ == '__main__':
    main()
