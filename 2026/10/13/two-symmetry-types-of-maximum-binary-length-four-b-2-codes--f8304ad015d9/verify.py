#!/usr/bin/env python3
from itertools import combinations, permutations
from collections import Counter
import hashlib

N = 4
VERTICES = tuple(range(1 << N))
POW3 = tuple(3 ** i for i in range(N))


def sum_code(a, b):
    s = 0
    for i in range(N):
        s += (((a >> i) & 1) + ((b >> i) & 1)) * POW3[i]
    return s


def is_b2(code):
    code = tuple(code)
    seen = set()
    for i, a in enumerate(code):
        for b in code[i:]:
            z = sum_code(a, b)
            if z in seen:
                return False
            seen.add(z)
    return True


def permute_bits(x, perm):
    y = 0
    for out_pos, in_pos in enumerate(perm):
        y |= ((x >> in_pos) & 1) << out_pos
    return y


def hamming(a, b):
    return (a ^ b).bit_count()

# Complete upper-bound check: no 8-subset is B2. Since B2 is hereditary,
# this excludes every larger subset as well.
eight_checked = 0
for C in combinations(VERTICES, 8):
    eight_checked += 1
    if is_b2(C):
        raise AssertionError(f"unexpected size-8 B2 code: {C}")
assert eight_checked == 12870

# Complete equality census at size 7.
maxima = []
for C in combinations(VERTICES, 7):
    if is_b2(C):
        maxima.append(tuple(C))
assert len(maxima) == 240
maxima_set = set(maxima)
assert sum(0 in C for C in maxima) == 105

# The OEIS witness is one of the maxima.
A = tuple(sorted(int(x, 2) for x in [
    "0000", "0001", "0010", "0100", "0111", "1001", "1110"
]))
B = tuple(sorted(int(x, 2) for x in [
    "0000", "0001", "0010", "0111", "1011", "1100", "1111"
]))
assert A in maxima_set and B in maxima_set

# Full standard Hamming-isometry group: coordinate permutations followed by
# independent coordinate complements, represented as XOR by t.
group = []
for p in permutations(range(N)):
    base = tuple(permute_bits(x, p) for x in VERTICES)
    for t in VERTICES:
        group.append(tuple(base[x] ^ t for x in VERTICES))
assert len(group) == 384 and len(set(group)) == 384

# Orbit partition of all 240 maxima.
seen = set()
orbits = []
for C in maxima:
    if C in seen:
        continue
    orb = {tuple(sorted(g[x] for x in C)) for g in group}
    assert orb <= maxima_set
    orbits.append(orb)
    seen |= orb
assert seen == maxima_set
orbit_sizes = sorted(len(o) for o in orbits)
assert orbit_sizes == [48, 192]


def orbit_of(C):
    return {tuple(sorted(g[x] for x in C)) for g in group}

OA = orbit_of(A)
OB = orbit_of(B)
assert len(OA) == 192
assert len(OB) == 48
assert OA.isdisjoint(OB)
assert OA | OB == maxima_set

stab_A = sum(tuple(sorted(g[x] for x in A)) == A for g in group)
stab_B = sum(tuple(sorted(g[x] for x in B)) == B for g in group)
assert (stab_A, stab_B) == (2, 8)
assert 384 // stab_A == len(OA)
assert 384 // stab_B == len(OB)


def dist_profile(C):
    c = Counter(hamming(a, b) for a, b in combinations(C, 2))
    return tuple(c[d] for d in range(1, N + 1))

profile_A = dist_profile(A)
profile_B = dist_profile(B)
assert profile_A == (4, 10, 6, 1)
assert profile_B == (4, 8, 8, 1)
assert profile_A != profile_B
for C in OA:
    assert dist_profile(C) == profile_A
for C in OB:
    assert dist_profile(C) == profile_B

# Stable census digest over literal maxima, one hexadecimal vertex list per line.
blob = "\n".join(",".join(f"{x:x}" for x in C) for C in maxima).encode("ascii") + b"\n"
digest = hashlib.sha256(blob).hexdigest()

print(
    "VERIFY_OK "
    f"vertices=16 size8_checked={eight_checked} maximum=7 labeled_maxima={len(maxima)} "
    f"origin_maxima=105 natural_group=384 orbits=2 orbit_sizes=48,192 "
    f"stabilizers_A_B={stab_A},{stab_B} profile_A=4,10,6,1 profile_B=4,8,8,1 "
    f"maxima_sha256={digest}"
)
