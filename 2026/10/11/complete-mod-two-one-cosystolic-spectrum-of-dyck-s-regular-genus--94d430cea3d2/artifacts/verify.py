from itertools import combinations
from collections import Counter, deque

FACETS = [
(1,2,4),(1,2,10),(1,3,5),(1,3,11),(1,4,9),(1,5,8),(1,8,10),(1,9,11),
(2,4,7),(2,5,6),(2,5,12),(2,6,10),(2,7,11),(2,11,12),
(3,4,6),(3,4,12),(3,5,7),(3,6,11),(3,7,10),(3,10,12),
(4,6,9),(4,7,8),(4,8,12),(5,6,8),(5,7,9),(5,9,12),
(6,8,11),(6,9,10),(7,8,10),(7,9,11),(8,11,12),(9,10,12)
]
EDGES = sorted({tuple(sorted(e)) for f in FACETS for e in combinations(f,2)})
EI = {e:i for i,e in enumerate(EDGES)}
FSET = {tuple(sorted(f)) for f in FACETS}

def rref(rows,n):
    rows=[x for x in rows if x]
    piv=[]; i=0
    for c in range(n):
        j=next((j for j in range(i,len(rows)) if (rows[j]>>c)&1),None)
        if j is None: continue
        rows[i],rows[j]=rows[j],rows[i]
        for k in range(len(rows)):
            if k!=i and ((rows[k]>>c)&1): rows[k]^=rows[i]
        piv.append(c); i+=1
        if i==len(rows): break
    return rows[:i],piv

def rank(vs): return len(rref(vs,48)[1])

tri=[]
for f in FACETS:
    row=0
    for e in combinations(f,2): row ^= 1<<EI[tuple(sorted(e))]
    tri.append(row)
rr,piv=rref(tri,48)
free=[c for c in range(48) if c not in piv]
Z=[]
for fc in free:
    v=1<<fc
    for row,pc in zip(rr,piv):
        if (row>>fc)&1: v |= 1<<pc
    Z.append(v)
Bgens=[]
for a in range(1,13):
    v=0
    for i,(x,y) in enumerate(EDGES):
        if (x==a) ^ (y==a): v |= 1<<i
    Bgens.append(v)
B,_=rref(Bgens,48)
basis=list(B)
for z in Z:
    if rank(basis+[z])>len(basis): basis.append(z)
assert len(EDGES)==48 and len(FACETS)==32
assert len(piv)==31 and len(Z)==17 and len(B)==11 and len(basis)==17

vec=[0]*(1<<17)
mins=[99]*64; counts=[0]*64; supports=[[] for _ in range(64)]
for m in range(1,1<<17):
    lb=m & -m; j=lb.bit_length()-1
    vec[m]=vec[m^lb]^basis[j]
for m,v in enumerate(vec):
    c=m>>11; w=v.bit_count()
    if w<mins[c]: mins[c]=w; counts[c]=1; supports[c]=[v]
    elif w==mins[c]: counts[c]+=1; supports[c].append(v)
assert Counter((mins[c],counts[c]) for c in range(1,64)) == Counter({(6,1):16,(10,4):24,(12,8):6,(14,18):16,(16,12):1})

def perm(cycles):
    p={i:i for i in range(1,13)}
    for cyc in cycles:
        for a,b in zip(cyc,cyc[1:]+cyc[:1]): p[a]=b
    return tuple(p[i] for i in range(1,13))
G0=[
perm([(1,12),(2,3),(6,7),(8,9)]),
perm([(1,3,5,7,9,11),(2,4,6,8,10,12)]),
perm([(1,3),(2,12),(4,10),(5,11),(6,8),(7,9)]),
perm([(4,10),(5,11),(6,7),(8,9)])]
def compose(p,q): return tuple(p[q[i]-1] for i in range(12))
idp=tuple(range(1,13)); G={idp}; q=deque([idp])
while q:
    h=q.popleft()
    for g in G0:
        z=compose(g,h)
        if z not in G: G.add(z); q.append(z)
assert len(G)==192
for p in G:
    assert {tuple(sorted(p[x-1] for x in f)) for f in FACETS}==FSET

def act(v,p):
    out=0
    for i,(a,b) in enumerate(EDGES):
        if (v>>i)&1: out ^= 1<<EI[tuple(sorted((p[a-1],p[b-1])))]
    return out
class_of={v:(m>>11) for m,v in enumerate(vec)}
reps={c:vec[c<<11] for c in range(64)}
action={p:{c:class_of[act(reps[c],p)] for c in range(64)} for p in G}
unseen=set(range(1,64)); orbs=[]
while unseen:
    c=min(unseen); o={action[p][c] for p in G}; orbs.append(o); unseen-=o
profile=sorted((mins[next(iter(o))],len(o),counts[next(iter(o))]) for o in orbs)
assert profile==[(6,16,1),(10,24,4),(12,6,8),(14,16,18),(16,1,12)]

support_profile=[]
for o in sorted(orbs,key=lambda o: mins[next(iter(o))]):
    w=mins[next(iter(o))]
    union=set().union(*(set(supports[c]) for c in o))
    rem=set(union); parts=[]
    while rem:
        s=next(iter(rem)); oo={act(s,p) for p in G} & union
        parts.append(len(oo)); rem-=oo
    support_profile.append((w,len(union),sorted(parts)))
assert support_profile==[(6,16,[16]),(10,96,[48,48]),(12,48,[24,24]),(14,288,[96,192]),(16,12,[12])]

print('VERIFY_OK')
print('f_vector=12,48,32')
print('rank_triangle_cocycle_equations=31')
print('dim_Z1_F2=17')
print('dim_B1_F2=11')
print('dim_H1_cohomology_F2=6')
print('all_cocycles_exhausted=131072')
print('nonzero_class_orbits=(weight,class_orbit,minimizers_per_class)=6:16:1;10:24:4;12:6:8;14:16:18;16:1:12')
print('support_orbits=6:16[16];10:96[48,48];12:48[24,24];14:288[96,192];16:12[12]')
print('automorphism_group_order=192')
