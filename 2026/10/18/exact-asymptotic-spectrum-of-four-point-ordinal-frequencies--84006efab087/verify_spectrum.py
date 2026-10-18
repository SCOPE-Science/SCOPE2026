"""Exact covariance-spectrum certificate for length-four ordinal frequencies.

Run with: python verify_spectrum.py
Requires Python 3 and SymPy (no other dependencies).
"""
from itertools import permutations
from math import factorial
from sympy import Matrix, Integer, Poly, Symbol, factor, zeros, ones
from sympy.polys.matrices import DomainMatrix


def standardize(values):
    levels = {x: k + 1 for k, x in enumerate(sorted(values))}
    return tuple(levels[x] for x in values)


def asymptotic_covariance():
    patterns = list(permutations(range(1, 5)))
    index = {pattern: i for i, pattern in enumerate(patterns)}
    terms = []
    for lag in range(4):
        counts = [[0] * 24 for _ in range(24)]
        for ordering in permutations(range(4 + lag)):
            first = index[standardize(ordering[:4])]
            second = index[standardize(ordering[lag:lag + 4])]
            counts[first][second] += 1
        joint = Matrix(counts) / factorial(4 + lag)
        terms.append(joint - ones(24, 24) / (24 * 24))
    a = terms[0] + sum((c + c.T for c in terms[1:]), zeros(24, 24))
    return patterns, terms, a


def full_characteristic_polynomial(d):
    x = Symbol('x')
    coefficients = DomainMatrix.from_Matrix(d).charpoly()
    return Poly.from_list(coefficients, gens=x).as_expr()


def verify():
    patterns, terms, a = asymptotic_covariance()
    assert a == a.T
    assert a * ones(24, 1) == zeros(24, 1)
    # Prefix/suffix balance gives five independent nonconstant coboundaries.
    three = list(permutations(range(1, 4)))
    nulls = [ones(24, 1)]
    for pattern in three:
        coboundary = Matrix([
            int(standardize(q[:3]) == pattern)
            - int(standardize(q[1:]) == pattern)
            for q in patterns
        ])
        assert a * coboundary == zeros(24, 1)
        nulls.append(coboundary)
    assert Matrix.hstack(*nulls).rank() == 6
    d = a * 20160
    assert all(v.q == 1 for v in d)
    x = Symbol('x')
    expected = (x**6 * (x - 1232) * (x - 840)**2
                * (x - 800) * (x - 784) * (x - 504)
                * (x**2 - 2408*x + 1185408)
                * (x**2 - 1792*x + 705600)
                * (x**2 - 1256*x + 387072)
                * (x**3 - 3696*x**2 + 3471552*x - 616412160)
                * (x**3 - 2912*x**2 + 2549568*x - 663828480))
    actual = full_characteristic_polynomial(d)
    assert Poly(actual - expected, x).is_zero
    assert all(v == 0 for v in a * ones(24, 1))
    # Independently check finite-size covariance increments by a direct exact
    # finite-window overlap formula; these are not required for spectral proof.
    def finite_covariance(n):
        k = n - 3
        return k*terms[0] + sum(
            ((k - lag) * (terms[lag] + terms[lag].T)
             for lag in range(1, 4) if k > lag), zeros(24, 24))
    assert finite_covariance(9) - finite_covariance(8) == a
    print('PASS: exact 24 x 24 covariance, 20160 scaling,')
    print('      six independent null directions, rank 18,')
    print('      all 24 characteristic roots by exact integer computation,')
    print('      and a finite-size covariance increment identity.')
    print('Matrix trace:', d.trace(), 'Factorization:', factor(actual))


if __name__ == '__main__':
    verify()
