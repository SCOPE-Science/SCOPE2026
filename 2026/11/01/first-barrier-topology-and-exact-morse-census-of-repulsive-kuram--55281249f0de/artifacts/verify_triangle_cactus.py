"""Finite checks of a triangle-cactus repulsive Kuramoto theorem.

Run: python verify_triangle_cactus.py
Requires Python 3.10+ and NumPy. Finite tests do not prove the all-size theorem.
"""
from collections import Counter
from itertools import product
from math import cos, pi, sin
import numpy as np

STATES = [
    (2*pi/3, -2*pi/3, -1.5, 0, 0, 0),
    (-2*pi/3, 2*pi/3, -1.5, 0, 0, 0),
    (0, pi, -1.0, 1, 1, 1),
    (pi, 0, -1.0, 1, 1, 1),
    (pi, pi, -1.0, 1, 1, 1),
    (0, 0, 3.0, 2, 9, 2),
]


def cactus(r, shape):
    triangles = []
    for i in range(r):
        parent = 0 if shape == 'windmill' or i == 0 else 2*i
        a, b = 2*i+1, 2*i+2
        triangles.append((parent, a, b))
    edges = []
    for p, a, b in triangles:
        edges.extend(((p, a), (p, b), (a, b)))
    return triangles, edges


def reconstruct(config, triangles):
    theta = np.zeros(2*len(triangles)+1)
    for s, (p, a, b) in zip(config, triangles):
        theta[a] = theta[p] + STATES[s][0]
        theta[b] = theta[p] + STATES[s][1]
    return theta


def energy_grad_hess(theta, edges):
    d = len(theta)
    g = np.zeros(d)
    h = np.zeros((d, d))
    en = 0.0
    for a, b in edges:
        delta = theta[a]-theta[b]
        en += cos(delta)
        g[a] -= sin(delta)
        g[b] += sin(delta)
        weight = -cos(delta)
        h[a, a] += weight
        h[b, b] += weight
        h[a, b] -= weight
        h[b, a] -= weight
    return en, g, h


def coeffs(r):
    c = {(0, 0): 1}
    for _ in range(r):
        nxt = Counter()
        for (e, ind), count in c.items():
            for de, di, mul in ((0, 0, 2), (1, 1, 3), (9, 2, 1)):
                nxt[(e+de, ind+di)] += mul*count
        c = dict(nxt)
    return c


def main():
    configurations = 0
    gradient_checks = 0
    hessian_checks = 0
    first_barrier_checks = 0
    for r in range(1, 5):
        for shape in ('windmill', 'chain'):
            triangles, edges = cactus(r, shape)
            population = Counter()
            for config in product(range(6), repeat=r):
                theta = reconstruct(config, triangles)
                en, g, h = energy_grad_hess(theta, edges)
                predicted_en = sum(STATES[s][2] for s in config)
                predicted_index = sum(STATES[s][3] for s in config)
                z_degree = sum(STATES[s][4] for s in config)
                assert abs(en-predicted_en) < 2e-11
                assert max(abs(g)) < 2e-11
                evals = np.linalg.eigvalsh(h)
                assert abs(evals[0]) < 2e-9 or np.sum(abs(evals)<2e-9) == 1
                assert np.sum(abs(evals)<2e-9) == 1
                index = int(np.sum(evals < -2e-9))
                assert index == predicted_index, (r, shape, config, evals)
                population[(z_degree, index)] += 1
                configurations += 1
                gradient_checks += 1
                hessian_checks += 1
            assert dict(population) == coeffs(r)
            nmins = 2**r
            saddles = 3*r*2**(r-1)
            assert sum(v for (z, i), v in population.items() if i == 0) == nmins
            assert sum(v for (z, i), v in population.items() if z == 1 and i == 1) == saddles
            assert sum(population.values()) == 6**r
            # Exhibit a path between every pair of ground states below the exact barrier.
            for first in product((0, 1), repeat=r):
                for last in product((0, 1), repeat=r):
                    if first >= last:
                        continue
                    config = list(first)
                    max_seen = -1.5*r
                    for i in range(r):
                        if first[i] == last[i]:
                            continue
                        start_t = 2*pi/3 if config[i] == 0 else 4*pi/3
                        end_t = 4*pi/3 if config[i] == 0 else 2*pi/3
                        saved = config[i]
                        for j in range(65):
                            t = start_t + (end_t-start_t)*j/64
                            theta = np.zeros(2*r+1)
                            for j, (p, a, b) in enumerate(triangles):
                                x, y = (t, -t) if j == i else STATES[config[j]][:2]
                                theta[a] = theta[p] + x
                                theta[b] = theta[p] + y
                            en, _, _ = energy_grad_hess(theta, edges)
                            max_seen = max(en, max_seen)
                            assert en <= -1.5*r+0.5+2e-11
                            first_barrier_checks += 1
                        config[i] = 1-saved
                    assert tuple(config) == tuple(last)
                    assert abs(max_seen-(-1.5*r+0.5)) < 2e-11
            print(f'r={r} shape={shape}: states={6**r} minima={nmins} first_saddles={saddles} beta1={saddles-nmins+1} OK')
    print(f'Checks: {configurations} full equilibrium configurations, {gradient_checks} gradients, '
          f'{hessian_checks} complete Hessian inertias, {first_barrier_checks} sampled path points.')
    print('TRIANGLE_CACTUS_REPULSIVE_VERIFY_OK')

if __name__ == '__main__':
    main()
