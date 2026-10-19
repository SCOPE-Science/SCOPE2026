"""Check prefix-code decoder transitions and exact reset lengths at finite depths."""
from collections import deque


def automaton(m):
    assert m >= 2
    states = ['']
    for h in range(1, m):
        states.extend(format(i, f'0{h}b') for i in range(1 << h))
    states.append('1' * m)
    index = {s: k for k, s in enumerate(states)}
    assert len(states) == 1 << m
    transitions = []
    for state in states:
        successors = []
        for bit in '01':
            t = state + bit
            if len(t) < m or t == '1' * m:
                successors.append(index[t])
            else:
                successors.append(index[''])
        transitions.append(tuple(successors))
    return states, transitions


def step(mask, c, transitions):
    image = 0
    while mask:
        low = mask & -mask
        i = low.bit_length() - 1
        mask -= low
        image |= 1 << transitions[i][c]
    return image


def shortest(m):
    states, transitions = automaton(m)
    initial = (1 << len(states)) - 1
    todo = deque([initial])
    parents = {initial: (None, None)}
    terminal = None
    while todo:
        mask = todo.popleft()
        if mask.bit_count() == 1:
            terminal = mask
            break
        for bit in (0, 1):
            succ = step(mask, bit, transitions)
            if succ not in parents:
                parents[succ] = (mask, bit)
                todo.append(succ)
    assert terminal is not None
    letters = []
    k = terminal
    while parents[k][0] is not None:
        k, bit = parents[k]
        letters.append(str(bit))
    letters.reverse()
    return states, transitions, len(parents), ''.join(letters)


def verify(m):
    states, transitions, explored, shortest_word = shortest(m)
    expected = ('0' + '1' * m) * (m - 1) + '0'
    assert len(shortest_word) == len(expected) == m * m
    initial = (1 << len(states)) - 1
    mask = initial
    for bit in expected:
        mask = step(mask, int(bit), transitions)
    assert mask == 1  # root is the only image
    factor = '0' + '1' * m
    mask = initial
    for iteration in range(1, m):
        for bit in factor:
            mask = step(mask, int(bit), transitions)
        expected_states = {'1' * h for h in range(iteration, m + 1)}
        assert {states[k] for k in range(len(states)) if mask >> k & 1} == expected_states
    print(f'm={m:2d} states={len(states):4d} bfs_subsets={explored:7d} shortest={len(shortest_word):3d} verified')


if __name__ == '__main__':
    for m in range(2, 10):
        verify(m)
    print('All finite-state checks passed.')
