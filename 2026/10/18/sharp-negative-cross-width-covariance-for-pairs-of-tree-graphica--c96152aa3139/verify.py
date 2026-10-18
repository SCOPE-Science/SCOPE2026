#!/usr/bin/env python3
"""Reproduce exact graph-pair overlap and directional-width checks."""
import itertools
import math
import random

DELTA = 1 / 3 + (2 * math.sqrt(3) - 4) / math.pi
LAMBDA = 4 / 3 + (4 - 4 * math.sqrt(3)) / math.pi
MU2 = 4 / math.pi


def prufer_edges(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    edges = set()
    for x in code:
        leaf = next(v for v in range(n) if degree[v] == 1)
        edges.add(tuple(sorted((x, leaf))))
        degree[x] -= 1
        degree[leaf] -= 1
    leaves = [v for v in range(n) if degree[v] == 1]
    edges.add(tuple(leaves))
    return frozenset(edges)


def optimal_pair(n):
    a = {(0, 1), (0, 2), (1, 3)}
    b = {(0, 3), (1, 2), (2, 3)}
    for v in range(4, n):
        a.add((0, v))
        b.add((2, v))
    return frozenset(a), frozenset(b)


def edge_statistics(g, h, n):
    dg = [0] * n
    dh = [0] * n
    for u, v in g:
        dg[u] += 1
        dg[v] += 1
    for u, v in h:
        dh[u] += 1
        dh[v] += 1
    s = sum(a * b for a, b in zip(dg, dh))
    c = len(g.intersection(h))
    return s, c


def analytical_covariance(g, h, n):
    d = n - 1
    er2 = 2 * math.exp(2 * (math.lgamma((d + 1) / 2) - math.lgamma(d / 2)))
    s, c = edge_statistics(g, h, n)
    return MU2 * (d - d * d / er2) + (DELTA * s + LAMBDA * c) / d


def test_all_pairs():
    total_pairs = 0
    total_equality = 0
    for n in range(4, 7):
        trees = [prufer_edges(seq, n) for seq in itertools.product(range(n), repeat=n - 2)]
        min_score = DELTA * (3 * n - 4)
        count = 0
        for g in trees:
            for h in trees:
                s, c = edge_statistics(g, h, n)
                score = DELTA * s + LAMBDA * c
                assert score >= min_score - 1e-10
                if abs(score - min_score) < 1e-10:
                    assert s == 3 * n - 4 and c == 0
                    count += 1
                else:
                    assert s > 3 * n - 4 or c > 0
        a, b = optimal_pair(n)
        assert edge_statistics(a, b, n) == (3 * n - 4, 0)
        assert count > 0
        total_pairs += len(trees) ** 2
        total_equality += count
        print('ORDER', n, 'LABELED_TREES', len(trees), 'ORDERED_PAIRS', len(trees) ** 2, 'MINIMIZERS', count)
    return total_pairs, total_equality


def width(g, u):
    return sum(abs(u[i] - u[j]) for i, j in g)


def verify_vertices():
    rng = random.Random(351)
    tests = 0
    for n in range(4, 8):
        g, _ = optimal_pair(n)
        for _ in range(40):
            u = [rng.gauss(0, 1) for _ in range(n)]
            mean = sum(u) / n
            u = [x - mean for x in u]
            norm = math.sqrt(sum(x * x for x in u))
            u = [x / norm for x in u]
            vertex_objectives = []
            for signs in itertools.product([-0.5, 0.5], repeat=n - 1):
                vertex_objectives.append(sum(sign * (u[i] - u[j]) for sign, (i, j) in zip(signs, sorted(g))))
            actual = max(vertex_objectives) - min(vertex_objectives)
            assert abs(actual - width(g, u)) < 5e-12
            tests += 1
    return tests


def verify_monte_carlo():
    rng = random.Random(786)
    outcomes = []
    for n in [4, 12]:
        g, h = optimal_pair(n)
        count = 150000
        sx = sy = sxy = 0.0
        for _ in range(count):
            z = [rng.gauss(0, 1) for _ in range(n)]
            avg = sum(z) / n
            z = [x - avg for x in z]
            radius = math.sqrt(sum(x*x for x in z))
            u = [x / radius for x in z]
            x, y = width(g, u), width(h, u)
            sx += x
            sy += y
            sxy += x * y
        observed = sxy / count - (sx * sy) / count ** 2
        expected = analytical_covariance(g, h, n)
        print('SPHERE_SAMPLE',n,'EXPECTED',round(expected,8),'EMPIRICAL',round(observed,8))
        assert expected < 0 and abs(expected - observed) < 0.025
        outcomes.append((n,expected,observed))
    return outcomes


def main():
    assert DELTA > 0 and LAMBDA > 0
    exact_pairs, equal_pairs = test_all_pairs()
    vertex_tests = verify_vertices()
    verify_monte_carlo()
    for n in (4, 5, 6, 12, 50, 1000):
        g, h = optimal_pair(n)
        assert edge_statistics(g, h, n) == (3*n-4, 0)
    assert 3*DELTA-2/math.pi < -0.14
    print('EXACT_ORDERED_PAIRS', exact_pairs)
    print('EXACT_MINIMIZING_PAIRS', equal_pairs)
    print('VERTEX_SUPPORT_TESTS', vertex_tests)
    print('VERIFY_OK')

if __name__=='__main__':
    main()
