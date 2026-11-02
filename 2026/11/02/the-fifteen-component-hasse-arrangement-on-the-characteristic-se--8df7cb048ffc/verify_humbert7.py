#!/usr/bin/env python3
"""Exact finite combinatorics of five branch points in characteristic seven."""
from itertools import permutations
from collections import Counter
P=7
S={2,4,6}
T={2,3,4,5,6}

def inv(x):
    if x%P==0: raise ZeroDivisionError
    return pow(x,-1,P)

def cr(u,v):
    return (u,v,(v*inv(u))%P,((v-1)*inv(u-1))%P,
            (u*(v-1)*inv(v)*inv(u-1))%P)

def ss(u,v):
    return tuple(i for i,t in enumerate(cr(u,v)) if t in S)

# The cubic is the standard Deuring polynomial sum_{j=0}^3 binom(3,j)^2 t^j.
from math import comb
coeff=[(comb(3,j)**2)%P for j in range(4)]
assert coeff==[1,2,2,1]
assert {x for x in range(P) if sum(coeff[j]*pow(x,j,P) for j in range(4))%P==0}==S

# Every rational point in M0,5(F7) has three supersingular elliptic factors.
pts={(u,v) for u in T for v in T if u!=v}
assert len(pts)==20
assert {len(ss(u,v)) for u,v in pts}=={3}
assert len({tuple(sorted(ss(u,v))) for u,v in pts})==10
assert Counter(i for u,v in pts for i in ss(u,v))==Counter({i:12 for i in range(5)})

# For every pair of omitted labels the intersection has six reduced points.
for i in range(5):
    for j in range(i+1,5):
        pair={(u,v) for u,v in pts if i in ss(u,v) and j in ss(u,v)}
        assert len(pair)==6,(i,j,pair)

# All twenty points are in a single S5-orbit. Determinants avoid infinity divisions.
def vec(x): return (1,0) if x is None else (x,1)
def det(x,y):
    a,b=vec(x),vec(y)
    return (a[0]*b[1]-a[1]*b[0])%P

def mob(a,b,c,x):
    if x==a:return None
    return (det(x,b)*det(c,a)*inv(det(x,a)*det(c,b)))%P

B=(None,0,1,2,4)
orbit=set()
for a,b,c,u,v in permutations(B):
    orbit.add((mob(a,b,c,u),mob(a,b,c,v)))
assert orbit==pts
assert len(orbit)==20
assert 120//len(orbit)==6

# Hasse curve components indexed by omitted point i and harmonic root s.
# Count membership in the 15 components by f_i(u,v)=s.
components={(i,s) for i in range(5) for s in S}
assert len(components)==15
for i,s in components:
    locations={(u,v) for u,v in pts if cr(u,v)[i]==s}
    assert len(locations)==4,(i,s,locations)
for u,v in pts:
    assert len([k for k in components if cr(u,v)[k[0]]==k[1]])==3

# Three local tangent directions are distinct at one orbit representative:
# the three zero factors are u-2, v-4, v-2u, with gradients
# (1,0),(0,1),(-2,1). All 2x2 determinants nonzero mod seven.
normals=[(1,0),(0,1),(-2,1)]
for a,b in zip(normals,normals[1:]+normals[:1]):
    assert (a[0]*b[1]-a[1]*b[0])%P

# These F7 tests accompany (do NOT replace) the proof using S5 and
# the fact that any two Hasse divisors are conjugate to u,v in S.
print('VERIFY_OK: Deuring cubic (t-2)(t-4)(t-6), 20 F7 points with three vanishing factors')
print('PAIR_OK: all ten pairwise Hasse intersections have six distinct F7 points')
print('ORBIT_OK: one S5 orbit of 20, stabilizer size six, 15_4 / 20_3 incidence')
print('LOCAL_OK: three reduced transverse local factors at representative (2,4)')
