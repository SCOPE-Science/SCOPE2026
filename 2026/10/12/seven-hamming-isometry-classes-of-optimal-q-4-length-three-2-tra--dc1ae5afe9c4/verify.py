#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter, deque
import hashlib

Q = range(4)
WORDS = list(product(Q, repeat=3))
INDEX = {w:i for i,w in enumerate(WORDS)}
N = len(WORDS)


def hd(a,b):
    return sum(x != y for x,y in zip(a,b))


def descendants_pair(a,b):
    pools = [(a[j],) if a[j] == b[j] else (a[j],b[j]) for j in range(3)]
    return product(*pools)


def direct_2ta(code):
    """Check the definition directly for parent sets of size 1 or 2."""
    C = [WORDS[i] for i in code]
    # Singleton-parent descendants are just the parent word and cause no issue
    # for a set-valued code. Check all two-parent descendants.
    for ia, ib in combinations(range(len(C)), 2):
        parents = {ia, ib}
        a, b = C[ia], C[ib]
        for w in descendants_pair(a,b):
            dist = [hd(w,x) for x in C]
            m = min(dist)
            nearest = {j for j,z in enumerate(dist) if z == m}
            if not nearest.issubset(parents):
                return False
    return True


def triple_good(a,b,c):
    return direct_2ta((a,b,c))

# A 2-TA violation is witnessed by two parents and one outside codeword, so a
# code is 2-TA iff each of its three-subsets is 2-TA.
GOOD3 = set()
for tri in combinations(range(N), 3):
    if triple_good(*tri):
        GOOD3.add(tri)

# Enumerate all maximum candidates of size four.
MAXCODES = []
for C in combinations(range(N), 4):
    if all(tuple(sorted(t)) in GOOD3 for t in combinations(C, 3)):
        MAXCODES.append(C)
MAXSET = set(MAXCODES)

# Independently replay the literal definition on every enumerated code.
assert all(direct_2ta(C) for C in MAXCODES)

# Verify there is no five-code by a complete recursive search in the 3-uniform
# compatibility hypergraph. Any 2-TA five-code would have every triple in GOOD3.
def can_extend(prefix, start, target):
    if len(prefix) == target:
        return tuple(prefix)
    need = target - len(prefix)
    for v in range(start, N - need + 1):
        if all(tuple(sorted((a,b,v))) in GOOD3 for a,b in combinations(prefix,2)):
            prefix.append(v)
            ans = can_extend(prefix, v+1, target)
            if ans is not None:
                return ans
            prefix.pop()
    return None

assert can_extend([], 0, 5) is None

# Natural equivalence: independent S_4 symbol permutations in each coordinate,
# together with S_3 coordinate permutations. Adjacent transpositions generate it.
GENS = []
for coord in range(3):
    for s in range(3):
        p = list(Q)
        p[s], p[s+1] = p[s+1], p[s]
        mapping = []
        for w in WORDS:
            z = list(w)
            z[coord] = p[z[coord]]
            mapping.append(INDEX[tuple(z)])
        GENS.append(tuple(mapping))
for s in range(2):
    mapping = []
    for w in WORDS:
        z = list(w)
        z[s], z[s+1] = z[s+1], z[s]
        mapping.append(INDEX[tuple(z)])
    GENS.append(tuple(mapping))


def image(code,g):
    return tuple(sorted(g[v] for v in code))

unseen = set(MAXCODES)
orbits = []
while unseen:
    seed = min(unseen)
    unseen.remove(seed)
    orb = {seed}
    q = deque([seed])
    while q:
        C = q.popleft()
        for g in GENS:
            D = image(C,g)
            assert D in MAXSET
            if D not in orb:
                orb.add(D)
                unseen.discard(D)
                q.append(D)
    orbits.append(orb)


def coord_profile(C):
    ps=[]
    for j in range(3):
        cnt=Counter(WORDS[v][j] for v in C)
        ps.append(tuple(sorted(cnt.values(), reverse=True)))
    return tuple(sorted(ps))


def distance_profile(C):
    cnt=Counter(hd(WORDS[a],WORDS[b]) for a,b in combinations(C,2))
    return tuple(sorted(cnt.items()))

orbits.sort(key=lambda O:(len(O), min(O)))
EXPECTED = [48,288,576,2592,3456,10368,10368]
assert [len(O) for O in orbits] == EXPECTED
assert sum(map(len,orbits)) == len(MAXCODES) == 27696
assert len(orbits) == 7
assert 24**3 * 6 == 82944
assert [82944//len(O) for O in orbits] == [1728,288,144,32,24,8,8]

reps=[]
for O in orbits:
    C=min(O)
    reps.append((tuple(WORDS[v] for v in C), coord_profile(C), distance_profile(C)))

expected_reps = [
    ((0,0,0),(0,0,1),(0,0,2),(0,0,3)),
    ((0,0,0),(0,1,1),(0,2,2),(0,3,3)),
    ((0,0,0),(1,1,1),(2,2,2),(3,3,3)),
    ((0,0,0),(0,1,1),(1,2,2),(1,3,3)),
    ((0,0,0),(0,1,1),(0,2,2),(1,3,3)),
    ((0,0,0),(0,1,1),(1,2,2),(2,2,3)),
    ((0,0,0),(0,1,1),(1,2,2),(2,3,3)),
]
assert [r[0] for r in reps] == expected_reps

# Canonical digest of all literal maxima, each code as four comma-separated
# 3-digit words, codes lexicographically ordered, one code per line.
lines=[]
for C in sorted(MAXCODES):
    lines.append(','.join(''.join(map(str,WORDS[v])) for v in C))
blob=('\n'.join(lines)+'\n').encode()
digest=hashlib.sha256(blob).hexdigest()
assert digest == 'b22fb6b34d0cca55a2b161541233bcf81435a8d81d55122fc7c8e0c8263c9779'

print('VERIFY_OK',
      f'vertices={N}',
      f'good_triples={len(GOOD3)}',
      'maximum=4',
      f'labeled_maxima={len(MAXCODES)}',
      f'natural_group={82944}',
      f'orbits={len(orbits)}',
      'orbit_sizes=' + ','.join(map(str,EXPECTED)),
      'stabilizers=1728,288,144,32,24,8,8',
      'maxima_sha256=' + digest)
for i,(rep,cp,dp) in enumerate(reps,1):
    rs=';'.join(''.join(map(str,w)) for w in rep)
    cps='/'.join('-'.join(map(str,p)) for p in cp)
    dps=','.join(f'{d}x{m}' for d,m in dp)
    print(f'ORBIT_{i} size={len(orbits[i-1])} rep={rs} coord_profile={cps} distance_profile={dps}')
