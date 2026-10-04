from itertools import combinations
from collections import deque

def lollipop(m,ell):
    # Clique vertices c=0,u_1,...,u_{m-1}; path p_1,...,p_ell has labels m,...,m+ell-1.
    n=m+ell
    adj=[set() for _ in range(n)]
    for i in range(m):
        for j in range(i+1,m):
            adj[i].add(j); adj[j].add(i)
    adj[0].add(m); adj[m].add(0)
    for j in range(ell-1):
        adj[m+j].add(m+j+1); adj[m+j+1].add(m+j)
    return adj

def distances(adj):
    n=len(adj)
    D=[[10**9]*n for _ in range(n)]
    for s in range(n):
        D[s][s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if D[s][v]==10**9:
                    D[s][v]=D[s][u]+1
                    q.append(v)
    return D

def edge_list(adj):
    return [(u,v) for u in range(len(adj)) for v in adj[u] if u<v]

def vertex_cover(E,mask):
    return all(((mask>>u)&1) or ((mask>>v)&1) for u,v in E)

def edge_resolving(E,D,mask,n):
    S=[s for s in range(n) if (mask>>s)&1]
    seen=set()
    for u,v in E:
        sig=tuple(min(D[s][u],D[s][v]) for s in S)
        if sig in seen:
            return False
        seen.add(sig)
    return True

def predicted_dim(m,ell):
    return m-1 + ell//2

def predicted_basis_count(m,ell):
    if ell%2:
        return m-1
    r=ell//2
    return (m-1)*(r+1)+1

graphs=subsets=vertex_covers=minimum_bases=0
for m in range(3,8):
    for ell in range(2,10):
        adj=lollipop(m,ell)
        D=distances(adj)
        E=edge_list(adj)
        n=len(adj)
        covers=[]
        demd=[]
        for mask in range(1<<n):
            subsets += 1
            if vertex_cover(E,mask):
                vertex_covers += 1
                assert edge_resolving(E,D,mask,n), (m,ell,mask)
                covers.append(mask)
                demd.append(mask)
        minsize=min(mask.bit_count() for mask in covers)
        assert minsize==predicted_dim(m,ell), (m,ell,minsize,predicted_dim(m,ell))
        bases=[mask for mask in covers if mask.bit_count()==minsize]
        assert len(bases)==predicted_basis_count(m,ell), (m,ell,len(bases),predicted_basis_count(m,ell))
        minimum_bases += len(bases)

        # Structural classification of minimum covers.
        c=0
        path=list(range(m,m+ell))
        clique_nonroot=list(range(1,m))
        for mask in bases:
            if (mask>>c)&1:
                # exactly one nonroot clique vertex omitted;
                # path part is a minimum vertex cover of P_ell.
                assert sum((mask>>x)&1 for x in clique_nonroot)==m-2
                pathmask=sum(((mask>>x)&1)<<i for i,x in enumerate(path))
                # direct path cover / size check
                assert pathmask.bit_count()==ell//2
                assert all(((pathmask>>i)&1) or ((pathmask>>(i+1))&1) for i in range(ell-1))
            else:
                # This minimum case exists only for even ell:
                # all other clique vertices and p1 are selected.
                assert ell%2==0
                assert all((mask>>x)&1 for x in clique_nonroot)
                assert (mask>>path[0])&1
        graphs += 1

print("VERIFY_OK")
print("lollipop_parameter_pairs_checked =",graphs)
print("vertex_subsets_checked =",subsets)
print("vertex_covers_checked =",vertex_covers)
print("minimum_bases_checked =",minimum_bases)
print("parameters m = 3..7, ell = 2..9")
print("every vertex cover was directly verified to edge-resolve")
print("all dominant edge metric dimensions matched m-1+floor(ell/2)")
print("all minimum-basis counts matched the parity formulas")
print("all minimum-basis structural classifications matched")
