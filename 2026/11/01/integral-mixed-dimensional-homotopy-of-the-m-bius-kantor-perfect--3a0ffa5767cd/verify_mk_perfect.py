#!/usr/bin/env python3
"""Exact finite homotopy verification for the perfect-matching complex of GP(8,3)."""
import collections
import functools
import itertools
from fractions import Fraction

N=8
edges=set()
def add(u,v):edges.add(tuple(sorted((u,v))))
for i in range(N):
    add(i,(i+1)%N)
    add(i,N+i)
    add(N+i,N+(i+3)%N)
E=sorted(edges)
assert len(E)==24
ad=[[] for _ in range(16)]
for j,(a,b) in enumerate(E):
    ad[a].append((b,j));ad[b].append((a,j))
@functools.lru_cache(None)
def complete(unused):
    if not unused:return (0,)
    u=(unused&-unused).bit_length()-1
    v=[]
    for w,k in ad[u]:
        if unused>>w&1:
            for m in complete(unused^(1<<u)^(1<<w)):
                v.append(m|(1<<k))
    return tuple(v)
PM=sorted(set(complete((1<<16)-1)))
assert len(PM)==33 and all(m.bit_count()==8 for m in PM)

# Entirely different bipartite-permutation enumeration checks perfect matchings.
colour=lambda x: (x%8)%2 if x<8 else 1-((x-8)%2)
left=[v for v in range(16) if colour(v)==0]
right=[v for v in range(16) if colour(v)==1]
assert len(left)==len(right)==8
edgeidx={e:j for j,e in enumerate(E)}
bip=[]
for per in itertools.permutations(right):
    try: bip.append(sum(1<<edgeidx[tuple(sorted((u,v)))] for u,v in zip(left,per)))
    except KeyError: pass
assert sorted(set(bip))==PM

# Downward closure generates exactly the perfect-matching complex.
F={0}
for p in PM:
    s=p
    while s:
        F.add(s);s=(s-1)&p
assert len(F)==6052
faces=F-{0}
bydim=[[s for s in sorted(faces) if s.bit_count()==d+1] for d in range(8)]
fvec=tuple(len(b) for b in bydim)
assert fvec==(24,228,984,1842,1752,924,264,33)

# Independently generate ALL partial matchings, then check extendibility
# by residual perfect-matching feasibility, memoized solely by unused vertices.
matchings={0:0}
for j,(u,v) in enumerate(E):
    taken=(1<<u)|(1<<v)
    addnext={s|1<<j:occupied|taken for s,occupied in tuple(matchings.items()) if not(occupied&taken)}
    matchings.update(addnext)
@functools.lru_cache(None)
def canfinish(unused):
    if not unused:return True
    u=(unused&-unused).bit_length()-1
    return any(unused>>v&1 and canfinish(unused^(1<<u)^(1<<v)) for v,_ in ad[u])
other={s for s,occupied in matchings.items() if canfinish(((1<<16)-1)^occupied)}
assert other==F

# Explicit acyclic staged toggle matching on complete nonempty face poset.
unpaired=set(faces)
pairs={}
for k in range(24):
    bit=1<<k
    for s in sorted(unpaired):
        if not s&bit and s|bit in unpaired:
            upper=s|bit
            unpaired.remove(s);unpaired.remove(upper)
            pairs[s]=upper
crit=collections.Counter(s.bit_count()-1 for s in unpaired)
assert crit=={0:1,2:9,3:13} and len(pairs)==3014
assert 2*len(pairs)+len(unpaired)==len(faces)

indeg={s:0 for s in faces}
out=collections.defaultdict(list)
inc=0
for upper in faces:
    mask=upper
    while mask:
        bit=mask&-mask;mask-=bit
        lower=upper^bit
        if not lower:continue
        inc+=1
        tail,head=(lower,upper) if pairs.get(lower)==upper else (upper,lower)
        out[tail].append(head)
        indeg[head]+=1
q=collections.deque(s for s,d in indeg.items() if d==0)
visited=0
while q:
    s=q.popleft();visited+=1
    for t in out[s]:
        indeg[t]-=1
        if indeg[t]==0:q.append(t)
assert visited==len(faces)

# Signed critical 3 -> critical 2 Morse differential via full integer gradient paths.
low=sorted(s for s in unpaired if s.bit_count()==3)
high=sorted(s for s in unpaired if s.bit_count()==4)
index={s:k for k,s in enumerate(low)}
@functools.lru_cache(None)
def project(s):
    if s in index:return {index[s]:1}
    if s not in pairs:return {}
    up=pairs[s]
    bits=[j for j in range(24) if up>>j&1]
    pos=bits.index((up^s).bit_length()-1)
    sign=(-1)**pos
    v=collections.defaultdict(int)
    for k,j in enumerate(bits):
        rest=up^(1<<j)
        if rest==s:continue
        for i,c in project(rest).items():v[i]-=sign*((-1)**k)*c
    return {i:x for i,x in v.items() if x}
cols=[]
for s in high:
    coeff=collections.defaultdict(int)
    for k,j in enumerate(j for j in range(24) if s>>j&1):
        for i,c in project(s^(1<<j)).items():coeff[i]+=((-1)**k)*c
    cols.append(tuple(coeff[i] for i in range(len(low))))
M=[[cols[j][i] for j in range(len(high))] for i in range(len(low))]
assert len(M)==9 and all(len(row)==13 for row in M)

def rational_rank(A):
    B=[[Fraction(v) for v in row] for row in A]
    if not B:return 0
    nr,nc=len(B),len(B[0]);i=0
    for j in range(nc):
        pivot=next((k for k in range(i,nr) if B[k][j]),None)
        if pivot is None:continue
        B[pivot],B[i]=B[i],B[pivot]
        b=B[i][j]
        B[i]=[v/b for v in B[i]]
        for k in range(nr):
            if k!=i and B[k][j]:
                p=B[k][j]
                B[k]=[v-p*w for v,w in zip(B[k],B[i])]
        i+=1
        if i==nr:break
    return i

def det_int(A):
    from fractions import Fraction
    B=[[Fraction(v) for v in r] for r in A]
    n=len(B);sgn=1;result=Fraction(1)
    for j in range(n):
        p=next((k for k in range(j,n) if B[k][j]),None)
        if p is None:return 0
        if p!=j:B[p],B[j]=B[j],B[p];sgn*=-1
        t=B[j][j];result*=t
        for k in range(j+1,n):
            q=B[k][j]/t
            for c in range(j+1,n):B[k][c]-=q*B[j][c]
    assert (sgn*result).denominator==1
    return int(sgn*result)
assert rational_rank(M)==5
rr=(1,2,3,4,5);cc=(0,1,4,5,7)
unit=det_int([[M[i][j] for j in cc] for i in rr])
assert unit==-1
# Unit 5x5 minor + rank 5 forces Smith diagonal 1,1,1,1,1.

# Independently calculate every mod-2 simplicial boundary rank.
ranks=[]
for d in range(1,8):
    positions={s:i for i,s in enumerate(bydim[d-1])}
    pivots={}
    for u in bydim[d]:
        vec=0;mask=u
        while mask:
            bit=mask&-mask;mask-=bit
            vec^=1<<positions[u^bit]
        while vec:
            t=vec.bit_length()-1
            if t not in pivots:pivots[t]=vec;break
            vec^=pivots[t]
    ranks.append(len(pivots))
betti=[]
for d,n in enumerate(fvec):
    betti.append(n-(ranks[d-1] if d else 0)-(ranks[d] if d<7 else 0)-(1 if d==0 else 0))
assert betti==(0,0,4,8,0,0,0,0) or betti==[0,0,4,8,0,0,0,0],betti
print('GRAPH_VE',16,24)
print('PERFECT_MATCHINGS',len(PM),'INDEPENDENT_BIPARTITE_AGREEMENT',True)
print('NONEMPTY_FACES',len(faces),'F_VECTOR',fvec)
print('ALL_PARTIAL_MATCHINGS_CHECKED',len(matchings),'RESIDUAL_PERFECT_MATCHING_MEMBERSHIP_AGREEMENT',True)
print('MORSE_PAIRS',len(pairs),'CRITICAL_DIMENSIONS',sorted(crit.items()))
print('HASSE_INCIDENCES',inc,'COMPLETE_ACYCLICITY',visited==len(faces))
print('CRITICAL_2_MASKS',tuple(low))
print('CRITICAL_3_MASKS',tuple(high))
print('INTEGRAL_MORSE_BOUNDARY_9x13')
for row in M:print(' ',row)
print('RATIONAL_RANK',rational_rank(M),'UNIT_MINOR_ROWS',rr,'COLS',cc,'DETERMINANT',unit)
print('SMITH_DIAGONAL',(1,1,1,1,1,0,0,0,0))
print('INDEPENDENT_MOD2_BOUNDARY_RANKS',tuple(ranks),'REDUCED_BETTI',tuple(betti))
print('MOBIUS_KANTOR_PERFECT_MATCHING_WEDGE_4_S2_8_S3_VERIFIED')
