from collections import Counter
from functools import lru_cache
from math import ceil

BLOCK = [
    (0, 2), (2, 4), (4, 6), (6, 8),
    (0, 11), (0, 13), (0, 15), (0, 17),
    (2, 11), (4, 11), (6, 11), (8, 11),
    (11, 13), (13, 15), (15, 17), (17, 19), (8, 10),
]
GAMMA = [
    (0, 13), (0, 15), (1, 3), (1, 12), (1, 13), (3, 5),
    (3, 10), (3, 12), (5, 7), (5, 10), (7, 9), (7, 10),
    (10, 12), (13, 15), (15, 17),
]

TEMPLATES = {
    0: (),
    1: (8,),
    2: (8, 10),
    3: (8, 10, 11),
    4: (9, 9, 10, 12),
    5: (8, 8, 7, 11, 10),
    6: (8, 8, 7, 11, 10, 2),
    7: (8, 10, 8, 9, 8, 12, 9),
    8: (8, 10, 8, 9, 8, 12, 9, 16),
    9: (("c", 9), ("c", 9), ("N", 2), ("N", 3), ("N", 2),
        ("N", 6), ("N", 4), ("c", 10), ("c", 12)),
    10: (8, 8, 8, 8, 12, 11, 8, 11, 10, 8),
    11: (9, 9, 10, 12, 10, 9, 12, 13, 13, 12, 11),
    12: (8, 8, 8, 8, 12, 11, 8, 11, 10, 8, 10, 2),
    13: (8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9),
    14: (8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2),
    15: (8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2, 4),
    16: (8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2, 4, 5),
    17: (8, 8, 8, 8, 12, 11, 8, 11, 10, 1, 10, 10, 9, 2, 2, 1, 5),
}

EXPECTED_DELTA = {
    0: {},
    1: {4: 1},
    2: {2: 1, 5: 1, 6: -1, 7: 1},
    3: {2: 1, 3: 1, 5: 1, 6: -1, 8: 1},
    4: {2: 2, 5: 2, 6: -1, 8: 1},
    5: {2: 2, 5: 2, 6: 1},
    6: {2: 2, 3: 1, 5: 2, 7: 1},
    7: {2: 3, 5: 3, 7: 1},
    8: {2: 3, 3: 1, 5: 3, 8: 1},
    9: {2: 4, 5: 4, 8: 1},
    10: {2: 4, 4: 1, 5: 4, 8: 1},
    11: {2: 5, 5: 4, 6: 1, 8: 1},
    12: {2: 5, 4: 1, 5: 5, 6: -1, 7: 1, 8: 1},
    13: {2: 5, 3: 1, 5: 5, 6: 1, 8: 1},
    14: {2: 5, 3: 1, 4: 1, 5: 5, 6: 1, 8: 1},
    15: {2: 6, 3: 1, 5: 6, 7: 1, 8: 1},
    16: {2: 6, 3: 2, 5: 6, 8: 2},
    17: {2: 7, 4: 1, 5: 7, 7: 1, 8: 1},
}

SMALL_WITNESSES = {
    5: [(1, 4), (2, 4)],
    6: [(1, 5), (2, 5), (3, 5)],
    7: [(1, 6), (2, 6), (3, 6), (4, 6)],
    8: [(1, 7), (2, 7), (3, 5), (3, 6), (3, 7)],
    9: [(1, 8), (2, 4), (2, 5), (2, 8), (5, 7), (5, 8)],
    10: [(1, 9), (2, 4), (2, 7), (2, 9), (4, 6), (4, 7), (7, 9)],
    11: [(1, 10), (2, 10), (3, 5), (3, 8), (3, 10), (5, 7), (5, 8), (8, 10)],
    12: [(1, 11), (2, 4), (2, 9), (2, 11), (4, 6), (4, 9), (6, 8), (6, 9), (9, 11)],
    13: [(1, 12), (2, 12), (3, 12), (4, 6), (4, 11), (4, 12), (6, 8), (6, 11), (8, 10), (8, 11)],
    14: [(0, 8), (0, 10), (0, 12), (1, 3), (1, 7), (1, 8), (3, 5), (3, 7), (5, 7), (8, 10), (10, 12)],
    15: [(1, 14), (2, 4), (2, 12), (2, 14), (4, 6), (4, 11), (4, 12), (6, 8), (6, 11), (8, 10), (8, 11), (12, 14)],
    16: [(0, 10), (0, 12), (0, 14), (1, 3), (1, 9), (1, 10), (3, 7), (3, 9), (4, 7), (5, 7), (7, 9), (10, 12), (12, 14)],
    17: [(0, 10), (0, 12), (0, 14), (1, 3), (1, 9), (1, 10), (3, 5), (3, 7), (3, 9), (5, 7), (7, 9), (10, 12), (12, 14), (14, 16)],
    18: [(0, 11), (0, 13), (0, 15), (1, 10), (1, 11), (2, 4), (2, 8), (2, 10), (4, 6), (4, 8), (6, 8), (8, 10), (11, 13), (13, 15), (15, 17)],
    19: [(0, 12), (0, 14), (0, 16), (1, 3), (1, 11), (1, 12), (3, 5), (3, 9), (3, 11), (5, 7), (5, 9), (7, 9), (9, 11), (12, 14), (14, 16), (16, 18)],
}

EXPECTED_SMALL = {5: 5, 6: 5, 7: 6, 8: 6, 9: 6, 10: 6, 11: 7, 12: 7, 13: 8}
CATALAN_TRIANGULATIONS = {5: 5, 6: 14, 7: 42, 8: 132, 9: 429, 10: 1430, 11: 4862, 12: 16796, 13: 58786}


def edge(u, v):
    return (u, v) if u < v else (v, u)


def add_edge(E, u, v):
    E.add(edge(u, v))


def degree_counts(E):
    deg = Counter()
    for u, v in E:
        deg[u] += 1
        deg[v] += 1
    return Counter(deg.values())


def spread_two(E):
    counts = degree_counts(E)
    maximum = max(counts)
    return max(sum(counts[d] for d in range(p, p + 3)) for p in range(2, maximum + 1))


def build_H(k):
    n = 18 * k + 2
    E = set()
    for i in range(n):
        add_edge(E, i, (i + 1) % n)
    add_edge(E, n - 3, n - 1)
    c = 9 * k - 9
    for i in range(k - 1):
        a = 9 * i
        b = 18 * k - 1 - 9 * i
        add_edge(E, a, b)
        def local(x):
            return a + x if x <= 9 else b + x - 19
        for x, y in BLOCK:
            add_edge(E, local(x), local(y))
    add_edge(E, c, c + 17)
    for x, y in GAMMA:
        add_edge(E, c + x, c + y)
    return list(range(n)), E


def insert_ear(order, E, position):
    N = len(order)
    position %= N
    u = order[position]
    v = order[(position + 1) % N]
    assert edge(u, v) in E
    w = max(order) + 1
    add_edge(E, u, w)
    add_edge(E, w, v)
    if position == N - 1:
        order.append(w)
    else:
        order.insert(position + 1, w)


def extend_H(k, r):
    order, E = build_H(k)
    c = 9 * k - 9
    for entry in TEMPLATES[r]:
        if isinstance(entry, tuple):
            kind, q = entry
            position = c + q if kind == "c" else len(order) - q
        else:
            position = c + entry
        insert_ear(order, E, position)
    return order, E


def chords_to_graph(n, chords):
    E = set()
    for i in range(n):
        add_edge(E, i, (i + 1) % n)
    for u, v in chords:
        add_edge(E, u, v)
    return E


def chords_cross(a, b, c, d):
    if len({a, b, c, d}) < 4:
        return False
    if a > b:
        a, b = b, a
    return (a < c < b) != (a < d < b)


def verify_polygon_witness(n, chords):
    assert len(chords) == n - 3
    assert len({edge(*e) for e in chords}) == n - 3
    for i, (a, b) in enumerate(chords):
        assert (b - a) % n not in (1, n - 1)
        for c, d in chords[i + 1:]:
            assert not chords_cross(a, b, c, d)
    E = chords_to_graph(n, chords)
    assert len(E) == 2 * n - 3
    return E


@lru_cache(None)
def triangulations(vertices):
    vertices = tuple(vertices)
    m = len(vertices)
    if m <= 3:
        return (frozenset(),)
    a, b = vertices[0], vertices[-1]
    out = []
    for j in range(1, m - 1):
        pivot = vertices[j]
        for left in triangulations(vertices[:j + 1]):
            for right in triangulations(vertices[j:]):
                chords = set(left) | set(right)
                if j > 1:
                    chords.add(edge(a, pivot))
                if j < m - 2:
                    chords.add(edge(pivot, b))
                out.append(frozenset(chords))
    return tuple(dict.fromkeys(out))


def exact_small_value(n):
    families = triangulations(tuple(range(n)))
    assert len(families) == CATALAN_TRIANGULATIONS[n]
    best = n
    for chords in families:
        best = min(best, spread_two(chords_to_graph(n, chords)))
    return best


def target(n):
    return ceil((4 * n + 10) / 9)


def main():
    for n in range(5, 14):
        value = exact_small_value(n)
        assert value == EXPECTED_SMALL[n]
        witness = verify_polygon_witness(n, SMALL_WITNESSES[n])
        assert spread_two(witness) == value
        print(f"n={n}: triangulations={CATALAN_TRIANGULATIONS[n]}, MOP(n,2)={value}")

    for n in range(14, 20):
        witness = verify_polygon_witness(n, SMALL_WITNESSES[n])
        assert spread_two(witness) == target(n)
        print(f"n={n}: explicit triangulation has spread {target(n)}")

    checked = 0
    for k in range(1, 51):
        order0, E0 = build_H(k)
        base = degree_counts(E0)
        assert len(E0) == 2 * len(order0) - 3
        assert base == Counter({2: 8 * k, 3: 2, 5: 8 * k, 6: 2, 8: 2 * k - 2})
        for r in range(18):
            order, E = extend_H(k, r)
            n = 18 * k + 2 + r
            assert len(order) == n
            assert len(E) == 2 * n - 3
            counts = degree_counts(E)
            delta = {d: counts[d] - base[d] for d in set(counts) | set(base) if counts[d] != base[d]}
            assert delta == EXPECTED_DELTA[r]
            assert spread_two(E) == target(n)
            checked += 1
    print(f"ear templates: {checked} parameter pairs verified (k=1..50, r=0..17)")
    print("all checks passed")


if __name__ == "__main__":
    main()
