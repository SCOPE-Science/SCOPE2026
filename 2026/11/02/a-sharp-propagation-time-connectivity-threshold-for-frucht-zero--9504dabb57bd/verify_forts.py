"""Independent certificate via forts and the LCF representation.
Run: python verify_forts.py
"""
from itertools import combinations
from collections import Counter
from hashlib import sha256

N = 12
LCF = (-5,-2,-4,2,5,-2,2,5,-2,-5,4,2)
EDGES = {tuple(sorted((i,(i+1)%N))) for i in range(N)}
EDGES.update(tuple(sorted((i,(i+d)%N))) for i,d in enumerate(LCF))
assert len(EDGES) == 18
NEIGH = [set() for _ in range(N)]
for u,v in EDGES:
    NEIGH[u].add(v)
    NEIGH[v].add(u)
assert all(len(s)==3 for s in NEIGH)
# Explicit isomorphism of the independent LCF construction to the
# 12-vertex 18-edge representation used in verify_direct.py.
P = (5,3,2,1,0,7,6,4,10,11,8,9)
CANONICAL = {(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),
             (3,9),(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),
             (8,9),(8,11),(10,11)}
assert {tuple(sorted((P[u],P[v]))) for u,v in CANONICAL} == EDGES

VERTICES = frozenset(range(N))
# F is a fort if no vertex outside F has exactly one neighbor in F.
FORTS = []
for k in range(1,N+1):
    for t in combinations(range(N),k):
        f = frozenset(t)
        if all(len(NEIGH[v] & f) != 1 for v in VERTICES-f):
            FORTS.append(f)
MIN_FORTS=[]
for f in FORTS:  # sorted by cardinality
    if not any(h <= f for h in MIN_FORTS):
        MIN_FORTS.append(f)
assert MIN_FORTS

def survives_all_forts(b):
    return all(bool(b & f) for f in MIN_FORTS)
# Every smaller seed set fails since it misses a minimal fort.
assert not any(survives_all_forts(frozenset(t))
               for k in range(4) for t in combinations(range(N),k))
BASES = [frozenset(t) for t in combinations(range(N),4)
         if survives_all_forts(frozenset(t))]
assert len(BASES)==89
# Compare the entire 89-set roster in the edge-list labeling. The LCF
# presentation and fort test do not depend on the direct forcing test.
INV = {v:k for k,v in enumerate(P)}
MASKS = sorted(sum(1 << INV[v] for v in b) for b in BASES)
assert sha256(','.join(map(str,MASKS)).encode()).hexdigest() == \
       'ced4bd0df213493a9ce37d11a5d15d181998edcdc493efe0d439870c99d57d1b'

# Independent parallel propagation algorithm using pure set operations.
def time(b):
    seen = set(b)
    for t in range(13):
        if len(seen)==N: return t
        nxt = {next(iter(NEIGH[v]-seen))
               for v in seen if len(NEIGH[v]-seen)==1}
        if not nxt: return None
        seen.update(nxt)
    raise AssertionError('process exceeded vertex-count upper bound')
assert all(time(b) is not None for b in BASES)
T = [time(b) for b in BASES]
assert Counter(T)=={3:8,4:32,5:43,6:6}

# Exchange adjacency from set intersection, not bitmask XOR.
J = [set() for _ in BASES]
for i,b in enumerate(BASES):
    for j in range(i+1,len(BASES)):
        if len(b & BASES[j])==3:
            J[i].add(j); J[j].add(i)
assert sum(map(len,J))//2==366

def signature(threshold):
    V={i for i,t in enumerate(T) if t <= threshold}
    count=sum(len(J[i]&V) for i in V)//2
    components=[]
    while V:
        root=next(iter(V)); V.remove(root)
        comp={root};front=[root]
        while front:
            node=front.pop()
            for target in J[node]&V:
                V.remove(target);comp.add(target);front.append(target)
        components.append(comp)
    return count,sorted(map(len,components),reverse=True)
assert signature(3)==(10,[6,2]);assert signature(4)==(100,[40])
assert signature(5)==(322,[83]);assert signature(6)==(366,[89])
print('LCF_FORT_HYPERGRAPH_AND_PARALLEL_TIMES_PASS')
print('MINIMAL_FORTS',len(MIN_FORTS),'ALL_FORTS',len(FORTS))
print('INDEPENDENT_FOUR_SPEED_LEVELS_PASS')
