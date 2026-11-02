#!/usr/bin/env python3
"""Independent arithmetic checks for the conductor-41 residue-sum theorem."""
from math import gcd

P = 41
G = 6
K = frozenset(pow(G, 8*j, P) for j in range(5))
assert K == frozenset({1, 10, 16, 18, 37})
assert min(j for j in range(1, P) if pow(G, j, P) == 1) == 40
COS = [frozenset((pow(G, j, P)*a) % P for a in K) for j in range(8)]
assert len(set.union(*map(set, COS))) == 40
assert all(len(c) == 5 for c in COS)
SUMS = [sum(c) for c in COS]
assert SUMS == [82, 82, 123, 123, 123, 123, 82, 82]
LOOKUP = {a: j for j, c in enumerate(COS) for a in c}


def prime(n):
    return n >= 2 and all(n % d for d in range(2, int(n**0.5) + 1))


checked = 0
cosets_checked = 0
witness_checked = False
for q in range(3, 251, 2):
    if q == P or not prime(q):
        continue
    modulus = P*q
    target = modulus*5*(q-1)//2
    qclass = LOOKUP[q % P]
    invclass = (-qclass) % 8
    expect = q*(SUMS[0] - SUMS[invclass])
    assert expect in (0, -P*q)
    assert (expect == 0) == (qclass in (0, 1, 2, 7))
    for j, c in enumerate(COS):
        H = [x for x in range(1, modulus)
             if x % P in c and x % q != 0]
        assert len(H) == 5*(q-1)
        delta = sum(H) - target
        assert delta == q*(SUMS[j] - SUMS[(j-qclass)%8])
        if j == 0:
            assert delta == expect
        cosets_checked += 1
    assert (all(SUMS[j] == SUMS[(j-qclass)%8] for j in range(8))) == (qclass == 0)
    # The two cyclic factors have orders 5 and q-1.
    assert (gcd(5, q-1) == 1) == ((q-1) % 5 != 0)
    if q == 3:
        H = [x for x in range(1, modulus) if x % P in K and x % q]
        assert H == [1, 10, 16, 37, 59, 83, 92, 98, 100, 119]
        assert sum(H) == 615
        assert sum(x for x in range(1, modulus)
                   if x % P in COS[1] and x % q) == 492
        witness_checked = True
    checked += 1
assert witness_checked

# Dirichlet progression census modulo 41*5, independent of primality.
R = [r for r in range(1, P*5) if gcd(r, P*5) == 1]
assert len(R) == 160
cyc = [r for r in R if r % 5 != 1]
centered = [r for r in cyc if LOOKUP[r % P] in (0, 1, 2, 7)]
all_cosets = [r for r in centered if LOOKUP[r % P] == 0]
assert (len(cyc), len(centered), len(all_cosets),
        len(centered) - len(all_cosets)) == (120, 60, 15, 45)
assert all(not prime(p) for p in (9, 25)) and prime(41)
assert not any(prime(p) and p < 41 and p % 16 == 9 for p in range(3, 41, 2))
print(f'VERIFY_OK prime_moduli={checked} cosets={cosets_checked} '
      f'density_classes=160:120:60:15:45 witness_modulus=123')
