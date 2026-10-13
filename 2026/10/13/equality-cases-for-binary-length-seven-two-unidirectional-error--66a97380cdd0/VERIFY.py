from itertools import combinations, permutations
from collections import Counter

N = 7
T = 2
MASK = (1 << N) - 1
V = list(range(1 << N))

def n10(x, y):
    return (x & (~y & MASK)).bit_count()

def du(x, y):
    a = n10(x, y)
    b = n10(y, x)
    return a + b if (a == 0 or b == 0) else 2 * max(a, b)

def ball(x):
    ones = [i for i in range(N) if (x >> i) & 1]
    zeros = [i for i in range(N) if not ((x >> i) & 1)]
    out = {x}
    for pos in (ones, zeros):
        for r in (1, 2):
            for S in combinations(pos, r):
                y = x
                for i in S:
                    y ^= 1 << i
                out.add(y)
    return frozenset(out)

balls = [ball(x) for x in V]
adj = [0] * len(V)
edges = 0
for x in V:
    for y in range(x + 1, len(V)):
        by_ball = balls[x].isdisjoint(balls[y])
        by_distance = du(x, y) >= 2 * T + 1
        assert by_ball == by_distance
        if by_ball:
            adj[x] |= 1 << y
            adj[y] |= 1 << x
            edges += 1

# Enumerate every 4-clique with increasing vertex labels.
maxima = []
for a in V:
    B = adj[a] & ~((1 << (a + 1)) - 1)
    bm = B
    while bm:
        lb = bm & -bm
        b = lb.bit_length() - 1
        bm -= lb
        C = B & adj[b] & ~((1 << (b + 1)) - 1)
        cm = C
        while cm:
            lc = cm & -cm
            c = lc.bit_length() - 1
            cm -= lc
            D = C & adj[c] & ~((1 << (c + 1)) - 1)
            dm = D
            while dm:
                ld = dm & -dm
                d = ld.bit_length() - 1
                dm -= ld
                maxima.append((a, b, c, d))

# No 4-clique has a common neighbor, so there is no 5-clique.
assert maxima
for C in maxima:
    common = MASK ^ MASK  # zero, then initialize below
    common = (1 << len(V)) - 1
    for x in C:
        common &= adj[x]
    assert common == 0
assert len(maxima) == 1680

weight_profiles = Counter(tuple(sorted(x.bit_count() for x in C)) for C in maxima)
assert weight_profiles == Counter({(2, 3, 4, 5): 1260, (1, 3, 4, 6): 420})

def pair_profile(C):
    return tuple(sorted(tuple(sorted((n10(x, y), n10(y, x)))) for x, y in combinations(C, 2)))

pair_profiles = Counter(pair_profile(C) for C in maxima)
P_A = ((1, 3), (1, 3), (1, 4), (2, 3), (2, 3), (2, 3))
P_B = ((0, 5), (1, 3), (1, 3), (1, 4), (1, 4), (2, 3))
assert pair_profiles == Counter({P_A: 1260, P_B: 420})

coverage_profiles = Counter(sum(len(balls[x]) for x in C) for C in maxima)
assert coverage_profiles == Counter({72: 1260, 80: 420})

# Coordinate permutations together with global complementation are isometries.
PERMS = list(permutations(range(N)))
def perm_word(x, p):
    y = 0
    for i in range(N):
        if (x >> i) & 1:
            y |= 1 << p[i]
    return y

def orbit(C):
    out = set()
    for p in PERMS:
        D = tuple(sorted(perm_word(x, p) for x in C))
        out.add(D)
        out.add(tuple(sorted(x ^ MASK for x in D)))
    return out

all_max = set(maxima)
rep_A = next(C for C in maxima if tuple(sorted(x.bit_count() for x in C)) == (2, 3, 4, 5))
rep_B = next(C for C in maxima if tuple(sorted(x.bit_count() for x in C)) == (1, 3, 4, 6))
orb_A = orbit(rep_A)
orb_B = orbit(rep_B)
assert len(orb_A) == 1260
assert len(orb_B) == 420
assert orb_A.isdisjoint(orb_B)
assert orb_A | orb_B == all_max
GROUP = 2 * len(PERMS)
assert GROUP == 10080
assert GROUP // len(orb_A) == 8
assert GROUP // len(orb_B) == 24

# Representative binary words (displayed in the usual 7-bit notation).
def word(x):
    return format(x, '07b')

print(
    'VERIFY_OK '
    f'vertices={len(V)} edges={edges} maximum=4 labeled_maxima={len(maxima)} '
    f'weight_profiles=1260x(2,3,4,5),420x(1,3,4,6) '
    f'coverage_profiles=1260x72,420x80 '
    f'natural_group={GROUP} orbits=1260,420 stabilizers=8,24 '
    f'repA={"/".join(word(x) for x in rep_A)} '
    f'repB={"/".join(word(x) for x in rep_B)}'
)
