"""Exact witness construction and finite checks for degree-two interval housing.

No third-party packages are used. Houses 0..n-1 are candidate vacant sites.
Each resident constraint is (tuple of 0, 1 or 2 distinct neighboring sites,
lowest acceptable count, highest acceptable count). Each candidate site
occurs in at most two resident-neighborhood lists.
"""
from collections import defaultdict, deque
from itertools import product
from random import Random


def solve(n, constraints, requested=None):
    """Return (minimum feasible subset, maximum feasible subset, k-witness).

    None means globally infeasible; when k is outside the feasible range,
    the third output is None. Runs in O(n + number of constraints).
    """
    unary = [set((0, 1)) for _ in range(n)]
    pairs = {}
    degrees = [0]*n
    for sites, lo, hi in constraints:
        assert len(set(sites)) == len(sites) and 0 <= lo <= hi <= len(sites)
        for a in sites:
            assert 0 <= a < n
            degrees[a] += 1
        if not sites:
            if lo > 0: return None
        elif len(sites) == 1:
            unary[sites[0]] &= {b for b in (0,1) if lo <= b <= hi}
        elif len(sites) == 2:
            a,b = sorted(sites)
            key=(a,b)
            old=pairs.get(key,(0,2))
            pairs[key]=(max(lo,old[0]),min(hi,old[1]))
        else:
            raise ValueError('maximum resident degree exceeded')
    if any(d>2 for d in degrees):
        raise ValueError('maximum candidate degree exceeded')
    if any(not x for x in unary) or any(lo>hi for lo,hi in pairs.values()):
        return None
    adj = [[] for _ in range(n)]
    for a,b in pairs:
        adj[a].append(b);adj[b].append(a)
    assert all(len(x)<=2 for x in adj)
    visited=[False]*n
    components=[]
    for first in range(n):
        if visited[first]: continue
        # Follow a path from an endpoint, or follow a full cycle.
        stack=[first];group=[];visited[first]=True
        while stack:
            a=stack.pop();group.append(a)
            for b in adj[a]:
                if not visited[b]: visited[b]=True;stack.append(b)
        if any(len(adj[v])<=1 for v in group):
            start=next(v for v in group if len(adj[v])<=1)
            cyclic=False
        else:
            start=group[0];cyclic=True
        order=[];prev=None;cur=start
        while True:
            order.append(cur)
            nxt=[v for v in adj[cur] if v!=prev]
            if not nxt: break
            nxt=nxt[0]
            if nxt==start:
                assert cyclic and len(order)==len(group)
                break
            prev,cur=cur,nxt
            assert len(order)<=len(group)
        assert len(order)==len(group)
        components.append((order,cyclic))

    def best_on(order,cyclic,maximize):
        best=None
        trials=(0,1) if cyclic else (None,)
        for initial in trials:
            dp={b:b for b in (0,1) if b in unary[order[0]] and (initial is None or b==initial)}
            back=[]
            for i in range(1,len(order)):
                a,b=order[i-1],order[i]
                lo,hi=pairs[(min(a,b),max(a,b))]
                new={};pred={}
                for cur in (0,1):
                    if cur not in unary[b]:continue
                    opts=[(val+cur,old) for old,val in dp.items() if lo<=old+cur<=hi]
                    if opts:
                        val,old=(max(opts) if maximize else min(opts))
                        new[cur]=val;pred[cur]=old
                dp=new;back.append(pred)
            options=[]
            for final,val in dp.items():
                if not cyclic or (pairs[(min(order[0],order[-1]),max(order[0],order[-1]))][0]
                                    <= initial+final <=
                                    pairs[(min(order[0],order[-1]),max(order[0],order[-1]))][1]):
                    options.append((val,final))
            if not options:continue
            score,last=max(options) if maximize else min(options)
            out=[0]*len(order);out[-1]=last
            for j in range(len(order)-2,-1,-1):
                out[j]=back[j][out[j+1]]
            if best is None or (score>best[0] if maximize else score<best[0]):
                best=(score,dict(zip(order,out)))
        return best
    lower=[0]*n;upper=[0]*n
    for order,cyclic in components:
        lo=best_on(order,cyclic,False)
        hi=best_on(order,cyclic,True)
        if lo is None or hi is None:return None
        for v,x in lo[1].items():lower[v]=x
        for v,x in hi[1].items():upper[v]=x
    lower=tuple(lower);upper=tuple(upper)
    if requested is None: return (lower,upper,None)
    k=requested
    if not sum(lower)<=k<=sum(upper):return (lower,upper,None)
    if k==sum(lower):return (lower,upper,lower)
    if k==sum(upper):return (lower,upper,upper)
    # Disagreement-switching formula.  Switch i=1 selects upper[i] instead
    # of lower[i].  A forbidden mixed state yields one directed implication.
    D=[i for i in range(n) if lower[i]!=upper[i]]
    Dset=set(D)
    arc=[[] for _ in range(n)];rev=[[] for _ in range(n)]
    for (a,b),(lo,hi) in pairs.items():
        if a not in Dset or b not in Dset: continue
        if not lo<=upper[a]+lower[b]<=hi:
            arc[a].append(b);rev[b].append(a)
        if not lo<=lower[a]+upper[b]<=hi:
            arc[b].append(a);rev[a].append(b)
    # Iterative Kosaraju, O(n); isolated disagreement vertices are singleton SCCs.
    seen=set();post=[]
    for start in D:
        if start in seen:continue
        seen.add(start);stack=[(start,0)]
        while stack:
            u,j=stack[-1]
            if j<len(arc[u]):
                v=arc[u][j];stack[-1]=(u,j+1)
                if v not in seen:
                    seen.add(v);stack.append((v,0))
            else:
                post.append(u);stack.pop()
    comp={};members=[]
    for start in reversed(post):
        if start in comp:continue
        cid=len(members);members.append([]);stack=[start];comp[start]=cid
        while stack:
            u=stack.pop();members[cid].append(u)
            for v in rev[u]:
                if v not in comp:comp[v]=cid;stack.append(v)
    out=[set() for _ in members];indeg=[0]*len(members)
    for u in D:
        for v in arc[u]:
            i,j=comp[u],comp[v]
            if i!=j and j not in out[i]:out[i].add(j);indeg[j]+=1
    queue=deque(i for i,d in enumerate(indeg) if not d)
    topo=[]
    while queue:
        i=queue.popleft();topo.append(i)
        for j in out[i]:
            indeg[j]-=1
            if not indeg[j]:queue.append(j)
    assert len(topo)==len(members)
    result=list(lower);cnt=sum(result)
    for cid in reversed(topo):
        jump=sum(upper[v]-lower[v] for v in members[cid])
        assert abs(jump)<=1, ('invalid structural bound',members[cid],jump)
        for v in members[cid]:result[v]=upper[v]
        cnt+=jump
        if cnt==k:return (lower,upper,tuple(result))
    raise AssertionError('cardinality path did not cross requested value')


def brute(n, constraints):
    out={}
    for v in product((0,1),repeat=n):
        if all(lo<=sum(v[u] for u in sites)<=hi for sites,lo,hi in constraints):
            out.setdefault(sum(v),v)
    return out


def verify_case(n,constraints):
    observed=brute(n,constraints)
    answer=solve(n,constraints)
    if not observed:
        assert answer is None
        return
    assert answer is not None
    low,high,_=answer
    assert sum(low)==min(observed) and sum(high)==max(observed)
    assert set(observed)==set(range(min(observed),max(observed)+1)),(n,constraints,observed)
    for k in range(0,n+1):
        witness=solve(n,constraints,k)[2]
        if k in observed:
            assert witness is not None
            assert sum(witness)==k
            assert all(lo<=sum(witness[u] for u in sites)<=hi for sites,lo,hi in constraints)
        else:assert witness is None


def main():
    intervals=((0,0),(1,1),(2,2),(0,1),(1,2),(0,2))
    trials=0
    # Every possible list of interval constraints on small path/cycle incidence graphs.
    for n in range(1,6):
        for base in ('path','cycle'):
            if base=='cycle' and n<3:continue
            edges=[(i,i+1) for i in range(n-1)]
            if base=='cycle':edges.append((n-1,0))
            for inds in product(range(6),repeat=len(edges)):
                constraints=[(edges[j],*intervals[x]) for j,x in enumerate(inds)]
                verify_case(n,constraints);trials+=1
    print('exhaustive path/cycle constraint systems:',trials)
    rng=Random(20261028)
    random_cases=0
    for case in range(2400):
        n=rng.randrange(1,12)
        base=rng.choice(['path','cycle'])
        edges=[(i,i+1) for i in range(n-1)]
        if base=='cycle' and n>=3:edges.append((n-1,0))
        cons=[(e,*intervals[rng.randrange(6)]) for e in edges]
        for i in range(n):
            if rng.random()<0.18:
                lo,hi=rng.choice(((0,0),(1,1),(0,1)))
                cons.append(((i,),lo,hi))
        # Incidence degree can exceed two when unary constraints adjoin cycle.
        if all(sum(u in sites for sites,_,_ in cons)<=2 for u in range(n)):
            verify_case(n,cons);random_cases+=1
    print('random feasible-incidence systems:',random_cases)
    # Three-arm exact-one star: its spectrum is {1,3}, so degree 3 is sharp.
    star=[((0,i),1,1) for i in (1,2,3)]
    assert set(brute(4,star))=={1,3}
    try:solve(4,star)
    except ValueError:pass
    else:raise AssertionError('degree-three instance should exceed solver contract')
    print('sharp degree-three counterexample: four sites, three residents, sizes {1,3}')
    # Large constructive consistency check, not an asymptotic timing certificate.
    n=10000
    long_cons=[((i,i+1),1,1) for i in range(0,n-1,3)]
    ans=solve(n,long_cons,(n//3)+2)
    assert ans is not None and ans[2] is not None
    assert sum(ans[2])==(n//3)+2
    assert all(lo<=sum(ans[2][j] for j in sites)<=hi for sites,lo,hi in long_cons)
    print('large construction: 10000 candidate sites; feasible requested count verified')


if __name__=='__main__':main()
