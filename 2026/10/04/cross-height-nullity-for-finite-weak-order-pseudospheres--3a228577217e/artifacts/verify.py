from itertools import product

CASES=[
 ((2,2),(2,2,2)),
 ((3,2),(2,3,2)),
 ((2,3,2),(3,2)),
 ((3,2),(2,2,2,2)),
 ((2,2,2,2),(2,2)),
 ((3,3),(2,2,3)),
 ((4,2),(2,2,2)),
]

def levels(sizes):
    lev=[]
    for i,n in enumerate(sizes): lev += [i]*n
    return lev

def qle(a,b,ql): return a==b or ql[a] < ql[b]

def is_monotone(f,pl,ql):
    n=len(f)
    for x in range(n):
        for y in range(n):
            if pl[x] < pl[y] and not qle(f[x],f[y],ql):
                return False
    return True

def pointwise_le(f,g,ql):
    return all(qle(a,b,ql) for a,b in zip(f,g))

def blocks(sizes):
    out=[]; a=0
    for n in sizes:
        out.append(list(range(a,a+n))); a+=n
    return out

def singleton_fence(f, ps, qs, z):
    ql=levels(qs); t=ql[z]
    g=tuple(z if ql[v] <= t else v for v in f)
    c=tuple(z for _ in f)
    assert is_monotone(g,levels(ps),ql)
    assert pointwise_le(f,g,ql)
    assert pointwise_le(c,g,ql)
    return [f,g,c]

def null_witness(f, ps, qs):
    pl=levels(ps); ql=levels(qs); pb=blocks(ps); qb=blocks(qs)
    # occupied target-level distinct-point sets
    occ=[set() for _ in qs]
    for v in f: occ[ql[v]].add(v)
    # Case 1: singleton occupied target level.
    for S in occ:
        if len(S)==1:
            z=next(iter(S))
            return singleton_fence(f,ps,qs,z), 'singleton'
    # Case 2: a source level spans >1 target levels. Push all but one
    # point out of its lowest occupied target level to an already used higher point.
    for inds in pb:
        levset={ql[f[x]] for x in inds}
        if len(levset)>1:
            j=min(levset)
            low=[x for x in inds if ql[f[x]]==j]
            assert len({f[x] for x in low})>=2
            u=next(f[x] for x in inds if ql[f[x]]>j)
            keep=low[0]
            g=list(f)
            for x in low:
                if x!=keep: g[x]=u
            g=tuple(g)
            assert is_monotone(g,pl,ql)
            assert pointwise_le(f,g,ql)
            occj={g[x] for x in range(len(g)) if ql[g[x]]==j}
            assert len(occj)==1
            tail=singleton_fence(g,ps,qs,next(iter(occj)))
            return [f]+tail, 'spanning'
    # Case 3: each source level lies in one target level. No singleton means
    # the target levels are strictly increasing and each image is nonconstant.
    t=[]
    for inds in pb:
        tt={ql[f[x]] for x in inds}
        assert len(tt)==1
        t.append(next(iter(tt)))
    assert all(t[i] < t[i+1] for i in range(len(t)-1))
    assert len(ps) < len(qs), 'strict injection impossible when source has more levels'
    omitted=next(j for j in range(len(qs)) if j not in t)
    z=qb[omitted][0]
    g=list(f)
    if omitted < t[0]:
        for x in pb[0]: g[x]=z
        direction='down'
    elif omitted > t[-1]:
        for x in pb[-1]: g[x]=z
        direction='up'
    else:
        i=max(i for i,v in enumerate(t) if v<omitted)
        for x in pb[i]: g[x]=z
        direction='up'
    g=tuple(g)
    assert is_monotone(g,pl,ql)
    if direction=='up': assert pointwise_le(f,g,ql)
    else: assert pointwise_le(g,f,ql)
    occj={g[x] for x in range(len(g)) if ql[g[x]]==omitted}
    assert occj=={z}
    tail=singleton_fence(g,ps,qs,z)
    return [f]+tail, 'gap'

def verify_case(ps,qs):
    pl=levels(ps); ql=levels(qs)
    count=0; modes={}
    for f in product(range(len(ql)), repeat=len(pl)):
        if not is_monotone(f,pl,ql): continue
        count += 1
        path,mode = null_witness(f,ps,qs)
        modes[mode]=modes.get(mode,0)+1
        assert path[0]==f
        # Every consecutive pair is pointwise comparable.
        for a,b in zip(path,path[1:]):
            assert pointwise_le(a,b,ql) or pointwise_le(b,a,ql)
        assert len(set(path[-1]))==1
    return count,modes

if __name__=='__main__':
    total=0
    for ps,qs in CASES:
        n,m=verify_case(ps,qs); total+=n
        print(f'{ps}->{qs}: maps={n} modes={m}')
    print('TOTAL_MAPS',total)
    print('VERIFY_OK')
