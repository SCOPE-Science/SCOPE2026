"""Exact four-round first-order types and local extension profiles of Moore graphs."""
from itertools import product,combinations
from collections import defaultdict


def moore_known(degree):
    if degree==2:
        return [{(i-1)%5,(i+1)%5} for i in range(5)]
    if degree==3:
        pairs=list(combinations(range(5),2))
        return [{j for j,t in enumerate(pairs) if i!=j and set(s).isdisjoint(t)} for i,s in enumerate(pairs)]
    if degree==7:
        vertices=list(product(range(2),range(5),range(5)))
        ix={v:i for i,v in enumerate(vertices)}
        g=[set() for _ in vertices]
        def edge(a,b):
            ai=ix[a];bi=ix[b];g[ai].add(bi);g[bi].add(ai)
        for t in range(5):
            for x in range(5):
                edge((0,t,x),(0,t,(x+1)%5))
                edge((1,t,x),(1,t,(x+2)%5))
        for j in range(5):
            for i in range(5):
                for k in range(5):
                    edge((0,j,i),(1,k,(i+j*k)%5))
        return g
    raise ValueError(degree)


def parameters(g):
    n=len(g);k={len(a) for a in g};assert len(k)==1;k=k.pop()
    for a in range(n):
        assert a not in g[a]
        for b in range(a+1,n):
            assert (b in g[a])==(a in g[b])
            assert len(g[a]&g[b])==(0 if b in g[a] else 1)
    assert n==k*k+1
    return n,k


def triple_kind(g,vs):
    x,y,z=vs
    e=sum(b in g[a] for a,b in ((x,y),(x,z),(y,z)))
    if e==0:
        c=any((v in g[x] and v in g[y] and v in g[z]) for v in range(len(g)) if v not in vs)
        return 'independent_concurrent' if c else 'independent_separate'
    if e==1:return 'one_edge'
    if e==2:return 'path'
    raise AssertionError('girth-5 graph has no triangle')


def profile(g,vs):
    ans=set()
    for w in range(len(g)):
        if w in vs:continue
        mask=sum((1<<i) for i,v in enumerate(vs) if w in g[v])
        ans.add(mask)
    return frozenset(ans)

# Bit masks: independent order for three selected vertices: 0=no neighbors, 7=all three.
EXPECTED={
    'independent_concurrent': frozenset((0,1,2,4,7)),
    'independent_separate': frozenset((0,1,2,4,3,5,6)),
    'one_edge': None,
    'path': frozenset((0,1,2,4)),
}

def check_patterns(g,d):
    tally=defaultdict(set)
    seen=defaultdict(int)
    for vs in combinations(range(len(g)),3):
        typ=triple_kind(g,vs)
        signs=profile(g,vs)
        seen[typ]+=1;tally[typ].add(signs)
        if d>=4:
            if typ=='one_edge':
                # Unique edge can be in any of the three positions: one pair mask is forbidden.
                edge=next((1<<i)|(1<<j) for i in range(3) for j in range(i+1,3) if vs[j] in g[vs[i]])
                expect=frozenset(set(range(8))-{edge,7})
            else: expect=EXPECTED[typ]
            assert signs==expect,(typ,vs,signs,expect)
    if d>=4:
        assert set(seen)==set(EXPECTED)
    print('TRIPLE_EXTENSIONS',d, 'classes',dict(seen),'profile_variants',{x:len(v) for x,v in tally.items()})
    if d==3:
        assert frozenset((1,2,4,7)) in tally['independent_concurrent']
        assert 0 not in next(iter(tally['independent_concurrent']))


def qf(g,vs):
    # 2 means identical, 1 adjacent, 0 distinct nonadjacent.
    return tuple(2 if vs[i]==vs[j] else int(vs[j] in g[vs[i]]) for i in range(len(vs)) for j in range(i+1,len(vs)))


def root_types(gs):
    # Exact full first-order types: a stage with r remaining rounds stores
    # the complete set of possible types obtained by one additional vertex.
    intern={}
    def identifier(key):
        if key not in intern:intern[key]=len(intern)
        return intern[key]
    out=[]
    for name,g in gs:
        n=len(g)
        tri={}
        for x in range(n):
            for y in range(n):
                for z in range(n):
                    vs=(x,y,z)
                    opts=frozenset(qf(g,vs+(w,)) for w in range(n))
                    tri[vs]=identifier((1,qf(g,vs),opts))
        pair={}
        for x in range(n):
            for y in range(n):
                pair[x,y]=identifier((2,qf(g,(x,y)),frozenset(tri[x,y,z] for z in range(n))))
        single={x:identifier((3,(),frozenset(pair[x,y] for y in range(n)))) for x in range(n)}
        root=identifier((4,(),frozenset(single.values())))
        out.append((name,root))
        print('RANK4_TYPE',name,root,'INTERNED_SO_FAR',len(intern))
    assert len(set(x for _,x in out))==3
    return out

if __name__=='__main__':
    gs=[]
    for d,name in [(2,'Five-cycle'),(3,'Petersen'),(7,'Hoffman-Singleton')]:
        g=moore_known(d);n,k=parameters(g);assert k==d
        print('PARAMETERS_OK',name,n,k,0,1)
        check_patterns(g,d)
        gs.append((name,g))
    assert len({p for name,p in root_types(gs)})==3
    # The rank-three and rank-four separating sentences are evaluated directly.
    def indep3(g):
        return any(not (y in g[x] or z in g[x] or z in g[y])
                   for x,y,z in combinations(range(len(g)),3))
    def dominating_concurrent_triple(g):
        for vs in combinations(range(len(g)),3):
            if triple_kind(g,vs)!='independent_concurrent':continue
            if all(w in vs or any(w in g[x] for x in vs) for w in range(len(g))):
                return True
        return False
    assert [indep3(g) for _,g in gs]==[False,True,True]
    assert [dominating_concurrent_triple(g) for _,g in gs]==[False,True,False]
    print('RANK3_AND_RANK4_SEPARATORS_OK')
    print('FINITE_EXACT_TYPES_AND_TRIPLE_SUPPORTS_OK')
