#!/usr/bin/env python3
"""Standalone finite checks for strict blocking-pair matching dynamics on cycles.

Does not prove the unrestricted cycle or feedback-edge-set theorem.
"""
from functools import lru_cache


def cycle_states(n):
    return [mask for mask in range(1 << n)
            if all(not ((mask >> e & 1) and (mask >> ((e + 1) % n) & 1))
                   for e in range(n))]


def partners(n, mask):
    mate = [-1] * n
    for e in range(n):
        if mask >> e & 1:
            a, b = e, (e + 1) % n
            assert mate[a] == mate[b] == -1
            mate[a], mate[b] = b, a
    return mate


def first_choice(n, orient, vertex):
    return (vertex + 1) % n if orient >> vertex & 1 else (vertex - 1) % n


def prefers(n, orient, vertex, new_partner, old_partner):
    assert new_partner in ((vertex + 1) % n, (vertex - 1) % n)
    return old_partner == -1 or first_choice(n, orient, vertex) == new_partner


def transitions(n, orient, mask):
    mate = partners(n, mask)
    for e in range(n):
        if mask >> e & 1:
            continue
        a, b = e, (e + 1) % n
        if prefers(n, orient, a, b, mate[a]) and prefers(n, orient, b, a, mate[b]):
            nxt = mask
            for x in (a, b):
                if mate[x] >= 0:
                    edge = min(x, mate[x])
                    if {x, mate[x]} == {0, n - 1}:
                        edge = n - 1
                    nxt &= ~(1 << edge)
            nxt |= (1 << e)
            yield e, nxt


def has_cycle(graph):
    color = {}
    def visit(v):
        color[v] = 1
        for w in graph[v]:
            if color.get(w, 0) == 1:
                return True
            if color.get(w, 0) == 0 and visit(w):
                return True
        color[v] = 2
        return False
    return any(color.get(v, 0) == 0 and visit(v) for v in graph)


def main():
    tested = cycles = stable_cases = no_stable_cases = moves = 0
    for n in range(3, 11):
        states = cycle_states(n)
        assertion_count = 0
        for orient in range(1 << n):
            graph = {}
            for mask in states:
                out = [x for _, x in transitions(n, orient, mask)]
                graph[mask] = out
                moves += len(out)
                assert all(x in states for x in out)
            cyclic = has_cycle(graph)
            expectation = orient in (0, (1 << n) - 1)
            assert cyclic == expectation, (n, orient, cyclic)
            cycles += int(cyclic)
            stable = any(not out for out in graph.values())
            assert stable == (not expectation or n % 2 == 0), (n, orient)
            stable_cases += int(stable)
            no_stable_cases += int(not stable)
            tested += 1
            if expectation:
                # The single matched edge rotates by one position at each step.
                for e in range(n):
                    dest = (e + 1) % n if orient else (e - 1) % n
                    assert (1 << dest) in graph[1 << e]
                    assertion_count += 1
        assert assertion_count == 2*n
        print(f'C_{n}: profiles={1<<n} cycle_profiles=2 stable_profiles={(1<<n)-(2 if n%2 else 0)}')
    print(f'VERIFY_OK profiles={tested} cycle_profiles={cycles} stable_profiles={stable_cases} no_stable_profiles={no_stable_cases} directed_moves={moves}')

if __name__ == '__main__':
    main()
