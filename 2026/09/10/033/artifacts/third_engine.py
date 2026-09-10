"""Third engine: max-insertion tree with DIRECT full pattern checks (no incremental filters)."""
import itertools
def std(p):
    s = sorted(p); r = {v:i+1 for i,v in enumerate(s)}
    return tuple(r[v] for v in p)
def contains(p, q):
    k=len(q)
    if k>len(p): return False
    for idx in itertools.combinations(range(len(p)), k):
        if std([p[i] for i in idx])==q: return True
    return False
P2413=(2,4,1,3); P3142=(3,1,4,2); T1=(1,2,3,6,5,4); T2=(3,2,1,6,5,4)
cur=[()]
res={}
for m in range(1,11):
    nxt=[]
    u=c1=c2=0
    for p in cur:
        for j in range(m):
            a=tuple(list(p[:j])+[m]+list(p[j:]))
            if contains(a,P2413) or contains(a,P3142): continue
            nxt.append(a)
            u+=1
            if not contains(a,T1): c1+=1
            if not contains(a,T2): c2+=1
    res[m]=(u,c1,c2); cur=nxt
    print(f"n={m}: U={u} C1={c1} C2={c2}", flush=True)
