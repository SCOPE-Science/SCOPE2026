"""Independent exact checks for triangle/degree-frequency covariance in G(n,n-1).
Uses only the Python standard library. The proof of the unbounded-n theorem is analytic.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def choose(a, b):
    return comb(a, b) if 0 <= b <= a else 0


def falling(a, k):
    z = 1
    for j in range(k):
        z *= a - j
    return z if a >= k else 0


def model(n, r):
    N = choose(n, 2)
    B = choose(n - 1, 2)
    m = n - 1
    prob = Fraction(choose(n - 1, r) * choose(B, m - r), choose(N, m))
    mean = Fraction(choose(n, 3) * falling(m, 3), falling(N, 3))
    conditional = Fraction(choose(r, 2) * (m - r), B)
    conditional += Fraction(choose(n - 1, 3) * falling(m - r, 3), falling(B, 3))
    return n * prob * (conditional - mean)


def exhaustive(n):
    edges = list(combinations(range(n), 2))
    num = choose(len(edges), n - 1)
    tris = [frozenset((tuple(sorted((i, j))), tuple(sorted((i, k))),
                       tuple(sorted((j, k)))))
            for i, j, k in combinations(range(n), 3)]
    total_tri = 0
    totals = [0] * n
    joint = [0] * n
    for inds in combinations(range(len(edges)), n - 1):
        es = set(edges[i] for i in inds)
        deg = [0] * n
        for u, v in es:
            deg[u] += 1
            deg[v] += 1
        counts = [deg.count(r) for r in range(n)]
        tri = sum(t <= es for t in tris)
        total_tri += tri
        for r in range(n):
            totals[r] += counts[r]
            joint[r] += tri * counts[r]
    for r in range(n):
        brute = Fraction(joint[r], num) - Fraction(total_tri * totals[r], num * num)
        assert brute == model(n, r), (n, r, brute, model(n, r))
    return n


def sign_checks(start, stop):
    for n in range(start, stop + 1):
        for r in range(n):
            cov = model(n, r)
            expected = 1 if r == 0 or 4 <= r <= n - 3 else -1
            assert cov * expected > 0, (n, r, cov)
    return stop-start+1


def run():
    for n in range(4, 8):
        exhaustive(n)
    assert model(13, 11) > 0
    assert model(14, 12) < 0
    total = sign_checks(14, 120)
    print(f"PASS: exhaustive all fixed-edge graphs for n=4..7, 22 exact covariance identities")
    print(f"PASS: boundary at n=13,14 and {total} checked sizes with complete sign profiles")
    print("Analytic three-root and positivity arguments, not finite tests, prove all n>=14.")


if __name__ == '__main__':
    run()
