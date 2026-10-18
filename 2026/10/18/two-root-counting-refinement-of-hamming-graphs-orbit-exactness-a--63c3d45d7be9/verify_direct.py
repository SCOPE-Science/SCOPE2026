"""Direct marked-Hamming color refinement; no third-party dependencies."""
from itertools import product
from collections import Counter, defaultdict

def labels(q,d,t):
    V=list(product(range(q), repeat=d)); idx={v:i for i,v in enumerate(V)}
    a=(0,)*d; b=(1,)*t+(0,)*(d-t)
    neighbors=[]
    for v in V:
        ns=[]
        for i in range(d):
            for z in range(q):
                if z!=v[i]:ns.append(idx[v[:i]+(z,)+v[i+1:]])
        neighbors.append(ns)
    orig=[0 if x!=a and x!=b else (1 if x==a else 2) for x in V]
    colors=orig[:]; rounds=0
    while True:
        signatures=[(colors[i],tuple(sorted(Counter(colors[j] for j in neighbors[i]).items()))) for i in range(len(V))]
        catalog={s:k for k,s in enumerate(sorted(set(signatures)))}
        new=[catalog[s] for s in signatures]
        if len(set(new))==len(set(colors)): break
        colors=new; rounds+=1
        assert rounds<=len(V)
    profiles=[]; triple=[]; pairs=[]
    for i,v in enumerate(V):
        aa=sum(v[j]==0 for j in range(t))
        bb=sum(v[j]==1 for j in range(t))
        cc=t-aa-bb
        ff=sum(v[j]!=0 for j in range(t,d))
        da=sum(z!=0 for z in v)
        db=sum(v[j]!=b[j] for j in range(d))
        count=sum((sum(V[j][h]!=0 for h in range(d))==da-1 and sum(V[j][h]!=b[h] for h in range(d))==db-1) for j in neighbors[i])
        assert count==ff
        profiles.append((aa,bb,cc,ff)); triple.append((da,db,count));pairs.append((da,db))
    csets=defaultdict(set); osets=defaultdict(set); tsets=defaultdict(set)
    for o,c,tr in zip(profiles,colors,triple): csets[c].add(o);osets[o].add(c);tsets[tr].add(o)
    assert all(len(x)==1 for x in csets.values())
    assert all(len(x)==1 for x in osets.values())
    assert all(len(x)==1 for x in tsets.values())
    expect=(t+1)*(d-t+1) if q==2 else ((t+1)*(t+2)//2)*(d-t+1)
    assert len(csets)==expect
    by_pair=defaultdict(set)
    for p,o in zip(pairs,profiles):by_pair[p].add(o)
    metric_exact=all(len(s)==1 for s in by_pair.values())
    assert metric_exact==(q==2 or t==1 or t==d)
    return len(V), rounds, expect

def main():
    configs=0;total_vertices=0;maxround=0
    for q,dmax in [(2,8),(3,6),(4,5),(5,4)]:
        for d in range(1,dmax+1):
            for t in range(1,d+1):
                n,rd,c=labels(q,d,t)
                configs+=1;total_vertices+=n;maxround=max(maxround,rd)
    print('DIRECT_OK configs=%s accumulated_vertices=%s maximum_refinement_rounds=%s'%(configs,total_vertices,maxround))
if __name__=='__main__': main()
