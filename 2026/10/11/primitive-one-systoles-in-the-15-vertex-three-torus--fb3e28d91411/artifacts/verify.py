from itertools import permutations, combinations
from collections import Counter
from math import gcd

N=15

def add(a,b): return tuple(x+y for x,y in zip(a,b))
def neg(a): return tuple(-x for x in a)
def canon(v): return min(v,neg(v))

def det3(a,b,c):
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
           -a[1]*(b[0]*c[2]-b[2]*c[0])
           +a[2]*(b[0]*c[1]-b[1]*c[0]))

# Kühnel-Lassmann d=3 difference construction on Z/15.
facets=set()
for i in range(N):
    for p,q,r in permutations((1,2,4)):
        assert p+q+r==7
        facets.add(tuple(sorted((i,(i+p)%N,(i+p+q)%N,(i+7)%N))))
assert len(facets)==90
faces=[set() for _ in range(4)]
for F in facets:
    for k in range(1,5):
        for s in combinations(F,k): faces[k-1].add(tuple(sorted(s)))
assert [len(x) for x in faces]==[15,105,180,90]

# Standard Freudenthal cover of R^3 with vertex label phi(a,b,c)=a+2b+4c mod 15.
# The deck lattice L=ker(phi) has basis b1=(15,0,0), b2=(-2,1,0), b3=(-4,0,1).
steps={0:(0,0,0),1:(1,0,0),2:(0,1,0),3:(1,1,0),4:(0,0,1),5:(1,0,1),6:(0,1,1),7:(1,1,1)}
for d in range(8,15): steps[d]=neg(steps[15-d])
def edge_lift(a,b): return steps[(b-a)%15]
def lattice_coords(v):
    a,b,c=v
    num=a+2*b+4*c
    assert num%15==0
    return (num//15,b,c)
def tri_class(T):
    a,b,c=T
    v=add(add(edge_lift(a,b),edge_lift(b,c)),edge_lift(c,a))
    return lattice_coords(v)

# Every actual triangle has zero deck displacement.
for T in faces[2]: assert tri_class(T)==(0,0,0)

missing=[T for T in combinations(range(N),3) if T not in faces[2]]
assert len(missing)==275
classes=Counter(canon(tri_class(T)) for T in missing)
assert len(classes)==7
assert Counter(classes.values())==Counter({45:6,5:1})
assert all(any(x for x in c) for c in classes)
assert all(gcd(gcd(abs(c[0]),abs(c[1])),abs(c[2]))==1 for c in classes)
expected_classes={
 (0,-1,0),(0,-1,1),(0,-2,1),(-1,0,-3),
 (-1,-2,-2),(-1,-1,-3),(-1,-3,-2)
}
assert set(classes)==expected_classes
assert classes[(-1,0,-3)]==5
exceptional={T for T in missing if canon(tri_class(T))==(-1,0,-3)}
assert exceptional=={tuple(sorted((i,(i+5)%15,(i+10)%15))) for i in range(5)}

# The seven shortest classes generate the full deck lattice (hence include an integral basis).
cs=list(classes)
assert any(abs(det3(a,b,c))==1 for a,b,c in combinations(cs,3))

# Translation orbits.
miss=set(missing); seen=set(); torb=[]
for T in missing:
    if T in seen: continue
    O={tuple(sorted((x+k)%15 for x in T)) for k in range(15)}
    assert O <= miss
    seen |= O; torb.append(O)
assert Counter(map(len,torb))==Counter({15:18,5:1})

# Full automorphism group from Köhler-Lutz Table 13 / Kühnel-Lassmann affine group.
def perm_from_cycles(cycles):
    p=list(range(15))
    for cyc in cycles:
        z=[x-1 for x in cyc]
        for a,b in zip(z,z[1:]+z[:1]): p[a]=b
    return tuple(p)
def comp(p,q): return tuple(p[q[i]] for i in range(15))
g1=tuple((i+1)%15 for i in range(15))
g2=perm_from_cycles([(1,7,4,13),(2,14,8,11),(3,6,12,9)])
g3=perm_from_cycles([(1,11),(2,7),(4,14),(5,10),(8,13)])
G={tuple(range(15))}; frontier=list(G)
while frontier:
    a=frontier.pop()
    for b in (g1,g2,g3):
        c=comp(b,a)
        if c not in G: G.add(c); frontier.append(c)
assert len(G)==120
for p in G:
    assert {tuple(sorted(p[x] for x in F)) for F in facets}==facets

seen=set(); gorb=[]
for T in missing:
    if T in seen: continue
    O={tuple(sorted(p[x] for x in T)) for p in G}
    assert O<=miss
    seen |= O; gorb.append(O)
assert Counter(map(len,gorb))==Counter({5:1,30:1,60:2,120:1})
reps=sorted((len(O),min(O)) for O in gorb)
assert reps==[(5,(0,5,10)),(30,(0,3,6)),(60,(0,1,2)),(60,(0,1,4)),(120,(0,1,6))]

# Verify the induced action on the seven unoriented classes is well-defined from all representatives.
byclass={c:[T for T in missing if canon(tri_class(T))==c] for c in classes}
def image_class(p,T): return canon(tri_class(tuple(sorted(p[x] for x in T))))
class_action={}
for p in G:
    for c,Ts in byclass.items():
        vals={image_class(p,T) for T in Ts}
        assert len(vals)==1
        class_action[(p,c)]=next(iter(vals))
seen=set(); corbits=[]
for c in classes:
    if c in seen: continue
    O={class_action[(p,c)] for p in G}
    seen |= O; corbits.append(O)
assert sorted(map(len,corbits))==[1,2,4]
assert any(O=={(-1,0,-3)} for O in corbits)

# Mod-p chain ranks independently recover beta_1=3.
edges=sorted(faces[1]); triangles=sorted(faces[2])
edge_index={e:i for i,e in enumerate(edges)}
def rank_mod(mat,p):
    if not mat: return 0
    A=[row[:] for row in mat]
    m,n=len(A),len(A[0]); r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]%p),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(A[i][j]-f*A[r][j])%p for j in range(n)]
        r+=1
        if r==m: break
    return r
# d1 rows vertices, cols edges
d1=[[0]*len(edges) for _ in range(15)]
for j,(a,b) in enumerate(edges): d1[a][j]=-1; d1[b][j]=1
# d2 rows edges, cols triangles
d2=[[0]*len(triangles) for _ in range(len(edges))]
for j,(a,b,c) in enumerate(triangles):
    for e,s in [((b,c),1),((a,c),-1),((a,b),1)]: d2[edge_index[e]][j]=s
for p in (2,3,5,7):
    assert rank_mod(d1,p)==14
    assert rank_mod(d2,p)==88

print('VERIFY_OK f=15,105,180,90 H1_rank=3 missing3=275 essential3=275 primitive3=275 classes=7 multiplicities=45x6+5 translation_orbits=15x18+5 full_group=120 systole_orbits=5,30,60,60,120 class_orbits=1,2,4 exceptional=0-5-10')
