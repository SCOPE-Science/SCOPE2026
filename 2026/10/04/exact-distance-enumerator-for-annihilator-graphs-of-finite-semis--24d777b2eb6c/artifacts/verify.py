from collections import deque, Counter
from itertools import combinations

def proper_supports(n):
    full = (1 << n) - 1
    return [s for s in range(1, full)]

def incomparable(s, t):
    return not ((s & t) == s or (s & t) == t)

def ann_support(s, n):
    return ((1 << n) - 1) ^ s

def union_equals_sum_for_coordinate_ideals(a, b):
    # Coordinate ideals are comparable iff one support contains the other.
    comparable = ((a & b) == a) or ((a & b) == b)
    return comparable

def badawi_adj(s, t, n):
    ax = ann_support(s, n)
    ay = ann_support(t, n)
    # ann(xy) has coordinate support ax union ay.
    # Set union of two ideals equals their sum exactly when they are comparable.
    return not union_equals_sum_for_coordinate_ideals(ax, ay)

def weight(s, qs):
    z = 1
    for i, q in enumerate(qs):
        if (s >> i) & 1:
            z *= q - 1
    return z

def check(qs):
    n = len(qs)
    supports = proper_supports(n)
    vertices = []
    for s in supports:
        vertices.extend((s, k) for k in range(weight(s, qs)))

    for s in supports:
        for t in supports:
            assert badawi_adj(s, t, n) == incomparable(s, t)

    adj = {v: set() for v in vertices}
    for i, u in enumerate(vertices):
        for v in vertices[i+1:]:
            if incomparable(u[0], v[0]):
                adj[u].add(v)
                adj[v].add(u)

    dcounts = Counter()
    for i, u in enumerate(vertices):
        dist = {u: 0}
        q = deque([u])
        while q:
            x = q.popleft()
            for y in adj[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    q.append(y)
        assert len(dist) == len(vertices)
        for v in vertices[i+1:]:
            dcounts[dist[v]] += 1

    Q = 1
    A = 1
    B = 1
    P = 1
    for q in qs:
        Q *= q
        A *= q - 1
        B *= q*q - 2*q + 2
        P *= q*q - q + 1
    N = Q - A - 1
    E = (Q*Q + B - 2*P) // 2
    D2 = N*(N-1)//2 - E
    W = E + 2*D2

    assert len(vertices) == N
    assert dcounts[1] == E
    assert dcounts[2] == D2
    assert sum(dcounts.values()) == N*(N-1)//2
    assert W == N*(N-1) - E
    assert all(k in (1,2) for k in dcounts)

tests = [
    (2,2),
    (2,3),
    (3,3),
    (2,2,2),
    (2,3,4),
    (2,3,5),
    (3,4,5),
]
for qs in tests:
    check(qs)

print("VERIFY_OK")
