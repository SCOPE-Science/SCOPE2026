"""Exact verification of exponential domination in the Tutte--Coxeter Levi graph.

Vertices 0..14: duads of [0..5]; vertices 15..29: synthemes.
Only standard-library Python is required.  All arithmetic is rational.
"""
from collections import Counter, deque
from fractions import Fraction
from itertools import combinations

DUADS = tuple(combinations(range(6), 2))

def pair_partitions(available):
    if not available:
        yield ()
        return
    x = available[0]
    for j in range(1, len(available)):
        y = available[j]
        for rest in pair_partitions(available[1:j] + available[j+1:]):
            yield ((x, y),) + rest

SYNTHEMES = tuple(pair_partitions(tuple(range(6))))
assert len(SYNTHEMES) == 15
A = [set() for _ in range(30)]
for k, partition in enumerate(SYNTHEMES):
    for edge in partition:
        i = DUADS.index(edge)
        A[i].add(15+k)
        A[15+k].add(i)
assert sum(map(len, A)) == 90 and all(len(x)==3 for x in A)

def distances(source, forbidden=frozenset()):
    d = [-1]*30
    if source in forbidden:
        return d
    d[source] = 0
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in A[u]:
            if d[v] == -1 and v not in forbidden:
                d[v] = d[u]+1
                queue.append(v)
    return d

D = [distances(x) for x in range(30)]
assert all(max(row)==4 for row in D)
assert all(Counter(d for d in row if d>0) == Counter({1:3,2:6,3:12,4:8}) for row in D)

def porous(S):
    selected = set(S)
    for v in range(30):
        if v in selected:
            continue
        # Multiplication by 8 clears all denominators (diameter four).
        if sum(1 << (4-D[s][v]) for s in S) < 8:
            return False
    return True

def blocked_weights(S):
    selected = set(S)
    rows = [distances(s,selected-{s}) for s in S]
    return tuple(sum((Fraction(2,2**row[u]) if row[u]>=0 else Fraction(0))
                     for row in rows)
                 for u in range(30) if u not in selected)

for k in range(1,4):
    assert not any(porous(S) for S in combinations(range(30),k))

POR = tuple(S for S in combinations(range(30),4) if porous(S))
assert len(POR) == 45
assert all(sum(i<15 for i in S)==2 for S in POR)
assert all(min(blocked_weights(S))>=1 for S in POR)

# Canonical correspondence: flag (point r on line L), with its other two
# points and the other two lines through r selected.
FLAGS = set()
for k, partition in enumerate(SYNTHEMES):
    line = 15+k
    for r in A[line]:
        other_points = A[line]-{r}
        other_lines = A[r]-{line}
        assert len(other_points)==len(other_lines)==2
        FLAGS.add(tuple(sorted(other_points | other_lines)))
assert len(FLAGS)==45 and set(POR)==FLAGS

representative = POR[0]
weights = Counter(str(w) for w in blocked_weights(representative))
assert weights == Counter({'9/8':16, '21/16':8, '3':2}), weights

# Each edge of the reconfiguration graph replaces three out of four tokens.
sets = [frozenset(S) for S in POR]
R = [set() for _ in sets]
intersection_hist = Counter()
for i, S in enumerate(sets):
    for j in range(i+1,len(sets)):
        n = len(S & sets[j])
        intersection_hist[n]+=1
        if n==1:
            R[i].add(j)
            R[j].add(i)
assert intersection_hist == Counter({0:540,1:450}), intersection_hist
assert all(len(N)==20 for N in R)
assert sum(map(len,R))//2 == 450
for root in range(len(R)):
    depths = [-1]*len(R)
    depths[root] = 0
    Q = deque([root])
    while Q:
        i = Q.popleft()
        for j in R[i]:
            if depths[j] < 0:
                depths[j]=depths[i]+1;Q.append(j)
    assert Counter(depths)==Counter({0:1,1:20,2:24})

print('structure 30 vertices 45 edges distance_layers=3,6,12,8')
print('porous_optimum=4 count=45 blocked_optimum=4 count=45')
print('flag_count=45 sides=2+2')
print('blocked_weight_profile', '9/8:16 21/16:8 3:2')
print('intersection_pair_distribution',dict(sorted(intersection_hist.items())))
print('three_token_reconfiguration vertices=45 edges=450 degree=20 diameter=2 radius=2')
