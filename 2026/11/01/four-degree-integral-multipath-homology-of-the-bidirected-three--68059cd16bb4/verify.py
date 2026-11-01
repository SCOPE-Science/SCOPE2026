#!/usr/bin/env python3
"""Reconstruct the multipath complex of the bidirected 3-cube and integer Morse chains."""
from itertools import product
from collections import Counter, defaultdict
from functools import lru_cache
import itertools, sys, json

ARCS=tuple(sorted((u,u^(1<<k)) for u in range(8) for k in range(3)))
assert len(ARCS)==24

def isface(mask):
    indeg=[0]*8; outdeg=[0]*8
    for j,(u,v) in enumerate(ARCS):
        if mask>>j&1:
            indeg[v]+=1;outdeg[u]+=1
            if indeg[v]>1 or outdeg[u]>1:return False
    # if a directed cycle, all vertices on that cycle have in=out=1;
    # use a successor walk from each used vertex.
    nextv={u:v for j,(u,v) in enumerate(ARCS) if mask>>j&1}
    for u in nextv:
        seen=set();x=u
        while x in nextv:
            if x in seen:return False
            seen.add(x);x=nextv[x]
    return True

def enumerate_faces():
    allfaces={0}
    def walk(start,mask,ind,outs,link):
        for i in range(start,24):
            u,v=ARCS[i]
            if ((ind>>v)&1) or ((outs>>u)&1):continue
            x=v
            while x in link and x!=u:x=link[x]
            if x==u:continue
            nm=mask|1<<i
            allfaces.add(nm)
            link[u]=v
            walk(i+1,nm,ind|1<<v,outs|1<<u,link)
            del link[u]
    walk(0,0,0,0,{})
    return allfaces

FACES=enumerate_faces()

# Independent generation from 8-vertex partial functions: a path forest is
# a partial injection with no directed cycles. The two generators should agree.
def independent_face_enumeration():
    index={arc:i for i,arc in enumerate(ARCS)}
    result=set()
    for choices in product(range(4),repeat=8):
        successor={}
        targets=set()
        mask=0
        valid=True
        for source,c in enumerate(choices):
            if c==0:continue
            target=source ^ (1<<(c-1))
            if target in targets:valid=False;break
            targets.add(target)
            successor[source]=target
            mask |= 1<<index[source,target]
        if not valid:continue
        for u in successor:
            seen=set();x=u
            while x in successor:
                if x in seen:valid=False;break
                seen.add(x);x=successor[x]
            if not valid:break
        if valid:result.add(mask)
    return result
assert FACES==independent_face_enumeration()
assert len(FACES)==6497
FACES.remove(0)
assert all(isface(f) for f in FACES)
assert all((f^(1<<i)) in FACES for f in FACES for i in range(24) if f>>i&1 and f.bit_count()>1)
SORTED=sorted(FACES,key=lambda x:(x.bit_count(),x))
FV=Counter(f.bit_count()-1 for f in FACES)
assert [FV[d] for d in range(7)]==[24,216,928,2016,2160,1008,144]

def boundary(f):
    return tuple((f^(1<<i),(-1)**j) for j,i in enumerate(i for i in range(24) if f>>i&1))

# Sequential matching in a chosen order of simplicial vertices is acyclic:
# the earliest coordinate switched on a closed alternating directed path
# cannot change back, and later coordinates cannot alter it.
ORDER=[6,16,21,14,1,5,19,10,9,13,23,12,3,8,20,22,0,2,15,11,4,17,18,7]
assert sorted(ORDER)==list(range(24))
remaining=set(FACES); lower_to_upper={};upper_to_lower={}
for i in ORDER:
    bit=1<<i
    for f in SORTED:
        if f in remaining and not f&bit and (f|bit) in remaining:
            g=f|bit
            lower_to_upper[f]=g
            upper_to_lower[g]=f
            remaining.remove(f);remaining.remove(g)
CRIT=set(remaining)
assert [Counter(f.bit_count()-1 for f in CRIT)[d] for d in (0,1,2,3,4,5,6)]==[1,0,0,7,47,37,12]
assert len(CRIT)+2*len(lower_to_upper)==len(FACES)

# Independent exhaustive acyclicity check: all codimension-one incidences are
# directed upper -> lower unless matched, when reversed.
incs=0;adj=defaultdict(list);indeg=defaultdict(int)
for g in FACES:
    for f,_ in boundary(g):
        if not f:continue
        assert f in FACES
        if lower_to_upper.get(f)==g:
            a,b=f,g
        else:
            a,b=g,f
        adj[a].append(b);indeg[b]+=1
        incs+=1
from collections import deque
q=deque(x for x in FACES if not indeg[x]);seen=0
while q:
    x=q.popleft();seen+=1
    for y in adj[x]:
        indeg[y]-=1
        if indeg[y]==0:q.append(y)
assert seen==len(FACES)
print('COUNTS_OK',len(FACES),dict(sorted(FV.items())),incs,len(lower_to_upper),len(CRIT), flush=True)

sys.setrecursionlimit(30000)
@lru_cache(None)
def reduction(f):
    """Project a face onto critical cells after integral matched-pair elimination."""
    if f in CRIT:return {f:1}
    if f in upper_to_lower:return {}
    upper=lower_to_upper[f]
    s=dict(boundary(upper))[f]
    answer={}
    for g,eps in boundary(upper):
        if g==f:continue
        coef=-s*eps
        for c,z in reduction(g).items():
            answer[c]=answer.get(c,0)+coef*z
            if answer[c]==0:del answer[c]
    return answer

CRIT_BY_DIM={d:sorted(f for f in CRIT if f.bit_count()==d+1) for d in range(7)}
MORSE={}
for k in range(1,7):
    lower=CRIT_BY_DIM[k-1];upper=CRIT_BY_DIM[k]
    row_index={f:i for i,f in enumerate(lower)}
    A=[[0 for _ in upper] for _ in lower]
    for j,face in enumerate(upper):
        v={}
        for f,s in boundary(face):
            for critical,c in reduction(f).items():
                v[critical]=v.get(critical,0)+s*c
        for f,c in v.items():
            if c:A[row_index[f]][j]=c
    MORSE[k]=A

# Consecutive Morse differentials must compose to zero.
for k in range(2,7):
    B=MORSE[k-1]
    A=MORSE[k]
    nr=len(B)
    mid=len(CRIT_BY_DIM[k-1])
    nc=len(CRIT_BY_DIM[k])
    for i in range(nr):
        for j in range(nc):
            assert sum(B[i][h]*A[h][j] for h in range(mid))==0

# An integer matrix has Smith normal form (1,0,...) iff it has
# rank exactly one over the rationals and contains a unit entry.
# Check rank-one minors using a unimodular pivot, with no external CAS.
RANK={};INVARIANTS={}
for k,A in MORSE.items():
    rows=len(CRIT_BY_DIM[k-1])
    cols=len(CRIT_BY_DIM[k])
    witness=next(((i,j) for i in range(rows) for j in range(cols) if A[i][j]),None)
    if witness is None:
        RANK[k]=0; INVARIANTS[k]=[]
    else:
        i0,j0=witness
        pivot=A[i0][j0]
        assert abs(pivot)==1
        for i in range(rows):
            for j in range(cols):
                assert A[i][j]*pivot==A[i][j0]*A[i0][j]
        RANK[k]=1; INVARIANTS[k]=[1]
    print('MORSE_BOUNDARY',k,'shape',(rows,cols),'rank',RANK[k],
          'smith_nonzero',INVARIANTS[k],
          'nonzero_entries',[(i,j,A[i][j]) for i in range(rows) for j in range(cols) if A[i][j]][:50],flush=True)
BETTI={d:len(CRIT_BY_DIM[d])-RANK.get(d,0)-RANK.get(d+1,0) for d in range(7)}
assert BETTI=={0:1,1:0,2:0,3:6,4:45,5:36,6:12}
assert all(v==1 for a in INVARIANTS.values() for v in a)
# Independent rank check on the original, unreduced chain complex over F_2.
def direct_rank_gf2(k):
    if k<1:return 0
    lower=[f for f in FACES if f.bit_count()==k]
    index={f:i for i,f in enumerate(lower)}
    pivots={}
    for upper in (f for f in FACES if f.bit_count()==k+1):
        v=0
        for f,_ in boundary(upper):v^=1<<index[f]
        while v:
            p=v.bit_length()-1
            if p in pivots:v^=pivots[p]
            else:pivots[p]=v;break
    return len(pivots)
assert [direct_rank_gf2(k) for k in range(1,7)]==[23,193,735,1275,840,132]

print('VERIFY_OK',len(FACES),len(lower_to_upper),seen,incs,'betti',BETTI,'invariants',INVARIANTS,flush=True)
if len(sys.argv)>1 and sys.argv[1]=='--json':
    print(json.dumps({'fvector':[FV[d] for d in range(7)],'incidences':incs,'matched_pairs':len(lower_to_upper),
        'critical':[len(CRIT_BY_DIM[d]) for d in range(7)],'morse_boundary_invariants':INVARIANTS,
        'betti':BETTI,'order':ORDER},sort_keys=True))
