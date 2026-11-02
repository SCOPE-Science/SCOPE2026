"""Independent exhaustive tests and constructive DP for synchronized temporal proxy trees.
Only Python 3 standard library required.
"""
from itertools import product
from random import Random
import heapq

NEG = -10**80


def compatible_child(f, horizon, L):
    """For each parent action time t, maximize child subtree value over
    child action times s with s-horizon[s] <= t <= s.
    Return optimum and a maximizing child action time or zero if unavailable.
    """
    buckets = [[] for _ in range(L+1)]
    for s in range(1,L+1):
        if f[s] != NEG:
            left = s-horizon[s]
            assert 1 <= left <= s
            buckets[left].append((-f[s],s))
    pq=[]
    values=[NEG]*(L+1)
    arg=[0]*(L+1)
    for t in range(1,L+1):
        for p in buckets[t]: heapq.heappush(pq,p)
        while pq and pq[0][1] < t:
            heapq.heappop(pq)
        if pq:
            values[t] = -pq[0][0]
            arg[t] = pq[0][1]
    return values,arg


def optimum(n, parent, offers, horizons, root, casting_start):
    """Rooted undirected voter tree; one casting voter root, others delegates.
    Every (neighbor,time,weight) is an approved action; time ranges 1..L.
    Casting action is available independently to child paths at times
    casting_start..L. Delegating voters choose one time-stamped action total.
    Returns (optimal welfare, [(neighbor,time,weight) for each voter]) or None.
    """
    L=len(horizons[root])-1
    assert 1<=casting_start<=L
    children=[[] for _ in range(n)]
    for v in range(n):
        if v!=root:
            children[parent[v]].append(v)
    f=[None]*n
    chosen=[None]*n
    childarg=[None]*n
    def dfs(v):
        for c in children[v]: dfs(c)
        if v==root: return
        own=[NEG]*(L+1)
        ownaction=[None]*(L+1)
        for dest,t,w in offers[v]:
            if dest == parent[v] and w>own[t]:
                own[t]=w
                ownaction[t]=(dest,t,w)
        terms={}
        for c in children[v]:
            terms[c]=compatible_child(f[c],horizons[c],L)
        subtotal=[NEG]*(L+1)
        for t in range(1,L+1):
            if own[t]==NEG: continue
            terms_here=[terms[c][0][t] for c in children[v]]
            if any(z==NEG for z in terms_here):continue
            subtotal[t]=own[t]+sum(terms_here)
        f[v]=subtotal
        chosen[v]=ownaction
        childarg[v]={c:terms[c][1] for c in children[v]}
    dfs(root)
    rootarg={}
    total=0
    for c in children[root]:
        s=max(range(casting_start,L+1),key=lambda s:f[c][s])
        if f[c][s]==NEG:return None
        rootarg[c]=s
        total+=f[c][s]
    result=[None]*n
    def recover(v,t):
        assert chosen[v][t] is not None
        result[v]=chosen[v][t]
        for c in children[v]:
            recover(c,childarg[v][c][t])
    for c,t in rootarg.items(): recover(c,t)
    return total,result


def exhaustive(n,parent,offers,horizons,root,casting_start):
    """Directly enumerate every action choice, including wrong-way arcs,
    and check all path-to-caster and time conditions, with independent
    terminal timestamp choices. This does NOT use the DP recurrence.
    """
    voters=[v for v in range(n) if v!=root]
    if any(not offers[v] for v in voters):return None
    best=None
    for actions in product(*(offers[v] for v in voters)):
        d=dict(zip(voters,actions))
        score=sum(w for u,t,w in actions)
        if best is not None and score<best:continue
        ok=True
        for v in voters:
            seen=set()
            p=v
            while p!=root:
                if p in seen or p not in d:
                    ok=False;break
                seen.add(p)
                u,t,w=d[p]
                if u==root:
                    if t<casting_start:
                        ok=False;break
                else:
                    if u not in d:
                        ok=False;break
                    ut=d[u][1]
                    if not(t-horizons[p][t]<=ut<=t):
                        ok=False;break
                p=u
            if not ok:break
        if ok:best=score
    return best


def individually_feasible(start,offers,horizons,root,casting_start):
    seen=set()
    def go(v,last,lo):
        if v==root:return last>=casting_start
        for u,t,_ in offers[v]:
            if not(lo<=t<=last) or v in seen:continue
            seen.add(v)
            if go(u,t,t-horizons[v][t]):return True
            seen.remove(v)
        return False
    return go(start,len(horizons[root])-1,1)


def hard_witness():
    # voter 0 and 1 both delegate to voter 2, who delegates to casting 3.
    # Voters 0,1 demand action times 1,2 of voter 2, respectively.
    n,L,root=4,3,3
    parent=[2,2,3,None]
    offers=[[(2,1,1),(2,3,1)],
            [(2,2,1),(2,3,1)],
            [(3,1,1),(3,2,1),(0,3,1)], []]
    h=[[0]*(L+1) for _ in range(n)]
    assert all(individually_feasible(v,offers,h,root,1) for v in (0,1,2))
    assert all(any(t==L for _,t,_ in offers[v]) for v in (0,1,2))
    assert optimum(n,parent,offers,h,root,1) is None
    assert exhaustive(n,parent,offers,h,root,1) is None
    return True


def random_exact_tests():
    rng=Random(20261028)
    num=0
    feasible=0
    for n in range(2,7):
      for L in (2,3,4):
       for _ in range(260):
        root=0
        parent=[None]+[rng.randrange(v) for v in range(1,n)]
        offers=[[] for _ in range(n)]
        h=[[0]+[rng.randrange(t) for t in range(1,L+1)] for _ in range(n)]
        start=rng.randrange(1,L+1)
        for v in range(1,n):
            nbrs=[parent[v]]+[u for u in range(v+1,n) if parent[u]==v]
            for t in range(1,L+1):
                for u in nbrs:
                    if rng.random()<0.28:
                        offers[v].append((u,t,rng.randrange(1,8)))
            if not any(t==L for _,t,_ in offers[v]):
                offers[v].append((rng.choice(nbrs),L,rng.randrange(1,8)))
        nopts=1
        for v in range(1,n):nopts*=len(offers[v])
        if nopts>25000:continue
        fast=optimum(n,parent,offers,h,root,start)
        slow=exhaustive(n,parent,offers,h,root,start)
        assert (None if fast is None else fast[0]) == slow,(n,L,fast,slow,offers,h,parent,start)
        if fast is not None:
            feasible+=1
            assert sum(w for a in fast[1] if a is not None for _,_,w in [a])==slow
            assert exhaustive(n,parent,[[a] if a is not None else [] for a in fast[1]],h,root,start)==slow
        num+=1
    return num,feasible

if __name__=='__main__':
    hard_witness()
    n,nf=random_exact_tests()
    print(f'PASS: minimal four-voter obstruction; {n} independent exact-enumeration tests, {nf} feasible')
