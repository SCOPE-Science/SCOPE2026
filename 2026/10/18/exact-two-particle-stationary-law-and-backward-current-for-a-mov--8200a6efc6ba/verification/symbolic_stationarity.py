#!/usr/bin/env python3
"""Symbolic finite-size diagnostic for a two-particle moving-defect ring.

This is a finite diagnostic, not the proof for unbounded ring size.
All calculations are exact polynomial identities in z.
"""
from itertools import combinations
from sympy import Symbol, simplify, expand

z = Symbol('z', real=True)

def weights(L):
    for i, j in combinations(range(L), 2):
        if i == 0:
            w = z if j == L - 1 else 1
        elif j == L - 1:
            w = z**2
        else:
            w = (1 + z**2) / 2
        yield (i, j), w

def transitions(L, state):
    ss = set(state)
    def rotated(new):
        return tuple(sorted((i - 1) % L for i in new))
    if 0 not in ss:
        return [(rotated(ss), 1, 0)]
    moves = [step for step in (-1, +1) if step % L not in ss]
    if not moves:
        return [(rotated(ss), 1, 0)]
    stay = z if len(moves) == 1 else z**2
    result = [(rotated(ss), stay, 0)]
    for step in moves:
        new = (ss - {0}) | {step % L}
        result.append((rotated(new), (1 - stay) / len(moves), step))
    return result

for L in range(3, 21):
    w = dict(weights(L))
    incoming = {s: 0 for s in w}
    signed = 0
    for state, weight in w.items():
        edges = transitions(L, state)
        assert simplify(sum(prob for _, prob, _ in edges) - 1) == 0
        for to, probability, step in edges:
            incoming[to] += weight * probability
            signed += weight * probability * step
    assert all(expand(incoming[s] - w[s]) == 0 for s in w), L
    T = (L-2)*(L+1)*(1+z**2)/4 + z
    assert expand(sum(w.values()) - T) == 0
    assert simplify(signed - (-(1-z)**2)) == 0
    print(f'L={L:2d}: {len(w):3d} exact balance identities, normalization and current verified')
print('PASS: finite symbolic diagnostics; all-size proof is separately provided.')
