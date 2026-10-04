#!/usr/bin/env python3
from itertools import combinations


def integer_partitions(n):
    out = []
    def rec(rem, lo, cur):
        if rem == 0:
            if len(cur) >= 2:
                out.append(tuple(cur))
            return
        for x in range(lo, rem + 1):
            rec(rem - x, x, cur + [x])
    rec(n, 1, [])
    return out


def vertices(parts):
    return [(i, j) for i, n in enumerate(parts) for j in range(n)]


def is_k_limited_dominating(parts, mask, k):
    verts = vertices(parts)
    N = len(verts)
    chosen = [(mask >> v) & 1 for v in range(N)]
    if not any(chosen):
        return False
    for v in range(N):
        if chosen[v]:
            continue
        pv = verts[v][0]
        if not any(chosen[u] and verts[u][0] != pv for u in range(N)):
            return False
    for u in range(N):
        if not chosen[u]:
            continue
        pu = verts[u][0]
        outside_neighbors = sum(
            1 for v in range(N)
            if not chosen[v] and verts[v][0] != pu
        )
        if outside_neighbors > k:
            return False
    return True


def brute_gamma(parts, k):
    N = sum(parts)
    best = N + 1
    tested = 0
    for mask in range(1, 1 << N):
        tested += 1
        size = mask.bit_count()
        if size >= best:
            continue
        if is_k_limited_dominating(parts, mask, k):
            best = size
    if best == N + 1:
        raise AssertionError((parts, k, 'no feasible set'))
    return best, tested


def theorem_gamma(parts, k):
    parts = tuple(sorted(parts))
    N = sum(parts)
    feasible = []
    for t in range(0, N - k - 1):
        if t < parts[-2] and sum(min(n, t) for n in parts) <= k + t:
            feasible.append(t)
    if not feasible:
        raise AssertionError((parts, k, 'empty threshold set'))
    T = max(feasible)
    return N - k - T, T


def published_biclique(m, n, k):
    if not (2 <= m <= n and 1 <= k < n):
        raise ValueError
    return 1 + n - k if m <= k else m + n - 2 * k


def balanced_formula(r, m, k):
    return r * m - k - (k // (r - 1))


def main():
    types = 0
    cases = 0
    subsets = 0
    for N in range(3, 12):
        for parts in integer_partitions(N):
            types += 1
            Delta = N - min(parts)
            for k in range(1, Delta):
                predicted, T = theorem_gamma(parts, k)
                actual, tested = brute_gamma(parts, k)
                subsets += tested
                cases += 1
                if actual != predicted:
                    raise AssertionError((parts, k, actual, predicted, T))

    biclique_cases = 0
    for m in range(2, 9):
        for n in range(m, 9):
            for k in range(1, n):
                predicted, _ = theorem_gamma((m, n), k)
                expected = published_biclique(m, n, k)
                biclique_cases += 1
                if predicted != expected:
                    raise AssertionError(('biclique', m, n, k, predicted, expected))

    balanced_cases = 0
    for r in range(2, 7):
        for m in range(1, 7):
            Delta = (r - 1) * m
            for k in range(1, Delta):
                predicted, _ = theorem_gamma((m,) * r, k)
                expected = balanced_formula(r, m, k)
                balanced_cases += 1
                if predicted != expected:
                    raise AssertionError(('balanced', r, m, k, predicted, expected))

    print(
        'ALL CHECKS PASSED; '
        f'multipartite_types={types}; parameter_cases={cases}; '
        f'subsets_tested={subsets}; max_order=11; '
        f'biclique_checks={biclique_cases}; balanced_checks={balanced_cases}'
    )


if __name__ == '__main__':
    main()
