"""Independent finite checks for P3-convex sets of one-subdivided graphs.

This program enumerates the actual convex subsets from adjacency, compares them
with the general matching decomposition and complete-host closed expression,
and checks the exponential-generating-function recurrence.
"""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def polynomial_from_matching(host_n, host_edges):
    host_edges = tuple(tuple(sorted(e)) for e in host_edges)
    edge_set = set(host_edges)
    counts = Counter()
    for vertices_mask in range(1 << host_n):
        chosen = {v for v in range(host_n) if (vertices_mask >> v) & 1}
        outside = set(range(host_n)) - chosen
        mandatory = sum(e[0] in chosen and e[1] in chosen for e in host_edges)
        free_edges = [e for e in host_edges if e[0] in outside and e[1] in outside]
        for mmask in range(1 << len(free_edges)):
            matching = [e for i, e in enumerate(free_edges) if (mmask >> i) & 1]
            used = {v for e in matching for v in e}
            if len(used) != 2 * len(matching):
                continue
            residual = [v for v in outside if v not in used]
            poly = Counter({len(chosen) + mandatory + len(matching): 1})
            for v in residual:
                d = sum(tuple(sorted((v, u))) in edge_set for u in chosen)
                following = Counter()
                for deg, c in poly.items():
                    following[deg] += c
                    following[deg + 1] += d * c
                poly = following
            counts.update(poly)
    return +counts


def direct(host_n, host_edges):
    edges = tuple(host_edges)
    adjacency = [[] for _ in range(host_n + len(edges))]
    for idx, (u, v) in enumerate(edges):
        adjacency[u].append(host_n + idx)
        adjacency[v].append(host_n + idx)
        adjacency[host_n + idx] = [u, v]
    counts = Counter()
    maxima = []
    for mask in range(1 << len(adjacency)):
        if any(not (mask >> v & 1) and sum((mask >> w) & 1 for w in neighbors) > 1
               for v, neighbors in enumerate(adjacency)):
            continue
        size = mask.bit_count()
        counts[size] += 1
        if size < len(adjacency):
            if not maxima or size > maxima[0].bit_count():
                maxima = [mask]
            elif size == maxima[0].bit_count():
                maxima.append(mask)
    return +counts, maxima


def formula_kn(n):
    count = Counter()
    for u in range(n + 1):
        w = n-u
        for j in range(w//2 + 1):
            coeff = comb(n, u) * factorial(w)//(2**j * factorial(j) * factorial(w-2*j))
            for t in range(w-2*j+1):
                count[u+comb(u, 2)+j+t] += coeff*comb(w-2*j, t)*u**t
    return +count


def egf_coeff(n):
    """Coefficient of t^n/n! in exp(t + t^2/2 + t exp(t))."""
    a = [1]
    for m in range(n):
        # d/dt exponent = 1+t + (1+t)exp(t)
        # derivative k has value: 2 if k=0, 3 if k=1, k+1 if k>=2.
        coefficient = lambda k: 2 if k == 0 else (3 if k == 1 else k+1)
        a.append(sum(comb(m, k)*coefficient(k)*a[m-k] for k in range(m+1)))
    return a[n]


def main():
    hosts = 0
    for n in range(1, 5):
        pairs = list(combinations(range(n), 2))
        for mask in range(1 << len(pairs)):
            edges = [pair for idx, pair in enumerate(pairs) if mask >> idx & 1]
            actual, _ = direct(n, edges)
            expected = polynomial_from_matching(n, edges)
            assert actual == expected, (n, mask, actual, expected)
            hosts += 1
    # Host K_n with all 2^(n+binom(n,2)) convexity candidates, n=2,...,6
    for n in range(2, 7):
        edges = list(combinations(range(n), 2))
        actual, maxima = direct(n, edges)
        expected = formula_kn(n)
        assert actual == expected, (n, actual, expected)
        assert sum(actual.values()) == egf_coeff(n)
        assert len(maxima) == n*(n-1)
        assert maxima[0].bit_count() == n + comb(n-1, 2)
        assert all(sum((mask >> v) & 1 for v in range(n)) == n-1 for mask in maxima)
        print('K', n, 'count', sum(actual.values()), 'max_proper', maxima[0].bit_count(),
              'extremizers', len(maxima))
    # EGF coefficients cross-checked against the direct closed sum beyond brute force.
    for n in range(0, 31):
        assert sum(formula_kn(n).values()) == egf_coeff(n), n
    print('VERIFY_OK general_hosts=', hosts, 'complete_hosts=5', 'egf_orders=31')

if __name__ == '__main__':
    main()
