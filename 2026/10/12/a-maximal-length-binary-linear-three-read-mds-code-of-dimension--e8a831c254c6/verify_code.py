#!/usr/bin/env python3
"""Reproduce the finite generator check for a binary three-read code."""
from collections import Counter
COLUMNS = (31, 6, 24, 12, 8, 25, 18, 27, 7, 19, 2, 29, 30, 23, 4, 5, 14, 13, 21, 15)
N = len(COLUMNS)
K = 5
assert N == 20 and all(0 <= c < (1 << K) for c in COLUMNS)
words = []
triple_zeros = []
for m in range(1 << K):
    v = tuple((m & g).bit_count() % 2 for g in COLUMNS)
    words.append(v)
    if m:
        z = sum(not any(v[(i+j)%N] for j in range(3)) for i in range(N))
        triple_zeros.append(z)
        assert z <= 2, (m,z)
assert len(set(words)) == 1 << K
assert max(triple_zeros) == 2
triple_counts = []
for i in range(N):
    n = sum(all(words[m][(i+j)%N] == 0 for j in range(3)) for m in range(1,1<<K))
    triple_counts.append(n)
assert all(c == 3 for c in triple_counts), triple_counts
assert sum(triple_zeros) == sum(triple_counts) == 3*N
assert sum(((72 + (1<<i)-1)//(1<<i)) for i in range(K)) == 140
assert 7*N == 140
assert 3*N <= 2*(2**K-1) < 3*(N+1)
print('VERIFY_OK binary_linear=[20,5] min_3_symbol_distance=18',
      'zero_triple_distribution=', dict(sorted(Counter(triple_zeros).items())),
      'total_zero_triples=',sum(triple_zeros),
      'all_cyclic_column_triplets_rank=3',
      'Griesmer=140=7*20')
