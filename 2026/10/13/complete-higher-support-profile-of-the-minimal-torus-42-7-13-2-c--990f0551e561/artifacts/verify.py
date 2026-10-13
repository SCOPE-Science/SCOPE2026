#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/'artifacts'/'certificate.json').read_text(encoding='utf-8'))
facets=set()
for i in range(7):
    facets.add(tuple(sorted((i,(i+1)%7,(i+3)%7))))
    facets.add(tuple(sorted((i,(i+2)%7,(i+3)%7))))
assert len(facets)==14
faces=set()
for f in facets:
    for r in (1,2,3): faces.update(itertools.combinations(f,r))
assert collections.Counter(map(len,faces))=={1:7,2:21,3:14}
edge_to_facets=collections.defaultdict(list)
for f in facets:
    for e in itertools.combinations(f,2): edge_to_facets[tuple(sorted(e))].append(f)
assert len(edge_to_facets)==21 and all(len(v)==2 for v in edge_to_facets.values())
for v in range(7):
    L=[]
    for f in facets:
        if v in f: L.append(tuple(sorted(x for x in f if x!=v)))
    deg=collections.Counter(x for e in L for x in e)
    assert len(L)==6 and len(deg)==6 and set(deg.values())=={2}
def edge_coeff(tri,e):
    a,b,c=tri; e=tuple(sorted(e))
    if e==(b,c): return 1
    if e==(a,c): return -1
    if e==(a,b): return 1
    raise AssertionError
sgn={next(iter(facets)):1}; stack=list(sgn)
while stack:
    f=stack.pop()
    for e in itertools.combinations(f,2):
        e=tuple(sorted(e)); fs=edge_to_facets[e]; g=fs[0] if fs[1]==f else fs[1]
        want=-sgn[f]*edge_coeff(f,e)//edge_coeff(g,e)
        if g in sgn: assert sgn[g]==want
        else: sgn[g]=want; stack.append(g)
assert len(sgn)==14 and 7-21+14==0
cols=[sum(1<<v for v in f) for f in sorted(faces,key=lambda x:(len(x),x))]
rows=[]
for v in range(7):
    z=0
    for j,c in enumerate(cols):
        if (c>>v)&1: z|=1<<j
    rows.append(z)
assert len(cols)==42 and [z.bit_count() for z in rows]==[13]*7
def rank2(vs):
    piv={}
    for x in vs:
        y=x
        while y:
            p=y.bit_length()-1
            if p in piv: y^=piv[p]
            else: piv[p]=y; break
    return len(piv)
assert rank2(rows)==7
words=[]
for u in range(128):
    z=0
    for i in range(7):
        if (u>>i)&1: z^=rows[i]
    words.append(z)
assert collections.Counter(z.bit_count() for z in words)=={0:1,13:7,20:42,21:43,24:21,25:14}
def qbinom(n,r):
    a=b=1
    for i in range(r): a*=2**(n-i)-1; b*=2**(r-i)-1
    return a//b
def subspaces_rref(n,d):
    for piv in itertools.combinations(range(n),d):
        P=set(piv); free=[]
        for i,p in enumerate(piv):
            for c in range(p+1,n):
                if c not in P: free.append((i,c))
        for vals in itertools.product((0,1),repeat=len(free)):
            B=[1<<p for p in piv]
            for (i,c),v in zip(free,vals):
                if v: B[i]|=1<<c
            yield B
expected={int(r):{int(w):n for w,n in sp.items()} for r,sp in CERT['support_spectra'].items()}
gh=[]; mins=[]; total=0
for r in range(1,8):
    ctr=collections.Counter(); count=0
    for B in subspaces_rref(7,r):
        support=0
        for u in B: support|=words[u]
        ctr[support.bit_count()]+=1; count+=1
    assert count==qbinom(7,r)==CERT['subspace_counts'][str(r)]
    assert dict(sorted(ctr.items()))==expected[r]
    gh.append(min(ctr)); mins.append(ctr[min(ctr)]); total+=count
assert total==CERT['subspaces_checked']==29211
assert gh==CERT['generalized_hamming_weights']
assert mins==CERT['minimum_subcode_counts']
print('VERIFY_OK')
