#!/usr/bin/env python3
"""Exact checks for the central-slab cube's Hilbert-distance formulas.

The proof is analytical; finite checks test the formulas and vertex descriptions.
Only Python's standard library is required.
"""
from fractions import Fraction as F
from itertools import product


def norm_quad(v, beta):
    return sum(x*x for x in v) + beta*sum(v)**2


def vertices(n, t):
    half_width = 1 / t
    out = set()
    for sig in product((-1, 1), repeat=n):
        if abs(sum(sig)) <= half_width:
            out.add(tuple(F(s) for s in sig))
    for sig in product((-1, 1), repeat=n-1):
        base = sum(sig)
        for total in (-half_width, half_width):
            last = total - base
            if -1 <= last <= 1:
                out.add(tuple(F(s) for s in sig) + (last,))
    return out


def square_distance(n, t):
    return (n*(n*n*t*t - 2*(n-1)*t + n-2) / (n*n*t*t-1)
            if n % 2 == 0 else
            n*((n*n-n+1)*t*t + n-2) / (n*n*t*t-1))


def product_objective(n, t, beta, vert):
    assert 1 + n*beta > 0
    R = max((1+(n-1)*beta)/(1+n*beta), n*t*t/(1+n*beta))
    return R*max(norm_quad(x, beta) for x in vert)

checks = 0
cases = 0
parameters = [F(1), F(6,5), F(3,2), F(2), F(5,2), F(3), F(7,2), F(4)]
for n in range(2, 11):
    for t in parameters:
        cases += 1
        vert = vertices(n, t)
        beta = (n*t*t - 1)/(n-1)
        L = 1/t
        assert beta >= 1 and 1+n*beta > 0
        checks += 1
        target_max = (n - 2*L + (1+beta)*L*L if n % 2 == 0 else
                      n - 1 + (1+beta)*L*L)
        actual_max = max(norm_quad(x, beta) for x in vert)
        assert target_max == actual_max
        checks += 1
        R1 = (1+(n-1)*beta)/(1+n*beta)
        R2 = n*t*t/(1+n*beta)
        assert R1 == R2
        checks += 1
        formula = square_distance(n, t)
        assert product_objective(n, t, beta, vert) == formula
        checks += 1
        for den in (F(1,5), F(1,10), F(1,50), F(1,100), F(1,1000)):
            assert product_objective(n, t, beta+den, vert) >= formula
            assert product_objective(n, t, beta-den, vert) >= formula
            checks += 2
        for x in vert:
            assert -1 <= min(x) <= max(x) <= 1 and abs(sum(x)) <= L
            checks += 1
        if n % 2 == 0:
            assert formula >= F(n*n, n+1) and formula < n
        else:
            assert n-1+F(1,n) < formula <= n
        checks += 2

assert square_distance(2, F(1)) == F(4,3)
assert square_distance(3, F(1)) == 3
assert square_distance(4, F(1)) == F(16,5)
assert square_distance(5, F(1)) == 5
checks += 4
for n in range(2, 11):
    last = square_distance(n, F(1))
    for t in [F(6,5), F(3,2), F(2), F(3), F(5), F(12)]:
        next_val = square_distance(n, t)
        assert (next_val > last if n%2 == 0 else next_val < last)
        last = next_val
        checks += 1

print('CHECK_OK', 'exact_parameter_cases=', cases, 'exact_assertions=', checks,
      'vertex_sets_explicit=yes', 'parity_monotonicity=yes')
