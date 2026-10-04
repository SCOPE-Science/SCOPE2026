#!/usr/bin/env python3
from pathlib import Path
from itertools import product
from math import gcd
import json

ROOT=Path(__file__).resolve().parent.parent
C=json.loads((ROOT/"artifacts"/"certificate.json").read_text(encoding="utf-8"))
p=C["prime"]; M=C["modulus"]; n=C["length"]

def pmul(a,b,mod):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]=(out[i+j]+x*y)%mod
    return out

def pdivmod(a,b,mod):
    a=[x%mod for x in a]
    b=[x%mod for x in b]
    while len(a)>1 and a[-1]==0: a.pop()
    while len(b)>1 and b[-1]==0: b.pop()
    inv=pow(b[-1],-1,mod)
    q=[0]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and any(a):
        d=len(a)-len(b)
        c=a[-1]*inv%mod
        q[d]=c
        for j in range(len(b)):
            a[d+j]=(a[d+j]-c*b[j])%mod
        while len(a)>1 and a[-1]==0: a.pop()
    return q,a

def reduce_quot(poly,mod,sign):
    a=[x%mod for x in poly]
    if len(a)<n: a += [0]*(n-len(a))
    for d in range(len(a)-1,n-1,-1):
        c=a[d]%mod
        if c:
            a[d-n]=(a[d-n]+sign*c)%mod
    return a[:n]

def mulmat(poly,mod,sign):
    cols=[]
    for j in range(n):
        cols.append(reduce_quot([0]*j+poly,mod,sign))
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def rank_fp(A,p):
    if not A or not A[0]: return 0
    A=[[x%p for x in row] for row in A]
    r=0
    for c in range(len(A[0])):
        q=next((i for i in range(r,len(A)) if A[i][c]),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(inv*x)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(A[i][j]-z*A[r][j])%p for j in range(len(A[0]))]
        r+=1
        if r==len(A): break
    return r

def image_exp_p2(A,p):
    mod=p*p
    A=[[x%mod for x in row] for row in A]
    rows=len(A); cols=len(A[0]); r=0
    for c in range(cols):
        q=next((i for i in range(r,rows) if A[i][c]%p),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,mod)
        A[r]=[(inv*x)%mod for x in A[r]]
        for i in range(rows):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(A[i][j]-z*A[r][j])%mod for j in range(cols)]
        r+=1
        if r==rows: break
    # The remaining lower-right block is divisible by p.
    # Pivot columns remove the upper-right block by invertible column operations.
    B=[[(A[i][j]//p)%p for j in range(r,cols)] for i in range(r,rows)]
    s=rank_fp(B,p)
    return r,s,2*r+s

f0=C["printed_components_low_to_high"]["cyclic"]
g0=C["printed_components_low_to_high"]["negacyclic"]
fh=C["corrected_components_low_to_high"]["cyclic"]
gh=C["corrected_components_low_to_high"]["negacyclic"]
xm1=[-1]+[0]*6+[1]
xp1=[1]+[0]*6+[1]

assert pdivmod(xm1,f0,M)[1] == C["printed_remainders_low_to_high"]["x7_minus_1_mod_cyclic"]
assert pdivmod(xp1,g0,M)[1] == C["printed_remainders_low_to_high"]["x7_plus_1_mod_negacyclic"]
assert pdivmod(xm1,fh,M)[1] == [0]
assert pdivmod(xp1,gh,M)[1] == [0]
assert pdivmod(xm1,fh,M)[0] == C["corrected_cofactors_low_to_high"]["cyclic"]
assert pdivmod(xp1,gh,M)[0] == C["corrected_cofactors_low_to_high"]["negacyclic"]
assert [x%p for x in fh] == [x%p for x in f0]
assert [x%p for x in gh] == [x%p for x in g0]

for poly,sign,key in [
    (f0,1,"cyclic"),(g0,-1,"negacyclic")
]:
    r,s,e=image_exp_p2(mulmat(poly,M,sign),p)
    assert e == C["printed_ideal_cardinality_exponents_base_13"][key]
assert sum(C["printed_ideal_cardinality_exponents_base_13"][k] for k in ("cyclic","negacyclic")) == C["printed_ideal_cardinality_exponents_base_13"]["direct_sum"]

for poly,sign in [(fh,1),(gh,-1)]:
    r,s,e=image_exp_p2(mulmat(poly,M,sign),p)
    assert e == C["corrected_component_cardinality_exponent_base_13"]

def shift(v,mod,sign):
    return [(sign*v[-1])%mod]+v[:-1]

def component_rows(poly,mod,sign):
    r0=reduce_quot(poly,mod,sign)
    return [r0,shift(r0,mod,sign)]

def enumerate_component(poly,mod,sign):
    rows=component_rows(poly,mod,sign)
    dist={}
    d=n+1
    for a,b in product(range(mod),repeat=2):
        w=[(a*rows[0][j]+b*rows[1][j])%mod for j in range(n)]
        wt=sum(x!=0 for x in w)
        dist[wt]=dist.get(wt,0)+1
        if a or b:
            d=min(d,wt)
    gram=[[sum(rows[i][k]*rows[j][k] for k in range(n))%mod for j in range(2)] for i in range(2)]
    det=(gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0])%mod
    return rows,d,dist,gram,det

for key,poly,sign in [("cyclic",fh,1),("negacyclic",gh,-1)]:
    rows,d,dist,gram,det=enumerate_component(poly,M,sign)
    expected={int(k):v for k,v in C["corrected_component_weight_distributions"][key].items()}
    assert d==6
    assert dist==expected
    assert gram==C["corrected_component_gram_matrices"][key]
    assert det==C["corrected_component_gram_determinants_mod_169"][key]
    assert gcd(det,M)==1

# Baseline: the printed polynomials are valid over F_13.
assert pdivmod([x%p for x in xm1],[x%p for x in f0],p)[1]==[0]
assert pdivmod([x%p for x in xp1],[x%p for x in g0],p)[1]==[0]
for poly,sign in [(f0,1),(g0,-1)]:
    rows,d,dist,gram,det=enumerate_component(poly,p,sign)
    assert d==6
    assert dist=={int(k):v for k,v in C["residue_field_check"]["component_weight_distribution"].items()}
    assert gcd(det,p)==1

print("VERIFY_OK")
