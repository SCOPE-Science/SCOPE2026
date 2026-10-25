"""Independent numerical rank checks for quantum absorption in triangular graphs.
Only standard Python and NumPy are required.
"""
import itertools
import random
import numpy as np

def bipartite_components(n,edges):
    neighbors=[set() for _ in range(n)]
    for u,v in edges:
        neighbors[u].add(v);neighbors[v].add(u)
    visited=set();count=0;all_balanced=True
    for start in range(n):
        if start in visited: continue
        stack=[start];col={start:0};visited.add(start);bip=True;sizes=[0,0]
        while stack:
            u=stack.pop();sizes[col[u]]+=1
            for v in neighbors[u]:
                if v not in col:
                    col[v]=1-col[u];visited.add(v);stack.append(v)
                elif col[v]==col[u]:
                    bip=False
        if bip:
            count+=1
            if sizes[0]!=sizes[1]: all_balanced=False
    return count,all_balanced

def predicted(n,F):
    edges=list(itertools.combinations(range(n),2))
    FS=set(F); complement=set(edges)-FS
    bF,balanced=bipartite_components(n,FS)
    bC,_=bipartite_components(n,complement)
    delta=int(balanced)
    return n+len(FS)+1-bF-bC-delta if FS else 0

def actual_projectors(n,all_edges):
    N=len(all_edges)
    U=np.zeros((n,N),dtype=float)
    for j,(a,b) in enumerate(all_edges):U[a,j]=U[b,j]=1
    P0=np.ones((N,N))/N
    C=np.eye(n)-np.ones((n,n))/n
    P1=U.T@C@U/(n-2)
    P2=np.eye(N)-P0-P1
    for P in (P0,P1,P2):
        assert np.linalg.norm(P@P-P,ord=np.inf)<1e-10
    return [P0,P1,P2]

def main():
    random.seed(421016)
    total=0
    for n in [5,6,7,8]:
        edges=list(itertools.combinations(range(n),2));N=len(edges)
        Ps=actual_projectors(n,edges)
        if n==5:
            masks=range(1,1<<N)
        else:
            masks=[random.getrandbits(N) for _ in range(500)]
        for mask in masks:
            ids=[j for j in range(N) if mask>>j&1]
            if not ids:continue
            F=[edges[j] for j in ids]
            a=sum(np.linalg.matrix_rank(P[:,ids],tol=5e-8) for P in Ps)
            p=predicted(n,F)
            assert a==p, (n,F,a,p)
            total+=1
        print('n',n,'checks',total)
    for n in [7,8,11,14]:
        edge_list=list(itertools.combinations(range(n),2))
        cyc=[(0,1),(1,2),(2,3),(0,3)]
        tri=[(0,1),(1,2),(0,2),(2,3)]
        Ps=actual_projectors(n,edge_list)
        r=[]
        for F in (cyc,tri):
            ix=[edge_list.index(e) for e in F]
            a=sum(np.linalg.matrix_rank(P[:,ix],tol=5e-8) for P in Ps)
            assert a==predicted(n,F)
            r.append(a)
        assert r==[8,9],(n,r)
        total+=2
    print('PASS',total,'independent finite projector-rank checks; 4-cycle rank 8 vs triangle-with-tail rank 9')
if __name__=='__main__':main()
