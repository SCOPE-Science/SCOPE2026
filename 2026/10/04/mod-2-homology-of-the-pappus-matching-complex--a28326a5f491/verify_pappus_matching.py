#!/usr/bin/env python3
from functools import lru_cache

N=18
SHIFTS=[5,7,-7,7,-7,-5]*3
# Independent LCF construction of the Pappus graph.
edges=set()
for i in range(N):
    edges.add(tuple(sorted((i,(i+1)%N))))
for i,s in enumerate(SHIFTS):
    edges.add(tuple(sorted((i,(i+s)%N))))
edges=sorted(edges)
assert len(edges)==27
assert all(u!=v for u,v in edges)
deg=[0]*N
for u,v in edges:
    deg[u]+=1; deg[v]+=1
assert deg==[3]*N

# Exhaustive edge-recursion: every branch either omits the next edge or,
# when possible, includes it. Hence every graph matching occurs exactly once.
faces=[[] for _ in range(10)]
def enum(i, used_vertices, edge_mask, size):
    if i==len(edges):
        faces[size].append(edge_mask)
        return
    enum(i+1, used_vertices, edge_mask, size)
    u,v=edges[i]
    bu,bv=1<<u,1<<v
    if not (used_vertices & (bu|bv)):
        enum(i+1, used_vertices|bu|bv, edge_mask|(1<<i), size+1)
enum(0,0,0,0)
counts=[len(x) for x in faces]
EXPECTED=[1,27,297,1719,5643,10557,10737,5319,1026,42]
assert counts==EXPECTED, (counts,EXPECTED)
assert sum(counts)==35368

# Independent matching-polynomial recursion on vertex-induced subgraphs:
# p_G(t)=p_{G-v}(t)+t*sum_{u~v} p_{G-v-u}(t).
adj=[0]*N
for u,v in edges:
    adj[u]|=1<<v; adj[v]|=1<<u
@lru_cache(None)
def poly(vertices):
    if not vertices:
        return (1,)
    v=(vertices & -vertices).bit_length()-1
    rest=vertices & ~(1<<v)
    a=list(poly(rest))
    nbrs=adj[v] & rest
    while nbrs:
        b=nbrs & -nbrs; nbrs-=b
        u=b.bit_length()-1
        q=poly(rest & ~(1<<u))
        if len(a)<len(q)+1: a += [0]*(len(q)+1-len(a))
        for j,c in enumerate(q): a[j+1]+=c
    return tuple(a)
assert list(poly((1<<N)-1))==EXPECTED

# Exact ranks of augmented simplicial boundary maps over F_2.
# A simplex is an edge-mask; deleting each chosen graph edge gives its facets.
def gf2_rank(columns):
    piv={}
    rank=0
    for col in columns:
        x=col
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x; rank+=1; break
    return rank

ranks=[]
for k in range(1,10):
    row={m:i for i,m in enumerate(faces[k-1])}
    cols=[]
    for m in faces[k]:
        c=0; x=m
        while x:
            b=x & -x; x-=b
            c ^= 1 << row[m^b]
        cols.append(c)
    ranks.append(gf2_rank(cols))
EXPECTED_RANKS=[1,26,271,1448,4195,6362,4335,984,42]
assert ranks==EXPECTED_RANKS, (ranks,EXPECTED_RANKS)

# Reduced Betti numbers in simplex dimensions 0,...,8.
f=[len(faces[d+1]) for d in range(9)]
r=ranks+[0]
betti=[f[d]-r[d]-r[d+1] for d in range(9)]
assert betti==[0,0,0,0,0,40,0,0,0], betti
# Euler characteristic cross-check: reduced chi equals (-1)^5*40=-40.
chi=sum((1 if d%2==0 else -1)*f[d] for d in range(9))
assert chi==-39 and chi-1==-40
print('vertices=18 edges=27')
print('matching_counts=',counts)
print('augmented_boundary_ranks=',ranks)
print('reduced_betti=',betti)
print('VERIFY_OK')
