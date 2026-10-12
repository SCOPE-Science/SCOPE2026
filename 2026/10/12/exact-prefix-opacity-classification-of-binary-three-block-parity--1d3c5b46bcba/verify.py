#!/usr/bin/env python3
"""Reproduce the exact prefix-opacity census for binary three-block parity counters.

Uses only the Python standard library.  The state partition and path search are
finite exhaustive algorithms; their mathematical justification is in RESULT.md.
"""
from collections import defaultdict, deque
from itertools import product

BLOCKS = tuple(''.join(b) for b in product('01', repeat=3))
EXPECTED = {
    2: {0, 68, 136, 204},
    3: {85, 170},
    4: {255},
}


def raw_machine(mask):
    marked = {BLOCKS[i] for i in range(8) if (mask >> i) & 1}
    suffixes = ('', '0', '1', '00', '01', '10', '11')
    states = tuple((suffix, parity) for suffix in suffixes for parity in (0, 1)) + ('L',)
    output = {s: (0 if s == 'L' else s[1]) for s in states}
    delta = {}
    for s in states:
        for bit in '01':
            if s == 'L':
                delta[s, bit] = 'L' if bit == '0' else ('1', 0)
            else:
                suffix, parity = s
                extension = suffix + bit
                parity ^= (len(extension) == 3 and extension in marked)
                new_suffix = extension if len(extension) < 3 else extension[-2:]
                delta[s, bit] = (new_suffix, parity)
    return states, output, delta


def minimized_machine(mask):
    states, output, delta = raw_machine(mask)
    reachable = ['L']
    visited = {'L'}
    for s in reachable:
        for bit in '01':
            nxt = delta[s, bit]
            if nxt not in visited:
                visited.add(nxt)
                reachable.append(nxt)
    partition = {s: output[s] for s in reachable}
    # Each iteration refines by one additional input-symbol observation.
    while True:
        signatures = {
            s: (partition[s], partition[delta[s, '0']], partition[delta[s, '1']])
            for s in reachable
        }
        keys = {sig: i for i, sig in enumerate(sorted(set(signatures.values())))}
        refined = {s: keys[signatures[s]] for s in reachable}
        if len(set(refined.values())) == len(set(partition.values())):
            partition = refined
            break
        partition = refined
    quotient = {}
    out = {}
    for s in reachable:
        state = partition[s]
        quotient[state] = (partition[delta[s, '0']], partition[delta[s, '1']])
        out[state] = output[s]
    assert len(quotient) == len(set(partition.values()))
    return partition['L'], quotient, out


def least_inhomogeneous_path(initial, delta):
    # mask has 2 bits per target state, recording which incoming labels
    # have occurred on the current path. BFS is exhaustive over all
    # homogeneous finite paths up to their first conflict.
    queue = deque([(initial, 0, '')])
    seen = {(initial, 0)}
    while queue:
        state, used, word = queue.popleft()
        for digit in (0, 1):
            target = delta[state][digit]
            if used & (1 << (2 * target + (1 - digit))):
                return len(word) + 1, word + str(digit), len(seen)
            new_used = used | (1 << (2 * target + digit))
            pair = (target, new_used)
            if pair not in seen:
                seen.add(pair)
                queue.append((target, new_used, word + str(digit)))
    return 0, None, len(seen)


def direct_count(mask, n):
    digits = bin(n)[2:]
    return sum((mask >> BLOCKS.index(digits[j:j+3])) & 1
               for j in range(len(digits) - 2)) % 2


def machine_output(initial, delta, output, n):
    state = initial
    for digit in bin(n)[2:]:
        state = delta[state][int(digit)]
    return output[state]


def main():
    classes = defaultdict(set)
    max_configs = 0
    max_states = 0
    examples = {}
    for mask in range(256):
        initial, delta, output = minimized_machine(mask)
        assert all(machine_output(initial, delta, output, n) == direct_count(mask, n)
                   for n in range(2048)), ('digit-count disagreement', mask)
        shortest, witness, configs = least_inhomogeneous_path(initial, delta)
        classes[shortest].add(mask)
        max_configs = max(max_configs, configs)
        max_states = max(max_states, len(delta))
        if shortest:
            examples[mask] = witness
    assert classes[0] == set(range(256)) - set.union(*EXPECTED.values())
    assert {k: classes[k] for k in EXPECTED} == EXPECTED
    assert set(classes) == {0, 2, 3, 4}
    assert sum(map(len, classes.values())) == 256
    print('VERIFY_OK total=256 transparent=249 opacity_one=4 '
          'opacity_half=2 opacity_quarter=1 '
          f'max_minimal_states={max_states} max_bfs_configurations={max_configs}')
    print('exception_witnesses=' + str(dict(sorted(examples.items()))))

if __name__ == '__main__':
    main()
