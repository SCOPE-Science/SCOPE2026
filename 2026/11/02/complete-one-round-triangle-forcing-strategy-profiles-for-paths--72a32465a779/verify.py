"""Self-contained exhaustive checks for one-round triangle-forcing strategy enumerators.

Uses only the Python standard library; run: python3 verify.py.
"""
from collections import Counter
from itertools import combinations
from math import comb


def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def path_profile(n, k, j):
    if k == 0:
        return int(j == 0)
    if not 0 <= j < k:
        return 0
    return choose(k - 1, j) * choose(n - 2*k + 1, k - j)


def cycle_profile(n, k, j):
    if k == 0:
        return int(j == 0)
    if 2*k > n or j < 0 or j > k:
        return 0
    if n == 2*k:
        return 2 if j == k else 0
    if j == k:
        return 0
    return n * choose(k, j) * choose(n - 2*k - 1, k - j - 1) // k


def graph_edges(n, cycle):
    ed = {(i, i+1) for i in range(n-1)}
    if cycle:
        ed.add((0, n-1))
    return tuple(sorted(ed))


def all_matchings(edges):
    for k in range(len(edges)//2 + 2):
        for selection in combinations(edges, k):
            vs = [v for e in selection for v in e]
            if len(set(vs)) == 2*k:
                yield selection


def triangles_after_growth(n, edges, matching):
    endpoints = {v for e in matching for v in e}
    survivors = set(edges).difference(matching)
    # Any triangle in a path/cycle grown from a matching contains the new vertex.
    tris = []
    for (a, b) in survivors:
        if a in endpoints and b in endpoints:
            tris.append(frozenset(((a, b), (a, n), (b, n))))
    return tris


def check_partition_count(n, edges, matching, tris):
    if not tris:
        return 0
    endpoints = {v for e in matching for v in e}
    growth_edges = set(edges).difference(matching)
    growth_edges.update((v, n) for v in endpoints)
    all_e = sorted(growth_edges)
    indices = [{all_e.index(e) for e in t} for t in tris]
    target = 0
    for mask in range(1 << len(all_e)):
        red = blue = False
        for t in indices:
            if all((mask >> ix) & 1 for ix in t):
                red = True
            if all(not ((mask >> ix) & 1) for ix in t):
                blue = True
            if red and blue:
                target += 1
                break
    return target


def predicted_partition_count(m, k, j):
    if j < 2:
        return 0
    assert m + k - 3*j >= 0
    return 2 ** (m + k - 3*j) * (8**j - 2*7**j + 6**j)


def series_coefficients(cycle, max_degree, weight):
    # Exact univariate specialization of both rational generating functions.
    # The common denominator is (1-x-y*x**3)**2 * (1-x-y*x**2).
    def multiply(a, b):
        c = [0]*(max_degree+1)
        for i, ai in enumerate(a):
            for j, bj in enumerate(b):
                if i+j <= max_degree:
                    c[i+j] += ai*bj
        return c
    A = [1, -1, 0, -weight]+[0]*max_degree
    B = [1, -1, -weight]+[0]*max_degree
    den = multiply(multiply(A, A), B)
    z = [0]*(max_degree+1)
    if cycle:
        # x**4*y**2*(1-x)*(2*(1-x)**2+y*x**3)
        left = [1, -1]
        right = [2, -4, 2, weight]
        for i, a in enumerate(left):
            for j, b in enumerate(right):
                if i+j+4 <= max_degree:
                    z[i+j+4] += weight**2*a*b
    else:
        # y**3*x**5*(1-x)
        if 5 <= max_degree: z[5] = weight**3
        if 6 <= max_degree: z[6] = -weight**3
    result = [0]*(max_degree+1)
    for d in range(max_degree+1):
        result[d] = z[d] - sum(den[i]*result[d-i] for i in range(1, d+1))
    return result


def run():
    total_matchings = 0
    total_partition_tests = 0
    exhaustive_partition_tests = 0
    cases = 0
    for cycle in (False, True):
        for n in range(4 if cycle else 2, 17):
            edges = graph_edges(n, cycle)
            counts = Counter()
            winner_by_k = Counter()
            for M in all_matchings(edges):
                k = len(M)
                tris = triangles_after_growth(n, edges, M)
                j = len(tris)
                # Check cross edges are vertex-disjoint from the reconstructed graph.
                used = [v for e in set(edges).difference(M) if e[0] in {x for a,b in M for x in (a,b)} and e[1] in {x for a,b in M for x in (a,b)} for v in e]
                assert len(used) == len(set(used))
                counts[k, j] += 1
                if j >= 2:
                    winner_by_k[k] += 1
                if n <= 8:
                    actual = check_partition_count(n, edges, M, tris)
                    expected = predicted_partition_count(len(edges), k, j)
                    assert actual == expected, ('partition', cycle, n, M, actual, expected)
                    total_partition_tests += 1
                    if tris:
                        exhaustive_partition_tests += 1
                total_matchings += 1
            for k in range(n//2+1):
                for j in range(k+1):
                    expected = (cycle_profile(n, k, j) if cycle else path_profile(n,k,j))
                    assert counts[k,j] == expected, ('coefficient',cycle,n,k,j,counts[k,j],expected)
            # The univariate rational function must match every coefficient of y^k upon specialization.
            for weight in (1, 2, 3, 5):
                series = series_coefficients(cycle, n if cycle else n-1, weight)
                actual = sum(v*weight**k for k,v in winner_by_k.items())
                assert series[n if cycle else n-1] == actual, ('rational',cycle,n,weight,actual)
            cases += 1
    print('ALL_MATCHING_PROFILES_OK', cases, 'graph_cases', total_matchings, 'matchings')
    print('PARTITION_COUNT_CHECKS_OK', total_partition_tests, 'matchings', exhaustive_partition_tests, 'full_exhaustions', total_partition_tests-exhaustive_partition_tests, 'zero_triangle_shortcuts')
    print('RATIONAL_GENERATING_FUNCTIONS_OK', 4*cases, 'specializations')
    print('VERIFY_OK')

if __name__ == '__main__':
    run()
