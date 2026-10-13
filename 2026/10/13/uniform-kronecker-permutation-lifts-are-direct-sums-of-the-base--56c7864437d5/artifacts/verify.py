#!/usr/bin/env python3
from itertools import product
from collections import Counter, deque
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CERT = json.loads((ROOT / "artifacts" / "certificate.json").read_text(encoding="utf-8"))

def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(x) for x in zip(*A)]

def matmul2(A,B):
    bt = transpose(B)
    return [[sum(x*y for x,y in zip(r,c)) & 1 for c in bt] for r in A]

def matvec2(A,x):
    return [sum(a*b for a,b in zip(r,x)) & 1 for r in A]

def kron(A,B):
    out=[]
    for ar in A:
        for br in B:
            row=[]
            for a in ar:
                row.extend([(a*b)&1 for b in br])
            out.append(row)
    return out

def rank2(A):
    rows=[]
    ncols=len(A[0]) if A else 0
    for row in A:
        bits=0
        for j,v in enumerate(row):
            bits |= (v&1)<<j
        rows.append(bits)
    r=0
    for c in range(ncols):
        p=next((i for i in range(r,len(rows)) if (rows[i]>>c)&1),None)
        if p is None:
            continue
        rows[r],rows[p]=rows[p],rows[r]
        for i in range(len(rows)):
            if i != r and ((rows[i]>>c)&1):
                rows[i] ^= rows[r]
        r += 1
    return r

def tanner_components(H):
    nr=len(H); nc=len(H[0]) if H else 0
    adj=[[] for _ in range(nr+nc)]
    for i,row in enumerate(H):
        for j,v in enumerate(row):
            if v:
                adj[i].append(nr+j)
                adj[nr+j].append(i)
    seen=set(); comps=[]
    for s in range(nr+nc):
        if s in seen:
            continue
        seen.add(s); q=[s]; comp=[]
        while q:
            u=q.pop()
            comp.append(u)
            for v in adj[u]:
                if v not in seen:
                    seen.add(v); q.append(v)
        comps.append(comp)
    return sorted(len(c) for c in comps)

# Published Cayley-digraph example.
n=12
S={1,2,6}
A=[[1 if (j-i)%n in S else 0 for j in range(n)] for i in range(n)]
assert rank2(A)==10

base_words=[]
for mask in range(1<<n):
    x=[(mask>>j)&1 for j in range(n)]
    if not any(matvec2(A,x)):
        base_words.append(x)
assert len(base_words)==4
base_enum=Counter(sum(x) for x in base_words)
assert dict(sorted(base_enum.items()))=={0:1,8:3}
assert min(sum(x) for x in base_words if any(x))==8
assert tanner_components(A)==[24]

# Three-cycle permutation.
P=[
    [0,1,0],
    [0,0,1],
    [1,0,0],
]
m=3
H=kron(A,P)
R=kron(eye(n),transpose(P))
B1=matmul2(H,R)
assert B1==kron(A,eye(m))

# Perfect shuffle: old index (i,a) -> new index (a,i).
N=n*m
old_to_new=[0]*N
for i in range(n):
    for a in range(m):
        old=i*m+a
        new=a*n+i
        old_to_new[old]=new

B2=[[0]*N for _ in range(N)]
for old_r in range(N):
    new_r=old_to_new[old_r]
    for old_c in range(N):
        new_c=old_to_new[old_c]
        B2[new_r][new_c]=B1[old_r][old_c]
assert B2==kron(eye(m),A)

assert rank2(H)==30
assert N-rank2(H)==6

# Enumerate direct-sum words, transport them to ker(H), and check exhaustively.
lift_enum=Counter()
transported=set()
for blocks in product(base_words, repeat=m):
    z=[bit for block in blocks for bit in block]  # ordering (a,j), kernel of I_m \otimes A
    lift_enum[sum(z)] += 1

    # y = Q^T z, where Q implements old (j,a) -> new (a,j).
    y=[0]*N
    for old in range(N):
        y[old]=z[old_to_new[old]]

    # x = R y. Then Hx = H R y = (A \otimes I_m)y = 0.
    x=matvec2(R,y)
    assert not any(matvec2(H,x))
    key=tuple(x)
    assert key not in transported
    transported.add(key)

assert len(transported)==64
assert dict(sorted(lift_enum.items()))=={0:1,8:9,16:27,24:27}
assert 2**(N-rank2(H))==len(transported)

# Tanner graph is exactly three connected copies in this connected base example.
assert tanner_components(H)==[24,24,24]

assert CERT["source_example"]["base_rank"]==10
assert CERT["source_example"]["base_weight_enumerator"]=={"0":1,"8":3}
assert CERT["verification_lift"]["lift_rank"]==30
assert CERT["verification_lift"]["lift_word_count"]==64
assert CERT["verification_lift"]["lift_weight_enumerator"]=={"0":1,"8":9,"16":27,"24":27}
assert CERT["verification_lift"]["tanner_components"]==3

print("VERIFY_OK")
