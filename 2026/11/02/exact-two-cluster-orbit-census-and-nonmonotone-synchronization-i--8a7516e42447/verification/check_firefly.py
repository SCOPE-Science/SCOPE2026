#!/usr/bin/env python3
"""Separately implemented finite-state checks for the entry-trigger, parallel quorum map.
No finite check is used as an infinite-parameter proof.
"""
from collections import defaultdict


def step(x, y, C, w):
    s = C - w
    a, b = (x + 1) % C, (y + 1) % C
    advance_a = int(a == s and b >= s)
    advance_b = int(b == s and a >= s)
    return (a + advance_a) % C, (b + advance_b) % C


def agent_step(x, y, C, w, group_size):
    z = [x] * group_size + [y] * group_size
    a = [(q + 1) % C for q in z]
    flash = [q >= C - w for q in a]
    extra = []
    for i, phase in enumerate(a):
        n_flash = sum(flash[j] for j in range(2 * group_size) if j != i)
        extra.append(int(phase == C - w and 2 * n_flash > 2 * group_size - 1))
    out = [(phase + boost) % C for phase, boost in zip(a, extra)]
    assert len(set(out[:group_size])) == 1
    assert len(set(out[group_size:])) == 1
    return out[0], out[group_size]


def cycle_census(C, w):
    f = {(x, y): step(x, y, C, w) for x in range(C) for y in range(C)}
    cycle_by_state = {}
    cycles = {}
    for start in f:
        if start in cycle_by_state:
            continue
        local = {}
        path = []
        state = start
        while state not in local and state not in cycle_by_state:
            local[state] = len(path)
            path.append(state)
            state = f[state]
        if state in cycle_by_state:
            label = cycle_by_state[state]
        else:
            cyc = path[local[state]:]
            label = min(cyc)
            cycles[label] = cyc
        for state in path:
            cycle_by_state[state] = label
    basins = defaultdict(int)
    for label in cycle_by_state.values():
        basins[label] += 1
    return cycles, basins, f


def wave(C, w, k):
    s = C - w
    return ({(x, (x + k) % C) for x in range(s)}
            | {(x, (x + k) % C) for x in range(C + s - k + 1, C)}
            | {(x, (x + k - 1) % C) for x in range(s + 1, C + s - k + 1)})


def test_range(max_C=72):
    cases = states = 0
    for C in range(4, max_C + 1):
        for w in range(1, C):
            s = C - w
            J = max(0, C - 2 * w + 1)
            K = max(0, 2 * w - C - 2)
            cycles, basin, f = cycle_census(C, w)
            expected = {(0, 0): C - 1}
            expected.update({(0, d): C for d in range(w, s + 1)})
            expected.update({(0, k): C - 1 for k in range(s + 2, w)})
            assert set(cycles) == set(expected), (C, w, 'cycle labels', cycles.keys(), expected.keys())
            assert all(len(cycles[k]) == expected[k] for k in cycles), (C, w, 'cycle periods')
            for k, cyc in cycles.items():
                if k == (0, 0):
                    assert basin[k] == C * C - J * C - K * (C + 1)
                elif len(cyc) == C:
                    assert basin[k] == C
                else:
                    assert basin[k] == C + 1
                    parameter = k[1]
                    assert set(cyc) == wave(C, w, parameter)
                    extras = {(s, s + parameter - 1), (C + s - parameter, s)}
                    assert all(f[q] in cyc for q in extras)
                    assert all(q not in f.values() for q in extras)
                    assert all(q not in cyc for q in extras)
            assert sum(basin.values()) == C * C
            cases += 1
            states += C * C
    return cases, states


def main():
    group_cases = 0
    for C in range(4, 19):
        for w in range(1, C):
            for m in (1, 2, 5):
                for x in range(C):
                    for y in range(C):
                        assert step(x, y, C, w) == agent_step(x, y, C, w, m)
                        group_cases += 1
    ncase, states = test_range()
    print('PASS: agent-level parallel quorum agrees with two-clock reduction:', group_cases, 'instances')
    print('PASS: complete cycle, period, basin, and explicit-wave census:', ncase, 'parameter pairs;', states, 'states')
    for C, w in ((10, 3), (10, 5), (10, 6), (10, 7), (10, 9), (11, 6), (11, 7)):
        J = max(0, C - 2 * w + 1)
        K = max(0, 2 * w - C - 2)
        print(f'C={C} w={w} coasting={J} accelerated={K} synchrony_basin={C*C-J*C-K*(C+1)}/{C*C}')


if __name__ == '__main__':
    main()
