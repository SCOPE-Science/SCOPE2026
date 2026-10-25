#!/usr/bin/env python3
"""Exact finite-graph checks for even-subgraph branch laws on multipath networks."""
from fractions import Fraction as F
from itertools import product, combinations

CHECKS = 0

def equal(a, b, label):
    global CHECKS
    CHECKS += 1
    assert a == b, f'{label}: {a} != {b}'


def construct(lengths, parameters):
    assert len(lengths) == len(parameters) >= 2
    edges = []
    paths = []
    next_vertex = 2
    for length, probs in zip(lengths, parameters):
        assert length >= 2 and len(probs) == length
        prev, this = 0, []
        for pos, p in enumerate(probs):
            assert F(0) < p < F(1)
            nxt = 1 if pos == length - 1 else next_vertex
            if pos < length - 1:
                next_vertex += 1
            this.append(len(edges))
            edges.append((prev, nxt, p))
            prev = nxt
        paths.append(this)
    return edges, paths, next_vertex


def exact_distribution(lengths, parameters):
    edges, paths, vertices = construct(lengths, parameters)
    assert len(edges) <= 13
    masses = {}
    normalizer = F(0)
    for bits in product((0, 1), repeat=len(edges)):
        deg = [0] * vertices
        weight = F(1)
        for bit, (u, v, p) in zip(bits, edges):
            weight *= p if bit else (1-p)
            deg[u] += bit
            deg[v] += bit
        if any(d % 2 for d in deg):
            continue
        status = []
        for branch in paths:
            signs = {bits[e] for e in branch}
            assert len(signs) == 1
            status.append(bits[branch[0]])
        assert sum(status) % 2 == 0
        status = tuple(status)
        masses[status] = masses.get(status, F(0)) + weight
        normalizer += weight
    return {s: a/normalizer for s, a in masses.items()}


def predicted(lengths, parameters):
    q = []
    t = []
    a_plus_b = F(1)
    for row in parameters:
        a = F(1)
        b = F(1)
        for p in row:
            a *= p
            b *= (1-p)
        a_plus_b *= a + b
        qi = a/(a+b)
        q.append(qi)
        t.append(1-2*qi)
    T = F(1)
    for ti in t: T *= ti
    mass = {}
    for status in product((0, 1), repeat=len(q)):
        if sum(status) % 2: continue
        w = F(1)
        for x, qi in zip(status, q): w *= qi if x else (1-qi)
        mass[status] = 2*w/(1+T)
    return q, t, mass, a_plus_b*(1+T)/2


def tests(lengths, params):
    obs = exact_distribution(lengths, params)
    q, t, pred, _ = predicted(lengths, params)
    equal(sum(obs.values()), F(1), 'probability sum')
    equal(sum(pred.values()), F(1), 'analytic sum')
    for outcome in pred:
        equal(obs.get(outcome, F(0)), pred[outcome], 'whole distribution')
    m = len(lengths)
    T = F(1)
    for val in t: T *= val
    for order in range(1, m+1):
        for sub in combinations(range(m), order):
            outside = set(range(m)) - set(sub)
            R = F(1)
            for j in outside: R *= t[j]
            for value in product((0, 1), repeat=order):
                actual = sum(weight for status, weight in obs.items()
                             if tuple(status[i] for i in sub) == value)
                base = F(1)
                for j, bit in zip(sub, value): base *= q[j] if bit else (1-q[j])
                formula = base*(1+(-1)**sum(value)*R)/(1+T)
                equal(actual, formula, 'subset marginal')
                if order >= 2 and R == 0:
                    equal(actual, base, 'shielded independence')
    for i, j in combinations(range(m), 2):
        e_i = sum(w for s,w in obs.items() if s[i])
        e_j = sum(w for s,w in obs.items() if s[j])
        e_ij = sum(w for s,w in obs.items() if s[i] and s[j])
        R = F(1)
        for k in range(m):
            if k not in (i, j): R *= t[k]
        cov = 4*q[i]*(1-q[i])*q[j]*(1-q[j])*R/(1+T)**2
        equal(e_ij-e_i*e_j, cov, 'covariance')
        if R == 0: equal(e_ij, e_i*e_j, 'pair independence')


def main():
    scenarios = [
      ([2, 3, 4], [[F(1,4),F(1,3)], [F(1,5),F(2,3),F(3,7)], [F(3,5),F(1,4),F(4,9),F(3,4)]]),
      ([2, 2, 2], [[F(1,4),F(1,3)], [F(3,5),F(3,4)], [F(1,3),F(2,3)]]),
      ([2, 2, 2, 3], [[F(4,5)]*2,[F(2,3)]*2,[F(3,5)]*2,[F(7,9)]*3]),
      ([2, 2, 2, 2, 2], [[F(3,4)]*2]*5),
      ([2, 2, 2, 2, 2], [[F(1,4)]*2]*5),
      ([2, 2, 2, 2, 2], [[F(1,2)]*2]*5),
      ([2, 2, 2, 2, 2, 2], [[F(3,5)]*2]*6),
      ([2, 2], [[F(2,3)]*2]*2),
      ([2, 2, 2, 2], [[F(1,4),F(3,5)],[F(2,3),F(2,3)],[F(1,3),F(2,3)],[F(3,5),F(4,7)]]),
    ]
    for lens, params in scenarios:
        tests(lens, params)
    # Inhomogeneous edge probabilities can balance one whole path without
    # any individual edge having probability one half.
    q, t, _, _ = predicted(*scenarios[1])
    equal(q, [F(1,7),F(9,11),F(1,2)], 'nontrivial path balance')
    equal(t[2], F(0), 'balanced third branch')
    print('VERIFIED', CHECKS, 'exact equalities for', len(scenarios), 'finite network cases')

if __name__ == '__main__':
    main()
