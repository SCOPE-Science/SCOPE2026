"""Independent shortest-path checks and exact integer coefficient checks."""
from math import comb
from itertools import combinations


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def coefficient_formula(r, a):
    assert a in (3, 4) and r >= 1
    if r == 1:
        return [choose(a, k) for k in range(a + 1)]
    n = r * a
    b = [0] * (max(r, a, 4) + 1)
    b[0], b[1], b[2] = 1, n, choose(n, 2)
    if r == 2:
        for k in range(3, a + 1):
            b[k] = 2 * choose(a, k)
        return b
    for k in range(3, len(b)):
        b[k] = (a * choose(r, k) + r * choose(a, k)
                + __import__('math').factorial(k) * choose(a, k) * choose(r, k))
    b[3] += 4 * choose(a, 2) * choose(r, 2)
    b[4] += choose(a, 2) * choose(r, 2)
    return b


def directly_enumerated_coefficients(r, a):
    vertices = list(range(a * r))
    order = len(vertices)
    edges = [[False] * order for _ in vertices]
    for u, v in combinations(vertices, 2):
        partu, labelu = divmod(u, r)
        partv, labelv = divmod(v, r)
        edges[u][v] = edges[v][u] = (partu != partv and labelu != labelv)
    INF = order + 1
    dist = [[0 if i == j else (1 if edges[i][j] else INF) for j in vertices] for i in vertices]
    for k in vertices:
        for i in vertices:
            for j in vertices:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    forbidden = []
    for u, v, w in combinations(vertices, 3):
        if any(dist[x][z] < INF and dist[x][z] == dist[x][y] + dist[y][z]
               for x, y, z in ((u, v, w), (u, w, v), (v, u, w))):
            forbidden.append((1 << u) | (1 << v) | (1 << w))
    counts = [0] * (order + 1)
    for mask in range(1 << order):
        if all((mask & bad) != bad for bad in forbidden):
            counts[mask.bit_count()] += 1
    while len(counts) > 1 and counts[-1] == 0:
        counts.pop()
    return counts, 1 << order


def unimodal(seq):
    decreased = False
    for x, y in zip(seq, seq[1:]):
        if y < x:
            decreased = True
        elif y > x and decreased:
            return False
    return True


def main():
    raw_subsets = 0
    graph_cases = 0
    for a, upto in ((3, 5), (4, 4)):
        for r in range(1, upto + 1):
            expected = coefficient_formula(r, a)
            observed, subsets = directly_enumerated_coefficients(r, a)
            expected = expected[:]
            while len(expected) > 1 and expected[-1] == 0:
                expected.pop()
            assert observed == expected, (a, r, expected, observed)
            raw_subsets += subsets
            graph_cases += 1
    formula_cases = 0
    for a in (3, 4):
        for r in range(1, 1001):
            predicted = (r <= 10 or r >= 18) if a == 3 else (r <= 11 or r >= 40)
            assert unimodal(coefficient_formula(r, a)) == predicted, (a, r)
            formula_cases += 1
    print(f"VERIFICATION_OK independent_graph_cases={graph_cases} inspected_vertex_subsets={raw_subsets} exact_integer_formula_cases={formula_cases} classification_thresholds=a3:11..17,a4:12..39")


if __name__ == '__main__':
    main()
