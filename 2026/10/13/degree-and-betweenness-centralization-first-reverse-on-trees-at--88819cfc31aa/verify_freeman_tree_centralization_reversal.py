#!/usr/bin/env python3
from itertools import product, combinations
from fractions import Fraction

EXPECTED_TREE_COUNTS = {3:1,4:2,5:3,6:6,7:11,8:23}
EXPECTED_REVERSALS = {3:0,4:0,5:0,6:0,7:0,8:8}

def prufer_tree(seq):
    n=len(seq)+2
    deg=[1]*n
    for x in seq:
        deg[x]+=1
    edges=[]
    for x in seq:
        leaf=min(i for i,d in enumerate(deg) if d==1)
        edges.append((leaf,x))
        deg[leaf]-=1
        deg[x]-=1
    leaves=[i for i,d in enumerate(deg) if d==1]
    edges.append(tuple(leaves))
    return n, tuple(sorted(tuple(sorted(e)) for e in edges))

def adjacency(n, edges):
    adj=[set() for _ in range(n)]
    for u,v in edges:
        adj[u].add(v); adj[v].add(u)
    return adj

def centers(n, edges):
    if n<=2:
        return list(range(n))
    adj=adjacency(n,edges)
    deg=[len(a) for a in adj]
    leaves=[i for i,d in enumerate(deg) if d<=1]
    remaining=n
    while remaining>2:
        remaining-=len(leaves)
        new=[]
        for u in leaves:
            for v in adj[u]:
                deg[v]-=1
                if deg[v]==1:
                    new.append(v)
            deg[u]=0
        leaves=new
    return sorted(leaves)

def rooted_code(adj, root, parent):
    cs=[rooted_code(adj,v,root) for v in adj[root] if v!=parent]
    cs.sort()
    return "("+"".join(cs)+")"

def canonical_tree_code(n, edges):
    adj=adjacency(n,edges)
    cs=centers(n,edges)
    if len(cs)==1:
        return rooted_code(adj,cs[0],-1)
    a,b=cs
    ca=rooted_code(adj,a,b)
    cb=rooted_code(adj,b,a)
    x,y=sorted((ca,cb))
    return "("+x+y+")"

def unlabeled_trees(n):
    reps={}
    if n==2:
        return {"(())":(2,((0,1),))}
    for seq in product(range(n), repeat=n-2):
        _,edges=prufer_tree(seq)
        code=canonical_tree_code(n,edges)
        reps.setdefault(code,(n,edges))
    return reps

def degree_centralization(n, edges):
    adj=adjacency(n,edges)
    ds=[len(a) for a in adj]
    m=max(ds)
    return Fraction(sum(m-d for d in ds),(n-1)*(n-2))

def vertex_betweenness_tree(n, edges):
    adj=adjacency(n,edges)
    out=[]
    for v in range(n):
        sizes=[]
        seen={v}
        for w in adj[v]:
            if w in seen:
                continue
            stack=[w]; seen.add(w); size=0
            while stack:
                u=stack.pop(); size+=1
                for z in adj[u]:
                    if z not in seen:
                        seen.add(z); stack.append(z)
            sizes.append(size)
        b=sum(sizes[i]*sizes[j] for i in range(len(sizes)) for j in range(i+1,len(sizes)))
        out.append(b)
    return out

def betweenness_centralization(n, edges):
    bs=vertex_betweenness_tree(n,edges)
    m=max(bs)
    # Star maximum for unordered-pair point betweenness:
    # (n-1)*C(n-1,2).
    denom=(n-1)*(n-1)*(n-2)//2
    return Fraction(sum(m-b for b in bs),denom)

def spider(arms):
    # center 0; each arm is a path of the stated edge length
    edges=[]
    nxt=1
    for L in arms:
        prev=0
        for _ in range(L):
            edges.append((prev,nxt))
            prev=nxt; nxt+=1
    return nxt, tuple(sorted(tuple(sorted(e)) for e in edges))

all_reversals={}
for n in range(3,9):
    reps=unlabeled_trees(n)
    assert len(reps)==EXPECTED_TREE_COUNTS[n], (n,len(reps))
    vals=[]
    for code,(nn,edges) in reps.items():
        vals.append((code,degree_centralization(nn,edges),betweenness_centralization(nn,edges),edges))
    rev=[]
    for a,b in combinations(vals,2):
        if (a[1]-b[1])*(a[2]-b[2])<0:
            rev.append((a[0],b[0]))
    assert len(rev)==EXPECTED_REVERSALS[n], (n,len(rev))
    all_reversals[n]=rev

A=spider((4,1,1,1))
B=spider((3,2,2))
assert A[0]==B[0]==8
assert canonical_tree_code(*A) in unlabeled_trees(8)
assert canonical_tree_code(*B) in unlabeled_trees(8)
assert degree_centralization(*A)==Fraction(3,7)
assert betweenness_centralization(*A)==Fraction(11,21)
assert degree_centralization(*B)==Fraction(5,21)
assert betweenness_centralization(*B)==Fraction(4,7)
assert degree_centralization(*A)>degree_centralization(*B)
assert betweenness_centralization(*A)<betweenness_centralization(*B)

# Independent hand-count checks for the witness.
assert sorted(len(x) for x in adjacency(*A)) == [1,1,1,1,2,2,2,4]
assert vertex_betweenness_tree(*A) == [15,12,10,6,0,0,0,0]
assert sorted(vertex_betweenness_tree(*B), reverse=True) == [16,10,6,6,6,0,0,0]
assert sum(15-b for b in vertex_betweenness_tree(*A)) == 77
assert sum(16-b for b in vertex_betweenness_tree(*B)) == 84
assert Fraction(77,147)==Fraction(11,21)
assert Fraction(84,147)==Fraction(4,7)

print("VERIFY_OK")
print("tree_counts", EXPECTED_TREE_COUNTS)
print("strict_reversal_counts", EXPECTED_REVERSALS)
print("first_strict_reversal_order", 8)
print("A=S(4,1,1,1)", degree_centralization(*A), betweenness_centralization(*A))
print("B=S(3,2,2)", degree_centralization(*B), betweenness_centralization(*B))
print("n8_reversing_pair_count", len(all_reversals[8]))
