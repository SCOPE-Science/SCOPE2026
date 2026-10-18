#!/usr/bin/env python3
"""Reproduce phase cancellation and apex-moment checks for bicyclic bases.

Uses only the Python 3 standard library. Finite checks corroborate the separate
all-orders mathematical argument; they do not certify all graph orders.
"""
from cmath import exp
from math import pi, sqrt
from itertools import product

OMEGA = complex(-0.5, sqrt(3) / 2)

class GainGraph:
    def __init__(self):
        self.edges = []
        self.order = 0

    def vertex(self):
        u = self.order
        self.order += 1
        return u

    def edge(self, u, v, phase):
        assert u != v and abs(abs(phase) - 1) < 2e-13
        assert not any({u, v} == {a, b} for a, b, _ in self.edges)
        self.edges.append((u, v, phase))

    def path(self, u, v, length, first):
        prev = u
        for j in range(length):
            nxt = v if j == length - 1 else self.vertex()
            z = first if j % 2 == 0 else -first.conjugate()
            self.edge(prev, nxt, z)
            prev = nxt

    def cycle(self, root, length, first):
        assert length >= 3
        prev = root
        for j in range(length):
            nxt = root if j == length - 1 else self.vertex()
            z = first if j % 2 == 0 else -first.conjugate()
            self.edge(prev, nxt, z)
            prev = nxt

    def check(self):
        n = self.order
        assert len(self.edges) == n + 1  # connected bicyclic base
        row = [0j] * n
        for a, b, z in self.edges:
            row[a] += z
            row[b] += z.conjugate()
        assert max(map(abs, row)) < 5e-13

        # Full cone action on (apex, base) with apex-to-base gains equal to 1.
        def action(v):
            w = [complex(sum(v[1:]))] + [v[0]] * n
            for a, b, z in self.edges:
                w[a + 1] += z * v[b + 1]
                w[b + 1] += z.conjugate() * v[a + 1]
            return w

        v = [1 + 0j] + [0j] * n
        for j in range(1, 13):
            v = action(v)
            target = n ** (j // 2) if j % 2 == 0 else 0
            assert abs(v[0] - target) < 2e-11 * max(1, abs(target)), (n, j, v[0], target)
            if j % 2:
                # Odd powers lie uniformly on the base, with no apex amplitude.
                target_base = n ** ((j - 1) // 2)
                assert max(abs(v[k] - target_base) for k in range(1, n + 1)) < 2e-11 * max(1, target_base)
            else:
                assert max(map(abs, v[1:])) < 2e-11 * max(1, n ** (j // 2))
        return 1


def theta(lengths, sign=1, rotation=0.):
    g = GainGraph()
    u, v = g.vertex(), g.vertex()
    minority_even = [j for j, length in enumerate(lengths) if length % 2 == 0]
    if len(minority_even) in (1, 2):
        j = minority_even[0] if len(minority_even) == 1 else next(j for j in range(3) if j not in minority_even)
        phases = [None] * 3
        phases[j] = sign * 1j
        k, l = [x for x in range(3) if x != j]
        phases[k] = phases[j] * OMEGA
        phases[l] = phases[j] * OMEGA ** 2
    else:
        z = exp(1j * rotation)
        phases = [z, z * OMEGA, z * OMEGA ** 2]
        if sign == -1:
            phases[1], phases[2] = phases[2], phases[1]
    for length, phase in zip(lengths, phases):
        g.path(u, v, length, phase)
    return g


def figure_eight(left, right):
    g = GainGraph()
    root = g.vertex()
    g.cycle(root, left, 1j)
    g.cycle(root, right, 1j)
    return g


def barbell(left, right, distance, bridge=1, s_left=1, s_right=1):
    g = GainGraph()
    u, v = g.vertex(), g.vertex()
    g.path(u, v, distance, bridge)
    end_bridge = (-1) ** (distance - 1) * bridge
    t_left = (-bridge + s_left * 1j * sqrt(3)) / 2
    t_right = (-end_bridge + s_right * 1j * sqrt(3)) / 2
    g.cycle(u, left, t_left)
    g.cycle(v, right, t_right)
    return g


def main():
    count = 0
    for a, b, c in product(range(1, 7), range(2, 7), range(2, 7)):
        for sign in (-1, 1):
            lengths = (a, b, c)
            uniform = len({j % 2 for j in lengths}) == 1
            for ang in ((0, .25, 1.1) if uniform else (0,)):
                count += theta(lengths, sign, ang).check()
    for a, b in product(range(3, 10), repeat=2):
        count += figure_eight(a, b).check()
    for a, b, distance in product(range(3, 10, 2), range(3, 10, 2), range(1, 6)):
        for bridge, s1, s2 in product((-1, 1), repeat=3):
            count += barbell(a, b, distance, bridge, s1, s2).check()
    # Analytically, an even lobe's two incident contributions always cancel;
    # the bridge contributes unit modulus, so cancellation is impossible.
    even_lobes = 0
    for length in range(4, 17, 2):
        for angle in (0, .2, .9, 2.3):
            z = exp(1j * angle)
            at_root = z + (-z.conjugate() if length % 2 == 0 else z).conjugate()
            assert abs(at_root) < 2e-14
            even_lobes += 1
    print('VERIFY_OK constructed_cones=', count, 'even_lobe_obstructions=', even_lobes, 'cone_moment_orders=1..12')

if __name__ == '__main__':
    main()
