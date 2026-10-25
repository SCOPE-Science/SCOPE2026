#!/usr/bin/env python3
"""Exact verification of the rational symmetry-homology claim.

Requires Python 3.9+ standard library only. Run from the directory containing
kernel_certificate.json. All matrices, signs and actions are reconstructed.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations
import json
from pathlib import Path

cert = json.loads(Path(__file__).with_name('kernel_certificate.json').read_text(encoding='utf-8'))
assert cert['schema_version'] == 1
labels = list(combinations(range(5), 2))
edges = [(i,j) for i in range(10) for j in range(i+1,10)
         if set(labels[i]).isdisjoint(labels[j])]
assert len(edges) == 15
faces = {}
for k in range(5):
    faces[k] = [face for face in combinations(range(15),k+1)
                if all(set(edges[a]).isdisjoint(edges[b])
                       for a,b in combinations(face,2))]
assert tuple(len(faces[k]) for k in range(5)) == (15,75,145,90,6)
index = {k:{f:i for i,f in enumerate(faces[k])} for k in faces}

def make_boundary(k):
    return [{index[k-1][face[:j]+face[j+1:]]:(-1)**j
             for j in range(k+1)} for face in faces[k]]

boundary = {k:make_boundary(k) for k in range(1,5)}

def rank_mod_two(cols, nrows):
    rows = [0]*nrows
    for j,col in enumerate(cols):
        for i,c in col.items():
            if c & 1: rows[i] ^= (1<<j)
    pivots = {}
    for v in rows:
        while v:
            bit = v.bit_length()-1
            if bit not in pivots:
                pivots[bit]=v
                break
            v ^= pivots[bit]
    return len(pivots)

ranks = tuple(rank_mod_two(boundary[k],len(faces[k-1])) for k in range(1,5))
assert ranks == (14,61,79,6), ranks
for k in (2,3,4):
    for upper in boundary[k]:
        out = Counter()
        for middle,coef in upper.items():
            for low,bcoef in boundary[k-1][middle].items():
                out[low] += coef*bcoef
        assert all(v==0 for v in out.values())

# Explicit exact integer kernel columns, with a left coordinate inverse on
# selected face rows. Their existence forces rank_Q(boundary_3) <= 79,
# while the mod-two rank 79 gives the converse inequality.
K = []
for sparse in cert['basis_vectors']:
    z = [0]*len(faces[3]); touched=set()
    for i,value in sparse:
        assert 0<=i<len(z) and i not in touched and isinstance(value,int)
        touched.add(i);z[i]=value
    K.append(z)
assert len(K)==11
for z in K:
    dz = Counter()
    for a,c in enumerate(z):
        if c:
            for i,b in boundary[3][a].items():dz[i]+=c*b
    assert all(v==0 for v in dz.values())
rows=cert['coordinate_rows'];inverse=cert['coordinate_inverse']
assert len(rows)==len(set(rows))==11 and all(0<=i<90 for i in rows)
assert len(inverse)==11 and all(len(row)==11 for row in inverse)
R=[[K[j][i] for j in range(11)] for i in rows]
for a in range(11):
    for b in range(11):
        assert sum(inverse[a][i]*R[i][b] for i in range(11)) == int(a==b)
        assert sum(R[a][i]*inverse[i][b] for i in range(11)) == int(a==b)

def coordinates(z):
    return [sum(inverse[j][i]*z[rows[i]] for i in range(11))
            for j in range(11)]

def rebuild(coeff):
    return [sum(coeff[j]*K[j][i] for j in range(11)) for i in range(90)]

# boundary_4 is an injected six-dimensional invariant subspace of ker d_3.
for col in boundary[4]:
    z=[0]*90
    for i,v in col.items(): z[i]=v
    coord=coordinates(z)
    assert rebuild(coord)==z
    assert coord[6:]==[0]*5

# Ranks over Q are therefore (14,61,79,6). In particular the only
# nonzero reduced rational homology has dimensions 5 in degrees 2 and 3.
assert len(faces[1])-14-61==0
assert len(faces[2])-61-79==5
assert len(faces[3])-79-6==5

def sign_of_sequence(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values))
                     for j in range(i+1,len(values)))&1 else 1

def induced_edge_perm(p):
    vp=[labels.index(tuple(sorted(p[i] for i in v))) for v in labels]
    return [edges.index(tuple(sorted((vp[u],vp[v])))) for u,v in edges]

def act_chain(k,z,eperm):
    out=[0]*len(faces[k])
    for a,c in enumerate(z):
        if c:
            transformed=[eperm[i] for i in faces[k][a]]
            out[index[k][tuple(sorted(transformed))]]+=sign_of_sequence(transformed)*c
    return out

def trace_chains(k,eperm):
    tr=0
    for f in faces[k]:
        im=[eperm[i] for i in f]
        if set(im)==set(f):tr+=sign_of_sequence(im)
    return tr

def cycle_type(p):
    seen=set();sizes=[]
    for i in range(5):
        if i in seen:continue
        j=i;n=0
        while j not in seen:
            seen.add(j);j=p[j];n+=1
        sizes.append(n)
    return tuple(sorted(sizes,reverse=True))

classes={};sum_all=[0,0];sum_even=[0,0];even_count=0
for p in permutations(range(5)):
    eperm=induced_edge_perm(p)
    traceK=0
    for j,z in enumerate(K):
        gz=act_chain(3,z,eperm)
        coeff=coordinates(gz)
        assert rebuild(coeff)==gz
        traceK+=coeff[j]
    traces=[trace_chains(k,eperm) for k in range(5)]
    h3=traceK-traces[4]
    h2=sum((-1)**k*traces[k] for k in range(5))-1+h3
    f=sum(p[i]==i for i in range(5))
    fixed_pairs=sum({p[i],p[j]}=={i,j} for i,j in combinations(range(5),2))
    assert h2==sign_of_sequence(p)*f
    assert h3==fixed_pairs-f
    cl=cycle_type(p)
    if cl in classes:assert classes[cl]==(h2,h3)
    classes[cl]=(h2,h3)
    sum_all[0]+=h2;sum_all[1]+=h3
    if sign_of_sequence(p)==1:
        sum_even[0]+=h2;sum_even[1]+=h3;even_count+=1

assert len(classes)==7 and sum_all==[0,0]
assert even_count==60 and sum_even==[60,0]
expected={
 (1,1,1,1,1):(5,5), (2,1,1,1):(-3,1),
 (2,2,1):(1,1), (3,1,1):(2,-1), (3,2):(0,1),
 (4,1):(-1,-1), (5,):(0,0)}
assert classes==expected
print('EXACT_BOUNDARY_RANKS_VERIFIED',ranks)
print('UNIMODULAR_KERNEL_CERTIFICATE_VERIFIED',len(K))
print('ALL_S5_CHARACTERS_VERIFIED',120)
print('FULL_S5_HOMOLOGY_REPRESENTATIONS_VERIFIED')
