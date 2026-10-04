#!/usr/bin/env python3

def det(u, v):
    return u[0] * v[1] - u[1] * v[0]

def shoelace2(poly):
    s = 0
    for i, (x, y) in enumerate(poly):
        x2, y2 = poly[(i + 1) % len(poly)]
        s += x * y2 - y * x2
    return abs(s)

fan = [(1, 0), (0, 1), (-1, -2), (0, -1)]
assert [abs(det(fan[i], fan[(i + 1) % 4])) for i in range(4)] == [1, 1, 1, 1]
assert (fan[2][0] + fan[0][0], fan[2][1] + fan[0][1]) == (0, -2)
assert (0, -2) == (2 * fan[3][0], 2 * fan[3][1])

for r in range(1, 80):
    k = 2 * r + 1
    points = []
    triples = []
    for j in range(r + 1):
        for q in range(k - 2 * j + 1):
            p = k - q - 2 * j
            assert p >= 0
            triples.append((p, q, j))
            points.append((q, j))

    vertices = {(0, 0), (k, 0), (1, r), (0, r)}
    assert vertices.issubset(set(points))
    for q, j in points:
        assert q >= 0
        assert j >= 0
        assert j <= r
        assert q + 2 * j <= k

    assert max(j for _, j in points) == r
    assert max(q for q, j in points if j == 0) == k
    assert max(q for q, j in points if j == r) == 1

    assert all(p + q > 0 for p, q, j in triples)
    assert (k, 0, 0) in triples
    assert (0, k, 0) in triples

    poly = [(0, 0), (k, 0), (1, r), (0, r)]
    normalized_area = shoelace2(poly)
    assert normalized_area == (k * k - 1) // 2

    edge_pairs = [
        ((1, 0), (0, 1)),
        ((-1, 0), (-2, 1)),
        ((2, -1), (-1, 0)),
        ((1, 0), (0, -1)),
    ]
    assert all(abs(det(a, b)) == 1 for a, b in edge_pairs)

print("VERIFY_OK")
