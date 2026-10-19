"""Standalone exact and asymptotic checks for a conditional leaf profile in Cayley trees.

Run with Python 3 (standard library only): python tree_leaf_distance_verify.py
The finite enumerations corroborate but do not replace the counting proof.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import product
from math import e, pi, sqrt


def decode_prufer(code, n):
    degree = [1] * n
    for x in code:
        degree[x] += 1
    adjacency = [[] for _ in range(n)]
    for x in code:
        u = next(i for i, d in enumerate(degree) if d == 1)
        adjacency[u].append(x)
        adjacency[x].append(u)
        degree[u] -= 1
        degree[x] -= 1
    u, v = [i for i, d in enumerate(degree) if d == 1]
    adjacency[u].append(v)
    adjacency[v].append(u)
    return adjacency


def distance(adj, source, target):
    queue = deque([(source, 0)])
    visited = {source}
    while queue:
        v, depth = queue.popleft()
        if v == target:
            return depth
        for w in adj[v]:
            if w not in visited:
                visited.add(w)
                queue.append((w, depth + 1))
    raise AssertionError('tree path not found')


def conditional_mean(n, k):
    assert n >= 3 and 1 <= k < n
    a = Fraction(n-1, n)
    return (Fraction(n-k-1) + Fraction(2*k, k+1)) * a ** (n-k-2)


def distance_probability(n, k):
    numerator = k + 1
    for j in range(k-1):
        numerator *= n - 2 - j
    return Fraction(numerator, n**k)


def forward_difference(n, k):
    a = Fraction(n-1, n)
    return a ** (n-k-3) * Fraction(2*n-(k+2)*(k*k+1), n*(k+1)*(k+2))


def exhaustive():
    total = 0
    for n in range(3, 9):
        counts = defaultdict(int)
        leaves = defaultdict(int)
        for code in product(range(n), repeat=n-2):
            adj = decode_prufer(code, n)
            k = distance(adj, 0, 1)
            counts[k] += 1
            leaves[k] += sum(len(neighbors) == 1 for neighbors in adj)
        assert sum(counts.values()) == n**(n-2)
        for k in range(1, n):
            assert Fraction(counts[k], n**(n-2)) == distance_probability(n, k), (n,k,'distance law')
            assert Fraction(leaves[k], counts[k]) == conditional_mean(n, k), (n,k,'leaf regression')
        total += n**(n-2)
    return total


def exact_shape_checks():
    tests = 0
    plateau = []
    for n in range(3, 181):
        values = [conditional_mean(n, k) for k in range(1, n)]
        for k in range(1, n-1):
            delta = values[k] - values[k-1]
            assert delta == forward_difference(n, k)
            sgn = (delta > 0) - (delta < 0)
            expected = (2*n > (k+2)*(k*k+1)) - (2*n < (k+2)*(k*k+1))
            assert sgn == expected
            tests += 1
            if delta == 0:
                plateau.append((n, k, k+1))
        max_indices = [k for k, v in enumerate(values, start=1) if v==max(values)]
        assert len(max_indices) <= 2 and max_indices == list(range(min(max_indices), max(max_indices)+1))
    assert plateau == [(3,1,2),(10,2,3),(25,3,4),(51,4,5),(91,5,6),(148,6,7)], plateau
    return tests, plateau


def finite_covariance_signs():
    """Check the global leaf-count/distance covariance as an exact rational number."""
    for n in range(3, 101):
        law = [distance_probability(n, k) for k in range(1, n)]
        mu = [conditional_mean(n, k) for k in range(1, n)]
        e_d = sum(k*p for k, p in enumerate(law, 1))
        e_l = sum(p*value for p, value in zip(law, mu))
        e_dl = sum(k*p*value for k, (p, value) in enumerate(zip(law, mu), 1))
        covariance = e_dl-e_d*e_l
        assert (covariance==0 if n==3 else covariance<0), (n, covariance)
    return 98


def asymptotics():
    target = -sqrt(pi/2)/(2*e)
    output = []
    for n in (100, 1000, 10000):
        p = 2/n
        ed = el = edl = 0.0
        a = (n-1)/n
        for k in range(1,n):
            if k > 1:
                p *= (k+1)/k*(1-k/n)
            if p < 1e-295:
                break
            mu = (n-k-1+2*k/(k+1))*a**(n-k-2)
            ed += k*p
            el += p*mu
            edl += p*k*mu
        scaled = (edl-ed*el)/sqrt(n)
        assert scaled < 0
        output.append((n, scaled))
    assert abs(output[-1][1]-target) < 0.012
    return target, output


if __name__ == '__main__':
    count = exhaustive()
    tests, plateau = exact_shape_checks()
    cov_count = finite_covariance_signs()
    target, output = asymptotics()
    print('Exhaustive labeled trees:', count, 'all cases through n=8 PASS')
    print('Exact consecutive-difference comparisons:', tests, 'PASS')
    print('Equality cases n<=180:', plateau)
    print('Finite exact covariance signs n=3..100:', cov_count, 'PASS')
    print('Asymptotic covariance / sqrt(n), expected limit:', target)
    print('Finite values:', output)
    print('ALL CHECKS PASS')
