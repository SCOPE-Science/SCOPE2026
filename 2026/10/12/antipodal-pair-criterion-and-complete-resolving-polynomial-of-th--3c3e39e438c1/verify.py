"""Exact finite verifier for the resolving polynomial of the dodecahedral graph.

Run: python3 verify.py
Only Python 3 standard-library modules are required.
The mathematical argument in RESULT.md explains why these finite checks
prove the asserted exhaustive statement for this fixed twenty-vertex graph.
"""
from collections import Counter, deque
from itertools import combinations
from math import comb

N = 20
# The first ten vertices are outer u_0,...,u_9; the next ten inner v_0,...,v_9.
edges = set()
for i in range(10):
    for a,b in ((i,(i+1)%10), (i,10+i), (10+i,10+(i+2)%10)):
        edges.add(tuple(sorted((a,b))))
assert len(edges) == 30
adj = [set() for _ in range(N)]
for a,b in edges:
    adj[a].add(b)
    adj[b].add(a)
assert all(len(v)==3 for v in adj)

def distances(start):
    row = [-1]*N
    row[start] = 0
    Q = deque([start])
    while Q:
        v=Q.popleft()
        for w in adj[v]:
            if row[w]==-1:
                row[w]=row[v]+1
                Q.append(w)
    assert -1 not in row
    return row

dist = [distances(x) for x in range(N)]
assert max(map(max,dist))==5
A = (0,1,2,3,4,5,4,3,2,1)
B = (1,2,2,3,3,4,3,3,2,2)
C = (0,3,1,4,2,5,2,4,1,3)
assert tuple(dist[0][:10]) == A
assert tuple(dist[0][10:]) == B
assert tuple(dist[10][:10]) == B
assert tuple(dist[10][10:]) == C

# Antipodal classes: five pairs of each vertex type.
pairs = [(i, i+5) for i in range(5)] + [(10+i,15+i) for i in range(5)]
pair_masks = [(1<<x)|(1<<y) for x,y in pairs]
assert len(set(v for pair in pairs for v in pair)) == N
antipode = [None]*N
for x,y in pairs:
    antipode[x]=y
    antipode[y]=x
assert all(dist[x][antipode[x]]==5 for x in range(N))
assert all(dist[x][antipode[y]]==5-dist[x][y] for x in range(N) for y in range(N))

# All vertex-pair equidistance sets are either empty or exactly two antipodal pairs.
equidistance_masks=[]
equalizer_fiber_pairs=Counter()
for x,y in combinations(range(N),2):
    e = sum(1<<s for s in range(N) if dist[s][x]==dist[s][y])
    equidistance_masks.append(e)
    if y == antipode[x]:
        assert e==0
    else:
        assert e.bit_count()==4
        fiber_pair=tuple(i for i,pairmask in enumerate(pair_masks) if (e & pairmask)==pairmask)
        assert len(fiber_pair)==2
        equalizer_fiber_pairs[fiber_pair]+=1
assert Counter(e.bit_count() for e in equidistance_masks)=={4:180,0:10}
assert len(equalizer_fiber_pairs)==comb(10,2)==45
assert Counter(equalizer_fiber_pairs.values())=={2:30,8:15}

# Direct signatures: no two vertices ever have identical distance vectors
# to one or two representatives. Also check precisely the resolving 3-/4-sets.
def directly_resolves(sensors):
    profiles={tuple(dist[v][s] for s in sensors) for v in range(N)}
    return len(profiles)==N
for k in (0,1,2,3,4):
    for indices in combinations(range(N),k):
        mask = sum(1<<v for v in indices)
        hit = sum(bool(mask&p) for p in pair_masks)
        assert directly_resolves(indices)==(hit>=3)

# Exhaustively check the antipodal quotient criterion over all 2^20 subsets
# and derive each coefficient, without extrapolating from a sample.
counts=[0]*(N+1)
nonresolving=0
for mask in range(1<<N):
    hit=sum(bool(mask & p) for p in pair_masks)
    if hit>=3:
        counts[mask.bit_count()]+=1
    else:
        nonresolving+=1
formula=[sum(comb(10,j)*comb(j,k-j)*(2**(2*j-k)) for j in range(3,11) if j<=k<=2*j) for k in range(N+1)]
assert counts==formula
assert sum(counts)==(1<<20)-436
assert nonresolving==436
assert all(counts[k]==0 for k in range(3))
assert counts[3]==960
assert sum(counts)==1048140
print('VERIFY_OK graph_vertices=20 graph_edges=30 antipodal_pairs=10 distance_diameter=5')
print('VERIFY_OK equidistance_sets=190 empty=10 four_vertices=180 all_45_fiber_pairs_realized=YES')
print('VERIFY_OK direct_distance_signatures_all_subsets_sizes_0_through_4=6196')
print('VERIFY_OK all_masks=1048576 resolving=1048140 nonresolving=436')
print('VERIFY_OK metric_dimension=3 metric_bases=960 full_resolving_polynomial=exact')
print('VERIFY_OK coefficients_k3_to_k20='+','.join(map(str,counts[3:])))
