"""Finite checks for automorphisms of ordered-block partial-bijection monoids."""
from itertools import permutations, combinations, product
from math import factorial


def compose(p, q):
    """p after q, written as tuples of images."""
    return tuple(p[x] for x in q)


def inv(p):
    q = [0] * len(p)
    for i, v in enumerate(p):
        q[v] = i
    return tuple(q)


def all_monoid(k, m):
    sym = list(permutations(range(m)))
    elems = []
    for r in range(k+1):
        for ins in combinations(range(k),r):
            for outs in combinations(range(k),r):
                for perms in product(sym, repeat=r):
                    elems.append(tuple(zip(ins,outs,perms)))
    return elems


def mult(x,y):
    # x followed by y, so label of resulting block is y_label after x_label.
    yd = {src:(tgt,p) for src,tgt,p in y}
    out=[]
    for src,j,p in x:
        if j in yd:
            tgt,q = yd[j]
            out.append((src,tgt,compose(q,p)))
    return tuple(out)


def relabel(x,k,m,reversed_blocks,phi,a):
    t=lambda i: k-1-i if reversed_blocks else i
    z=[]
    for i,j,p in x:
        ip,jp=t(i),t(j)
        label = compose(compose(a[jp],phi[p]),inv(a[ip]))
        z.append((ip,jp,label))
    return tuple(sorted(z,key=lambda u:u[0]))


def checks(k,m,expected):
    syms=list(permutations(range(m)))
    ident=tuple(range(m))
    elems=all_monoid(k,m)
    lookup={e:i for i,e in enumerate(elems)}
    assert len(lookup)==len(elems)
    assert len(elems)==sum(__import__('math').comb(k,r)**2*factorial(m)**r for r in range(k+1))
    # For m=2, automorphism group of S2 is trivial. For m=3, all Aut(S3) are inner.
    inner=[]
    seen=set()
    for h in syms:
        ph={p:compose(compose(h,p),inv(h)) for p in syms}
        s=tuple(ph[p] for p in syms)
        if s not in seen:
            seen.add(s);inner.append(ph)
    assert len(inner)==(1 if m==2 else factorial(m))
    prod=[[lookup[mult(x,y)] for y in elems] for x in elems]
    seen_maps=set()
    for rev,phi,rest in product((False,True),inner, product(syms,repeat=k-1)):
        gauges=(ident,)+rest
        im=tuple(lookup[relabel(x,k,m,rev,phi,gauges)] for x in elems)
        assert sorted(im)==list(range(len(elems)))
        assert im not in seen_maps
        seen_maps.add(im)
        for i in range(len(elems)):
            for j in range(len(elems)):
                assert im[prod[i][j]]==prod[im[i]][im[j]]
    assert len(seen_maps)==expected
    print(f'VERIFY_OK k={k} m={m} elements={len(elems)} explicit_automorphisms={len(seen_maps)} all_pairs_checked={len(seen_maps)*len(elems)**2}')

if __name__=='__main__':
    checks(2,2,4)
    checks(3,2,8)
    checks(2,3,72)
