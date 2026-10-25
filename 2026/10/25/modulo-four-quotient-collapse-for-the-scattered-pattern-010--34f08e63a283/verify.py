"""Reproducible finite checks for modular 010-subsequence DFA complexity.

This is a finite check, not a substitute for the parameter-uniform proof.
Python 3.9+ standard library only.
"""
from itertools import product


def count_010_by_positions(word):
    return sum(word[i] == '0' and word[j] == '1' and word[k] == '0'
               for i in range(len(word))
               for j in range(i + 1, len(word))
               for k in range(j + 1, len(word)))


def update(s, letter, m):
    x, y, z = s
    if letter == '0':
        return ((x + 1) % m, y, (z + y) % m)
    return (x, (y + x) % m, z)


def expected(m, residue):
    if m % 2:
        return m ** 3
    if m % 4 == 0 and residue % 2:
        return m ** 3 // 8
    return m ** 3 // 2


def automaton(m):
    states = [(0, 0, 0)]
    index = {states[0]: 0}
    transitions = []
    for s in states:
        row = []
        for a in '01':
            t = update(s, a, m)
            if t not in index:
                index[t] = len(states)
                states.append(t)
            row.append(index[t])
        transitions.append(tuple(row))
    return states, transitions


def minimal_size(states, transitions, residue):
    # Successively refine the output partition by two transition preimages.
    colors = [int(z == residue) for x, y, z in states]
    old_count = len(set(colors))
    while True:
        keys = [(colors[i], colors[u], colors[v])
                for i, (u, v) in enumerate(transitions)]
        class_index = {}
        fresh = [class_index.setdefault(k, len(class_index)) for k in keys]
        num = len(class_index)
        if num == old_count:
            return num
        assert num > old_count
        colors = fresh
        old_count = num


def main():
    checked = 0
    residues = 0
    for m in range(2, 15):
        states, transitions = automaton(m)
        reachable = m**3 if m % 2 else m**3 // 2
        assert len(states) == reachable, (m, len(states), reachable)
        for residue in range(m):
            got = minimal_size(states, transitions, residue)
            assert got == expected(m, residue), (m, residue, got,
                                                   expected(m, residue))
            residues += 1
        checked += 1
    # Compare automaton output to an independent triple-position count.
    num_words = 0
    for size in range(12):
        for bits in product('01', repeat=size):
            word = ''.join(bits)
            direct = count_010_by_positions(word)
            for m in (2, 3, 4, 5, 6, 8, 9, 12):
                state = (0, 0, 0)
                for bit in word:
                    state = update(state, bit, m)
                assert state[2] == direct % m, (word, m, state)
            num_words += 1
    # Verify the parity obstruction separately from automaton minimization.
    for m in (2, 4, 6, 8, 12):
        states, _ = automaton(m)
        assert all(z % 2 == (x - 1) * y % 2 for x, y, z in states)
    print('VERIFY_OK', 'moduli=', checked, 'residues=', residues,
          'words=', num_words, 'largest_reachable=', 13**3)


if __name__ == '__main__':
    main()
