"""Independent exact check: planar-face labeling and degree-one peeling.
Run with Python 3.10+; standard library only.
"""
from itertools import combinations
from collections import Counter, deque

# Dodecahedral graph in a planar pentagonal-face walk labeling, different
# from the generalized Petersen labeling used in the other verification.
EDGES = [(0,1),(0,10),(0,19),(1,2),(1,8),(2,3),(2,6),
         (3,4),(3,19),(4,5),(4,17),(5,6),(5,15),(6,7),
         (7,8),(7,14),(8,9),(9,10),(9,13),(10,11),
         (11,12),(11,18),(12,13),(12,16),(13,14),(14,15),
         (15,16),(16,17),(17,18),(18,19)]
N = 20
near = [0]*N
for a,b in EDGES:
    near[a] |= 1<<b
    near[b] |= 1<<a
assert len(EDGES)==30 and all(m.bit_count()==3 for m in near)

# An explicit relabeling witnesses the isomorphism to GP(10,2).
P = (0,1,8,7,14,15,16,17,18,19,10,2,9,6,13,5,12,4,11,3)
assert set(tuple(sorted((P[i], P[(i+1)%10]))) for i in range(10)) <= set(EDGES)
assert set(tuple(sorted((P[i], P[10+i]))) for i in range(10)) <= set(EDGES)
assert set(tuple(sorted((P[10+i], P[10+(i+2)%10]))) for i in range(10)) <= set(EDGES)

def is_forest_after(deleted):
    """Repeatedly remove vertices of current degree at most 1.
    This empties an induced graph exactly when it is a forest."""
    active = ((1<<N)-1) ^ deleted
    dq=deque(i for i in range(N) if active>>i&1 and (near[i]&active).bit_count()<=1)
    while dq:
        a=dq.popleft()
        if not active>>a&1 or (near[a]&active).bit_count()>1: continue
        active ^= 1<<a
        for b in range(N):
            if active>>b&1 and near[a]>>b&1 and (near[b]&active).bit_count()<=1:
                dq.append(b)
    return active==0

config = [sum(1<<i for i in c) for c in combinations(range(N),6)
          if is_forest_after(sum(1<<i for i in c))]
assert len(config)==2520
T = len(config)
# Define the exchange graph by the Johnson adjacency test, rather than by
# constructing candidate swaps as in the direct certificate.
adj=[[] for _ in range(T)]
for i in range(T):
    for j in range(i+1,T):
        if (config[i]&config[j]).bit_count()==5:
            adj[i].append(j)
            adj[j].append(i)
assert sum(len(row) for row in adj)==47880

degree_counts=Counter(len(a) for a in adj)
assert dict(degree_counts)=={12:420,16:600,18:360,21:120,22:360,
                            24:320,25:240,26:60,27:40}
intersection_distance=Counter()
extra_by_overlap=Counter()
extra_endpoints=Counter()
for i in range(T):
    d=[-1]*T
    d[i]=0
    q=deque([i])
    while q:
        x=q.popleft()
        for y in adj[x]:
            if d[y]<0:
                d[y]=d[x]+1
                q.append(y)
    assert all(0<=x<=6 for x in d)
    assert max(d)==6
    for j in range(i+1,T):
        overlap=(config[i]&config[j]).bit_count()
        distance=d[j]
        intersection_distance[overlap,distance]+=1
        extra=distance-(6-overlap)
        if extra:
            extra_by_overlap[extra,overlap]+=1
        if extra==2:
            extra_endpoints[i]+=1
            extra_endpoints[j]+=1
            common=config[i]&config[j]
            assert sum(bool(common>>a&1 and common>>b&1) for a,b in EDGES)==1
assert dict(intersection_distance)=={
    (0,6):330480,(1,5):972420,(1,6):1920,
    (2,4):1067430,(2,5):21510,(2,6):120,
    (3,3):567820,(3,4):20960,(3,5):60,
    (4,2):162870,(4,3):4410,(5,1):23940}
assert dict(extra_by_overlap)=={(1,1):1920,(1,2):21510,(1,3):20960,
                                 (1,4):4410,(2,2):120,(2,3):60}
assert len(extra_endpoints)==360 and set(extra_endpoints.values())=={1}
print('INDEPENDENT_PLANAR_PEELING_METRIC_PASS')
print('FVS=2520; edges=23940; eccentricity=6 for all; exceptional pairs=180; 360 endpoints each used once')
