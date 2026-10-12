from itertools import product
from collections import Counter
from math import prod

# Vertices: 0 is the universal center; each subsequent block is one clique blade.
def build(ms):
    N=1+sum(ms)
    adj=[set() for _ in range(N)]
    off=1
    for m in ms:
        vs=list(range(off,off+m)); off+=m
        for v in vs:
            adj[0].add(v); adj[v].add(0)
        for i in range(m):
            for j in range(i+1,m):
                adj[vs[i]].add(vs[j]); adj[vs[j]].add(vs[i])
    return adj

def support_dominates(f,adj):
    P={i for i,a in enumerate(f) if a>0}
    return all(i in P or any(j in P for j in adj[i]) for i in range(len(f)))

def is_wrdf(f,adj):
    for u,a in enumerate(f):
        if a!=0:
            continue
        ok=False
        for v in adj[u]:
            if f[v]>0:
                g=list(f)
                g[u]=1
                g[v]-=1
                if support_dominates(g,adj):
                    ok=True
                    break
        if not ok:
            return False
    return True

def classified(f,ms):
    s=f[0]
    off=1
    empty=0
    for m in ms:
        if all(x==0 for x in f[off:off+m]):
            empty+=1
        off+=m
    return s==2 or (s==1 and empty<=1) or (s==0 and empty==0)

def mul(a,b):
    c=Counter()
    for i,x in a.items():
        for j,y in b.items():
            c[i+j]+=x*y
    return c

def power(base,k):
    out=Counter({0:1})
    for _ in range(k):
        out=mul(out,base)
    return out

def formula(ms):
    T=Counter({0:1,1:1,2:1})
    As=[]
    for m in ms:
        a=power(T,m)
        a[0]-=1
        As.append(+a)
    all_nonempty=Counter({0:1})
    for a in As:
        all_nonempty=mul(all_nonempty,a)
    out=Counter()
    for d,c in power(T,sum(ms)).items():
        out[d+2]+=c
    for d,c in all_nonempty.items():
        out[d]+=c
        out[d+1]+=c
    for i in range(len(ms)):
        q=Counter({0:1})
        for j,a in enumerate(As):
            if i!=j:
                q=mul(q,a)
        for d,c in q.items():
            out[d+1]+=c
    return +out

cases=[(2,2),(2,3),(3,3),(2,2,2),(2,2,3),(2,3,3)]
labelings=0
coefficient_checks=0
minimum_checks=0
for ms in cases:
    adj=build(ms)
    cnt=Counter()
    for f in product(range(3),repeat=len(adj)):
        direct=is_wrdf(f,adj)
        structural=classified(f,ms)
        labelings+=1
        if direct!=structural:
            raise SystemExit(('criterion mismatch',ms,f,direct,structural))
        if direct:
            cnt[sum(f)]+=1
    predicted=formula(ms)
    if cnt!=predicted:
        raise SystemExit(('polynomial mismatch',ms,cnt,predicted))
    coefficient_checks+=len(set(cnt)|set(predicted))
    r=len(ms)
    observed=(min(cnt),cnt[min(cnt)])
    if r==2:
        expected=(2,1+sum(ms)+prod(ms))
    else:
        expected=(2,1)
    if observed!=expected:
        raise SystemExit(('minimum mismatch',ms,observed,expected))
    minimum_checks+=1
print(f'VERIFY_OK cases={len(cases)} labelings={labelings} coefficient_checks={coefficient_checks} minimum_checks={minimum_checks} max_order={max(1+sum(ms) for ms in cases)}')
