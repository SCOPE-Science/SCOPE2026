#!/usr/bin/env python3
"""Exact finite verification of the two-independence complex of GP(8,3).
All integer operations use Python's unbounded integers. Requires Python >=3.9.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations
from math import gcd

N = 16
EDGES = set()
for i in range(8):
    for a, b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        EDGES.add(tuple(sorted((a,b))))
assert len(EDGES)==24
ADJ = [0]*N
for a,b in EDGES:
    ADJ[a]|=1<<b
    ADJ[b]|=1<<a
assert all(z.bit_count()==3 for z in ADJ)

# An induced graph has components of order <=2 iff its maximum degree <=1.
def face(s):
    return all((ADJ[v]&s).bit_count()<=1 for v in range(N) if s&(1<<v))
FACES = tuple(s for s in range(1,1<<N) if face(s))
FSET = set(FACES)
assert len(FACES)==6812
FV = tuple(sum(s.bit_count()==k for s in FACES) for k in range(1,9))
assert FV == (16,120,512,1324,2064,1840,816,120)
FACETS=tuple(s for s in FACES if not any((s|(1<<v)) in FSET for v in range(N) if not s&(1<<v)))
assert Counter(s.bit_count()-1 for s in FACETS)=={6:96,7:120}

# Greedy sequential element matching, with all nonempty faces included.
REMAIN=set(FACES)
MATCH_LOWER={}
MATCH_UPPER={}
for v in range(N):
    bit=1<<v
    for s in sorted(REMAIN):
        if (s&bit)==0 and (s|bit) in REMAIN:
            b=s|bit
            MATCH_LOWER[s]=b
            MATCH_UPPER[b]=s
            REMAIN.remove(s)
            REMAIN.remove(b)
CRITICAL=tuple(sorted(REMAIN))
assert len(MATCH_LOWER)==3400
assert Counter(s.bit_count()-1 for s in CRITICAL)=={0:1,4:1,5:4,6:6}
assert len(CRITICAL)+2*len(MATCH_LOWER)==len(FACES)

def boundary(s):
    sign=1
    for v in range(N):
        bit=1<<v
        if s&bit:
            yield s^bit,sign
            sign=-sign

# Complete face-poset DAG check: reverse exactly the matched edges.
# Unmatched cover incidences are oriented downward.
INDEG={s:0 for s in FACES}
OUT=defaultdict(list)
INCIDENCES=0
for b in FACES:
    if b.bit_count()==1:continue
    for a,sgn in boundary(b):
        assert a in FSET
        INCIDENCES+=1
        if MATCH_LOWER.get(a)==b:
            u,v=a,b
        else:
            u,v=b,a
        OUT[u].append(v)
        INDEG[v]+=1
queue=deque(x for x in FACES if INDEG[x]==0)
visited=0
while queue:
    u=queue.popleft()
    visited+=1
    for v in OUT[u]:
        INDEG[v]-=1
        if INDEG[v]==0:queue.append(v)
assert visited==len(FACES), 'matching is cyclic'
assert all(v==0 for v in INDEG.values())

# Integral algebraic Morse boundary via signed gradient-path recursion.
# Empty faces are not part of the unreduced chain complex.
@lru_cache(None)
def projection(s):
    if s in REMAIN:
        return {s:1}
    if s in MATCH_UPPER:
        return {}
    b=MATCH_LOWER[s]
    pivot=next(c for a,c in boundary(b) if a==s)
    ans=Counter()
    for a,c in boundary(b):
        if a==s:continue
        for t,k in projection(a).items():
            ans[t]-=pivot*c*k
    return {t:k for t,k in ans.items() if k}

CRIT_BY_DIM={d:tuple(s for s in CRITICAL if s.bit_count()==d+1) for d in range(8)}
def morse_boundary(dim):
    rows=CRIT_BY_DIM[dim-1]
    cols=CRIT_BY_DIM[dim]
    rid={r:i for i,r in enumerate(rows)}
    M=[[0]*len(cols) for _ in rows]
    for j,b in enumerate(cols):
        c=Counter()
        for a,sgn in boundary(b):
            for r,k in projection(a).items():c[r]+=sgn*k
        for a,k in c.items():M[rid[a]][j]=k
    return M
B5=morse_boundary(5)
B6=morse_boundary(6)
assert B5==[[-1,0,-1,-1]],B5
assert B6==[[-1,0,0,0,1,-1],[-1,0,-1,-1,1,0],[0,1,0,0,0,1],[1,-1,0,0,-1,0]], B6
assert all(sum(B5[0][i]*B6[i][j] for i in range(4))==0 for j in range(6))

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
          - A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
          + A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
UNIMODULAR = [(rr,cc,det3([[B6[i][j] for j in cc] for i in rr]))
              for rr in combinations(range(4),3) for cc in combinations(range(6),3)
              if abs(det3([[B6[i][j] for j in cc] for i in rr]))==1]
assert UNIMODULAR

# Completely separate mod-2 boundary-rank calculation in the original simplicial chains.
LEVELS={d:tuple(x for x in FACES if x.bit_count()==d+1) for d in range(8)}
RANK={0:0}
for dim in range(1,8):
    rid={s:i for i,s in enumerate(LEVELS[dim-1])}
    piv={}
    for b in LEVELS[dim]:
        col=0
        for a,_ in boundary(b):col ^= 1<<rid[a]
        while col:
            k=col.bit_length()-1
            if k not in piv:
                piv[k]=col
                break
            col^=piv[k]
    RANK[dim]=len(piv)
BETTI={dim:len(LEVELS[dim])-RANK[dim]-RANK.get(dim+1,0) for dim in range(8)}
BETTI[0]-=1
assert BETTI=={0:0,1:0,2:0,3:0,4:0,5:0,6:3,7:0},BETTI

# Every graph automorphism is obtained by exact adjacency-preserving backtracking.
AUT=[]
def find_automorphisms(mapping,used):
    if len(mapping)==N:
        AUT.append(tuple(mapping[i] for i in range(N)))
        return
    v=max((i for i in range(N) if i not in mapping),
          key=lambda i:(sum(bool(ADJ[i]&(1<<j)) for j in mapping),-i))
    for w in range(N):
        if used&(1<<w):continue
        if any(bool(ADJ[v]&(1<<j)) != bool(ADJ[w]&(1<<mapping[j])) for j in mapping):continue
        mapping[v]=w
        find_automorphisms(mapping,used|(1<<w))
        del mapping[v]
find_automorphisms({},0)
assert len(AUT)==96 and len(set(AUT))==96

def ctype(p):
    seen=set();parts=[]
    for i in range(N):
        if i in seen:continue
        k=i;n=0
        while k not in seen:
            seen.add(k);n+=1;k=p[k]
        parts.append(n)
    return tuple(sorted(parts))

def lefschetz(p):
    total=-1  # reduced Lefschetz number: remove the augmentation constant
    for s in FACES:
        v=[i for i in range(N) if s&(1<<i)]
        pi=[p[i] for i in v]
        if sorted(pi)!=v:continue
        inv=sum(pi[i]>pi[j] for i in range(len(pi)) for j in range(i+1,len(pi)))
        total+=(-1)**(len(v)-1+inv)
    return total
CT=defaultdict(Counter)
for p in AUT:CT[ctype(p)][lefschetz(p)]+=1
EXPECTED={
 (1,)*16:{3:1},
 (1,)*4+(2,)*6:{-1:12},
 (1,)*4+(3,)*4:{0:8},
 (2,)*8:{1:18,3:1},
 (2,)*2+(6,)*2:{0:8},
 (4,)*4:{-1:6,-3:2},
 (4,12):{0:16},
 (8,8):{-1:12,1:12},
}
assert {k:dict(v) for k,v in CT.items()}==EXPECTED
assert sum(c*n for ct,counts in CT.items() for c,n in counts.items())==0
assert sum(counts.get(3,0) for counts in CT.values())==2
ROTATION=[]
for j in range(8):
    p=tuple((i+j)%8 if i<8 else 8+(i-8+j)%8 for i in range(N))
    assert p in AUT
    ROTATION.append(lefschetz(p))
assert ROTATION==[3,-1,-1,-1,3,-1,-1,-1]

print('MOBIUS_KANTOR_IND2_HOMOTOPY_AND_FULL_AUT_CHARACTER_OK')
print('face vector',FV,'faces',len(FACES),'facets',len(FACETS),'incidences',INCIDENCES)
print('matched pairs',len(MATCH_LOWER),'critical dimensions',dict(Counter(s.bit_count()-1 for s in CRITICAL)))
print('Morse B5',B5)
print('Morse B6',B6)
print('unimodular 3x3 certificate',UNIMODULAR[0])
print('original mod2 ranks',RANK,'mod2 reduced Betti',BETTI)
print('graph automorphisms',len(AUT),'reduced homology character',dict((str(k),dict(v)) for k,v in sorted(CT.items())))
print('rotation character',ROTATION,'full invariant multiplicity',0,'homology-action kernel order',2)
