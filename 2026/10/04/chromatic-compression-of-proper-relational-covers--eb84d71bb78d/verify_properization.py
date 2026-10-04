from itertools import product
import random

def conflict_graph(W, Rs):
    E=set()
    for x in W:
        for y in W:
            if x==y: continue
            if all((x,y) in R for R in Rs) or all((y,x) in R for R in Rs):
                E.add(tuple(sorted((x,y))))
    return E

def kcolor(W,E,k):
    adj={x:set() for x in W}
    for a,b in E: adj[a].add(b); adj[b].add(a)
    order=sorted(W,key=lambda x:-len(adj[x]))
    c={}
    def rec(i):
        if i==len(order): return c.copy()
        x=order[i]
        used={c[y] for y in adj[x] if y in c}
        for z in range(k):
            if z not in used:
                c[x]=z
                r=rec(i+1)
                if r is not None:return r
                del c[x]
        return None
    return rec(0)

def chromatic(W,E):
    for k in range(1,len(W)+1):
        c=kcolor(W,E,k)
        if c is not None:return k,c

def lift(W,Rs,c,q):
    WW=[(x,t) for x in W for t in range(q)]
    RRs=[]
    for i,R in enumerate(Rs):
        RR=set()
        for (x,t),(y,s) in product(WW,repeat=2):
            if (x,y) not in R: continue
            if i==0:
                if (t-c[x])%q==(s-c[y])%q: RR.add(((x,t),(y,s)))
            else:
                if t==s: RR.add(((x,t),(y,s)))
        RRs.append(RR)
    return WW,RRs

def proper(WW,RRs):
    for a,b in product(WW,repeat=2):
        if a!=b and all((a,b) in R for R in RRs):return False
    return True

def bounded(W,Rs,WW,RRs):
    for i,(R,RR) in enumerate(zip(Rs,RRs)):
        # forth
        for a,b in RR:
            if (a[0],b[0]) not in R:return False
        # back
        for a in WW:
            x=a[0]
            for y in W:
                if (x,y) in R:
                    if not any((a,b) in RR and b[0]==y for b in WW):return False
    return True

def prop(R, W, name):
    if name=='reflexive': return all((x,x) in R for x in W)
    if name=='symmetric': return all((y,x) in R for x,y in R)
    if name=='transitive': return all((x,z) in R for x,y in R for y2,z in R if y==y2)
    if name=='serial': return all(any((x,y) in R for y in W) for x in W)
    if name=='euclidean': return all((y,z) in R for x,y in R for x2,z in R if x==x2)
    raise ValueError

random.seed(4)
for m in range(2,7):
    W=list(range(m))
    for _ in range(50):
        Rs=[]
        for i in range(3):
            R={(x,y) for x in W for y in W if random.random()<.35}
            Rs.append(R)
        E=conflict_graph(W,Rs)
        q,c=chromatic(W,E)
        WW,RRs=lift(W,Rs,c,q)
        assert len(WW)==m*q
        assert proper(WW,RRs)
        assert bounded(W,Rs,WW,RRs)
# property-preserving examples (equivalences from random partitions)
for m in range(2,7):
    W=list(range(m))
    for _ in range(30):
        Rs=[]
        for i in range(3):
            labels=[random.randrange(max(1,m//2)) for _ in W]
            R={(x,y) for x in W for y in W if labels[x]==labels[y]}
            Rs.append(R)
        E=conflict_graph(W,Rs); q,c=chromatic(W,E); WW,RRs=lift(W,Rs,c,q)
        for R,RR in zip(Rs,RRs):
            for name in ['reflexive','symmetric','transitive','serial','euclidean']:
                assert not prop(R,W,name) or prop(RR,WW,name)
# C5 example q=3 and K_m q=m
W=list(range(5)); C5={(i,i) for i in W}
for i in W:
    C5.add((i,(i+1)%5)); C5.add(((i+1)%5,i))
E=conflict_graph(W,[C5,C5]); q,c=chromatic(W,E); assert q==3
W=list(range(5)); U={(x,y) for x in W for y in W}; E=conflict_graph(W,[U,U]); q,c=chromatic(W,E); assert q==5
print('VERIFY_OK')
