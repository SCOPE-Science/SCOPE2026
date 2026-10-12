#!/usr/bin/env python3
import json, math
from itertools import combinations
from pathlib import Path

def dp_counts(s,k):
    offsets={}
    off=0
    for ell in range(1,k+1):
        offsets[ell]=off
        off += 2**ell
    zero=(0,)*off
    a2=zero
    a1=zero
    for ch in s:
        b=int(ch)
        cur=list(a1)
        cur[offsets[1]+b] += 1
        for ell in range(2,k+1):
            for q in range(2**(ell-1)):
                cur[offsets[ell]+(q<<1)+b] += a2[offsets[ell-1]+q]
        a2,a1=a1,tuple(cur)
    out={}
    off=0
    for ell in range(1,k+1):
        for q in range(2**ell):
            out[format(q,f"0{ell}b")] = a1[off+q]
        off += 2**ell
    return out

def direct_counts(s,k):
    n=len(s)
    out={}
    for ell in range(1,k+1):
        c={format(q,f"0{ell}b"):0 for q in range(2**ell)}
        # If j_0<...<j_{ell-1} are chosen from 0..n-ell,
        # then i_r=j_r+r are exactly all index tuples with gaps at least 2.
        for js in combinations(range(n-ell+1),ell):
            idx=[js[r]+r for r in range(ell)]
            p=''.join(s[i] for i in idx)
            c[p]+=1
        out.update(c)
    return out

root=Path(__file__).resolve().parent
cert=json.loads((root/"certificate.json").read_text(encoding="utf-8"))
x=cert["published_length_24_pair"]["x"]
y=cert["published_length_24_pair"]["y"]
u=cert["witness"]["u"]
v=cert["witness"]["v"]
assert len(x)==len(y)==24 and x!=y
assert len(u)==len(v)==50 and u!=v
assert u=="0"+x+y+"1"
assert v=="0"+y+x+"1"

# Reproduce the published k=4 confusable pair.
assert dp_counts(x,4)==dp_counts(y,4)

du=dp_counts(u,5)
dv=dp_counts(v,5)
assert du==dv==cert["common_gapped_subsequence_counts"]

# Independent direct enumeration of every nonadjacent occurrence.
eu=direct_counts(u,5)
ev=direct_counts(v,5)
assert eu==ev==du

for ell in range(1,6):
    subtotal=sum(c for p,c in du.items() if len(p)==ell)
    assert subtotal==math.comb(50-ell+1,ell)

assert len(du)==sum(2**ell for ell in range(1,6))==62
published_bound=4*(2**5-1)-2
assert published_bound==122
print("VERIFY_OK length=50 patterns=62 G5_upper=50 published_bound=122 reduction=72 source_pair_length=24")
