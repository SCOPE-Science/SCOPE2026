#!/usr/bin/env python3
from itertools import product
from collections import Counter
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
cert = json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# GF(16)=GF(2)[a]/(a^4+a+1); a is primitive.
MOD = 0b10011
def mul16(a,b):
    r=0
    while b:
        if b&1:
            r ^= a
        b >>= 1
        a <<= 1
        if a & 0b10000:
            a ^= MOD
    return r & 0b1111

def pow16(a,n):
    r=1
    while n:
        if n&1:
            r=mul16(r,a)
        a=mul16(a,a)
        n >>= 1
    return r

alpha=2
assert pow16(alpha,15)==1
omega=pow16(alpha,5)
omega2=mul16(omega,omega)
F4=[0,1,omega,omega2]
assert pow16(omega,3)==1 and omega not in (0,1)

def inv4(a):
    assert a
    for b in F4:
        if mul16(a,b)==1:
            return b
    raise AssertionError

def coset(w):
    out=[]
    x=w
    while x not in out:
        out.append(x)
        x=(4*x)%15
    return out

R=set()
for w in cert["defining_set_representatives"]["Delta1"] + cert["defining_set_representatives"]["Delta2"] + cert["defining_set_representatives"]["added"]:
    R.update(coset(w))
assert sorted(R)==cert["defining_set"]
T=sorted(set(range(15))-R)
assert T==cert["complement_exponents"]==[10,11,14]

def pmul(A,B):
    C=[0]*(len(A)+len(B)-1)
    for i,a in enumerate(A):
        for j,b in enumerate(B):
            C[i+j] ^= mul16(a,b)
    return C

h=[1]
for t in T:
    h=pmul(h,[pow16(alpha,t),1])
assert h==[omega,1,0,1]  # omega + x + x^3

def pdiv(num,den):
    num=num[:]
    q=[0]*(len(num)-len(den)+1)
    while True:
        while num and num[-1]==0:
            num.pop()
        if len(num)<len(den):
            break
        k=len(num)-len(den)
        c=mul16(num[-1],inv4(den[-1]))
        q[k]=c
        for j,d in enumerate(den):
            num[k+j] ^= mul16(c,d)
    return q,num

g,rem=pdiv([1]+[0]*14+[1],h)
assert rem==[]
expected_g=[omega2,omega,1,1,omega,omega,omega,0,1,omega,1,0,1]
assert g==expected_g

def peval(poly,x):
    y=0
    for c in reversed(poly):
        y=mul16(y,x)^c
    return y

zeros=[i for i in range(15) if peval(g,pow16(alpha,i))==0]
assert zeros==sorted(R)

G=[]
for shift in range(3):
    row=[0]*15
    for j,c in enumerate(g):
        row[shift+j]=c
    G.append(row)

def rank4(A):
    A=[row[:] for row in A]
    r=0
    for c in range(len(A[0]) if A else 0):
        p=next((i for i in range(r,len(A)) if A[i][c]!=0),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        z=inv4(A[r][c])
        A[r]=[mul16(z,x) for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[x ^ mul16(f,y) for x,y in zip(A[i],A[r])]
        r += 1
    return r

assert rank4(G)==3

def dot(u,v):
    s=0
    for a,b in zip(u,v):
        s ^= mul16(a,b)
    return s

assert all(dot(G[i],G[j])==0 for i in range(3) for j in range(3))

words=[]
weights=Counter()
for c in product(F4,repeat=3):
    w=[]
    for j in range(15):
        x=0
        for i in range(3):
            x ^= mul16(c[i],G[i][j])
        w.append(x)
    words.append(tuple(w))
    weights[sum(x!=0 for x in w)] += 1

assert len(set(words))==64
assert weights==Counter({0:1,11:45,12:15,15:3})

def norm(v):
    for x in v:
        if x:
            z=inv4(x)
            return tuple(mul16(z,y) for y in v)
    return None

points=set()
for v in product(F4,repeat=3):
    if any(v):
        points.add(norm(v))
assert len(points)==21

cols=[norm(tuple(G[i][j] for i in range(3))) for j in range(15)]
assert len(set(cols))==15
missing=points-set(cols)
assert len(missing)==6

normal=(1,1,omega)
line={p for p in points if (mul16(normal[0],p[0]) ^ mul16(normal[1],p[1]) ^ mul16(normal[2],p[2]))==0}
assert len(line)==5
P=(1,omega2,omega)
assert P not in line
assert missing==line|{P}

# Projective line intersection spectrum of retained points.
S=set(cols)
intersection_counts=Counter()
for n in points:
    M={p for p in points if (mul16(n[0],p[0]) ^ mul16(n[1],p[1]) ^ mul16(n[2],p[2]))==0}
    intersection_counts[len(M&S)] += 1
assert intersection_counts==Counter({4:15,3:5,0:1})

# Generalized Hamming weight d2: enumerate all 2-spaces of message space.
vectors=[v for v in product(F4,repeat=3) if any(v)]
subspaces=set()
support_hist=Counter()
for u in vectors:
    for v in vectors:
        if rank4([list(u),list(v)])<2:
            continue
        U=frozenset(
            tuple(mul16(a,u[j]) ^ mul16(b,v[j]) for j in range(3))
            for a,b in product(F4,repeat=2)
        )
        if U in subspaces:
            continue
        subspaces.add(U)
        supp=set()
        for c in U:
            for j in range(15):
                x=0
                for i in range(3):
                    x ^= mul16(c[i],G[i][j])
                if x:
                    supp.add(j)
        support_hist[len(supp)] += 1

assert len(subspaces)==21
assert support_hist==Counter({14:15,15:6})
assert min(support_hist)==14
assert cert["generalized_hamming_weights"]==[11,14,15]

# Bound checks used in the statement.
assert 11 + ((11+3)//4) + ((11+15)//16) == 15  # Griesmer
assert 15-3+2 == 14  # generalized Singleton upper bound for d2

print("VERIFY_OK")
