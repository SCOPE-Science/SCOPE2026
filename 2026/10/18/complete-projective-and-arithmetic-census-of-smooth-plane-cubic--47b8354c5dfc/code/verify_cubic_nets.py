#!/usr/bin/env python3
"""Exact census of smooth plane-cubic nets over the two-element field.

Only the Python standard library is required. All calculations take place in
finite vector spaces and binary polynomial rings, without numerical tolerance.
"""
from collections import Counter
from itertools import product

M3 = [(3,0,0),(2,1,0),(2,0,1),(1,2,0),(1,1,1),
      (1,0,2),(0,3,0),(0,2,1),(0,1,2),(0,0,3)]
M2 = [(2,0,0),(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
M4 = [(a,b,4-a-b) for a in range(5) for b in range(5-a)]
PROJ = [(x,y,z) for x,y,z in product((0,1),repeat=3) if x or y or z]

def binary_rank(rows):
    pivots={}
    for t in rows:
        while t:
            j=t.bit_length()-1
            if j in pivots: t^=pivots[j]
            else: pivots[j]=t; break
    return len(pivots)

DIFF = [[(j,M2.index(tuple(e - (i==k) for k,e in enumerate(m))))
         for j,m in enumerate(M3) if m[i]%2] for i in range(3)]
SHIFT = [[M4.index(tuple(a+b for a,b in zip(u,v))) for v in M2] for u in M2]

def smooth(f):
    derivatives=[]
    for terms in DIFF:
        d=0
        for j,k in terms:
            if (f>>j)&1: d^=1<<k
        derivatives.append(d)
    degree4=[]
    for d in derivatives:
        for shifted in SHIFT:
            row=0
            for k,j in enumerate(shifted):
                if (d>>k)&1: row^=1<<j
            degree4.append(row)
    return binary_rank(degree4)==15

EVAL=[]
for P in PROJ:
    EVAL.append(sum(1<<j for j,m in enumerate(M3)
                    if all(P[k] or not exponent for k,exponent in enumerate(m))))

def point_count(f):
    return sum(((f & ev).bit_count()%2)==0 for ev in EVAL)

SMOOTH={f for f in range(1,1024) if smooth(f)}
assert len(SMOOTH)==336
assert Counter(point_count(f) for f in SMOOTH)=={1:42,2:84,3:84,4:84,5:42}

# Each two-dimensional binary subspace has its three nonzero elements.
PENCILS=set()
for a in sorted(SMOOTH):
    for b in sorted(x for x in SMOOTH if x>a):
        c=a^b
        if c in SMOOTH and b<c:
            PENCILS.add((a,b,c))
assert len(PENCILS)==5544

# Every three-dimensional subspace contains one of these pencils.
NETS=set()
for a,b,c in PENCILS:
    for v in SMOOTH:
        if v in (a,b,c):continue
        net=tuple(sorted((a,b,c,v,a^v,b^v,c^v)))
        if set(net)<=SMOOTH:NETS.add(net)
assert len(NETS)==864

# A four-dimensional subspace would extend some maximal net.
FOUR=set()
for net in NETS:
    S=set(net)|{0}
    for v in SMOOTH-S:
        if all((v^w) in SMOOTH for w in S):
            FOUR.add(tuple(sorted((S|{v^w for w in S})-{0})))
assert len(FOUR)==0

SPECTRA=Counter(tuple(sorted(point_count(f) for f in net)) for net in NETS)
EXPECT={
    (1,1,2,4,4,4,5):168,
    (1,1,3,3,3,5,5):168,
    (1,2,2,3,4,4,5):336,
    (2,2,2,3,3,4,5):168,
    (3,3,3,3,3,3,3):24,
}
assert SPECTRA==EXPECT

# PGL_3(F_2)=GL_3(F_2) acts by degree-three substitution.
def multiply(A,B):
    out=set()
    for x in A:
        for y in B:
            z=tuple(a+b for a,b in zip(x,y))
            if z in out:out.remove(z)
            else:out.add(z)
    return out

def power(P,n):
    out={(0,0,0)}
    for _ in range(n):out=multiply(out,P)
    return out

GL=[]
for rows in product(range(1,8),repeat=3):
    if binary_rank(rows)==3:GL.append(rows)
assert len(GL)==168

TRANSFORMS=[]
for A in GL:
    L=[{tuple(int(k==j) for k in range(3)) for j in range(3)
        if (A[i]>>j)&1} for i in range(3)]
    images=[]
    for exponents in M3:
        P={(0,0,0)}
        for i,e in enumerate(exponents):P=multiply(P,power(L[i],e))
        images.append(sum(1<<M3.index(e) for e in P))
    TRANSFORMS.append(images)

def substitute(f,images):
    g=0
    for i in range(10):
        if (f>>i)&1:g^=images[i]
    return g

remaining=set(NETS)
ORBIT_REPS=[]
while remaining:
    rep=min(remaining)
    orbit={tuple(sorted(substitute(f,A) for f in rep)) for A in TRANSFORMS}
    assert orbit<=NETS
    remaining-=orbit
    ORBIT_REPS.append((rep,len(orbit)))
assert len(ORBIT_REPS)==8
assert Counter(size for _,size in ORBIT_REPS)=={168:5,8:3}
assert sum(size for _,size in ORBIT_REPS)==len(NETS)
assert not remaining

print('smooth cubics:',len(SMOOTH))
print('smooth pencils:',len(PENCILS))
print('smooth nets:',len(NETS))
print('smooth four-dimensional systems:',len(FOUR))
print('net projective orbits:',len(ORBIT_REPS))
print('orbit sizes:',sorted(size for _,size in ORBIT_REPS))
print('point-count multisets:',dict(sorted(SPECTRA.items())))
for rep,size in ORBIT_REPS:
    a,b=rep[:2]
    c=next(v for v in rep if v not in (a,b,a^b))
    print('orbit: basis', (a,b,c),'size',size,'counts',tuple(sorted(point_count(f) for f in rep)))
