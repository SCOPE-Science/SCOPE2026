#!/usr/bin/env python3
"""Standalone verification for independent truncations of a tetrahedron.

This is a finite-exhaustion and numerical cross-check, not a substitute for
analytic arguments concerning all tetrahedra and all real truncation depths.
Python standard library only. Run: python tetra_truncation_verify.py
"""
from fractions import Fraction as F
from itertools import combinations,product
from collections import Counter
import math, random

I=range(4)
IDX=tuple((i,j) for i in I for j in I if i!=j)
LOC={a:k for k,a in enumerate(IDX)}
EDGES=[]
for i in I:
    for j,k in combinations([a for a in I if a!=i],2):
        EDGES.append((LOC[i,j],LOC[i,k]))
for i,j in combinations(I,2):
    EDGES.append((LOC[i,j],LOC[j,i]))
assert len(IDX)==12 and len(EDGES)==18

# Exhaust every nontrivial vertex sign cut in the 12-vertex, 18-edge graph.
three=[]
for mask in range(1,(1<<12)-1):
    edge_count=sum(((mask>>a)&1)!=((mask>>b)&1) for a,b in EDGES)
    if edge_count==3:
        selected={IDX[a] for a in range(12) if mask>>a&1}
        three.append(selected)
        assert len(selected) in (1,3,9,11)
        if len(selected)==3:
            assert any(selected=={(i,j) for j in I if j!=i} for i in I)
        if len(selected)==9:
            assert any({z for z in IDX if z not in selected}==
                       {(i,j) for j in I if j!=i} for i in I)
assert len(three)==32
assert Counter(map(len,three))=={1:12,3:4,9:4,11:12}

V=((F(1),F(1),F(1)),(F(1),F(-1),F(-1)),
   (F(-1),F(1),F(-1)),(F(-1),F(-1),F(1)))
assert all(sum(v[k] for v in V)==0 for k in range(3))

def dot(x,y):return sum(a*b for a,b in zip(x,y))
def add(x,y):return tuple(a+b for a,b in zip(x,y))
def scale(a,x):return tuple(a*v for v in x)

def truncated(v,t):
    return {ij:add(scale(1-t[ij[0]],v[ij[0]]),
                   scale(t[ij[0]],v[ij[1]])) for ij in IDX}

def n_section(p,u):
    ht=[dot(u,p[ij]) for ij in IDX]
    if any(z==0 for z in ht):return None
    return sum((ht[a]>0)!=(ht[b]>0) for a,b in EDGES)

def predicting_triangle(v,t,u):
    # The cone conditions, not graph sign-cut enumeration.
    a=[dot(u,w) for w in v]
    for sign in (1,-1):
        for i in I:
            if sign*a[i]<=0 or any(sign*a[j]>=0 for j in I if j!=i):continue
            if all(-sign*a[j]*(1-t[j])>sign*a[i]*t[j] for j in I if j!=i):
                return True
    return False

# Exact signs on integer normal directions, with distinct rational truncations.
rng=random.Random(24681357)
matrices=[
    ((F(1),F(0),F(0)),(F(0),F(1),F(0)),(F(0),F(0),F(1))),
    ((F(2),F(1),F(0)),(F(0),F(3,2),F(1,3)),(F(0),F(0),F(2,3))),
]
depths=[(F(1,10),F(1,10),F(1,10),F(1,10)),
        (F(6,25),)*4,
        (F(13,50),)*4,
        (F(1,10),F(9,50),F(27,100),F(2,5)),
        (F(9,20),F(9,20),F(1,10),F(1,10)),
        (F(2,5),F(1,10),F(1,10),F(1,10))]
verified=0
for A in matrices:
    w=[tuple(sum(A[k][j]*v[j] for j in range(3)) for k in range(3)) for v in V]
    for t in depths:
        p=truncated(w,t)
        for _ in range(1200):
            u=tuple(F(rng.randrange(-50,51)) for _ in range(3))
            n=n_section(p,u)
            if n is None:continue
            assert (n==3)==predicting_triangle(w,t,u), (A,t,u,n)
            verified+=1
assert verified>=10000

def omega_and_prob(v,t):
    om=[]
    for i in I:
        jj=[j for j in I if j!=i]
        if sum(float(t[j]/(1-t[j])) for j in jj)>=1:
            om.append(0.0);continue
        normals=[add(scale(1-t[j],v[j]),scale(t[j],v[i])) for j in jj]
        val=2*math.pi
        for a,b in combinations(normals,2):
            val-=math.acos(max(-1,min(1,float(dot(a,b))/math.sqrt(float(dot(a,a)*dot(b,b))))))
        om.append(val)
    return om,sum(om)/(2*math.pi)

# Check analytic spherical solid angles against independent MC directions.
# Confidence bound is intentionally generous: MC is supplementary, not a proof.
num=150000
for t in (depths[0],depths[1],depths[2],depths[3],depths[5]):
    p=truncated(V,t)
    om,prob=omega_and_prob(V,t)
    hit=0;tot=0
    for _ in range(num):
        u=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
        vv={ij:tuple(float(x) for x in p[ij]) for ij in IDX}
        ht=[sum(u[k]*vv[ij][k] for k in range(3)) for ij in IDX]
        n=sum((ht[a]>0)!=(ht[b]>0) for a,b in EDGES)
        hit+=(n==3)
        tot+=1
    freq=hit/tot
    bound=6*math.sqrt(max(prob*(1-prob),1/tot)/tot)+0.001
    assert abs(freq-prob)<bound,(t,prob,freq,bound)
    print('NUMERICAL', [float(x) for x in t],f'formula={prob:.9f}',
          f'frequency={freq:.9f}',f'bound={bound:.9f}')

for t in (0,0.1,0.2,0.24,0.249):
    c=(4*t*t-1)/(3-8*t+8*t*t)
    p=2*(2*math.pi-3*math.acos(c))/math.pi
    _,general=omega_and_prob(V,tuple(F(str(t)) for _ in I))
    assert abs(p-general)<1e-10
assert omega_and_prob(V,(F(1,4),)*4)[1]==0
assert omega_and_prob(V,(F(2,5),)*4)[1]==0
print('EXACT_GRAPH_CUTS_OK',len(three),'EXACT_RATIONAL_NORMALS_OK',verified)
print('SPHERICAL_SOLID_ANGLE_FORMULAS_OK')
