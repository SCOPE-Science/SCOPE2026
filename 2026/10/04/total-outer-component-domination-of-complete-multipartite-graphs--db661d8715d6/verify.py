#!/usr/bin/env python3
from itertools import combinations
from math import comb


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for rest in partitions(n - a, a):
            yield (a,) + rest


def build_vertices(parts):
    return [(i, j) for i, n in enumerate(parts) for j in range(n)]


def component_count(parts, C_indices):
    if not C_indices:
        return 0
    verts = build_vertices(parts)
    support = {verts[v][0] for v in C_indices}
    if len(support) >= 2:
        return 1
    return len(C_indices)


def is_total_dominating(parts, D):
    verts = build_vertices(parts)
    for v, (pi, _) in enumerate(verts):
        if not any(u != v and verts[u][0] != pi for u in D):
            return False
    return True


def literal_tokcds(parts, D, k):
    N = sum(parts)
    C = [v for v in range(N) if v not in D]
    return bool(C) and is_total_dominating(parts, D) and component_count(parts, C) == k


def profile_characterization(parts, D, k):
    r = len(parts)
    verts = build_vertices(parts)
    d = [0] * r
    for v in D:
        d[verts[v][0]] += 1
    c = [parts[i] - d[i] for i in range(r)]
    p = sum(x > 0 for x in d)
    q = sum(x > 0 for x in c)
    ctot = sum(c)
    if p < 2 or ctot == 0:
        return False
    if k == 1:
        return q >= 2 or ctot == 1
    return q == 1 and ctot == k


def formula_counts(parts):
    r = len(parts)
    N = sum(parts)
    beta = [n if r >= 3 else n - 1 for n in parts]
    counts = {}
    # k=1 polynomial by D-size.
    for s in range(N + 1):
        total = comb(N, s)
        if s == 0:
            non_total = 1
        else:
            non_total = sum(comb(n, s) for n in parts if s <= n)
        total_dom = total - non_total
        if s == N:
            total_dom -= 1  # complement must be nonempty
        j = N - s
        disconnected_complement = 0
        if j >= 2:
            disconnected_complement = sum(comb(n, j) for n, b in zip(parts, beta) if j <= b)
        c = total_dom - disconnected_complement
        if c:
            counts[(1, s)] = c
    # k>=2: the complement is exactly k vertices in one part.
    for k in range(2, max(parts) + 1):
        b = sum(comb(n, k) for n, lim in zip(parts, beta) if k <= lim)
        if b:
            counts[(k, N - k)] = b
    return counts


def gamma_formula(parts, k):
    r = len(parts)
    N = sum(parts)
    L = max(parts)
    if k == 1:
        if r >= 3:
            return 2
        a, b = sorted(parts)
        if a >= 2 or b == 2:
            return 2
        return b  # K_{1,b}, b>=3
    if r >= 3:
        return N - k if 2 <= k <= L else 0
    return N - k if 2 <= k < L else 0


def brute_counts(parts):
    N = sum(parts)
    counts = {}
    for mask in range(1 << N):
        D = {v for v in range(N) if mask & (1 << v)}
        for k in range(1, N + 1):
            if literal_tokcds(parts, D, k):
                counts[(k, len(D))] = counts.get((k, len(D)), 0) + 1
    return counts


def brute_gamma(parts, k):
    N = sum(parts)
    vals = []
    for mask in range(1 << N):
        D = {v for v in range(N) if mask & (1 << v)}
        if literal_tokcds(parts, D, k):
            vals.append(len(D))
    return min(vals) if vals else 0

profiles = subset_checks = criterion_checks = coefficient_checks = gamma_checks = 0
boundary_checks = 0
for N in range(3, 11):
    for parts in partitions(N):
        if len(parts) < 2:
            continue
        profiles += 1
        expected = formula_counts(parts)
        actual = {}
        for mask in range(1 << N):
            D = {v for v in range(N) if mask & (1 << v)}
            subset_checks += 1
            for k in range(1, N + 1):
                a = literal_tokcds(parts, D, k)
                b = profile_characterization(parts, D, k)
                criterion_checks += 1
                assert a == b, (parts, D, k, a, b)
                if a:
                    actual[(k, len(D))] = actual.get((k, len(D)), 0) + 1
        keys = set(actual) | set(expected)
        for key in keys:
            coefficient_checks += 1
            assert actual.get(key, 0) == expected.get(key, 0), (parts, key, actual.get(key, 0), expected.get(key, 0))
        for k in range(1, N + 1):
            gamma_checks += 1
            assert brute_gamma(parts, k) == gamma_formula(parts, k), (parts, k, brute_gamma(parts, k), gamma_formula(parts, k))

# Boundary where Proposition 3.2 of Rad--Volkmann (2016) states a positive value for K_{m,n} at k=n.
# Under the defining total-domination condition, these cases have no TO_nCDS.
for m in range(2, 7):
    for n in range(m, 8):
        parts = (m, n)
        boundary_checks += 1
        assert brute_gamma(parts, n) == 0, (parts, n, brute_gamma(parts, n))
# In particular K_{2,2}=C4 has gamma_tc^2=0, agreeing with Theorem 2.6 of the same paper.
assert brute_gamma((2, 2), 2) == 0

print(
    'VERIFY_OK '
    f'profiles={profiles} subset_checks={subset_checks} criterion_checks={criterion_checks} '
    f'coefficient_checks={coefficient_checks} gamma_checks={gamma_checks} '
    f'boundary_checks={boundary_checks} max_order=10'
)
