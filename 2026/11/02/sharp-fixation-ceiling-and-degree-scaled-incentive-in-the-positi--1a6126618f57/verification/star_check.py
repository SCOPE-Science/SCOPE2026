"""Reproducibility checks for the positional-voter star fixation theorem.

Requires Python 3.10+ and sympy. All small-state checks use exact rationals.
"""
from fractions import Fraction
import sympy as sp


def symbolic_checks():
    m, r, k = sp.symbols('m r k', positive=True)
    d = lambda j: m + (r - 1) * j
    e = lambda j: d(j) + 1
    u = lambda j: r * j * (m * r + 1) / (m * (r + 1) * e(j + 1))
    v = lambda j: (m * r + 1) / ((m + 1) * (r + 1)) * (1 + (m + r) * j / (m * e(j)))
    identities = [u(0), v(m) - 1,
                  u(k) - u(k - 1) - r * (v(k) - u(k)) / d(k),
                  v(k + 1) - v(k) - (v(k) - u(k)) / d(k),
                  v(1) - (m * r + 1) / (m * (r + 1))]
    assert all(sp.factor(x) == 0 for x in identities)
    finite = sp.factor((v(0) + m * u(1)) / (m + 1))
    target = (m * r + 1) * (m * r + m + 3 * r - 1) / ((m + 1) ** 2 * (r + 1) * (m + 2 * r - 1))
    assert sp.factor(finite - target) == 0
    strong = sp.factor(sp.limit(finite, r, sp.oo))
    assert strong == m * (m + 3) / (2 * (m + 1) ** 2)
    assert sp.factor(strong - sp.Rational(9, 16)) == -(m - 3) ** 2 / (16 * (m + 1) ** 2)
    t = sp.symbols('t', positive=True)
    assert sp.simplify(sp.limit(finite.subs(r, t * m), m, sp.oo) - t / (1 + 2 * t)) == 0
    print('Symbolic boundary equations, harmonic equations, exact probability, and sharp limits: PASS')


def exact_markov(m, r):
    # One hub state c and a count k of mutant leaves. Absorbing configurations are (0,0),(1,m).
    states = [(0, k) for k in range(1, m + 1)] + [(1, k) for k in range(m)]
    lookup = {state: i for i, state in enumerate(states)}
    size = 2 * m
    matrix = [[sp.Rational(0) for _ in range(size)] for _ in range(size)]
    rhs = [sp.Rational(0) for _ in range(size)]
    for i, (c, k) in enumerate(states):
        denom = m + (r - 1) * k
        if not c:
            events = [((0, k - 1), sp.Rational(k, m + 1)),
                      ((1, k), sp.Rational(r * k, (m + 1) * denom))]
        else:
            events = [((1, k + 1), sp.Rational(m - k, m + 1)),
                      ((0, k), sp.Rational(m - k, (m + 1) * denom))]
        for state, probability in events:
            matrix[i][i] += probability
            if state == (1, m):
                rhs[i] += probability
            elif state in lookup:
                matrix[i][lookup[state]] -= probability
    solution = sp.linsolve((sp.Matrix(matrix), sp.Matrix(rhs)))
    vals = list(next(iter(solution)))
    return {state: vals[lookup[state]] for state in states}


def small_state_checks():
    tested = 0
    for m in range(2, 9):
        for r in (1, 2, 3, 7):
            probs = exact_markov(m, r)
            for k in range(1, m + 1):
                formula = sp.Rational(r * k * (m * r + 1), m * (r + 1) * (m + r + (r - 1) * k))
                assert probs[(0, k)] == formula
            for k in range(m):
                ek = m + 1 + (r - 1) * k
                formula = sp.Rational(m * r + 1, (m + 1) * (r + 1)) * (1 + sp.Rational((m + r) * k, m * ek))
                assert probs[(1, k)] == formula
            v0 = probs[(1, 0)]
            u1 = probs[(0, 1)]
            initial = sp.factor((v0 + m * u1) / (m + 1))
            assert initial <= sp.Rational(m * (m + 3), 2 * (m + 1) ** 2)
            if r == 1:
                assert initial == sp.Rational(1, m + 1)
            tested += 1
    print(f'{tested} independently solved exact finite Markov chains: PASS')


if __name__ == '__main__':
    symbolic_checks()
    small_state_checks()
