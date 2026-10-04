#!/usr/bin/env python3
from itertools import product, combinations

def tree_from_prufer(n, seq):
    if n == 1:
        return []
    if n == 2:
        return [(0, 1)]
    deg = [1] * n
    for x in seq:
        deg[x] += 1
    edges = []
    for x in seq:
        leaf = next(i for i in range(n) if deg[i] == 1)
        edges.append((leaf, x))
        deg[leaf] -= 1
        deg[x] -= 1
    rem = [i for i in range(n) if deg[i] == 1]
    edges.append(tuple(rem))
    return edges

def adj_und(n, edges):
    A=[[] for _ in range(n)]
    for u,v in edges:
        A[u].append(v); A[v].append(u)
    return A

def unique_path(A,s,t):
    parent={s:-1}; q=[s]
    for u in q:
        if u==t: break
        for v in A[u]:
            if v not in parent:
                parent[v]=u; q.append(v)
    p=[]; x=t
    while x!=-1:
        p.append(x); x=parent[x]
    return p[::-1]

def orient_edges(edges, mask):
    arcs=set()
    for i,(u,v) in enumerate(edges):
        arcs.add((v,u) if (mask>>i)&1 else (u,v))
    return arcs

def directed_path(A, arcs, s, t):
    p=unique_path(A,s,t)
    return p if all((p[i],p[i+1]) in arcs for i in range(len(p)-1)) else None

def reachability(n,A,arcs):
    R=[[False]*n for _ in range(n)]
    for i in range(n): R[i][i]=True
    for s in range(n):
        for t in range(n):
            if s!=t and directed_path(A,arcs,s,t) is not None:
                R[s][t]=True
    return R

def direct_gp_ok(S,n,A,arcs):
    SS=set(S)
    # Direct definition: no directed geodesic contains three selected vertices.
    for s in range(n):
        for t in range(n):
            if s==t: continue
            p=directed_path(A,arcs,s,t)
            if p is not None and sum(v in SS for v in p)>=3:
                return False
    return True

def two_family_ok(S,R):
    for x,y,z in combinations(S,3):
        tri=(x,y,z)
        for a,b,c in ((tri[0],tri[1],tri[2]),(tri[0],tri[2],tri[1]),(tri[1],tri[0],tri[2]),
                      (tri[1],tri[2],tri[0]),(tri[2],tri[0],tri[1]),(tri[2],tri[1],tri[0])):
            if a!=b and b!=c and R[a][b] and R[b][c]:
                return False
    return True

def max_subset(n,pred):
    best=0
    for mask in range(1<<n):
        k=mask.bit_count()
        if k<=best: continue
        S=[i for i in range(n) if (mask>>i)&1]
        if pred(S): best=k
    return best

def set_partitions(items):
    if not items:
        yield []
        return
    first=items[0]
    for p in set_partitions(items[1:]):
        yield [[first]]+[b[:] for b in p]
        for i in range(len(p)):
            q=[b[:] for b in p]
            q[i]=[first]+q[i]
            yield q

def is_chain(block,R):
    for a,b in combinations(block,2):
        if not (R[a][b] or R[b][a]):
            return False
    return True

def chain_partition_min(n,R):
    best=10**9
    for p in set_partitions(list(range(n))):
        if all(is_chain(b,R) for b in p):
            val=sum(min(2,len(b)) for b in p)
            if val<best: best=val
    return best

def main():
    total=0
    by_n={}
    for n in range(1,7):
        seqs=[()] if n<=2 else product(range(n), repeat=n-2)
        count=0
        for seq in seqs:
            edges=tree_from_prufer(n,seq)
            A=adj_und(n,edges)
            for mask in range(1<<len(edges)):
                arcs=orient_edges(edges,mask)
                R=reachability(n,A,arcs)
                g=max_subset(n,lambda S: direct_gp_ok(S,n,A,arcs))
                a=max_subset(n,lambda S: two_family_ok(S,R))
                m=chain_partition_min(n,R)
                assert g==a==m, (n,seq,mask,g,a,m)
                count+=1; total+=1
        by_n[n]=count
    assert total==43615, total
    print('ALL CHECKS PASSED; cases=%d; by_n=%s' % (total, by_n))
if __name__=='__main__':
    main()
