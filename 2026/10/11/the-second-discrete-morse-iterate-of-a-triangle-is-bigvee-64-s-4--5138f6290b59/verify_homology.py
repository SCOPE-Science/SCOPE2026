"""Independent forest-root and mod-two homology check for a six-vertex prism."""
from collections import defaultdict
from itertools import product

V = range(6)
E = [(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)]
E = sorted(E)
incs = sorted((u, (u,v)) for u,v in E) + sorted((v, (u,v)) for u,v in E)
incs = sorted(incs, key=lambda x:(x[1],x[0]))
index = {p:i for i,p in enumerate(incs)}
faces = {0}
for eflags in range(1<<9):
    adj={v:[] for v in V}
    chosen=[E[i] for i in range(9) if eflags>>i & 1]
    for u,v in chosen:
        adj[u].append(v);adj[v].append(u)
    comps=[];seen=set()
    for v in V:
        if v in seen:continue
        stack=[v];comp=[];seen.add(v)
        while stack:
            a=stack.pop();comp.append(a)
            for b in adj[a]:
                if b not in seen: seen.add(b);stack.append(b)
        comps.append(comp)
    if len(comps)!=6-len(chosen):continue # forest test
    for roots in product(*comps):
        rootdict={v:r for c,r in zip(comps,roots) for v in c}
        flags=0
        for v in V:
            if v==rootdict[v]:continue
            # orient all tree edges toward the component's root
            root=rootdict[v]
            q=[root];par={root:None}
            for x in q:
                for y in adj[x]:
                    if y not in par:
                        par[y]=x;q.append(y)
            edge=tuple(sorted((v,par[v])))
            flags|=1<<index[(v,edge)]
        assert flags.bit_count()==len(chosen)
        faces.add(flags)
assert len(faces)==1728
bydim={d:sorted(f for f in faces if f.bit_count()==d+1) for d in range(5)}
assert [len(bydim[d]) for d in range(5)] == [18,126,428,705,450]

def rankmod2(cols):
    pivots={}
    for col in cols:
        while col:
            j=col.bit_length()
            if j in pivots: col ^= pivots[j]
            else:
                pivots[j]=col;break
    return len(pivots)

ranks=[]
for d in range(1,5):
    inds={f:i for i,f in enumerate(bydim[d-1])}
    cols=[]
    for f in bydim[d]:
        v=0
        for i in range(18):
            if (f>>i)&1: v ^= 1 << inds[f^(1<<i)]
        cols.append(v)
    ranks.append(rankmod2(cols))
assert ranks==[17,109,319,386], ranks
assert [len(bydim[d])-(1 if d==0 else ranks[d-1])-(ranks[d] if d<4 else 0) for d in range(5)] == [0,0,0,0,64]
print('HOMOLOGY_OK faces=%d ranks=%s reduced_F2_Betti=%s' % (len(faces)-1,ranks,[0,0,0,0,64]))
