#!/usr/bin/env python3
"""Independent finite tests for a closed-form factor/suffix automaton.

No third-party modules are required. Exhaustive tests do not replace the proof.
"""
from collections import Counter, defaultdict


def zimin_word(rank):
    word = ()
    for letter in range(1, rank + 1):
        word = word + (letter,) + word
    return word


def predicted_transition(rank, state, letter):
    if not 1 <= letter <= rank:
        return None
    if state == 0:
        return 1 << (letter - 1)
    block = state.bit_length()
    if state == (1 << block) - 1:
        return (1 << (letter - 1)) if letter > block else None
    next_position = state + 1
    expected_letter = (next_position & -next_position).bit_length()
    return next_position if letter == expected_letter else None


def canonical_suffix_automaton(word):
    transitions = [{}]
    links = [-1]
    lengths = [0]
    last = 0
    for letter in word:
        current = len(transitions)
        transitions.append({})
        links.append(0)
        lengths.append(lengths[last] + 1)
        state = last
        while state >= 0 and letter not in transitions[state]:
            transitions[state][letter] = current
            state = links[state]
        if state < 0:
            links[current] = 0
        else:
            follow = transitions[state][letter]
            if lengths[state] + 1 == lengths[follow]:
                links[current] = follow
            else:
                clone = len(transitions)
                transitions.append(transitions[follow].copy())
                links.append(links[follow])
                lengths.append(lengths[state] + 1)
                while state >= 0 and transitions[state].get(letter) == follow:
                    transitions[state][letter] = clone
                    state = links[state]
                links[follow] = clone
                links[current] = clone
        last = current
    return transitions, lengths


def verify(rank, exhaustive):
    word = zimin_word(rank)
    length = len(word)
    assert length == (1 << rank) - 1
    for position, letter in enumerate(word, 1):
        assert letter == (position & -position).bit_length()

    counts = Counter()
    for state in range(length + 1):
        for letter in range(1, rank + 1):
            target = predicted_transition(rank, state, letter)
            if target is not None:
                assert 0 < target <= length
                counts[letter] += 1
    for letter in range(1, rank + 1):
        assert counts[letter] == (1 << (rank - letter)) + letter - 1
    assert sum(counts.values()) == length + rank * (rank - 1) // 2

    # Independent linear-time construction of the classical suffix automaton;
    # its canonical prefix-state IDs must agree with the explicit transition map.
    actual, longest_lengths = canonical_suffix_automaton(word)
    assert len(actual) == length + 1, (rank, len(actual), length)
    for state, arcs in enumerate(actual):
        assert longest_lengths[state] == state
        for letter in range(1, rank + 1):
            assert arcs.get(letter) == predicted_transition(rank, state, letter), (
                rank, state, letter, arcs.get(letter),
                predicted_transition(rank, state, letter))

    if exhaustive:
        ends = defaultdict(set)
        for start in range(length):
            for stop in range(start + 1, length + 1):
                ends[word[start:stop]].add(stop)
        factor_states = defaultdict(set)
        for factor, ending_positions in ends.items():
            state = 0
            for letter in factor:
                state = predicted_transition(rank, state, letter)
                assert state is not None
            assert state == min(ending_positions)
            factor_states[state].add(tuple(sorted(ending_positions)))
            suffix = factor == word[-len(factor):]
            is_final_suffix = state == (1 << state.bit_length()) - 1
            assert suffix == is_final_suffix
        assert len(factor_states) == length
        assert all(len(v) == 1 for v in factor_states.values())
        for state in range(1, length + 1):
            block = state.bit_length()
            j = state - (1 << (block - 1))
            expected_endings = tuple(
                (1 << (block - 1)) + j + (offset << block)
                for offset in range(1 << (rank - block)))
            assert next(iter(factor_states[state])) == expected_endings
        print(f'rank={rank}: {len(ends)} distinct factors, full end-position and suffix checks passed')
    else:
        print(f'rank={rank}: {length+1} states and {sum(counts.values())} arcs verified')


if __name__ == '__main__':
    for r in range(1, 12):
        verify(r, exhaustive=(r <= 7))
    print('ALL CHECKS PASSED')
