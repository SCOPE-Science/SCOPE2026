"""Finite sanity checks of ancestor retractions on Hamming boxes.

This is supplementary verification, not an infinite proof.
"""
from itertools import product


def support(x):
    return tuple(i for i, a in enumerate(x) if a)


def order_key(x):
    s = support(x)
    return (len(s), s, tuple(x[i] for i in s))


def parent(x):
    y = list(x)
    y[support(x)[-1]] = 0
    return tuple(y)


def distance(x, y):
    return sum(a != b for a, b in zip(x, y))


def verify(alphabets):
    vertices = sorted(product(*(range(q) for q in alphabets)), key=order_key)
    edges = [(x, y) for j, x in enumerate(vertices) for y in vertices[j + 1:] if distance(x, y) == 1]
    old = {}
    maximum = 0
    for m in range(1, len(vertices) + 1):
        target = set(vertices[:m])
        r = {}
        for v in vertices:
            a = v
            while a not in target:
                a = parent(a)
            r[v] = a
        assert set(r.values()) == target
        assert all(r[t] == t for t in target)
        for j, s in old.items():
            assert all(s[r[v]] == s[v] == r[s[v]] for v in vertices), (alphabets, j, m)
        maximum = max(maximum, *(distance(r[x], r[y]) for x, y in edges))
        old[m] = r
    assert maximum <= 2, (alphabets, maximum)
    return maximum


if __name__ == '__main__':
    sizes = ((2,), (3,), (2, 2), (2, 3), (3, 3), (2, 2, 2),
             (2, 2, 3), (2, 3, 3), (3, 3, 3), (2, 2, 2, 2),
             (2, 2, 2, 3), (2, 3, 3, 3), (2, 2, 2, 2, 2))
    for dims in sizes:
        print(dims, 'Lipschitz maximum', verify(dims))
    square = ((0, 0), (1, 0), (0, 1), (1, 1))
    square_maps = [
        {v: (0, 0) for v in square},
        {(0, 0): (0, 0), (1, 0): (1, 0), (0, 1): (0, 0), (1, 1): (0, 0)},
        {(0, 0): (0, 0), (1, 0): (1, 0), (0, 1): (0, 1), (1, 1): (0, 0)},
        {v: v for v in square},
    ]
    for m, r in enumerate(square_maps, 1):
        assert set(r.values()) == set(square[:m])
        assert all(distance(r[u], r[v]) <= distance(u, v) for u in square for v in square)
        for s in square_maps[:m-1]:
            assert all(s[r[v]] == s[v] == r[s[v]] for v in square)
    print('binary square nested norm-one exception: checked')
