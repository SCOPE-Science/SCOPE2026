from itertools import product, combinations


def leq_capped(a,b,p,m):
    # points ('p',i) in base antichain and ('t',j) in maximal cap
    if a==b: return True
    if a[0]=='p' and b[0]=='t': return True
    return False

def capped_points(p,m):
    return [('p',i) for i in range(p)] + [('t',j) for j in range(m)]

def prod_leq(x,y, specs):
    return all(leq_capped(xi, yi, p, m) for xi, yi, (p,m) in zip(x,y,specs))

def maxima(points, leq):
    return [x for x in points if not any(x!=y and leq(x,y) for y in points)]

def has_maximum(points, leq):
    return any(all(leq(y,x) for y in points) for x in points)

def beat_points(points, leq):
    out=[]
    for x in points:
        lower=[y for y in points if y!=x and leq(y,x)]
        upper=[y for y in points if y!=x and leq(x,y)]
        down=any(all(leq(y,z) for y in lower) for z in lower) if lower else False
        up=any(all(leq(z,y) for y in upper) for z in upper) if upper else False
        if down or up: out.append(x)
    return out

def check_case(specs):
    factors=[capped_points(p,m) for p,m in specs]
    pts=list(product(*factors))
    leq=lambda x,y: prod_leq(x,y,specs)
    maxs=maxima(pts, leq)
    expected=1
    for _,m in specs: expected*=m
    assert len(maxs)==expected
    # principal opens at global maxima cover and each has a maximum
    union=set()
    for a in maxs:
        Ua=[x for x in pts if leq(x,a)]
        assert has_maximum(Ua,leq)
        union.update(Ua)
    assert union==set(pts)
    pair_checks=0
    for a,b in combinations(maxs,2):
        j=next(i for i,(u,v) in enumerate(zip(a,b)) if u!=v)
        assert a[j][0]=='t' and b[j][0]=='t'
        fixed=[('p',0) if i!=j else None for i in range(len(specs))]
        p_j,m_j=specs[j]
        def embed(y):
            z=[]
            for i in range(len(specs)):
                z.append(y if i==j else fixed[i])
            return tuple(z)
        Y=[('p',i) for i in range(p_j)] + [a[j],b[j]]
        # the slice lies in any lower set containing a and b
        for y in Y:
            z=embed(y)
            assert leq(z,a) or leq(z,b)
        # Y itself is a noncontractible core for the tested antichain bases
        leqY=lambda x,y: leq_capped(x,y,p_j,2)
        # relabel its two top points for the local test
        Ystd=[('p',i) for i in range(p_j)]+[('t',0),('t',1)]
        assert not beat_points(Ystd,leqY)
        assert len(Ystd)>1
        # explicit retraction of the factor onto the selected two-top subspace
        for x in factors[j]:
            rx=x if (x[0]=='p' or x in {a[j],b[j]}) else a[j]
            assert rx in Y
        for x in factors[j]:
            for y in factors[j]:
                if leq_capped(x,y,*specs[j]):
                    rx=x if (x[0]=='p' or x in {a[j],b[j]}) else a[j]
                    ry=y if (y[0]=='p' or y in {a[j],b[j]}) else a[j]
                    assert (rx==ry) or (rx[0]=='p' and ry[0]=='t')
        pair_checks+=1
    return len(pts), len(maxs), pair_checks

cases=[[(2,2),(2,2)],[(2,2),(2,3)],[(3,3),(2,2)],[(2,2),(2,2),(2,2)]]
tot_pairs=0
for specs in cases:
    npts,nmax,npairs=check_case(specs)
    tot_pairs+=npairs
    print('CASE',specs,'points',npts,'maxima',nmax,'maximal_pairs',npairs)
print('VERIFY_OK cases=%d maximal_pairs=%d' % (len(cases),tot_pairs))
