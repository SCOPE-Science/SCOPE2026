"""Exact finite checks for an asynchronous bounded-confidence averaging theorem.

Run with Python 3.9+ as: python hk_contact_monotonicity_verifier.py
The uniform graph-family statement and spectral sharpness require the proof.
"""
from fractions import Fraction
from itertools import combinations, product
from math import cos, pi, sin
from random import Random

Q = Fraction


def active_edges(edges, positions, radius=Q(1)):
    return {e for e in edges if abs(positions[e[0]] - positions[e[1]]) <= radius}


def update(edges, positions, vertex, radius=Q(1)):
    out = list(positions)
    accepted = [other for other in range(len(positions))
                if tuple(sorted((vertex, other))) in edges
                and abs(positions[vertex] - positions[other]) <= radius]
    out[vertex] = (positions[vertex] + sum((positions[u] for u in accepted), Q(0))) / (len(accepted) + 1)
    return out


def test_small_graphs():
    # Check all simple labeled graphs with up to four vertices,
    # all integer opinions from -2 through 2, and all first activations.
    verified = 0
    sharp_witnesses = 0
    for n in range(1, 5):
        possible = list(combinations(range(n), 2))
        for mask in range(1 << len(possible)):
            edges = {e for k, e in enumerate(possible) if mask >> k & 1}
            degree = [sum(v in e for e in edges) for v in range(n)]
            for state in product(range(-2, 3), repeat=n):
                positions = [Q(s) for s in state]
                old = active_edges(edges, positions)
                for vertex in range(n):
                    nxt = update(edges, positions, vertex)
                    new = active_edges(edges, nxt)
                    if max(degree, default=0) <= 2:
                        assert old.issubset(new), (n, edges, state, vertex, old - new)
                    verified += 1
            if max(degree, default=0) >= 3:
                center = degree.index(max(degree))
                neighbor = [v for v in range(n) if tuple(sorted((center, v))) in edges]
                pos = [Q(0) for _ in range(n)]
                pos[neighbor[0]] = Q(-1)
                for v in neighbor[1:]:
                    pos[v] = Q(1)
                old = active_edges(edges, pos)
                new = active_edges(edges, update(edges, pos, center))
                assert not old.issubset(new)
                sharp_witnesses += 1
    return verified, sharp_witnesses


def test_random_multistep():
    rng = Random(2026)
    passes = 0
    for n in range(3, 9):
        for typ in ('path', 'cycle'):
            edges = {(i, i+1) for i in range(n-1)}
            if typ == 'cycle':
                edges.add((0, n-1))
            for _ in range(200):
                state = [Q(rng.randrange(-18, 19), 12) for _ in range(n)]
                last = active_edges(edges, state)
                for __ in range(35):
                    vertex = rng.randrange(n)
                    state = update(edges, state, vertex)
                    new = active_edges(edges, state)
                    assert last <= new
                    last = new
                    passes += 1
    return passes


def cycle_energy(state):
    return sum((state[v] - state[(v+1) % len(state)]) ** 2
               for v in range(len(state)))


def test_sharp_cycle_factor():
    # Analytic verification uses Laplacian eigenvalues; this is a floating
    # cross-check of the one-step conditional expectation at a first mode.
    checks = []
    for n in range(3, 19):
        state = [0.1 * cos(2*pi*v/n) for v in range(n)]
        energy = cycle_energy(state)
        edges = {(i, i+1) for i in range(n-1)} | {(0, n-1)}
        next_mean = sum(cycle_energy(update(edges, state, vertex)) for vertex in range(n)) / n
        q = 1 - 16 * sin(pi/n)**2 / (9*n)
        assert abs(next_mean / energy - q) < 1e-11, (n, next_mean/energy, q)
        checks.append(n)
    return checks


if __name__ == '__main__':
    exact_checks, witnesses = test_small_graphs()
    multistep = test_random_multistep()
    cycles = test_sharp_cycle_factor()
    print('PASS')
    print('Exhaustive exact first-update cases:', exact_checks)
    print('Exact high-degree witness graphs:', witnesses)
    print('Exact randomized path/cycle updates:', multistep)
    print('First-mode spectral tests, cycle lengths:', cycles)
