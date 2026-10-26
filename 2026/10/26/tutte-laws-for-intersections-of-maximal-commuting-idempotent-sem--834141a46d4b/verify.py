"""Independent finite-field checks of incidence-monoid Boolean subsemilattices.

Only Python standard library is required. Matrices are sparse matrices over prime fields.
"""
from itertools import product, combinations
from collections import Counter
from math import comb


def add(a, b, q):
    return tuple((x + y) % q for x, y in zip(a, b))


def mul(a, b, pairs, q):
    lookup = {z: i for i, z in enumerate(pairs)}
    return tuple(sum(a[lookup[(x, z)]] * b[lookup[(z, y)]]
                     for z in range(len(set(t[0] for t in pairs)))
                     if (x, z) in lookup and (z, y) in lookup) % q
                 for x, y in pairs)


def run_case(n, edges, q):
    # Pairs already include transitive closure.
    edges = tuple(sorted(edges))
    pairs = tuple((i, i) for i in range(n)) + edges
    z = (0,) * len(pairs)
    one = tuple(int(i == j) for i, j in pairs)
    units = []
    idems = []
    diag = []
    for vals in product(range(q), repeat=len(pairs)):
        if vals[:n] == (1,)*n:
            units.append(vals)
        if mul(vals, vals, pairs, q) == vals:
            idems.append(vals)
        if all(t == 0 for t in vals[n:]) and all(t in (0, 1) for t in vals[:n]):
            diag.append(vals)
    assert len(units) == q**len(edges)
    assert len(diag) == 2**n
    maximal = []
    for g in units:
        inv = next(h for h in units if mul(g, h, pairs, q) == one and mul(h,g,pairs,q) == one)
        conj = frozenset(mul(mul(g, e, pairs, q), inv, pairs, q) for e in diag)
        maximal.append(conj)
        assert len(conj) == 2**n
        # A maximal semilattice is its own commuting-idempotent centralizer.
        assert set(e for e in idems if all(mul(e, f, pairs, q) == mul(f, e, pairs, q) for f in conj)) == set(conj)
    assert len(set(maximal)) == q**len(edges)
    d = frozenset(diag)
    histogram = Counter(len(d & t) for t in maximal)
    # Independently count edge support subgraphs, without any matrix operations.
    expected = Counter()
    for bits in product((0, 1), repeat=len(edges)):
        roots = list(range(n))
        def find(x):
            while roots[x] != x:
                x=roots[x]
            return x
        for (u,v),b in zip(edges,bits):
            if b:
                roots[find(u)] = find(v)
        c = len({find(i) for i in range(n)})
        expected[2**c] += (q-1)**sum(bits)
    assert histogram == expected, (histogram, expected)
    # Direct enumeration of maximal cliques for tiny cases.
    if len(idems) <= 55:
        commutes = [[mul(a, b, pairs, q) == mul(b, a, pairs, q) for b in idems] for a in idems]
        N=len(idems)
        # Standard Bron-Kerbosch, with largest neighborhoods selected as pivot.
        neighbors=[{j for j in range(N) if j!=i and commutes[i][j]} for i in range(N)]
        cliques=[]
        def bron(R,P,X):
            if not P and not X:
                cliques.append(frozenset(idems[i] for i in R));return
            pivot=max(P|X, key=lambda u:len(P & neighbors[u])) if P|X else None
            for v in list(P - (neighbors[pivot] if pivot is not None else set())):
                bron(R|{v},P & neighbors[v],X & neighbors[v]);P.remove(v);X.add(v)
        bron(set(),set(range(N)),set())
        assert set(cliques) == set(maximal), (len(cliques),len(set(maximal)))
    print('CASE',n,'q',q,'strict_intervals',len(edges), 'idempotents',len(idems), 'maxima',len(set(maximal)), 'intersection_histogram', sorted(histogram.items()))


if __name__=='__main__':
    run_case(2, [(0,1)],2)
    run_case(2, [(0,1)],3)
    run_case(3, [(0,1),(0,2)],2)    # V poset
    run_case(3, [(0,1),(1,2),(0,2)],2) # chain
    run_case(4, [(0,2),(0,3),(1,2),(1,3)],2) # complete height-two
    run_case(4, [(0,1),(0,2),(0,3),(1,3),(2,3)],2) # diamond
    print('VERIFY_OK')
