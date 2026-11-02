#!/usr/bin/env python3
"""Exact reproducibility checks for a degree-normalized epidemic process.

Requires Python 3 and SymPy. All assertions use exact arithmetic.
"""
from itertools import combinations, permutations
import sympy as sp

A, B = sp.symbols('a b', positive=True)


def automorphism_orbits(n, edges):
    edges = {frozenset(e) for e in edges}
    autos = [p for p in permutations(range(n))
             if {frozenset((p[i], p[j])) for i, j in combinations(range(n), 2)
                 if frozenset((i, j)) in edges} == edges]
    found = set()
    orbits = []
    for s in range(1 << n):
        if s in found:
            continue
        orbit = sorted({sum(((s >> i) & 1) << p[i] for i in range(n))
                        for p in autos})
        orbits.append(orbit)
        found.update(orbit)
    return orbits


def quotient_generator(n, edges, a, b):
    edges = {frozenset(e) for e in edges}
    neighbors = [tuple(j for j in range(n) if frozenset((i, j)) in edges)
                 for i in range(n)]
    degrees = [len(neighbors[i]) for i in range(n)]
    assert all(d > 0 for d in degrees)
    orbits = automorphism_orbits(n, edges)
    where = {s: k for k, orbit in enumerate(orbits) for s in orbit}
    q = sp.zeros(len(orbits))
    for k, orbit in enumerate(orbits):
        state = orbit[0]
        for dest in range(n):
            if state & (1 << dest):
                t = state ^ (1 << dest)
                rate = sp.Integer(1)
            else:
                t = state | (1 << dest)
                rate = a + b * sum((sp.Rational(1, degrees[src])
                                    for src in neighbors[dest]
                                    if state & (1 << src)), sp.Integer(0))
            q[k, where[t]] += rate
            q[k, k] -= rate
    assert all(sp.simplify(sum(q[k, j] for j in range(q.cols))) == 0
               for k in range(q.rows))
    return orbits, q


def prevalence(n, edges, a, b):
    orbits, q = quotient_generator(n, edges, a, b)
    m = q.T.copy()
    m[-1, :] = sp.ones(1, q.rows)
    rhs = sp.zeros(q.rows, 1)
    rhs[-1] = 1
    stationary_orbit_weights = m.inv() * rhs
    return sp.factor(sum(stationary_orbit_weights[k] *
                         sp.Rational(orbit[0].bit_count(), n)
                         for k, orbit in enumerate(orbits)))


def full_generator(n, edges, a, b):
    edge_set = {frozenset(e) for e in edges}
    neighbors = [tuple(j for j in range(n) if frozenset((i, j)) in edge_set)
                 for i in range(n)]
    degree = [len(neighbors[i]) for i in range(n)]
    q = sp.zeros(1 << n)
    for state in range(1 << n):
        for dest in range(n):
            if state & (1 << dest):
                t, rate = state ^ (1 << dest), sp.Integer(1)
            else:
                t = state | (1 << dest)
                rate = a + b * sum((sp.Rational(1, degree[src])
                                    for src in neighbors[dest]
                                    if state & (1 << src)), sp.Integer(0))
            q[state, t] += rate
            q[state, state] -= rate
    return q


def full_prevalence(n, edges, a, b):
    q = full_generator(n, edges, a, b)
    m = q.T.copy()
    m[-1, :] = sp.ones(1, 1 << n)
    rhs = sp.zeros(1 << n, 1)
    rhs[-1] = 1
    pi = m.inv() * rhs
    return sum(pi[s] * sp.Rational(s.bit_count(), n)
               for s in range(1 << n))


def poly_f(a, b):
    coefficients = [
      486*(a+1)**8*(8*a-7),
      27*(a+1)**6*(684*a**2+5*a-337),
      3*(a+1)**4*(12438*a**3+11505*a**2-3359*a-3143),
      (a+1)**2*(41886*a**4+79422*a**3+33673*a**2-8200*a-4391),
      2*(a+1)*(14292*a**4+27708*a**3+14246*a**2+589*a-280),
      12152*a**4+25111*a**3+15356*a**2+2683*a+256,
      3146*a**3+4047*a**2+1127*a+80,
      2*a*(227*a+136),
      28*a]
    return sp.expand(sum(coef*b**k for k,coef in enumerate(coefficients))), coefficients


def check():
    cycle4 = [(0,1), (1,2), (2,3), (3,0)]
    diamond4 = cycle4 + [(0,2)]
    path3 = [(0,1), (1,2)]
    triangle3 = path3 + [(0,2)]
    pc = prevalence(4, cycle4, A, B)
    pd = prevalence(4, diamond4, A, B)
    delta = sp.factor(pd - pc)
    num, den = sp.fraction(delta)
    f, coefficients = poly_f(A, B)
    assert sp.expand(num + A*B**2*f) == 0
    factors = sp.factor_list(den)[1]
    assert len(factors) == 2 and all(mul == 1 for _,mul in factors)
    assert all(coef > 0 for d,m in factors
               for exp,coef in sp.Poly(d, A, B).terms())
    # For k=0,1,2,3,4 each coefficient has exactly one positive
    # root; check the strict order by disjoint rational brackets.
    brackets = [(sp.Rational(7,8),sp.Rational(7,8)),
                (sp.Rational(2,3),sp.Rational(3,4)),
                (sp.Rational(1,2),sp.Rational(3,5)),
                (sp.Rational(3,10),sp.Rational(1,3)),
                (sp.Rational(1,10),sp.Rational(1,8))]
    for k, (lo,hi) in enumerate(brackets):
        c = coefficients[k]
        if lo == hi:
            assert sp.factor(c.subs(A,lo)) == 0
        else:
            assert c.subs(A,lo) < 0 and c.subs(A,hi) > 0
        # A coefficient polynomial has exactly one sign change
        # in descending degree after removing a positive (a+1)^power.
        coeff = [v for v in sp.Poly(c,A).all_coeffs() if v]
        assert sum(1 if x*y < 0 else 0 for x,y in zip(coeff,coeff[1:])) == 1
    shifted = sp.Poly(sp.expand(f.subs(A, sp.Rational(7,8)+sp.Symbol('z'))), B, sp.Symbol('z'))
    assert all(c >= 0 for _, c in shifted.terms())
    dp3 = sp.factor(prevalence(3, triangle3, A, B) -
                    prevalence(3, path3, A, B))
    expected3 = (A*B**2*(2*A+B+1)*(2*A+B+2)*(2*A**2+A*B+4*A+2))
    numerator3, denominator3 = sp.fraction(dp3)
    assert sp.expand(numerator3-expected3) == 0
    assert all(coef > 0 for _,coef in sp.Poly(denominator3,A,B).terms())
    for a,b in ((1,1),(sp.Rational(1,10),sp.Rational(1,10)),
                (sp.Rational(1,10),10),(sp.Rational(7,8),1),
                (1,10)):
        for edges, symbolic in ((cycle4,pc),(diamond4,pd)):
            exact = full_prevalence(4, edges, a, b)
            assert sp.simplify(exact - symbolic.subs({A:a,B:b})) == 0
    assert sp.simplify(pc.subs({A:1,B:1}) - sp.Rational(270,443)) == 0
    assert sp.simplify(pd.subs({A:1,B:1}) - sp.Rational(2366908,3887983)) == 0
    assert sp.simplify(delta.subs({A:1,B:1}) + sp.Rational(1215166,1722376469)) == 0
    # For a<7/8, c0 is negative and leading coefficient positive;
    # the ordered coefficient roots show exactly one Descartes change.
    for a in (sp.Rational(1,20), sp.Rational(1,5),
              sp.Rational(2,5), sp.Rational(3,5), sp.Rational(4,5)):
        signs = [sp.sign(c.subs(A,a)) for c in coefficients]
        nonzero = [s for s in signs if s]
        assert nonzero[0] == -1 and nonzero[-1] == 1
        assert sum(1 if x*y < 0 else 0 for x,y in zip(nonzero,nonzero[1:])) == 1
    print('PASS: exact quotient and full-state stationarity; phase polynomial;')
    print('      root-order certificate; all-three-vertex bound; rational examples.')
    print('orbit sizes', len(automorphism_orbits(4,cycle4)),
          len(automorphism_orbits(4,diamond4)))
    print('example drop', sp.Rational(1215166,1722376469))


if __name__ == '__main__':
    check()
