"""Independent finite checks for perfect-matching incidence closure (complete graphs)."""
from itertools import combinations
from math import comb, factorial
from random import Random

def edges(n):
    return list(combinations(range(2*n),2))

def perfect_matchings(vertices):
    if not vertices:
        yield ()
    else:
        v=vertices[0]
        for i in range(1,len(vertices)):
            w=vertices[i]
            for rest in perfect_matchings(vertices[1:i]+vertices[i+1:]):
                yield ((v,w),)+rest

def data(n):
    ed=edges(n); idx={e:i for i,e in enumerate(ed)}
    pms=[]
    for pm in perfect_matchings(tuple(range(2*n))):
        pms.append(sum(1<<idx[e] for e in pm))
    E=(1<<len(ed))-1
    return ed,pms,E

def from_models(S, models, E):
    hits=[p for p in models if (S&p)==S]
    x=E
    for p in hits: x&=p
    return x

def structural(S, ed, E, n):
    seen=0; size=0
    for i,(u,v) in enumerate(ed):
        if S>>i&1:
            if seen & ((1<<u)|(1<<v)): return E
            seen|=1<<u|1<<v
            size+=1
    if size<=n-2 or size==n:return S
    missing=((1<<(2*n))-1)^seen
    uv=tuple(i for i in range(2*n) if (missing>>i)&1)
    j=ed.index(uv)
    return S|(1<<j)

def rule_masks(n,ed,E):
    incident=[]
    for i,e in enumerate(ed):
        for j in range(i):
            if set(e)&set(ed[j]): incident.append((1<<i)|(1<<j))
    near=set()
    for pm in perfect_matchings(tuple(range(2*n))):
        idx=[ed.index(e) for e in pm]
        for i in idx:
            near.add(sum(1<<j for j in idx if j!=i))
    assert len(incident)==2*n*comb(2*n-1,2)
    P=factorial(2*n)//(2**n*factorial(n))
    assert len(near)==n*P
    return incident,list(near)

def one_round(S, incident,near,ed,n,E):
    res=S
    for A in incident:
        if S&A==A:
            return E
    for A in near:
        if S&A==A:
            used=0
            for i,(u,v) in enumerate(ed):
                if A>>i&1:used|=1<<u|1<<v
            remaining=[u for u in range(2*n) if not(used>>u&1)]
            res|=1<<ed.index(tuple(remaining))
    return res

def matchings_list(n,ed):
    out=[]
    for k in range(n+1):
        cur=[]
        for inds in combinations(range(len(ed)),k):
            used=0
            for i in inds:
                uv=(1<<ed[i][0])|(1<<ed[i][1])
                if used&uv:break
                used|=uv
            else: cur.append(sum(1<<i for i in inds))
        out.append(cur)
    return out

def hermite_at_one(order):
    return sum((-1)**k*factorial(order)//(factorial(order-2*k)*2**k*factorial(k)) for k in range(order//2+1))

def mobius_in_lattice(closed):
    closed=sorted(set(closed),key=lambda x:(x.bit_count(),x))
    # enumerate all intervals; degree at most 105+others here
    by_top={}; vals={}
    for top in closed:
        below=[x for x in closed if x&top==x]
        z={}
        for x in reversed(below):
            if x==top:z[x]=1
            else:z[x]=-sum(z[y] for y in below if x!=y and x&y==x)
        by_top[top]=z
    return by_top

def check(n, exhaustive):
    ed,pms,E=data(n)
    incident,near=rule_masks(n,ed,E)
    matching_by_size=matchings_list(n,ed)
    closed=set([E])|set(pms)
    for k in range(n-1):closed.update(matching_by_size[k])
    predicted=1+len(pms)+sum(len(matching_by_size[k]) for k in range(n-1))
    assert len(closed)==predicted
    for k in range(n+1):
        assert len(matching_by_size[k])==factorial(2*n)//(factorial(2*n-2*k)*2**k*factorial(k))
    cases=range(1<<len(ed)) if exhaustive else (list(closed)+[Random(20261018+n).getrandbits(len(ed)) for _ in range(15000)])
    count=0
    for S in cases:
        direct=from_models(S,pms,E)
        assert direct==structural(S,ed,E,n),(n,S,'structure')
        assert direct==one_round(S,incident,near,ed,n,E),(n,S,'one_round')
        assert (direct==S)==(S in closed),(n,S,'closed')
        count+=1
    if n in (3,4):
        mus=mobius_in_lattice(closed)
        for top, bot_values in mus.items():
            for A, mu in bot_values.items():
                if top==A: expected=1
                elif top==E:
                    if A in pms:expected=-1
                    else:expected=-hermite_at_one(2*(n-A.bit_count()))
                elif top in pms:
                    r=n-A.bit_count()
                    expected=(-1)**(r-1)*(r-1)
                else:
                    expected=(-1)**(top.bit_count()-A.bit_count())
                assert mu==expected,(A,top,mu,expected)
        print('ALL_INTERVAL_MOBIUS',n,'intervals',sum(map(len,mus.values())),'PASS')
    print('CHECK',n,'models',len(pms),'closed',predicted,'rules',len(incident)+len(near),'inputs',count,'PASS')
    print('RANKS',n,[len(matching_by_size[k]) for k in range(n-1)]+[len(pms),1])

if __name__=='__main__':
    check(3, True)
    check(4, False)
    print('VERIFY_OK complete_graph_matching_closure=PASS minimal_premises=PASS one_round_basis=PASS interval_mobius=PASS')
