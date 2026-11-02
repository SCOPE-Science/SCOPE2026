#!/usr/bin/env python3
"""Independent Pappus-graph certificate: LCF construction, maximal clique search.
Requires only the Python standard library. Run: python lcf_certificate.py
"""
from itertools import combinations
from collections import Counter, deque
n=18
chords=[5,7,-7,7,-7,-5]*3
edges=sorted({tuple(sorted((i,(i+1)%n))) for i in range(n)} |
             {tuple(sorted((i,(i+chords[i])%n))) for i in range(n)})
assert len(edges)==27
N=[set() for _ in range(n)]
for a,b in edges:N[a].add(b);N[b].add(a)
assert set(map(len,N))=={3}
# The 27 conflict vertices are graph edges. Compatible vertices correspond
# to edges that together form an induced matching.
C=[set() for _ in range(27)]
for i,(a,b) in enumerate(edges):
    for j,(c,d) in enumerate(edges):
        if i!=j and len({a,b,c,d})==4 and all(v not in N[u] for u in (a,b) for v in (c,d)):
            C[i].add(j)
# Independently enumerate all maximal cliques of the compatibility graph.
cliques=[]
def grow(R,P,X):
    if not P and not X:
        cliques.append(frozenset(R));return
    u=max(P|X,key=lambda i:len(P&C[i])) if P or X else None
    for v in sorted(P-(C[u] if u is not None else set())):
        grow(R|{v},P&C[v],X&C[v])
        P.remove(v);X.add(v)
grow(set(),set(range(27)),set())
hist=Counter(map(len,cliques))
assert max(hist)==5 and hist[5]==27
print("maximal-clique histogram:",dict(hist))
maxima=sorted(c for c in cliques if len(c)==5)
F=[set() for _ in maxima]
for i,j in combinations(range(27),2):
    if len(maxima[i]&maxima[j])==3:F[i].add(j);F[j].add(i)
assert all(len(a)==4 for a in F)

# Pairwise all-source metric, without orbit or symmetry reductions.
def bfs(source):
    d={source:0};queue=deque([source])
    while queue:
        a=queue.popleft()
        for b in F[a]:
            if b not in d:d[b]=d[a]+1;queue.append(b)
    return d
profile=Counter(); distances=Counter();detours=Counter()
for i in range(27):
    di=bfs(i);assert len(di)==27
    profile[tuple(Counter(di.values())[j] for j in range(5))]+=1
    for j in range(i):
        distances[di[j]]+=1
        lower=(5-len(maxima[i]&maxima[j])+1)//2
        detours[di[j]-lower]+=1
assert profile=={(1,4,8,12,2):27}
assert distances=={1:54,2:108,3:162,4:27}
assert detours=={0:324,1:27}

# In a line graph of a triangle-free cubic graph every edge belongs to one
# K3 and every vertex to two K3s. Recover its underlying graph as the graph
# on triangles, joined when they have an exchange vertex in common.
tri=[frozenset((i,j,k)) for i,j,k in combinations(range(27),3)
     if j in F[i] and k in F[i] and k in F[j]]
assert len(tri)==18
T=[set() for _ in range(18)]
for i,j in combinations(range(18),2):
    if tri[i]&tri[j]:T[i].add(j);T[j].add(i)
assert sorted(map(len,T))==[3]*18
# Verify the graph on triangles and the original LCF graph are isomorphic.
# Partitioned backtracking enforces both edges and nonedges at each step.
def isomorphic(A,B):
    order=list(range(len(A)))
    f={};g={}
    def rec():
        if len(f)==len(A):return True
        un=[v for v in order if v not in f]
        v=max(un,key=lambda v:(len(set(A[v])&f.keys()),-v))
        for w in order:
            if w in g:continue
            if len(A[v])!=len(B[w]):continue
            if any(((u in A[v])!=(f[u] in B[w])) for u in f):continue
            f[v]=w;g[w]=v
            if rec():return True
            del f[v];del g[w]
        return False
    return rec()
assert isomorphic(T,N)
print('LCF_MAXIMAL_CLIQUE_AND_METRIC_PASS')
print('maximal_histogram=',dict(sorted(hist.items())))
print('maximum=5 number=27 exchange_edges=54 edge_triangles=18')
print('all_source_profile=',dict(profile),'pair_distances=',dict(distances))
print('extra_batch_moves=',dict(detours),'triangle_graph_is_Pappus=True')
