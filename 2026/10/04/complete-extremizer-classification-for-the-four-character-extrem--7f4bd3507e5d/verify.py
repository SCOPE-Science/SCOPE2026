#!/usr/bin/env python3
from itertools import permutations

MOD = 15

def triple_zero(exps):
    s = set(e % MOD for e in exps)
    return any(s == {(r) % MOD, (r + 5) % MOD, (r + 10) % MOD} for r in range(MOD))

def correlations(v):
    e0, e1, e2, e3 = v
    c1 = [e1 - e0, e2 - e1, e3 - e2]
    c2 = [e2 - e0, e3 - e1, e0 - e3]
    return c1, c2

# Exhaust the parametrization forced by C1=0 and then C2=0.
from_proof = set()
for p, q, r in permutations((0, 1, 2)):
    for s in range(MOD):
        # xi^s is t and t^5 = omega^q iff s == q (mod 3).
        if s % 3 != q:
            continue
        v = (0, (s + 5*p) % MOD, (2*s + 5*(p+q)) % MOD, (3*s) % MOD)
        c1, c2 = correlations(v)
        assert triple_zero(c1)
        assert triple_zero(c2)
        from_proof.add(v)

canonical = set()
for eps in (1, 2):
    for m in range(5):
        # t = xi^(3m), omega = xi^5.
        v = (0, (3*m + 5*eps) % MOD, (6*m + 5*eps) % MOD, (9*m) % MOD)
        c1, c2 = correlations(v)
        assert triple_zero(c1)
        assert triple_zero(c2)
        canonical.add(v)

assert from_proof == canonical
assert len(canonical) == 10

# The two explicit literature witnesses.
third_root = (0, 5, 5, 0)
fifteenth_root = (0, 1, 7, 3)
assert third_root in canonical
assert fifteenth_root in canonical

# Each epsilon-family is one orbit under character modulation m -> m+1.
for eps in (1, 2):
    family = {(0, (3*m + 5*eps) % MOD, (6*m + 5*eps) % MOD, (9*m) % MOD) for m in range(5)}
    assert len(family) == 5

print('VERIFY_OK normalized_extremizers=10 modulation_orbits=2')
