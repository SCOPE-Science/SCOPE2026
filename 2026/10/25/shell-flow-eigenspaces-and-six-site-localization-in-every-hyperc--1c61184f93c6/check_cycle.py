#!/usr/bin/env python3
"""Reproduce compact Grover eigenvectors and Hamming-shell flow counts.

Standard library only. Intended for finite-dimensional sanity checks, not as
an alternative to the proof for arbitrary dimensions.
"""
import cmath
import math
from collections import deque
from itertools import combinations


def vertices_of_weight(d, m):
    return [sum(1 << j for j in js) for js in combinations(range(d), m)]


def make_state(d, m, branch=1):
    assert d >= 3 and 1 <= m <= d - 2 and branch in (-1, 1)
    # Base subset of size m-1; three fresh indices form a six-cycle.
    base = sum(1 << j for j in range(m - 1))
    a, b, c = m - 1, m, m + 1
    verts = [base | (1 << a), base | (1 << a) | (1 << b),
             base | (1 << b), base | (1 << b) | (1 << c),
             base | (1 << c), base | (1 << c) | (1 << a)]
    phi_lo = m * math.pi / d
    phi_hi = (m + 1) * math.pi / d
    mu = branch * cmath.exp(-0.5j * (phi_lo + phi_hi))
    p_lo = cmath.exp(-1j * phi_lo)
    state = {}
    for edge in range(6):
        s, t = verts[edge], verts[(edge + 1) % 6]
        assert (s ^ t).bit_count() == 1
        k = (s ^ t).bit_length() - 1
        sign = 1 if edge % 2 == 0 else -1
        lo, hi = (s, t) if s.bit_count() == m else (t, s)
        state[lo, k] = complex(sign)
        state[hi, k] = -p_lo * sign / mu
    return state, mu, verts


def residual(d, state, mu):
    position_sum = {}
    for (v, k), a in state.items():
        position_sum[v] = position_sum.get(v, 0j) + a
    for v, a in position_sum.items():
        assert abs(a) < 2e-12, (d, v, a)
    output = {}
    for (v, k), a in state.items():
        src_sum = position_sum[v]
        g = (2 / d) * src_sum - a
        dst = v ^ (1 << k)
        p = cmath.exp(-1j * math.pi * v.bit_count() / d)
        output[dst, k] = output.get((dst, k), 0j) + p * g
    return max(abs(output.get(i, 0j) - mu * state.get(i, 0j))
               for i in set(output) | set(state))


def incidence_rank_by_graph(d, m):
    lo = vertices_of_weight(d, m)
    hi = vertices_of_weight(d, m + 1)
    left, right = set(lo), set(hi)
    adj = {v: set() for v in lo + hi}
    for v in lo:
        for k in range(d):
            if (v >> k) & 1 == 0:
                w = v ^ (1 << k)
                adj[v].add(w)
                adj[w].add(v)
    edges = sum(map(len, adj.values())) // 2
    assert edges == (d - m) * math.comb(d, m)
    reached = {lo[0]}
    queue = deque([lo[0]])
    while queue:
        for w in adj[queue.popleft()]:
            if w not in reached:
                reached.add(w)
                queue.append(w)
    assert len(reached) == len(lo) + len(hi)
    return edges - len(lo) - len(hi) + 1


def run():
    checks = 0
    for d in range(3, 10):
        sum_r = 0
        for m in range(1, d - 1):
            r = incidence_rank_by_graph(d, m)
            assert r == (d - m) * math.comb(d, m) - math.comb(d, m) - math.comb(d, m + 1) + 1
            assert r > 0
            sum_r += r
            checks += 3
            for branch in (-1, 1):
                vec, mu, verts = make_state(d, m, branch)
                assert len(verts) == 6 and len(set(verts)) == 6
                assert abs(abs(mu) - 1) < 1e-12
                assert abs(mu ** 2 - cmath.exp(-1j * (2*m+1)*math.pi/d)) < 1e-12
                assert residual(d, vec, mu) < 3e-12
                masses = {}
                for (v, k), z in vec.items():
                    masses[v] = masses.get(v, 0.) + abs(z)**2
                assert len(masses) == 6
                assert abs(sum(masses.values())-12) < 5e-11
                assert all(abs(weight / 12 - 1/6) < 1e-11 for weight in masses.values())
                assert len(vec) == 12
                checks += 8
        assert sum_r == (d - 4) * 2**(d - 1) + d + 2
        assert 2*sum_r <= d*2**d
        checks += 2
        print(f'd={d}: cycle-flow dimensions per sign/shell sum={sum_r}; guaranteed orthogonal eigenmodes={2*sum_r}/{d*2**d}')
    print(f'PASS: {checks} finite sanity checks')

if __name__ == '__main__':
    run()
