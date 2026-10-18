"""Finite exhaustive verification of a weighted random one-out tree law.
Only Python standard library is required; uses exact rational arithmetic.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import defaultdict


def test(edges, n):
    edges = [(min(u, v), max(u, v), F(w)) for u, v, w in edges]
    nbr = [[] for _ in range(n)]
    for u, v, w in edges:
        nbr[u].append((v, w)); nbr[v].append((u, w))
    d = [sum(w for v, w in adj) for adj in nbr]
    den = F(1)
    for x in d: den *= x
    def tree(E):
        if len(E) != n-1: return False
        p = list(range(n))
        def find(a):
            while p[a] != a: a = p[a]
            return a
        for u, v in E:
            a, b = find(u), find(v)
            if a == b: return False
            p[a] = b
        return len(set(find(i) for i in range(n))) == 1
    selected = {}
    for z in combinations(edges, n-1):
        pairs = tuple(sorted((u, v) for u, v, w in z))
        if tree(pairs):
            wprod = F(1)
            for u, v, w in z: wprod *= w
            selected[pairs] = (wprod, sum(w for u, v, w in z))
    actual = defaultdict(F)
    for choices in product(*nbr):
        pairs = tuple(sorted(set((min(i, v), max(i, v)) for i, (v, w) in enumerate(choices))))
        if tree(pairs):
            p = F(1)
            for i, (v, w) in enumerate(choices): p *= w / d[i]
            actual[pairs] += p
    for pairs, (wp, csum) in selected.items():
        assert actual[pairs] == wp * csum / den, (pairs, actual[pairs], wp * csum / den)
    assert set(actual) == set(selected)
    A = sum(actual.values()); tau = sum(w for w, c in selected.values())
    mu = sum(w * c for w, c in selected.values()) / tau
    assert A == tau * mu / den
    conditional = {t: p / A for t, p in actual.items()}
    tv = sum(abs(conditional[t] - selected[t][0] / tau) for t in selected) / 2
    exact_tv = sum(selected[t][0] / tau * abs(selected[t][1] - mu) for t in selected) / (2 * mu)
    assert tv == exact_tv
    var = sum(w * (c - mu)**2 for w, c in selected.values()) / tau
    assert sum(conditional[t] * selected[t][1] for t in selected) - mu == var / mu
    low, high = min(w for u, v, w in edges), max(w for u, v, w in edges)
    assert tv * tv * 4 <= high / ((n-1) * low)
    return len(selected), tv, A

if __name__ == '__main__':
    examples = [
        ([(0,1,1),(1,2,2),(0,2,3)],3),
        ([(0,1,1),(1,2,1),(0,2,1)],3),
        ([(0,1,1),(1,2,2),(0,2,3),(2,3,1),(3,4,1),(4,5,2),(3,5,3)],6),
        ([(0,1,2),(1,2,3),(0,2,5),(0,3,1),(1,3,2),(2,3,4)],4),
        ([(0,1,1),(1,2,2),(2,3,3)],4),
        ([(0,1,1)],2),
    ]
    for edges,n in examples:
        trees,tv,event = test(edges,n)
        print('n=',n,'trees=',trees,'TV=',str(tv),'Pr(tree)=',str(event))
    print('All exact finite checks passed.')
