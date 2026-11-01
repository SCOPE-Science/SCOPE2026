#!/usr/bin/env python3
"""Exact, self-contained certificate for the Mobius--Kantor two-independence complex.

No numerical approximations and no third-party dependencies are used.
Run: python3 verify_mk.py
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
from math import gcd

N=16
EDGES=sorted(set(tuple(sorted(edge)) for edge in (
    [(i,(i+1)%8) for i in range(8)]+
    [(8+i,8+(i+3)%8) for i in range(8)]+
    [(i,8+i) for i in range(8)]
)))
assert len(EDGES)==24
ADJ=[0]*N
for a,b in EDGES:
    assert a!=b
    ADJ[a]|=1<<b
    ADJ[b]|=1<<a
assert all(a.bit_count()==3 for a in ADJ)

def valid_by_degrees(s):
    z=s
    while z:
        bit=z&-z;z-=bit
        if (ADJ[bit.bit_length()-1]&s).bit_count()>1:
            return False
    return True

def valid_by_components(s):
    # Independent definition: connected-component cardinalities are at most 2.
    left=s
    while left:
        start=left&-left
        reached=start
        frontier=start
        while frontier:
            ne=0
            t=frontier
            while t:
                bit=t&-t;t-=bit
                ne|=ADJ[bit.bit_length()-1]
            frontier=(ne&s)&~reached
            reached|=frontier
        if reached.bit_count()>2:
            return False
        left &= ~reached
    return True

FACES={s for s in range(1<<N) if valid_by_degrees(s)}
assert all(valid_by_degrees(s)==valid_by_components(s) for s in range(1<<N))
NONEMPTY=FACES-{0}
FV=tuple(sum(s.bit_count()==k+1 for s in NONEMPTY) for k in range(8))
assert FV==(16,120,512,1324,2064,1840,816,120)
print('vertices',N,'edges',len(EDGES),'nonempty_faces',len(NONEMPTY))
print('face_vector',FV)

# Greedy vertex-toggle matching on the augmented face poset.
# Breaking the empty/vertex matching makes a genuine vertex-critical
# ordinary discrete-Morse matching without changing positive-dimensional
# Morse differentials.
UNPAIRED=set(FACES)
PAIRS=[]
for vertex in range(N):
    bit=1<<vertex
    for a in sorted(UNPAIRED):
        if a&bit:
            continue
        b=a|bit
        if b in UNPAIRED:
            UNPAIRED.remove(a)
            UNPAIRED.remove(b)
            PAIRS.append((a,b))
assert any(a==0 for a,b in PAIRS)
ORIGIN=next(b for a,b in PAIRS if a==0)
PAIRS=[(a,b) for a,b in PAIRS if a!=0]
UNPAIRED.add(ORIGIN)
UNPAIRED.add(0)
CRITICAL=UNPAIRED-{0}
C_BY_DIM={k:tuple(sorted(s for s in CRITICAL if s.bit_count()==k+1)) for k in range(8)}
assert {k:len(v) for k,v in C_BY_DIM.items() if v}=={0:1,4:1,5:4,6:6}
assert len(PAIRS)==3400
print('matching_pairs',len(PAIRS),'critical_cell_counts',tuple(map(len,C_BY_DIM.values())))
print('critical_masks_dimensions_4_5_6',C_BY_DIM[4],C_BY_DIM[5],C_BY_DIM[6])

# Global acyclicity, computed directly rather than assumed from matching style.
L2U=dict(PAIRS)
U2L={b:a for a,b in PAIRS}
assert len(L2U)==len(U2L)==len(PAIRS)
assert not (set(L2U)&set(U2L))
indeg={s:0 for s in NONEMPTY}
out=defaultdict(list)
incidence_count=0
for upper in NONEMPTY:
    t=upper
    while t:
        bit=t&-t;t-=bit
        lower=upper^bit
        if lower==0:
            continue
        if L2U.get(lower)==upper:
            source,target=lower,upper
        else:
            source,target=upper,lower
        out[source].append(target)
        indeg[target]+=1
        incidence_count+=1
queue=deque(s for s,d in indeg.items() if d==0)
visited=0
while queue:
    x=queue.popleft()
    visited+=1
    for y in out[x]:
        indeg[y]-=1
        if indeg[y]==0:
            queue.append(y)
assert visited==len(NONEMPTY)
print('acyclic_Hasse_vertices',visited,'oriented_incidences',incidence_count)

# Integral Morse differentials via exhaustive signed gradient paths.
def bdy(s):
    x=s;i=0
    while x:
        bit=x&-x;x-=bit
        yield s^bit, (-1 if (i&1) else 1)
        i+=1

@lru_cache(maxsize=None)
def reduction(t):
    if t in CRITICAL:
        return {t:1}
    if t in U2L:
        return {}
    upper=L2U.get(t)
    assert upper is not None, ('unexpected unmatched simplex',t)
    # The sign of the removed vertex in the upper oriented simplex.
    d=dict(bdy(upper))
    pivot=d[t]
    result={}
    for other,coeff in d.items():
        if other==t or other==0:
            continue
        for crit,z in reduction(other).items():
            result[crit]=result.get(crit,0)-coeff*pivot*z
    return {crit:z for crit,z in result.items() if z}

def morse_matrix(k):
    rows=C_BY_DIM[k-1]
    cols=C_BY_DIM[k]
    rowloc={s:i for i,s in enumerate(rows)}
    arr=[[0]*len(cols) for _ in rows]
    for j,c in enumerate(cols):
        for face,z in bdy(c):
            if face==0: continue
            for r,a in reduction(face).items():
                arr[rowloc[r]][j]+=z*a
    return arr

D5=morse_matrix(5)
D6=morse_matrix(6)
assert D5==[[-1,0,-1,-1]]
assert D6==[
    [-1,0,0,0,1,-1],
    [-1,0,-1,-1,1,0],
    [0,1,0,0,0,1],
    [1,-1,0,0,-1,0]
]
assert all(sum(D5[0][k]*D6[k][j] for k in range(4))==0 for j in range(6))

def det(A):
    size=len(A)
    if size==0:return 1
    return sum(((-1)**sum(p[i]>p[j] for i in range(size) for j in range(i+1,size))) *
               __import__('math').prod(A[i][p[i]] for i in range(size))
               for p in permutations(range(size)))

def divisors(M):
    r=len(M);c=len(M[0])
    output=[]
    for k in range(1,min(r,c)+1):
        d=0
        for ii in combinations(range(r),k):
            for jj in combinations(range(c),k):
                d=gcd(d,abs(det([[M[i][j] for j in jj] for i in ii])))
        output.append(d)
    return output

assert divisors(D5)==[1]
assert divisors(D6)==[1,1,1,0]
print('Morse_d5',D5,'determinantal_divisors',divisors(D5))
print('Morse_d6',D6,'determinantal_divisors',divisors(D6))
print('reduced_integral_homology',{'dimension_6':'Z^3','other_degrees':0})

# Unrelated mod-two cross-check from the ORIGINAL simplicial boundaries.
# Each column is a Python integer bit-vector of its boundary.
def gf2_rank(columns):
    piv={}
    for col in columns:
        while col:
            k=col.bit_length()-1
            if k not in piv:
                piv[k]=col
                break
            col^=piv[k]
    return len(piv)

BY_DIM={k:tuple(sorted(s for s in NONEMPTY if s.bit_count()==k+1)) for k in range(8)}
RANKS=[]
for k in range(1,8):
    loc={s:i for i,s in enumerate(BY_DIM[k-1])}
    cols=[]
    for sigma in BY_DIM[k]:
        vec=0
        for face,_ in bdy(sigma):vec^=1<<loc[face]
        cols.append(vec)
    RANKS.append(gf2_rank(cols))
assert RANKS==[15,105,407,917,1147,693,120]
print('simplicial_GF2_boundary_ranks',RANKS)

# Exact, exhaustive graph automorphisms via all partial adjacency-preserving maps.
# Includes all solutions, so no external group order is assumed.
AUT=[]
def extend(f,used):
    if len(f)==N:
        AUT.append(tuple(f[i] for i in range(N)))
        return
    keys=tuple(f)
    known=sum(1<<v for v in keys)
    unmapped=(x for x in range(N) if x not in f)
    v=max(unmapped,key=lambda x:((ADJ[x]&known).bit_count(),-x))
    for w in range(N):
        if used>>w&1:
            continue
        if all(bool(ADJ[v]>>x&1)==bool(ADJ[w]>>f[x]&1) for x in keys):
            f[v]=w
            extend(f,used|(1<<w))
            del f[v]
extend({},0)
AUT=sorted(set(AUT))
assert len(AUT)==96
assert all(len(set(p))==N and all(bool(ADJ[i]>>j&1)==bool(ADJ[p[i]]>>p[j]&1)
              for i in range(N) for j in range(N)) for p in AUT)
print('graph_automorphisms',len(AUT))

def cycles(p):
    used=set();cyc=[]
    for i in range(N):
        if i not in used:
            path=[];x=i
            while x not in used:
                used.add(x)
                path.append(x)
                x=p[x]
            cyc.append(tuple(path))
    return cyc

def trace_via_orbits(p):
    orbits=cycles(p)
    total=-1  # empty face has reduced Lefschetz contribution +1
    for select in range(1,1<<len(orbits)):
        face=0;orbit_count=0
        for j,orbit in enumerate(orbits):
            if select>>j&1:
                orbit_count+=1
                for vertex in orbit:face|=1<<vertex
        if face in FACES:
            # (-1)^(face dimension) times simplex orientation sign.
            total+=(-1 if (orbit_count&1)==0 else 1)
    return total

def trace_via_faces(p):
    value=-1
    for face in NONEMPTY:
        vertices=[i for i in range(N) if face>>i&1]
        images=[p[v] for v in vertices]
        if set(images)!=set(vertices):
            continue
        inv=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
        value+=(-1 if ((len(vertices)-1+inv)&1) else 1)
    return value

TRACES={p:trace_via_orbits(p) for p in AUT}
assert all(TRACES[p]==trace_via_faces(p) for p in AUT)
DIST=Counter((tuple(sorted(len(c) for c in cycles(p))),TRACES[p]) for p in AUT)
EXPECTED={
((1,)*16,3):1,
((1,)*4+(2,)*6,-1):12,
((1,)*4+(3,)*4,0):8,
((2,)*8,1):18,
((2,)*8,3):1,
((2,)*2+(6,)*2,0):8,
((4,)*4,-3):2,
((4,)*4,-1):6,
( (4,12),0):16,
((8,8),-1):12,
((8,8),1):12,
}
assert DIST==EXPECTED
assert sum(count for count in DIST.values())==96
assert sum(a*a for a in TRACES.values())==96
identity=tuple(range(N))
half_turn=tuple((i+4)%8 if i<8 else 8+(i-8+4)%8 for i in range(N))
assert [p for p in AUT if TRACES[p]==3]==[identity,half_turn] or set(p for p in AUT if TRACES[p]==3)=={identity,half_turn}
assert all(tuple(half_turn[p[i]] for i in range(N))==tuple(p[half_turn[i]] for i in range(N)) for p in AUT)
print('character_distribution_cycle_type_trace_multiplicity')
for (type_,char),count in sorted(DIST.items()):print(type_,char,count)
print('character_squared_norm_numerator',sum(a*a for a in TRACES.values()))
print('representation_irreducible_absolute',True,'kernel_order',2,'kernel_nontrivial',half_turn)
print('ALL_CHECKS_PASS')
