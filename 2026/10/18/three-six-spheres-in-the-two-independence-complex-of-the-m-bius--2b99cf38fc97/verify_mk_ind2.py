#!/usr/bin/env python3
"""Stand-alone exact certificate for Ind_2(GP(8,3)). Pure Python 3.

The argument checks a complete finite acyclic discrete-Morse matching, its
integral boundary matrices, and a rank-three unimodular minor. The final
homotopy step uses elementary CW theory, not extrapolation from samples.
"""
from collections import Counter,deque
from functools import lru_cache
from itertools import combinations
from math import gcd

N=16

def gp83_edges():
    E=set()
    for i in range(8):
        for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
            E.add(tuple(sorted((a,b))))
    return tuple(sorted(E))
E=gp83_edges()
assert len(E)==24
neighbor=[0]*N
for a,b in E:
    neighbor[a]|=1<<b
    neighbor[b]|=1<<a
assert all(x.bit_count()==3 for x in neighbor)

# A vertex set induces components of order <=2 if and only if it
# contains no (not necessarily induced) path of length two.
forbidden=set()
for center in range(N):
    adj=[v for v in range(N) if neighbor[center] & 1<<v]
    for a,b in combinations(adj,2):
        forbidden.add((1<<a)|(1<<center)|(1<<b))
assert len(forbidden)==48
F={m for m in range(1,1<<N) if all((m&t)!=t for t in forbidden)}
by_dim={d:sorted(m for m in F if m.bit_count()==d+1) for d in range(8)}
fvector=[len(by_dim[d]) for d in range(8)]
assert fvector==[16,120,512,1324,2064,1840,816,120],fvector
assert len(F)==6812

def facets(b):
    for i,v in enumerate(k for k in range(N) if b>>k&1):
        yield b^(1<<v),(-1 if i%2 else 1)

# Fully prescribed element-order matching; one pass per vertex.
free=set(F)
pairs=[]
stages=[]
for v in range(N):
    for a in sorted(free):
        if a>>v&1:continue
        b=a|(1<<v)
        if b in free:
            pairs.append((a,b));free.remove(a);free.remove(b)
    stages.append(len(free))
assert len(pairs)==3400,len(pairs)
assert sorted(free)==[1,818,8916,10898,15048,17304,17714,18344,21924,23714,43684,58008]
critical={d: sorted(m for m in free if m.bit_count()-1==d) for d in range(8)}
assert {d:len(v) for d,v in critical.items() if v}=={0:1,4:1,5:4,6:6}
up=dict(pairs);down={b:a for a,b in pairs}
assert len(up)==len(down)==len(pairs)
assert not (set(up)&set(down))

# Check every facet Hasse arrow, reversing exactly matched arrows.
adj={m:[] for m in F}
indeg={m:0 for m in F}
covers=0
for b in F:
    for a,_ in facets(b):
        if not a:continue
        assert a in F
        covers+=1
        src,dst=(a,b) if up.get(a)==b else (b,a)
        adj[src].append(dst);indeg[dst]+=1
queue=deque(sorted(m for m in F if indeg[m]==0))
visited=0
while queue:
    a=queue.popleft();visited+=1
    for b in adj[a]:
        indeg[b]-=1
        if indeg[b]==0:queue.append(b)
assert visited==len(F), ('cycle',visited)

# Integral algebraic Morse projection onto critical cells.
# For a lower matched cell a and its matched upper cell b, solve
# 0=project(boundary b) for project(a). This is integer arithmetic
# since each incidence coefficient is +1 or -1.
@lru_cache(None)
def project(a):
    if a in free:return {a:1}
    if a in down:return {}
    b=up[a]
    factor=next(s for x,s in facets(b) if x==a)
    result={}
    for x,s in facets(b):
        if x==a:continue
        for c,z in project(x).items():
            result[c]=result.get(c,0)-factor*s*z
    return {c:z for c,z in result.items() if z}

def morse_boundary(b):
    result={}
    for a,s in facets(b):
        for c,z in project(a).items():
            result[c]=result.get(c,0)+s*z
    return {c:z for c,z in result.items() if z}

c4=critical[4];c5=critical[5];c6=critical[6]
d5=[[morse_boundary(x).get(y,0) for x in c5] for y in c4]
d6=[[morse_boundary(x).get(y,0) for x in c6] for y in c5]
assert d5==[[-1,0,-1,-1]],d5
assert d6==[[-1,0,0,0,1,-1],
            [-1,0,-1,-1,1,0],
            [0,1,0,0,0,1],
            [1,-1,0,0,-1,0]],d6
assert all(sum(d5[0][i]*d6[i][j] for i in range(4))==0 for j in range(6))

# Choose the 5-cell in c5[0], whose boundary has degree -1, and
# collapse its degree-one 4/5 CW subcomplex. The remaining three
# 5-cell rows and all six 6-cell columns give the quotient attaching map.
B=d6[1:]
minor=[[B[i][j] for j in (0,1,2)] for i in range(3)]
det=(minor[0][0]*(minor[1][1]*minor[2][2]-minor[1][2]*minor[2][1])
    -minor[0][1]*(minor[1][0]*minor[2][2]-minor[1][2]*minor[2][0])
    +minor[0][2]*(minor[1][0]*minor[2][1]-minor[1][1]*minor[2][0]))
assert abs(det)==1,det

# Independent boundary-column reduction over GF(2), with no Morse matching.
# The 0th column rank is computed using the ordinary C0 boundary zero.
def rank_mod2(d):
    if d==0:return 0
    index={m:i for i,m in enumerate(by_dim[d-1])}
    pivots={}
    for b in by_dim[d]:
        col=0
        for a,s in facets(b):col ^=1<<index[a]
        while col:
            k=col.bit_length()-1
            if k not in pivots:
                pivots[k]=col;break
            col ^= pivots[k]
    return len(pivots)
ranks=[rank_mod2(d) for d in range(8)]
betti=[fvector[d]-ranks[d]-(ranks[d+1] if d<7 else 0) for d in range(8)]
betti[0]-=1
assert betti==[0,0,0,0,0,0,3,0],(ranks,betti)
assert sum((-1)**d*fvector[d] for d in range(8))==4

print('GRAPH GP(8,3): vertices=16 edges=24 degree=3 forbidden_2_paths=',len(forbidden))
print('FACE_VECTOR',fvector,'NONEMPTY',len(F))
print('MATCHED_PAIRS',len(pairs),'CRITICAL_BY_DIM',{d:len(v) for d,v in critical.items() if v})
print('MATCHING_STAGE_REMAINDERS',stages)
print('HASSE_COVERS',covers,'ACYCLIC_TOPO_VISITS',visited)
print('CRITICAL_MASKS',{d:v for d,v in critical.items() if v})
print('INTEGRAL_MORSE_D5',d5)
print('INTEGRAL_MORSE_D6',d6)
print('QUOTIENT_BOUNDARY_3x6',B)
print('UNIT_3x3_MINOR',det)
print('DIRECT_GF2_BOUNDARY_RANKS',ranks,'REDUCED_BETTI',betti)
print('CONCLUSION: Ind_2(GP(8,3)) has homotopy type wedge of three six-spheres')
