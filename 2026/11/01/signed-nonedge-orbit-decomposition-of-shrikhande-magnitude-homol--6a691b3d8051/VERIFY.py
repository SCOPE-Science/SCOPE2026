#!/usr/bin/env python3
"""Exact rational-chain verification for the Shrikhande magnitude-homology representation.

Run: python3 VERIFY.py .  (Python 3.10+; standard library only).
Requires CHARACTER.csv in the selected directory and checks every record.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
from pathlib import Path
import csv
import sys

P = tuple((x,y) for x in range(4) for y in range(4))
STEPS={(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)}
I=tuple(range(16))

def add(a,b): return ((a[0]+b[0])%4,(a[1]+b[1])%4)
def act(m,v): return ((m[0]*v[0]+m[1]*v[1])%4,(m[2]*v[0]+m[3]*v[1])%4)
def multiply_perm(p,q): return tuple(p[q[j]] for j in range(16))

MAT=[m for m in product(range(4),repeat=4)
     if (m[0]*m[3]-m[1]*m[2])%2==1 and {act(m,s) for s in STEPS}==STEPS]
assert len(MAT)==12
G=[(m,t,tuple(P.index(add(act(m,v),t)) for v in P)) for m in MAT for t in P]
assert len(G)==192 and len({g for _,_,g in G})==192
PERMS={g:i for i,(_,_,g) in enumerate(G)}
INV=[PERMS[tuple(g.index(j) for j in I)] for m,t,g in G]
assert I in PERMS

def mul(i,j): return PERMS[multiply_perm(G[i][2],G[j][2])]
N=[{j for j in I if j!=i and ((P[j][0]-P[i][0])%4,(P[j][1]-P[i][1])%4) in STEPS} for i in I]
DIST=[[0 if i==j else (1 if j in N[i] else 2) for j in I] for i in I]
assert all(len(n)==6 for n in N)
assert all(DIST[g[i]][g[j]]==DIST[i][j] for m,t,g in G for i in I for j in I)
# The link of 0 is a hexagon; the 9 nonneighbors have pairwise different
# intersections with that link, so every automorphism fixing 0 injects into D_12.
assert sorted(len(N[v]&N[0]) for v in N[0])==[2]*6
assert all(len(N[v]&N[0])==2 for v in I if v!=0 and v not in N[0])
assert len({tuple(sorted(N[v]&N[0])) for v in I if v!=0 and v not in N[0]})==9
assert sorted(len(N[v]&N[0]) for v in N[0])==[2]*6
assert len({tuple(sorted((v,w))) for v in N[0] for w in N[0] if w in N[v]})==6

# Exact rational linear algebra, computed on sparse integer boundary columns.
def elim(basis,col):
    c={i:Fraction(v) for i,v in col.items() if v}
    for pivot,vec in sorted(basis.items()):
        if pivot in c:
            scalar=c[pivot]
            for i,a in vec.items():
                new=c.get(i,0)-scalar*a
                if new:c[i]=new
                elif i in c:del c[i]
    return c

def insert(basis,col):
    c=elim(basis,col)
    if not c:return False
    pivot=min(c);scale=c[pivot]
    basis[pivot]={i:v/scale for i,v in c.items()}
    return True

def basis_for(cols):
    basis={}
    for c in cols:insert(basis,c)
    return basis

def chain(a,b,k):
    return [s for mid in product(I,repeat=k-1)
            if all(u!=v for u,v in zip((a,)+mid,mid+(b,)))
            for s in [(a,)+mid+(b,)]
            if sum(DIST[s[j]][s[j+1]] for j in range(k))==4]

def boundary(seq):
    result={}
    for i in range(1,len(seq)-1):
        if DIST[seq[i-1]][seq[i]]+DIST[seq[i]][seq[i+1]]==DIST[seq[i-1]][seq[i+1]]:
            face=seq[:i]+seq[i+1:]
            result[face]=result.get(face,0)+(-1)**i
            if result[face]==0:del result[face]
    return result

def local(a,b):
    c2,c3,c4=(chain(a,b,k) for k in (2,3,4))
    rows2={v:i for i,v in enumerate(c2)}
    rows3={v:i for i,v in enumerate(c3)}
    def columns(cs,rows):return [{rows[f]:v for f,v in boundary(s).items()} for s in cs]
    b3=columns(c3,rows2); b4=columns(c4,rows3)
    # Verify the chain identity on every column, not only on the ranks.
    for c in c4:
        dd=defaultdict(int)
        for face,sgn in boundary(c).items():
            for ff,sgn2 in boundary(face).items():dd[ff]+=sgn*sgn2
        assert all(v==0 for v in dd.values())
    basis3=basis_for(b3);basis4=basis_for(b4)
    return (c2,c3,c4,rows3,basis3,basis4)

# Four full orbits of ordered pairs; no global rank inference from an unchecked sample.
REP=(0,1,2,6)
EXPECTED={0:(9,54,96,9,45,0),1:(6,54,80,6,48,0),
          2:(4,66,80,4,61,1),6:(4,66,80,4,61,1)}
for b in REP:
    c2,c3,c4,rm,b3,b4=local(0,b)
    data=(len(c2),len(c3),len(c4),len(b3),len(b4),len(c3)-len(b3)-len(b4))
    assert data==EXPECTED[b],(b,data)

# The affine group is exactly the full group of graph automorphisms.
# Its action partitions ordered pairs into the following four orbits.
ORBIT={}
for a in I:
    for b in I:
        for rep in [(0,v) for v in REP]:
            if any(g[rep[0]]==a and g[rep[1]]==b for _,_,g in G):
                ORBIT[(a,b)]=rep;break
        assert (a,b) in ORBIT
assert Counter(ORBIT.values())==Counter({(0,0):16,(0,1):96,(0,2):48,(0,6):96})

# Give a closed nonboundary chain generator in each of the two nonedge fibers.
GENERATORS={(0,2):(0,4,13,2),(0,6):(0,3,10,6)}
SIGNS={}
for rep,gen in GENERATORS.items():
    a,b=rep
    c2,c3,c4,rows,basis3,basis4=local(a,b)
    assert gen in rows and not boundary(gen)
    assert elim(basis4,{rows[gen]:1}) # nonzero homology class
    stab=[]
    for gi,(m,t,g) in enumerate(G):
        if g[a]==a and g[b]==b:
            image=tuple(g[x] for x in gen)
            assert image in rows and not boundary(image)
            poss=[]
            for sgn in (-1,1):
                difference={rows[image]:1}
                difference[rows[gen]]=difference.get(rows[gen],0)-sgn
                if not elim(basis4,difference):poss.append(sgn)
            assert len(poss)==1,(rep,m,t,poss)
            SIGNS[(rep,gi)]=poss[0]
            stab.append(poss[0])
    assert Counter(stab)==(Counter({1:2,-1:2}) if b==2 else Counter({1:1,-1:1}))

# Transporter conjugation evaluates every fixed local summand, producing the
# entire character on the 192 group elements.
TRANS={}
for a in I:
    for b in I:
        if DIST[a][b]!=2:continue
        for rep in GENERATORS:
            candidates=[gi for gi,(_,_,g) in enumerate(G) if g[rep[0]]==a and g[rep[1]]==b]
            if candidates:
                TRANS[a,b]=(rep,candidates[0]);break
        assert (a,b) in TRANS
assert len(TRANS)==144
CHAR=[]
for gi,(m,t,g) in enumerate(G):
    trace=0
    for (a,b),(rep,tr) in TRANS.items():
        if g[a]==a and g[b]==b:
            s=mul(mul(INV[tr],gi),tr)
            trace+=SIGNS[(rep,s)]
    CHAR.append(trace)
assert Counter(CHAR)==Counter({0:163,-12:16,4:12,144:1})
assert CHAR[PERMS[I]]==144 and sum(CHAR)==0
# The induced character must be constant on every conjugacy class.
for h in range(len(G)):
    for g in range(len(G)):
        assert CHAR[mul(mul(h,g),INV[h])]==CHAR[g]

# Verify that the delivered full character table is the one computed here.
output_dir=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent
p=output_dir/'CHARACTER.csv'
assert p.is_file(),'Missing character table'
with p.open(newline='',encoding='utf-8') as fp:
    r=list(csv.DictReader(fp))
assert len(r)==192
for i,row in enumerate(r):
    m,t,_=G[i]
    assert tuple(int(row[f'm{j}']) for j in range(4))==m
    assert tuple(int(row[f't{j}']) for j in range(2))==t
    assert int(row['trace'])==CHAR[i]
print('GRAPH_OK vertices=16 automorphisms=192 ordered_nonedge_orbits=48,96')
for b in REP:print('LOCAL_RANKS',b,EXPECTED[b])
print('STABILIZER_SIGNS orbit48=+,+,-,- orbit96=+,-')
print('CHARACTER_COUNTS identity=144:1 positive4:12 negative12:16 zero:163')
print('INVARIANTS_DIM=0')
print('VERIFY_OK')
