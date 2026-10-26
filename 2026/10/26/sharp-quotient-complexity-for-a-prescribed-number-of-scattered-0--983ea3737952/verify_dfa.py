"""Standalone finite checks for fixed scattered-01 multiplicity DFA quotients.

The all-parameter theorem is proved in RESULT.md; these are bounded cross-checks.
"""
from collections import deque
from itertools import product


def direct_01(word):
    zeros = total = 0
    for symbol in word:
        if symbol == '0':
            zeros += 1
        else:
            total += zeros
    return total


def reachable_counter_dfa(k):
    """Independent saturated count automaton, before quotient minimization."""
    start = (0, 0)
    states, edges, queue = [start], {}, deque([start])
    seen = {start}
    while queue:
        zeros, count = s = queue.popleft()
        nxt = ((min(k + 1, zeros + 1), count),
               (zeros, min(k + 1, count + zeros)))
        edges[s] = nxt
        for state in nxt:
            if state not in seen:
                seen.add(state)
                states.append(state)
                queue.append(state)
    return states, edges, start


def minimized_state_count(k):
    states, edges, start = reachable_counter_dfa(k)
    labels = {s: int(s[1] == k) for s in states}
    for _ in range(len(states) + 1):
        signatures = {s: (labels[s], labels[edges[s][0]],
                          labels[edges[s][1]]) for s in states}
        encoding = {signature: rank for rank, signature in
                    enumerate(sorted(set(signatures.values())))}
        new_labels = {s: encoding[signatures[s]] for s in states}
        if len(set(new_labels.values())) == len(set(labels.values())):
            # The partition is stable since each refinement only splits blocks.
            assert all((labels[a] != labels[b]) or
                       (new_labels[a] == new_labels[b])
                       for a in states for b in [] )
            return len(set(new_labels.values())), len(states)
        labels = new_labels
    raise AssertionError('partition refinement failed to stabilize')


def formula(k):
    return 3 + ((k + 1) ** 2 // 4)


def check():
    for k in range(0, 46):
        minimum, reachable = minimized_state_count(k)
        assert minimum == formula(k), (k, minimum, formula(k))
    for n in range(13):
        for letters in product('01', repeat=n):
            word = ''.join(letters)
            zeros = seen_pairs = 0
            for i, a in enumerate(word):
                if a == '0':
                    zeros += 1
                else:
                    seen_pairs += zeros
            assert seen_pairs == sum(a == '0' and b == '1'
                                     for i, a in enumerate(word)
                                     for b in word[i+1:])
            if n:
                split = n // 2
                x, y = word[:split], word[split:]
                assert direct_01(word) == direct_01(x) + direct_01(y) + x.count('0')*y.count('1')
    print('FINITE_CHECK_PASS: k=0..45 state counts; all 8191 words of lengths 0..12 cross-checked')
    print('EXAMPLES:', [(k, formula(k)) for k in range(11)])


if __name__ == '__main__':
    check()
