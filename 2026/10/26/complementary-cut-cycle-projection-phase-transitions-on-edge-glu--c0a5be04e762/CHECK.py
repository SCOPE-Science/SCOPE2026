"""Exact-rational reproduction of edge-clique-sum cut/cycle projector columns.

Uses only the Python standard library; the derivation for unrestricted parameters
is in RESULT.md. This finite computation is not an all-parameter proof.
"""
from fractions import Fraction as F
from itertools import combinations


def graph(a, b):
    assert a >= 2 and b >= 2
    aa = list(range(2, a + 2))
    bb = list(range(a + 2, a + b + 2))
    edge_set = {tuple(sorted(ij))
                for vertices in ((0, 1, *aa), (0, 1, *bb))
                for ij in combinations(vertices, 2)}
    return a + b + 2, sorted(edge_set), aa, bb


def reduced_inverse(size, edges):
    """Invert a grounded combinatorial Laplacian exactly, independently of formulas."""
    n = size - 1
    a = [[F(0) for _ in range(2 * n)] for _ in range(n)]
    for i in range(n):
        a[i][n + i] = F(1)
    for u, v in edges:
        if u < n:
            a[u][u] += 1
        if v < n:
            a[v][v] += 1
        if u < n and v < n:
            a[u][v] -= 1
            a[v][u] -= 1
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        d = a[k][k]
        a[k] = [z / d for z in a[k]]
        for i in range(n):
            if i == k:
                continue
            d = a[i][k]
            if d:
                a[i] = [x - d * y for x, y in zip(a[i], a[k])]
    return [row[n:] + [F(0)] for row in a] + [[F(0)] * size]


def formula(a, b):
    t = a + b + 2
    def touching(x, y):
        return (F(2*x + 1, x+2) + F(y+1, t),
                1 + F(2*(x-1), x+2) + F(y, t))
    def internal(x):
        return (F(2*(x+1), x+2), 3 - F(6, x+2))
    return {
        'shared': (F(2*(a+b+1), t), 3-F(6, t)),
        'a_touch': touching(a, b),
        'b_touch': touching(b, a),
        'a_internal': internal(a),
        'b_internal': internal(b),
    }


def evaluate(a, b, full=False):
    n, edges, aa, bb = graph(a, b)
    inverse = reduced_inverse(n, edges)
    samples = {'shared': (0, 1), 'a_touch': (0, aa[0]),
               'b_touch': (0, bb[0]), 'a_internal': (aa[0], aa[1]),
               'b_internal': (bb[0], bb[1])}
    reps = {tuple(sorted(e)): key for key, e in samples.items()}
    expected = formula(a, b)
    tested = 0
    for u, v in (edges if full else samples.values()):
        potentials = [inverse[i][u] - inverse[i][v] for i in range(n)]
        q = sum(abs(potentials[i] - potentials[j]) for i, j in edges)
        diagonal = potentials[u] - potentials[v]
        p = 1 + q - 2*diagonal
        if full:
            if u in (0,1) and v in (0,1):
                key = 'shared'
            elif (u in (0,1)) and v in aa or (v in (0,1)) and u in aa:
                key = 'a_touch'
            elif (u in (0,1)) and v in bb or (v in (0,1)) and u in bb:
                key = 'b_touch'
            elif u in aa and v in aa:
                key = 'a_internal'
            elif u in bb and v in bb:
                key = 'b_internal'
            else:
                raise AssertionError('unrecognized edge orbit')
        else:
            key = reps[tuple(sorted((u, v)))]
        assert (q, p) == expected[key], (a, b, key, (q, p), expected[key])
        tested += 1
    assert max(v[0] for v in expected.values()) == max(expected['a_touch'][0], expected['b_touch'][0])
    assert max(v[1] for v in expected.values()) == max(expected[k][1] for k in ('shared', 'a_touch', 'b_touch'))
    return tested


def main():
    configs = 0
    columns = 0
    all_edges = 0
    for a in range(2, 6):
        for b in range(2, 6):
            full = (a <= 5 and b <= 5)
            n, edges, _, _ = graph(a, b)
            count = evaluate(a, b, full=full)
            configs += 1
            columns += count
            if full:
                all_edges += len(edges)
    for a, b in [(2, 9), (3, 8), (7, 5), (8, 3)]:
        columns += evaluate(a, b)
        configs += 1
    for a in range(2, 35):
        for b in range(2, 35):
            f = formula(a, b)
            t = a+b+2
            ca, pa = f['a_touch']
            cb, pb = f['b_touch']
            assert ca-cb == F((a-b)*(a+b+2-a*b), (a+2)*(b+2)*t)
            assert pa-pb == F((a-b)*(4*a+4*b+8-a*b), (a+2)*(b+2)*t)
            assert pa-f['shared'][1] == F(b*(a-4), (a+2)*t)
            assert pb-f['shared'][1] == F(a*(b-4), (b+2)*t)
            assert ca-f['shared'][0] == F(b*(a-1), (a+2)*t)
            assert ca-f['a_internal'][0] == F(b*(a+1), (a+2)*t)
            assert ca < 3 and cb < 3 and pa < 4 and pb < 4
    print('EDGE_CLIQUE_SUM_EXACT_OK graph_configurations=%d projection_columns=%d exhaustive_edge_columns=%d comparison_cases=%d' % (configs, columns, all_edges, 33*33))


if __name__ == '__main__':
    main()
