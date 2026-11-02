#!/usr/bin/env python3
"""Exact finite checks for the independence complex of the Pappus graph.
Run: python3 pappus_independence_checker.py (Python 3.9+, standard library)."""
from collections import Counter, defaultdict, deque

EDGES = ((0,1),(0,5),(0,17),(1,2),(1,8),(2,3),(2,13),(3,4),(3,10),
         (4,5),(4,15),(5,6),(6,7),(6,11),(7,8),(7,14),(8,9),
         (9,10),(9,16),(10,11),(11,12),(12,13),(12,17),(13,14),
         (14,15),(15,16),(16,17))
ORDER = (11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12)
N = 18
ADJ = [0]*N
for a,b in EDGES:
    ADJ[a] |= 1<<b
    ADJ[b] |= 1<<a
assert len(EDGES)==27 and all(x.bit_count()==3 for x in ADJ)

FACES = []
def build(face, start, forbidden):
    if face: FACES.append(face)
    for i in range(start,N):
        if not (forbidden>>i)&1:
            build(face|1<<i, i+1, forbidden|ADJ[i]|1<<i)
build(0,0,0)
FACESET = set(FACES)
assert len(FACES)==2597 == len(FACESET)
fvec = Counter(f.bit_count()-1 for f in FACES)
assert tuple(fvec[k] for k in range(9)) == (18,126,438,801,756,348,90,18,2)

# Vertex sweeps: every pair is a cover relation in the face poset.
remaining = FACESET.copy()
matched = {}
for v in ORDER:
    bit=1<<v
    for lo in FACES:
        if lo not in remaining or lo & bit: continue
        hi=lo|bit
        if hi in remaining:
            remaining.remove(lo)
            remaining.remove(hi)
            matched[lo]=hi
critical=Counter(f.bit_count()-1 for f in remaining)
assert len(matched)==1293 and critical=={0:1,4:10}

# Independent directed-Hasse-graph acyclicity test: unmatched arrows point
# from coface to facet; matched arrows are reversed.
indeg={f:0 for f in FACES}
out=defaultdict(list)
count_arrows=0
for hi in FACES:
    bits=hi
    while bits:
        bit=bits&-bits;bits-=bit
        lo=hi^bit
        if not lo:continue
        u,v=(lo,hi) if matched.get(lo)==hi else (hi,lo)
        out[u].append(v)
        indeg[v]+=1
        count_arrows+=1
queue=deque(f for f in FACES if indeg[f]==0)
visited=0
while queue:
    f=queue.popleft();visited+=1
    for h in out[f]:
        indeg[h]-=1
        if indeg[h]==0: queue.append(h)
assert visited==len(FACES) and count_arrows==11430

# An independent mod-2 rank calculation on unmodified simplicial boundaries.
by_dim={d:[] for d in range(9)}
for f in FACES: by_dim[f.bit_count()-1].append(f)
ranks={}
for d in range(1,9):
    ids={f:i for i,f in enumerate(by_dim[d-1])}
    pivot={}
    for f in by_dim[d]:
        x=0;bits=f
        while bits:
            b=bits&-bits;bits-=b
            x ^=1<<ids[f^b]
        while x:
            k=x.bit_length()-1
            if k in pivot:x^=pivot[k]
            else:pivot[k]=x;break
    ranks[d]=len(pivot)
assert ranks == {1:17,2:109,3:329,4:472,5:274,6:74,7:16,8:2}
assert all((len(by_dim[d])-ranks.get(d,0)-ranks.get(d+1,0)) ==
           (10 if d==4 else 1 if d==0 else 0) for d in range(9))

# All graph automorphisms, without graph packages: choose the unmapped vertex
# with most mapped neighbors, then require adjacency and nonadjacency agreement.
def automorphisms():
    mapping={};used=set()
    def rec():
        if len(mapping)==N:
            yield tuple(mapping[i] for i in range(N));return
        u=max((i for i in range(N) if i not in mapping),
              key=lambda i:(sum((ADJ[i]>>j)&1 for j in mapping),-i))
        for v in range(N):
            if v in used:continue
            if any(bool(ADJ[u]&(1<<w)) != bool(ADJ[v]&(1<<mapping[w])) for w in mapping):continue
            mapping[u]=v;used.add(v)
            yield from rec()
            used.remove(v);del mapping[u]
    yield from rec()

def perm_sign(values):
    inversions=sum(values[i]>values[j] for i in range(len(values))
                   for j in range(i+1,len(values)))
    return -1 if inversions&1 else 1

def cycle_type(p):
    seen=set();lengths=[]
    for i in range(N):
        if i in seen:continue
        j=i;length=0
        while j not in seen:
            seen.add(j);j=p[j];length+=1
        lengths.append(length)
    return tuple(sorted(lengths))

def char(p):
    # Ordinary degree-0 Lefschetz trace equals one (connectedness).
    lef=0
    for face,items in zip(FACES,TUPLES):
        mapped=tuple(p[i] for i in items)
        if sum(1<<j for j in mapped)==face:
            lef+=(-1 if len(items)%2==0 else 1)*perm_sign(mapped)
    return lef-1

TUPLES=[tuple(i for i in range(N) if f>>i&1) for f in FACES]
characters=Counter()
class_counts=defaultdict(Counter)
seen=set()
for p in automorphisms():
    assert p not in seen
    seen.add(p)
    c=char(p)
    characters[c]+=1
    class_counts[cycle_type(p)][c]+=1
assert len(seen)==216
assert characters=={10:1,-2:21,-1:72,0:54,1:32,2:36}
assert sum(k*v for k,v in characters.items())==0
assert sum(k*k*v for k,v in characters.items())==432 # two complex irreducible constituents
r=tuple((i+6)%18 for i in range(N))
assert r in seen and char(r)==-2
assert tuple((i+12)%18 for i in range(N)) in seen and char(tuple((i+12)%18 for i in range(N)))==-2
assert class_counts[(3,3,3,3,3,3)] == {-2:12,1:2}
print('PAPPUS_2597_FACES_1293_ACYCLIC_PAIRS_216_FULL_CHARACTERS_OK')
print('f_vector:',[fvec[d] for d in range(9)])
print('boundary_ranks_mod2:',[ranks[d] for d in range(1,9)])
print('critical:',dict(critical),'arrows:',count_arrows)
print('character_histogram:',dict(sorted(characters.items())))
print('character_square_inner_product:',sum(k*k*v for k,v in characters.items())//216)
print('all_cycle_types_and_character_counts:',[(key,dict(val)) for key,val in sorted(class_counts.items())])
