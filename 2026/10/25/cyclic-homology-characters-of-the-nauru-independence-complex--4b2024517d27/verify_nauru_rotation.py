#!/usr/bin/env python3
"""Exact integral Morse and cyclic-Lefschetz check for the Nauru independence complex.

All arithmetic is over Z; no third-party dependencies. Conventions:
vertex i is u_i, 12+i is v_i, and sorted vertex order orients simplices.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 12
adj = [0] * (2*N)
for i in range(N):
    for a,b in ((i,(i+1)%N),(i,i+N),(N+i,N+(i+5)%N)):
        adj[a] |= 1 << b
        adj[b] |= 1 << a
assert all(x.bit_count()==3 for x in adj)

faces = set()
levels = Counter()
def enumerate_faces(remaining, chosen):
    if chosen:
        faces.add(chosen)
        levels[chosen.bit_count()-1] += 1
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        vertex = bit.bit_length()-1
        enumerate_faces(remaining & ~adj[vertex], chosen | bit)
enumerate_faces((1<<(2*N))-1, 0)
assert [levels[i] for i in range(12)] == [24,240,1304,4212,8328,10036,7176,2964,752,156,24,2]
assert len(faces)==35218

match = {}
face_order = sorted(faces, key=lambda mask:(mask.bit_count(),mask))
for v in range(2*N):
    bit = 1<<v
    for f in face_order:
        if f & bit or f in match:
            continue
        g = f|bit
        if g in faces and g not in match:
            match[f]=g
            match[g]=f
assert len(match)==35208
critical = defaultdict(list)
for f in face_order:
    if f not in match:
        critical[f.bit_count()-1].append(f)
assert {k:len(v) for k,v in critical.items()} == {0:1,5:6,6:3}


def boundary(face):
    remaining=face
    while remaining:
        bit=remaining & -remaining
        remaining ^= bit
        v=bit.bit_length()-1
        lower=face ^ bit
        if lower:
            yield lower, -1 if (face & (bit-1)).bit_count() % 2 else 1

# Complete directed-Hasse-graph acyclicity certificate.
indeg={f:0 for f in faces}
succ=defaultdict(list)
incidences=0
for high in faces:
    for low,sign in boundary(high):
        incidences+=1
        if match.get(low)==high:
            src,dst=low,high
        else:
            src,dst=high,low
        succ[src].append(dst)
        indeg[dst]+=1
queue=deque(f for f in faces if indeg[f]==0)
visited=0
while queue:
    f=queue.popleft()
    visited+=1
    for g in succ[f]:
        indeg[g]-=1
        if indeg[g]==0:
            queue.append(g)
assert visited==len(faces),(visited,len(faces))
# Avoid retaining the Hasse graph during chain computations.
del indeg,succ,queue

@lru_cache(None)
def project(face):
    if face not in match:
        return {face:1}
    upper=match[face]
    if upper.bit_count()<face.bit_count():
        return {}
    eps=next(sign for low,sign in boundary(upper) if low==face)
    out=Counter()
    for low,sign in boundary(upper):
        if low==face:
            continue
        for basis,coeff in project(low).items():
            out[basis]-=eps*sign*coeff
    return {f:c for f,c in out.items() if c}

@lru_cache(None)
def homotopy(face):
    if face not in match:
        return {}
    upper=match[face]
    if upper.bit_count()<face.bit_count():
        return {}
    eps=next(sign for low,sign in boundary(upper) if low==face)
    out=Counter({upper:eps})
    for low,sign in boundary(upper):
        if low==face:
            continue
        for basis,coeff in homotopy(low).items():
            out[basis]-=eps*sign*coeff
    return {f:c for f,c in out.items() if c}

def chain_boundary(chain):
    out=Counter()
    for f,c in chain.items():
        for low,s in boundary(f):
            out[low]+=c*s
    return {f:c for f,c in out.items() if c}

def chain_project(chain):
    out=Counter()
    for f,c in chain.items():
        for basis,z in project(f).items():
            out[basis]+=c*z
    return {f:c for f,c in out.items() if c}

def lift(face):
    out=Counter({face:1})
    for lower,s in boundary(face):
        for upper,z in homotopy(lower).items():
            out[upper]-=s*z
    return {f:c for f,c in out.items() if c}

C5=critical[5]
C6=critical[6]
B=[]
for f in C6:
    vec=chain_project(chain_boundary({f:1}))
    B.append([vec.get(g,0) for g in C5])
assert B == [[1,0,0,1,1,0],[1,0,0,0,0,0],[0,0,0,-1,-1,0]],B
# Two independent primitive columns: rows 0 and 3, columns 0 and 1 give determinant -1.
assert B[0][0]*B[1][3]-B[0][3]*B[1][0]==-1
assert [B[0][i]-B[1][i]+B[2][i] for i in range(6)] == [0]*6
# This proves reduced integral Betti ranks b_5=4, b_6=1 with no torsion.
z=Counter()
for f,coeff in zip(C6,(1,-1,1)):
    for sigma,c in lift(f).items():
        z[sigma]+=coeff*c
z={f:c for f,c in z.items() if c}
assert not chain_boundary(z)
assert chain_project(z)==dict(zip(C6,(1,-1,1)))

def rotated(face,k):
    image=[(v+k)%N if v<N else N+(v-N+k)%N
           for v in range(2*N) if face & (1<<v)]
    out=sum(1<<i for i in image)
    parity=sum(a>b for t,a in enumerate(image) for b in image[t+1:])%2
    return out,(-1 if parity else 1)

rotated_z=Counter()
for f,c in z.items():
    g,s=rotated(f,1)
    rotated_z[g]+=c*s
p_rz=chain_project(rotated_z)
assert p_rz=={C6[0]:-1,C6[1]:1,C6[2]:-1},p_rz
assert not chain_boundary(rotated_z)

L=[]
for k in range(12):
    # Augmentation contributes -1, so this is a reduced Lefschetz number.
    value=-1
    for f in faces:
        g,s=rotated(f,k)
        if f==g:
            value+=((-1 if (f.bit_count()-1)%2 else 1)*s)
    L.append(value)
assert L == [-3,-1,1,-1,-3,-1,1,-1,-3,-1,1,-1], L
H6=[(-1)**k for k in range(12)]
H5=[H6[k]-L[k] for k in range(12)]
assert H5 == [4,0,0,0,4,0,0,0,4,0,0,0]
assert sum(H5)==12 # one invariant in H5
assert sum(H6)==0  # no invariant in H6
print('FACE_VECTOR', [levels[d] for d in range(12)])
print('FACE_INCIDENCES', incidences)
print('MATCHED_PAIRS', len(match)//2)
print('CRITICAL_COUNTS', {k:len(v) for k,v in critical.items()})
print('INTEGER_MORSE_BOUNDARY_COLUMNS', B)
print('INTEGRAL_HOMOLOGY', {5:'Z^4',6:'Z'})
print('CYCLE_SUPPORT', len(z))
print('ROTATION_TOP_ACTION', -1)
print('REDUCED_LEFSCHETZ', L)
print('H5_CHARACTER', H5)
print('H6_CHARACTER', H6)
print('VERIFY_OK')
