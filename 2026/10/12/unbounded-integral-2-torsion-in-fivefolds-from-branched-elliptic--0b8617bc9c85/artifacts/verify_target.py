#!/usr/bin/env python3
"""Exact finite presentation sanity checks for the integral fivefold invariant.

The universal topology is proved in RESULT.md; these checks only replay the
finite group abelianization counts and polynomial bookkeeping.
"""
from math import comb


def poly_mul(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, v in enumerate(a):
        for j, w in enumerate(b):
            out[i + j] += v * w
    return out


def poly_add(*polys):
    out = [0] * max(map(len, polys))
    for p in polys:
        for i, v in enumerate(p):
            out[i] += v
    return out


base = poly_mul([1, 0, 1, 0, 1, 0, 1, 0, 1], [1, 2, 1])
center = [1, 4, 6, 4, 1]
exceptional = poly_mul([0, 0, 1, 0, 1], center)
betti = poly_add(base, exceptional)
assert betti == [1, 2, 3, 6, 9, 10, 9, 6, 3, 2, 1], betti
assert betti == betti[::-1]
for r in range(2, 18, 2):
    # Abelianization of genus-one orbifold group has the mod-2 branch
    # generators, subject to the single all-ones relation.
    # Canonical coset representatives are r-bit words with final bit zero.
    reps = [v for v in range(1 << r) if not v & (1 << (r - 1))]
    assert len(reps) == 2 ** (r - 1)
    kernel = [v for v in reps if v.bit_count() % 2 == 0]
    assert len(kernel) == 2 ** (r - 2), (r, len(kernel))
    assert r % 2 == 0
    print('r=', r, 'genus=', (r // 2 + 1), 'torsion_exponent=', r - 2)
# Blow-up shift of the torsion in H^2(S) and H^3(S).
center_torsion = {2: 1, 3: 1}
shifts = [2, 4]
torsion_degrees = {k: sum(center_torsion.get(k - sh, 0) for sh in shifts)
                   for k in range(11)}
assert torsion_degrees == {k: int(k in (4, 5, 6, 7)) for k in range(11)}
# Integral oriented-manifold torsion duality pairs degrees k and 11-k.
assert all(torsion_degrees[k] == torsion_degrees[11 - k]
           for k in range(1, 11))
print('betti=', betti)
print('torsion degrees=', [k for k, v in torsion_degrees.items() if v])
print('VERIFY_OK')
