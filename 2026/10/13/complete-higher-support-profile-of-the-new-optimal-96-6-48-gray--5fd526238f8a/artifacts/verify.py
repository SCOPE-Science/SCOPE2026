#!/usr/bin/env python3
import itertools, collections, json, math
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

A={0,1}
B={0,2}

def delta(S):
    out=set()
    for vals in itertools.product((0,1),repeat=len(S)):
        v=0
        for i,x in zip(sorted(S),vals):
            if x:v|=1<<i
        out.add(v)
    return out

DA=delta(A)
DB=delta(B)

D=[(d1,d2) for d1 in range(8) for d2 in range(8)
   if not (d1 in DA and d2 in DB)]
assert len(D)==48

cols=[]
for d1,d2 in D:
    cols.append(d2 | (d1<<3))
    cols.append((d1^d2) | (d1<<3))
assert len(cols)==96
assert 0 not in cols

def rank_binary(rows):
    piv={}
    for x in rows:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv:y^=piv[p]
            else:
                piv[p]=y
                break
    return len(piv)

# generator rows encoded as 96-bit integers
G=[]
for i in range(6):
    row=0
    for j,c in enumerate(cols):
        if (c>>i)&1:row|=1<<j
    G.append(row)
assert rank_binary(G)==6

weights=collections.Counter()
for u in range(64):
    z=0
    for i in range(6):
        if (u>>i)&1:z^=G[i]
    weights[z.bit_count()]+=1
assert dict(sorted(weights.items()))=={0:1,48:58,56:4,64:1}

S1={d2 | (d1<<3) for d1 in DA for d2 in DB}
S2={(d1^d2) | (d1<<3) for d1 in DA for d2 in DB}
assert len(S1)==16 and len(S2)==16 and len(S1&S2)==8

mult=collections.Counter(cols)
assert len(mult)==56
assert collections.Counter(mult.values())=={1:16,2:40}

def rref_subspaces(n,d):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv)
              for c in range(p+1,n) if c not in P]
        for vals in itertools.product((0,1),repeat=len(free)):
            R=[1<<p for p in piv]
            for (i,c),v in zip(free,vals):
                if v:R[i]|=1<<c
            yield R

def span(B):
    S={0}
    for v in B:
        S |= {x^v for x in list(S)}
    return S

def orthogonal_subspace(U):
    return {x for x in range(64)
            if all(((x&u).bit_count()&1)==0 for u in U)}

expected={int(r):{int(w):n for w,n in sp.items()}
          for r,sp in CERT["support_spectra"].items()}

count=0
gh=[]
mins=[]
for r in range(1,7):
    ctr=collections.Counter()
    nr=0
    for B0 in rref_subspaces(6,r):
        U=span(B0)
        nr+=1
        count+=1

        # direct support
        support=sum(any(((u&c).bit_count()&1) for u in U) for c in cols)

        W=orthogonal_subspace(U)
        a=(len(W&S1)).bit_length()-1
        b=(len(W&S2)).bit_length()-1
        structural=96-2**(7-r)+2**a+2**b
        assert support==structural
        ctr[support]+=1

    assert nr==CERT["subspaces_by_dimension"][str(r)]
    assert dict(sorted(ctr.items()))==expected[r]
    gh.append(min(ctr))
    mins.append(ctr[min(ctr)])

assert count==CERT["subspaces_checked"]==2824
assert gh==CERT["generalized_hamming_weights"]
assert mins==CERT["minimum_subcode_counts"]

# Check displayed simultaneous Grassmann-bound witnesses.
for r in range(1,7):
    B0=[int(s,2) for s in CERT["annihilator_witness_bases"][f"r{r}"]]
    W=span(B0)
    assert len(W)==2**(6-r)
    target=max(0,4-r)
    assert len(W&S1)==2**target
    assert len(W&S2)==2**target

print("VERIFY_OK")
