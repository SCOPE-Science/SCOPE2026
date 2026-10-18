"""Exact state enumeration for an eight-vertex risk-aware SIR contact graph.

Requires Python 3 and SymPy. All probability computations are symbolic and exact.
"""
from fractions import Fraction
from itertools import product
from sympy import Poly, Rational, Symbol, diff, cancel, expand, nroots

x, t = Symbol('x'), Symbol('t')
# O,A,B,D,H,Q1,Q2,Q3. Edge list alone determines transition law.
edges = ((0, 1), (0, 2), (1, 3), (2, 3), (1, 4), (2, 4),
         (4, 5), (4, 6), (4, 7), (5, 6), (5, 7), (6, 7))
neighbors = [set() for _ in range(8)]
for i, j in edges:
    neighbors[i].add(j)
    neighbors[j].add(i)
assert tuple(map(len, neighbors)) == (2, 3, 3, 2, 5, 3, 3, 3)

# Infectious bits, recovered bits -> symbolic probability polynomial.
states = {(1 << 0, 0): Poly(1, x)}
updates = 0
while True:
    if all(I == 0 for I, R in states):
        break
    assert updates < 9, 'infection failed to become extinct'
    new_states = {}
    for (I, R), probability in states.items():
        if I == 0:
            key = (I, R)
            new_states[key] = new_states.get(key, Poly(0, x)) + probability
            continue
        infection_trials = []
        for v in range(8):
            if ((I | R) >> v) & 1:
                continue
            k = sum((I >> w) & 1 for w in neighbors[v])
            if not k or 8 * k > 3 * len(neighbors[v]):
                continue  # no infectious contacts, or protected by 3/8 threshold
            infection_trials.append((v, Poly(1 - (1 - x)**k, x)))
        for choices in product((0, 1), repeat=len(infection_trials)):
            weight, next_I = probability, 0
            for (v, p), infected in zip(infection_trials, choices):
                weight *= p if infected else (Poly(1, x) - p)
                if infected:
                    next_I |= (1 << v)
            if weight.is_zero:
                continue
            key = (next_I, R | I)
            new_states[key] = new_states.get(key, Poly(0, x)) + weight
    states = new_states
    updates += 1
assert updates <= 6
assert sum(states.values(), Poly(0, x)) == Poly(1, x)
expected = sum((prob * R.bit_count() for (I, R), prob in states.items()), Poly(0, x))

# Analytically predicted polynomial: tested against independent transition DP.
formula = 1 + 2*x + 2*x**2*(1-x)*(1+4*x+6*x**2*(1-x)**2+6*x**3*(1-x)**3)
assert expected == Poly(formula, x)
assert expected.degree() == 9
assert expected.all_coeffs() == [12, -48, 60, -12, -24, 4, 6, 2, 2, 1]
assert expected.eval(0) == 1
assert expected.eval(1) == 3
assert expected.eval(Rational(4, 5)) == Rational(7267213, 1953125)
assert expected.eval(Rational(4, 5)) > 3

d = diff(formula, x)
assert cancel((1+t)**8*d.subs(x, t/(1+t))/2) == (
    1+10*t+51*t**2+160*t**3+255*t**4+110*t**5+27*t**6-4*t**7-4*t**8)
assert d.subs(x, 0) == 2 and d.subs(x, 1) == -8
assert sum((1 if a*b < 0 else 0) for a,b in zip(
    [1,10,51,160,255,110,27,-4,-4], [10,51,160,255,110,27,-4,-4])) == 1
roots = [complex(z) for z in nroots(d, maxsteps=150)]
interior = [z.real for z in roots if abs(z.imag) < 1e-11 and 0 < z.real < 1]
assert len(interior) == 1
assert abs(interior[0] - 0.794710107785494) < 1e-11

# Check the universally quantified comparison with every possible social fraction
# by endpoint dominance for each infectious-neighbour count.
for theta in (Fraction(7, 20), Fraction(3, 8), Fraction(39, 100)):
    lower = max(Fraction(3, 2)*(1-theta), Fraction(5, 2)*theta)
    assert lower < 1
    alpha = (lower + 1) / 2
    for degree in (2, 3, 5):
        for k in range(degree + 1):
            q = Fraction(k, degree)
            if q < theta:
                assert alpha*q + (1-alpha) < theta
            else:
                assert q > theta and alpha*q > theta

# Representative graph-family inequalities; the printed proof handles all m.
for m in range(3, 100):
    theta = (Fraction(1, m) + Fraction(2, m+2))/2
    assert Fraction(1,m) < theta < Fraction(2,m+2)
    assert Fraction(1,2) > theta
    lower_cases = Fraction(1785 + 128*m, 625)
    assert lower_cases > 3

print('PASS: exact symbolic absorption distribution, degree-nine expectation,')
print('unimodality polynomial, mixed-awareness margins, and family inequalities.')
print(f'Absorption after {updates} synchronous steps; max near x={interior[0]:.12f}.')
