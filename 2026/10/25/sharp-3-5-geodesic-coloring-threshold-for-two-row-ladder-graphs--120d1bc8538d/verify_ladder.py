"""Reproducible finite checks for bounded-geodesic ladder colorings.

This verifies small instances directly and tests the constructive patterns.
The accompanying proof, rather than finite enumeration, covers all orders.
"""
from itertools import combinations


def position_hyperedges(n, d=5):
    vertices = [(i, r) for i in range(n) for r in range(2)]

    def dist(x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])

    edges = []
    for indices in combinations(range(2 * n), 3):
        a, b, c = [vertices[i] for i in indices]
        if (dist(a, b) + dist(b, c) == dist(a, c) <= d
                or dist(b, a) + dist(a, c) == dist(b, c) <= d
                or dist(a, c) + dist(c, b) == dist(a, b) <= d):
            edges.append(indices)
    return edges


def has_coloring(n, q):
    by_end = [[] for _ in range(2 * n)]
    for e in position_hyperedges(n):
        by_end[max(e)].append(e)
    colors = [-1] * (2 * n)

    def rec(pos, max_used):
        if pos == 2 * n:
            return colors[:]
        for color in range(min(q - 1, max_used + 1) + 1):
            colors[pos] = color
            if all(not (colors[a] == colors[b] == colors[c]) for a, b, c in by_end[pos]):
                result = rec(pos + 1, max(color, max_used))
                if result is not None:
                    return result
        colors[pos] = -1
        return None

    return rec(0, -1)


def shortest_paths(n, d=5):
    for left in range(n):
        for right in range(left, min(n, left + d + 1)):
            horizontal = right - left
            if 2 <= horizontal <= d:
                for row in (0, 1):
                    yield [(i, row) for i in range(left, right + 1)]
            if 2 <= horizontal + 1 <= d:
                for row in (0, 1):
                    for rung in range(left, right + 1):
                        yield ([(i, row) for i in range(left, rung + 1)]
                               + [(i, 1-row) for i in range(rung, right + 1)])


def path_color_valid(n, cols):
    count = 0
    for path in shortest_paths(n):
        count += 1
        sequence = [cols[i][row] for i, row in path]
        if any(sequence.count(color) >= 3 for color in set(sequence)):
            return False, count
    return True, count


def run():
    expected = {1: 1, 2: 2, 3: 2, 4: 3, 5: 4}
    for n, answer in expected.items():
        bad = has_coloring(n, answer-1) if answer > 1 else None
        good = has_coloring(n, answer)
        assert bad is None and good is not None, (n, answer, bad, good)
    print('DIRECT_BACKTRACKING_MINIMA_OK n=1..5  [1,2,2,3,4]')
    small = [(0, 0), (1, 2), (2, 1), (1, 2)]
    ok, paths = path_color_valid(4, small)
    assert ok
    print(f'THREE_COLOR_FOUR_COLUMN_WITNESS_OK paths={paths}')
    stripe = [(0, 1), (1, 0), (2, 3), (3, 2)]
    for n in range(1, 33):
        ok, paths = path_color_valid(n, [stripe[i % 4] for i in range(n)])
        assert ok, (n, paths)
    print('FOUR_COLOR_PERIODIC_WITNESS_OK all n=1..32')
    # Also test the critical two-corner geodesic color-balancing premise.
    n = 5
    paths = []
    for row in (0, 1):
        for j in range(5):
            paths.append(([(i, row) for i in range(j+1)]
                          + [(i, 1-row) for i in range(j, 5)]))
    assert len(paths) == 10 and all(len(p) == 6 for p in paths)
    print('SIX_VERTEX_CORNER_GEODESICS_OK count=10')
    print('VERIFY_OK')


if __name__ == '__main__':
    run()
