#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

MOD=0x11D  # X^8+X^4+X^3+X^2+1

def mul(a,b):
    r=0
    while b:
        if b&1:
            r^=a
        b>>=1
        a<<=1
        if a&0x100:
            a^=MOD
    return r&0xff

def power(a,n):
    r=1
    while n:
        if n&1:
            r=mul(r,a)
        a=mul(a,a)
        n//=2
    return r

def trace(a):
    z=0
    x=a
    for _ in range(8):
        z^=x
        x=mul(x,x)
    assert z in (0,1)
    return z

alpha=2
assert power(alpha,255)==1
assert all(power(alpha,d)!=1 for d in (1,3,5,15,17,51,85))
a1=power(alpha,17)
a2=alpha
assert power(a1,15)==1 and a1 not in (0,1)
assert power(a2,16)!=a2

D=[
    x for x in range(1,256)
    if trace(mul(a1,power(x,17)))==0
    and trace(mul(a2,power(x,17)))==0
]
assert len(D)==119

basis=[1<<i for i in range(8)]

def codeword(b):
    z=0
    for j,x in enumerate(D):
        if trace(mul(b,x)):
            z|=1<<j
    return z

rows=[codeword(b) for b in basis]

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

assert rank_bits(rows)==8
for i in range(8):
    for j in range(i,8):
        assert (rows[i]&rows[j]).bit_count()%2==0

words=[]
for u in range(256):
    z=0
    for i in range(8):
        if (u>>i)&1:
            z^=rows[i]
    words.append(z)

assert collections.Counter(w.bit_count() for w in words)=={0:1,56:136,64:119}

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
        for mask in range(1<<len(free)):
            B=[1<<p for p in piv]
            for k,(i,c) in enumerate(free):
                if (mask>>k)&1:
                    B[i]|=1<<c
            yield B

expected={
    int(r):{int(w):n for w,n in sp.items()}
    for r,sp in CERT["support_spectra"].items()
}

gh=[]
mins=[]
total=0
for r in range(1,9):
    ctr=collections.Counter()
    count=0
    for B in subspaces_rref(8,r):
        support=0
        for u in B:
            support|=words[u]
        ctr[support.bit_count()]+=1
        count+=1
    assert count==qbinom(8,r)
    assert count==CERT["subspace_counts"][str(r)]
    assert dict(sorted(ctr.items()))==expected[r]
    gh.append(min(ctr))
    mins.append(ctr[min(ctr)])
    total+=count

assert total==CERT["subspaces_checked"]==417198
assert gh==CERT["generalized_hamming_weights"]
assert mins==CERT["minimum_subcode_counts"]

print("VERIFY_OK")
