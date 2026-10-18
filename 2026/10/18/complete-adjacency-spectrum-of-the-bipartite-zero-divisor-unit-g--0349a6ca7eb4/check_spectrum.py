#!/usr/bin/env python3
"""Exact adjacency-gram certificate for a ring-defined bipartite graph.

Each nonzero finite-field element is labelled by its additive negative.  The
incidence relation therefore becomes equality of a nonzero row label with a
nonzero unit label in at least one coordinate.  Only field cardinalities matter.
All characteristic-polynomial calculations use integer arithmetic.
"""
from itertools import product
from math import prod


def polynomial_times_linear(poly, eigenvalue):
    ans = [0] * (len(poly) + 1)
    for j, coefficient in enumerate(poly):
        ans[j] += coefficient
        ans[j + 1] -= eigenvalue * coefficient
    return ans


def characteristic_polynomial(matrix):
    n = len(matrix)
    assert all(len(row) == n for row in matrix)
    if n == 0:
        return [1]
    power = [[int(i == j) for j in range(n)] for i in range(n)]
    traces = []
    for _ in range(n):
        power = [[sum(power[i][h] * matrix[h][j] for h in range(n))
                  for j in range(n)] for i in range(n)]
        traces.append(sum(power[i][i] for i in range(n)))
    coef = [1]
    for k in range(1, n + 1):
        numerator = -sum(coef[k-i] * traces[i-1] for i in range(1, k+1))
        assert numerator % k == 0
        coef.append(numerator // k)
    return coef


def spectral_parameters(qs):
    assert len(qs) >= 2 and all(q >= 2 for q in qs)
    m = [q - 1 for q in qs]
    b = [q - 2 for q in qs]
    c = [mi + bi * bi for mi, bi in zip(m, b)]
    Q = prod(qs); M = prod(m); B = prod(b); C = prod(c)
    lambdas = {}
    for flags in product((0, 1), repeat=len(qs)):
        T = tuple(i for i, flag in enumerate(flags) if flag)
        multiplicity = prod(b[i] for i in T)
        if T:
            other = tuple(i for i in range(len(qs)) if i not in T)
            lam = prod(c[i] for i in other) - prod(b[i]**2 for i in other)
        else:
            lam = M*Q - 3*M*M + 2*M*B + C - B*B
        assert lam >= 0
        lambdas[T] = (lam, multiplicity)
    assert lambdas[tuple(range(len(qs)))][0] == 0
    assert lambdas[()][0] > 0
    assert sum(mult for eig, mult in lambdas.values()) == M
    assert sum(mult for eig, mult in lambdas.values() if eig > 0) == M - B
    return lambdas, Q - 1 - 2*(M-B)


def incidence(qs):
    m = [q-1 for q in qs]
    rows = [z for z in product(*[range(q) for q in qs])
            if any(x == 0 for x in z) and any(x != 0 for x in z)]
    cols = list(product(*[range(1,q) for q in qs]))
    return rows, cols, [[int(any(zi != 0 and zi == ui for zi,ui in zip(z,u)))
                         for u in cols] for z in rows]


def independent_prime_field_incidence(qs, rows, cols, generic):
    # Convert nonzero row labels to their additive negatives in F_p.
    if not all(q in (2,3,5,7) for q in qs):
        return
    for k,z in enumerate(rows):
        actual = tuple((-zi)%q for zi,q in zip(z,qs))
        for j,u in enumerate(cols):
            expected = int(any((zi + ui) % q == 0 for zi,ui,q in zip(actual,u,qs)))
            assert expected == generic[k][j]


def check(qs):
    rows,cols,H = incidence(qs)
    independent_prime_field_incidence(qs,rows,cols,H)
    Gram=[[sum(row[i]*row[j] for row in H) for j in range(len(cols))]
          for i in range(len(cols))]
    observed = characteristic_polynomial(Gram)
    lambdas,zero = spectral_parameters(qs)
    predicted = [1]
    for lam,multiplicity in lambdas.values():
        for _ in range(multiplicity):
            predicted = polynomial_times_linear(predicted, lam)
    assert observed == predicted, (qs, observed, predicted)
    assert zero >= 0
    assert len(rows)+len(cols) == prod(qs)-1
    # Trace of Gram equals the number of edges; this tests both spectra and degrees.
    assert sum(Gram[i][i] for i in range(len(cols))) == sum(map(sum,H))
    print('ok',qs,'rows',len(rows),'units',len(cols),'nonzero_gram_eigenvalues',len(cols)-prod(q-2 for q in qs),'whole_graph_zero_mult',zero)

if __name__ == '__main__':
    configs=((2,2),(2,3),(3,3),(2,5),(3,5),(2,2,2),(2,3,3),
             (3,3,3),(2,3,4),(2,2,2,2),(2,2,3,3),(2,4,5),(4,4,4))
    for qs in configs:
        check(qs)
    print('VERIFY_OK: exact Gram characteristic polynomials and nonprime-size combinatorics')
