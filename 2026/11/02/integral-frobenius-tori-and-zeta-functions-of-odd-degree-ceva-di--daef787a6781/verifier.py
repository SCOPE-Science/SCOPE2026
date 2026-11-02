#!/usr/bin/env python3
"""Exact standalone checks for a family of reduced Fermat/Ceva line divisors.
No package dependencies. Exhaustive finite graph and prime-field checks; the
proof for arbitrary odd n is combinatorial and is given separately.
"""
from collections import deque


def graph(n):
    L = [(c, i) for c in 'ABC' for i in range(n)]
    P = [('P', c) for c in 'ABC'] + [('M', i, j) for i in range(n) for j in range(n)]
    E = []
    for c, i in L:
        E.append(((c, i), ('P', c)))
        for j in range(n):
            if c == 'A':
                p = ('M', i, j)
            elif c == 'B':
                p = ('M', j, i)
            else:
                p = ('M', j, (-i-j) % n)
            E.append(((c, i), p))
    assert len(E) == len(set(E)) == 3*n*(n+1)
    assert len(L) == 3*n and len(P) == n*n+3
    adj = {v: set() for v in L + P}
    for u, v in E:
        adj[u].add(v)
        adj[v].add(u)
    assert all(len(adj[l]) == n+1 for l in L)
    assert all(len(adj[p]) == (n if p[0] == 'P' else 3) for p in P)
    return L, P, E, adj


def flip(v, n):
    if v[0] == 'P':
        return v
    if v[0] == 'M':
        return ('M', -v[1] % n, -v[2] % n)
    return (v[0], -v[1] % n)


def graph_check(n):
    assert n >= 3 and n % 2 == 1
    L, P, E, adj = graph(n)
    Eset = set(E)
    def ef(e): return (flip(e[0], n), flip(e[1], n))
    assert all(ef(e) in Eset for e in E)
    fixed_v = set(v for v in L + P if flip(v, n) == v)
    fixed_e = set(e for e in E if ef(e) == e)
    assert len(fixed_v) == 7 and len(fixed_e) == 6
    # Verify the fixed subgraph is one connected acyclic graph.
    reached = {next(iter(fixed_v))}
    while True:
        new = reached | {v for u, v in fixed_e if u in reached} | {u for u, v in fixed_e if v in reached}
        if new == reached: break
        reached = new
    assert reached == fixed_v
    # Construct a Frobenius-stable spanning tree by adjoining free vertex
    # orbits two at a time. Every fixed edge belongs to the starting tree.
    visited, tree = set(fixed_v), set(fixed_e)
    while len(visited) < len(L) + len(P):
        candidates = [(u, v) for (u, v) in E if u in visited and v not in visited]
        candidates += [(v, u) for (u, v) in E if v in visited and u not in visited]
        assert candidates, 'connectedness or invariant BFS failed'
        a, b = candidates[0]
        e = (a, b) if (a, b) in Eset else (b, a)
        assert b != flip(b, n) and flip(b, n) not in visited
        assert e != ef(e) and ef(e) in Eset
        tree.add(e); tree.add(ef(e))
        visited.add(b); visited.add(flip(b, n))
    assert len(tree) == len(L) + len(P) - 1
    assert all(ef(e) in tree for e in tree)
    chords = Eset - tree
    assert len(chords) == 2*n*n-2
    assert not any(ef(e) == e for e in chords)
    assert all(ef(e) in chords for e in chords)
    assert len({frozenset((e, ef(e))) for e in chords}) == n*n-1
    # The fundamental-cycle basis is permuted in n^2-1 disjoint pairs.
    assert 3*n*(n+1) - (3*n+n*n+3) + 1 == 2*n*n-2
    print('GRAPH_CERT', n, 'components', 3*n, 'singular_supports', n*n+3,
          'edges', len(E), 'fixed_vertices', 7, 'fixed_edges', 6,
          'paired_fundamental_cycles', n*n-1)


def field_point_count(n, q):
    assert q > n and q % n in (1, n-1)
    points = [(1, a, b) for a in range(q) for b in range(q)]
    points += [(0, 1, b) for b in range(q)] + [(0, 0, 1)]
    def on_curve(x, y, z):
        return ((pow(x, n, q) - pow(y, n, q)) *
                (pow(y, n, q) - pow(z, n, q)) *
                (pow(z, n, q) - pow(x, n, q))) % q == 0
    actual = sum(on_curve(*point) for point in points)
    predicted = 3*n*q+3-2*n*n if q % n == 1 else 3*q+1
    assert actual == predicted, (n, q, actual, predicted)
    print('POINTS_CERT', 'n', n, 'q', q, 'actual', actual, 'predicted', predicted)


def zeta_check(n, q):
    # Exponent lists [degree d, exponent e] for products (1-a*T^d)^e.
    if q % n == 1:
        terms = [(1, 1, 2*n*n-3), (1, q, -3*n)]
    else:
        terms = [(2, 1, n*n-1), (1, 1, -1),
                 (1, q, -3), (2, q*q, -3*(n-1)//2)]
    # logarithmic differentiation: a factor (1-a*T^d)^e
    # contributes -d*e*a^(m/d) when d divides m.
    for m in range(1, 9):
        N = sum(-d*e*pow(a, m//d) for d,a,e in terms if m%d == 0)
        expected = (3*n*pow(q, m)+3-2*n*n if (pow(q, m, n) == 1)
                    else 3*pow(q, m)+1)
        assert N == expected, (n, q, m, N, expected)
    print('ZETA_CERT', n, q, 'eight_extension_degrees')


def main():
    for n in (3, 5, 7, 9, 11, 13, 15):
        graph_check(n)
    for n, q in ((5,11),(5,19),(7,13),(7,29),(9,17),(9,19),
                 (11,23),(11,43),(13,53),(13,103)):
        field_point_count(n, q)
        zeta_check(n, q)
    print('VERIFY_OK')

if __name__ == '__main__': main()
