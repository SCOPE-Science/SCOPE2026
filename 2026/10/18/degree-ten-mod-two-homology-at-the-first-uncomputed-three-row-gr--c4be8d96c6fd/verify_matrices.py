#!/usr/bin/env python3
"""Independently check the two mod-two boundary certificates by bitset elimination."""
from pathlib import Path
cases = [
    ('certificates/ascending_mod2.txt', 122, 393, 120),
    ('certificates/descending_mod2.txt', 30, 301, 28),
]
for name, nrows, ncols, expected_rank in cases:
    text = Path(name).read_text(encoding='utf-8').splitlines()
    assert len(text) == nrows
    seen, rows = set(), []
    for line in text:
        key, bits = line.split()
        assert key.isdigit() and key not in seen
        seen.add(key)
        assert len(bits) == ncols and set(bits) <= {'0', '1'}
        rows.append(int(bits, 2))
    pivots = {}
    for row in rows:
        while row:
            h = row.bit_length() - 1
            if h not in pivots:
                pivots[h] = row
                break
            row ^= pivots[h]
    rank = len(pivots)
    assert rank == expected_rank
    assert nrows - rank == 2
    assert ncols - rank == 273
    print(f'{name}: {nrows}x{ncols}, rank={rank}, Betti_10=2, Betti_9=273')
print('Both independent certificates PASS.')
