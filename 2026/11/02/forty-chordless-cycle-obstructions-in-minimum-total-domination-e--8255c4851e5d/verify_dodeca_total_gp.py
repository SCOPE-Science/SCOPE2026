"""Independent bitset checker using the generalized Petersen graph GP(10,2).

Only Python's standard library is required.
"""
from itertools import combinations
from collections import Counter, deque

n = 10
N = [0] * 20
for i in range(n):
    u, v = i, 10+i
    for a,b in ((u,(i+1)%n), (u,v), (v,10+(i+2)%n)):
        N[a] |= 1<<b
        N[b] |= 1<<a
assert sorted(x.bit_count() for x in N) == [3]*20
assert sum(x.bit_count() for x in N)//2 == 30

def covers(mask):
    return all(neighbors & mask for neighbors in N)

# Completeness: exactly all eight-subsets are enumerated; cardinality seven
# is excluded by an exhaustive independent scan and <=6 by edge counting.
assert not any(covers(sum(1<<v for v in S)) for S in combinations(range(20),7))
sets = {sum(1<<v for v in S) for S in combinations(range(20),8) if covers(sum(1<<v for v in S))}
assert len(sets) == 190
E = {mask:set() for mask in sets}
for mask in sets:
    for i in range(20):
        if mask&(1<<i):
            stripped=mask^(1<<i)
            for j in range(20):
                if not mask&(1<<j):
                    candidate = stripped | (1<<j)
                    if candidate in sets: E[mask].add(candidate)
assert all(mask in E[neighbor] for mask in E for neighbor in E[mask])
assert sum(map(len,E.values()))//2 == 360
assert Counter(map(len,E.values())) == {0:40,4:120,8:30}

remain=set(sets)
component_sizes=[]
main=None
while remain:
    start=next(iter(remain));reached={start};todo=[start]
    for x in todo:
        for y in E[x]:
            if y not in reached:reached.add(y);todo.append(y)
    remain-=reached
    component_sizes.append(len(reached))
    if len(reached)>1:main=reached
assert sorted(component_sizes,reverse=True) == [150] + [1]*40
assert main is not None

def distances(start):
    d={start:0}; q=deque([start])
    while q:
        x=q.popleft()
        for y in E[x]:
            if y not in d:
                d[y]=d[x]+1;q.append(y)
    return d

assert all(len(distances(x))==150 and max(distances(x).values())==10 for x in main)
# Confirm 30/10 split of the isolated configurations by their induced maximum
# degree: two four-vertex paths versus two four-vertex stars.
shapes=Counter()
for mask in sets:
    if E[mask]:continue
    d=tuple(sorted((N[v]&mask).bit_count() for v in range(20) if mask>>v&1))
    shapes[d]+=1
assert shapes[(1,1,1,1,2,2,2,2)] == 30
assert shapes[(1,1,1,1,1,1,3,3)] == 10
assert sum(shapes.values())==40
# A complement is a chordless 12-cycle precisely when every included
# vertex has two included neighbours and the induced subgraph is connected.
full = (1<<20)-1

def induced_cycle(mask):
    if mask.bit_count()!=12 or any((N[i]&mask).bit_count()!=2 for i in range(20) if mask>>i&1):
        return False
    seed=(mask & -mask).bit_length()-1
    found=1<<seed;todo=[seed]
    for u in todo:
        for v in range(20):
            if N[u]>>v&1 and mask>>v&1 and not found>>v&1:
                found|=1<<v;todo.append(v)
    return found==mask

assert {x for x in sets if len(E[x])==0} == {x for x in sets if induced_cycle(full^x)}
assert sum(induced_cycle(sum(1<<v for v in C)) for C in combinations(range(20),12))==40
print('DODECAHEDRON_GP_BITSET_PASS')
print('MINIMUM_SIZE 8; SETS 190; EXCHANGE_EDGES 360')
print('COMPONENTS 150 and 40 singletons; ALL_GIANT_ECCENTRICITIES 10')
print('ISOLATED_SHAPES',dict(shapes))
