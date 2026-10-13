#!/usr/bin/env python3
from itertools import product, combinations
from collections import deque, Counter
from pathlib import Path
import json

N=5
FULL_MASK=(1<<N)-1
C=(1,2,3,4,0)
ID=(0,1,2,3,4)

def rank(t):
    return len(set(t))

def image_mask(mask,t):
    out=0
    for q in range(N):
        if mask>>q & 1:
            out |= 1<<t[q]
    return out

CIMG=[image_mask(m,C) for m in range(32)]
TWOS=[sum(1<<i for i in s) for s in combinations(range(N),2)]
PAIR_STATES=[(TWOS[i],TWOS[j]) for i in range(len(TWOS)) for j in range(i+1,len(TWOS))]

def is_target(x,y):
    return (x.bit_count()==1) != (y.bit_count()==1)

# Engine A. For every admissible f, build the complete ordered-pair subset
# transition graph under c and f. Reverse BFS from all distinguishing states
# computes the exact shortest distinguishing-word length for every pair state.
hist=Counter()
maxdist=0
sharp=0
map_counts=Counter()
for f in product(range(N), repeat=N):
    r=rank(f)
    if r not in (2,3,4):
        continue
    map_counts[r]+=1
    FIMG=[image_mask(m,f) for m in range(32)]

    rev=[[] for _ in range(32*32)]
    valid=[]
    targets=[]
    for x in range(1,32):
        for y in range(1,32):
            s=x*32+y
            valid.append(s)
            if is_target(x,y):
                targets.append(s)
            for XIMG in (CIMG,FIMG):
                u,v=XIMG[x],XIMG[y]
                rev[u*32+v].append(s)

    dist=[-1]*(32*32)
    q=deque()
    for s in targets:
        dist[s]=0
        q.append(s)
    while q:
        s=q.popleft()
        nd=dist[s]+1
        for p in rev[s]:
            if dist[p]<0:
                dist[p]=nd
                q.append(p)

    for x,y in PAIR_STATES:
        d=dist[x*32+y]
        assert d>=1,(f,x,y)
        hist[d]+=1
        if d>maxdist:
            maxdist=d
            sharp=1
        elif d==maxdist:
            sharp+=1

assert map_counts==Counter({3:1500,4:1200,2:300})
assert sum(hist.values())==3000*45
assert dict(sorted(hist.items()))=={
    1:45000,2:42360,3:28420,4:13525,5:4395,
    6:1005,7:235,8:50,9:10
}
assert maxdist==9 and hist[9]==10

# Engine B. Quotient transformations by f ~ c^a f c^b. These maps generate
# the same monoid together with c. Quotient pair inputs by simultaneous
# rotation, then explicitly generate each monoid and scan it for a separator.
def compose(g,f):
    return tuple(g[f[i]] for i in range(N))

def cpower(k):
    return tuple((i+k)%N for i in range(N))

CPOW=[cpower(k) for k in range(N)]

def equiv_transform(f,a,b):
    return compose(CPOW[a], compose(f,CPOW[b]))

def canon_f(f):
    return min(equiv_transform(f,a,b) for a in range(N) for b in range(N))

reps_by_rank={2:set(),3:set(),4:set()}
for f in product(range(N),repeat=N):
    r=rank(f)
    if r in reps_by_rank:
        reps_by_rank[r].add(canon_f(f))
assert {r:len(v) for r,v in reps_by_rank.items()}=={2:12,3:60,4:48}

def rot_mask(mask,k):
    return image_mask(mask,CPOW[k])

def canon_pair(x,y):
    return min(
        tuple(sorted((rot_mask(x,k),rot_mask(y,k))))
        for k in range(N)
    )

PAIR_REPS=sorted({canon_pair(x,y) for x,y in PAIR_STATES})
assert len(PAIR_REPS)==9

def generated_monoid(f):
    seen={ID}
    q=deque([ID])
    while q:
        h=q.popleft()
        for g in (C,f):
            z=compose(g,h)
            if z not in seen:
                seen.add(z)
                q.append(z)
    return seen

monoid_sizes=Counter()
for r in (2,3,4):
    for f in sorted(reps_by_rank[r]):
        M=generated_monoid(f)
        monoid_sizes[(r,len(M))]+=1
        for x,y in PAIR_REPS:
            assert any(is_target(image_mask(x,h),image_mask(y,h)) for h in M),(r,f,x,y)

assert monoid_sizes==Counter({
    (2,60):12,
    (3,135):4,(3,160):4,(3,210):4,(3,260):8,(3,285):20,(3,360):12,(3,460):8,
    (4,610):8,(4,1010):8,(4,2110):32
})

# Degree-five classification step: strong sync-maximality is monotone upward
# in the permutation-group argument. Any transitive degree-five group has order
# divisible by 5, hence contains an element of order 5; on five points this is
# a 5-cycle. Thus every primitive degree-five group contains a conjugate of C5.
# The converse strong => primitive is the published proposition used by RESULT.
cert=json.loads((Path(__file__).resolve().parent/"certificate.json").read_text(encoding="utf-8"))
assert cert["classification"]=="A degree-5 permutation group is strongly sync-maximal if and only if it is primitive."
assert cert["maximum_shortest_distinguishing_word_length"]==9

print(
    "VERIFY_OK maps=3000 pair_instances=135000 "
    "dist_hist=45000,42360,28420,13525,4395,1005,235,50,10 "
    "max_shortest=9 sharp_instances=10 "
    "double_rotation_reps=12+60+48 pair_orbits=9 "
    "engines=full_reverse_pair_BFS+symmetry_reduced_explicit_monoids"
)
