"""Exact finite enumeration of the Petersen graph's four-edge-colouring flip space.

Run with Python >=3.9; only the standard library is required. All graphs
and edge/colour assignments are constructed here from definitions.
"""
from collections import Counter, deque
from itertools import combinations, permutations

# Petersen graph: vertices are the 2-subsets of a five-element set; edges
# connect disjoint pairs. Coordinates and edge order are fixed lexicographically.
V = tuple(combinations(range(5), 2))
E = tuple((i, j) for i in range(10) for j in range(i+1, 10)
          if set(V[i]).isdisjoint(V[j]))
assert len(V) == 10 and len(E) == 15
m = len(E)
N = tuple(frozenset(j for j, (a,b) in enumerate(E)
                    if j != i and (a in (u,v) or b in (u,v)))
          for i, (u,v) in enumerate(E))
INC = tuple(tuple(i for i,(a,b) in enumerate(E) if v in (a,b))
            for v in range(10))
assert all(len(t)==3 for t in INC)

# The chromatic index is four: each perfect matching leaves two odd
# five-cycles, so a three-edge-colouring would force an impossible
# two-colouring of an odd-cycle complement. Enumeration also constructs
# proper four-edge-colourings below.
perfect = []
for idxs in combinations(range(m), 5):
    nodes = set()
    for e in idxs:nodes.update(E[e])
    if len(nodes)==10:perfect.append(frozenset(idxs))
assert len(perfect)==6
for matching in perfect:
    rest=[e for e in range(m) if e not in matching]
    adjv=[set() for _ in V]
    for e in rest:
        a,b=E[e];adjv[a].add(b);adjv[b].add(a)
    assert all(len(a)==2 for a in adjv)
    found=set();lens=[]
    for v in range(10):
        if v in found:continue
        q=[v]; found.add(v)
        for u in q:
            for w in adjv[u]:
                if w not in found: found.add(w); q.append(w)
        lens.append(len(q))
    assert sorted(lens)==[5,5]

# Method A: direct edge-by-edge proper-colouring backtracking.
c = [-1]*m
C = []
def extend(i):
    if i == m:
        C.append(tuple(c)); return
    occupied = {c[j] for j in N[i] if c[j] >= 0}
    for x in range(4):
        if x not in occupied:
            c[i] = x
            extend(i+1)
    c[i] = -1
extend(0)
assert len(C) == 49920
assert len(set(C)) == len(C)
index = {c:i for i,c in enumerate(C)}

# Method B: partition all edges into four (unlabelled) nonempty matchings.
# Choose the class containing the smallest yet unassigned edge at each step.
# This visits every four-class partition once, with no permutation division.
full = (1<<m)-1
matchings = []
for mask in range(1,full+1):
    taken = 0
    okay = True
    for i,(u,v) in enumerate(E):
        if mask & (1<<i):
            b = (1<<u)|(1<<v)
            if taken & b:
                okay = False;break
            taken |= b
    if okay:matchings.append(mask)
by_first = [[a for a in matchings if a & (1<<i)] for i in range(m)]
classes = []
partitions = set()
def partition(remain):
    if not remain:
        if len(classes) == 4:
            arr = [-1]*m
            for x,mask in enumerate(classes):
                for e in range(m):
                    if mask & (1<<e):arr[e] = x
            partitions.add(tuple(arr))
        return
    if len(classes) == 4:return
    i = (remain & -remain).bit_length()-1
    for mask in by_first[i]:
        if mask & remain == mask:
            classes.append(mask)
            partition(remain ^ mask)
            classes.pop()
partition(full)

def canon(s):
    seen = {};t=[]
    for col in s:
        if col not in seen:seen[col]=len(seen)
        t.append(seen[col])
    return tuple(t)
assert len(partitions)==2080
assert partitions == {canon(s) for s in C}
assert all(len({s[e] for e in INC[v]}) == 3
           for s in C for v in range(10))
assert Counter(tuple(sorted(Counter(s).values())) for s in C) == {
    (2,4,4,5):7200, (3,3,4,5):14400, (3,4,4,4):28320}

# Enumerate single-edge recolourings by missing colours at the two endpoints.
# Cross-check with an independent adjacency-union test and run two
# independent component computations (flood-fill and disjoint-set union).
parent = list(range(len(C))); rank = [0]*len(C)
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x
def union(a,b):
    a=find(a);b=find(b)
    if a==b:return
    if rank[a] < rank[b]:a,b=b,a
    parent[b]=a
    if rank[a]==rank[b]:rank[a]+=1

neighbors = [[] for _ in C]
for i,s in enumerate(C):
    atv = [set(s[e] for e in INC[v]) for v in range(10)]
    for e,(u,v) in enumerate(E):
        forbidden = set(s[j] for j in N[e])
        assert forbidden == (atv[u] | atv[v]) - {s[e]}
        for col in range(4):
            if col != s[e] and col not in forbidden:
                z = list(s);z[e]=col
                j=index[tuple(z)]
                neighbors[i].append(j)
                if i < j:union(i,j)
    assert len(neighbors[i]) == len(set(neighbors[i]))
assert all(i in neighbors[j] for i, row in enumerate(neighbors) for j in row)
edge_count=sum(map(len, neighbors))//2
assert edge_count==109440

seen=[-1]*len(C);sizes=[];n_edges=[];representatives=[]
for i in range(len(C)):
    if seen[i]>=0:continue
    ci=len(sizes);seen[i]=ci;q=[i];total=0
    for a in q:
        total+=len(neighbors[a])
        for b in neighbors[a]:
            if seen[b]<0:seen[b]=ci;q.append(b)
            else:assert seen[b]==ci
    sizes.append(len(q));n_edges.append(total//2);representatives.append(i)
assert Counter(zip(sizes,n_edges)) == {(1,0):960,(24480,54720):2}
assert Counter((sum(1 for j in range(len(C)) if find(i)==find(j)))
               for i in representatives) == {1:960,24480:2}
assert len(set(find(i) for i in range(len(C))))==962
frozen={i for i,s in enumerate(C) if all(
    len({s[j] for j in N[e]})==3 for e in range(m))}
assert len(frozen)==960
assert frozen == {i for i,a in enumerate(neighbors) if not a}
assert Counter(tuple(sorted(Counter(C[i]).values())) for i in frozen)=={
    (3,4,4,4):960}

# The natural S_5 action on the 2-subset model induces all 120 automorphisms.
pairidx={a:i for i,a in enumerate(V)}
edidx={a:i for i,a in enumerate(E)}
def permuted_state(s,p):
    t = [-1]*m
    for i,(a,b) in enumerate(E):
        x=pairidx[tuple(sorted((p[V[a][0]],p[V[a][1]])))]
        y=pairidx[tuple(sorted((p[V[b][0]],p[V[b][1]])))]
        t[edidx[tuple(sorted((x,y)))]]=s[i]
    return tuple(t)
def parity(p):
    return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5))%2
perms=list(permutations(range(5)))
assert len(perms)==120
large=[i for i,n in enumerate(sizes) if n>1]
assert len(large)==2
for k in large:
    s=C[representatives[k]]
    for p in perms:
        dst=seen[index[permuted_state(s,p)]]
        assert dst == (k if parity(p)==0 else next(c for c in large if c!=k))
# Every palette permutation preserves each large component.
for k in large:
    s=C[representatives[k]]
    for p in permutations(range(4)):
        assert seen[index[tuple(p[x] for x in s)]]==k
# The frozen states constitute exactly one S_5 x S_4 orbit.
s=C[next(iter(frozen))]
images={tuple(p[x] for x in permuted_state(s,q))
        for q in perms for p in permutations(range(4))}
assert len(images)==960 and images=={C[i] for i in frozen}

print('PETERSEN_4_COLORINGS=49920')
print('UNLABELED_PALETTE_CLASSES=2080')
print('RECOLORING_EDGES=109440')
print('COMPONENT_PROFILE=2*(24480 vertices, 54720 edges)+960*(1 vertex, 0 edges)')
print('FROZEN_STATES=960 ONE_S5_X_S4_ORBIT=YES')
print('GIANTS_EXCHANGED_BY_ODD_S5=YES; ALL_S4_FIX_GIANTS=YES')
print('VERIFY_OK')
