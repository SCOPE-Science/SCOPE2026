#!/usr/bin/env python3
import itertools
from collections import Counter

N = 6
WORDS = list(itertools.product((0, 1), repeat=N))
INDEX = {w:i for i,w in enumerate(WORDS)}
ZERO = (0,)*N

def pair_distance(a,b):
    return sum((a[i],a[(i+1)%N]) != (b[i],b[(i+1)%N]) for i in range(N))

def xor(a,b):
    return tuple(x^y for x,y in zip(a,b))

# Direct compatibility graph for minimum pair-distance at least 5.
adj = [0]*len(WORDS)
pair_checks = 0
for i in range(len(WORDS)):
    for j in range(i+1,len(WORDS)):
        pair_checks += 1
        if pair_distance(WORDS[i],WORDS[j]) >= 5:
            adj[i] |= 1 << j
            adj[j] |= 1 << i

# Independent pair-weight identity check: d_p(x,y)=w_p(x+y) over F_2.
for i,a in enumerate(WORDS):
    for j,b in enumerate(WORDS):
        lhs = pair_distance(a,b)
        rhs = pair_distance(ZERO, xor(a,b))
        assert lhs == rhs

# Exact maximum-clique size with greedy-color upper bounds.
def maximum_clique_size():
    best = 0
    def expand(size, P):
        nonlocal best
        if not P:
            if size > best:
                best = size
            return
        verts=[]; colors=[]; Q=P; color=0
        while Q:
            color += 1
            avail = Q
            while avail:
                lb = avail & -avail
                v = lb.bit_length()-1
                verts.append(v); colors.append(color)
                Q ^= lb
                avail ^= lb
                avail &= ~adj[v]
        for k in range(len(verts)-1,-1,-1):
            if size + colors[k] <= best:
                return
            v = verts[k]
            if (P >> v) & 1:
                expand(size+1, P & adj[v])
                P &= ~(1 << v)
    expand(0, (1 << len(WORDS))-1)
    return best

maximum = maximum_clique_size()
assert maximum == 8

# Independently enumerate all size-8 cliques by increasing-index recursion.
maxima=[]
def enum_k(chosen, P, k):
    if len(chosen) == k:
        maxima.append(frozenset(chosen)); return
    if len(chosen) + P.bit_count() < k:
        return
    while P:
        lb=P & -P
        v=lb.bit_length()-1
        P ^= lb
        enum_k(chosen+[v], P & adj[v], k)

enum_k([], (1 << len(WORDS))-1, maximum)
assert len(maxima) == len(set(maxima)) == 32
MAXIMA=set(maxima)

# Exactly four maxima contain zero, and each is a 3-dimensional linear subspace.
z = INDEX[ZERO]
zero_maxima={C for C in MAXIMA if z in C}
assert len(zero_maxima) == 4
for C in zero_maxima:
    S={WORDS[i] for i in C}
    assert len(S)==8 and ZERO in S
    assert all(xor(a,b) in S for a in S for b in S)
    pws=Counter(pair_distance(ZERO,w) for w in S if w != ZERO)
    assert pws == Counter({5:6, 6:1})

# Every maximum is affine: translate by any of its codewords and obtain one
# of the four zero-containing linear maxima.
for C in MAXIMA:
    S={WORDS[i] for i in C}
    for c in S:
        T=frozenset(INDEX[xor(w,c)] for w in S)
        assert T in zero_maxima

# Dihedral coordinate action on the cyclic six positions.
def coord_transform(w,k,reflect):
    s=-1 if reflect else 1
    return tuple(w[(s*i+k)%N] for i in range(N))

def act_code(C,t,k,reflect):
    return frozenset(INDEX[xor(coord_transform(WORDS[i],k,reflect),t)] for i in C)

rep=min(zero_maxima, key=lambda C: tuple(sorted(C)))
dihedral_orbit={act_code(rep,ZERO,k,r) for k in range(N) for r in (0,1)}
assert dihedral_orbit == zero_maxima

full_orbit={act_code(rep,t,k,r) for t in WORDS for k in range(N) for r in (0,1)}
assert full_orbit == MAXIMA
stabilizer=sum(act_code(rep,t,k,r)==rep for t in WORDS for k in range(N) for r in (0,1))
assert stabilizer == 24

# Pair-distance distribution is the same in every maximum.
profiles=Counter()
for C in MAXIMA:
    L=sorted(C)
    prof=Counter(pair_distance(WORDS[L[i]],WORDS[L[j]]) for i in range(8) for j in range(i+1,8))
    profiles[tuple(sorted(prof.items()))]+=1
assert profiles == Counter({((5,24),(6,4)):32})

# A reproducible representative and generator basis.
rep_words={WORDS[i] for i in rep}
basis=[]
span={ZERO}
for w in sorted(rep_words):
    if w not in span:
        basis.append(w)
        new=set(span)
        new.update(xor(v,w) for v in span)
        span=new
assert len(basis)==3 and span==rep_words
basis_strings=','.join(''.join(map(str,b)) for b in basis)

print(
    'VERIFY_OK '
    f'vertices={len(WORDS)} pair_checks={pair_checks} maximum={maximum} '
    f'labeled_maxima={len(MAXIMA)} zero_maxima={len(zero_maxima)} '
    'all_affine=true linear_translation_classes=4 '
    'natural_group=768 orbits=1 orbit_size=32 stabilizer=24 '
    'distance_profile=5x24,6x4 '
    f'representative_basis={basis_strings}'
)
