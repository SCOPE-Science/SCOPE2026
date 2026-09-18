from collections import deque


def build(a, b, c, d):
    q = a + b + c + d
    x, y = q, q + 1
    adj = [set() for _ in range(q + 2)]

    for i in range(q):
        for j in range(i + 1, q):
            adj[i].add(j)
            adj[j].add(i)

    adj[x].add(y)
    adj[y].add(x)

    pos = 0
    A = range(pos, pos + a)
    pos += a
    B = range(pos, pos + b)
    pos += b
    C = range(pos, pos + c)

    for v in A:
        adj[x].add(v)
        adj[v].add(x)
    for v in B:
        adj[y].add(v)
        adj[v].add(y)
    for v in C:
        adj[x].add(v)
        adj[v].add(x)
        adj[y].add(v)
        adj[v].add(y)

    return adj


def all_distances(adj):
    distances = []
    for source in range(len(adj)):
        dist = [-1] * len(adj)
        dist[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if dist[v] < 0:
                    dist[v] = dist[u] + 1
                    queue.append(v)
        distances.append(dist)
    return distances


def gap(adj):
    distances = all_distances(adj)
    n = len(adj)
    assert all(-1 not in row for row in distances)

    wiener = sum(
        distances[i][j]
        for i in range(n)
        for j in range(i + 1, n)
    )

    szeged = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                nu = sum(
                    distances[z][u] < distances[z][v]
                    for z in range(n)
                )
                nv = sum(
                    distances[z][v] < distances[z][u]
                    for z in range(n)
                )
                szeged += nu * nv

    return szeged - wiener


def formula(a, b, c, d):
    return (
        8 * a * b
        + 2 * c * (a + b)
        + 3 * d * (a + b)
        + 4 * c * d
        - 4 * d
    )


def two_connected_parameters(a, b, c, d):
    q = a + b + c + d
    return (
        q >= 2
        and a + c >= 1
        and b + c >= 1
        and a + b + c >= 2
    )


checked = 0
equality = []

for q in range(2, 21):
    for a in range(q + 1):
        for b in range(q - a + 1):
            for c in range(q - a - b + 1):
                d = q - a - b - c
                if not two_connected_parameters(a, b, c, d):
                    continue

                observed = gap(build(a, b, c, d))
                expected = formula(a, b, c, d)
                assert observed == expected
                checked += 1

                if q >= 8 and observed == 2 * (q + 2):
                    equality.append((q, a, b, c, d))


expected_equality = [
    (q, 1, 1, 0, q - 2)
    for q in range(8, 21)
]
expected_equality += [
    (8, 1, 0, 1, 6),
    (8, 0, 1, 1, 6),
]

assert sorted(equality) == sorted(expected_equality)

print(f"verified formula on {checked} two-connected parameter quadruples")
print("verified equality classification for 8 <= q <= 20")
