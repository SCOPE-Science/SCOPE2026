"""Exact rational enumerations for tree-incidence richness rarefaction.

Run: python3 verify.py (Python standard library only). No random sampling.
"""
from itertools import product, combinations
from collections import Counter, defaultdict
from fractions import Fraction
from math import comb


def prufer_tree(code, n):
    deg = [1] * n
    for x in code:
        deg[x] += 1
    edges = []
    for x in code:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((min(leaf, x), max(leaf, x)))
        deg[leaf] -= 1
        deg[x] -= 1
    a, b = (i for i in range(n) if deg[i] == 1)
    edges.append((min(a, b), max(a, b)))
    return tuple(edges)


def wedge_count(edges, n):
    d = [0] * n
    for u, v in edges:
        d[u] += 1
        d[v] += 1
    return sum(comb(x, 2) for x in d)


def rarefaction_distribution(edges, n, k):
    hist = Counter()
    for chosen in combinations(range(n), k):
        S = set(chosen)
        richness = sum(u in S or v in S for u, v in edges)
        hist[richness] += 1
    return hist


def formula(n, m, w, k):
    h = n-k
    denom = comb(n, h)
    p = {j: Fraction(comb(n-j, h-j), denom) if h >= j else Fraction(0)
         for j in (2, 3, 4)}
    mean = m*(1-p[2])
    var = m*p[2] + m*(m-1)*p[4] + 2*w*(p[3]-p[4]) - m*m*p[2]*p[2]
    return mean, var


def check():
    total_trees, total_marginal_cases, total_site_subsets = 0, 0, 0
    deg_profile = defaultdict(lambda: defaultdict(int))
    for n in range(4, 8):
        for code in product(range(n), repeat=n-2):
            E = prufer_tree(code, n)
            w = wedge_count(E, n)
            assert n-2 <= w <= comb(n-1, 2), (n, E, w)
            total_trees += 1
            deg_profile[n][w] += 1
            for k in range(n+1):
                hist = rarefaction_distribution(E, n, k)
                total_site_subsets += sum(hist.values())
                total_marginal_cases += 1
                den = sum(hist.values())
                mean = sum(a*c for a, c in hist.items())
                square = sum(a*a*c for a, c in hist.items())
                mu, var = formula(n, len(E), w, k)
                assert Fraction(mean, den) == mu, (n, k, E, mu)
                assert Fraction(square, den)-mu*mu == var, (n, k, E, var)
                if 1 <= k <= n-3:
                    deg = Counter(t for e in E for t in e)
                    if w == n-2:
                        assert max(deg.values()) == 2  # a connected degree-2 tree is a path
                    if w == comb(n-1, 2):
                        assert max(deg.values()) == n-1  # equality is a star
        print('n', n, 'W classes and labeled counts', dict(sorted(deg_profile[n].items())))
    A = ((0, 1), (1, 3), (0, 2), (2, 4), (0, 5))
    B = ((0, 1), (1, 2), (2, 3), (0, 4), (0, 5))
    assert wedge_count(A, 6) == wedge_count(B, 6) == 5
    hA, hB = rarefaction_distribution(A, 6, 2), rarefaction_distribution(B, 6, 2)
    print('A', sorted(hA.items()), 'B', sorted(hB.items()))
    assert hA != hB
    assert formula(6, 5, 5, 2) == (Fraction(3), Fraction(2, 3))
    assert {j: hA[j] for j in sorted(hA)} == {2: 5, 3: 5, 4: 5}
    assert {j: hB[j] for j in sorted(hB)} == {2: 4, 3: 8, 4: 2, 5: 1}
    assert hB[5] == 1 and hA[5] == 0
    def third_central(hist):
        mu = Fraction(sum(x*c for x,c in hist.items()), sum(hist.values()))
        return sum((Fraction(x)-mu)**3*c for x,c in hist.items())/sum(hist.values())
    assert third_central(hB)-third_central(hA) == Fraction(2,5)
    # Infinite witness: attach the same t additional leaves to vertex zero.
    # The two laws continue to differ at richness two for two sampled sites.
    for t in range(0, 10):
        n = 6 + t
        extra = tuple((0, v) for v in range(6, n))
        ea, eb = A + extra, B + extra
        assert wedge_count(ea, n) == wedge_count(eb, n) == comb(n-3, 2)+2
        for k in range(n+1):
            assert formula(n, n-1, wedge_count(ea, n), k) == formula(n, n-1, wedge_count(eb, n), k)
        ha, hb = rarefaction_distribution(ea, n, 2), rarefaction_distribution(eb, n, 2)
        assert ha[2] - hb[2] == 1, (n, ha, hb)
    for n in range(4, 6):
        # At n<=5, the wedge value uniquely determines the degree profile and tree type.
        profiles = defaultdict(set)
        for code in product(range(n), repeat=n-2):
            E = prufer_tree(code, n)
            d = Counter(t for pair in E for t in pair)
            profiles[wedge_count(E, n)].add(tuple(sorted(d.values())))
        assert all(len(q)==1 for q in profiles.values()), profiles
    print('VERIFY_OK', 'trees', total_trees, 'tree-sample-size_cases', total_marginal_cases,
          'site-subsets', total_site_subsets)

if __name__ == '__main__':
    check()
