#!/usr/bin/env python3
"""Exact verification of a displayed finite cyclic orientable word.

Run with Python 3 from any working directory; only the Python standard library
and the adjacent witness.txt are required. No optimization software is needed.
"""
from collections import Counter
from hashlib import sha256
from pathlib import Path

s = Path(__file__).with_name('witness.txt').read_text(encoding='ascii').strip()
assert len(s) == 448, 'Period is not 448'
assert set(s) == set('0123'), 'Unexpected alphabet'
N = len(s)

# Independent direct cyclic-indexing implementation of the full window census.
windows = [tuple(s[(i+j) % N] for j in range(5)) for i in range(N)]
assert len(set(windows)) == N, 'An oriented window repeats'
assert all(t != t[::-1] for t in windows), 'A palindromic window exists'
canonical = [min(t, t[::-1]) for t in windows]
assert len(set(canonical)) == N, 'Two windows agree up to reversal'

# Independently reconstruct all cyclic windows by wraparound concatenation.
extended = s + s[:4]
windows2 = [extended[i:i+5] for i in range(N)]
assert {''.join(t) for t in windows} == set(windows2)
assert len(windows2) == len(set(windows2)) == N
for i, t in enumerate(windows2):
    assert t[::-1] not in set(windows2), ('Reverse factor', i)

# Balance checks provide auxiliary, independently reproducible statistics.
assert Counter(s) == {'0':112,'1':112,'2':112,'3':112}
assert N <= (4**5 - 4**3)//2  # reversal classes of nonpalindromes
print('CHECK_OK')
print('alphabet=4 order=5 cyclic_period=448')
print('distinct_length5_windows=448')
print('distinct_nonpalindromic_reversal_classes=448')
print('symbol_counts=0:112,1:112,2:112,3:112')
print('witness_sha256=' + sha256(s.encode('ascii')).hexdigest())
