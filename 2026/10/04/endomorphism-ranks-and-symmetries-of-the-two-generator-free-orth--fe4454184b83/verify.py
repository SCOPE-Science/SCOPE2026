#!/usr/bin/env python3
from collections import Counter, deque
from itertools import permutations

# Context encoding for MO2:
# 0 = bottom, 1 = top, 2,3 and 4,5 are complement pairs.
C = range(6)
comp_c = [1, 0, 3, 2, 5, 4]

def meet_c(x, y):
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    if x == y:
        return x
    return 0

def join_c(x, y):
    if x == 1 or y == 1:
        return 1
    if x == 0:
        return y
    if y == 0:
        return x
    if x == y:
        return x
    return 1

# Elements are encoded as 16*c + b, where b is a four-bit Boolean vector.
N = 96
def elem(c, b):
    return 16*c + b

def ctx(x):
    return x // 16

def bits(x):
    return x % 16

comp = [0] * N
meet = [[0] * N for _ in range(N)]
join = [[0] * N for _ in range(N)]

for x in range(N):
    cx, bx = ctx(x), bits(x)
    comp[x] = elem(comp_c[cx], 15 ^ bx)
    for y in range(N):
        cy, by = ctx(y), bits(y)
        meet[x][y] = elem(meet_c(cx, cy), bx & by)
        join[x][y] = elem(join_c(cx, cy), bx | by)

ZERO = elem(0, 0)
ONE = elem(1, 15)

def generated(pair):
    S = {ZERO, ONE, pair[0], pair[1]}
    changed = True
    while changed:
        changed = False
        current = list(S)
        for x in current:
            z = comp[x]
            if z not in S:
                S.add(z)
                changed = True
        current = list(S)
        for i, x in enumerate(current):
            for y in current[i:]:
                for z in (meet[x][y], join[x][y]):
                    if z not in S:
                        S.add(z)
                        changed = True
    return frozenset(S)

# Published coordinate representatives for two free generators.
xgen = elem(2, 0b1100)
ygen = elem(4, 0b1010)
assert len(generated((xgen, ygen))) == 96

# Exhaustive endomorphism image-rank profile.
ranks = Counter()
generating_pairs = []
for u in range(N):
    for v in range(N):
        r = len(generated((u, v)))
        ranks[r] += 1
        if r == 96:
            generating_pairs.append((u, v))

expected = {
    2: 4,
    4: 564,
    8: 3720,
    12: 32,
    16: 2880,
    24: 672,
    48: 1152,
    96: 192,
}
assert dict(sorted(ranks.items())) == expected, ranks
assert sum(ranks.values()) == 96 * 96
assert len(generating_pairs) == 192
assert all(u != v for u, v in generating_pairs)
assert len({tuple(sorted((u, v))) for u, v in generating_pairs}) == 96

# All MO2 automorphisms: permutations of middle elements commuting with complement.
middle = (2, 3, 4, 5)
ctx_autos = []
for p in permutations(middle):
    f = {0: 0, 1: 1}
    f.update(dict(zip(middle, p)))
    if all(f[comp_c[c]] == comp_c[f[c]] for c in C):
        # Verify lattice operations.
        if all(
            f[meet_c(a, b)] == meet_c(f[a], f[b])
            and f[join_c(a, b)] == join_c(f[a], f[b])
            for a in C for b in C
        ):
            ctx_autos.append(f)
assert len(ctx_autos) == 8

# Coordinate permutations of the Boolean factor.
bit_perms = list(permutations(range(4)))
assert len(bit_perms) == 24

def perm_bits(b, p):
    out = 0
    for i in range(4):
        if (b >> i) & 1:
            out |= 1 << p[i]
    return out

autos = []
for fc in ctx_autos:
    for p in bit_perms:
        mapping = tuple(elem(fc[ctx(z)], perm_bits(bits(z), p)) for z in range(N))
        assert len(set(mapping)) == N
        assert mapping[ZERO] == ZERO and mapping[ONE] == ONE
        for z in range(N):
            assert mapping[comp[z]] == comp[mapping[z]]
        # Full meet/join check.
        for a in range(N):
            ma = mapping[a]
            for b in range(N):
                mb = mapping[b]
                assert mapping[meet[a][b]] == meet[ma][mb]
                assert mapping[join[a][b]] == join[ma][mb]
        autos.append(mapping)

assert len(autos) == 192
assert len(set(autos)) == 192

# Orbit census under the 192 automorphisms.
unseen = set(range(N))
orbits = []
while unseen:
    z = next(iter(unseen))
    orb = {g[z] for g in autos}
    # The constructed group is closed; a one-step image set is the full orbit.
    unseen -= orb
    orbits.append(orb)

assert len(orbits) == 15
sizes = sorted(len(o) for o in orbits)
assert sizes == sorted([1,4,6,4,1, 1,4,6,4,1, 4,16,24,16,4])

# Check the claimed invariant description: context type and Hamming weight.
def ctype(c):
    return 0 if c == 0 else 1 if c == 1 else 2

def weight(b):
    return b.bit_count()

profile = Counter((ctype(ctx(z)), weight(bits(z))) for z in range(N))
for o in orbits:
    keys = {(ctype(ctx(z)), weight(bits(z))) for z in o}
    assert len(keys) == 1
for key, count in profile.items():
    assert any(
        {(ctype(ctx(z)), weight(bits(z))) for z in o} == {key} and len(o) == count
        for o in orbits
    )

print("ENDOMORPHISM_RANKS", dict(sorted(ranks.items())))
print("AUTOMORPHISMS", len(autos))
print("ELEMENT_ORBITS", len(orbits))
print("ORDERED_GENERATING_PAIRS", len(generating_pairs))
print("UNORDERED_GENERATING_PAIRS", len({tuple(sorted(p)) for p in generating_pairs}))
print("VERIFY_OK")
