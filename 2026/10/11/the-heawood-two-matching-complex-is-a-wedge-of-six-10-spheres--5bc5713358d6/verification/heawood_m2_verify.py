#!/usr/bin/env python3
from collections import Counter
from functools import lru_cache
from math import gcd

# Heawood graph: points 0,...,6 and lines 7,...,13. Point j is incident
# to line 7+i exactly when j-i mod 7 is in {0,1,3}.
NV = 14
EDGES = sorted((j, 7+i) for j in range(7) for i in range(7)
               if (j-i) % 7 in {0,1,3})
M = len(EDGES)
assert M == 21

def is_two_matching(mask: int) -> bool:
    deg = [0] * NV
    x = mask
    while x:
        b = x & -x
        i = b.bit_length() - 1
        x -= b
        a, c = EDGES[i]
        deg[a] += 1
        deg[c] += 1
        if deg[a] > 2 or deg[c] > 2:
            return False
    return True

# Exhaustive simplicial complex.
faces = [mask for mask in range(1, 1 << M) if is_two_matching(mask)]
face_set = set(faces)
face_vector = Counter(mask.bit_count() - 1 for mask in faces)
expected_face_vector = {
    0: 21, 1: 210, 2: 1316, 3: 5733, 4: 18228, 5: 43246,
    6: 76968, 7: 101892, 8: 98042, 9: 65730, 10: 28560,
    11: 7091, 12: 798, 13: 24,
}
assert len(faces) == 447859
assert dict(sorted(face_vector.items())) == expected_face_vector

# Repeated element toggling in the fixed edge order. This is the standard
# acyclic matching obtained by applying element matchings successively.
unmatched = set(faces)
pair_up = {}
pair_low = {}
for e in range(M):
    lows = [x for x in unmatched
            if not ((x >> e) & 1) and (x | (1 << e)) in unmatched]
    for low in lows:
        high = low | (1 << e)
        if low in unmatched and high in unmatched:
            assert high in face_set
            assert low.bit_count() + 1 == high.bit_count()
            unmatched.remove(low)
            unmatched.remove(high)
            pair_up[low] = high
            pair_low[high] = low

# Pairing is disjoint and exhaustive except for the stated critical cells.
assert len(pair_up) == len(pair_low) == 223925
assert 2 * len(pair_up) + len(unmatched) == len(faces)
crit = sorted(unmatched, key=lambda x: (x.bit_count(), x))
crit_counts = Counter(mask.bit_count() - 1 for mask in crit)
assert crit_counts == Counter({10: 7, 9: 1, 0: 1})

critical_9 = [c for c in crit if c.bit_count() == 10]
critical_10 = [c for c in crit if c.bit_count() == 11]
assert len(critical_9) == 1 and len(critical_10) == 7
beta = critical_9[0]

# Oriented simplicial incidence number <d sigma, tau> for tau a codimension-1 face.
def incidence(sigma: int, tau: int) -> int:
    removed = sigma ^ tau
    assert removed and removed & (removed - 1) == 0
    r = removed.bit_length() - 1
    vertices = [i for i in range(M) if (sigma >> i) & 1]
    return -1 if vertices.index(r) % 2 else 1

# Algebraic discrete-Morse projection in dimensions 10 -> 9.
# For a matched 9-cell tau with upper partner sigma and incidence a=±1,
# eliminate tau using tau = -a * sum_{tau' != tau}<d sigma,tau'> tau'.
memo = {beta: 1}
active = set()

def projection_to_beta(tau: int) -> int:
    if tau in memo:
        return memo[tau]
    if tau in active:
        raise AssertionError("gradient cycle detected")
    active.add(tau)
    sigma = pair_up.get(tau)
    if sigma is None:
        value = 0
    else:
        a = incidence(sigma, tau)
        value = 0
        x = sigma
        while x:
            b = x & -x
            x -= b
            other = sigma ^ b
            if other == tau:
                continue
            if other.bit_count() == 10 and other in face_set:
                value += (-a) * incidence(sigma, other) * projection_to_beta(other)
    active.remove(tau)
    memo[tau] = value
    return value

boundary = []
for alpha in critical_10:
    coeff = 0
    x = alpha
    while x:
        b = x & -x
        x -= b
        tau = alpha ^ b
        if tau in face_set:
            coeff += incidence(alpha, tau) * projection_to_beta(tau)
    boundary.append(coeff)

assert boundary == [1, 1, 0, 0, 0, -1, 1]
assert gcd(*[abs(x) for x in boundary]) == 1

# Euler characteristic independently checks the reduced rank expected from the Morse complex.
chi = sum(((-1) ** d) * c for d, c in face_vector.items())
assert chi == 7
assert chi - 1 == 6

# A Morse CW model has one 0-cell, one 9-cell, and seven 10-cells.
# Since pi_9(S^9)=Z, the attaching map is classified by this primitive row.
# A unimodular change of basis sends it to (1,0,...,0), giving a contractible
# 9/10-cell pair and six free 10-cells.
print("HEAWOOD_M2_VERIFY_OK")
print("faces=447859 pairs=223925 critical=(1 in d0, 1 in d9, 7 in d10)")
print("morse_boundary=" + repr(boundary) + " reduced_euler=6")
