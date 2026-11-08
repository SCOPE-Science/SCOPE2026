"""Exact integer/rational checks for the bipartite RK4 local positivity theorem.

Self-contained (Python 3 standard library); the infinite-size proof is in RESULT.md.
"""
from fractions import Fraction
from itertools import combinations
from collections import deque


def multiply(a, b):
    n = len(a)
    return [[sum(a[i][k] * b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def graph_matrices(n, edges):
    a = [[0] * n for _ in range(n)]
    for i, j in edges:
        a[i][j] = a[j][i] = 1
    d = [sum(row) for row in a]
    b = [[a[i][j] + (d[i] if i == j else 0) for j in range(n)] for i in range(n)]
    l = [[(d[i] if i == j else 0) - a[i][j] for j in range(n)] for i in range(n)]
    return a, d, b, l


def bipartite_connected(a):
    n = len(a)
    colors = [-1] * n
    colors[0] = 0
    q = deque([0])
    while q:
        i = q.popleft()
        for j, yes in enumerate(a[i]):
            if not yes:
                continue
            if colors[j] == -1:
                colors[j] = 1 - colors[i]
                q.append(j)
            elif colors[j] == colors[i]:
                return False, colors
    return all(c != -1 for c in colors), colors


def distances(a):
    n = len(a)
    out = [[n + 1] * n for _ in range(n)]
    for i in range(n):
        out[i][i] = 0
        q = deque([i])
        while q:
            v = q.popleft()
            for w in range(n):
                if a[v][w] and out[i][w] > out[i][v] + 1:
                    out[i][w] = out[i][v] + 1
                    q.append(w)
    return out


def h2(x, y, z):
    return x*x + y*y + z*z + x*y + x*z + y*z


def h3(x, y):
    return x**3 + x*x*y + x*y*y + y**3


def evaluate(l, h):
    n = len(l)
    p = [[int(i == j) for j in range(n)] for i in range(n)]
    ans = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    for k in range(1, 5):
        p = multiply(p, l)
        from math import factorial
        f = (-h)**k / factorial(k)
        for i in range(n):
            for j in range(n):
                ans[i][j] += f * p[i][j]
    return ans


def check_graph(n, edges):
    a, d, b, l = graph_matrices(n, edges)
    yes, colors = bipartite_connected(a)
    if not yes:
        return False, 0
    dist = distances(a)
    a2 = multiply(a, a)
    a3 = multiply(a2, a)
    a4 = multiply(a3, a)
    b2 = multiply(b, b)
    b3 = multiply(b2, b)
    b4 = multiply(b3, b)
    ecount = 0
    for i in range(n):
        for j in range(i + 1, n):
            di = dist[i][j]
            if di == 1:
                ecount += 1
                x, y = d[i], d[j]
                s = x + y
                p2 = x*x + x*y + y*y + a3[i][j]
                w = sum(d[i] + d[u] + d[v] + d[j]
                        for u in range(n) for v in range(n)
                        if a[i][u] and a[u][v] and a[v][j])
                p3 = h3(x, y) + w
                assert (b2[i][j], b3[i][j], b4[i][j]) == (s, p2, p3)
                assert a3[i][j] <= x*y
                assert 4*p2*p2 < 9*s*p3
            elif di == 2:
                s = sum(d[i] + d[u] + d[j] for u in range(n)
                        if a[i][u] and a[u][j])
                z = sum(h2(d[i], d[u], d[j]) for u in range(n)
                        if a[i][u] and a[u][j])
                assert (b2[i][j], b3[i][j], b4[i][j]) == (a2[i][j], s, z + a4[i][j])
                for u in range(n):
                    if a[i][u] and a[u][j]:
                        t = d[i] + d[u] + d[j]
                        assert 3*h2(d[i], d[u], d[j]) >= 2*t*t
            elif di == 3:
                w = sum(d[i] + d[u] + d[v] + d[j]
                        for u in range(n) for v in range(n)
                        if a[i][u] and a[u][v] and a[v][j])
                assert b3[i][j] == a3[i][j] > 0
                assert b4[i][j] == w > 0
            elif di == 4:
                assert b4[i][j] == a4[i][j] > 0
            elif di >= 5:
                assert b4[i][j] == 0
    for h in (Fraction(1, 20), Fraction(1, 5), Fraction(1, 2), Fraction(1), Fraction(2), Fraction(4)):
        t = evaluate(l, h)
        predicted = True
        for i in range(n):
            assert sum(t[i]) == 1
            assert t[i][i] > 0
            for j in range(i + 1, n):
                di = dist[i][j]
                if di == 1:
                    s, q, r = b2[i][j], b3[i][j], b4[i][j]
                    g = 1 - h*s/2 + h*h*q/6 - h*h*h*r/24
                    assert t[i][j] == h*g
                    if g < 0:
                        predicted = False
                elif di == 2:
                    assert t[i][j] > 0
                elif di == 3:
                    val = h**3*(4*b3[i][j] - h*b4[i][j])/24
                    assert t[i][j] == val
                    if val < 0:
                        predicted = False
                elif di == 4:
                    assert t[i][j] == h**4*a4[i][j]/24 > 0
                else:
                    assert t[i][j] == 0
        assert predicted == all(t[i][j] >= 0 for i in range(n) for j in range(n))
    return True, ecount


def run():
    graph_count = edge_count = 0
    per_n = {}
    for n in range(2, 7):
        pairs = list(combinations(range(n), 2))
        good = 0
        for mask in range(1, 1 << len(pairs)):
            edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
            valid, edges_examined = check_graph(n, edges)
            if valid:
                good += 1
                edge_count += edges_examined
        per_n[n] = good
        graph_count += good
    witness = [(0, 1), (0, 4), (0, 6), (2, 6), (3, 6), (5, 6)]
    a, d, b, l = graph_matrices(7, witness)
    b2 = multiply(b, b); b3 = multiply(b2, b); b4 = multiply(b3, b)
    assert (b2[0][6], b3[0][6], b4[0][6]) == (7, 43, 247)
    h = Fraction(4, 9)
    g = 1 - h * b2[0][6] / 2 + h*h*b3[0][6]/6 - h*h*h*b4[0][6]/24
    assert g == -Fraction(95, 2187)
    for i, j in witness:
        if (i, j) == (0, 6):
            continue
        gs = 1 - h * b2[i][j] / 2 + h*h*b3[i][j] / 6 - h*h*h*b4[i][j] / 24
        assert gs == (Fraction(859, 2187) if 0 in (i, j) else Fraction(541, 2187))
    path_a, path_d, path_b, path_l = graph_matrices(6, [(i, i+1) for i in range(5)])
    path_b2 = multiply(path_b, path_b)
    path_b3 = multiply(path_b2, path_b)
    path_b4 = multiply(path_b3, path_b)
    half = Fraction(1, 2)
    for i in range(5):
        q = 1 - half*path_b2[i][i+1]/2 + half**2*path_b3[i][i+1]/6 - half**3*path_b4[i][i+1]/24
        assert q > 0
    path_dist = distances(path_a)
    assert min(Fraction(4*path_b3[i][j], path_b4[i][j])
               for i in range(6) for j in range(i+1,6) if path_dist[i][j] == 3) == Fraction(1,2)
    for u, v in ((1, 2), (4, 3)):
        assert (b3[u][v], b4[u][v]) == (1, 9)
    print('VERIFY_OK')
    print('Connected labeled bipartite graphs checked by order:', per_n)
    print('Total verified graphs:', graph_count)
    print('Edge discriminants checked:', edge_count)
    print('Exact rational test timesteps per graph: 6')
    print('Double-star central edge at h=4/9: g=-95/2187; distance-three entries only reach zero')

if __name__ == '__main__':
    run()
