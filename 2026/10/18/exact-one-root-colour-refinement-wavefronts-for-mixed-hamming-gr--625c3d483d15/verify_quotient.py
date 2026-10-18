"""Independent exact-arithmetic orbit-quotient verification for products of cliques."""
from collections import Counter
from itertools import combinations_with_replacement, product
from math import prod


def canonical_coloring(coloring, states, neighbours):
    signatures = {}
    for state in states:
        neighbors = Counter()
        for next_state, weight in neighbours[state].items():
            neighbors[coloring[next_state]] += weight
        signatures[state] = (coloring[state], tuple(sorted(neighbors.items())))
    kinds = {signature: index for index, signature in enumerate(sorted(set(signatures.values())))}
    return {state: kinds[signatures[state]] for state in states}


def predicted_key(state, dimension, round_index):
    weight = sum(state)
    if round_index >= dimension:
        return ('orbit', state)
    if weight < round_index:
        return ('orbit', state)
    if weight == round_index:
        return ('shell', round_index)
    return ('outside',)


def check(qs):
    dimension = len(qs)
    values = tuple(sorted(set(qs)))
    counts = tuple(qs.count(q) for q in values)
    states = list(product(*(range(c + 1) for c in counts)))
    neighbours = {}
    for state in states:
        m = Counter()
        for j, (q, count) in enumerate(zip(values, counts)):
            if state[j]:
                target = list(state)
                target[j] -= 1
                m[tuple(target)] += state[j]
                m[state] += state[j] * (q - 2)
            if state[j] < count:
                target = list(state)
                target[j] += 1
                m[tuple(target)] += (count - state[j]) * (q - 1)
        neighbours[state] = m
    color = {s: int(any(s)) for s in states}
    rounds = dimension - 1 if len(values) == 1 else dimension
    for t in range(rounds + 2):
        label_to_predicted = {}
        predicted_to_label = {}
        for state in states:
            expected = predicted_key(state, dimension, t)
            observed = color[state]
            assert label_to_predicted.setdefault(observed, expected) == expected, (qs,t,state)
            assert predicted_to_label.setdefault(expected, observed) == observed, (qs,t,state)
        if t == rounds + 1:
            break
        new = canonical_coloring(color, states, neighbours)
        if t < rounds:
            assert len(set(new.values())) > len(set(color.values())), (qs,t)
        else:
            assert len(set(new.values())) == len(set(color.values())), (qs,t)
        color = new
    return len(states)


def main():
    cases = 0
    state_visits = 0
    for d in range(1, 9):
        for qs in combinations_with_replacement(range(2,8), d):
            states = check(qs)
            state_visits += states
            cases += 1
    for d in (9, 10, 12, 15):
        for qs in ((2,) * (d-1)+(3,), tuple(2 + i%3 for i in range(d)), (2,)*d):
            state_visits += check(qs)
            cases += 1
    print(f'PASS exact orbit-quotient wavefront partitions, {cases} factor tuples, {state_visits} quotient states')

if __name__ == '__main__':
    main()
