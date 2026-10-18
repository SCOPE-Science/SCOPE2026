#!/usr/bin/env python3
"""Exact standalone verification of the ordinary independence complex of the
20-vertex flower snark. Standard-library Python only; no downloaded data.
"""
from collections import Counter, deque
from functools import lru_cache
from itertools import combinations

N = 20
# Coordinates: a_i=i, b_i=5+i, c_j=10+j, 0<=i<5, 0<=j<10.
EDGE_SET = set()
def edge(u,v):
    assert u != v
    EDGE_SET.add(tuple(sorted((u,v))))
for i in range(5):
    edge(i,5+i)
    edge(i,10+i)
    edge(i,15+i)
    edge(5+i,5+(i+1)%5)
for j in range(10):
    edge(10+j,10+(j+1)%10)
assert len(EDGE_SET)==30
NEIGHBORS=[0]*N
for u,v in EDGE_SET:
    NEIGHBORS[u] |= 1<<v
    NEIGHBORS[v] |= 1<<u
assert [a.bit_count() for a in NEIGHBORS]==[3]*N

# Enumerate *all* 2^20 vertex subsets by a locally checkable recursion.
IS_INDEPENDENT=bytearray(1<<N)
IS_INDEPENDENT[0]=1
FACES=[]
for mask in range(1,1<<N):
    bit=mask&-mask
    v=bit.bit_length()-1
    rest=mask^bit
    if IS_INDEPENDENT[rest] and not(rest&NEIGHBORS[v]):
        IS_INDEPENDENT[mask]=1
        FACES.append(mask)
assert len(FACES)==6113
F_VECTOR=tuple(Counter(x.bit_count()-1 for x in FACES)[j] for j in range(9))
assert F_VECTOR==(20,160,660,1510,1923,1310,450,75,5)
assert sum(F_VECTOR)==len(FACES)

# Deterministic greedy face matching, with vertices considered in order.
REMAINING=set(FACES)
PAIRS=[]
for v in range(N):
    for face in FACES:
        if face not in REMAINING or face & (1<<v):
            continue
        coface=face|(1<<v)
        if coface in REMAINING:
            REMAINING.remove(face)
            REMAINING.remove(coface)
            PAIRS.append((face,coface))
assert len(PAIRS)==3054
CRITICAL=Counter(x.bit_count()-1 for x in REMAINING)
assert CRITICAL=={0:1,4:3,5:1},CRITICAL
assert len(PAIRS)*2+len(REMAINING)==len(FACES)

# Acyclicity certificate: reverse every matched cover relation in Hasse DAG.
MATCHED=set(PAIRS)
INDEX={face:i for i,face in enumerate(FACES)}
ADJ=[[] for _ in FACES]
INDEG=[0]*len(FACES)
COVERS=0
for face in FACES:
    bits=face
    while bits:
        bit=bits&-bits
        bits-=bit
        subface=face^bit
        if subface==0:
            continue
        source,target=(subface,face) if (subface,face) in MATCHED else (face,subface)
        j,k=INDEX[source],INDEX[target]
        ADJ[j].append(k)
        INDEG[k]+=1
        COVERS+=1
assert COVERS==29610
QUEUE=deque(i for i,d in enumerate(INDEG) if not d)
VISITED=0
while QUEUE:
    j=QUEUE.popleft()
    VISITED+=1
    for k in ADJ[j]:
        INDEG[k]-=1
        if INDEG[k]==0:
            QUEUE.append(k)
assert VISITED==len(FACES),('directed cycle',VISITED,len(FACES))

# Signed simplicial boundary for lexicographically oriented ordered vertices.
def boundary(face):
    result=[]
    parity=1
    bits=face
    while bits:
        bit=bits&-bits
        bits-=bit
        result.append((face^bit,parity))
        parity=-parity
    return result

LOW_TO_HIGH=dict(PAIRS)
HIGH_TO_LOW={higher:lower for lower,higher in PAIRS}
CRIT4=sorted(x for x in REMAINING if x.bit_count()==5)
CRIT5=sorted(x for x in REMAINING if x.bit_count()==6)
assert CRIT4==[140864,280736,534688]
assert CRIT5==[696896]

@lru_cache(maxsize=None)
def project_degree_four(cell):
    # Algebraic Morse projection: paired higher four-cells project to 0;
    # each lower four-cell is eliminated with its upper five-cell.
    assert cell.bit_count()==5
    if cell in REMAINING:
        return {cell:1}
    if cell in HIGH_TO_LOW:
        return {}
    upper=LOW_TO_HIGH[cell]
    incidence=dict(boundary(upper))
    pivot=incidence.pop(cell)
    assert abs(pivot)==1
    total=Counter()
    for lower,coeff in incidence.items():
        for basis,value in project_degree_four(lower).items():
            total[basis]-=coeff*value//pivot
    return {basis:coeff for basis,coeff in total.items() if coeff}

MORSE_BOUNDARY=Counter()
for f,sign in boundary(CRIT5[0]):
    for basis,value in project_degree_four(f).items():
        MORSE_BOUNDARY[basis]+=sign*value
MORSE_BOUNDARY={CRIT4.index(cell):value for cell,value in MORSE_BOUNDARY.items() if value}
assert MORSE_BOUNDARY=={0:1,2:-1},MORSE_BOUNDARY
# The only nonzero reduced Morse boundary is primitive: 5 -> 4.
# The 5-cell kills one 4-sphere homotopy summand, leaving two.

# The graph is triangle-free; every five-cycle is therefore induced.
assert all(not (tuple(sorted((i,j))) in EDGE_SET and tuple(sorted((j,k))) in EDGE_SET and tuple(sorted((i,k))) in EDGE_SET) for i,j,k in combinations(range(N),3))

# Unique 5-cycle provides a graph-intrinsic characterization of the b-ring.
FIVE_CYCLES=[]
for sub in combinations(range(N),5):
    subset=sum(1<<v for v in sub)
    if all((NEIGHBORS[v]&subset).bit_count()==2 for v in sub):
        todo=[sub[0]];visited={sub[0]}
        while todo:
            u=todo.pop()
            for v in sub:
                if (NEIGHBORS[u]>>v)&1 and v not in visited:
                    visited.add(v)
                    todo.append(v)
        if len(visited)==5:
            FIVE_CYCLES.append(sub)
assert FIVE_CYCLES==[(5,6,7,8,9)],FIVE_CYCLES

# Full automorphism group: each symmetry acts dihedrally on the unique
# b-five-cycle. Once b's and their respective a-neighbors are fixed,
# the ten-cycle permits only identity or a global c_i <-> c_(5+i) swap.
# Hence |Aut| <= 10*2. Exhibit 20 different automorphisms below.
def compose(f,g):
    return tuple(f[g[i]] for i in range(N))
def power(p,k):
    ans=tuple(range(N))
    for _ in range(k):
        ans=compose(p,ans)
    return ans
r=list(range(N));s=list(range(N))
for i in range(5):
    r[i]=(i+1)%5
    r[5+i]=5+(i+1)%5
    s[i]=(-i)%5
    s[5+i]=5+(-i)%5
for j in range(10):
    r[10+j]=10+(j+1)%10
    s[10+j]=10+(-j)%10
r=tuple(r);s=tuple(s)
def is_automorphism(p):
    return {tuple(sorted((p[u],p[v]))) for u,v in EDGE_SET}==EDGE_SET
assert is_automorphism(r) and is_automorphism(s)
assert power(r,10)==tuple(range(N))
assert power(r,5)!=tuple(range(N))
assert compose(s,s)==tuple(range(N))
assert compose(s,compose(r,s))==power(r,9)
GROUP=[power(r,k) for k in range(10)]+[compose(s,power(r,k)) for k in range(10)]
assert len(set(GROUP))==20
assert all(is_automorphism(p) for p in GROUP)

def reduced_lefschetz(p):
    # Reduced cellular Lefschetz number: empty augmented simplex contributes -1.
    answer=-1
    for face in FACES:
        orig=[i for i in range(N) if face>>i&1]
        target=[p[i] for i in orig]
        if sorted(target)!=orig:
            continue
        inversions=sum(target[i]>target[j] for i in range(len(target)) for j in range(i+1,len(target)))
        answer+=(-1)**(len(orig)-1+inversions)
    return answer
TR_R=[reduced_lefschetz(power(r,k)) for k in range(10)]
TR_SR=[reduced_lefschetz(compose(s,power(r,k))) for k in range(10)]
assert TR_R==[2 if k%2==0 else 0 for k in range(10)]
assert TR_SR==[2 if k%2==0 else 0 for k in range(10)]
# With reduced homology only in degree four, these are H_4 character values,
# namely the character of 1 plus epsilon with epsilon(r)=-1, epsilon(s)=+1.
# Cross-identify the presentation with the independently published Sage
# graph6 label using an explicit graph isomorphism (no graph library needed).
G6='ShCGHC@?GGg@?@?Gp?K??C?CA?G?_G?Cc'
assert ord(G6[0])-63==N
bits=''.join(format(ord(c)-63,'06b') for c in G6[1:])
canonical_edges=set()
cursor=0
for j in range(1,N):
    for i in range(j):
        if bits[cursor]=='1':
            canonical_edges.add((i,j))
        cursor+=1
CANONICAL_MAP=(0,12,9,6,3,15,19,18,17,16,1,11,10,5,4,14,13,8,7,2)
assert len(set(CANONICAL_MAP))==N
assert {tuple(sorted((CANONICAL_MAP[u],CANONICAL_MAP[v]))) for u,v in EDGE_SET}==canonical_edges
assert len(canonical_edges)==30

print('VERIFY_OK_FLOWER_SNARK_INDEPENDENCE_HOMOTOPY_AND_FULL_DIHEDRAL_CHARACTER')
print('GRAPH_N_M',N,len(EDGE_SET),'UNIQUE_5_CYCLE',FIVE_CYCLES[0])
print('F_VECTOR',F_VECTOR,'FACES',len(FACES))
print('MORSE_PAIRS',len(PAIRS),'HASSE_COVERS',COVERS,'ACYCLIC_VERTICES',VISITED)
print('CRITICAL_DIMS',dict(CRITICAL),'CRITICAL_FIVE_TO_FOUR',MORSE_BOUNDARY)
print('HOMOTOPY_WEDGE_TWO_S4')
print('AUTOMORPHISM_GROUP_D10_ORDER',len(GROUP))
print('H4_TRACES_ROTATIONS',tuple(TR_R))
print('H4_TRACES_REFLECTIONS',tuple(TR_SR))
print('H4_Q_MODULE_TRIVIAL_PLUS_ROTATION_SIGN')
