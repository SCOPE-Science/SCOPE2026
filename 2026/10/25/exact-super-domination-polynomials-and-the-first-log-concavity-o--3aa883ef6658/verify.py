#!/usr/bin/env python3
"""Exact checks for super domination polynomials of radius-two spider trees.

Only Python standard-library integer arithmetic is used.  The finite inequality
certificate handles every possible parameter a in the stated range for b.
"""
from math import comb


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def predicted_coefficients(a, b):
    """Coefficient list from the closed formula."""
    n = 1 + a + 2 * b
    c = [0] * (n + 1)
    if a >= 1:
        for j in range(b + 1):
            c[a + b + j] += (a + 1) * choose(b, j)
        for j in range(b + 1):
            c[a + b + 1 + j] += (2 ** (b - j)) * choose(b, j)
    else:
        for j in range(1, b + 1):
            c[b + j] += choose(b, j)
        for j in range(b + 1):
            c[b + 1 + j] += (2 ** (b - j)) * choose(b, j)
    return c


def original_definition_coefficients(a, b):
    n = 1 + a + 2 * b
    adj = [set() for _ in range(n)]
    for j in range(1, a + 1):
        adj[0].add(j)
        adj[j].add(0)
    for i in range(b):
        u, v = 1 + a + i, 1 + a + b + i
        adj[0].add(u)
        adj[u].add(0)
        adj[u].add(v)
        adj[v].add(u)
    adj_masks = [sum(1 << x for x in neighbors) for neighbors in adj]
    out = [0] * (n + 1)
    universe = (1 << n) - 1
    for d in range(1 << n):
        outside = universe ^ d
        witnesses = 0
        for vertex in range(n):
            if not (d & (1 << vertex)):
                continue
            omitted_neighbors = adj_masks[vertex] & outside
            if omitted_neighbors and omitted_neighbors.bit_count() == 1:
                witnesses |= omitted_neighbors
        if witnesses == outside:
            out[d.bit_count()] += 1
    return out


def binomial_unshifted(b, k):
    return choose(b, k)


def shifted_weighted(b, k):
    return (2 ** (b - k + 1)) * choose(b, k - 1) if 1 <= k <= b + 1 else 0


def exact_uniform_parameter_certificate():
    symbolic = 0
    negative_mixed = 0
    direct = 0
    for b in range(44):
        for k in range(1, b + 1):
            ak = binomial_unshifted(b, k)
            bk = shifted_weighted(b, k)
            p = ak * ak - binomial_unshifted(b, k - 1) * binomial_unshifted(b, k + 1)
            q = (2 * ak * bk
                 - binomial_unshifted(b, k - 1) * shifted_weighted(b, k + 1)
                 - binomial_unshifted(b, k + 1) * shifted_weighted(b, k - 1))
            r = bk * bk - shifted_weighted(b, k - 1) * shifted_weighted(b, k + 1)
            assert p >= 0 and r >= 0
            assert q >= 0 or q * q <= 4 * p * r, (b, k)
            symbolic += 1
            negative_mixed += q < 0
        # For a=0 the leading zero of the polynomial is removed exactly.
        c = [choose(b, j + 1) + 2 ** (b - j) * choose(b, j)
             for j in range(b + 1)]
        for k in range(1, b):
            assert c[k] * c[k] >= c[k - 1] * c[k + 1], (b, k)
            direct += 1
    assert symbolic == 946 and direct == 903
    print(f"PARAMETER_CERTIFICATE_OK b=0..43 symbolic_quadratics={symbolic} "
          f"negative_mixed={negative_mixed} direct_a0_inequalities={direct}")


def exact_first_counterexample():
    b = 44
    a = (1 << 24) - 1
    t = a + 1
    def coeff(k):
        return t * binomial_unshifted(b, k) + shifted_weighted(b, k)
    c20, c21, c22 = coeff(20), coeff(21), coeff(22)
    deficit = c20 * c22 - c21 * c21
    assert deficit == 323906111900267026871809275246673920
    assert deficit > 0
    print(f"COUNTEREXAMPLE_OK a={a} b={b} indices=20,21,22 "
          f"coefficients={c20},{c21},{c22} deficit={deficit}")


def exhaustive_small_graphs():
    cases = 0
    subsets = 0
    for a in range(5):
        for b in range(5):
            n = a + 2 * b + 1
            actual = original_definition_coefficients(a, b)
            formula = predicted_coefficients(a, b)
            assert actual == formula, (a, b, actual, formula)
            cases += 1
            subsets += 1 << n
    print(f"DEFINITION_EXHAUSTIVE_OK graph_instances={cases} "
          f"examined_subsets={subsets}")


if __name__ == '__main__':
    exhaustive_small_graphs()
    exact_uniform_parameter_certificate()
    exact_first_counterexample()
    print('VERIFICATION_OK')
