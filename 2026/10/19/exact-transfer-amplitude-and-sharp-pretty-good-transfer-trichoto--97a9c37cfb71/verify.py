#!/usr/bin/env python3
"""Reproduce exact butterfly-walk transfer identities; no external dependencies needed.

The unitary is assembled on all directed edges, independently of the
symmetry-reduced matrix used in the mathematical proof.
"""
from fractions import Fraction as F
from math import acos, cos, pi


def grover_step(amplitudes, arcs, marked):
    degree = {}
    outsum = {}
    for a, b in arcs:
        degree[a] = degree.get(a, 0) + 1
        outsum[a] = outsum.get(a, F(0)) + amplitudes[(a, b)]
    updated = {}
    for a, b in arcs:
        sign = -1 if a in marked else 1
        val = sign * (2 * outsum[a] / degree[a] - amplitudes[(a, b)])
        updated[(b, a)] = val
    return updated


def arcs_of(m):
    edges = [((j, 0), (j, 1)) for j in range(m + 1)]
    edges += [((0, b), (j, b)) for j in range(1, m + 1) for b in (0, 1)]
    return [arc for a, b in edges for arc in ((a, b), (b, a))]


def chebyshev(n, c):
    if n == 0:
        return F(1)
    a, b = F(1), c
    for i in range(1, n):
        a, b = b, 2 * c * b - a
    return b


def exact_outgoing_amplitude(m, t):
    if t % 2 == 0:
        return F(0)
    c = F(m - 1, 2 * (m + 1))
    return F(-(m + 1), 3 * m + 1) + F(2 * m, 3 * m + 1) * chebyshev(t, c)


def test_full_graph():
    checked = 0
    for m in range(0, 16):
        arcs = arcs_of(m)
        src, dst = (0, 0), (0, 1)
        marked = {src, dst}
        state = {arc: F(int(arc[0] == src)) for arc in arcs}
        incoming = {arc for arc in arcs if arc[1] == dst}
        outgoing = {arc for arc in arcs if arc[0] == dst}
        # Since unnormalized source and receiver each have norm sqrt(m+1),
        # divide exact rational overlaps by m+1.
        for t in range(0, 55):
            outamp = sum((state[a] for a in outgoing), F(0)) / (m + 1)
            if t >= 1:
                assert outamp == exact_outgoing_amplitude(m, t), (m, t, outamp)
            if t == 0:
                assert outamp == 0
            nextstate = grover_step(state, arcs, marked)
            inamp = sum((nextstate[a] for a in incoming), F(0)) / (m + 1)
            assert inamp == -outamp, (m, t, inamp, outamp)
            state = nextstate
            checked += 1
    return checked


def test_numerical_boundaries():
    for m in (2, 3, 4, 7, 11):
        theta = acos((m - 1) / (2 * (m + 1)))
        for t in (1, 3, 5, 7, 11, 31, 93):
            a = exact_outgoing_amplitude(m, t)
            closed = (-(m + 1) + 2 * m * cos(t * theta)) / (3 * m + 1)
            assert abs(float(a) - closed) < 2e-10, (m, t)
    m, t = 3, 31
    val = exact_outgoing_amplitude(m, t) ** 2
    print('m=3 t=31 exact fidelity:', val)
    print('m=3 t=31 decimal fidelity:', float(val))
    assert F(9997,10000) < val < F(9998,10000)
    for m in (2, 3, 5):
        avg = F(3*m*m+2*m+1, 2*(3*m+1)**2)
        print('m=',m,'predicted Cesaro fidelity:',float(avg))


if __name__ == '__main__':
    print('full-graph exact state updates checked:', test_full_graph())
    test_numerical_boundaries()
    print('VERIFY_OK')
