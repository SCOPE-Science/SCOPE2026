#!/usr/bin/env python3
import json
from itertools import combinations, combinations_with_replacement, product
from collections import defaultdict, Counter
from pathlib import Path

N=18
OFFSETS=[5,7,-7,7,-7,-5]*3
edges=set()
for i,o in enumerate(OFFSETS):
    edges.add(tuple(sorted((i,(i+o)%N))))
for i in range(N):
    edges.add(tuple(sorted((i,(i+1)%N))))
E=sorted(edges)
assert len(E)==27
assert Counter(x for e in E for x in e)==Counter({v:3 for v in range(N)})
eid={e:i for i,e in enumerate(E)}
inc={v:sorted(eid[e] for e in E if v in e) for v in range(N)}
# alpha[v][a] has boundary e_plus-e_ref.
alpha={v:[(inc[v][1],inc[v][0]),(inc[v][2],inc[v][0])] for v in range(N)}

# C2: two reduced local generators and one edge particle.
c2_index={}
c2=[]
for vs in combinations(range(N),2):
    for aa in product(range(2),repeat=2):
        for e in range(27):
            c2_index[(vs,aa,e)]=len(c2); c2.append((vs,aa,e))
# C3: three reduced local generators and no edge particle.
c3=[]; d3=[]
for vs in combinations(range(N),3):
    for aa in product(range(2),repeat=3):
        c3.append((vs,aa)); col=defaultdict(int)
        for pos,v in enumerate(vs):
            rvs=vs[:pos]+vs[pos+1:]; raa=aa[:pos]+aa[pos+1:]
            ep,em=alpha[v][aa[pos]]; s=1 if pos%2==0 else -1
            col[c2_index[(rvs,raa,ep)]] += s
            col[c2_index[(rvs,raa,em)]] -= s
        d3.append({r:c for r,c in col.items() if c})
assert len(c3)==6528 and len(c2)==16524
assert all(len(c)==6 for c in d3)

# Build C1 and d2 solely to check d2*d3=0 with the same sign convention.
pairs=list(combinations_with_replacement(range(27),2))
c1_index={}
for v in range(N):
    for a in range(2):
        for mm in pairs:
            c1_index[(v,a,mm)]=len(c1_index)
d2=[]
for vs,aa,e in c2:
    col=defaultdict(int)
    for pos,v in enumerate(vs):
        rv=vs[1-pos]; ra=aa[1-pos]
        ep,em=alpha[v][aa[pos]]; s=1 if pos==0 else -1
        col[c1_index[(rv,ra,tuple(sorted((e,ep))))]] += s
        col[c1_index[(rv,ra,tuple(sorted((e,em))))]] -= s
    d2.append({r:c for r,c in col.items() if c})
for col in d3:
    out=defaultdict(int)
    for r,c in col.items():
        for q,a in d2[r].items(): out[q]+=c*a
    assert not {q:a for q,a in out.items() if a}

def rank_mod(cols,p):
    basis={}
    for col0 in cols:
        v={r:c%p for r,c in col0.items() if c%p}
        while v:
            r=min(v)
            if r not in basis:
                inv=pow(v[r],-1,p)
                v={q:(a*inv)%p for q,a in v.items() if (a*inv)%p}
                basis[r]=v
                break
            b=basis[r]; fac=v[r]
            for q,a in b.items():
                z=(v.get(q,0)-fac*a)%p
                if z: v[q]=z
                elif q in v: del v[q]
    return len(basis)

cert=json.loads(Path(__file__).with_name('kernel_basis.json').read_text(encoding='utf-8'))
vecs=cert['vectors']
assert len(vecs)==7
leading=[]
for entries in vecs:
    coeff={int(j):int(c) for j,c in entries}
    assert coeff
    out=defaultdict(int)
    for j,c in coeff.items():
        for r,a in d3[j].items(): out[r]+=c*a
    assert not {r:a for r,a in out.items() if a}
    leading.append(max(coeff))
assert leading==sorted(leading) and len(set(leading))==7
# Each vector has zero coefficients above its own leading index, so distinct
# increasing leading indices give triangular linear independence.
ranks={p:rank_mod(d3,p) for p in (2,3,5)}
assert ranks[3]==6521 and ranks[5]==6521 and ranks[2]==6515
assert 6528-7==6521
print('PAPPUS_B3_TOP_HOMOLOGY_VERIFY_OK')
print('chain_ranks',{'C3':len(c3),'C2':len(c2),'C1':len(c1_index)})
print('d3_ranks_mod',ranks)
print('kernel_vector_supports',[len(v) for v in vecs])
print('kernel_leading_columns',leading)
print('conclusion','H_3(B_3(P);Z) = Z^7')
