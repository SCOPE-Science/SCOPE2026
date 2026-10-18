#!/usr/bin/env python3
"""Self-contained finite proof checks for the higher-independence filtration of Petersen's graph.
The mathematical graph, enumerations, Morse pairings, incidence signs and persistence
are defined from scratch. Requires Python 3 standard library only.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque

VERTICES = tuple(combinations(range(5),2))
N = len(VERTICES)
EDGES = {(i,j) for i in range(N) for j in range(i) if set(VERTICES[i]).isdisjoint(VERTICES[j])}
assert len(EDGES) == 15
NEIGH = [0]*N
for i,j in EDGES:
    NEIGH[i] |= 1<<j
    NEIGH[j] |= 1<<i

def max_component(s):
    rest=s
    best=0
    while rest:
        part=rest & -rest
        fringe=part
        while fringe:
            nb=0
            while fringe:
                low=fringe & -fringe
                fringe-=low
                nb |= NEIGH[low.bit_length()-1]
            fringe=nb & s & ~part
            part |= fringe
        best=max(best,part.bit_count())
        rest &= ~part
    return best

level={s:max(1,max_component(s)) for s in range(1<<N)}
assert level[0]==1 and max(level.values())==10
ORDERS={
    1:tuple(range(10)),2:tuple(range(10)),
    3:(6,2,3,0,9,5,7,4,1,8),
    4:(1,2,6,8,4,7,3,0,5,9),
    5:(0,7,8,4,6,5,3,9,2,1),
    6:tuple(range(10)),7:tuple(range(10)),
    8:tuple(range(10)),9:tuple(range(10)),
}
EXPECTED={
    1:{0:1,2:4},2:{0:1,3:1},3:{0:1,3:1},
    4:{0:1,3:15,4:4},5:{0:1,4:61},6:{0:1,5:74},
    7:{0:1,6:36},8:{0:1,7:9},9:{0:1,8:1}
}

def morse_faces(r,order):
    F={s for s in range(1,1<<N) if level[s]<=r}
    unmatched=set(F)
    matching=[]
    for v in order:
        bit=1<<v
        for lo in sorted(unmatched):
            if lo not in unmatched or lo&bit:continue
            hi=lo|bit
            if hi in unmatched:
                unmatched.remove(lo);unmatched.remove(hi)
                matching.append((lo,hi))
    return F,unmatched,matching

def check_acyclic(F,matching):
    matched=set(matching)
    indegree={s:0 for s in F}
    outgoing=defaultdict(list)
    for hi in F:
        if hi.bit_count()<=1:continue
        bitset=hi
        while bitset:
            bit=bitset&-bitset;bitset-=bit
            lo=hi^bit
            # Matched cover reverses the downward face-poset orientation.
            src,dst=(lo,hi) if (lo,hi) in matched else (hi,lo)
            outgoing[src].append(dst)
            indegree[dst]+=1
    queue=deque(s for s in F if not indegree[s]);visited=0
    while queue:
        src=queue.popleft();visited+=1
        for dst in outgoing[src]:
            indegree[dst]-=1
            if indegree[dst]==0:queue.append(dst)
    return visited==len(F)

# Signed codimension-one incidence from the increasing vertex ordering.
def signed_boundary(s):
    result={}
    bitset=s;pos=0
    while bitset:
        bit=bitset&-bitset;bitset-=bit
        result[s^bit]=1 if pos%2==0 else -1
        pos+=1
    return result

def morse_boundary4(F,critical,matching):
    # Restrict to dimension-(4 -> 3) chain differential.  The algebraic
    # cancellation of each noncritical degree-(3,4) face pair produces exactly
    # the integral Morse differential between critical degrees four and three.
    uppers=sorted(s for s in F if s.bit_count()==5)
    lowers={s for s in F if s.bit_count()==4}
    B={hi:signed_boundary(hi) for hi in uppers}
    assert all(set(B[s]).issubset(lowers) for s in uppers)
    pairs=[(lo,hi) for lo,hi in matching if lo.bit_count()==4]
    liveup=set(uppers)
    for lo,hi in pairs:
        assert hi in liveup
        pivot=B[hi].get(lo,0)
        assert abs(pivot)==1,('nonunit matched incidence',lo,hi,pivot)
        bh=B[hi]
        for other in tuple(liveup):
            if other==hi:continue
            coeff=B[other].get(lo,0)
            if not coeff:continue
            fac=coeff//pivot
            for face,num in bh.items():
                nxt=B[other].get(face,0)-fac*num
                if nxt:B[other][face]=nxt
                else:B[other].pop(face,None)
        liveup.remove(hi);del B[hi]
    critup=sorted(s for s in critical if s.bit_count()==5)
    critlo=sorted(s for s in critical if s.bit_count()==4)
    assert set(critup).issubset(liveup)
    # Other remaining degree-four columns are paired upward with degree-five cells;
    # degree-three rows paired downward with degree-two cells are discarded.
    A=[[B[hi].get(lo,0) for hi in critup] for lo in critlo]
    # This displayed 4x4 minor is a unit over Z; in particular, the
    # column lattice is primitive and the integral Smith invariants are all 1.
    minor=[A[i] for i in (1,3,8,12)]
    def determinant(M):
        if len(M)==1:return M[0][0]
        return sum((-1)**j*M[0][j]*determinant(
            [row[:j]+row[j+1:] for row in M[1:]])
            for j in range(len(M)))
    d=determinant(minor)
    return A,d

print('Petersen edges',len(EDGES))
for r in range(1,10):
    F,crit,matching=morse_faces(r,ORDERS[r])
    assert len(F)==2*len(matching)+len(crit)
    assert all(lo in F and hi in F and hi.bit_count()==lo.bit_count()+1
               and (hi^lo).bit_count()==1 for lo,hi in matching)
    assert check_acyclic(F,matching),('cyclic matching',r)
    vector=dict(Counter(s.bit_count()-1 for s in crit))
    assert vector==EXPECTED[r],(r,vector,EXPECTED[r])
    print('r',r,'faces',len(F),'matched',len(matching),'critical',sorted(vector.items()),'acyclic True')
    if r==4:
        A,det=morse_boundary4(F,crit,matching)
        assert len(A)==15 and all(len(row)==4 for row in A) and abs(det)==1
        print('integral Morse boundary (15 rows x 4 columns):')
        for row in A: print(*row)
        print('unit 4-by-4 minor determinant:',det)

# All parameter levels are filtered by maximum connected induced-component size.
# Augment with the empty face in dimension -1: vertices have augmented boundary
# to the empty face, yielding REDUCED homology persistently.
order=sorted(range(1<<N), key=lambda s:(level[s],s.bit_count(),s))
index={s:i for i,s in enumerate(order)}
assert len(order)==1024
pivots={};empty_columns=[];birthdeath=[]
for j,s in enumerate(order):
    chain=0
    if s:
        for v in range(N):
            if s&(1<<v):chain^=1<<index[s^(1<<v)]
    while chain:
        p=chain.bit_length()-1
        if p not in pivots:break
        chain ^= pivots[p]
    if chain:
        p=chain.bit_length()-1
        pivots[p]=chain
        birthdeath.append((p,j))
    else:empty_columns.append(j)

bars=Counter()
paired={p for p,j in birthdeath}
for p,j in birthdeath:
    simplex=order[p];coface=order[j]
    b,d=level[simplex],level[coface]
    if b!=d:bars[(simplex.bit_count()-1,b,d)]+=1
for z in empty_columns:
    if z not in paired:
        simplex=order[z]
        bars[(simplex.bit_count()-1,level[simplex],11)]+=1
EXPECTED_BARS={
    (2,1,2):4,(3,2,5):1,(3,4,5):10,(4,5,6):61,
    (5,6,7):74,(6,7,8):36,(7,8,9):9,(8,9,10):1,
}
assert bars==EXPECTED_BARS,(bars,EXPECTED_BARS)
assert len(birthdeath)==512 and len(empty_columns)==512
print('Reduced F2 persistence barcode (dim, birth, death) : multiplicity')
for key,mult in sorted(bars.items()):print(key,':',mult)
print('ALL CHECKS PASSED')
