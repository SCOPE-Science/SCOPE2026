"""Exact verification of balanced graph-Laplacian trace probing identities.

Uses only Python's standard library. Every comparison of moments is rational.
This finite verification complements, but does not replace, the general proof.
"""
from fractions import Fraction as R
from itertools import combinations
from random import Random

CHECKS = 0

def check(condition):
    global CHECKS
    CHECKS += 1
    assert condition, 'exact check %d failed' % CHECKS


def quantities(n, w):
    W = sum(w.values())
    Q = sum(t*t for t in w.values())
    d = [0] * n
    for (i, j), t in w.items():
        d[i] += t
        d[j] += t
    u = [R(d[i] - R(W, n-1), n-2) for i in range(n)]
    residual = {e: R(t) - u[e[0]] - u[e[1]] for e, t in w.items()}
    res2 = sum((t*t for t in residual.values()), R(0))
    formula = R(4*(n-1), n*(n-3)) * (
        (n-2)*Q - sum(t*t for t in d) + R(2*W*W, n-1)
    )
    projection = R(4*(n-1)*(n-2), n*(n-3)) * res2
    return 2*W, formula, projection, u, residual


def enumerate_balanced(n, w):
    vals = []
    for plus in combinations(range(n), n//2):
        P = set(plus)
        cut = sum(t for (i, j), t in w.items() if (i in P) != (j in P))
        vals.append(R(4*(n-1), n)*cut)
    mean = sum(vals, R(0))/len(vals)
    var = sum(((t-mean)**2 for t in vals), R(0))/len(vals)
    return mean, var


def exact_tests():
    rng = Random(649291)
    for n in (4, 6, 8, 10):
        pairs = list(combinations(range(n), 2))
        for _ in range(150):
            w = {e: rng.randrange(6) for e in pairs}
            expected_mean, v1, v2, u, residual = quantities(n, w)
            mean, var = enumerate_balanced(n, w)
            check(mean == expected_mean)
            check(var == v1)
            check(var == v2)
            check(sum((residual[e] for e in pairs if i in e), R(0)) == 0 for i in range(n))
            check(all(R(w[e]) == residual[e]+u[e[0]]+u[e[1]] for e in pairs))
        # Weighted additive matrices, including signed potentials with nonnegative edges
        for _ in range(50):
            potential = [rng.randrange(7) for _ in range(n)]
            w = {e: potential[e[0]]+potential[e[1]] for e in pairs}
            check(quantities(n, w)[1] == 0)
            check(enumerate_balanced(n, w)[1] == 0)

    # Exhaustive classification for all simple graphs on four and six vertices.
    for n in (4, 6):
        pairs = list(combinations(range(n), 2))
        zero_count = 0
        for mask in range(1 << len(pairs)):
            w = {e: (mask >> k) & 1 for k, e in enumerate(pairs)}
            variance = quantities(n, w)[1]
            if variance == 0:
                zero_count += 1
                edge_set = {e for e, t in w.items() if t}
                empty = len(edge_set) == 0
                complete = len(edge_set) == len(pairs)
                star = any(edge_set == {e for e in pairs if v in e} for v in range(n))
                clique_plus_isolate = any(
                    edge_set == {e for e in pairs if v not in e} for v in range(n)
                )
                check(empty or complete or star or clique_plus_isolate)
        check(zero_count == 2*n+2)

    # Explicit nonzero Hutchinson variance on every nonempty star.
    for n in (4, 6, 8, 10):
        w = {e: (1 if 0 in e else 0) for e in combinations(range(n), 2)}
        check(quantities(n, w)[1] == 0)
        check(4 * sum(t*t for t in w.values()) == 4*(n-1))
    print('PASS:', CHECKS, 'exact assertions; 600 random weighted graphs;'
          ' 200 additive weighted graphs; exhaustive simple graphs n=4,6')

if __name__ == '__main__':
    exact_tests()
