#!/usr/bin/env python3
"""Exact automorphism census for the ten-point poset models in arXiv:2605.06155.

This standalone checker requires only Python 3 standard library. The two incidence
lists are the cover relations C<B and B<A, indexed from zero, from Sections 4.1
and 5.1 of Ponaki Das and Sainkupar Marwein Mawiong (2026).
"""
from itertools import permutations
from collections import Counter

# C_B[i] = indices of middle points strictly covering the i-th minimal point.
# B_A[j] = indices of maximal points strictly covering the j-th middle point.
MODELS = {
    'I': ([[0, 1], [0, 2], [1, 2]], [[0, 1], [0, 2, 3], [0, 1, 2, 3]]),
    'II': ([[0, 1], [0, 2], [1, 2]], [[0, 1, 2], [0, 1, 3], [0, 2, 3]]),
    'III': ([[0, 2], [1, 2], [0, 1, 2]], [[0, 1, 2], [0, 1, 3], [2, 3]]),
    'IV': ([[0, 2], [1, 3], [0, 1, 2, 3]], [[0, 1], [0, 1], [0, 2], [0, 2]]),
    'V': ([[0, 2], [0, 1, 3], [1, 2, 3]], [[0, 1], [0, 1], [0, 2], [0, 2]]),
    'VI': ([[0, 2], [1, 3], [0, 1, 2, 3]], [[0, 1], [0, 1], [0, 2], [1, 2]]),
    'VII': ([[0, 2], [0, 1, 3], [1, 2, 3]], [[0, 1], [0, 1], [0, 2], [1, 2]]),
}
EXPECTED_AUTOMORPHISMS = {'I': 2, 'II': 6, 'III': 4,
                          'IV': 4, 'V': 2, 'VI': 2, 'VII': 1}
EXPECTED_ANTIAUTOMORPHISMS = {'I': 0, 'II': 0, 'III': 0,
                              'IV': 4, 'V': 0, 'VI': 0, 'VII': 1}


def incidences(model):
    cb, ba = model
    m, r, n = len(cb), len(ba), max(max(s) for s in ba) + 1
    lower = {(i, j) for i, S in enumerate(cb) for j in S}
    upper = {(j, k) for j, S in enumerate(ba) for k in S}
    assert len(lower) == sum(map(len, cb))
    assert len(upper) == sum(map(len, ba))
    return m, r, n, lower, upper


def automorphisms(model):
    m, r, n, lower, upper = incidences(model)
    found = []
    for pm in permutations(range(r)):
        pc_choices = [p for p in permutations(range(m))
                      if {(p[i], pm[j]) for i, j in lower} == lower]
        pa_choices = [p for p in permutations(range(n))
                      if {(pm[j], p[k]) for j, k in upper} == upper]
        for pc in pc_choices:
            for pa in pa_choices:
                found.append((pc, pm, pa))
    return found


def antiautomorphisms(model):
    m, r, n, lower, upper = incidences(model)
    if m != n:
        return []
    found = []
    # The order-reversing bijection sends C to A and A to C; B to B.
    for pb in permutations(range(r)):
        pc_to_a = [p for p in permutations(range(n))
                   if {(pb[j], p[i]) for i, j in lower} == upper]
        pa_to_c = [p for p in permutations(range(m))
                   if {(p[k], pb[j]) for j, k in upper} == lower]
        for f in pc_to_a:
            for g in pa_to_c:
                found.append((f, pb, g))
    return found


def order_of_permutation(p):
    q = tuple(range(len(p)))
    for degree in range(1, 30):
        q = tuple(p[x] for x in q)
        if q == tuple(range(len(p))):
            return degree
    raise AssertionError('Unexpectedly high permutation order')


def order_of_triple(t):
    q = [tuple(range(len(p))) for p in t]
    for degree in range(1, 30):
        q = [tuple(p[x] for x in z) for p, z in zip(t, q)]
        if all(z == tuple(range(len(z))) for z in q):
            return degree
    raise AssertionError('Unexpectedly high automorphism order')


def run():
    for kind, model in MODELS.items():
        m, r, n, lower, upper = incidences(model)
        assert m + r + n == 10
        autos = automorphisms(model)
        antis = antiautomorphisms(model)
        assert len(autos) == EXPECTED_AUTOMORPHISMS[kind]
        assert len(antis) == EXPECTED_ANTIAUTOMORPHISMS[kind]
        orders = Counter(order_of_triple(a) for a in autos)
        if kind == 'II':
            assert orders == Counter({1: 1, 2: 3, 3: 2})  # S_3
        if kind in ('III', 'IV'):
            assert orders == Counter({1: 1, 2: 3})  # C_2 x C_2
        if kind in ('I', 'V', 'VI'):
            assert orders == Counter({1: 1, 2: 1})  # C_2
        if kind == 'VII':
            assert orders == Counter({1: 1})
            f, pb, g = antis[0]
            assert all(g[f[i]] == i for i in range(m))
            assert all(f[g[k]] == k for k in range(n))
            assert all(pb[pb[j]] == j for j in range(r))
        print(kind, 'automorphisms:', len(autos),
              'anti-automorphisms:', len(antis),
              'element orders:', sorted(orders.items()))
    print('All exact incidence and group assertions passed.')


if __name__ == '__main__':
    run()
