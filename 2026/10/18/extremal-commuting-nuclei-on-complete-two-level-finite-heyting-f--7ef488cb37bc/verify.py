"""Alternate finite checks for commuting nuclei on complete two-level frames."""
from itertools import combinations
from math import comb


def frames(r,s):
    masks=[]
    top=((1<<s)-1)<<r
    for u in range(1<<(r+s)):
        if (u&((1<<r)-1)) and (u&top)!=top:continue
        masks.append(u)
    return masks


def nu(support,u,r,s):
    out=0
    top=((1<<s)-1)<<r
    for x in range(r+s):
        cone=(1<<x)|(top if x<r else 0)
        if not ((support&cone)&~u):out|=1<<x
    return out


def commute_direct(a,b,r,s,ups):
    return all(nu(a,nu(b,u,r,s),r,s)==nu(b,nu(a,u,r,s),r,s) for u in ups)


def commute_claim(a,b,r,s):
    low=(1<<r)-1
    x=a&low; y=b&low
    c=a>>r;d=b>>r
    return not (((x&~y)!=0 and (d&~c)!=0) or ((y&~x)!=0 and (c&~d)!=0))


def clique_max(G):
    N=len(G)
    maxc=0; max_sets=[]; maximal=0
    def bk(R,P,X):
        nonlocal maxc,maximal,max_sets
        if not P and not X:
            maximal+=1
            sz=len(R)
            if sz>maxc: maxc=sz;max_sets=[]
            if sz==maxc:max_sets.append(frozenset(R))
            return
        # Pivot maximizing the number of current candidates adjacent to it.
        p=max(P|X,key=lambda x:len(P&G[x]),default=None)
        candidates=sorted(P-(G[p] if p is not None else set()))
        for v in candidates:
            bk(R+[v],P&G[v],X&G[v])
            P.remove(v);X.add(v)
    bk([],set(range(N)),set())
    return maxc,max_sets,maximal


def fixed_family_exhaustive(r,s):
    UP=frames(r,s)
    top=(1<<(r+s))-1
    unionsets={tuple(nu(S,u,r,s) for u in UP) for S in range(1<<(r+s))}
    assert len(unionsets)==(1<<(r+s))
    m=len(UP)
    found=set()
    for bits in range(1<<m):
        fixed=[u for i,u in enumerate(UP) if bits>>i&1]
        if top not in fixed:continue
        if any((a&b) not in fixed for a in fixed for b in fixed):continue
        im=[]
        for u in UP:
            im.append(next((t for t in fixed if (t&u)==u and
                    all((t&v)==t for v in fixed if (v&u)==u)),None))
        assert all(x is not None for x in im)
        j=dict(zip(UP,im))
        if all(j[a&b]==(j[a]&j[b]) for a in UP for b in UP):found.add(tuple(im))
    assert found==unionsets,(len(found),len(unionsets))
    return len(found)


def run():
    assert fixed_family_exhaustive(2,2)==16
    for r,s in [(2,2),(2,3),(3,2),(3,3)]:
        up=frames(r,s);n=1<<(r+s)
        for a in range(n):
            f=[nu(a,u,r,s) for u in up]
            assert len(set(f))>0
            assert all((u&v)==u and nu(a,nu(a,u,r,s),r,s)==nu(a,u,r,s) for u,v in zip(up,f))
            assert all(nu(a,u&v,r,s)==(nu(a,u,r,s)&nu(a,v,r,s)) for u in up for v in up)
        graph=[set() for _ in range(n)];paired=0
        for a in range(n):
            for b in range(n):
                c=commute_direct(a,b,r,s,up)
                assert c==commute_claim(a,b,r,s)
                paired+=c
                if a!=b and c:graph[a].add(b)
        predicted=(2**r)*(4**s)+2*(3**r-2**r)*(3**s)+(4**r-2*3**r+2**r)*(2**s)
        assert paired==predicted,(r,s,paired,predicted)
        size,best,total=clique_max(graph)
        assert size==2**r+2**s-1,(r,s,size)
        assert len(best)==2,(r,s,len(best))
        lo=(1<<r)-1;upmask=(1<<s)-1
        expected=[]
        # Two extremizers: full bottom index carries every top subset, other bottom indices carry fixed top extreme.
        for b0,t0 in [(0,upmask),(lo,0)]:
            e={b+(a<<r) for a in range(1<<s) for b in [b0]}
            e.update(b+(t0<<r) for b in range(1<<r))
            expected.append(frozenset(e))
        assert set(best)==set(expected),(r,s,best,expected)
        print(f'r={r},s={s}: nuclei={n}, commuting_pairs={paired}, max_family={size}, maximizers=2, maximal_cliques={total}')
    print('VERIFY_OK')

if __name__=='__main__':run()
