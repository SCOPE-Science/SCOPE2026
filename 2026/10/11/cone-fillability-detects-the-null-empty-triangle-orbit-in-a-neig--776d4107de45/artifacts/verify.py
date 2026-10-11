from itertools import combinations
from collections import Counter
from math import gcd

FACETS = [
(1,2,3,6),(1,2,3,7),(1,2,5,7),(1,2,5,10),(1,2,6,10),
(1,3,6,8),(1,3,7,8),(1,4,6,9),(1,4,6,10),(1,4,9,10),
(1,5,6,7),(1,5,6,9),(1,5,9,10),(1,6,7,8),
(2,3,4,7),(2,3,4,8),(2,3,6,8),(2,4,7,9),(2,4,8,9),
(2,5,7,10),(2,6,7,8),(2,6,7,10),(2,7,8,9),
(3,4,5,8),(3,4,5,9),(3,4,7,9),(3,5,8,10),(3,5,9,10),
(3,7,8,9),(3,8,9,10),(4,5,6,9),(4,5,6,10),(4,5,8,10),
(4,8,9,10),(5,6,7,10)]
FACETS = {tuple(sorted(f)) for f in FACETS}
VERTICES = tuple(range(1,11))
TRI = {tuple(sorted(t)) for f in FACETS for t in combinations(f,3)}
EDGES = {tuple(sorted(e)) for f in FACETS for e in combinations(f,2)}
assert (len(VERTICES),len(EDGES),len(TRI),len(FACETS)) == (10,45,70,35)
assert EDGES == set(combinations(VERTICES,2))

TREE = {(1,v) for v in range(2,11)}
CHORDS = sorted(EDGES - TREE)
INDEX = {e:i for i,e in enumerate(CHORDS)}
assert len(CHORDS)==36

def edge_vector(a,b):
    e=tuple(sorted((a,b)))
    out=[0]*36
    if e not in TREE:
        out[INDEX[e]] = 1 if a<b else -1
    return out

def cycle_vector(seq):
    out=[0]*36
    for a,b in zip(seq, seq[1:]+seq[:1]):
        ev=edge_vector(a,b)
        for i,x in enumerate(ev): out[i]+=x
    return out

FACE_LIST=sorted(TRI)
R=[cycle_vector(list(t)) for t in FACE_LIST]
W=[0,1,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,-1,-1,0,0,0,0,-1,0,0,0,0,0,0,0,1,0,1,1,0]
assert len(W)==36 and gcd(*[abs(x) for x in W if x])==1
assert all(sum(a*b for a,b in zip(row,W))==0 for row in R)

MINOR_ROWS=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,24,25,26,27,34,35,36,37,40,41,42,43,48]
MINOR_COLS=[i for i in range(36) if i!=34]

def det_bareiss(A):
    A=[row[:] for row in A]
    n=len(A)
    if n==0: return 1
    sign=1; prev=1
    for k in range(n-1):
        if A[k][k]==0:
            j=next((j for j in range(k+1,n) if A[j][k]),None)
            if j is None: return 0
            A[k],A[j]=A[j],A[k]; sign=-sign
        piv=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                A[i][j]=(A[i][j]*piv-A[i][k]*A[k][j])//prev
        for i in range(k+1,n): A[i][k]=0
        prev=piv
    return sign*A[-1][-1]

minor=[[R[i][j] for j in MINOR_COLS] for i in MINOR_ROWS]
assert det_bareiss(minor)==-1
# The nonzero annihilator W gives rank(R)<=35; the unimodular 35-minor gives rank>=35
# and kills all torsion in Z^36 / rowspan(R). Thus H1 is Z.

def eval_cycle(t):
    return sum(a*b for a,b in zip(cycle_vector(list(t)),W))

ALL_TRI=list(combinations(VERTICES,3))
EMPTY=[t for t in ALL_TRI if t not in TRI]
assert len(ALL_TRI)==120 and len(EMPTY)==50
VAL={t:eval_cycle(t) for t in EMPTY}
assert Counter(VAL.values())==Counter({1:30,-1:10,0:10})
assert sum(v!=0 for v in VAL.values())==40
assert all(abs(v)==1 for v in VAL.values() if v)

def shift(t,k):
    return tuple(sorted((((x-1+k)%10)+1) for x in t))
seen=set(); orbit_data=[]
for t in EMPTY:
    if t in seen: continue
    orb=sorted({shift(t,k) for k in range(10)})
    seen.update(orb)
    orbit_data.append((orb[0],len(orb),tuple(sorted(Counter(VAL[x] for x in orb).items()))))
assert orbit_data == [
    ((1,2,4),10,((1,10),)),
    ((1,2,8),10,((0,10),)),
    ((1,2,9),10,((1,10),)),
    ((1,3,5),10,((1,10),)),
    ((1,4,7),10,((-1,10),)),
]
# Verify the cyclic shift preserves the facet set.
assert {shift(f,1) for f in FACETS}==FACETS

def cone_apices(t):
    a,b,c=t
    out=[]
    for v in VERTICES:
        if v in t: continue
        if all(tuple(sorted(s)) in TRI for s in ((v,a,b),(v,b,c),(v,c,a))): out.append(v)
    return out
CONE={t:cone_apices(t) for t in EMPTY}
assert Counter((VAL[t],len(CONE[t])) for t in EMPTY)==Counter({(1,0):30,(-1,0):10,(0,3):10})
assert CONE[(1,2,8)]==[3,6,7]
assert all((VAL[t]==0)==(len(CONE[t])>0) for t in EMPTY)

print('VERIFY_OK f=10,45,70,35 H1_Z=Z graph_triangles=120 facial3=70 empty3=50')
print('empty3_homology=primitive_nonzero40+null10 simple_integral_1_systole=3 minimizers=40')
print('C10_empty3_orbits=124:+1,128:0,129:+1,135:+1,147:-1 each_size10')
print('null_empty3_cone_fillable_iff=yes cone_apices_each=3 representative_128_apices=3,6,7')
print('unimodular_relation_minor_det=-1 rank_relation=35 quotient_torsionfree_rank1=yes')
