import sys, time, json
sys.path.insert(0, "work")
from pair_layer import cells_of, oidx, sym_of, NO
orbits = [(er, ec, d) for er in (0, 1) for ec in (0, 1) for d in range(5)]
oidx2 = {o: i for i, o in enumerate(orbits)}
g0 = [oidx2[(0, ec, d)] for ec in (0, 1) for d in range(5)]
g1 = [oidx2[(1, ec, d)] for ec in (0, 1) for d in range(5)]
isingrp0 = [False]*NO
for i in g0: isingrp0[i]=True
fix = oidx2[(0,0,0)]
order = [i for i in g0 if i != fix] + list(g1)
X=[-1]*NO; X[fix]=0
used=[set() for _ in range(2)]; used[0].add(0)
col_used=[set() for _ in range(10)]
count=[0]; t0=time.time(); nodes=[0]
sys.setrecursionlimit(10000)
LOG=open("output/artifacts/latin_census.log","a",buffering=1)
def bt(k):
    nodes[0]+=1
    if nodes[0]%2000000==0:
        LOG.write(json.dumps({"nodes":nodes[0],"count":count[0],"t":round(time.time()-t0,1)})+"\n")
    if k==len(order):
        count[0]+=1
        return
    i=order[k]; u=used[0 if isingrp0[i] else 1]
    for v in range(10):
        if v in u: continue
        ok=True; touched=[]
        for (r,c) in cells_of[i]:
            s=sym_of(v,r)
            if s in col_used[c]: ok=False; break
            touched.append((c,s))
        if not ok: continue
        X[i]=v; u.add(v)
        for (c,s) in touched: col_used[c].add(s)
        bt(k+1)
        for (c,s) in touched: col_used[c].discard(s)
        u.discard(v); X[i]=-1
bt(0)
LOG.write(json.dumps({"DONE":True,"count":count[0],"nodes":nodes[0],"t":round(time.time()-t0,1)})+"\n")
print(json.dumps({"count":count[0],"nodes":nodes[0],"t":round(time.time()-t0,1)}))
