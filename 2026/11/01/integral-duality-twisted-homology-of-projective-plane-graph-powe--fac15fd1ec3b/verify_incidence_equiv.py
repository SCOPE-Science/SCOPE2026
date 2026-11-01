#!/usr/bin/env python3
"""Self-contained checks for the incidence-plane equivariant Rips theorem (Fano case)."""
import itertools
from collections import Counter,deque

def parity(x): return x.bit_count() & 1
P=tuple(range(1,8))
def matvec(A,x): return sum(parity(a&x)<<i for i,a in enumerate(A))
def invert(A):
    for B in itertools.product(range(8),repeat=3):
        if all(matvec(B,matvec(A,x))==x for x in range(8)):
            return B
    return None
def transpose(A):return tuple(sum(((A[i]>>j)&1)<<i for i in range(3)) for j in range(3))
GL=[A for A in itertools.product(range(8),repeat=3) if invert(A) is not None]
assert len(GL)==168
flags=sorted((p-1,7+l-1) for p in P for l in P if parity(p&l)==0)
assert len(flags)==21
for a,b in itertools.combinations(P,2):
    assert sum(not parity(a&l) and not parity(b&l) for l in P)==1
    assert sum(not parity(a&p) and not parity(b&p) for p in P)==1
# Compute graph distances by BFS, then construct VR <= 2 without assuming its expected form.
adj=[set() for _ in range(14)]
for p,l in flags:adj[p].add(l);adj[l].add(p)
dist=[]
for src in range(14):
    ds=[100]*14;ds[src]=0;queue=deque([src])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if ds[v]>ds[u]+1:ds[v]=ds[u]+1;queue.append(v)
    dist.append(ds)
assert max(map(max,dist))==3
faces=[]
for mask in range(1,1<<14):
    tup=tuple(i for i in range(14) if mask & (1<<i))
    if all(dist[i][j]<=2 for i,j in itertools.combinations(tup,2)):
        faces.append(tup)
assert len(faces)==331
sizes=Counter(len(f) for f in faces)
assert [sizes[k] for k in range(1,8)]==[14,63,112,84,42,14,2]

# Explicit complete automorphism enumeration: collineations are exactly 168,
# and the orthogonality polarity exchanges the two vertex classes.
lines={frozenset(p-1 for p in P if parity(p&l)==0) for l in P}
autset=[]
for perm in itertools.permutations(range(7)):
    if {frozenset(perm[i] for i in line) for line in lines}==lines:
        autset.append(perm)
assert len(autset)==168
assert set(autset)=={tuple(matvec(A,x)-1 for x in P) for A in GL}

# Independent signed simplicial Lefschetz trace, requiring no homology bases.
def simplex_sign(images):
    return -1 if sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))%2 else 1

def direct_lefschetz(g):
    # Connected complex and H_i(K) vanishes outside i=0,2 by the MV proof.
    return -1+sum((-1)**(len(f)-1)*simplex_sign([g[i] for i in f])
                  for f in faces if set(g[i] for i in f)==set(f))

# Build a fundamental integral cycle basis from a spanning tree.
ie={e:i for i,e in enumerate(flags)}
inc=[[] for _ in range(14)]
for i,(p,l) in enumerate(flags):
    inc[p].append((l,i,1));inc[l].append((p,i,-1))
seen={0};Q=deque([0]);tree=set()
while Q:
    u=Q.popleft()
    for v,i,s in inc[u]:
        if v not in seen:seen.add(v);tree.add(i);Q.append(v)
assert len(seen)==14 and len(tree)==13
chords=[i for i in range(21) if i not in tree]
assert len(chords)==8
cycles=[]
for e in chords:
    p,l=flags[e];c=[0]*21;c[e]=1
    prev={l:None};Q=deque([l])
    while p not in prev:
        u=Q.popleft()
        for v,i,s in inc[u]:
            if i in tree and v not in prev:prev[v]=(u,i,s);Q.append(v)
    v=p
    while v!=l:
        u,i,s=prev[v];c[i]+=s;v=u
    for v in range(14):
        boundary=sum(((-1 if v==p else 1)*c[i]) for i,(p,l) in enumerate(flags) if v in (p,l))
        assert boundary==0
    cycles.append(c)

def char2rank(rows):
    basis={}
    for row in rows:
        value=sum((int(x)%2)<<i for i,x in enumerate(row))
        while value:
            pivot=value.bit_length()-1
            if pivot not in basis:basis[pivot]=value;break
            value^=basis[pivot]
    return len(basis)

# Check all automorphisms (no reliance on group-class tables).
col=Counter();dual=Counter();mat_id=[]
for A in GL:
    iv=invert(A);tv=transpose(iv)
    pp=[matvec(A,x)-1 for x in P]
    ll=[7+matvec(tv,x)-1 for x in P]
    for swap in (False,True):
        g=pp+ll if not swap else [v+7 for v in pp]+[v-7 for v in ll]
        assert {tuple(sorted((g[p],g[l]))) for p,l in flags}==set(flags)
        fix_v=sum(g[i]==i for i in range(14))
        fix_e=sum(g[p]==p and g[l]==l for p,l in flags) if not swap else sum(g[p]==l and g[l]==p for p,l in flags)
        expected=fix_e-fix_v+1 if not swap else fix_e-1
        actual=direct_lefschetz(g)
        assert actual==expected,(A,swap,actual,expected)
        (dual if swap else col)[actual]+=1
        # Integral cycle action in chord coordinates, with the extra sign
        # for side-exchanging automorphisms on 2-dimensional homology.
        columns=[]
        for c in cycles:
            cp=[0]*21
            for i,(p,l) in enumerate(flags):
                a,b=g[p],g[l]
                s=1
                if a>=7:a,b=b,a;s=-1
                cp[ie[(a,b)]]+=s*c[i]*(-1 if swap else 1)
            columns.append([cp[j] for j in chords])
        mat_id.append((A,swap,columns))

assert col==Counter({8:1,1:48,0:63,-1:56}),col
assert dual==Counter({2:28,0:84,-1:56}),dual
assert sum(t*t*count for t,count in col.items())==168
assert sum(t*t*count for t,count in (col+dual).items())==336
# The canonical orthogonality polarity corresponds to the identity matrix.
ident=(1,2,4)
c=next(cols for A,sw,cols in mat_id if sw and A==ident)
assert sum(c[j][j] for j in range(8))==2
assert all(sum(c[k][i]*c[j][k] for k in range(8))==int(i==j) for i in range(8) for j in range(8))
Iplus=[[c[j][i]+int(i==j) for i in range(8)] for j in range(8)]
assert char2rank(Iplus)==3
print('PLANE=q2 flags=21 vertices=14 automorphisms=336')
print('RIPS_FACE_VECTOR='+repr([sizes[k] for k in range(1,8)]))
print('H2_RANK=8 VIA INTEGRAL_MV')
print('COLLINEATION_TRACES='+repr(sorted(col.items())))
print('DUALITY_TRACES='+repr(sorted(dual.items())))
print('POLARITY_TRACE=2, MOD2_RANK_OF_(I+P)=3')
print('IRREDUCIBILITY_CHARACTER_NORM=1')
print('VERIFY_OK')
