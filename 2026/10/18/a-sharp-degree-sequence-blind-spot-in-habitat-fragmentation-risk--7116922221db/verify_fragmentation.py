"""Exact finite checks for component-count moments of vertex-thinned habitat trees."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb


def prufer_tree(code, n):
    if n == 1:
        return ()
    degrees = [1] * n
    for v in code:
        degrees[v] += 1
    edges = []
    for v in code:
        u = next(u for u in range(n) if degrees[u] == 1)
        edges.append(tuple(sorted((u, v))))
        degrees[u] -= 1
        degrees[v] -= 1
    a, b = [v for v in range(n) if degrees[v] == 1]
    edges.append(tuple(sorted((a, b))))
    return tuple(sorted(edges))


def canonical_tree(edges, n):
    adj = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    def rooted(u, parent):
        return "(" + "".join(sorted(rooted(v, u) for v in adj[u] if v != parent)) + ")"
    return min(rooted(v, -1) for v in range(n))


def degree_signature(edges, n):
    d = [0] * n
    for u, v in edges:
        d[u] += 1
        d[v] += 1
    return tuple(sorted(d))


def component_distribution_edge_count(edges, n, k):
    d = Counter()
    for s in combinations(range(n), k):
        S = set(s)
        count_edges = sum((u in S and v in S) for u, v in edges)
        d[k - count_edges] += 1
    return d


def component_distribution_dsu(edges, n, k):
    d = Counter()
    for s in combinations(range(n), k):
        parent = {v: v for v in s}
        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v
        for u, v in edges:
            if u in parent and v in parent:
                parent[root(u)] = root(v)
        d[len({root(v) for v in s})] += 1
    return d


def moment(dist, k, r):
    return Fraction(sum(val * (c ** r) for c, val in dist.items()), sum(dist.values()))


def pfall(k, n, r):
    if r > k:
        return Fraction(0)
    if r == 0:
        return Fraction(1)
    a = b = 1
    for j in range(r):
        a *= (k-j)
        b *= (n-j)
    return Fraction(a, b)


def fixed_sample_variance(edges, n, k):
    # C=k-E_induced, so Var(C)=Var(E_induced).
    a2, a3, a4 = [pfall(k, n, r) if r <= n else Fraction(0) for r in (2, 3, 4)]
    W = sum(comb(x, 2) for x in degree_signature(edges, n))
    t = n - 1
    return t*a2 + 2*W*a3 + 2*(comb(t, 2)-W)*a4 - (t*a2)**2


def check():
    counts = {}
    for n in range(1, 7):
        rep = {}
        codes = product(range(n), repeat=max(0, n-2)) if n > 2 else [()]
        for code in codes:
            E = prufer_tree(code, n)
            rep.setdefault(canonical_tree(E, n), E)
        counts[n] = len(rep)
        by_degree = defaultdict(list)
        for E in rep.values():
            by_degree[degree_signature(E, n)].append(E)
            for k in range(n+1):
                D = component_distribution_edge_count(E, n, k)
                assert D == component_distribution_dsu(E, n, k)
                assert sum(D.values()) == comb(n, k)
                mu = moment(D, k, 1)
                v = moment(D, k, 2)-mu**2
                assert mu == k-Fraction(k*(k-1), n)
                assert v == fixed_sample_variance(E, n, k)
        if n <= 5:
            assert all(len(v) == 1 for v in by_degree.values())
        if n == 6:
            twins = [v for v in by_degree.values() if len(v) > 1]
            assert len(twins) == 1 and len(twins[0]) == 2
            A, B = twins[0]
            assert degree_signature(A, n) == (1,1,1,2,2,3)
            for k in range(n+1):
                D1 = component_distribution_edge_count(A, n, k)
                D2 = component_distribution_edge_count(B, n, k)
                assert (D1 != D2) == (k == 4)
                for power in (1,2):
                    assert moment(D1, k, power) == moment(D2, k, power)
            print('TWIN_A',A)
            print('TWIN_B',B)
            print('DIST_A',dict(sorted(component_distribution_edge_count(A, n, 4).items())))
            print('DIST_B',dict(sorted(component_distribution_edge_count(B, n, 4).items())))
            for power in (1,2,3):
                differences=[]
                for k in range(7):
                    d1=component_distribution_edge_count(A, n, k)
                    d2=component_distribution_edge_count(B, n, k)
                    differences.append(sum((d1.get(c,0)-d2.get(c,0))*c**power for c in set(d1)|set(d2)))
                assert differences == ([0]*7 if power <= 2 else [0,0,0,0,6,0,0])
                print('RAW_MOMENT_COEFFICIENT_DIFFERENCE_POWER',power,differences)
            print('CENTRAL_THIRD_MOMENT_DIFFERENCE_GIVEN_K4',Fraction(2,5))
    assert counts == {1:1,2:1,3:1,4:2,5:3,6:6}
    print('CLASSES',counts)
    # Bernoulli site-survival cross-check, independent of the fixed-size covariance derivation.
    for n in range(1,7):
        codes = product(range(n), repeat=max(0,n-2)) if n>2 else [()]
        representatives = {}
        for code in codes:
            edges = prufer_tree(code,n)
            representatives.setdefault(canonical_tree(edges,n),edges)
        for edges in representatives.values():
            W = sum(comb(d,2) for d in degree_signature(edges,n))
            for p in (Fraction(1,3),Fraction(1,2),Fraction(3,4)):
                raw1=raw2=Fraction(0)
                for k in range(n+1):
                    law = component_distribution_dsu(edges,n,k)
                    for c,num in law.items():
                        prob=num*p**k*(1-p)**(n-k)
                        raw1+=prob*c
                        raw2+=prob*c*c
                predicted_mean=n*p-(n-1)*p*p
                predicted_var=(n*p*(1-p)+(n-1)*p*p*(1-p*p)
                    -4*(n-1)*p*p*(1-p)+2*W*p**3*(1-p))
                assert raw1 == predicted_mean
                assert raw2-raw1**2 == predicted_var
    print('INDEPENDENT_BERNOULLI_MOMENT_CHECKS_PASSED')
    # Independently check the sharp extremal range for a variety of n,k.
    for n in range(4,10):
        path = tuple((i,i+1) for i in range(n-1))
        star = tuple((0,i) for i in range(1,n))
        for k in range(n+1):
            va=fixed_sample_variance(path,n,k)
            vb=fixed_sample_variance(star,n,k)
            a3 = pfall(k,n,3)
            a4 = pfall(k,n,4) if n>=4 else Fraction(0)
            assert vb-va == (n-2)*(n-3)*(a3-a4)
            if 3<=k<=n-1: assert vb>va
            else: assert vb==va
    print('SHARP_PATH_STAR_VARIANCE_CHECKS',sum(n+1 for n in range(4,10)))
    print('ALL_CHECKS_PASSED')

if __name__ == '__main__':
    check()
