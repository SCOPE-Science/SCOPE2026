"""Independent finite tests for shifted binary digit-sum DFAOs.

Usage: python checker.py
No third-party packages are required.
"""
from collections import deque


def reachable(shift, modulus):
    states = [(shift, 0)]
    index = {states[0]: 0}
    transitions = []
    for d, a in states:
        edges = []
        for bit in (0, 1):
            z = d + bit
            target = (z // 2, (a + z % 2) % modulus)
            if target not in index:
                index[target] = len(states)
                states.append(target)
            edges.append(index[target])
        transitions.append(tuple(edges))
    return states, transitions


def quotient_classes(states, transitions, modulus):
    # Iterated Moore refinement, independently of the proposed formula.
    outputs = [(a + d.bit_count()) % modulus for d, a in states]
    current = outputs[:]
    for _ in range(len(states) + 2):
        signatures = [(outputs[i], current[edges[0]], current[edges[1]])
                      for i, edges in enumerate(transitions)]
        dictionary = {x: i for i, x in enumerate(sorted(set(signatures)))}
        refined = [dictionary[s] for s in signatures]
        if len(set(refined)) == len(set(current)):
            return len(set(refined))
        current = refined
    raise AssertionError('refinement failed to stabilize')


def explicit_count(shift, modulus):
    # Direct finite residue-pair formula; this does not traverse transition states.
    ell = shift.bit_length()
    positive = set()
    for h in range(ell + 1):
        power = 1 << h
        for y in range(shift, shift + power):
            d, low = divmod(y, power)
            if d:
                positive.add((d, low.bit_count() % modulus))
    return modulus + len(positive)


def output_for(states, transitions, bits, modulus):
    state = 0
    for bit in bits:
        state = transitions[state][bit]
    d, a = states[state]
    return (a + d.bit_count()) % modulus


def run():
    triples = 0
    tested_inputs = 0
    for modulus in range(2, 10):
        for shift in range(0, 129):
            states, transitions = reachable(shift, modulus)
            minimized = quotient_classes(states, transitions, modulus)
            predicted = explicit_count(shift, modulus)
            assert minimized == len(states) == predicted, (shift, modulus, predicted, minimized)
            if shift and shift & (shift - 1) == 0:
                r = shift.bit_length() - 1
                power_formula = modulus + sum(min(modulus, h + 1) for h in range(r + 1))
                assert predicted == power_formula
            for n in range(128):
                bits = [(n >> i) & 1 for i in range(7)]
                assert output_for(states, transitions, bits, modulus) == ((n + shift).bit_count() % modulus)
                tested_inputs += 1
            triples += 1
    print(f'CHECK_OK parameters={triples} direct_inputs={tested_inputs}')
    for shift in (0, 1, 2, 3, 4, 8, 16, 32, 64, 128):
        print('shift', shift, 'states_m2_m3_m4_m5', *(explicit_count(shift, m) for m in (2, 3, 4, 5)))


if __name__ == '__main__':
    run()
