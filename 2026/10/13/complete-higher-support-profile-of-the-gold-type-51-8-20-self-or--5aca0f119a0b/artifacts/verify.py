#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

MOD=(1<<8)|(1<<4)|(1<<3)|(1<<2)|1

def mul(a,b):
    r=0
    while b:
        if b&1:
            r^=a
        b>>=1
        a<<=1
        if a&(1<<8):
            a^=MOD
    return r&255

def power(a,n):
    r=1
    while n:
        if n&1:
            r=mul(r,a)
        a=mul(a,a)
        n>>=1
    return r

def trace(a):
    s=0
    x=a
    for _ in range(8):
        s^=x
        x=mul(x,x)
    assert s in (0,1)
    return s

alpha=2
x=alpha
order=1
while x!=1:
    x=mul(x,alpha)
    order+=1
assert order==255

a1=alpha
a2=mul(alpha,alpha)
D=[x for x in range(1,256)
   if trace(mul(a1,power(x,17)))==0
   and trace(mul(a2,power(x,17)))==0]
assert len(D)==51

betas=[power(alpha,i) for i in range(8)]
rows=[]
for b in betas:
    z=0
    for j,x in enumerate(D):
        if trace(mul(b,x)):
            z|=1<<j
    rows.append(z)

def rank_bits(vs):
    piv={}
    for z in vs:
        y=z
        while y:
            p=y.bit_length()-1
            if p in piv:
                y^=piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

assert rank_bits(rows)==8

words=[0]*256
for u in range(256):
    z=0
    for i in range(8):
        if (u>>i)&1:
            z^=rows[i]
    words[u]=z

assert collections.Counter(w.bit_count() for w in words)=={
    0:1,20:34,24:102,28:102,32:17
}

def qbinom(n,r):
    if r<0 or r>n:
        return 0
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

for r in range(1,9):
    B=[int(s,2) for s in CERT["minimizer_witness_bases"][str(r)]]
    assert rank_bits(B)==r
    support=0
    for u in B:
        support|=words[u]
    assert support.bit_count()==gh[r-1]

print("VERIFY_OK")
