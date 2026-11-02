"""Exact finite tests for Chermak--Delgado/centralizer lattices of chain-ring Heisenberg groups."""
from itertools import combinations, product


def ring_mul(a,b,ell):
    out=0
    for i in range(ell):
        if a>>i&1:
            for j in range(ell-i):
                if b>>j&1: out^=1<<(i+j)
    return out


def ring_add(a,b): return a^b


def span_binary(vectors):
    s={0}
    for x in vectors: s|={v^x for v in tuple(s)}
    return frozenset(s)


def subspaces_binary(width):
    # Generate each F2-linear subspace once, via adding all possible new generators.
    todo=[frozenset({0})]; seen={todo[0]};
    for w in todo:
        for v in range(1,1<<width):
            if v not in w:
                n=frozenset(w|{u^v for u in w})
                if n not in seen:
                    seen.add(n);todo.append(n)
    return todo


def pair(a,b,ell,d):
    m=(1<<ell)-1
    x1=[(a>>(ell*j))&m for j in range(d)]
    x2=[(b>>(ell*j))&m for j in range(d)]
    acc=0
    for i in range(d//2):
        acc^=ring_mul(x1[i],x2[d//2+i],ell)
        acc^=ring_mul(x2[i],x1[d//2+i],ell)
    return acc


def ring_scale(r,a,ell,d):
    mask=(1<<ell)-1
    return sum(ring_mul(r,(a>>(ell*j))&mask,ell)<<(ell*j) for j in range(d))


def test_submodules(ell,n):
    size=1<<ell; d=2*n; dim=ell*d
    subs=subspaces_binary(dim)
    mods=[u for u in subs if all(ring_scale(r,a,ell,d) in u for r in range(size) for a in u)]
    modset=set(mods)
    vspace=range(1<<dim)
    orth={u:frozenset(y for y in vspace if all(pair(x,y,ell,d)==0 for x in u)) for u in mods}
    assert all(o in modset and len(o)*len(u)==(size**d) and orth[o]==u for u,o in orth.items())
    # For every additive subgroup W (not necessarily an R-submodule), compute its R-span,
    # verify the Chermak--Delgado measure bound and the exact equality criterion.
    for W in subs:
        rw=span_binary(ring_scale(r,x,ell,d) for r in range(size) for x in W)
        wo=frozenset(y for y in vspace if all(pair(x,y,ell,d)==0 for x in W))
        assert wo==orth[rw]
        norm=len(W)*len(wo)
        assert norm<=size**d
        assert (norm==size**d)==(W in modset)
    # Number of distinct centralizers in the finite Heisenberg group equals #submodules.
    assert len({orth[span_binary(ring_scale(r,x,ell,d) for r in range(size) for x in w)] for w in subs})==len(mods)
    return len(subs),len(mods)


def group_check_64():
    # Directly enumerate the 64-element group and all 67 additive quotient subgroups.
    ell=2; size=4
    elts=range(size**3)
    def tup(g):return(g%size,(g//size)%size,g//(size*size))
    def prod(g,h):
        a,b,c=tup(g);u,v,w=tup(h)
        return (a^u)+size*(b^v)+size*size*(c^w^ring_mul(a,v,ell))
    def cen(H):return frozenset(g for g in elts if all(prod(g,h)==prod(h,g) for h in H))
    z=frozenset(range(0,64,16))
    assert len(z)==4
    max_measure=size**4
    wlist=subspaces_binary(4)
    cset=set(); winners=0
    for W in wlist:
        H=frozenset(w0%size + size*(w0//size)+size*size*c for w0 in W for c in range(size))
        C=cen(H);cset.add(C)
        m=len(H)*len(C)
        ismod=all(ring_scale(r,w,ell,2) in W for r in range(size) for w in W)
        assert (m==max_measure)==ismod
        winners+=m==max_measure
    for g in elts:
        H={0};f=0
        while True:
            f=prod(f,g)
            if f in H:break
            H.add(f)
        H=frozenset(H);C=cen(H)
        assert len(H)*len(C)<=max_measure
        # A proper central intersection cannot achieve the top measure.
        if not z.issubset(H):assert len(H)*len(C)<max_measure
    assert len(cset)==winners
    return len(wlist),winners,len(cset)


def sampled_n2():
    # Check selected additive subgroups of an 8-dimensional binary quotient.
    import random
    rr=random.Random(20261028);ell=2;d=4;size=4;total=256
    samples=set([frozenset({0}),frozenset(range(256))])
    for j in range(400):
        gens=[rr.randrange(total) for _ in range(rr.randrange(1,8))]
        samples.add(span_binary(gens))
    for W in samples:
        rw=span_binary(ring_scale(r,x,ell,d) for r in range(size) for x in W)
        orth=frozenset(y for y in range(total) if all(pair(x,y,ell,d)==0 for x in W))
        assert len(rw)*len(orth)==total
        ismod=all(ring_scale(r,x,ell,d) in W for r in range(size) for x in W)
        assert (len(W)*len(orth)==total)==ismod
    return len(samples)


def test_odd_field_q3():
    # Full additive-subgroup census for R=F3[t]/(t^2), n=1.
    q=3; mod=3**4
    def decomp(v): return tuple((v//(3**i))%3 for i in range(4))
    vlist=list(map(decomp,range(mod)))
    idx={v:i for i,v in enumerate(vlist)}
    def plus(a,b):return idx[tuple((x+y)%3 for x,y in zip(vlist[a],vlist[b]))]
    def scalar(a,t):return idx[tuple((t*x)%3 for x in vlist[a])]
    def span(vectors):
        s={0}
        for v in vectors:
            s={plus(u,scalar(v,r)) for u in s for r in range(3)}
        return frozenset(s)
    sub=[frozenset({0})];seen=set(sub)
    for U in sub:
        for v in range(1,mod):
            if v not in U:
                w=span((*U,v))
                if w not in seen:seen.add(w);sub.append(w)
    def tscale(v):
        a0,a1,b0,b1=vlist[v]
        return idx[(0,a0,0,b0)]
    def symplectic(a,b):
        a0,a1,b0,b1=vlist[a];c0,c1,d0,d1=vlist[b]
        return ((a0*d0-c0*b0)%3,(a0*d1+a1*d0-c0*b1-c1*b0)%3)
    mods=0
    for U in sub:
        per=frozenset(y for y in range(mod) if all(symplectic(x,y)==(0,0) for x in U))
        ismod=all(tscale(x) in U for x in U)
        assert len(per)*len(U)<=mod
        assert (len(per)*len(U)==mod)==ismod
        if ismod:
            mods+=1
            assert all(tscale(x) in per for x in per)
    return len(sub),mods


if __name__=='__main__':
    a=test_submodules(1,1)
    b=test_submodules(2,1)
    c=sampled_n2()
    e=test_odd_field_q3()
    d=group_check_64()
    print('VERIFY_OK', 'field q2:',a,'dual q4 n1:',b,'sampled n2:',c,'group64:',d,'odd q3:',e)
