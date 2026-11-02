"""Independent exact-arithmetic checks for bounded-Lipschitz graph grids.
Run: python3 bl_graph_dudley_checker.py (Python standard library only).
The exhaustive finite checks supplement, but do not replace, the general proof.
"""
from fractions import Fraction as Q
from itertools import combinations, product
from random import Random
from collections import deque

def diameter(n,edges):
    adj=[[] for _ in range(n)]
    for i,j in edges:adj[i].append(j);adj[j].append(i)
    D=0
    for start in range(n):
        ds=[-1]*n;ds[start]=0;todo=deque([start])
        while todo:
            x=todo.popleft()
            for y in adj[x]:
                if ds[y]<0:ds[y]=ds[x]+1;todo.append(y)
        assert min(ds)>=0
        D=max(D,max(ds))
    return D

def grid_vectors(n,edges,k):
    vals=range(-k,k+1,2)
    for z in product(vals,repeat=n):
        if all(abs(z[i]-z[j])<=2 for i,j in edges):
            yield z

def grid_dual(n,edges,masses):
    best=abs(sum(masses))
    for k in range(1,diameter(n,edges)+1):
        for z in grid_vectors(n,edges,k):
            best=max(best, sum(masses[i]*z[i] for i in range(n))/Q(k+2))
    return best

def dp_path(masses):
    n=len(masses)
    best=abs(sum(masses))
    for k in range(1,n):
        states=list(range(-k,k+1,2))
        d={s:masses[0]*s for s in states}
        for a in masses[1:]:
            d={s:a*s+max(d[t] for t in (s-2,s,s+2) if t in d) for s in states}
        best=max(best,max(d.values())/Q(k+2))
    return best

def inequalities(n,edges):
    rows=[]
    for i in range(n):
        for sign in (-1,1):
            v=[0]*(n+1);v[i]=sign;v[-1]=1;rows.append((tuple(v),1))
    for i,j in edges:
        for sign in (-1,1):
            v=[0]*(n+1);v[i]=sign;v[j]=-sign;v[-1]=-1;rows.append((tuple(v),0))
    v=[0]*(n+1);v[-1]=-1;rows.append((tuple(v),0))
    v=[0]*(n+1);v[-1]=1;rows.append((tuple(v),1))
    return rows

def solve_square(rows,n):
    aug=[[Q(c) for c in a]+[Q(b)] for a,b in rows]
    for col in range(n):
        pivot=next((i for i in range(col,n) if aug[i][col]),None)
        if pivot is None:return None
        aug[col],aug[pivot]=aug[pivot],aug[col]
        v=aug[col][col]; aug[col]=[x/v for x in aug[col]]
        for j in range(n):
            if j!=col and aug[j][col]:
                v=aug[j][col]
                aug[j]=[aug[j][h]-v*aug[col][h] for h in range(n+1)]
    return tuple(row[-1] for row in aug)

def vertices(n,edges):
    rows=inequalities(n,edges); candidates=set()
    for indices in combinations(range(len(rows)),n+1):
        v=solve_square([rows[i] for i in indices],n+1)
        if v is not None and all(sum(a[j]*v[j] for j in range(n+1))<=b for a,b in rows):
            candidates.add(v)
    return candidates

def boundary_extreme(v,edges):
    f,b=v[:-1],v[-1]
    M=max(map(abs,f));L=max(abs(f[i]-f[j]) for i,j in edges)
    return M+L==1 and b==L

def test_graph(n,edges):
    D=diameter(n,edges)
    V=[v for v in vertices(n,edges) if boundary_extreme(v,edges)]
    assert len(V)>0
    assert sum(v[-1]==0 for v in V)==2
    for v in V:
        f,b=v[:-1],v[-1]
        if not b:assert all(x==f[0] for x in f) and abs(f[0])==1;continue
        k=Q(2,b)-2
        assert k.denominator==1 and 1<=k<=D,(v,k)
        k=int(k)
        assert all((k+2)*x in range(-k,k+1,2) for x in f)
        assert all(abs(f[i]-f[j])<=b for i,j in edges)
    rng=Random(173+n*sum((i+1)*(j+1) for i,j in edges))
    for _ in range(18):
        a=[Q(rng.randint(-7,7)) for i in range(n)]
        from_vertices=max(sum(a[i]*v[i] for i in range(n)) for v in V)
        from_grids=grid_dual(n,edges,a)
        assert from_vertices==from_grids,(n,edges,a,from_vertices,from_grids)
    print('graph',n,edges,'boundary_vertices',len(V),'independent exact comparisons',18)
    return len(V)

def run():
    instances=[(2,[(0,1)]),(3,[(0,1),(1,2)]),
       (3,[(0,1),(1,2),(0,2)]),
       (4,[(0,1),(1,2),(2,3)]),
       (4,[(0,1),(0,2),(0,3)]),
       (4,[(0,1),(1,2),(2,3),(3,0)]),
       (4,[(i,j) for i in range(4) for j in range(i+1,4)])]
    total=0
    for n,e in instances:total+=test_graph(n,e)
    rng=Random(104729);cases=0
    for n in range(2,7):
        e=[(i,i+1) for i in range(n-1)]
        for _ in range(12):
            a=[Q(rng.randrange(-25,26),rng.randrange(1,10)) for i in range(n)]
            assert dp_path(a)==grid_dual(n,e,a)
            cases+=1
    print('PASS: exact projected-polytope enumeration',len(instances),'graphs,',total,'boundary vertices;',cases,'independent path DP/brute-grid comparisons')
if __name__=='__main__':run()
