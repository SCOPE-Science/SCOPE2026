#!/usr/bin/env python3
"""Independent finite checks of rank/atom-incomparability invariants.

The mathematical theorem is proved symbolically in RESULT.md; these checks
are finite corroboration, not a substitute for the universal argument.
"""
from itertools import product

MAX_SIDE = 18
cases = 0
pairs = 0
for m in range(1, MAX_SIDE + 1):
    for n in range(1, MAX_SIDE + 1):
        points = list(product(range(m), range(n)))
        levels = {p: sum(p) for p in points}
        height = max(levels.values())
        assert height == m + n - 2
        atoms = [p for p in points if levels[p] == 1]
        possible = []
        gaps = []
        for p in points:
            for q in points:
                if ((p[0] < q[0] and p[1] > q[1]) or
                        (p[0] > q[0] and p[1] < q[1])):
                    gaps.append(abs(levels[p] - levels[q]))
                    pairs += 1
                    if p in atoms:
                        possible.append(levels[q])
        if min(m, n) == 1:
            assert not gaps and not possible
            recovered = (1, height + 1)
        else:
            assert possible
            max_at_atom = max(possible)
            assert set(possible) == set(range(1, max(m, n)))
            assert max_at_atom == max(m, n) - 1
            assert max(gaps) == max(m, n) - 2
            recovered = (height - max_at_atom + 1, max_at_atom + 1)
        assert recovered == tuple(sorted((m, n)))
        cases += 1
print(f'PASS: checked {cases} ordered rectangles with side lengths 1..{MAX_SIDE}.')
print(f'PASS: checked {pairs} ordered incomparable pairs.')
print('PASS: height and atom-incomparability rank spectra reconstruct both side lengths.')
