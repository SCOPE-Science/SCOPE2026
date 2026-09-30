#!/usr/bin/env python3
import itertools, json

V=tuple(range(6))
TRIPLES=list(itertools.combinations(V,3))
TINDEX={t:i for i,t in enumerate(TRIPLES)}

def det_bareiss(M):
    A=[row[:] for row in M]
    n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]!=0),None)
            if j is None: return 0
            A[k],A[j]=A[j],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        prev=piv
        for i in range(k+1,n): A[i][k]=0
    return sign*A[n-1][n-1]

def graph_relation(mask):
    # relation of lambda_max(A) to 2: -1,0,+1
    edges=list(itertools.combinations(range(5),2))
    A=[[0]*5 for _ in range(5)]
    for b,(i,j) in enumerate(edges):
        if mask>>b & 1: A[i][j]=A[j][i]=1
    B=[[2*(i==j)-A[i][j] for j in range(5)] for i in range(5)]
    all_nonneg=True; all_pos=True
    for s in range(1,1<<5):
        idx=[i for i in range(5) if s>>i & 1]
        d=det_bareiss([[B[i][j] for j in idx] for i in idx])
        if d<0: all_nonneg=False
        if d<=0: all_pos=False
    if all_pos: return -1
    if all_nonneg: return 0
    return 1
REL=[graph_relation(m) for m in range(1<<10)]

PAIRS=[]; seen=set()
for t in TRIPLES:
    if t in seen: continue
    c=tuple(sorted(set(V)-set(t)))
    PAIRS.append((t,c)); seen.add(t); seen.add(c)

# local edge bit for each triple and incident vertex
LOCAL={}
for t in TRIPLES:
    for v in t:
        others=[x for x in V if x!=v]
        pos={x:i for i,x in enumerate(others)}
        a,b=[x for x in t if x!=v]
        e=tuple(sorted((pos[a],pos[b])))
        bit=list(itertools.combinations(range(5),2)).index(e)
        LOCAL[(TINDEX[t],v)]=1<<bit

def family_link_masks(edge_indices):
    lm=[0]*6
    for ei in edge_indices:
        t=TRIPLES[ei]
        for v in t: lm[v] |= LOCAL[(ei,v)]
    return lm

def canon(edge_indices):
    emasks=[sum(1<<x for x in TRIPLES[i]) for i in edge_indices]
    best=None
    for p in itertools.permutations(V):
        out=[]
        for m in emasks:
            nm=0
            for i in V:
                if m>>i & 1: nm |= 1<<p[i]
            out.append(nm)
        key=tuple(sorted(out))
        if best is None or key<best: best=key
    return best

def key_to_edges(key):
    out=[]
    for m in key:
        out.append(''.join(str(i) for i in V if m>>i&1))
    return out

def degrees(edge_indices):
    return sorted(sum(v in TRIPLES[i] for i in edge_indices) for v in V)

count=0; equality=[]; worst=-2
for choices in itertools.product((0,1,2), repeat=10):
    E=[]
    for c,(a,b) in zip(choices,PAIRS):
        if c==1: E.append(TINDEX[a])
        elif c==2: E.append(TINDEX[b])
    rels=[REL[m] for m in family_link_masks(E)]
    s=min(rels)
    if s>worst: worst=s
    if s==0: equality.append(tuple(E))
    count+=1

classes={}
for E in equality:
    k=canon(E)
    classes.setdefault(k,[]).append(E)
rows=[]
for k, fams in classes.items():
    E=fams[0]
    rows.append({
        'representative':key_to_edges(k),
        'edge_count':len(E),
        'degree_sequence':degrees(E),
        'labeled_orbit_count':len(fams),
        'automorphism_order':720//len(fams),
    })
rows.sort(key=lambda r:(r['edge_count'],r['degree_sequence'],r['representative']))
summary={
    'enumeration':'3^10 complementary-pair choices',
    'intersecting_families_checked':count,
    'max_sigma_value':2,
    'no_family_has_sigma_gt_2':worst<=0,
    'equality_labeled_count':len(equality),
    'equality_isomorphism_types':len(rows),
    'classes':rows,
}
assert count==59049
assert worst==0
assert len(equality)==78
assert len(rows)==5
assert sorted(r['labeled_orbit_count'] for r in rows)==[6,12,20,20,20]
print(json.dumps(summary,sort_keys=True,separators=(',',':')))
