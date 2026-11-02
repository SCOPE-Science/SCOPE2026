#!/usr/bin/env python3
"""Reconstruct the source necklace directly from each displayed BWT witness."""
from pathlib import Path

def direct_bwt(word):
    rotations = sorted(word[i:] + word[:i] for i in range(len(word)))
    return ''.join(row[-1] for row in rotations)

rows = Path('witness_table.tsv').read_text(encoding='utf-8').splitlines()
assert rows[0] == 'n\tsharp_images\twitness'
assert len(rows) == 19
for row in rows[1:]:
    a,b,L = row.split('\t')
    n = int(a)
    assert 13 <= n <= 30 and len(L) == n and all(x in '012' for x in L)
    assert all(L[i] != L[i + 1] for i in range(n - 1))
    inverse = [''] * n
    for _ in range(n):
        inverse = sorted(L[i] + inverse[i] for i in range(n))
    u = inverse[0]
    assert len(set(inverse)) == n, (n, 'nonprimitive')
    assert direct_bwt(u) == L, (n, 'BWT mismatch')
    assert sum(u[i] != u[(i+1) % n] for i in range(n)) == (n+1)//2
    print(n, L, 'OK')
print('DIRECT_BWT_WITNESSES_OK')
