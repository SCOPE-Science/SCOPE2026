#!/usr/bin/env python3
import itertools
from collections import Counter

N=4
WORDS=tuple(range(1<<N))

def desc_key(parent):
    """Coordinate symbol-set encoding: 1={0}, 2={1}, 3={0,1}."""
    return tuple(sum(1 << ((x >> i) & 1) for x in parent) for i in range(N))

def desc_explicit(parent):
    """Independent explicit enumeration of the descendant box."""
    choices=[]
    for i in range(N):
        choices.append(sorted({(x >> i) & 1 for x in parent}))
    out=set()
    for tup in itertools.product(*choices):
        x=sum(b<<i for i,b in enumerate(tup))
        out.add(x)
    return frozenset(out)

def separable_key(C):
    seen=set()
    for r in (1,2):
        for P in itertools.combinations(C,r):
            d=desc_key(P)
            if d in seen:
                return False
            seen.add(d)
    return True

def separable_explicit(C):
    seen=set()
    for r in (1,2):
        for P in itertools.combinations(C,r):
            d=desc_explicit(P)
            if d in seen:
                return False
            seen.add(d)
    return True

# Exhaust every 7- and 8-subset; compare two independent descendant encodings.
max7=[]
for C in itertools.combinations(WORDS,7):
    a=separable_key(C); b=separable_explicit(C)
    assert a==b
    if a: max7.append(C)
valid8=[]
for C in itertools.combinations(WORDS,8):
    a=separable_key(C); b=separable_explicit(C)
    assert a==b
    if a: valid8.append(C)
assert len(max7)==240
assert not valid8
# Heredity: an admissible code with >=8 words would have an admissible 8-subcode.
# Thus maximum size is 7.

# Natural full binary Hamming-isometry group: translations and coordinate permutations.
perms=list(itertools.permutations(range(N)))
def perm_word(x,p):
    y=0
    for i,j in enumerate(p):
        if (x>>i)&1: y |= 1<<j
    return y
transforms=[]
for p in perms:
    pm=[perm_word(x,p) for x in WORDS]
    for a in WORDS:
        transforms.append(tuple(pm[x]^a for x in WORDS))
assert len(transforms)==384
maxset=set(max7)
def image_code(C,T): return tuple(sorted(T[x] for x in C))
seen=set(); orbits=[]
for C in sorted(max7):
    if C in seen: continue
    O={image_code(C,T) for T in transforms}
    assert O <= maxset
    seen |= O
    orbits.append(O)
assert seen==maxset
orbit_sizes=sorted(len(O) for O in orbits)
assert orbit_sizes==[48,192]
stabilizers=sorted(384//len(O) for O in orbits)
assert stabilizers==[2,8]

def dist_profile(C):
    c=Counter((x^y).bit_count() for x,y in itertools.combinations(C,2))
    return tuple((d,c[d]) for d in sorted(c))
profiles=Counter(dist_profile(C) for C in max7)
assert profiles==Counter({((1,4),(2,8),(3,8),(4,1)):48, ((1,4),(2,10),(3,6),(4,1)):192})
# The distance profiles distinguish the two group orbits.

def fmt(C): return ','.join(format(x,'04b') for x in C)
reps=[]
for O in sorted(orbits,key=lambda z:(len(z),min(z))):
    C=min(O); reps.append((len(O),384//len(O),C,dist_profile(C)))

print('AMBIENT=16 CHECK7=11440 CHECK8=12870')
print('MAXIMUM=7 LABELED_MAXIMA=240')
for i,(sz,stab,C,prof) in enumerate(reps,1):
    print(f'ORBIT{i} size={sz} stabilizer={stab} rep={fmt(C)} distance_profile={prof}')
print('VERIFY_OK maximum=7 labeled_maxima=240 orbits=2 orbit_sizes=48,192 stabilizers=8,2')
