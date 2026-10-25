#!/usr/bin/env python3
"""Finite checks for Rota--Baxter operators on odd-prime finite Heisenberg groups."""
from itertools import product
from math import prod
import random


def dot(x,y,p): return sum(a*b for a,b in zip(x,y))%p

def omega(v,w,p):
    n=len(v)//2
    return (dot(v[:n],w[n:],p)-dot(v[n:],w[:n],p))%p

def apply(T,v,p):
    return tuple(dot(row,v,p) for row in T)

def rb_matrix(T,c,p):
    d=len(T)
    basis=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    def sub(Tv,v): return tuple((x-c*y)%p for x,y in zip(Tv,v))
    sb=[sub(apply(T,v,p),v) for v in basis]
    m=c*(c+1)%p
    return all((omega(sb[i],sb[j],p)-m*omega(basis[i],basis[j],p))%p==0 for i in range(d) for j in range(d))

def make_rb(T,c,ell,p):
    inv2=pow(2,-1,p)
    def B(g):
        d=len(T);v=g[:d];z=g[d]; tv=apply(T,v,p)
        return tv+((c*z-c*inv2*omega(tv,v,p)+dot(ell,v,p))%p,)
    return B

def multiply(g,h,p):
    d=len(g)-1; a,b=g[:d],h[:d]
    return tuple((u+v)%p for u,v in zip(a,b))+((g[d]+h[d]+pow(2,-1,p)*omega(a,b,p))%p,)

def inverse(g,p): return tuple((-t)%p for t in g)

def rb_direct(T,c,ell,p,exhaustive=True,seed=32):
    d=len(T); B=make_rb(T,c,ell,p)
    rng=random.Random(seed)
    if exhaustive:
        gs=list(product(range(p),repeat=d+1))
        pairs=product(gs,gs)
    else:
        gs=list(product(range(p),repeat=d+1))
        pairs=((rng.choice(gs),rng.choice(gs)) for _ in range(1000))
    for g,h in pairs:
        bg=B(g); bh=B(h)
        lhs=multiply(bg,bh,p)
        gh=multiply(g,multiply(bg,multiply(h,inverse(bg,p),p),p),p)
        if lhs != B(gh): return False
    return True

def enumerate_n1(p):
    d=2; matrices=(tuple(tuple(vals[i*d:(i+1)*d]) for i in range(d)) for vals in product(range(p),repeat=d*d))
    by_c={c:0 for c in range(p)}
    for T in matrices:
        for c in range(p):
            truth=rb_matrix(T,c,p)
            if p==3:
                assert truth==rb_direct(T,c,(0,0),p), (T,c)
            if truth: by_c[c]+=1
    iso=1+((p*p-1)**2)//(p-1)
    sp=p*(p*p-1)
    expected={c:(iso if c in (0,p-1) else sp) for c in range(p)}
    assert by_c==expected,(by_c,expected)
    if p==3:
        rng=random.Random(97)
        for _ in range(40):
            T=tuple(tuple(rng.randrange(p) for j in range(d)) for i in range(d))
            c=rng.randrange(p)
            ell=tuple(rng.randrange(p) for _ in range(d))
            assert rb_matrix(T,c,p)==rb_direct(T,c,ell,p)
    return {"p":p,"by_scalar":by_c,"all_operator_count":p**d*sum(by_c.values())}

def number_isotropic_maps(n,p):
    d=2*n; count=0
    for r in range(n+1):
        # # symplectic totally isotropic r-subspaces times # surjections V -> a fixed r-space
        num=prod(p**(d-i)-p**i for i in range(r))
        den=prod(p**r-p**i for i in range(r))
        assert num%den==0
        iso_planes=num//den
        surj=prod(p**d-p**i for i in range(r))
        count+=iso_planes*surj
    return count

def symplectic_order(n,p): return p**(n*n)*prod(p**(2*i)-1 for i in range(1,n+1))

def random_n2():
    p=3; n=2;d=4
    rng=random.Random(871)
    for k in range(55):
        T=tuple(tuple(rng.randrange(p) for j in range(d)) for i in range(d))
        c=rng.randrange(p)
        ell=tuple(rng.randrange(p) for _ in range(d))
        assert rb_matrix(T,c,p)==rb_direct(T,c,ell,p,exhaustive=False,seed=100+k),(k,T,c)
    # Construct valid examples in all scalar regimes and check 1000 sampled pairs.
    for c in range(p):
        T=tuple(tuple((c*int(i==j))%p for j in range(d)) for i in range(d))
        ell=tuple(rng.randrange(p) for _ in range(d))
        if c in (0,p-1):
            assert rb_matrix(T,c,p)
            assert rb_direct(T,c,ell,p,False)
        else:
            # pick a fixed similitude with multiplier c(c+1), shift by cI.
            m=c*(c+1)%p
            S=tuple(m if i==j and i<n else int(i==j) for i in range(d) for j in range(d))
            S=tuple(S[i*d:(i+1)*d] for i in range(d))
            T=tuple(tuple((S[i][j]+c*int(i==j))%p for j in range(d)) for i in range(d))
            assert rb_matrix(T,c,p)
            assert rb_direct(T,c,ell,p,False)
    return "n=2 p=3, random crosschecks=55, constructed valid scalars=3"

if __name__ == '__main__':
    for p in [3,5,7]: print('small exact:', enumerate_n1(p))
    print(random_n2())
    for n,p in [(1,3),(1,5),(2,3),(2,5),(3,3)]:
        I=number_isotropic_maps(n,p);Sp=symplectic_order(n,p)
        print('formula',{'n':n,'p':p,'isotropic_matrices':I,'Sp_order':Sp,
                         'all_RB_operators':p**(2*n)*(2*I+(p-2)*Sp)})
    print('VERIFY_OK')
