from itertools import product, combinations

def forest(edges,n):
    p=list(range(n))
    def root(x):
        while x!=p[x]:x=p[x]
        return x
    for u,v in edges:
        a,b=root(u),root(v)
        if a==b:return False
        p[a]=b
    return True

def subset_sequence(n,arcs,init=0):
    adj=[0]*n
    for u,v in arcs:adj[u]|=1<<v
    q=1<<init; at={}; seq=[]
    while q not in at:
        at[q]=len(seq);seq.append(q)
        nextq=0
        for u in range(n):
            if (q>>u)&1: nextq|=adj[u]
        q=nextq
    p=len(seq)-at[q]
    return p,at[q],len(seq),seq

for n in range(1,5):
    pairs=list(combinations(range(n),2))
    count=0; maxstart=0; maxperiod=0
    for dirs in product(range(4),repeat=len(pairs)):
        support=[e for e,a in zip(pairs,dirs) if a]
        if not forest(support,n):continue
        arcs=[]
        for (u,v),a in zip(pairs,dirs):
            if a&1:arcs.append((u,v))
            if a&2:arcs.append((v,u))
        p,t,k,seq=subset_sequence(n,arcs)
        assert p<=2,(n,arcs,p,t,k)
        count+=1;maxstart=max(maxstart,t);maxperiod=max(maxperiod,p)
    print(n,count,maxstart,maxperiod)
print('VERIFY_OK')
