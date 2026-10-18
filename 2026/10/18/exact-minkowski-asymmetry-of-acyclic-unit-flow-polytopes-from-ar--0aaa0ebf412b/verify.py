"""Exact enumerative checks for the unit DAG-flow asymmetry/arc-poset theorem.
No external packages. Run: python verify.py
"""
from itertools import combinations
from functools import lru_cache
import random

def routes(n, arcs):
    out=[[] for _ in range(n)]; indeg=[0]*n
    for idx,(u,v) in enumerate(arcs):
        out[u].append((v,idx)); indeg[v]+=1
    ans=[]
    def rec(v, bits):
        if not out[v]:
            if bits: ans.append(bits)
            return
        for w,idx in out[v]:rec(w,bits|(1<<idx))
    for v in range(n):
        if indeg[v]==0:rec(v,0)
    return sorted(set(ans))

def calc(n,arcs):
    m=len(arcs); full=(1<<m)-1
    if m==0:return None
    paths=routes(n,arcs)
    assert all(any((p>>i)&1 for p in paths) for i in range(m))
    # Arc precedence is independently obtained from vertex reachability.
    reach=[[False]*n for _ in range(n)]
    for a,b in arcs:reach[a][b]=True
    for k in range(n):
        for i in range(n):
            for j in range(n):
                reach[i][j] |= reach[i][k] and reach[k][j]
    before=lambda i,j: arcs[i][1]==arcs[j][0] or reach[arcs[i][1]][arcs[j][0]]
    incomparable=[0]*m
    for i in range(m):
        for j in range(m):
            if i!=j and not before(i,j) and not before(j,i): incomparable[i]|=1<<j
    antichains=[]
    for mask in range(1,1<<m):
        if all(((mask & ~(1<<i)) & ~incomparable[i])==0 for i in range(m) if mask>>i&1):
            antichains.append(mask)
    width=max(a.bit_count() for a in antichains)
    # Independent exact set-cover dynamic program; not using Dilworth in computation.
    @lru_cache(None)
    def dp(uncovered):
        if not uncovered:return ()
        bit=uncovered & -uncovered
        return min(((p,)+dp(uncovered & ~p) for p in paths if p&bit),key=len)
    cover=dp(full)
    assert len(cover)==width,(n,arcs,width,len(cover))
    # Explicit reflection certificate. w*c-v is a nonnegative integral flow of size w-1.
    totals=[sum((p>>i)&1 for p in cover) for i in range(m)]
    for v in paths:
        rem=[totals[i]-((v>>i)&1) for i in range(m)]
        assert all(z>=0 for z in rem)
        for vert in range(n):
            inward=sum(rem[i] for i,(u,w) in enumerate(arcs) if w==vert)
            outward=sum(rem[i] for i,(u,w) in enumerate(arcs) if u==vert)
            if any(w==vert for _,w in arcs) and any(u==vert for u,_ in arcs):
                assert inward==outward
        source={v for v in range(n) if not any(b==v for a,b in arcs)}
        assert sum(rem[i] for i,(u,vv) in enumerate(arcs) if u in source)==width-1
    # Every largest antichain gives a sharp lower-bound certificate.
    for mask in antichains:
        if mask.bit_count()==width: assert all((mask&p).bit_count()<=1 for p in paths)
    return len(paths),width,len(cover),len(antichains),m

def run():
    counts=[0,0,0,0,0]
    for n in (3,4,5):
        all_arcs=list(combinations(range(n),2))
        for mask in range(1,1<<len(all_arcs)):
            a=[e for i,e in enumerate(all_arcs) if (mask>>i)&1]
            x=calc(n,a)
            if x:
                counts[0]+=1;counts[1]+=x[0];counts[2]+=x[2];counts[3]+=x[3];counts[4]+=len(a)
    rng=random.Random(20261011)
    all_arcs=list(combinations(range(6),2))
    for trial in range(300):
        a=[e for e in all_arcs if rng.randrange(4)<2]
        if a:
            x=calc(6,a)
            counts[0]+=1;counts[1]+=x[0];counts[2]+=x[2];counts[3]+=x[3];counts[4]+=len(a)
    print('PASS exact enumeration:',counts[0],'DAGs,',counts[1],
          'source-sink routes,',counts[2],'selected covering routes,',
          counts[3],'antichains,',counts[4],'total arc incidences')
if __name__=='__main__':run()
