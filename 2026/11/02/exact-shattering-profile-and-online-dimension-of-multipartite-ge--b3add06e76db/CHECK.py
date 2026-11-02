"""Independent finite checks for geodesically convex vertex classes in multipartite graphs."""
from itertools import product, combinations
from functools import lru_cache
from math import comb

def masks(parts):
    starts=[]; t=0
    for n in parts:
        starts.append(list(range(t,t+n))); t+=n
    N=t; allmask=(1<<N)-1
    # Independently check shortest-path intervals (distance at most 2).
    def isconvex(s):
        verts=[v for v in range(N) if s>>v&1]
        for u,v in combinations(verts,2):
            if any(u in p and v in p for p in starts):
                other=allmask
                for p in starts:
                    if u in p:
                        for w in p: other &= ~(1<<w)
                        break
                if other & ~s: return False
        return True
    return starts,N,[s for s in range(1<<N) if isconvex(s)]

def rank(cs,N):
    @lru_cache(None)
    def rec(states):
        best=0
        for p in range(N):
            a=tuple(c for c in states if c>>p&1)
            if not a or len(a)==len(states):continue
            b=tuple(c for c in states if not (c>>p&1))
            val=1+min(rec(a),rec(b))
            if val>best:best=val
        return best
    return rec(tuple(cs)),rec.cache_info().currsize

def verify(parts):
    starts,N,cs=masks(parts)
    full=(1<<N)-1
    expected=set([full])
    for choices in product(*([[-1]+p for p in starts])):
        mask=0
        for x in choices:
            if x>=0: mask|=1<<x
        expected.add(mask)
    assert set(cs)==expected,(parts,len(cs),len(expected))
    bysize={}
    for z in range(N+1):
        n=0
        for S0 in combinations(range(N),z):
            support=sum(1<<j for j in S0)
            traces=set(c&support for c in cs)
            valid=len(traces)==(1<<z)
            istransversal=all(sum(bool(support>>j&1) for j in p)<=1 for p in starts)
            ispair=(z==2 and any(sum(bool(support>>j&1) for j in p)==2 for p in starts))
            assert valid==(istransversal or ispair),(parts,S0,valid,istransversal,ispair)
            n+=valid
        bysize[z]=n
    phi=[0]*(N+1);phi[0]=1
    for p in starts:
        new=[0]*(N+1)
        for i,x in enumerate(phi):
            if x:
                new[i]+=x
                if i+1<=N:new[i+1]+=len(p)*x
        phi=new
    phi[2]+=sum(comb(len(p),2) for p in starts)
    assert all(bysize[i]==phi[i] for i in range(N+1))
    dim,states=rank(cs,N)
    assert dim==len(parts)+1,(parts,dim)
    assert max(i for i,c in bysize.items() if c)==len(parts)
    print('PASS',parts,'N',N,'concepts',len(cs),'VC',len(parts),'Ldim',dim,'shattered',sum(bysize.values()),'rank_states',states,'polynomial',[(i,phi[i]) for i in range(N+1) if phi[i]])

for p in [(2,2),(2,3),(3,3),(2,2,2),(3,2,2),(2,2,2,2),(2,2,2,2,2)]:
    verify(p)
print('ALL_GEODESIC_CONVEXITY_CENSUS_CHECKS_PASS')
