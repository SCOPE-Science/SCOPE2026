#!/usr/bin/env python3
"""Independent exact checks for two-colour rainbow connection on K_2 square K_n."""
from math import comb
from random import Random


def product_coefficients(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def power_coefficients(a, exponent):
    out = [1]
    for _ in range(exponent):
        out = product_coefficients(out, a)
    return out


def predicted(n):
    result = [0] * (n * n + 1)
    for b in range(n + 1):
        p = [1]
        p = product_coefficients(p, power_coefficients([0, 2, 1], comb(n - b, 2)))
        p = product_coefficients(p, power_coefficients([1, 2], comb(b, 2)))
        p = product_coefficients(p, power_coefficients([1, 0, 1], b * (n - b)))
        for i, a in enumerate(p):
            result[i + b] += comb(n, b) * a
    return result


def graph(n):
    edges = []
    for a in range(2):
        for i in range(n):
            for j in range(i + 1, n):
                edges.append((a * n + i, a * n + j))
    for j in range(n):
        edges.append((j, n + j))
    adjacency = [[None for _ in range(2 * n)] for _ in range(2 * n)]
    for edge_index, (u, v) in enumerate(edges):
        adjacency[u][v] = edge_index
        adjacency[v][u] = edge_index
    return edges, adjacency


def direct_condition(mask, n, adjacency):
    """Check actual graph paths, without using the pair-factor formula."""
    for u in range(2 * n):
        for v in range(u + 1, 2 * n):
            if adjacency[u][v] is not None:
                continue
            connected = False
            for w in range(2 * n):
                e = adjacency[u][w]
                f = adjacency[w][v]
                if e is not None and f is not None and ((mask >> e) & 1) != ((mask >> f) & 1):
                    connected = True
                    break
            if not connected:
                return False
    return True


def local_condition(mask, n):
    """Test necessary/sufficient local pair restrictions directly from bits."""
    row_edges = n * (n - 1) // 2
    for i in range(n):
        for j in range(i + 1, n):
            idx = i * (2*n - i - 1) // 2 + (j-i-1)
            a = (mask >> idx) & 1
            b = (mask >> (row_edges+idx)) & 1
            ci = (mask >> (2*row_edges+i)) & 1
            cj = (mask >> (2*row_edges+j)) & 1
            if ci == cj:
                if a == b == ci:
                    return False
            elif a != b:
                return False
    return True


def verify():
    for n in range(2, 5):
        edges, adj = graph(n)
        assert len(edges) == n*n
        actual = [0] * (n*n+1)
        for mask in range(1 << len(edges)):
            direct = direct_condition(mask, n, adj)
            assert direct == local_condition(mask, n), (n, mask)
            if direct:
                actual[mask.bit_count()] += 1
        expected = predicted(n)
        assert actual == expected, (n, actual, expected)
        assert next(i for i,x in enumerate(actual) if x) == n-1
        assert actual[n-1] == n*n
        print('FULL_GRAPH_EXHAUSTION_OK', n, 1 << len(edges), sum(actual), actual[n-1])
    rng = Random(20261101)
    for n in range(5, 9):
        edges, adj = graph(n)
        for _ in range(25000):
            mask = rng.getrandbits(len(edges))
            assert direct_condition(mask, n, adj) == local_condition(mask, n)
        coeffs = predicted(n)
        assert coeffs[n-1] == n*n
        assert all(t == coeffs[n*n - i] for i, t in enumerate(coeffs))
        assert sum(coeffs) == sum(comb(n,b) * 3**(comb(n-b,2)+comb(b,2)) * 2**(b*(n-b)) for b in range(n+1))
        print('RANDOM_GRAPH_AND_SYMMETRY_OK', n, 25000, coeffs[n-1], sum(coeffs))
    print('VERIFY_OK')

if __name__ == '__main__':
    verify()
