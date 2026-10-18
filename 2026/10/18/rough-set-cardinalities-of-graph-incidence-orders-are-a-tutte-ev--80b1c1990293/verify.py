#!/usr/bin/env python3
"""Reproducible checks for rough-set counting on dual incidence orders.

No external packages. All calculations use exact integer arithmetic.
"""
from itertools import combinations, combinations_with_replacement
from math import comb


def rough_pairs_hypergraph(n, neighborhoods):
    """Direct enumeration of images (L(S), U(S)) from all possible S."""
    m = len(neighborhoods)
    neigh = [1 << v for v in range(n)]
    for j, h in enumerate(neighborhoods):
        bits = 1 << (n+j)
        for v in h:
            bits |= 1 << v
        neigh.append(bits)
    observed = set()
    for s in range(1 << (n+m)):
        lo = 0
        hi = 0
        for x, nbr in enumerate(neigh):
            if s & nbr == nbr:
                lo |= 1 << x
            if s & nbr:
                hi |= 1 << x
        observed.add((lo, hi))
    return len(observed)


def hypergraph_formula(n, neighborhoods):
    ans = 0
    for t in range(1 << n):
        c = 0
        for h in neighborhoods:
            present = sum((t >> v) & 1 for v in h)
            if present == 0 or present == len(h):
                c += 1
        ans += 1 << c
    return ans


def spin_formula(n, edges):
    result = 0
    for t in range(1 << n):
        count = sum(((t >> u) & 1) == ((t >> v) & 1) for u,v in edges)
        result += 1 << count
    return result


def random_cluster(n, edges):
    count = 0
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        def find(i):
            while parent[i] != i:
                i = parent[i]
            return i
        for j, (u,v) in enumerate(edges):
            if mask >> j & 1:
                parent[find(u)] = find(v)
        count += 1 << len({find(v) for v in range(n)})
    return count


def contraction(n, edges, chosen):
    u,v = edges[chosen]
    assert u != v
    rem = [i for i in range(n) if i != v]
    ren = {x:j for j,x in enumerate(rem)}
    def project(x):
        return ren[u if x == v else x]
    return n-1, [(project(a),project(b)) for j,(a,b) in enumerate(edges) if j != chosen]


def verify():
    general = 0
    direct_subsets = 0
    for n in range(4):
        for m in range(4):
            choices = [frozenset(v for v in range(n) if mask >> v & 1)
                       for mask in range(1 << n)]
            from itertools import product
            for hs in product(choices, repeat=m):
                actual = rough_pairs_hypergraph(n, hs)
                expected = hypergraph_formula(n, hs)
                assert actual == expected, (n,hs,actual,expected)
                general += 1
                direct_subsets += 1 << (n+m)
    graph_cases = 0
    for n in range(5):
        universe = list(combinations(range(n), 2))
        for mask in range(1 << len(universe)):
            es = [p for j,p in enumerate(universe) if mask >> j & 1]
            a = rough_pairs_hypergraph(n, [frozenset(e) for e in es])
            b = spin_formula(n, es)
            c = random_cluster(n, es)
            assert a == b == c, (n,es,a,b,c)
            graph_cases += 1
    graph_complex_cases = 0
    for n in range(1, 4):
        all_edges = list(combinations_with_replacement(range(n), 2))
        for m in range(4):
            for es in combinations_with_replacement(all_edges, m):
                a=spin_formula(n, es)
                b=random_cluster(n, es)
                assert a == b, (n,es,a,b)
                for j,(u,v) in enumerate(es):
                    gone=list(es[:j]+es[j+1:])
                    if u == v:
                        assert a == 2*spin_formula(n,gone)
                    else:
                        q,collapsed=contraction(n,es,j)
                        assert a == spin_formula(n,gone)+spin_formula(q,collapsed)
                graph_complex_cases += 1
    for n in range(1, 9):
        path = [(i,i+1) for i in range(n-1)]
        assert spin_formula(n,path) == 2*3**(n-1)
        if n>=3:
            cycle = path+[(n-1,0)]
            assert spin_formula(n,cycle) == 3**n+1
        kn = list(combinations(range(n),2))
        val = sum(comb(n,r)*2**(comb(r,2)+comb(n-r,2)) for r in range(n+1))
        assert spin_formula(n,kn)==val
    print('VERIFY_OK', 'height_two_hypergraphs='+str(general),
          'hypergraph_subsets='+str(direct_subsets),
          'simple_graphs='+str(graph_cases),
          'multigraph_deletion_contraction='+str(graph_complex_cases),
          'paths_cycles_complete_n_le_8=PASS')

if __name__=='__main__':
    verify()
