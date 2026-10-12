#!/usr/bin/env python3
from itertools import combinations
from collections import Counter

MOD = 6
I = ((1,0),(0,1))
R = ((0,-1),(1,-1))  # multiplication by a primitive cube root in a Z[ζ]-basis

def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % MOD for j in range(2)) for i in range(2))

def mv(A,v):
    return ((A[0][0]*v[0]+A[0][1]*v[1])%MOD,
            (A[1][0]*v[0]+A[1][1]*v[1])%MOD)

def add(*vs):
    return (sum(v[0] for v in vs)%MOD, sum(v[1] for v in vs)%MOD)

# E[6] ≅ (Z/6)^2; E[3] is the subgroup of even vectors.
E6=[(a,b) for a in range(6) for b in range(6)]
E3=[(a,b) for a,b in E6 if a%2==0 and b%2==0]
S=[v for v in E6 if v not in E3]  # E[6] \ E[3]
assert len(E6)==36 and len(E3)==9 and len(S)==27

# Collinearity on a plane cubic with flex origin: P,Q,R are collinear iff P+Q+R=0.
lines={frozenset(c) for c in combinations(S,3) if add(*c)==(0,0)}
assert len(lines)==81
assert Counter(sum(v in L for L in lines) for v in S)==Counter({9:27})

# Full projective automorphism group E[3] ⋊ μ6.
R2=mm(R,R)
mats=[]
for M in (I,R,R2):
    mats.append(M)
    mats.append(tuple(tuple((-M[i][j])%MOD for j in range(2)) for i in range(2)))
assert len(set(mats))==6
G=[(M,t) for M in mats for t in E3]
assert len(G)==54

def act_pt(g,v):
    M,t=g
    w=mv(M,v)
    return ((w[0]+t[0])%MOD,(w[1]+t[1])%MOD)

def act_line(g,L):
    return frozenset(act_pt(g,v) for v in L)

assert all(act_line(g,L) in lines for g in G for L in lines)

# Orbit decomposition of the 81 lines.
unseen=set(lines)
orbits=[]
while unseen:
    L=next(iter(unseen))
    O={act_line(g,L) for g in G}
    orbits.append(O)
    unseen-=O
sizes=sorted(len(O) for O in orbits)
assert sizes==[9,18,54]
stab_sizes=sorted(54//len(O) for O in orbits)
assert stab_sizes==[1,3,6]

# Doubling-image classifier in E[3] ≅ F_3^2.
def two_mod3(v):
    q=((2*v[0])%6,(2*v[1])%6)
    assert q[0]%2==0 and q[1]%2==0
    return ((q[0]//2)%3,(q[1]//2)%3)

def classifier(L):
    D={two_mod3(v) for v in L}
    if len(D)==1:
        return 'singleton'
    assert len(D)==3
    # Direction is difference of two points, normalized projectively in F3^2.
    pts=list(D)
    dx=((pts[1][0]-pts[0][0])%3,(pts[1][1]-pts[0][1])%3)
    # unique fixed direction of R mod 3 is span(1,2), since (R-I)(1,2)=0 mod 3.
    fixed = dx in {(1,2),(2,1)}
    return 'fixed_direction' if fixed else 'other_direction'

profile={}
for O in orbits:
    kinds={classifier(L) for L in O}
    assert len(kinds)==1
    profile[next(iter(kinds))]=len(O)
assert profile=={'singleton':9,'fixed_direction':18,'other_direction':54}

# Fibres of the doubling image: 1 line over each E[3] point, 6 lines over each affine F3-line.
Ds=Counter()
for L in lines:
    D=frozenset(two_mod3(v) for v in L)
    Ds[D]+=1
point_images=[D for D in Ds if len(D)==1]
line_images=[D for D in Ds if len(D)==3]
assert len(point_images)==9 and all(Ds[D]==1 for D in point_images)
assert len(line_images)==12 and all(Ds[D]==6 for D in line_images)

print('VERIFY_OK points=27 lines=81 incidences=81x3=27x9 group=54 orbits=9+18+54 stabilizers=6,3,1 doubling=singleton+fixed_CM_direction+other_directions fibres=1_or_6')
