#!/usr/bin/env python3
from itertools import permutations, combinations
from collections import deque, Counter
import hashlib

N = 5
PERMS = list(permutations(range(N)))
INDEX = {p:i for i,p in enumerate(PERMS)}
IDENTITY = tuple(range(N))
ID = INDEX[IDENTITY]

def lcs_length(a, b):
    dp = [0]*(N+1)
    for x in a:
        new = [0]*(N+1)
        for j, y in enumerate(b, 1):
            if x == y:
                new[j] = dp[j-1] + 1
            else:
                new[j] = max(dp[j], new[j-1])
        dp = new
    return dp[N]

def ulam_lcs(a, b):
    return N - lcs_length(a, b)

def translocation_neighbors(p):
    out = set()
    a = list(p)
    for i in range(N):
        x = a[i]
        rem = a[:i] + a[i+1:]
        for j in range(N):
            q = tuple(rem[:j] + [x] + rem[j:])
            if q != p:
                out.add(q)
    return out

# Independent metric reconstruction by shortest paths in the one-translocation graph.
neighbors = [[] for _ in PERMS]
for i, p in enumerate(PERMS):
    neighbors[i] = [INDEX[q] for q in translocation_neighbors(p)]

dist = [[N+1]*len(PERMS) for _ in PERMS]
for s in range(len(PERMS)):
    dist[s][s] = 0
    q = deque([s])
    while q:
        v = q.popleft()
        for w in neighbors[v]:
            if dist[s][w] == N+1:
                dist[s][w] = dist[s][v] + 1
                q.append(w)

pair_checks = 0
for i, j in combinations(range(len(PERMS)), 2):
    d1 = ulam_lcs(PERMS[i], PERMS[j])
    d2 = dist[i][j]
    assert d1 == d2
    pair_checks += 1

# Compatibility graph: minimum Ulam distance at least 3.
V = len(PERMS)
ADJ = [0]*V
for i in range(V):
    bits = 0
    for j in range(V):
        if i != j and dist[i][j] >= 3:
            bits |= 1 << j
    ADJ[i] = bits

# Exhaustive enumeration of all 4-cliques, using increasing vertex indices.
maxima = []
for i in range(V):
    cand_i = ADJ[i] & ~((1 << (i+1)) - 1)
    x = cand_i
    while x:
        bj = x & -x
        j = bj.bit_length() - 1
        x -= bj
        cand_j = cand_i & ADJ[j] & ~((1 << (j+1)) - 1)
        y = cand_j
        while y:
            bk = y & -y
            k = bk.bit_length() - 1
            y -= bk
            cand_k = cand_j & ADJ[k] & ~((1 << (k+1)) - 1)
            z = cand_k
            while z:
                bl = z & -z
                l = bl.bit_length() - 1
                z -= bl
                maxima.append((i, j, k, l))

assert len(maxima) == 4020
MAXSET = set(maxima)

# Every 4-clique is maximal, so no 5-clique exists.
for c in maxima:
    common = (1 << V) - 1
    for v in c:
        common &= ADJ[v]
    assert common == 0

# Every maximum is equidistant with all six pair distances equal to 3.
for c in maxima:
    profile = sorted(dist[a][b] for a, b in combinations(c, 2))
    assert profile == [3, 3, 3, 3, 3, 3]

normalized = [c for c in maxima if ID in c]
assert len(normalized) == 134
assert len(maxima) * 4 == len(normalized) * 120

# Natural order-240 isometry group: arbitrary symbol relabelings and position reversal.
transforms = []
for f in PERMS:
    for reverse in (False, True):
        mapping = []
        for p in PERMS:
            q = tuple(f[x] for x in p)
            if reverse:
                q = q[::-1]
            mapping.append(INDEX[q])
        transforms.append(tuple(mapping))
assert len(set(transforms)) == 240

seen = set()
orbit_sizes = []
for c in maxima:
    if c in seen:
        continue
    orb = set()
    for m in transforms:
        image = tuple(sorted(m[v] for v in c))
        assert image in MAXSET
        orb.add(image)
    seen.update(orb)
    orbit_sizes.append(len(orb))
assert len(seen) == 4020
assert Counter(orbit_sizes) == Counter({60:5, 120:7, 240:12})

def word(p):
    return ''.join(str(x+1) for x in p)

def code_line(c):
    return '|'.join(sorted(word(PERMS[v]) for v in c))

normalized_text = ''.join(line + '\n' for line in sorted(code_line(c) for c in normalized)).encode('ascii')
all_text = ''.join(line + '\n' for line in sorted(code_line(c) for c in maxima)).encode('ascii')
normalized_sha = hashlib.sha256(normalized_text).hexdigest()
all_sha = hashlib.sha256(all_text).hexdigest()

print(
    "VERIFY_OK "
    f"vertices={V} pair_checks={pair_checks} maximum=4 "
    f"normalized_maxima={len(normalized)} labeled_maxima={len(maxima)} "
    "distance_profile=3x6 natural_group=240 orbits=24 "
    "orbit_sizes=60x5,120x7,240x12 "
    f"normalized_sha256={normalized_sha} labeled_sha256={all_sha}"
)
