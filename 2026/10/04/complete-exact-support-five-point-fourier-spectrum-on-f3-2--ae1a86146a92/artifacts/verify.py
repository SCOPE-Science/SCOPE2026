#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, product

P=[(x,y) for x in range(3) for y in range(3)]
Z=(Fraction(0),Fraction(0)); O=(Fraction(1),Fraction(0)); W=(Fraction(0),Fraction(1))

def add(a,b): return (a[0]+b[0],a[1]+b[1])
def neg(a): return (-a[0],-a[1])
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    x,y=a; u,v=b
    return (x*u-y*v,x*v+y*u-y*v)
def inv(a):
    x,y=a; n=x*x-x*y+y*y
    return ((x-y)/n,-y/n)
def div(a,b): return mul(a,inv(b))
WP=[O,W,mul(W,W)]

def rank(A,ncols=5):
    A=[list(r) for r in A]
    m=len(A); r=0
    for c in range(ncols):
        p=next((i for i in range(r,m) if A[i][c]!=Z),None)
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]
        A[r]=[div(v,q) for v in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=Z:
                q=A[i][c]
                A[i]=[sub(A[i][j],mul(q,A[r][j])) for j in range(ncols)]
        r+=1
        if r==m: break
    return r

def F(A):
    return [[WP[(u*x+v*y)%3] for x,y in A] for u,v in P]

def coord_free(rows,j):
    e=[Z]*5; e[j]=O
    return rank(rows+[e])>rank(rows)

def closure(M,I):
    rows=[M[i] for i in I]; r=rank(rows)
    return tuple(i for i,row in enumerate(M) if rank(rows+[row])==r)

def eval_ft(A,c):
    ans=[]
    for u,v in P:
        s=Z
        for (x,y),a in zip(A,c): s=add(s,mul(a,WP[(u*x+v*y)%3]))
        ans.append(s)
    return ans

# The affine group AGL(2,3) gives exactly two orbits on five-subsets.
GL=[]
for a,b,c,d in product(range(3),repeat=4):
    if (a*d-b*c)%3: GL.append((a,b,c,d))
assert len(GL)==48

def act(A,M,t):
    a,b,c,d=M; s,t0=t
    return frozenset((((a*x+b*y+s)%3,(c*x+d*y+t0)%3) for x,y in A))
all5=[frozenset(S) for S in combinations(P,5)]
seen=set(); orbit_sizes=[]; orbit_reps=[]; ORBITS=[]
for A in all5:
    if A in seen: continue
    orb={act(A,M,t) for M in GL for t in P}
    seen|=orb; orbit_sizes.append(len(orb)); orbit_reps.append(min(orb,key=lambda B:tuple(sorted(B)))); ORBITS.append(orb)
assert len(seen)==126==len(all5)
assert sorted(orbit_sizes)==[54,72]

# Canonical representatives: a union of two intersecting lines, and the other orbit.
REPS=[
 [(0,0),(0,1),(0,2),(1,0),(2,0)],
 [(0,0),(0,1),(0,2),(1,0),(1,1)],
]
membership=[next(i for i,o in enumerate(ORBITS) if frozenset(A) in o) for A in REPS]
assert len(set(membership))==2
assert sorted(len(ORBITS[i]) for i in membership)==[54,72]

# Exhaust all 2^9 possible prescribed Fourier-zero row sets. A zero set must be
# row-span closed. Exact support on all five coefficients is possible iff the
# kernel is not trapped in a coordinate hyperplane. The resulting closure sizes
# are exactly 0,1,2,3,4 for both affine orbit types.
for A in REPS:
    M=F(A); sizes=set(); examples={}
    for mask in range(1<<9):
        I=[i for i in range(9) if (mask>>i)&1]
        rows=[M[i] for i in I]
        if rank(rows)>=5: continue
        if not all(coord_free(rows,j) for j in range(5)): continue
        C=closure(M,I)
        sizes.add(len(C)); examples.setdefault(len(C),C)
    assert sizes=={0,1,2,3,4}
    assert max(sizes)==4
    print('REP',A,'CLOSURE_SIZES',sorted(sizes))
    for z in sorted(examples):
        print('  zeros',z,'example_closure',[P[i] for i in examples[z]])

# Explicit Eisenstein-integer witnesses independently realize every zero count.
WIT=[
 [
  [(-2,2),(1,2),(-2,0),(-1,1),(-2,1)],
  [(-1,0),(2,0),(-1,0),(1,-2),(-1,2)],
  [(1,2),(-1,2),(0,2),(1,0),(2,0)],
  [(0,-1),(1,2),(-1,1),(0,2),(0,2)],
  [(0,1),(-1,0),(-1,0),(1,1),(1,1)],
 ],
 [
  [(0,-2),(0,2),(1,-1),(-2,1),(1,-1)],
  [(2,1),(2,2),(2,2),(0,1),(1,2)],
  [(-2,-2),(-2,-1),(-2,0),(0,-1),(0,1)],
  [(0,-1),(1,0),(1,-1),(-1,1),(1,2)],
  [(1,-1),(0,-1),(1,0),(2,2),(2,0)],
 ]
]
for A,table in zip(REPS,WIT):
    for wanted,c0 in enumerate(table):
        c=[(Fraction(a),Fraction(b)) for a,b in c0]
        assert all(a!=Z for a in c)
        zeros=[P[i] for i,v in enumerate(eval_ft(A,c)) if v==Z]
        assert len(zeros)==wanted
print('ORBIT_SIZES',sorted(orbit_sizes))
print('VERIFY_OK')
