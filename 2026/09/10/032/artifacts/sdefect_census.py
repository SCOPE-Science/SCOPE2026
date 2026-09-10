"""Exact pruned-branching sdefect census for D_l, l=1..12 (stdlib only).

Branching order follows max-degree-first with edge-pruning; values stored in
original vertex order. For each 2-cover (entries 0..2, complete by Lemma C):
minimality by single-decrement test; J^2 membership by minimal-cover
pair-sum divisibility. Prints exact sdefect sequence.
"""
import time, sys
sys.setrecursionlimit(10000)

def build_D(l):
    verts = ['a1','a2','a3','b1','b2','b3'] + ([f'z{i}' for i in range(1,l)] if l>=2 else [])
    idx={v:i for i,v in enumerate(verts)}
    edges=[('a1','a2'),('a2','a3'),('a1','a3'),('b1','b2'),('b2','b3'),('b1','b3')]
    if l==1: edges.append(('a1','b1'))
    else:
        edges.append(('a1','z1'))
        for i in range(1,l-1): edges.append((f'z{i}',f'z{i+1}'))
        edges.append((f'z{l-1}','b1'))
    return verts,[(idx[u],idx[v]) for u,v in edges]

def census(l):
    t0=time.time()
    verts,E=build_D(l); n=len(verts)
    adj=[set() for _ in range(n)]
    for i,j in E: adj[i].add(j); adj[j].add(i)
    order=sorted(range(n),key=lambda i:-len(adj[i]))
    Slist=[]
    for mask in range(1<<n):
        if all(((mask>>i)&1 or (mask>>j)&1) for i,j in E): Slist.append(mask)
    mins=[s for s in Slist if not any((t&s)==t and t!=s for t in Slist)]
    sets=[{i for i in range(n) if (s>>i)&1} for s in mins]
    pair=[tuple((1 if i in c1 else 0)+(1 if i in c2 else 0) for i in range(n))
          for c1 in sets for c2 in sets]
    a=[0]*n; assigned=[False]*n
    n2=nmin2=nout=0
    def rec(k):
        nonlocal n2,nmin2,nout
        if k==n:
            n2+=1
            for v in range(n):
                if a[v]>=1:
                    if all((a[i]-1 if i==v else a[i])+(a[j]-1 if j==v else a[j])>=2
                           for i,j in E):
                        return
            nmin2+=1
            for p in pair:
                if all(p[i]<=a[i] for i in range(n)): return
            nout+=1
            return
        v=order[k]
        for x in (0,1,2):
            a[v]=x
            if all(not assigned[u] or a[v]+a[u]>=2 for u in adj[v]):
                assigned[v]=True; rec(k+1); assigned[v]=False
        a[v]=0
    rec(0)
    return dict(l=l,n=n,n2covers=n2,n_min2=nmin2,sdefect=nout,time=round(time.time()-t0,1))

if __name__=="__main__":
    import json
    rows=[census(l) for l in range(1,13)]
    for r in rows: print(r,flush=True)
    json.dump(rows,open("output/artifacts/sdefect_census.json","w"),indent=1)
    print("wrote output/artifacts/sdefect_census.json")
