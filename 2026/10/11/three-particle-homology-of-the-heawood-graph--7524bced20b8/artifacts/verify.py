#!/usr/bin/env python3
from itertools import combinations, product, combinations_with_replacement
from pathlib import Path
from math import gcd
import json

verts=[('p',i) for i in range(7)]+[('l',i) for i in range(7)]
vid={v:i for i,v in enumerate(verts)}
edges=[]
for i in range(7):
    for d in (0,1,3):
        j=(i-d)%7
        a,b=vid[('p',i)],vid[('l',j)]
        if a>b:a,b=b,a
        edges.append((a,b))
edges=sorted(set(edges))
assert len(verts)==14 and len(edges)==21
inc=[[] for _ in verts]
for ei,(a,b) in enumerate(edges):
    inc[a].append(ei); inc[b].append(ei)
for x in inc:
    x.sort(); assert len(x)==3

def basis(d,n=3):
    mons=list(combinations_with_replacement(range(21),n-d)) if n-d else [()]
    out=[]
    for vs in combinations(range(14),d):
        for bits in product((0,1),repeat=d):
            gens=tuple(zip(vs,bits))
            for mo in mons: out.append((gens,mo))
    return out
B=[basis(d) for d in range(4)]
assert [len(x) for x in B]==[1771,6468,7644,2912]
idx=[{x:i for i,x in enumerate(b)} for b in B]

def boundary_col(d,cell):
    gens,mo=cell; out={}
    for pos,(v,bit) in enumerate(gens):
        base,other=inc[v][0],inc[v][bit+1]
        rg=gens[:pos]+gens[pos+1:]
        s=-1 if pos%2 else 1
        for e,c in ((other,s),(base,-s)):
            key=(rg,tuple(sorted(mo+(e,))))
            r=idx[d-1][key]
            out[r]=out.get(r,0)+c
            if not out[r]: del out[r]
    return out
cols=[None]+[[boundary_col(d,c) for c in B[d]] for d in range(1,4)]
for d in (2,3):
    for col in cols[d]:
        acc={}
        for r,c in col.items():
            for rr,c2 in cols[d-1][r].items():
                acc[rr]=acc.get(rr,0)+c*c2
                if not acc[rr]: del acc[rr]
        assert not acc

def rank_mod(columns,p):
    piv={}
    rank=0
    for col0 in columns:
        v={r:c%p for r,c in col0.items() if c%p}
        while v:
            pr=max(v)
            if pr not in piv:
                inv=pow(v[pr],-1,p)
                v={r:(c*inv)%p for r,c in v.items() if (c*inv)%p}
                piv[pr]=v; rank+=1; break
            fac=v[pr]; pv=piv[pr]
            for r,c in pv.items():
                nv=(v.get(r,0)-fac*c)%p
                if nv:v[r]=nv
                else:v.pop(r,None)
    return rank
expected={2:(1770,4689,2911),3:(1770,4690,2911)}
for p,want in expected.items():
    got=tuple(rank_mod(cols[d],p) for d in range(1,4))
    assert got==want,(p,got,want)
    betti=[]
    ranks=(0,)+got
    for d in range(4):
        ker=len(B[d])-(ranks[d] if d else 0)
        im=ranks[d+1] if d<3 else 0
        betti.append(ker-im)
    assert tuple(betti)==({2:(1,9,44,1),3:(1,8,43,1)}[p])

cert=json.loads((Path(__file__).with_name('d3_kernel.json')).read_text())
vec={int(k):int(v) for k,v in cert.items()}
assert len(vec)==881
assert set(vec.values()) <= {-1,1}
g=0
for v in vec.values():g=gcd(g,abs(v))
assert g==1
acc={}
for j,x in vec.items():
    assert 0<=j<len(B[3])
    for r,c in cols[3][j].items():
        acc[r]=acc.get(r,0)+x*c
        if not acc[r]:acc.pop(r,None)
assert not acc
print('HEAWOOD_B3_HOMOLOGY_VERIFY_OK')
