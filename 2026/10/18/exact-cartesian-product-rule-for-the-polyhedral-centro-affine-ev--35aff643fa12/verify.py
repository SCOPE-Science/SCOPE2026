"""Exact rational checks for weighted facet-operator product spectra.

This checks independent finite combinatorial networks; the accompanying
geometric argument proves the statement in arbitrary dimensions.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import factorial, prod


def crosspolytope(n):
    assert n >= 2
    signs = list(product((-1, 1), repeat=n))
    mass = {s: F(1, factorial(n - 1)) for s in signs}
    edge = {}
    for j, s in enumerate(signs):
        for t in signs[j+1:]:
            if sum(x != y for x, y in zip(s, t)) == 1:
                edge[(s, t)] = F(1, 2 * factorial(n - 2))
    return {'d': n, 'labels': signs, 'm': mass, 'c': edge,
            'volume': F(2 ** n, factorial(n))}


def segment():
    return {'d': 1, 'labels': [(-1,), (1,)],
            'm': {(-1,): F(1), (1,): F(1)},
            'c': {}, 'volume': F(2)}


def product_network(factors):
    V = prod((z['volume'] for z in factors), start=F(1))
    nodes = [(i, label) for i, z in enumerate(factors) for label in z['labels']]
    masses = {(i, a): factors[i]['m'][a] * V / factors[i]['volume']
              for i, a in nodes}
    edge = {}
    for i, z in enumerate(factors):
        for (a, b), w in z['c'].items():
            edge[((i, a), (i, b))] = w * V / z['volume']
    for i, z in enumerate(factors):
        for j in range(i+1, len(factors)):
            w = factors[j]
            for a in z['labels']:
                for b in w['labels']:
                    edge[((i, a), (j, b))] = z['m'][a] * w['m'][b] * V / (z['volume'] * w['volume'])
    return nodes, masses, edge


def verify(factors):
    nodes, mass, edges = product_network(factors)
    n = sum(z['d'] for z in factors)
    V = prod((z['volume'] for z in factors), start=F(1))
    assert sum(mass.values()) == n * V
    assert all(m > 0 for m in mass.values())
    def laplace(x):
        out = {key: F(0) for key in nodes}
        for (a, b), weight in edges.items():
            out[a] += weight * (x[a]-x[b])
            out[b] += weight * (x[b]-x[a])
        return {node: out[node]/mass[node] for node in nodes}
    def eigen(x, lam):
        out = laplace(x)
        assert all(out[v] == lam * x[v] for v in nodes), (n, lam, x, out)
    eigen({v: F(1) for v in nodes}, 0)
    for i in range(1, len(factors)):
        d0, di = factors[0]['d'], factors[i]['d']
        x = {(j, lab): (F(-di) if j == 0 else F(d0) if j == i else F(0))
             for j, lab in nodes}
        eigen(x, n)
        assert sum(mass[v]*x[v] for v in nodes) == 0
    modes = 1 + len(factors)-1
    for i, z in enumerate(factors):
        d = z['d']
        if d == 1:
            continue
        for k in range(2, d+1, 2):
            for subset in combinations(range(d), k):
                x = {(j, s): F(prod(s[t] for t in subset)) if j == i else F(0)
                     for j, s in nodes}
                lam = (n-d) + (d-1)*k
                eigen(x, lam)
                assert sum(mass[v]*x[v] for v in nodes) == 0
                modes += 1
    even_dimension = sum((2**(z['d']-1) if z['d'] >= 2 else 1) for z in factors)
    assert modes == even_dimension, (modes, even_dimension)
    return n, len(nodes), modes


if __name__ == '__main__':
    tests = []
    for d in range(2, 8):
        tests.append(verify([segment(), crosspolytope(d)]))
    for a in range(2, 6):
        for b in range(2, 6):
            tests.append(verify([crosspolytope(a), crosspolytope(b)]))
    for a, b in [(2,2), (3,3), (3,4), (2,5)]:
        tests.append(verify([segment(), crosspolytope(a), crosspolytope(b)]))
    print('VERIFY_OK exact weighted facet graph eigenidentities',
          len(tests), 'product networks; largest dimension', max(t[0] for t in tests))
