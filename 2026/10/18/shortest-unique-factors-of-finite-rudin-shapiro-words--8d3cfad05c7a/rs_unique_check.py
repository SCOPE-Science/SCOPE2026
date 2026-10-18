"""Exact finite checks used in the accompanying mathematical proof.
Run: python3 rs_unique_check.py
Python 3.9+; no external dependencies.
"""
from collections import Counter
from itertools import product


def bit(i):
    return ((i & (i >> 1)).bit_count() & 1)


def prefix(exponent):
    return ''.join(str(bit(j)) for j in range(1 << exponent))


# Confirm finite base and a longer independent recurrence check.
A = (11, 12, 13, 14, 23, 24, 25, 26)
for exponent in range(9, 13):
    text = prefix(exponent)
    target = (1 << (exponent-5)) + 2
    assert all(not any(v == 1 for v in Counter(text[j:j+k] for j in range(len(text)-k+1)).values())
               for k in range(1, target))
    counts = Counter(text[j:j+target] for j in range(len(text)-target+1))
    starts = tuple(j for j in range(len(text)-target+1) if counts[text[j:j+target]] == 1)
    expected = tuple(a * (1 << (exponent - 5)) - 1 for a in A)
    assert starts == expected, (exponent, starts, expected)
    print('base_or_extension', exponent, 'size', len(text), 'minimum_unique_length', target, 'unique_starts', starts)

# Every 8-aligned RS block is one of these 4, depending on r(m), m mod 2.
blocks = {}
for m in range(16):
    key = (bit(m), m % 2)
    word = ''.join(str(bit(8*m+j)) for j in range(8))
    assert key not in blocks or blocks[key] == word
    blocks[key] = word
assert len(blocks) == 4
print('eight_blocks', sorted(blocks.items()))

# Unconditional phase certificate, valid even for impossible adjacent pairs.
phases = {}
for u, v in product(blocks.values(), repeat=2):
    two = u + v
    for offset in range(8):
        factor = two[offset:offset+8]
        phases.setdefault(factor, set()).add(offset)
assert len(phases) == 56
assert all(len(v) == 1 for v in phases.values())
print('eight_window_phase_certificate', 'distinct_factors', len(phases), 'collisions', 0)

# Any 14-window lies in three consecutive 8-blocks. The second
# component of the underlying state is the parity of its block index.
allow = []
for u, v, w in product(blocks, repeat=3):
    if u[1] != v[1] and v[1] != w[1]:
        allow.append(blocks[u] + blocks[v] + blocks[w])
assert len(allow) == 16
all14 = {triple[t:t+14] for triple in allow for t in range(8)}
assert len(all14) == 104
w10 = prefix(10)
f14 = Counter(w10[i:i+14] for i in range(len(w10)-13))
assert all(f14[x] >= 2 for x in all14)
print('short_factor_certificate', 'allowed_state_triples', 16,
      'distinct_length14_factors', 104,
      'min_occurrences_in_first1024', min(f14[x] for x in all14))
print('ALL CHECKS PASS')
