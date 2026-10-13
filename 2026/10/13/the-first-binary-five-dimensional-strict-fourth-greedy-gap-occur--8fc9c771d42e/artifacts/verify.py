#!/usr/bin/env python3
import itertools, collections, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
CERT=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))

# Nonzero vectors of F_2^5 represent the 31 projective points.
PTS=list(range(1,32))
e1,e2,e3,e4,e5=1,2,4,8,16

mult={p:0 for p in PTS}
mult[e1]=3
mult[e2]=2
mult[e3]=2
mult[e2^e3]=2
mult[e4]=1
mult[e5]=1
assert sum(mult.values())==11

# Build generator columns and row bitmasks.
cols=[]
for p in PTS:
    cols.extend([p]*mult[p])
rows=[]
for i in range(5):
    z=0
    for j,p in enumerate(cols):
        if (p>>i)&1:
            z|=1<<j
    rows.append(z)

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

assert rank_bits(rows)==5

# Projective lines in PG(4,2) are {a,b,a+b}.
lines=set()
for a,b in itertools.combinations(PTS,2):
    lines.add(tuple(sorted((a,b,a^b))))
assert len(lines)==155

line_mass={ell:sum(mult[p] for p in ell) for ell in lines}
M=max(mult.values())
L=max(line_mass.values())
max_lines=[ell for ell,w in line_mass.items() if w==L]
B=max(mult[p] for ell in max_lines for p in ell)

assert M==CERT["witness"]["M"]==3
assert L==CERT["witness"]["L"]==6
assert B==CERT["witness"]["B"]==2
assert max_lines==[(e2,e3,e2^e3)]
assert 11-M==CERT["witness"]["d4"]==8
assert 11-B==CERT["witness"]["g4"]==9

# Message words.
words=[]
for u in range(32):
    z=0
    for i in range(5):
        if (u>>i)&1:
            z^=rows[i]
    words.append(z)

wd=collections.Counter(w.bit_count() for w in words)
CERT["witness"]["ordinary_weight_distribution"]={str(k):v for k,v in sorted(wd.items())}

def subspaces_rref(n,d):
    for piv in itertools.combinations(range(n),d):
        P=set(piv)
        free=[(i,c) for i,p in enumerate(piv)
              for c in range(p+1,n) if c not in P]
        for vals in itertools.product((0,1),repeat=len(free)):
            B0=[1<<p for p in piv]
            for (i,c),v in zip(free,vals):
                if v:
                    B0[i]|=1<<c
            yield B0

def span_set(B):
    S={0}
    for u in B:
        S |= {x^u for x in tuple(S)}
    return S

gh=[]
min_subspaces={}
histograms={}
for r in range(1,6):
    ctr=collections.Counter()
    best=99
    mins=[]
    for B0 in subspaces_rref(5,r):
        support=0
        for u in B0:
            support|=words[u]
        w=support.bit_count()
        ctr[w]+=1
        if w<best:
            best=w
            mins=[B0]
        elif w==best:
            mins.append(B0)
    gh.append(best)
    min_subspaces[r]=mins
    histograms[r]=dict(sorted(ctr.items()))

assert gh==CERT["witness"]["generalized_hamming_weights"]==[1,2,5,8,11]

# Direct CEZ g4: four-subcodes containing a three-subcode attaining d3.
d3=gh[2]
eligible=[]
for B3 in min_subspaces[3]:
    S3=span_set(B3)
    for B4 in subspaces_rref(5,4):
        if S3 <= span_set(B4):
            support=0
            for u in B4:
                support|=words[u]
            eligible.append(support.bit_count())

assert eligible
assert min(eligible)==9
assert len(min_subspaces[3])==1

# Check the lower-bound integer bottleneck used in the proof:
# 2b >= M+1, b <= M-1, M >= 1 => M>=3,
# and n >= 2M+b+3 has minimum 11.
feasible=[]
for Mm in range(1,20):
    for b in range(0,Mm):
        if 2*b >= Mm+1:
            feasible.append((2*Mm+b+3,Mm,b))
assert min(feasible)==(11,3,2)

print("VERIFY_OK")
