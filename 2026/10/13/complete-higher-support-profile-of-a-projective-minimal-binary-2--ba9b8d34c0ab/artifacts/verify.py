#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

MOD=0b1011  # X^3+X+1

def mul(a,b):
    r=0
    while b:
        if b&1:
            r^=a
        b>>=1
        a<<=1
        if a&8:
            a^=MOD
    return r&7

def power(a,n):
    r=1
    while n:
        if n&1:
            r=mul(r,a)
        a=mul(a,a)
        n//=2
    return r

def trace(a):
    t=a ^ power(a,2) ^ power(a,4)
    assert t in (0,1)
    return t

D=[]
for x in range(1,8):
    for y in range(8):
        value=mul(mul(x,x),y) ^ mul(x,y) ^ x
        if trace(value)==0:
            D.append((x,y))
assert len(D)==24

basis=[
    (1,0),(2,0),(4,0),
    (0,1),(0,2),(0,4)
]

def codeword(v):
    a,b=v
    z=0
    for j,(x,y) in enumerate(D):
        bit=trace(mul(mul(a,x),y) ^ mul(b,x))
        if bit:
            z|=1<<j
    return z

rows=[codeword(v) for v in basis]

def rank_bits(vs):
    piv={}
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:
                y^=piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

assert rank_bits(rows)==6

words=[]
for u in range(64):
    z=0
    for i in range(6):
        if (u>>i)&1:
            z^=rows[i]
    words.append(z)

assert collections.Counter(w.bit_count() for w in words)=={
    0:1,10:24,12:12,14:24,16:3
}

def qbinom(n,r):
    a=b=1
    for i in range(r):
        a*=2**(n-i)-1
        b*=2**(r-i)-1
    return a//b

def subspaces_rref(n,d):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv)
              for c in range(p+1,n) if c not in P]
        for vals in itertools.product((0,1),repeat=len(free)):
            B=[1<<p for p in piv]
            for (i,c),v in zip(free,vals):
                if v:
                    B[i]|=1<<c
            yield B

expected={
    int(r):{int(w):n for w,n in sp.items()}
    for r,sp in CERT["support_spectra"].items()
}

gh=[]
mins=[]
total=0
for r in range(1,7):
    ctr=collections.Counter()
    count=0
    for B in subspaces_rref(6,r):
        support=0
        for u in B:
            support|=words[u]
        ctr[support.bit_count()]+=1
        count+=1
    assert count==qbinom(6,r)
    assert count==CERT["subspace_counts"][str(r)]
    assert dict(sorted(ctr.items()))==expected[r]
    gh.append(min(ctr))
    mins.append(ctr[min(ctr)])
    total+=count

assert total==CERT["subspaces_checked"]==2824
assert gh==CERT["generalized_hamming_weights"]
assert mins==CERT["minimum_subcode_counts"]

print("VERIFY_OK")
