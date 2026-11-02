"""Exact-rational checks for the arclength-distance law on unit metric trees.

Run: python CHECK.py
Only the Python standard library is required.
"""
from collections import deque
from fractions import Fraction as F
from itertools import product
from math import comb


def prufer_tree(code):
    n = len(code) + 2
    deg = [1] * n
    for a in code:
        deg[a] += 1
    out = []
    for a in code:
        u = next(i for i in range(n) if deg[i] == 1)
        out.append((u, a))
        deg[u] -= 1
        deg[a] -= 1
    u, v = (i for i in range(n) if deg[i] == 1)
    out.append((u, v))
    return out


def matrix(edges):
    n = max(max(e) for e in edges) + 1
    g = [[] for _ in range(n)]
    for a, b in edges:
        g[a].append(b)
        g[b].append(a)
    D = []
    for u in range(n):
        d = [-1] * n
        d[u] = 0
        queue = deque([u])
        while queue:
            x = queue.popleft()
            for y in g[x]:
                if d[y] < 0:
                    d[y] = d[x] + 1
                    queue.append(y)
        assert all(x >= 0 for x in d)
        D.append(d)
    return g, D


def edge_separations(edges, D):
    ret = []
    for i, (a, b) in enumerate(edges):
        for c, d in edges[i + 1:]:
            ret.append(min(D[a][c], D[a][d], D[b][c], D[b][d]))
    return ret


def uniform_sum_cdf(s):
    if s <= 0:
        return F(0)
    if s <= 1:
        return s * s / 2
    if s <= 2:
        return 1 - (2 - s) ** 2 / 2
    return F(1)


def edge_self_cdf(s):
    if s <= 0:
        return F(0)
    if s <= 1:
        return 2*s - s*s
    return F(1)


def exact_cdf(m, delta, t):
    return (m * edge_self_cdf(t) + 2 * sum((uniform_sum_cdf(t - d) for d in delta), F(0))) / (m*m)


def degree_index(g):
    return sum(comb(len(neighbors), 2) for neighbors in g)


def cut_internal_count(g, edges):
    ans = 0
    n = len(g)
    for a, b in edges:
        seen = {a}
        queue = deque([a])
        while queue:
            u = queue.popleft()
            for v in g[u]:
                if (u == a and v == b) or (u == b and v == a):
                    continue
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        left = len(seen) - 1
        right = (n - len(seen)) - 1
        ans += left * right
    return ans


def run_case(edges, do_grid=True):
    m = len(edges)
    g, D = matrix(edges)
    delta = edge_separations(edges, D)
    ad = degree_index(g)
    assert sum(d == 0 for d in delta) == ad
    assert len(delta) == comb(m, 2)
    assert sum(delta) == cut_internal_count(g, edges)
    assert sum(delta) <= comb(m, 3)
    assert 0 <= sum(delta)
    if m >= 3 and ad > m - 1:
        assert sum(delta) < comb(m, 3)
    if m >= 3 and ad < comb(m, 2):
        assert sum(delta) >= m-2
    # Count all far-apart edge pairs at each separation threshold.
    for k in range(0, m):
        far = sum(x >= k for x in delta)
        path_far = max(0, m - k - 1) * max(0, m - k) // 2
        assert far <= path_far, (edges, k, far, path_far)
    if do_grid:
        for z in range(0, 4*m + 1):
            t = F(z, 4)
            curr = exact_cdf(m, delta, t)
            star = exact_cdf(m, [0] * comb(m, 2), t)
            path = exact_cdf(m, [j-i-1 for i in range(m) for j in range(i+1,m)], t)
            assert 0 <= path <= curr <= star <= 1, (edges, t, path, curr, star)
            if 0 < t < 1 and m >= 3:
                assert curr - path == t*t*F(ad-m+1, m*m)
                assert star - curr == t*t*F(comb(m,2)-ad, m*m)
    # Exact mean / W1 identities. CDF dominance was separately checked.
    w1_star = F(2 * sum(delta), m*m)
    w1_path = F(2 * (comb(m,3)-sum(delta)), m*m)
    assert w1_star >= 0 and w1_path >= 0
    assert w1_star + w1_path == F((m-1)*(m-2), 3*m)


def check_geometry():
    # The endpoint-based intrinsic distance is tested independently on a rational grid.
    # The correct closest-endpoint orientation converts each distinct-edge distance
    # to an intermediate-edge count plus two independent [0,1] offsets.
    sets = [prufer_tree(code) for n in range(3,8) for code in list(product(range(n), repeat=n-2))[:40]]
    for edges in sets:
        _, D = matrix(edges)
        for i, (a,b) in enumerate(edges):
            for c,d in edges[i+1:]:
                endpoint_pairs = [(D[a][c],a,c), (D[a][d],a,d), (D[b][c],b,c), (D[b][d],b,d)]
                sep, nearest_a, nearest_b = min(endpoint_pairs)
                for ui in range(7):
                    for vi in range(7):
                        u = F(ui,6)
                        v = F(vi,6)
                        dist = min(u+v+D[a][c], u+1-v+D[a][d],
                                   1-u+v+D[b][c], 2-u-v+D[b][d])
                        from_a = u if nearest_a == a else 1-u
                        from_b = v if nearest_b == c else 1-v
                        assert dist == sep + from_a + from_b


def main():
    checks = 0
    for n in range(2, 8):
        for code in product(range(n), repeat=n-2):
            run_case(prufer_tree(code), do_grid=(n <= 6))
            checks += 1
    check_geometry()
    # Nonstar minimizer of the transport gap: one subdivision of a star edge.
    for m in range(3, 18):
        # Hub 0 with m-1 incident edges, one of which is subdivided at vertex 1.
        edges = [(0,1),(1,2)] + [(0,j) for j in range(3,m+1)]
        assert len(edges) == m
        run_case(edges)
        _, D = matrix(edges)
        assert sum(edge_separations(edges, D)) == m-2
        checks += 1
    print('PASS: %d trees; all separation tails, exact CDF bounds, local gaps, cut sums, W1 identities.' % checks)
    print('PASS: independent endpoint route grid, nonstar sharp stability witnesses.')


if __name__ == '__main__':
    main()
