"""Direct exhaustive checks for the minimal-Roman corona classification.
No external libraries. Run with: python verify_roman_corona.py
The finite checks are corroboration, not a proof for arbitrary order.
"""
from itertools import product
from collections import Counter
from math import comb


def graph_edges(n, mask):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    return [edge for i, edge in enumerate(pairs) if mask & (1 << i)]


def adjacencies(n, edges):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    return adj


def formula(n, edges):
    adj = adjacencies(n, edges)
    counts = Counter()
    for mask in range(1 << n):
        X = {v for v in range(n) if mask & (1 << v)}
        boundary = (set().union(*(adj[v] for v in X)) - X) if X else set()
        remainder = n - len(X) - len(boundary)
        counts[2*n - len(boundary)] += 2 ** remainder
    return counts


def brute(n, edges):
    adj = adjacencies(2 * n, edges + [(v, n + v) for v in range(n)])
    def roman(f):
        return all(f[v] != 0 or any(f[u] == 2 for u in adj[v])
                   for v in range(2*n))
    counts = Counter()
    for f in product(range(3), repeat=2*n):
        if not roman(f):
            continue
        minimal = True
        for v, label in enumerate(f):
            if label > 0:
                g = list(f)
                g[v] -= 1
                if roman(g):
                    minimal = False
                    break
        if minimal:
            counts[sum(f)] += 1
    return counts


def domination_number(n, edges):
    adj = adjacencies(n, edges)
    for k in range(1, n + 1):
        for mask in range(1 << n):
            if mask.bit_count() != k:
                continue
            D = {v for v in range(n) if mask & (1 << v)}
            if all(v in D or bool(adj[v] & D) for v in range(n)):
                return k
    raise AssertionError('not found')


def component_orders(n, edges):
    adj = adjacencies(n, edges)
    unseen = set(range(n))
    sizes = []
    while unseen:
        v = unseen.pop()
        part = {v}
        fringe = [v]
        while fringe:
            u = fringe.pop()
            for w in adj[u]:
                if w in unseen:
                    unseen.remove(w)
                    part.add(w)
                    fringe.append(w)
        sizes.append(len(part))
    return sizes


def bipartite_independent_set_count(n, edges):
    adj = adjacencies(n, edges)
    count = 0
    for left in range(1 << n):
        X = {v for v in range(n) if left & (1 << v)}
        forbidden = X | (set().union(*(adj[v] for v in X)) if X else set())
        for right in range(1 << n):
            Y = {v for v in range(n) if right & (1 << v)}
            if not (Y & forbidden):
                count += 1
    return count


def biclique_formula(a, b):
    n = a + b
    counts = Counter({2*n:2**n})
    counts[2*a+b] += 3**a - 2**a
    counts[a+2*b] += 3**b - 2**b
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            counts[n+i+j] += comb(a, i) * comb(b, j)
    return counts


def run():
    graph_count = 0
    checked_labelings = 0
    minimal_count = 0
    for n in range(1, 5):
        for mask in range(1 << (n*(n-1)//2)):
            edges = graph_edges(n, mask)
            expected = formula(n, edges)
            direct = brute(n, edges)
            assert expected == direct, ('polynomial', n, edges, expected, direct)
            assert min(expected) == n + domination_number(n, edges)
            top = 1
            for order in component_orders(n, edges):
                top *= (2**order + 1)
            assert expected[2*n] == top
            assert sum(expected.values()) == bipartite_independent_set_count(n, edges)
            graph_count += 1
            checked_labelings += 3**(2*n)
            minimal_count += sum(direct.values())
    for n in (5,):
        for mask in (0, 1, 3, 11, 33, 85, 170, 255, 341, 511, 1023):
            edges = graph_edges(n, mask)
            expected = formula(n, edges)
            direct = brute(n, edges)
            assert expected == direct, ('polynomial', n, edges, expected, direct)
            assert min(expected) == n + domination_number(n, edges)
            top = 1
            for order in component_orders(n, edges):
                top *= (2**order + 1)
            assert expected[2*n] == top
            graph_count += 1
            checked_labelings += 3**(2*n)
            minimal_count += sum(direct.values())
    for a in range(1, 5):
        for b in range(1, 5):
            n = a+b
            edges = [(u, v) for u in range(a) for v in range(a, n)]
            assert formula(n, edges) == biclique_formula(a, b), (a, b)
    print('VERIFY_OK graphs=%d labelings=%d minimal_functions=%d '
          'full_polynomials=PASS extremal_weights=PASS independent_set_bridge=PASS '
          'bicliques=16' % (graph_count, checked_labelings, minimal_count))

if __name__ == '__main__':
    run()
