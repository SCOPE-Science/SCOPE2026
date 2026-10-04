#!/usr/bin/env python3
from collections import deque
import json

N = 7
FULL = (1 << N) - 1

# Theorem 3 construction of de Bondt--Don--Zantema, specialized to n=7.
# States 1,...,7 are represented internally by bits 0,...,6.
TRANS = {
    'a': [2,3,4,5,6,7,1],
    'b': [1,3,3,4,5,6,7],
    'e': [3,4,4,5,6,7,1],
}

def image(mask, letter):
    out = 0
    t = TRANS[letter]
    for i in range(N):
        if mask >> i & 1:
            out |= 1 << (t[i] - 1)
    return out

def subset_bfs(alphabet):
    dist = {FULL: 0}
    count = {FULL: 1}
    q = deque([FULL])
    first_singleton = None
    while q:
        s = q.popleft()
        d = dist[s]
        if first_singleton is not None and d >= first_singleton:
            continue
        for x in alphabet:
            t = image(s, x)
            nd = d + 1
            if t not in dist:
                dist[t] = nd
                count[t] = count[s]
                q.append(t)
                if t and t & (t - 1) == 0:
                    first_singleton = nd if first_singleton is None else min(first_singleton, nd)
            elif dist[t] == nd:
                count[t] += count[s]
    if first_singleton is None:
        raise AssertionError('automaton did not synchronize')
    by_target = {}
    for state in range(N):
        m = 1 << state
        if dist.get(m) == first_singleton:
            by_target[str(state + 1)] = count[m]
    return {
        'alphabet': ''.join(alphabet),
        'shortest_length': first_singleton,
        'shortest_count': sum(by_target.values()),
        'count_by_target_state': by_target,
        'reachable_subsets': len(dist),
    }

def apply_word(word):
    s = FULL
    for x in word:
        s = image(s, x)
    return s

def singleton_state(mask):
    if mask == 0 or mask & (mask - 1):
        return None
    return mask.bit_length()

# Published witness for A^{-cd}: (e a^{n-2})^{n-2} a e.
witness = ('e' + 'a' * (N - 2)) * (N - 2) + 'a' + 'e'
assert len(witness) == N * N - 3 * N + 4 == 32
assert singleton_state(apply_word(witness)) is not None

results = {
    'n': N,
    'published_witness': witness,
    'published_witness_length': len(witness),
    'published_witness_target_state': singleton_state(apply_word(witness)),
    'two_letter': subset_bfs(('a','e')),
    'three_letter': subset_bfs(('a','b','e')),
}

assert results['two_letter']['shortest_length'] == 32
assert results['two_letter']['shortest_count'] == 331_776
assert results['two_letter']['count_by_target_state'] == {'4': 331_776}
assert results['three_letter']['shortest_length'] == 32
assert results['three_letter']['shortest_count'] == 1_327_104
assert results['three_letter']['count_by_target_state'] == {'3': 663_552, '4': 663_552}
assert results['three_letter']['shortest_count'] == 4 * results['two_letter']['shortest_count']

print(json.dumps(results, sort_keys=True, separators=(',', ':')))
print('VERIFY_OK')
