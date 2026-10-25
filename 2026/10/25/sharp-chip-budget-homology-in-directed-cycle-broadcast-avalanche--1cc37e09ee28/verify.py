"""Standalone finite checks for directed cycle broadcast avalanche complexes.

Mathematical proof is in RESULT.md; these exhaustive finite tests are corroboration.
Requires Python 3.9+ standard library only.
"""
from itertools import combinations, product
from math import gcd, lcm, prod


def graph_data(lengths):
    k = len(lengths)
    vertices = [('b', 0)] + [(i, j) for i, n in enumerate(lengths) for j in range(n)]
    adj = {v: [] for v in vertices}
    adj[('b', 0)] = [(i, 0) for i in range(k)]
    for i, n in enumerate(lengths):
        for j in range(n):
            adj[(i, j)] = [(i, (j + 1) % n)]
    return vertices, adj


def simulate(lengths):
    vertices, adj = graph_data(lengths)
    k = len(lengths)
    chips = {v: 0 for v in vertices}
    chips[('b', 0)] = k
    L = lcm(*lengths)
    result = []
    # Complete cycle of recurrent states: t = 0 through L inclusive.
    for t in range(L + 1):
        firing = frozenset(v for v in vertices if chips[v] >= len(adj[v]))
        assert all(len(adj[v]) > 0 for v in vertices)
        result.append(firing)
        new = chips.copy()
        for v in firing:
            new[v] -= len(adj[v])
            for w in adj[v]:
                new[w] += 1
        assert sum(new.values()) == k and min(new.values()) >= 0
        chips = new
    assert result[0] == frozenset({('b', 0)})
    assert len(result[1:]) == L
    assert len(set(result[1:])) == L
    return result


def predicted_facets(lengths):
    k = len(lengths)
    g = gcd(*lengths)
    # Generalized CRT: consistency precisely common residue modulo g
    assert all(gcd(lengths[i], lengths[j]) == g
               for i in range(k) for j in range(i + 1, k))
    pieces = []
    for r in range(g):
        parts = [[(i, j) for j in range(n) if j % g == r]
                 for i, n in enumerate(lengths)]
        pieces.extend(frozenset(t) for t in product(*parts))
    return [frozenset({('b', 0)})] + pieces


def faces(facets):
    result = {frozenset()}
    for facet in facets:
        vs = list(facet)
        for a in range(1, len(vs)+1):
            result.update(frozenset(t) for t in combinations(vs, a))
    return result


def rank_mod_p(columns, row_index, p):
    pivots = {}
    for c in columns:
        col = {}
        for row, coefficient in c.items():
            v = coefficient % p
            if v:
                col[row_index[row]] = v
        while col:
            r = max(col)
            if r not in pivots:
                inv = pow(col[r], -1, p)
                pivots[r] = {i: (v * inv) % p for i,v in col.items()}
                break
            a = col[r]
            for i,v in pivots[r].items():
                nv = (col.get(i, 0) - a*v) % p
                if nv:
                    col[i] = nv
                else:
                    col.pop(i, None)
    return len(pivots)


def betti_mod_p(facets, prime):
    fs = faces(facets)
    levels = {}
    for s in fs:
        if s:
            levels.setdefault(len(s)-1, []).append(tuple(sorted(s, key=str)))
    levels = {d: sorted(set(items), key=str) for d,items in levels.items()}
    max_d = max(levels)
    ranks = [0]*(max_d+2)
    for d in range(1,max_d+1):
        rows = {frozenset(x):j for j,x in enumerate(levels[d-1])}
        columns=[]
        for simplex in levels[d]:
            columns.append({frozenset(simplex[:j]+simplex[j+1:]): (-1)**j
                            for j in range(len(simplex))})
        ranks[d]=rank_mod_p(columns,rows,prime)
    betti={d:len(levels[d])-ranks[d]-ranks[d+1] for d in levels}
    return betti


def check(lengths, compute_homology=True):
    k=len(lengths)
    assert k >= 2 and all(n>=3 for n in lengths)
    g=gcd(*lengths)
    assert all(gcd(a,b)==g for a,b in combinations(lengths,2))
    m=[n//g for n in lengths]
    assert all(x>=2 for x in m)
    observed = simulate(lengths)
    predicted = predicted_facets(lengths)
    assert set(observed)==set(predicted)
    assert len(predicted)==1+prod(lengths)//(g**(k-1))
    assert all(len(x)==k for x in predicted[1:])
    if compute_homology:
        expected={0:g,k-1:g*prod(x-1 for x in m)}
        for p in (2,3,5,7):
            got=betti_mod_p(predicted,p)
            reduced={d:val-(d==0) for d,val in got.items()}
            assert all(v==expected.get(d,0) for d,v in reduced.items()), (lengths,p,reduced,expected)
        print('PASS',lengths,'components',g+1,'top-Betti',expected[k-1],
              'facets',len(predicted),'over fields F2,F3,F5,F7')
    else:
        print('PASS',lengths,'CRT and full firing-facet equality',len(predicted))

if __name__=='__main__':
    for ns in ((3,4),(6,10),(9,15),(3,4,5),(4,6,10),(6,10,14)):
        check(ns)
    for ns in ((3,5,7),(2*3,2*5,2*7),(3,5,7,11)):
        check(ns,compute_homology=False)
    print('ALL CHECKS PASSED')
