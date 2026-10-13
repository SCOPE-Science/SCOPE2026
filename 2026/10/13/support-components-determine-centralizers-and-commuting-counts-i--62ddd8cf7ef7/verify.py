#!/usr/bin/env python3
"""Self-contained exhaustive checks for graph Lie commuting and adjoint-rank formulas.
Requires only Python 3 standard library; no third-party data.
"""
from itertools import product
from collections import Counter
from math import comb


def graph_edges(n, mask):
    return [e for j, e in enumerate((i, k) for i in range(n) for k in range(i + 1, n)) if (mask >> j) & 1]


def components_support(n, edges, support):
    parent = list(range(n))
    def find(a):
        while parent[a] != a:
            a = parent[a]
        return a
    for i, j in edges:
        if (support >> i) & 1 and (support >> j) & 1:
            parent[find(i)] = find(j)
    return len({find(i) for i in range(n) if (support >> i) & 1})


def support_rank(n, edges, support):
    c = components_support(n, edges, support)
    outside_free = sum(not (support >> j) & 1 and not any((i == j and (support >> k) & 1) or (k == j and (support >> i) & 1) for i, k in edges) for j in range(n))
    return n - c - outside_free


def Q_special(n, edges, q):
    return sum((q-1)**s.bit_count() * (q+1)**components_support(n, edges, s) for s in range(1 << n))


def support_enumerator(n, edges, q):
    return Counter({}) + sum_counters(Counter({support_rank(n, edges, s): (q-1)**s.bit_count()}) for s in range(1 << n))


def sum_counters(items):
    result = Counter()
    for item in items:
        result.update(item)
    return result


def determinant_edge_zero(a, b, edges, mul, sub):
    return all(sub(mul(a[i], b[j]), mul(a[j], b[i])) == 0 for i, j in edges)


def rank_field(matrix, q, mul, sub, inv):
    if not matrix: return 0
    a = [list(row) for row in matrix]
    nrows, ncols = len(a), len(a[0]); row = 0
    for col in range(ncols):
        pivot = next((i for i in range(row, nrows) if a[i][col]), None)
        if pivot is None: continue
        a[row], a[pivot] = a[pivot], a[row]
        t = inv(a[row][col]); a[row] = [mul(t, z) for z in a[row]]
        for i in range(nrows):
            if i != row and a[i][col]:
                t = a[i][col]
                a[i] = [sub(a[i][k], mul(t, a[row][k])) for k in range(ncols)]
        row += 1
        if row == nrows: break
    return row


def test_field(q, maxn):
    if q == 4:
        # GF(2)[alpha]/(alpha^2+alpha+1), integers represent binary coefficients.
        def mul(a, b):
            x = 0
            for i in range(2):
                for j in range(2):
                    if (a >> i) & 1 and (b >> j) & 1: x ^= (1 << (i + j))
            if x & 4: x ^= 7
            return x
        def sub(a, b): return a ^ b
        def inv(a):
            assert a
            return next(x for x in range(1, 4) if mul(a, x) == 1)
    else:
        assert q in (2, 3)
        def mul(a, b): return (a * b) % q
        def sub(a, b): return (a - b) % q
        def inv(a): return pow(a, -1, q)

    graphs = 0
    for n in range(maxn + 1):
        for gmask in range(1 << comb(n, 2)):
            edges = graph_edges(n, gmask)
            vectors = list(product(range(q), repeat=n))
            expected = Q_special(n, edges, q)
            brute = sum(determinant_edge_zero(a, b, edges, mul, sub) for a in vectors for b in vectors)
            assert expected == brute, (q, n, edges, brute, expected)
            predicted_rank_counts = support_enumerator(n, edges, q)
            actual = Counter()
            for x in vectors:
                # A row for each edge, columns for vertices, computing [x, y]_edge.
                matrix = []
                for i, j in edges:
                    row = [0]*n
                    row[j] = x[i]; row[i] = sub(0, x[j]); matrix.append(row)
                actual[rank_field(matrix, q, mul, sub, inv)] += 1
            assert actual == predicted_rank_counts, (q,n,edges,actual,predicted_rank_counts)
            assert sum(predicted_rank_counts.values()) == q**n
            graphs += 1
    return graphs


def forest_polynomial(n, edges, q):
    # Recursion on rooted components, including isolated vertices.
    neighbors = [[] for _ in range(n)]
    for a, b in edges:
        neighbors[a].append(b); neighbors[b].append(a)
    visited = set()
    def dfs(v, p):
        assert v not in visited
        visited.add(v)
        children = [dfs(w, v) for w in neighbors[v] if w != p]
        inactive, active_fixed = 1, q-1
        for a,b in children:
            inactive *= a + (q+1)*b
            active_fixed *= a+b
        return inactive, active_fixed
    result=1
    for v in range(n):
        if v not in visited:
            a,b=dfs(v,-1)
            result *= a+(q+1)*b
    return result


def all_trees(maxn):
    # Enumerate all labeled trees through Prüfer codes.
    for n in range(1, maxn+1):
        if n == 1:
            yield n, []
            continue
        for prufer in product(range(n), repeat=n-2):
            degrees = [1]*n
            for v in prufer: degrees[v] += 1
            edges = []
            for v in prufer:
                u = min(i for i in range(n) if degrees[i] == 1)
                edges.append((u,v)); degrees[u] -= 1; degrees[v] -= 1
            u,v=[i for i in range(n) if degrees[i] == 1]
            edges.append((u,v))
            yield n, edges


def main():
    stats=[]
    for q,maxn in [(2,4),(3,4),(4,3)]:
        stats.append((q,test_field(q,maxn)))
    # Numerical form of polynomial equality tested for many graphs and q;
    # global proof relies on two independent counts, not on this finite test.
    for n in range(6):
        for mask in range(1 << comb(n,2)):
            edges=graph_edges(n,mask)
            for q in (2,3,5):
                lhs=sum((q-1)**s.bit_count()*q**(n-support_rank(n,edges,s)) for s in range(1<<n))
                rhs=Q_special(n,edges,q)
                assert lhs==rhs, (n,edges,q,lhs,rhs)
    tree_n=0
    for n,edges in all_trees(6):
        for q in (2,3,5):
            assert forest_polynomial(n,edges,q)==Q_special(n,edges,q)
        tree_n+=1
    print('VERIFY_OK direct brute-force fields and graph counts',stats,
          'all simple graphs n<=5 support/direction identity q=2,3,5',
          'trees checked',tree_n,'char2 extension GF4 included')

if __name__=='__main__':
    main()
