"""Reproducible finite checks for the tree total-variation proximal stability theorem.
Uses only Python's standard library; finite checks supplement the analytical proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from collections import deque
import random

def connected_components(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges: adj[u].append(v); adj[v].append(u)
    seen=set(); result=[]
    for root in range(n):
        if root in seen: continue
        stack=[root];seen.add(root);part=[]
        while stack:
            u=stack.pop();part.append(u)
            for v in adj[u]:
                if v not in seen: seen.add(v);stack.append(v)
        result.append(tuple(sorted(part)))
    return result

def cut_indicator(n, edges, ei):
    u,v=edges[ei]
    components=connected_components(n, edges[:ei]+edges[ei+1:])
    assert len(components)==2
    ones=set(next(c for c in components if v in c))
    return [F(int(j in ones)) for j in range(n)]

def variation(edges,x):
    return sum((abs(x[u]-x[v]) for u,v in edges),F(0))

def project(components,x):
    out=list(x)
    for A in components:
        mean=sum((x[j] for j in A), F(0))/len(A)
        for j in A:out[j]=mean
    return out

def formula(n,edges):
    ans=F(1)
    for bitmask in range(1,1<<n):
        A={v for v in range(n) if (bitmask>>v)&1}
        inside=[edge for edge in edges if edge[0] in A and edge[1] in A]
        if len(A)<2 or len(inside)!=len(A)-1:continue
        if len(connected_components(n,inside)) != n-len(A)+1:continue
        for e in inside:
            a,b=connected_components(n,inside[:inside.index(e)]+inside[inside.index(e)+1:])[:2]
            # Explicitly compute the two A components independently.
            adj={v:set() for v in A}
            for u,v in inside:
                if (u,v)!=e and (v,u)!=e:adj[u].add(v);adj[v].add(u)
            group=set();todo=[e[0]]
            while todo:
                u=todo.pop()
                if u in group:continue
                group.add(u);todo.extend(adj[u]-group)
            left=group;right=A-left
            tleft=sum((u in left and v not in A) or (v in left and u not in A) for u,v in edges)
            tright=sum((u in right and v not in A) or (v in right and u not in A) for u,v in edges)
            value=F(len(right)*tleft+len(left)*tright,len(A))
            ans=max(ans,value)
    return ans

def direct(n,edges):
    # Enumerate all possible fused-edge subsets and all edge-step extreme rays.
    best=F(0)
    for selected in product((0,1), repeat=len(edges)):
        blocks=connected_components(n,[edge for edge,yes in zip(edges,selected) if yes])
        for ei in range(len(edges)):
            h=cut_indicator(n,edges,ei)
            assert variation(edges,h)==1
            best=max(best,variation(edges,project(blocks,h)))
    return best

def tree_from_prufer(seq):
    n=len(seq)+2
    deg=[1]*n
    for v in seq:deg[v]+=1
    edges=[]
    for v in seq:
        u=next(i for i in range(n) if deg[i]==1)
        edges.append((u,v));deg[u]-=1;deg[v]-=1
    u,v=[i for i in range(n) if deg[i]==1]
    edges.append((u,v))
    return edges

def comb(m):
    return [(i,i+1) for i in range(m-1)]+[(i,m+i) for i in range(m)]

def verify_kkt_pair(n, edges, fused, base_u, chosen_cut, epsilon, expected):
    """Construct two actual data pairs and verify their prox fits via exact KKT."""
    inner=set(fused)
    h=cut_indicator(n,edges,chosen_cut)
    clusters=connected_components(n,[edges[j] for j in fused])
    ph=project(clusters,h)
    signs=[F(0) if i in inner else F(1 if base_u[v]>base_u[u] else -1)
           for i,(u,v) in enumerate(edges)]
    assert all(base_u[u]==base_u[v] for j,(u,v) in enumerate(edges) if j in inner)
    assert all(base_u[u]!=base_u[v] for j,(u,v) in enumerate(edges) if j not in inner)
    def bt(q):
        out=[F(0)]*n
        for (u,v),val in zip(edges,q):out[u]-=val;out[v]+=val
        return out
    y=[u+z for u,z in zip(base_u,bt(signs))]
    y2=[v+epsilon*t for v,t in zip(y,h)]
    u2=[v+epsilon*t for v,t in zip(base_u,ph)]
    rhs=[epsilon*(hi-pi) for hi,pi in zip(h,ph)]
    # For each fused tree block, solve B_F^T dz=rhs by successive leaf removal.
    dz=[F(0)]*len(edges)
    adj=[set() for _ in range(n)]
    for j in fused:
        a,b=edges[j];adj[a].add(j);adj[b].add(j)
    pending=set(fused)
    while pending:
        leaf=next(v for v in range(n) if len(adj[v])==1)
        j=next(iter(adj[leaf]));a,b=edges[j]
        other=b if leaf==a else a
        dz[j]=rhs[leaf]*(F(-1) if leaf==a else F(1))
        rhs[leaf]=0
        rhs[other]-=dz[j]*(F(-1) if other==a else F(1))
        adj[leaf].remove(j);adj[other].remove(j);pending.remove(j)
    assert all(z==0 for z in rhs)
    q2=[q+d for q,d in zip(signs,dz)]
    assert all(abs(q2[j])<1 for j in fused)
    assert all(q2[j]==signs[j] for j in range(len(edges)) if j not in inner)
    assert all(u2[a]==u2[b] for j,(a,b) in enumerate(edges) if j in inner)
    assert all((u2[b]-u2[a])*q2[j]>0 for j,(a,b) in enumerate(edges) if j not in inner)
    assert [v+z for v,z in zip(u2,bt(q2))]==y2
    assert [v+z for v,z in zip(base_u,bt(signs))]==y
    assert variation(edges,h)==1
    assert variation(edges,[a-b for a,b in zip(u2,base_u)])/epsilon==expected
    print('Certified finite pair: n=%d, TV amplification=%s; all KKT signs, stationarity exact.'%(n,expected))

def main():
    count=0
    for n in range(2,7):
        for seq in product(range(n),repeat=n-2):
            edges=tree_from_prufer(seq)
            x=formula(n,edges); y=direct(n,edges)
            assert x==y,(n,edges,x,y)
            count+=1
    print('All labeled trees through six vertices: verified',count,'exact formula-vs-all-fusion-pattern comparisons.')
    for n in range(1,10):
        edges=[(0,i) for i in range(1,n+1)]
        got=formula(n+1,edges)
        want=max(F(1),F(n-1,2))
        assert got==want,(n,got,want)
    print('Stars with 1..9 leaves: exact closed-form regression passed.')
    for n in range(2,10):
        edges=[(i,i+1) for i in range(n-1)]
        assert formula(n,edges)==1
    print('Paths with 2..9 vertices: exact nonexpansivity regression passed.')
    for m in range(2,9):
        edges=comb(m)
        lower=F(2*(m//2)*(m-m//2),m)
        # prescribed spine-fusion block and central spine cut
        blocks=[tuple(range(m))]+[(i,) for i in range(m,2*m)]
        h=cut_indicator(2*m,edges,(m-1)//2)
        got=variation(edges,project(blocks,h))
        assert got==lower,(m,got,lower)
    print('Maximum-degree-three combs with 2..8 spine vertices: exact witnesses passed.')
    star=[(0,i) for i in range(1,5)]
    verify_kkt_pair(5,star,[0],[F(0),F(0),F(10),F(20),F(30)],0,F(1,4),F(3,2))
    tree=comb(4)
    verify_kkt_pair(8,tree,[0,1,2],[F(0)]*4+[F(10),F(20),F(30),F(40)],1,F(1,4),F(2))

if __name__=='__main__': main()
