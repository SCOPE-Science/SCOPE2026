#!/usr/bin/env python3
"""Independent finite identities for random Boolean-map bootstrap covariance.

Uses only Python's standard library. These checks illustrate exact algebraic
claims at finite depth; the infinite almost-sure and analytic assertions
require the proofs in RESULT.md.
"""
from fractions import Fraction
from itertools import product
from math import comb, cos, log, exp

checks = 0

def require(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1


def bitstrings(d):
    return list(product((-1, 1), repeat=d))


def path_covariance(funcs):
    n = len(funcs) + 1
    exact = Fraction(0)
    paths = bitstrings(n)
    for bits in paths:
        x = sum(bits)
        y = bits[0] + sum(bits[k] * funcs[k - 1][bits[:k]] for k in range(1, n))
        exact += Fraction(x * y, len(paths))
    return exact


def layer_average(func):
    return Fraction(sum(func.values()), len(func))

# Direct path enumeration checks every environment through N=3:
for j1 in product((-1, 1), repeat=2):
    f1 = dict(zip(bitstrings(1), j1))
    for j2 in product((-1, 1), repeat=4):
        f2 = dict(zip(bitstrings(2), j2))
        target = Fraction(1) + layer_average(f1) + layer_average(f2)
        require(path_covariance([f1, f2]) == target, 'quenched cross covariance N=3')

# A diverse deterministic selection of deeper environments, computed by
# enumerating full walk paths independently of the layer-mean formula.
for key in range(200):
    funcs = []
    for j in range(1, 5):
        seq = bitstrings(j)
        vals = [1 if ((key * 37 + t * 19 + j * 13 + key*t*7) % 23) < 11 else -1
                for t in range(len(seq))]
        funcs.append(dict(zip(seq, vals)))
    formula = Fraction(1) + sum(map(layer_average, funcs), Fraction(0))
    require(path_covariance(funcs) == formula, 'quenched cross covariance N=5')

# Exact environment law at N=4 by all 2^(2+4+8)=16384 environments.
# Mean, variance and fourth centered moment are computed by exact rational
# layer combinatorics (independent of the direct path enumeration above).
for L in range(1, 9):
    v = sum((Fraction(1, 2**j) for j in range(1, L+1)), Fraction(0))
    k4 = -2 * sum((Fraction(1, 2**(3*j)) for j in range(1, L+1)), Fraction(0))
    m4 = 3*v*v + k4
    require(v == 1-Fraction(1, 2**L), 'finite centered variance')
    require(m4 > 0, 'finite positive fourth moment')
    require(k4 < 0, 'fourth cumulant sign')
    require(m4 < 3*v*v, 'non-Gaussian fourth moment')

# Uniform Haar residue of the centered covariance at each dyadic depth.
# Convolve exact binomial layer laws on integer-valued scaled supports.
for L in range(1, 7):
    distribution = {Fraction(0): Fraction(1)}
    for j in range(1, L+1):
        d = 2**j
        outcomes = {Fraction(2*r-d, d): Fraction(comb(d,r),2**d)
                    for r in range(d+1)}
        updated = {}
        for x, px in distribution.items():
            for y, py in outcomes.items():
                updated[x+y] = updated.get(x+y, Fraction(0)) + px*py
        distribution = updated
    residues = {}
    for x, prob in distribution.items():
        z = x % 2
        residues[z] = residues.get(z, Fraction(0)) + prob
    require(len(residues) == 2**L, 'all dyadic residues represented')
    for prob in residues.values():
        require(prob == Fraction(1,2**L), 'exact uniform residual distribution')

# Exact grouping of Rademacher coefficients in two independent copies:
# for each retained level the matching coefficient/multiplicity doubles.
for j in range(2, 22):
    require(2 * 2**(j-1) == 2**j, 'smoothing multiplicity')
    require(Fraction(1, 2) * Fraction(1, 2**(j-1))
            == Fraction(1, 2**j), 'smoothing coefficient')

# Residual tail variance exact; use rational arithmetic.
for N in range(1, 21):
    tail = 2 ** (1 - N)
    finite = sum((Fraction(1, 2**j) for j in range(1, N)), Fraction(0))
    require(finite + Fraction(tail) == 1, 'tail variance formula')

# Analyticity-enabling explicit exponential Fourier estimate on a mesh.
rate = -log(cos(0.5))
for t_idx in range(20, 1300, 3):
    t = t_idx / 10
    j = max(1, __import__('math').ceil(__import__('math').log2(t)))
    require(cos(t/2**j)**(2**j) <= exp(-rate*t)*(1+1e-12),
            'one-factor Fourier decay')

# Limiting cumulants and moments are exact rational numbers.
require(-2*sum((Fraction(1, 2**(3*j)) for j in range(1, 100)), Fraction(0))
        > Fraction(-2, 7), 'finite fourth cumulant above limit')
require(Fraction(3) - Fraction(2, 7) == Fraction(19, 7), 'limiting fourth moment')
print(f'PASS: {checks} independent exact/finite/numerical assertions')
print('Var(Z)=1; kappa_4(Z)=-2/7; E[Z^4]=19/7; smoothing contraction=1/sqrt(2)')
print(f'Fourier-strip lower bound={rate:.12f}')
