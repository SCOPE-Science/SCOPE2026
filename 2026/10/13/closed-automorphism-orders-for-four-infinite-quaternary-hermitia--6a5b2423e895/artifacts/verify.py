#!/usr/bin/env python3
import itertools, math, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# F4 = F2[w]/(w^2+w+1), encoded 0,1,w,w^2 as 0,1,2,3.
def mul(a,b):
    r=0
    while b:
        if b&1:
            r^=a
        b>>=1
        a<<=1
        if a&4:
            a^=0b111
    return r&3

def conj(a):
    return mul(a,a)

INV={1:1,2:3,3:2}

def det2(A):
    return mul(A[0][0],A[1][1]) ^ mul(A[0][1],A[1][0])

def mat_vec(A,v):
    return (
        mul(A[0][0],v[0]) ^ mul(A[0][1],v[1]),
        mul(A[1][0],v[0]) ^ mul(A[1][1],v[1])
    )

PTS=[(1,0),(0,1),(1,1),(1,2),(1,3)]

def normalize(v):
    a,b=v
    if a:
        ia=INV[a]
        return (1,mul(ia,b))
    assert b
    return (0,1)

# Sum of Hermitian Gram contributions of the full projective line.
gram=[[0,0],[0,0]]
for v in PTS:
    for i in range(2):
        for j in range(2):
            gram[i][j] ^= mul(v[i],conj(v[j]))
assert gram==[[0,0],[0,0]]

GL=[]
for entries in itertools.product(range(4),repeat=4):
    A=[[entries[0],entries[1]],[entries[2],entries[3]]]
    if det2(A):
        GL.append(A)
assert len(GL)==180

perms=[]
for A in GL:
    p=[]
    for v in PTS:
        w=normalize(mat_vec(A,v))
        p.append(PTS.index(w))
    perms.append(tuple(p))
PGL=sorted(set(perms))
assert len(PGL)==60

def mults(name,s):
    if name=="A": return [s-1,s+1,s+2,s+2,s-1]
    if name=="B": return [s,s+1,s+1,s+2,s-1]
    if name=="C": return [s+1,s+1,s+1,s+2,s-2]
    if name=="D": return [s+1,s+1,s+2,s+2,s-3]
    raise ValueError

def projective_stab(m):
    count=0
    for p in PGL:
        if all(m[i]==m[p[i]] for i in range(5)):
            count+=1
    return count

assert [projective_stab(mults(x,6)) for x in "ABCD"]==[2,1,3,2]

def generator(m):
    rows=[[],[]]
    for j,v in enumerate(PTS):
        for _ in range(m[j]):
            rows[0].append(v[0])
            rows[1].append(v[1])
    return rows

def hermitian_gram(G):
    n=len(G[0])
    H=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            z=0
            for c in range(n):
                z ^= mul(G[i][c],conj(G[j][c]))
            H[i][j]=z
    return H

def rank2(H):
    return 2 if det2(H) else (1 if any(H[0]+H[1]) else 0)

def weight_enum(G):
    ctr={}
    n=len(G[0])
    for a,b in itertools.product(range(4),repeat=2):
        w=0
        for j in range(n):
            x=mul(a,G[0][j]) ^ mul(b,G[1][j])
            w += (x!=0)
        ctr[w]=ctr.get(w,0)+1
    return ctr

def expected_enum(name,s):
    if name=="A": return {0:1,4*s+1:6,4*s+2:3,4*s+4:6}
    if name=="B": return {0:1,4*s+1:3,4*s+2:6,4*s+3:3,4*s+4:3}
    if name=="C": return {0:1,4*s+1:3,4*s+2:9,4*s+5:3}
    if name=="D": return {0:1,4*s+1:6,4*s+2:6,4*s+6:3}

for s in (6,7,10):
    for name in "ABCD":
        m=mults(name,s)
        G=generator(m)
        assert len(G[0])==5*s+3
        assert rank2(hermitian_gram(G))==2
        assert weight_enum(G)==expected_enum(name,s)
        assert min(w for w in weight_enum(G) if w)>0
        assert min(w for w in weight_enum(G) if w)>0 and min(w for w in weight_enum(G) if w)==4*s+1
        st=projective_stab(m)
        assert st==CERT["classes"][name]["projective_stabilizer_order"]
        general=3*st
        for x in m:
            general*=math.factorial(x)
        if name=="A":
            closed=6*math.factorial(s-1)**2*math.factorial(s+1)*math.factorial(s+2)**2
        elif name=="B":
            closed=3*math.factorial(s-1)*math.factorial(s)*math.factorial(s+1)**2*math.factorial(s+2)
        elif name=="C":
            closed=9*math.factorial(s-2)*math.factorial(s+1)**3*math.factorial(s+2)
        else:
            closed=6*math.factorial(s-3)*math.factorial(s+1)**2*math.factorial(s+2)**2
        assert general==closed

# Verify the printed s=5 seed vectors.
assert [mults(x,5) for x in "ABCD"]==CERT["source_seed_vectors"]

print("VERIFY_OK")
