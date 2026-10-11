#!/usr/bin/env python3
from itertools import combinations
from collections import defaultdict, Counter, deque
from math import gcd

V = tuple(range(1,13))

def perm_from_cycles(cycles):
    p=list(V)
    for cyc in cycles:
        for i,a in enumerate(cyc): p[a-1]=cyc[(i+1)%len(cyc)]
    return tuple(p)

def compose(p,q): return tuple(p[q[i]-1] for i in range(12))
def image_face(f,p): return tuple(sorted(p[x-1] for x in f))

GENS=[
    perm_from_cycles([(1,9,5),(2,4,3),(6,8,7),(10,12,11)]),
    perm_from_cycles([(1,11,6),(2,9,7),(3,10,5),(4,8,12)]),
]
G={V}; q=[V]
while q:
    a=q.pop()
    for g in GENS:
        b=compose(g,a)
        if b not in G:
            G.add(b); q.append(b)
assert len(G)==12

seeds=[(1,2,3),(1,2,4),(1,3,8)]
F=set()
for s in seeds:
    O={image_face(s,g) for g in G}
    F |= O
assert [len({image_face(s,g) for g in G}) for s in seeds]==[12,12,4]
E=sorted({e for f in F for e in combinations(f,2)})
ES=set(E)
assert (len(V),len(E),len(F))==(12,42,28)
assert len(F)==28 and 12-42+28==-2
# surface checks: every edge degree two, every link a cycle
inc=Counter(e for f in F for e in combinations(f,2))
assert set(inc.values())=={2}
for v in V:
    ledges=[]
    for f in F:
        if v in f:
            a,b=sorted(set(f)-{v}); ledges.append((a,b))
    deg=Counter(x for e in ledges for x in e)
    assert all(x==2 for x in deg.values())
    adjL=defaultdict(list)
    for a,b in ledges: adjL[a].append(b);adjL[b].append(a)
    st=[next(iter(deg))]; seen={st[0]}
    while st:
        u=st.pop()
        for w in adjL[u]:
            if w not in seen: seen.add(w);st.append(w)
    assert len(seen)==len(deg)

# deterministic spanning tree and graph-cycle coordinates
adj=defaultdict(list)
for a,b in E: adj[a].append(b);adj[b].append(a)
for a in adj: adj[a].sort()
TREE=set(); seen={1}; Q=deque([1])
while Q:
    u=Q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v);Q.append(v);TREE.add(tuple(sorted((u,v))))
NTE=[e for e in E if e not in TREE]
EI={e:i for i,e in enumerate(NTE)}
assert len(NTE)==31

def trirow(t):
    a,b,c=sorted(t); r=[0]*len(NTE)
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]:
        if e in EI: r[EI[e]] += s
    return r
R=[trirow(t) for t in sorted(F)]

# Unimodularly isolate all available unit pivots. After 27 unit pivots,
# the remaining 1x4 row has gcd 2, proving Smith data 1^27,2.
def isolate_units(M):
    A=[row[:] for row in M]
    m=len(A); n=len(A[0]); r=c=0; piv=0
    while r<m and c<n:
        pos=None
        for i in range(r,m):
            for j in range(c,n):
                if abs(A[i][j])==1:
                    pos=(i,j);break
            if pos: break
        if pos is None: break
        i,j=pos
        A[r],A[i]=A[i],A[r]
        for row in A: row[c],row[j]=row[j],row[c]
        if A[r][c]==-1: A[r]=[-x for x in A[r]]
        for i2 in range(m):
            if i2!=r and A[i2][c]:
                q=A[i2][c]
                A[i2]=[A[i2][j2]-q*A[r][j2] for j2 in range(n)]
        for j2 in range(n):
            if j2!=c and A[r][j2]:
                q=A[r][j2]
                for i2 in range(m): A[i2][j2]-=q*A[i2][c]
        assert A[r][c]==1
        assert all(A[i][c]==0 for i in range(m) if i!=r)
        assert all(A[r][j]==0 for j in range(n) if j!=c)
        r+=1;c+=1;piv+=1
    return A,r,c,piv
A,r,c,piv=isolate_units(R)
assert piv==27
res=[A[i][c:] for i in range(r,len(A))]
assert len(res)==1 and len(res[0])==4
g=0
for x in res[0]: g=gcd(g,abs(x))
assert g==2 and any(res[0])
# Hence H1 = Z^(31-28) + Z/2.

Y=[
[0,0,1,0,0,0,0,0,0,0,0,0,-1,0,1,-1,0,0,0,1,0,1,1,-1,0,0,0,1,1,1,0],
[0,0,0,1,0,0,1,-1,0,0,0,1,1,0,0,0,0,0,0,-1,0,-1,0,1,0,0,-1,-1,0,0,0],
[0,0,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,-1,0,0,0,0,0,0,0,-1,0,-1,-1,-1,0],
]
WPOS={13,19,21,23,27,28,29}
# relation annihilation
for rr in R:
    assert [sum(a*b for a,b in zip(rr,y)) for y in Y]==[0,0,0]
    assert sum((rr[j]&1) for j in WPOS)&1==0

def pathrow(vs):
    rr=[0]*len(NTE); cyc=list(vs)+[vs[0]]
    for u,v in zip(cyc,cyc[1:]):
        e=tuple(sorted((u,v))); assert e in ES
        if e in EI: rr[EI[e]] += 1 if (u,v)==e else -1
    return rr

def coord(vs):
    rr=pathrow(vs)
    free=tuple(sum(a*b for a,b in zip(rr,y)) for y in Y)
    bit=sum((rr[j]&1) for j in WPOS)&1
    return free+(bit,)

basis=[(1,2,12),(1,3,4),(1,4,6)]
assert [coord(x) for x in basis]==[(1,0,0,0),(0,1,0,0),(0,0,1,0)]
torsion_witness=(1,2,5,7,8,11)
assert coord(torsion_witness)==(0,0,0,1)
# Since the proven group type is Z^3 + Z/2, these jointly onto coordinates are exact.

clq=[t for t in combinations(V,3) if all(tuple(sorted(e)) in ES for e in combinations(t,2))]
empty=[t for t in clq if t not in F]
assert (len(clq),len(empty))==(48,20)

def canon(fc):
    free=fc[:-1]; b=fc[-1]
    for x in free:
        if x:
            if x<0: free=tuple(-y for y in free)
            break
    return free+(b,)
C=Counter(canon(coord(t)) for t in empty)
expected=Counter({
    (0,1,0,0):4,
    (0,0,1,0):4,
    (1,-1,-1,0):4,
    (1,0,0,1):4,
    (1,0,0,0):1,
    (0,0,1,1):1,
    (1,-1,-1,1):1,
    (0,1,0,1):1,
})
assert C==expected
assert all(fc[:3]!=(0,0,0) or fc[3] for fc in (coord(t) for t in empty))
for t in empty:
    f=coord(t)[:3]
    assert gcd(gcd(abs(f[0]),abs(f[1])),abs(f[2]))==1

free_group=defaultdict(Counter)
for fc,n in C.items(): free_group[fc[:3]][fc[3]]+=n
assert set(free_group)=={(1,0,0),(0,1,0),(0,0,1),(1,-1,-1)}
assert all(sorted(cnt.values())==[1,4] and set(cnt)=={0,1} for cnt in free_group.values())

# Published A4 action on carriers.
remaining=set(empty); carrier_orbits=[]
while remaining:
    t=min(remaining)
    O={image_face(t,g) for g in G} & set(empty)
    carrier_orbits.append(O); remaining-=O
assert sorted(map(len,carrier_orbits))==[4,4,12]

class_rep={}
for t in empty: class_rep.setdefault(canon(coord(t)),t)
remaining=set(class_rep); class_orbits=[]
while remaining:
    cc=min(remaining); t=class_rep[cc]; O=set()
    for g in G:
        im=tuple(g[x-1] for x in t)  # preserve cycle orientation
        O.add(canon(coord(im)))
    class_orbits.append(O); remaining-=O
assert sorted(map(len,class_orbits))==[4,4]
multsets=sorted([sorted({C[x] for x in O}) for O in class_orbits])
assert multsets==[[1],[4]]

print(
    'VERIFY_OK f=12,42,28 surface=N4 H1_Z=Z^3+Z/2 '
    'graph_triangles=48 facial3=28 empty3=20 all_empty3_nonzero=yes '
    'all_free_projections_primitive=yes simple_integral_1_systole=3 '
    'free_directions=4 both_torsion_lifts_each=yes lift_counts_each=4+1 '
    'A4_carrier_orbits=4,4,12 A4_class_orbits=4,4 '
    'class_orbit_multiplicities=1|4 smith=1^27,2 torsion_witness_len=6'
)
