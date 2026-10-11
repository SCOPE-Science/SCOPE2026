#!/usr/bin/env python3
"""Standalone exact finite certificate for a generalized Petersen graph complex.

No network or third-party library is required.  All constructions are explicit.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 16
edges = set()
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        edges.add(tuple(sorted((a,b))))
assert len(edges) == 24
adj = [0]*N
for a,b in edges:
    adj[a] |= 1<<b
    adj[b] |= 1<<a
assert all(x.bit_count()==3 for x in adj)

def independent(mask):
    return all(not (mask&(1<<a) and mask&(1<<b)) for a,b in edges)

faces = [mask for mask in range(1,1<<N) if independent(mask)]
fset = set(faces)
assert len(faces)==1090
fvec = [sum(m.bit_count()==j for m in faces) for j in range(1,9)]
assert fvec==[16,96,272,376,240,72,16,2],fvec

available = set(faces)
pairs=[]
for i in range(N):
    bit=1<<i
    for low in faces:
        up=low|bit
        if not (low&bit) and low in available and up in available:
            available.remove(low)
            available.remove(up)
            pairs.append((low,up))
assert len(pairs)==541
crit = sorted(available)
assert len(crit)==8
crit_by_dimension = {d:sorted(x for x in crit if x.bit_count()==d+1) for d in range(8)}
assert {d:len(xs) for d,xs in crit_by_dimension.items() if xs}=={0:1,3:5,4:2}
pair_upper = {lower:upper for lower,upper in pairs}
pair_lower = {upper:lower for lower,upper in pairs}
assert len(pair_upper)==len(pair_lower)==len(pairs)

# Reverse matched cover arrows; orient all other face-poset covers downward.
indegree={x:0 for x in faces}
links=defaultdict(list)
edges_count=0
for up in faces:
    for i in range(N):
        if not up & (1<<i):continue
        low=up^(1<<i)
        if not low:continue
        assert low in fset
        if pair_upper.get(low)==up:
            src,dst=low,up
        else:
            src,dst=up,low
        links[src].append(dst)
        indegree[dst]+=1
        edges_count+=1
assert edges_count==4272
q=deque(x for x in faces if indegree[x]==0)
visited=0
while q:
    x=q.popleft();visited+=1
    for y in links[x]:
        indegree[y]-=1
        if indegree[y]==0:q.append(y)
assert visited==len(faces),('nonacyclic',visited)

def boundary(mask):
    ordered=[i for i in range(N) if mask&(1<<i)]
    for j,i in enumerate(ordered):
        face=mask^(1<<i)
        if face:yield face,(-1 if j%2 else 1)

@lru_cache(None)
def gradient_reduced(x):
    if x in available:
        return {x:1}
    if x in pair_lower:
        return {}
    assert x in pair_upper
    coface=pair_upper[x]
    coeff=dict(boundary(coface))
    own=coeff.pop(x)
    assert abs(own)==1
    result=defaultdict(int)
    for face,c in coeff.items():
        for target,v in gradient_reduced(face).items():
            result[target]-=own*c*v
    return {target:v for target,v in result.items() if v}

rows=crit_by_dimension[3]
cols=crit_by_dimension[4]
M=[[0]*len(cols) for _ in rows]
for j,top in enumerate(cols):
    result=defaultdict(int)
    for low,sgn in boundary(top):
        for target,coeff in gradient_reduced(low).items():
            result[target]+=sgn*coeff
    assert all(k in rows for k,v in result.items() if v)
    for i,low in enumerate(rows):M[i][j]=result.get(low,0)
assert M == [[0,0],[0,0],[1,1],[-1,-1],[0,0]],M
assert all(M[i][0]==M[i][1] for i in range(5))
assert sum(abs(M[i][0]) for i in range(5))>=1
assert 1 in (abs(M[i][0]) for i in range(5))

# Full simplicial F_2 homology computed directly from all original boundary maps.
by_d={d:sorted(x for x in faces if x.bit_count()==d+1) for d in range(8)}
ranks={}
for d in range(1,8):
    base={face:i for i,face in enumerate(by_d[d-1])}
    pivots={}
    for face in by_d[d]:
        bits=0
        for sub,_ in boundary(face): bits ^= 1<<base[sub]
        while bits:
            lead=bits.bit_length()-1
            if lead not in pivots:
                pivots[lead]=bits
                break
            bits^=pivots[lead]
    ranks[d]=len(pivots)
assert ranks == {1:15,2:81,3:191,4:181,5:58,6:14,7:2},ranks
bettis={0:len(by_d[0])-ranks[1]-1}
for d in range(1,8):
    bettis[d]=len(by_d[d])-ranks.get(d,0)-ranks.get(d+1,0)
assert bettis == {0:0,1:0,2:0,3:4,4:1,5:0,6:0,7:0},bettis
assert sum((-1)**d*len(by_d[d]) for d in range(8))==-2
print('VERIFY_OK N=16 edges=24 nonempty_faces=1090 face_vector='+repr(fvec))
print('MATCHING 541_pairs critical_cells=(1:dim0,5:dim3,2:dim4)')
print('ACYCLIC 1090_nodes 4272_oriented_covers')
print('CRITICAL_MASKS dim0=%s dim3=%s dim4=%s' % (crit_by_dimension[0],rows,cols))
print('INTEGRAL_MORSE_BOUNDARY_4_TO_3='+repr(M)+' rank=1 primitive_unit=1')
print('F2_BOUNDARY_RANKS='+repr(ranks)+' REDUCED_BETTI='+repr(bettis))
print('HOMOTOPY=4xS3+1xS4')
