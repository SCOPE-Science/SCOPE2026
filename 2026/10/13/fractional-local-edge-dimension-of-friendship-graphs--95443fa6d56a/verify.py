from itertools import combinations
from collections import deque
import numpy as np
from scipy.optimize import linprog

def friendship_graph(r):
    # center 0; blade i has outer vertices 2i-1, 2i
    n = 1 + 2*r
    adj = [set() for _ in range(n)]
    edges = []
    for i in range(r):
        a = 1 + 2*i
        b = a + 1
        for u,v in [(0,a),(0,b),(a,b)]:
            adj[u].add(v); adj[v].add(u)
            edges.append((min(u,v), max(u,v)))
    return adj, sorted(set(edges))

def all_dist(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D

def edge_dist(D,w,e):
    u,v=e
    return min(D[w][u],D[w][v])

def local_edge_neighborhoods(adj, edges, D):
    # constraints only for adjacent edges, i.e. edge pairs sharing an endpoint
    masks=[]
    pairs=[]
    for e1,e2 in combinations(edges,2):
        if len(set(e1)&set(e2)) != 1:
            continue
        mask=[]
        for w in range(len(adj)):
            if edge_dist(D,w,e1) != edge_dist(D,w,e2):
                mask.append(w)
        masks.append(tuple(mask))
        pairs.append((e1,e2))
    return pairs,masks

checked_pairs=0
lp_instances=0
uniqueness_coordinate_checks=0

for r in range(2,9):
    adj,edges=friendship_graph(r)
    D=all_dist(adj)
    pairs,masks=local_edge_neighborhoods(adj,edges,D)
    n=len(adj)
    checked_pairs += len(pairs)

    # Critical center-edge pairs: for any two distinct outer u,v,
    # edges 0u and 0v are adjacent and have exact resolver set {u,v}.
    mask_map={tuple(sorted((e1,e2))):set(mask) for (e1,e2),mask in zip(pairs,masks)}
    outers=list(range(1,n))
    for u,v in combinations(outers,2):
        e1=(0,u) if 0<u else (u,0)
        e2=(0,v) if 0<v else (v,0)
        key=tuple(sorted((e1,e2)))
        assert mask_map[key]=={u,v}, (r,u,v,mask_map[key])

    # Blade pair formulas.
    for i in range(r):
        a=1+2*i; b=a+1
        outside=set(outers)-{a,b}
        key=tuple(sorted(((0,a),(a,b))))
        assert mask_map[key]==({0,b}|outside), (r,i,"a",mask_map[key])
        key=tuple(sorted(((0,b),(a,b))))
        assert mask_map[key]==({0,a}|outside), (r,i,"b",mask_map[key])

    # Solve the actual fractional local edge LP from all adjacent-edge constraints.
    # minimize sum x_v; each mask constraint sum_{v in mask} x_v >= 1; 0<=x<=1.
    A=[]; bvec=[]
    for mask in masks:
        row=np.zeros(n)
        for v in mask: row[v]=-1.0
        A.append(row); bvec.append(-1.0)
    res=linprog(np.ones(n),A_ub=np.array(A),b_ub=np.array(bvec),
                bounds=[(0,1)]*n, method="highs")
    assert res.success
    assert abs(res.fun-r)<1e-8, (r,res.fun,res.x)
    lp_instances += 1

    candidate=np.array([0.0]+[0.5]*(2*r))
    assert all(sum(candidate[v] for v in mask)>=1-1e-12 for mask in masks)

    # Numerically certify uniqueness at the optimum by minimizing and maximizing
    # each coordinate over the optimal face sum x <= r.
    Aopt=np.vstack([np.array(A), np.ones(n)])
    bopt=np.concatenate([np.array(bvec), [r+1e-9]])
    for j in range(n):
        c=np.zeros(n); c[j]=1
        lo=linprog(c,A_ub=Aopt,b_ub=bopt,bounds=[(0,1)]*n,method="highs")
        hi=linprog(-c,A_ub=Aopt,b_ub=bopt,bounds=[(0,1)]*n,method="highs")
        assert lo.success and hi.success
        minv=lo.fun
        maxv=-hi.fun
        target=0.0 if j==0 else 0.5
        assert abs(minv-target)<2e-7 and abs(maxv-target)<2e-7, (r,j,minv,maxv,target)
        uniqueness_coordinate_checks += 1

print("VERIFY_OK")
print("friendship_parameters_checked = 2..8")
print("adjacent_edge_pairs_checked =", checked_pairs)
print("lp_instances =", lp_instances)
print("optimal_face_coordinate_checks =", uniqueness_coordinate_checks)
print("all center-edge resolver neighborhoods were exactly the two outer endpoints")
print("all blade-edge resolver neighborhoods matched the symbolic formulas")
print("all LP optima equaled r")
print("all optimum faces were the unique weighting: center 0, every outer vertex 1/2")
