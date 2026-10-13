#!/usr/bin/env python3
"""Cross-implementation equality of reachable terminal sets for every tested cycle."""
from verify_burning_cycles import terminal_code, boundary_count
from verify_burning_cycles_independent import code
for n in range(3,11):
    a, _, _=terminal_code(n)
    b, _=code(n)
    assert a==b, (n, len(a), len(b))
    print(f'n={n}: matching {len(a)} terminal words, maximal boundaries {max(boundary_count(w) for w in a)}')
print('ALL_TERMINAL_SETS_MATCH')
