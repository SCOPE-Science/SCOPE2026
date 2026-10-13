#!/usr/bin/env python3
"""Exact skew-line configuration census on the complex Fermat quartic.

Requires only the Python standard library. All geometry is computed in
Z[t]/(t^4+1), with t a primitive eighth root of unity.
"""
from itertools import combinations, permutations
from collections import Counter

MATCHINGS = (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2)))
EXPONENTS = (1,3,5,7)
LINES = tuple((m,r,s) for m in range(3) for r in EXPONENTS for s in EXPONENTS)
INDEX = {line:i for i,line in enumerate(LINES)}
assert len(LINES)==len(INDEX)==48
PERMS4 = tuple(permutations(range(4)))

def equations(line):
    m,r,s=line
    rows=[]
    for (a,b),exp in zip(MATCHINGS[m],(r,s)):
        row=[None]*4
        row[a]=(1,0)
        row[b]=(-1,exp)
        rows.append(tuple(row))
    return rows

# The determinant is reduced exactly in Z[t]/(t^4+1). A basis vector
# represents coefficients on 1,t,t^2,t^3.
def exact_determinant(rows):
    coeff=[0]*4
    for perm in PERMS4:
        sign=1; exponent=0
        for i in range(4):
            x=rows[i][perm[i]]
            if x is None: break
            sign*=x[0];exponent+=x[1]
        else:
            inversions=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))
            if inversions%2:sign=-sign
            exponent%=8
            if exponent>=4:sign=-sign;exponent-=4
            coeff[exponent]+=sign
    return tuple(coeff)

EQUATIONS=[equations(line) for line in LINES]
SKEW=[[False]*48 for _ in range(48)]
for i,j in combinations(range(48),2):
    d=exact_determinant(EQUATIONS[i]+EQUATIONS[j])
    SKEW[i][j]=SKEW[j][i]=any(d)

# Independent geometry cross-check: reduction at t=2 mod 17 and
# Gaussian elimination give the identical incidence matrix.
def rank17(rows):
    p=17
    a=[[sgn*pow(2,k,p)%p if entry is not None else 0
        for entry in row for sgn,k in ([entry] if entry is not None else [(0,0)])]
       for row in rows]
    rank=0
    for col in range(4):
        pivot=next((i for i in range(rank,4) if a[i][col]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        q=pow(a[rank][col],-1,p)
        a[rank]=[(q*x)%p for x in a[rank]]
        for i in range(4):
            if i!=rank:
                q=a[i][col]
                a[i]=[(x-q*y)%p for x,y in zip(a[i],a[rank])]
        rank+=1
    return rank

for i,j in combinations(range(48),2):
    assert SKEW[i][j] == (rank17(EQUATIONS[i]+EQUATIONS[j])==4)

# Each matching contributes at most four mutually skew lines: in that
# family, equal first exponents imply intersection. Thus a twelve-line
# skew set has exactly four lines in each family.
FOUR=[]
for family in range(3):
    FOUR.append(tuple(g for g in combinations(range(16*family,16*family+16),4)
                      if all(SKEW[i][j] for i,j in combinations(g,2))))
assert tuple(map(len,FOUR))==(24,24,24)

SYSTEMS=[]
for a in FOUR[0]:
    for b in FOUR[1]:
        if not all(SKEW[i][j] for i in a for j in b):continue
        for c in FOUR[2]:
            if all(SKEW[i][j] for i in a+b for j in c):
                SYSTEMS.append(tuple(sorted(a+b+c)))
assert len(SYSTEMS)==len(set(SYSTEMS))==128
ALL_SYSTEMS=set(SYSTEMS)

# A monomial projective automorphism is specified by a coordinate
# permutation and three fourth-root diagonal factors modulo scalars.
def transform_line(line,perm=(0,1,2,3),diag=(0,0,0,0),galois=1):
    m,r,s=line; out=[]
    for (a,b),k in zip(MATCHINGS[m],(r,s)):
        u,v=perm[a],perm[b]
        k=(galois*k+2*(diag[u]-diag[v]))%8
        if u>v:u,v=v,u;k=(-k)%8
        out.append(((u,v),k))
    out.sort()
    fam=next(q for q,P in enumerate(MATCHINGS)
             if sorted(P)==[pair for pair,_ in out])
    return INDEX[(fam,out[0][1],out[1][1])]

def transform_system(system,action):
    return tuple(sorted(action[i] for i in system))

GENERATORS=[]
for j in range(3):
    d=[0]*4;d[j]=1
    GENERATORS.append(tuple(transform_line(line,diag=d) for line in LINES))
for j in range(3):
    p=list(range(4));p[j],p[j+1]=p[j+1],p[j]
    GENERATORS.append(tuple(transform_line(line,perm=p) for line in LINES))
assert all(set(g)==set(range(48)) for g in GENERATORS)
for s in SYSTEMS:
    assert all(transform_system(s,g) in ALL_SYSTEMS for g in GENERATORS)

ORBIT_CLASSES=[]
remain=set(SYSTEMS)
while remain:
    representative=min(remain)
    orbit={representative};front=[representative]
    while front:
        s=front.pop()
        for gen in GENERATORS:
            t=transform_system(s,gen)
            if t not in orbit:
                orbit.add(t);front.append(t)
    ORBIT_CLASSES.append(orbit)
    remain-=orbit
assert sorted(map(len,ORBIT_CLASSES))==[32,96]

GALOIS={k:tuple(transform_line(line,galois=k) for line in LINES)
        for k in (1,3,5,7)}
FIXED={k:sum(transform_system(s,g)==s for s in SYSTEMS)
       for k,g in GALOIS.items()}
assert FIXED=={1:128,3:16,5:128,7:16}
GAL_ORBITS=[];remain=set(SYSTEMS)
while remain:
    s=min(remain)
    orbit={transform_system(s,g) for g in GALOIS.values()}
    assert orbit<=ALL_SYSTEMS
    GAL_ORBITS.append(orbit);remain-=orbit
assert Counter(map(len,GAL_ORBITS))=={1:16,2:56}

DEGREES=Counter(sum(j in s for s in SYSTEMS) for j in range(48))
assert DEGREES=={32:48}
INTERSECTIONS=Counter(len(set(a)&set(b)) for a,b in combinations(SYSTEMS,2))
assert dict(INTERSECTIONS)=={0:4160,2:384,4:960,6:1280,8:960,10:384}
assert sum(INTERSECTIONS.values())==128*127//2

print('VERIFY_OK')
print('lines=48; families=16,16,16; 4-skew families=24,24,24')
print('complete 12-skew systems=128; projective automorphism group order=1536')
print('projective orbit sizes=',sorted(map(len,ORBIT_CLASSES)))
print('projective stabilizer orders=',[1536//len(o) for o in sorted(ORBIT_CLASSES,key=len)])
print('Galois fixed counts=',FIXED)
print('Galois orbit sizes=',dict(sorted(Counter(map(len,GAL_ORBITS)).items())))
print('systems defined over Q=16; minimally over Q(i)=112')
print('each line belongs to 32 systems')
print('inter-system intersections=',dict(sorted(INTERSECTIONS.items())))
for orbit in sorted(ORBIT_CLASSES,key=len):
    print('orbit representative (%s)='%len(orbit),min(orbit))
