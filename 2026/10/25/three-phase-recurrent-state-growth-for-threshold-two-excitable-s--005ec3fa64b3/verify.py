"""Finite exhaustive certificate for three-state threshold-two excitation on split graphs.

Only Python's standard library is needed. Execute: python verify.py
"""
from itertools import product
from math import factorial


def site_step(state, signal):
    if state == 1:
        return 2
    if state == 2:
        return 0
    return 1 if signal else 0


def reduced_counts(weights, phases):
    counts = [0, 0, 0]
    for weight, phase in zip(weights, phases):
        counts[phase] += weight
    return counts


def reduced_step(core_weights, fringe_weights, phases):
    core = reduced_counts(core_weights, phases[:3])
    fringe = reduced_counts(fringe_weights, phases[3:])
    core_signal = core[1] + fringe[1] >= 2
    fringe_signal = core[1] >= 2
    return tuple(site_step(s, core_signal) for s in phases[:3]) + tuple(
        site_step(s, fringe_signal) for s in phases[3:]
    )


def admissible(core, fringe):
    return all(
        core[j] == 0 or core[(j + 1) % 3] + fringe[(j + 1) % 3] >= 2
        for j in range(3)
    ) and all(
        fringe[j] == 0 or core[(j + 1) % 3] >= 2
        for j in range(3)
    )


def multinomial(n, v):
    return factorial(n) // (factorial(v[0]) * factorial(v[1]) * factorial(v[2]))


def census(a, b):
    total = 1
    for c0 in range(a + 1):
        for c1 in range(a - c0 + 1):
            c = (c0, c1, a - c0 - c1)
            for i0 in range(b + 1):
                for i1 in range(b - i0 + 1):
                    i = (i0, i1, b - i0 - i1)
                    if admissible(c, i):
                        total += multinomial(a, c) * multinomial(b, i)
    return total


def direct_step(state, a):
    c = state[:a]
    f = state[a:]
    signal_c = c.count(1) + f.count(1) >= 2
    signal_f = c.count(1) >= 2
    return tuple(site_step(s, signal_c) for s in c) + tuple(
        site_step(s, signal_f) for s in f
    )


def test():
    checked = 0
    first = (0, 1, 2, 0, 1, 2)
    for weights in product(range(3), repeat=6):
        phases = first
        trajectory = [phases]
        for t in range(8):
            phases = reduced_step(weights[:3], weights[3:], phases)
            trajectory.append(phases)
        assert all(
            weights[j] == 0 or trajectory[5][j] == trajectory[8][j]
            for j in range(6)
        ), ('five-step identity', weights)
        on_cycle = all(
            weights[j] == 0 or trajectory[0][j] == trajectory[3][j]
            for j in range(6)
        )
        is_zero = all(
            weights[j] == 0 or first[j] == 0 for j in range(6)
        )
        predicted = is_zero or admissible(weights[:3], weights[3:])
        assert on_cycle == predicted, ('recurrent classification', weights)
        checked += 1
    assert checked == 729

    # Direct labelled dynamics, not using the six-class simulator.
    labelled = 0
    for a, b in ((1, 1), (2, 4), (3, 3), (4, 2), (4, 3),
                 (5, 1), (5, 2), (5, 3), (6, 1), (6, 2), (7, 1)):
        periodic = 0
        for state in product(range(3), repeat=a+b):
            s = state
            states = [s]
            for t in range(8):
                s = direct_step(s, a)
                states.append(s)
            assert states[5] == states[8], (a, b, state)
            if states[0] == states[3]:
                periodic += 1
            labelled += 1
        assert periodic == census(a, b), ('census', a, b, periodic)
    for b in range(1, 12):
        assert census(4, b) == 1 + 18 * (2**b - 1 - b)
        assert census(5, b) == 1 + 150 * (2**b - 1) - 60 * b
    assert all(census(a, b) == 1 for a in range(1, 4) for b in range(1, 12))
    assert census(4, 1) == 1 and census(4, 2) > 1
    assert census(5, 1) > 1 and census(6, 1) > 1

    witness = (0, 0, 1, 1, 2, 2)
    states = [witness]
    for _ in range(5):
        states.append(direct_step(states[-1], 3))
    assert states[4] != (0,) * 6 and states[5] == (0,) * 6
    assert states[4] != states[1]
    print('FINITE_CERTIFICATE_OK: all 729 saturated six-class types')
    print('DIRECT_CHECK_OK: %d labelled states' % labelled)
    print('EXACT_FORMULA_OK: a=4,5, b=1..11 and extinction at a<=3')
    print('SHARPNESS_OK: split graph a=3, b=3, state', witness)
    print('WITNESS_TRAJECTORY:', ' -> '.join(''.join(map(str, s)) for s in states))
    print('VERIFY_OK')


if __name__ == '__main__':
    test()
