"""Exact finite checks for local equations of banana graph hypersurfaces.

The unrestricted theorem follows from the symbolic identities in the mathematical proof;
finite checks provide independent arithmetic diagnostics rather than exhaustive proof.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def elem(values, r):
    total = Fraction(0)
    for indices in combinations(range(len(values)), r):
        product = Fraction(1)
        for j in indices:
            product *= values[j]
        total += product
    return total


def phi(values):
    return elem(values, len(values) - 1)


def grad(values):
    return [elem(values[:i] + values[i + 1:], len(values) - 2)
            for i in range(len(values))]


support_tests = 0
for n in range(3, 10):
    for zero_count in range(1, n):
        for zeros in combinations(range(n), zero_count):
            vec = [Fraction(2 + i) for i in range(n)]
            for i in zeros:
                vec[i] = Fraction(0)
            assert (phi(vec) == 0) == (zero_count >= 2)
            if zero_count >= 2:
                assert (all(x == 0 for x in grad(vec))) == (zero_count >= 3)
            support_tests += 1
    torus_point = [Fraction(1)] * (n - 1) + [Fraction(-1, n - 1)]
    assert phi(torus_point) == 0
    assert any(x != 0 for x in grad(torus_point))

# Verify the EXACT polynomial identity after denominators are cleared,
# with independent evaluations of the e_j by their defining subset sums.
coordinate_tests = 0
for k in range(2, 10):
    for seed in range(1, 23):
        xs = [Fraction(seed + 2 * j, seed + j + 1) for j in range(k - 1)]
        c = Fraction(seed - 3, seed + 5)
        y = Fraction(seed - 5, 5 * seed + 101)
        assert 1 - c * y != 0
        xk = y / (1 - c * y)
        f = elem(xs + [xk], k - 1) + c * elem(xs + [xk], k)
        assert (1 - c * y) * f == elem(xs + [y], k - 1)
        coordinate_tests += 1

# Independently enumerate standard monomials under a squarefree degree-(k-1)
# initial monomial. This directly checks the graded Hilbert-series counts.
def weak_compositions(total, pieces):
    if pieces == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for rest in weak_compositions(total - x, pieces - 1):
                yield (x,) + rest

hilbert_tests = 0
for n in range(4, 9):
    for k in range(3, n):
        variables = n - 1
        for q in range(0, 9):
            actual = sum(1 for exps in weak_compositions(q, variables)
                         if not all(exps[j] >= 1 for j in range(k-1)))
            predicted = comb(q + variables - 1, variables - 1) - (
                comb(q - (k - 1) + variables - 1, variables - 1)
                if q >= k - 1 else 0)
            assert actual == predicted, (n, k, q, actual, predicted)
            hilbert_tests += 1

print('Exact coordinate-support and Jacobian test configurations:', support_tests)
print('Exact rational local-coordinate identities:', coordinate_tests)
print('Enumerated standard-monomial Hilbert-function checks:', hilbert_tests)
print('All checks passed; no finite test is used as an infinite proof.')
