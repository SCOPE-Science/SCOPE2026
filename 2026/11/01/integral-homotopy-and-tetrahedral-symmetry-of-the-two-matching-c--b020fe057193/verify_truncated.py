#!/usr/bin/env python3
"""Finite integral and symmetry certificate for the truncated-tetrahedral two-matching complex.
Requires Python 3.10+ standard library only. Rebuilds all simplices and the discrete-Morse certificate.
"""
import itertools
import json
from collections import Counter, defaultdict, deque
from functools import lru_cache

V = tuple((i,j) for i in range(4) for j in range(4) if i != j)
VI = {v:k for k,v in enumerate(V)}
E = []
for i in range(4):
    for j,k in itertools.combinations([t for t in range(4) if t != i],2):
        E.append(tuple(sorted((VI[i,j],VI[i,k]))))
for i,j in itertools.combinations(range(4),2):
    E.append(tuple(sorted((VI[i,j],VI[j,i]))))
E = tuple(sorted(E))
EI = {e:i for i,e in enumerate(E)}
assert len(V)==12 and len(E)==18 and len(set(E))==18
ADJ = tuple(sum(1 << k for k,(u,w) in enumerate(E) if v in (u,w)) for v in range(12))
assert all(x.bit_count()==3 for x in ADJ)

# Exhaustive two-method membership agreement on ALL 2**18 edge selections.
faces=[]; counts=Counter()
for mask in range(1 << len(E)):
    incidence = all((mask & a).bit_count() <= 2 for a in ADJ)
    degree = [0]*12
    for k,(u,v) in enumerate(E):
        if mask & (1 << k):
            degree[u] += 1
            degree[v] += 1
    explicit = max(degree)<=2
    assert incidence == explicit
    if incidence:
        faces.append(mask)
        counts[mask.bit_count()-1] += 1
assert len(faces)==69075
assert [counts[i] for i in range(12)]==[18,153,804,2880,7326,13382,17352,15402,8698,2709,342,8]
face_set = set(faces)

# Repeated lexicographic toggles on each of the 18 edge-vertices.
remaining=face_set.copy();low_to_high={}
for i in range(len(E)):
    pairs=[]
    for s in remaining:
        if not (s & (1 << i)) and (s | (1 << i)) in remaining:
            pairs.append((s,s | (1 << i)))
    for a,b in pairs:
        remaining.remove(a)
        remaining.remove(b)
        low_to_high[a]=b
critical = remaining
assert len(low_to_high)==34533
assert Counter(s.bit_count()-1 for s in critical)=={8:7,9:2}
assert 0 in low_to_high
high_to_low={hi:lo for lo,hi in low_to_high.items()}

def oriented_boundary(mask):
    sign=1; bits=mask
    while bits:
        bit = bits & -bits
        yield mask ^ bit,sign
        bits -= bit
        sign = -sign

# Complete DAG check, not sampled paths.
indegree={s:0 for s in faces};outgoing=defaultdict(list);arcs=0
for hi in faces:
    for lo,_ in oriented_boundary(hi):
        if lo not in face_set:continue
        src,dst=(lo,hi) if low_to_high.get(lo)==hi else (hi,lo)
        outgoing[src].append(dst); indegree[dst]+=1; arcs+=1
queue=deque(s for s in faces if indegree[s]==0); visited=0
while queue:
    s=queue.popleft();visited+=1
    for w in outgoing[s]:
        indegree[w]-=1
        if indegree[w]==0:queue.append(w)
assert arcs==485088 and visited==len(faces), (arcs,visited)
del indegree,outgoing,queue

# Algebraic Morse projection: for each lower matched cell a paired with b,
# project a = -[b:a]^{-1} sum_{c!=a} [b:c] project(c).
@lru_cache(None)
def project(s):
    if s in critical:return {s:1}
    if s in high_to_low:return {}
    hi=low_to_high[s]
    sgn=next(sign for lo,sign in oriented_boundary(hi) if lo==s)
    result=defaultdict(int)
    for lo,sign in oriented_boundary(hi):
        if lo==s:continue
        for crit,multiple in project(lo).items():
            result[crit]-=sgn*sign*multiple
    return {c:v for c,v in result.items() if v}

rows=sorted(s for s in critical if s.bit_count()==9)
cols=sorted(s for s in critical if s.bit_count()==10)
index={s:i for i,s in enumerate(rows)}
matrix=[[0]*len(cols) for _ in rows]
for j,hi in enumerate(cols):
    for lo,sgn in oriented_boundary(hi):
        for crit,coeff in project(lo).items():
            assert crit in index
            matrix[index[crit]][j]+=sgn*coeff
# Exact two-column rank and primitive minor, so unit invariant factors.
nonzero_minor = None
for i,j in itertools.combinations(range(len(rows)),2):
    det=matrix[i][0]*matrix[j][1]-matrix[j][0]*matrix[i][1]
    if abs(det)==1:
        nonzero_minor={'row_indices':[i,j],'determinant':det};break
assert nonzero_minor is not None
assert len(rows)==7 and len(cols)==2

# Completely separate direct simplicial F_2 ranks for the full chain complex.
# Row dictionaries are bitset-encoded; independent of Morse construction.
by_degree=defaultdict(list)
for s in faces:
    if s:by_degree[s.bit_count()-1].append(s)
boundary_ranks={}
for k in range(1,12):
    lows={s:i for i,s in enumerate(by_degree[k-1])}
    pivots={}
    for hi in by_degree[k]:
        vec=0
        for lo,_ in oriented_boundary(hi):vec ^= 1<<lows[lo]
        while vec:
            pivot=vec.bit_length()-1
            if pivot in pivots:vec ^=pivots[pivot]
            else:pivots[pivot]=vec;break
    boundary_ranks[k]=len(pivots)
betti={}
for k in range(12):
    rank=boundary_ranks.get(k,0)
    up=boundary_ranks.get(k+1,0)
    b=len(by_degree[k])-rank-up
    if k==0:b-=1
    if b:betti[k]=b
assert betti=={8:5},betti

# S_4 action on signed simplicial-chain Lefschetz numbers.
def cycle_type(p):
    unvisited=set(range(4));out=[]
    while unvisited:
        i=min(unvisited);j=i;k=0
        while j in unvisited:
            unvisited.remove(j);k+=1;j=p[j]
        out.append(k)
    return '-'.join(map(str,sorted(out,reverse=True)))

def parity(items):
    n=0
    for i in range(len(items)):
        for j in range(i+1,len(items)):
            if items[i]>items[j]:n+=1
    return -1 if n%2 else 1

characters=defaultdict(set);class_counts=Counter()
for p in itertools.permutations(range(4)):
    vertex_perm=[VI[p[i],p[j]] for i,j in V]
    ep=[EI[tuple(sorted((vertex_perm[u],vertex_perm[v])))] for u,v in E]
    lefschetz=0
    for s in faces:
        if not s:continue
        inds=[i for i in range(18) if s & (1<<i)]
        imgs=[ep[i] for i in inds]
        if sum(1<<j for j in imgs)==s:
            lefschetz+=parity(imgs)*(-1 if (len(inds)-1)%2 else 1)
    t=cycle_type(p)
    characters[t].add(lefschetz - 1)  # χ_8 = reduced Lefschetz, as 8 is even.
    class_counts[t]+=1
assert all(len(v)==1 for v in characters.values())
character={k:next(iter(v)) for k,v in sorted(characters.items())}
assert character=={'1-1-1-1':5,'2-1-1':-1,'2-2':1,'3-1':2,'4':1},character
assert class_counts=={'1-1-1-1':1,'2-1-1':6,'2-2':3,'3-1':8,'4':6}
irreps={
  'trivial':{'1-1-1-1':1,'2-1-1':1,'2-2':1,'3-1':1,'4':1},
  'sign':{'1-1-1-1':1,'2-1-1':-1,'2-2':1,'3-1':1,'4':-1},
  'standard':{'1-1-1-1':3,'2-1-1':1,'2-2':-1,'3-1':0,'4':-1},
  'sign_twisted_standard':{'1-1-1-1':3,'2-1-1':-1,'2-2':-1,'3-1':0,'4':1},
  'two_dimensional':{'1-1-1-1':2,'2-1-1':0,'2-2':2,'3-1':-1,'4':0}
}
multiplicities={name:sum(class_counts[t]*character[t]*ir[t] for t in class_counts)//24 for name,ir in irreps.items()}
assert multiplicities=={'trivial':1,'sign':1,'standard':0,'sign_twisted_standard':1,'two_dimensional':0}

print(json.dumps({
 'marker':'TRUNCATED_TETRAHEDRON_TWO_MATCHING_INTEGRAL_S4_VERIFIED',
 'vertices':12,'edges':18,'subsets_checked':1<<18,'faces_including_empty':len(faces),
 'f_vector_0_to_11':[counts[i] for i in range(12)],
 'morse_pairs':len(low_to_high),'hasse_incidences':arcs,'acyclic_nodes_visited':visited,
 'critical_by_dimension':dict(sorted(Counter(s.bit_count()-1 for s in critical).items())),
 'critical_face_bitmasks':{'degree_8':rows,'degree_9':cols},
 'morse_boundary_9_to_8':matrix,'unit_minor':nonzero_minor,
 'direct_f2_boundary_ranks':boundary_ranks,'direct_reduced_f2_betti':betti,
 's4_class_cardinalities':class_counts,'s4_homology_character':character,
 's4_multiplicities':multiplicities,
 'homotopy':'wedge of five eight-spheres','integral_homology':'Z^5 in degree eight; zero otherwise'
},indent=2,sort_keys=True))
