#!/usr/bin/env python3
from pathlib import Path
from itertools import combinations
from collections import Counter
import json

ROOT=Path(__file__).resolve().parent.parent
cert=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
hexrows=cert["source_hex_rows"]

def bits_from_hex(s):
    out=[]
    for ch in s:
        v=int(ch,16)
        out += [(v>>b)&1 for b in (3,2,1,0)]
    return out

G56=[bits_from_hex(s) for s in hexrows]
assert all(len(r)==56 for r in G56)
assert all(r[-1]==0 for r in G56)
G=[r[:55] for r in G56]

def rank_rows(rows,ncols):
    vals=[]
    for r in rows:
        v=0
        for j,b in enumerate(r[:ncols]):
            if b:v|=1<<j
        vals.append(v)
    rr=0
    for c in range(ncols):
        p=next((i for i in range(rr,len(vals)) if (vals[i]>>c)&1),None)
        if p is None:continue
        vals[rr],vals[p]=vals[p],vals[rr]
        for i in range(len(vals)):
            if i!=rr and ((vals[i]>>c)&1):
                vals[i]^=vals[rr]
        rr+=1
    return rr

assert rank_rows(G,55)==7
Gram=[[sum(G[i][j]*G[k][j] for j in range(55))&1 for k in range(7)] for i in range(7)]
assert rank_rows(Gram,7)==7

dist=Counter()
for a in range(128):
    w=[0]*55
    for i in range(7):
        if (a>>i)&1:
            w=[x^y for x,y in zip(w,G[i])]
    dist[sum(w)]+=1
expected={int(k):v for k,v in cert["weight_distribution"].items()}
assert dict(sorted(dist.items()))==expected
assert min(w for w in dist if w)>0
assert min(w for w in dist if w)>0 and min(w for w in dist if w)==25

cols=[sum(G[i][j]<<i for i in range(7)) for j in range(55)]
assert all(cols)
freq=Counter(cols)
assert len(freq)==cert["distinct_nonzero_column_types"]
assert max(freq.values())==cert["maximum_column_type_multiplicity"]
duplicated=[j for j,v in enumerate(cols) if freq[v]==2]
# This lists both positions of the unique duplicated type.
assert duplicated==cert["duplicated_column_indices_zero_based"]

def rref_bases(n,d):
    if d==0:
        yield ()
        return
    for pivs in combinations(range(n),d):
        free=[j for j in range(n) if j not in pivs]
        positions=[(i,j) for i,p in enumerate(pivs) for j in free if j>p]
        for mask in range(1<<len(positions)):
            rows=[1<<p for p in pivs]
            for b,(i,j) in enumerate(positions):
                if (mask>>b)&1:
                    rows[i]|=1<<j
            yield tuple(rows)

def span(rows):
    s={0}
    for r in rows:
        s |= {x^r for x in tuple(s)}
    return s

counts=[]
maxima=[]
for d in range(7):
    count=0
    best=-1
    for B in rref_bases(7,d):
        count+=1
        S=span(B)
        hit=sum(v in S for v in cols)
        if hit>best:best=hit
    counts.append(count);maxima.append(best)
assert counts==cert["subspace_counts_by_dimension"]
assert maxima==cert["maximum_column_counts_by_subspace_dimension"]

for ds,w in cert["maximizing_subspace_witnesses"].items():
    d=int(ds)
    B=tuple(w["basis_ints"])
    assert len(B)==d
    S=span(B)
    got=[j for j,v in enumerate(cols) if v in S]
    assert got==w["contained_column_indices_zero_based"]
    assert len(got)==maxima[d]

ghw=[55-maxima[7-r] for r in range(1,8)]
assert ghw==cert["generalized_hamming_weights"]
print("VERIFY_OK")
