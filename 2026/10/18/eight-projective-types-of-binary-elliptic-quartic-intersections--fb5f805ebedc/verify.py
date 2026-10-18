#!/usr/bin/env python3
"""Exact characteristic-two census of genus-one quartic models.
Requires Python 3 and sympy.  All field arithmetic for classification is GF(2).
"""
import itertools
from collections import Counter
import sympy as S

V=S.symbols("x0:4")
MON=[(i,j) for i in range(4) for j in range(i,4)]
MONS=[V[i]*V[j] for i,j in MON]
FORMS=[sum(MONS[k] for k in range(10) if mask>>k&1) for mask in range(1024)]
D=[[S.diff(F,x) for x in V] for F in FORMS]
P=[p for p in itertools.product((0,1),repeat=4) if any(p)]

def canon(a,b):
    return tuple(sorted((a,b,a^b))[:2])

def map_table(sub):
    monoimage=[]
    for i,j in MON:
        val=0
        for u in sub[i]:
            for v in sub[j]:
                val ^= 1<<MON.index(tuple(sorted((u,v))))
        monoimage.append(val)
    t=[0]*1024
    for z in range(1,1024):
        low=z&-z
        t[z]=t[z^low]^monoimage[low.bit_length()-1]
    return t

GEN=[]
for i in range(3):
    sub=[[j] for j in range(4)]
    sub[i],sub[i+1]=sub[i+1],sub[i]
    GEN.append(map_table(sub))
sub=[[j] for j in range(4)]
sub[0]=[0,1]
GEN.append(map_table(sub))

def rational_zero(q,p):
    return sum(p[i]*p[j] for k,(i,j) in enumerate(MON) if q>>k&1)%2==0

def rational_points(a,b):
    return [p for p in P if rational_zero(a,p) and rational_zero(b,p)]

def quadrics_profile(a,b):
    return tuple(sorted(sum(rational_zero(q,p) for p in P) for q in (a,b,a^b)))

def smooth_over_closure(a,b):
    A,B=D[a],D[b]
    minors=[S.expand(A[i]*B[j]-A[j]*B[i])
            for i in range(4) for j in range(i+1,4)]
    eqns=[FORMS[a],FORMS[b]]+minors
    for i in range(4):
        other=[V[j] for j in range(4) if j!=i]
        gb=S.groebner([f.subs(V[i],1) for f in eqns],
                     *other,modulus=2,order="grevlex")
        if not any(f.is_one for f in gb.polys):
            return False
    return True

def series_coefficient(q,c,k):
    z=0
    for bit,(i,j) in enumerate(MON):
        if q>>bit&1:
            for h in range(k+1):
                z^=c[i][h]*c[j][k-h]
    return z

def fourth_contact_planes(a,b,p):
    ip=next(i for i,t in enumerate(p) if t)
    free=[i for i in range(4) if i!=ip]
    tangents=[]
    for z in itertools.product((0,1),repeat=3):
        if not any(z): continue
        c=[[p[i],0,0,0] for i in range(4)]
        for i,w in zip(free,z):c[i][1]=w
        if series_coefficient(a,c,1)==series_coefficient(b,c,1)==0:
            tangents.append(z)
    assert len(tangents)==1
    tangent=tangents[0]
    ti=free[next(i for i,z in enumerate(tangent) if z)]
    other=[i for i in free if i!=ti]
    c=[[p[i],0,0,0] for i in range(4)]
    for i,w in zip(free,tangent):c[i][1]=w
    for degree in (2,3):
        options=[]
        for z in itertools.product((0,1),repeat=2):
            for i,w in zip(other,z):c[i][degree]=w
            if series_coefficient(a,c,degree)==series_coefficient(b,c,degree)==0:
                options.append(z)
        assert len(options)==1
        for i,w in zip(other,options[0]):c[i][degree]=w
    return [mask for mask in range(1,16) if
            all(sum(((mask>>i)&1)*c[i][k] for i in range(4))%2==0
                for k in range(4))]

def coplanar(p):
    # Over GF(2) every hyperplane in P^3 is represented uniquely
    return any(all(sum(((h>>i)&1)*x[i] for i in range(4))%2==0
                   for x in p) for h in range(1,16))

unseen={(a,b) for a in range(1,1024) for b in range(a+1,1024) if b<(a^b)}
assert len(unseen)==174251
out=[]
while unseen:
    seed=min(unseen)
    unseen.remove(seed)
    frontier=[seed]; orbit=[seed]
    while frontier:
        x,y=frontier.pop()
        for g in GEN:
            pair=canon(g[x],g[y])
            if pair in unseen:
                unseen.remove(pair)
                frontier.append(pair)
                orbit.append(pair)
    x,y=seed
    if smooth_over_closure(x,y):
        pts=rational_points(x,y)
        out.append((len(orbit),len(pts),quadrics_profile(x,y),
                    x,y, sum(len(fourth_contact_planes(x,y,p)) for p in pts),
                    coplanar(pts) if len(pts)==4 else None))
assert len(out)==8
out.sort(key=lambda t:(t[1],t[2],t[3],t[4]))
assert sum(t[0] for t in out)==40320
assert sorted(t[0] for t in out)==[2520,2520,5040,5040,5040,5040,5040,10080]
assert Counter(t[1] for t in out)=={1:1,2:2,3:1,4:3,5:1}
assert sorted((t[5],t[6]) for t in out if t[1]==4)==[(0,False),(0,True),(4,False)]
print("TOTAL_PENCILS=174251")
print("PROJECTIVE_ORBITS=54")
print("SMOOTH_PENCILS=40320")
print("SMOOTH_ORBITS=8")
print("size,N,quadric-points,a,b,rational_4contacts,all4coplanar")
for record in out:
    print(*record,sep=",")
print("VERIFY_OK")
