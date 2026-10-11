from itertools import combinations
from collections import Counter

N=14
DIFFS=[(1,1,1,11),(1,2,4,7),(1,4,2,7),(1,4,7,2),(2,4,4,4),(2,5,2,5)]

def orbit_tet(c):
    a,b,c2,d=c
    base=(0,a,a+b,a+b+c2)
    return {tuple(sorted((x+s)%N for x in base)) for s in range(N)}

facets=set()
for d in DIFFS:
    facets |= orbit_tet(d)
faces=[set() for _ in range(4)]
for f in facets:
    for r in range(1,5):
        faces[r-1].update(combinations(f,r))
assert [len(x) for x in faces]==[14,91,154,77]
assert len(facets)==77
edges=sorted(faces[1]); tris=sorted(faces[2]); tri_set=set(tris)
eidx={e:i for i,e in enumerate(edges)}

def rank_mod(A,p):
    A=[[(x%p) for x in row] for row in A]
    m=len(A); n=len(A[0]) if m else 0
    r=0
    for c in range(n):
        q=next((i for i in range(r,m) if A[i][c]),None)
        if q is None: continue
        A[r],A[q]=A[q],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]
                A[i]=[(A[i][j]-z*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r

# Boundary ranks over F_3.
d1=[[0]*len(edges) for _ in range(N)]
for j,(a,b) in enumerate(edges):
    d1[a][j]=-1; d1[b][j]=1
d2=[[0]*len(tris) for _ in range(len(edges))]
for j,(a,b,c) in enumerate(tris):
    d2[eidx[(b,c)]][j]=1
    d2[eidx[(a,c)]][j]=-1
    d2[eidx[(a,b)]][j]=1
r1=rank_mod(d1,3); r2=rank_mod(d2,3)
h1=len(edges)-r1-r2
assert (r1,r2,h1)==(13,77,1)

# An explicit alternating cyclic 1-cocycle. For an oriented edge i->j,
# w(i,j)=(-1)^i q[j-i mod 14] in F_3.
q={1:1,2:0,3:1,4:1,5:0,6:1,7:0,8:2,9:0,10:2,11:1,12:0,13:1}
def w(i,j):
    if i==j: return 0
    return ((1 if i%2==0 else -1)*q[(j-i)%N])%3

def eval3(t):
    a,b,c=t
    return (w(a,b)+w(b,c)+w(c,a))%3

assert all(eval3(t)==0 for t in tris)
assert eval3((0,1,4))!=0
assert all(w((i+1)%N,(j+1)%N)==(-w(i,j))%3
           for i in range(N) for j in range(N) if i!=j)

all3=list(combinations(range(N),3))
empty=[t for t in all3 if t not in tri_set]
cnt=Counter(eval3(t) for t in empty)
assert len(empty)==210
assert cnt==Counter({0:28,1:91,2:91})

# Cyclic orbits of empty triangles.
def shift(t,s): return tuple(sorted((x+s)%N for x in t))
seen=set(); eorbits=[]
for t in all3:
    if t in seen: continue
    o={shift(t,s) for s in range(N)}
    seen |= o
    if t not in tri_set:
        eorbits.append(o)
assert len(eorbits)==15 and all(len(o)==14 for o in eorbits)
null_orbits=[]; essential_orbits=[]
for o in eorbits:
    vals=Counter(eval3(t) for t in o)
    if vals==Counter({0:14}): null_orbits.append(o)
    else:
        assert vals==Counter({1:7,2:7})
        essential_orbits.append(o)
assert len(null_orbits)==2 and len(essential_orbits)==13

def gap_type(o):
    triples=[]
    for t in o:
        if 0 in t:
            a,b=[x for x in t if x!=0]
            gaps=(a,b-a,N-b)
            triples.append(gaps)
    return min(triples)
null_gaps=sorted(gap_type(o) for o in null_orbits)
assert null_gaps==[(1,5,8),(3,6,5)]

# In a simplicial graph a simple cycle has at least three edges; the 182
# essential empty triangles therefore are exactly the shortest nonzero
# mod-3 homology cycles.
assert sum(v for k,v in cnt.items() if k)!=0
print('VERIFY_OK f=14,91,154,77 H1_F3=1 empty3=210 essential3=182 null3=28 essential_orbits=13 null_orbits=2 null_gaps=1:5:8,3:6:5 classes=91,91 translation=-1 systole=3')
