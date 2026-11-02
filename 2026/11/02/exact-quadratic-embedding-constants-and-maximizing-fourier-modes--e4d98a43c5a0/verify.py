"""Finite supplementary checks for Möbius-ladder graph-distance quadratic forms.

Requires only Python's standard library.  The all-size theorem rests on the
analytic Fourier argument, not on enumeration in this script.
"""
from collections import deque
from math import cos, sin, tan, pi, isclose


def all_pairs_graph_distance(n):
    N = 2 * n
    adj = [{(v - 1) % N, (v + 1) % N, (v + n) % N}
           for v in range(N)]
    rows = []
    for src in range(N):
        dist = [-1] * N
        dist[src] = 0
        queue = deque([src])
        while queue:
            v = queue.popleft()
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    queue.append(w)
        rows.append(dist)
    return rows


def predicted_fourier_eigenvalue(n, j):
    N = 2 * n
    j = min(j, N - j)
    if j == 0:
        raise ValueError('nonconstant frequencies only')
    phi = pi * j / N
    if j % 2:
        sign = -1 if (j + 1) // 2 % 2 else 1
        return sign / sin(phi) if n % 2 else sign / tan(phi)
    sign = 1 if j // 2 % 2 == 0 else -1
    if n % 2:
        return (sign * cos(phi) - 1) / sin(phi) ** 2
    return (sign * cos(phi) ** 2 - 1) / sin(phi) ** 2


def predicted_qec(n):
    phi = 3 * pi / (2 * n)
    return 1 / sin(phi) if n % 2 else 1 / tan(phi)


checks = 0
for n in range(3, 61):
    N = 2 * n
    distances = all_pairs_graph_distance(n)
    row = distances[0]
    for u in range(N):
        for v in range(N):
            k = (v - u) % N
            circular = min(k, N - k)
            wanted = min(circular, n + 1 - circular)
            assert distances[u][v] == wanted
            checks += 1
    eigen = [sum(row[k] * cos(pi * j * k / n) for k in range(N))
             for j in range(N)]
    for j in range(1, N):
        expected = predicted_fourier_eigenvalue(n, j)
        assert isclose(eigen[j], expected, rel_tol=1e-9, abs_tol=1e-9), (n, j)
        checks += 1
    expected_top = predicted_qec(n)
    actual_top = max(eigen[1:])
    assert isclose(actual_top, expected_top, rel_tol=1e-9, abs_tol=1e-9), n
    maximizers = [j for j in range(1, N)
                  if isclose(eigen[j], actual_top, abs_tol=1e-8)]
    assert maximizers == ([3] if n == 3 else [3, N - 3]), (n, maximizers)
    checks += 2
    if n <= 24:
        witness = [cos(3 * pi * k / n) for k in range(N)]
        norm2 = sum(x*x for x in witness)
        assert abs(sum(witness)) < 1e-9
        quadratic = sum(witness[u] * distances[u][v] * witness[v]
                        for u in range(N) for v in range(N))
        assert isclose(quadratic/norm2, expected_top, abs_tol=1e-8)
        checks += 2
for n in (101, 201, 401, 801, 1601):
    q = predicted_qec(n)
    assert abs(n * (q - 2*n/(3*pi)) - pi/4) < 0.005
    checks += 1
for n in (100, 200, 400, 800, 1600):
    q = predicted_qec(n)
    assert abs(n * (q - 2*n/(3*pi)) + pi/2) < 0.01
    checks += 1
print(f'PASS: {checks} supplementary separate shortest-path, Fourier and asymptotic checks')
