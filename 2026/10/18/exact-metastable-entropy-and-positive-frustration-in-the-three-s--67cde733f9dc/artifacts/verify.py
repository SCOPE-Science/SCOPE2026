#!/usr/bin/env python3
"""Reproduce the finite-graph one-spin metastability census on cyclic Potts ladders."""
from itertools import product
from math import log
import sympy as sp
import networkx as nx
import numpy as np

COLORS = range(3)
RUNGS = list(product(COLORS, repeat=2))
PAIRS = list(product(RUNGS, repeat=2))

def stable_rung(previous, current, following):
    for row in range(2):
        neighborhood = (previous[row], following[row], current[1-row])
        multiplicities = [neighborhood.count(c) for c in COLORS]
        if multiplicities[current[row]] > min(multiplicities):
            return False
    return True

def edge_energy(a, b):
    return int(a[0] == b[0]) + int(a[1] == b[1])

def transfer():
    m = sp.zeros(81)
    weights = {}
    for i, (a, b) in enumerate(PAIRS):
        for c in RUNGS:
            j = PAIRS.index((b, c))
            if stable_rung(a, b, c):
                m[i, j] = 1
                weights[(i, j)] = int(b[0] == b[1]) + edge_energy(b, c)
    return m, weights

def physical_counts(n):
    weak = ground = strict_ground = weak_total_energy = 0
    for flat in product(COLORS, repeat=2*n):
        rows = [flat[2*i:2*i+2] for i in range(n)]
        is_weak = True
        is_strict = True
        energy = 0
        for i, b in enumerate(rows):
            a = rows[(i-1) % n]
            c = rows[(i+1) % n]
            energy += int(b[0] == b[1]) + edge_energy(b, c)
            for row in range(2):
                neigh = (a[row], c[row], b[1-row])
                old = neigh.count(b[row])
                for new in COLORS:
                    if new == b[row]:
                        continue
                    change = neigh.count(new) - old
                    if change < 0:
                        is_weak = False
                    if change <= 0:
                        is_strict = False
        if is_weak:
            weak += 1
            weak_total_energy += energy
        if energy == 0:
            ground += 1
            if is_strict:
                strict_ground += 1
    return weak, ground, strict_ground, weak_total_energy

def main():
    m, weights = transfer()
    x = sp.Symbol('x')
    p6 = x**6 - 4*x**5 + x**4 - x**3 + 7*x**2 - 2*x - 1
    char_expected = x**27 * (x-1)**2 * (x+1)**2 * (x*x-x-1) * (x*x+x+1)**3 * \
        (x**6+x**4+x**3-x**2+1) * p6 * \
        (x**7-2*x**5+x**4-3*x**3+x**2-x+1)**2 * \
        (x**8+x**7+2*x**6+5*x**5-2*x**4+6*x**2-2*x+1)**2
    assert sp.Poly(m.charpoly(x).as_expr(), x) == sp.Poly(char_expected, x)
    graph = nx.DiGraph()
    graph.add_nodes_from(range(81))
    graph.add_edges_from(weights)
    components = sorted(nx.strongly_connected_components(graph), key=len, reverse=True)
    assert len(components[0]) == 48
    assert sorted(len(c) for c in components if len(c)>1) == [3, 3, 48]
    primary = sorted(components[0])
    a = np.array(m.extract(primary, primary), dtype=float)
    # Positive-length closed walks of lengths 4 and 5 prove aperiodicity.
    assert np.trace(np.linalg.matrix_power(a, 4)) > 0
    assert np.trace(np.linalg.matrix_power(a, 5)) > 0
    vals, vec = np.linalg.eig(a)
    k = np.argmax(vals.real)
    alpha = float(vals[k].real)
    assert abs(alpha - 3.67309969409233) < 1e-9
    assert abs(float(p6.subs(x, alpha))) < 1e-8
    assert all(abs(v) < alpha - 1e-8 for j, v in enumerate(vals) if j != k)
    right = vec[:, k].real
    if np.sum(right) < 0:
        right *= -1
    assert np.min(right) > 0
    vals_l, vec_l = np.linalg.eig(a.T)
    k_l = np.argmin(abs(vals_l - alpha))
    left = vec_l[:, k_l].real
    if np.sum(left) < 0:
        left *= -1
    assert np.min(left) > 0
    idx = {v:i for i,v in enumerate(primary)}
    derivative = np.zeros_like(a)
    for (i,j), e in weights.items():
        if i in idx and j in idx:
            derivative[idx[i],idx[j]] = e
    mu = float((left @ derivative @ right)/(alpha*(left@right)))
    assert abs(mu - 0.21744173751868) < 1e-9
    for n in range(3, 7):
        exact = physical_counts(n)
        value = int(sp.trace(m**n))
        proper = 3**n+1+2*(-2)**n
        frozen = 12 if n%3==0 else 0
        total_energy = n*int(sp.trace(sp.Matrix([[weights.get((i,j),0)*m[i,j] for j in range(81)] for i in range(81)]) * m**(n-1)))
        assert exact == (value, proper, frozen, total_energy), (n, exact, (value, proper, frozen, total_energy))
        print('n', n, 'weak', value, 'ground', proper, 'strict_ground', frozen)
    # On proper rungs, the 6-state ground-state transfer has the classical spectrum.
    proper_rungs = [r for r in RUNGS if r[0] != r[1]]
    ground_matrix = sp.Matrix([[int(a[0]!=b[0] and a[1]!=b[1]) for b in proper_rungs] for a in proper_rungs])
    assert sp.factor(ground_matrix.charpoly(x).as_expr()) == x*x*(x-3)*(x-1)*(x+2)**2
    proper_pairs = [(a,b) for a in proper_rungs for b in proper_rungs if a[0]!=b[0] and a[1]!=b[1]]
    strict_matrix=sp.zeros(len(proper_pairs))
    for i,(a,b) in enumerate(proper_pairs):
        for j,(u,c) in enumerate(proper_pairs):
            if u==b and a[0]!=c[0] and a[1]!=c[1] and \
               len({a[0],c[0],b[1]})==2 and len({a[1],c[1],b[0]})==2:
                strict_matrix[i,j]=1
    assert len(proper_pairs)==18
    assert sp.factor(strict_matrix.charpoly(x).as_expr()) == x**6*(x-1)**4*(x*x+x+1)**4
    for n in range(3,13):
        assert int(sp.trace(strict_matrix**n)) == (12 if n%3==0 else 0)
    print('proper-ground and strictly frozen transfer factors: PASS')
    print('characteristic polynomial factorization: PASS')
    print('main component irreducible primitive: PASS; alpha', format(alpha,'.14f'))
    print('typical energy per rung', format(mu,'.14f'))
    print('metastable entropy per site', format(log(alpha)/2,'.14f'))
    print('all checks PASS')

if __name__ == '__main__':
    main()
