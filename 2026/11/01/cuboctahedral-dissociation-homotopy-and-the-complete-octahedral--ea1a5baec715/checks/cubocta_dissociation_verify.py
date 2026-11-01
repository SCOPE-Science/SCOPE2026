#!/usr/bin/env python3
"""Reproducible exact chain-level and group-character verifier for cuboctahedral dissociation complex."""
from itertools import combinations, permutations, product
from collections import Counter,defaultdict,deque
from math import factorial

# The cube Q_3 has vertices the three-bit integers. A cuboctahedral vertex is a cube edge.
EDGES = tuple((a,b) for a in range(8) for b in range(a+1,8) if (a^b) in (1,2,4))
assert len(EDGES)==12
ADJ = tuple(sum(1<<j for j,(c,d) in enumerate(EDGES) if i!=j and (a==c or a==d or b==c or b==d)) for i,(a,b) in enumerate(EDGES))
N=len(EDGES)

def is_face(mask):
    return all((ADJ[i]&mask).bit_count()<=1 for i in range(N) if (mask>>i)&1)

# Two independently specified local tests: no induced vertex of degree >= 2, and no prohibited connected triple.
BAD3 = frozenset((1<<i)|(1<<j)|(1<<k) for i in range(N) for j,k in combinations([u for u in range(N) if (ADJ[i]>>u)&1],2))
FACES = frozenset(m for m in range(1,1<<N) if is_face(m))
assert FACES == frozenset(m for m in range(1,1<<N) if not any((m&t)==t for t in BAD3))
print('cube_edges',EDGES)
print('cuboctahedral_edges',sum(a.bit_count() for a in ADJ)//2)
print('forbidden_triples',len(BAD3))
print('nonempty_faces',len(FACES))
print('face_vector',tuple(sum(m.bit_count()==d+1 for m in FACES) for d in range(max(x.bit_count() for x in FACES))))

# A lexicographic fiberwise coordinate Morse matching: across stages, pair each
# remaining face not containing coordinate v with its still-unmatched extension by v.
# All other cover relations are directed down, matched covers up.
ORDER=(2,10,4,6,7,3,11,9,5,8,0,1)
FREE=set(FACES)
PAIRS=[]
for v in ORDER:
    bit=1<<v
    for f in sorted(FREE):
        t=f|bit
        if not f&bit and t in FREE:
            assert f in FREE
            FREE.remove(f)
            FREE.remove(t)
            PAIRS.append((f,t))
CRIT=sorted(FREE)
print('matching_pairs',len(PAIRS),'critical_count',len(CRIT),'critical_dimensions',dict(sorted(Counter(m.bit_count()-1 for m in CRIT).items())))
assert len(PAIRS)*2+len(CRIT)==len(FACES)
assert Counter(m.bit_count()-1 for m in CRIT)=={0:1,3:32}
matched=set(PAIRS)

# Independent mod-two simplicial boundary ranks (not used to infer integral homotopy type).
F_BY_DIM={d:sorted(m for m in FACES if m.bit_count()==d+1) for d in range(5)}
def gf2_rank(cols):
    pivots={}
    for v in cols:
        while v:
            k=v.bit_length()-1
            if k in pivots: v^=pivots[k]
            else: pivots[k]=v; break
    return len(pivots)
ranks=[]
for d in range(1,5):
    low={f:i for i,f in enumerate(F_BY_DIM[d-1])}
    cols=[]
    for high in F_BY_DIM[d]:
        bd=0
        for v in range(N):
            if high>>v&1:bd^=1<<low[high^(1<<v)]
        cols.append(bd)
    ranks.append(gf2_rank(cols))
print('mod2_boundary_ranks',tuple(ranks))
assert ranks==[11,55,109,36]

# Explicit complete directed Hasse DAG test, including all unmatched cover relations.
indeg={f:0 for f in FACES}
succ=defaultdict(list)
edgenum=0
for bigger in sorted(FACES):
    for v in range(N):
        if not bigger>>v&1:continue
        smaller=bigger^(1<<v)
        if smaller not in FACES:continue
        a,b=(smaller,bigger) if (smaller,bigger) in matched else (bigger,smaller)
        succ[a].append(b);indeg[b]+=1;edgenum+=1
queue=deque(f for f in FACES if indeg[f]==0)
visited=0
while queue:
    f=queue.popleft();visited+=1
    for g in succ[f]:
        indeg[g]-=1
        if not indeg[g]:queue.append(g)
print('hasse_incidence',edgenum,'dag_vertices_seen',visited)
assert visited==len(FACES)

# Group action: any cube automorphism is x -> a xor permute_bits(x).
def perm_bits(x,p):
    return sum((((x>>i)&1)<<p[i]) for i in range(3))

def parity(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))

def sign_of_restricted_perm(seq):
    return (-1)**sum(seq[i]>seq[j] for i in range(len(seq)) for j in range(i+1,len(seq)))

def cycle_type(p):
    n=len(p);used=set();lens=[]
    for i in range(n):
        if i in used:continue
        q=i;k=0
        while q not in used:
            used.add(q);q=p[q];k+=1
        lens.append(k)
    return tuple(sorted(lens,reverse=True))

edge_index={e:i for i,e in enumerate(EDGES)}
representatives=(0,1,2,3) # Q3 body diagonals represented by x<4.
rep_index={x:i for i,x in enumerate(representatives)}
records=[]
for a in range(8):
    for p in permutations(range(3)):
        cube_perm=tuple(a^perm_bits(x,p) for x in range(8))
        edge_perm=tuple(edge_index[tuple(sorted((cube_perm[x],cube_perm[y])))] for x,y in EDGES)
        assert len(set(edge_perm))==N
        assert all(bool((ADJ[i]>>j)&1)==bool((ADJ[edge_perm[i]]>>edge_perm[j])&1) for i in range(N) for j in range(N))
        diag_perm=tuple(rep_index[min(cube_perm[x],cube_perm[x]^7)] for x in representatives)
        assert len(set(diag_perm))==4
        ctype=cycle_type(diag_perm)
        det=(-1)**a.bit_count()*parity(p)
        lef=0
        for face in FACES:
            vertices=[i for i in range(N) if face>>i&1]
            image=[edge_perm[i] for i in vertices]
            if set(image)==set(vertices):
                lef+=(-1)**(len(vertices)-1)*sign_of_restricted_perm(image)
        character=1-lef  # reduced homology concentrated in odd dimension 3
        records.append((ctype,det,character,a,p))
assert len(records)==48
assert len({tuple(edge_index[tuple(sorted((a^perm_bits(x,p),a^perm_bits(y,p))))] for x,y in EDGES) for a in range(8) for p in permutations(range(3))})==48
byclass=defaultdict(set);counts=Counter()
for c,s,v,a,p in records:
    byclass[(c,s)].add(v);counts[(c,s)]+=1
assert len(byclass)==10
assert all(len(v)==1 for v in byclass.values())
print('S4_conjugacy_and_determinant_character:')
for (c,s),val in sorted(byclass.items(),key=lambda t:(t[0][0],t[0][1])):
    print(c,s,counts[(c,s)],next(iter(val)))
assert next(v for c,s,v,a,p in records if a==0 and p==(0,1,2))==32
assert sum(v for c,s,v,a,p in records)==48*2
assert (32+next(v for c,s,v,a,p in records if a==7 and p==(0,1,2)))//2==21
assert (32-next(v for c,s,v,a,p in records if a==7 and p==(0,1,2)))//2==11
print('full_group_fixed_dimension',sum(v for c,s,v,a,p in records)//48)

# Signed S4 character table on partitions 4,31,22,211,1111.
S4={
 (1,1,1,1):(1,3,2,3,1),
 (2,1,1):(1,1,0,-1,-1),
 (2,2):(1,-1,2,-1,1),
 (3,1):(1,0,-1,0,1),
 (4,):(1,-1,0,1,-1),
}
names=('(4)','(3,1)','(2,2)','(2,1,1)','(1,1,1,1)')
for sgn in (+1,-1):
    multiplicities=[]
    for rep in range(5):
        total=sum(v*S4[c][rep]*(1 if sgn==1 else det) for c,det,v,a,p in records)
        assert total%48==0
        multiplicities.append(total//48)
    print('irrep_multiplicities_sign',sgn,dict(zip(names,multiplicities)))
    assert all(m>=0 for m in multiplicities)
assert sum((multiplicity*dim for sg in (+1,-1) for dim,multiplicity in zip((1,3,2,3,1),[sum(v*S4[c][i]*(1 if sg==1 else det) for c,det,v,a,p in records)//48 for i in range(5)])))==32
print('ALL_CHECKS_PASS')
