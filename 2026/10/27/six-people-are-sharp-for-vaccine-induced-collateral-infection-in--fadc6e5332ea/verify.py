#!/usr/bin/env python3
"""Exact exhaustive verification of a sharp single-seed SIR vaccination motif.

No packages are required beyond Python's standard library. The local contact
choices are precisely all possible pairs of infection outcomes under identical
edge-by-round contacts in the unvaccinated and vaccinated experiments.
"""
from collections import deque


def successors(n, state):
    ui, ur, vi, vr = state
    full = (1 << n) - 1
    us = full & ~(ui | ur)
    vs = full & ~(vi | vr)
    options = [(0, 0)]
    for j in range(n):
        su = (us >> j) & 1
        sv = (vs >> j) & 1
        if not (su or sv):
            continue
        choices = [(0, 0)]
        if su and sv:
            common = ui & vi
            uonly = ui & ~vi
            vonly = vi & ~ui
            if uonly:
                choices.append((1, 0))
            if vonly:
                choices.append((0, 1))
            if common or (uonly and vonly):
                choices.append((1, 1))
        elif su and ui:
            choices.append((1, 0))
        elif sv and vi:
            choices.append((0, 1))
        options = [
            (next_ui | (a << j), next_vi | (b << j))
            for next_ui, next_vi in options for a, b in choices
        ]
    return {(next_ui, ur | ui, next_vi, vr | vi)
            for next_ui, next_vi in options}


def reachable(n):
    start = (1, 0, 1, 2)  # initial seed=0, vaccinated vertex=1
    seen = {start}
    pending = deque([start])
    while pending:
        current = pending.popleft()
        for follow in successors(n, current):
            if follow not in seen:
                seen.add(follow)
                pending.append(follow)
    return seen


def is_counterexample(state, n):
    ui, ur, vi, vr = state
    if ui or vi:
        return False
    # Ignore index 0 (original seed) and 1 (vaccinated vertex).
    targets = ((1 << n) - 1) & ~3
    return bool((vr & ~ur) & targets)


def contact_step(n, state, round_index, success):
    infectious, removed = state
    next_infected = 0
    for u, v, t in success:
        if t == round_index and infectious & (1 << u):
            if not ((infectious | removed) & (1 << v)):
                next_infected |= 1 << v
    return next_infected, removed | infectious


def exact_six_witness():
    # Six vertices 0 (seed), 1 (vaccinated), 2, 4, 3, 5 (target).
    # Contact outcomes are fixed independently of vaccination.
    successes = {(0, 1, 0), (0, 2, 0),
                 (1, 3, 1), (2, 4, 1),
                 (4, 3, 2), (3, 5, 3)}
    unvaccinated = (1, 0)
    vaccinated = (1, 2)
    for t in range(6):
        unvaccinated = contact_step(6, unvaccinated, t, successes)
        vaccinated = contact_step(6, vaccinated, t, successes)
    assert unvaccinated[0] == 0 and vaccinated[0] == 0
    assert not (unvaccinated[1] & (1 << 5))
    assert vaccinated[1] & (1 << 5)
    return unvaccinated, vaccinated


def main():
    states = reachable(5)
    assert len(states) == 140, len(states)
    assert not any(is_counterexample(s, 5) for s in states)
    # This also covers every smaller population by adding isolated vertices.
    witness = exact_six_witness()
    # Check that a six-vertex nonmonotone coupled trajectory is algorithmically possible.
    assert any(is_counterexample(s, 6) for s in reachable(6))
    print('PASS: 140 exhaustive paired states for five vertices')
    print('PASS: no terminal collateral infection on <= five vertices')
    print('PASS: exact six-vertex timed contact witness:', witness)
    print('PASS: six-vertex witness also found by universal-state enumeration')


if __name__ == '__main__':
    main()
