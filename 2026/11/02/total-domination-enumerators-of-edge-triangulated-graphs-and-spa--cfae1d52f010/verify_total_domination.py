"""Independent finite checks of total domination on edge-triangulation graphs.

Usage: python3 verify_total_domination.py
Uses only the Python standard library.
The all-order statements rely on the accompanying combinatorial proof, not
on the bounded enumeration performed here.
"""
from collections import Counter
from itertools import combinations
from math import comb


def build_triangle_expansion(n, edges):
    """Neighbor bitsets of R(G); original vertices are 0,...,n-1."""
    A = [0] * (n + len(edges))
    for j, (u, v) in enumerate(edges):
        w = n + j
        for r, s in ((u, v), (u, w), (v, w)):
            A[r] |= 1 << s
            A[s] |= 1 << r
    return A


def direct_polynomials(n, edges):
    A = build_triangle_expansion(n, edges)
    N = len(A)
    original_mask = (1 << n) - 1
    all_sets, minimal_sets = Counter(), Counter()
    for D in range(1 << N):
        if not all(D & A[v] for v in range(N)):
            continue
        key = ((D & original_mask).bit_count(), (D >> n).bit_count())
        all_sets[key] += 1
        minimal = True
        rem = D
        while rem:
            bit = rem & -rem
            rem -= bit
            D0 = D - bit
            if all(D0 & A[v] for v in range(N)):
                minimal = False
                break
        if minimal:
            minimal_sets[key] += 1
    return all_sets, minimal_sets, 1 << N


def universal_formula(n, edges):
    """Coefficient formula via vertex covers and disjoint support requirements."""
    degree = [0] * n
    neighbors = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        neighbors[u] |= 1 << v
        neighbors[v] |= 1 << u
    if any(d == 0 for d in degree):
        return Counter()
    out = Counter()
    m = len(edges)
    for S in range(1 << n):
        if any(not (S & (1 << u) or S & (1 << v)) for u, v in edges):
            continue
        I = [v for v in range(n) if S & (1 << v) and not (S & neighbors[v])]
        used = sum(degree[v] for v in I)
        # Exactly one of 0..d(v) selected incident edges is forbidden: zero.
        f = Counter({0: 1})
        for v in I:
            next_f = Counter()
            for j, c in f.items():
                for k in range(1, degree[v] + 1):
                    next_f[j + k] += c * comb(degree[v], k)
            f = next_f
        for j, c in f.items():
            for k in range(m - used + 1):
                out[(S.bit_count(), j + k)] += c * comb(m - used, k)
    return +out


def biclique(a, b):
    return a + b, [(i, a + j) for i in range(a) for j in range(b)]


def bivariate_formula(a, b):
    """Closed all-TDS polynomial for R(K_{a,b})."""
    result = Counter()
    m = a * b
    # S=A and S=B, each selected original vertex needs a triangle neighbor.
    for k in range(a, m + 1):
        # coefficient of y^k in ((1+y)^b-1)^a
        c = sum((-1)**(a-j) * comb(a, j) * comb(b*j, k)
                for j in range(a+1) if b*j >= k)
        if c:
            result[(a, k)] += c
    for k in range(b, m + 1):
        c = sum((-1)**(b-j) * comb(b, j) * comb(a*j, k)
                for j in range(b+1) if a*j >= k)
        if c:
            result[(b, k)] += c
    # S=A plus nonempty B-subset, and the transpose case.
    for t in range(1, b + 1):
        for k in range(m+1):
            result[(a+t, k)] += comb(b, t)*comb(m, k)
    for s in range(1, a + 1):
        for k in range(m+1):
            result[(b+s, k)] += comb(a, s)*comb(m, k)
    # S=A union B was counted twice.
    for k in range(m+1):
        result[(a+b, k)] -= comb(m, k)
    return +result


def minimal_formula(a, b):
    return +Counter({(a+1, 0):b, (b+1, 0):a, (a, a):b**a, (b, b):a**b}) if a!=b else \
        Counter({(a+1, 0):a+b, (a, a):b**a+a**b})


def run():
    general, bicliques, tested = 0, 0, 0
    for n in range(2, 5):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [edge for j, edge in enumerate(pairs) if mask & (1 << j)]
            if any(not any(v in edge for edge in edges) for v in range(n)):
                continue
            direct, _, size = direct_polynomials(n, edges)
            assert direct == universal_formula(n, edges), (n, edges, direct)
            general += 1
            tested += size
    for a in range(2, 5):
        for b in range(2, 6):
            n, edges = biclique(a,b)
            if n+len(edges) > 19:
                continue
            direct, minimal, size = direct_polynomials(n, edges)
            expected_min = minimal_formula(a, b)
            assert minimal == expected_min, (a,b,'minimal',minimal,expected_min)
            assert direct == bivariate_formula(a,b), (a,b,'all',direct,bivariate_formula(a,b))
            assert direct == universal_formula(n, edges), (a,b,'universal',direct)
            bicliques += 1
            tested += size
    arithmetic = 0
    for a in range(2,13):
        for b in range(2,13):
            F = minimal_formula(a,b)
            assert sum(F.values()) == a+b + b**a + a**b
            assert set(x+y for x,y in F) == {a+1,b+1,2*a,2*b}
            if a == 2 and b >= 5:
                assert set(x+y for x,y in F) == {3,4,b+1,2*b}
            arithmetic += 1
    print(f'VERIFY_OK general_graphs={general} biclique_graphs={bicliques} '
          f'direct_vertex_subsets={tested} arithmetic_pairs={arithmetic}')

if __name__ == '__main__':
    run()
