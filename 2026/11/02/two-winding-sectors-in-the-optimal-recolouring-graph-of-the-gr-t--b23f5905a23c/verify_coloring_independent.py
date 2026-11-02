"""Independent enumeration from cycle words and independent shadow choices.

Legal one-vertex replacements are found by grouping colorings by all ten
coordinates *except* the changed coordinate. There is no graph neighbor
recoloring test in this verifier, unlike verify_coloring_recursive.py.
"""
from collections import Counter, defaultdict, deque
from itertools import product, permutations

# All proper four-colorings of the OUTER C5, written independently of graph
# recursive enumeration. Shadow labels are independently selected from the
# allowable complement of the two adjacent outer colors and of the apex.
outer_words=[x for x in product(range(4),repeat=5)
             if all(x[i]!=x[(i+1)%5] for i in range(5))]
assert len(outer_words)==240
colors=[]
for apex in range(4):
    for o in outer_words:
        choices=[tuple(c for c in range(4)
                       if c not in (apex,o[(i-1)%5],o[(i+1)%5]))
                 for i in range(5)]
        if all(choices):
            for shadows in product(*choices):
                colors.append(o+shadows+(apex,))
assert len(colors)==12480 and len(set(colors))==len(colors)
idx={x:i for i,x in enumerate(colors)}
# All coordinate-deletion buckets: each pair in a bucket changes exactly
# one coordinate. Each pair changes exactly one coordinate iff exactly one
# coordinate-deletion bucket contains it. The graph is therefore complete.
buckets=defaultdict(list)
for a,s in enumerate(colors):
    for j in range(11):
        buckets[(j,s[:j]+s[j+1:])].append(a)
adj=[set() for _ in colors]
for bucket in buckets.values():
    for k,a in enumerate(bucket):
        for b in bucket[k+1:]:
            adj[a].add(b);adj[b].add(a)
assert sum(map(len,adj))//2==45240
assert Counter(map(len,adj))=={5:480,6:2640,7:3840,8:4320,9:1200}

# A distinct signed winding computation: derive the color order from the
# parity of a permutation (apex, other three in increasing order).
def orientation_sign(c):
    a=c[-1]
    t=tuple(i for i in range(4) if i!=a)
    parity=sum(x>y for i,x in enumerate((a,)+t) for y in ((a,)+t)[i+1:])%2
    rank={v:k for k,v in enumerate(t)}
    h=[rank[c[i] if c[i]!=a else c[5+i]] for i in range(5)]
    assert all(h[j]!=h[(j+1)%5] for j in range(5))
    increment=sum(1 if (h[(j+1)%5]-h[j])%3==1 else -1 for j in range(5))
    assert increment in (3,-3)
    return (1 if parity==0 else -1)*(1 if increment==3 else -1)
# parity of (apex, remaining ascending) is apex modulo 2, as required.
signs=list(map(orientation_sign,colors))
assert Counter(signs)=={1:6240,-1:6240}
assert all(signs[a]==signs[b] for a,A in enumerate(adj) for b in A)

# Disjoint-set union is independent of the recursive verifier's flood BFS.
parent=list(range(len(colors)));size=[1]*len(colors)
def find(a):
    while parent[a]!=a:
        parent[a]=parent[parent[a]];a=parent[a]
    return a
def union(a,b):
    a=find(a);b=find(b)
    if a!=b:
        if size[a]<size[b]:a,b=b,a
        parent[b]=a;size[a]+=size[b]
for a,A in enumerate(adj):
    for b in A:
        if a<b:union(a,b)
comps=defaultdict(list)
for a in range(len(colors)):comps[find(a)].append(a)
assert sorted(map(len,comps.values()))==[6240,6240]
assert all(len({signs[a] for a in C})==1 for C in comps.values())
# Prove the apex-color disconnection decomposition also directly by DSU
# on edges which do not change the apex.
par2=list(range(len(colors)))
def root2(i):
    while par2[i]!=i:par2[i]=par2[par2[i]];i=par2[i]
    return i
for a,A in enumerate(adj):
    for b in A:
        if colors[a][-1]==colors[b][-1]:par2[root2(a)]=root2(b)
blocks=Counter((colors[a][-1],root2(a)) for a in range(len(colors)))
assert len(blocks)==8 and set(blocks.values())=={1560}
# Check the signed orientation directly against all apex-changing edges.
apex_changes=Counter()
for a,A in enumerate(adj):
    for b in A:
        if colors[a][-1]<colors[b][-1]:
            apex_changes[(colors[a][-1],colors[b][-1],signs[a])]+=1
assert len(apex_changes)==12 and set(apex_changes.values())=={190}
# Eccentricity counts from one representative per automorphism orbit; 
# canonical-coloring-and-dihedral signatures are computed independently.
def canonical(s):
    forms=[]
    for t in range(5):
        for d in (1,-1):
            g=tuple(s[(d*i+t)%5] for i in range(5))
            g+=tuple(s[5+(d*i+t)%5] for i in range(5))+(s[-1],)
            rep={};w=[]
            for x in g:
                if x not in rep:rep[x]=len(rep)
                w.append(rep[x])
            forms.append(tuple(w))
    return min(forms)
reps={}
for i,s in enumerate(colors):reps.setdefault(canonical(s),i)
assert len(reps)==56
# Determine orbit weights by counting canonical strings, then run one BFS
# per representative. This certifies each radius/diameter claim exactly.
weights=Counter(canonical(s) for s in colors)
ecc=Counter()
for k,a in reps.items():
    dist={a:0};Q=deque([a])
    while Q:
        u=Q.popleft()
        for v in adj[u]:
            if v not in dist:dist[v]=dist[u]+1;Q.append(v)
    assert len(dist)==6240
    ecc[max(dist.values())]+=weights[k]
assert ecc=={15:2160,16:10200,17:120}
print('CYCLE_WORD_SHADOW_PRODUCT_12480_AND_HAMMING_BUCKET_EDGES_PASS')
print('UNION_FIND_TWO_SIGNED_COMPONENTS_AND_APEX_BLOCKS_PASS')
print('CANONICALIZED_ALL_ORBITS_RADIUS15_DIAMETER17_PASS')
