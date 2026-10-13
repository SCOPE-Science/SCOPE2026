#!/usr/bin/env python3
import itertools, collections, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

g=sum(1<<i for i in (0,2,3,6,7,9))
rows=[g<<i for i in range(6)]

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

words=[0]*64
for u in range(64):
    z=0
    for i in range(6):
        if (u>>i)&1:
            z^=rows[i]
    words[u]=z

assert collections.Counter(x.bit_count() for x in words)=={
    0:1,6:25,8:30,10:3,12:5
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

for r in range(1,7):
    B=[int(s,2) for s in CERT["minimizer_witness_bases"][str(r)]]
    assert rank_bits(B)==r
    support=0
    for u in B:
        support|=words[u]
    assert support.bit_count()==gh[r-1]

print("VERIFY_OK")
