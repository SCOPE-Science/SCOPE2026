#!/usr/bin/env python3
"""Finite-field direct checks for center-affine Rota--Baxter maps on Heisenberg groups.
Only elementary modular arithmetic is required.  This is independent of any symbolic proof.
"""
from itertools import product
from random import Random


def dot(a,b,p): return sum(x*y for x,y in zip(a,b))%p

def omega(v,w,p):
    n=len(v)//2
    return (dot(v[:n],w[n:],p)-dot(v[n:],w[:n],p))%p

def mv(T,v,p): return tuple(dot(row,v,p) for row in T)

def add(v,w,p): return tuple((a+b)%p for a,b in zip(v,w))

def gp(g,h,p):
    v,z=g;w,t=h
    return add(v,w,p), (z+t+omega(v,w,p)*pow(2,-1,p))%p

def neg(g,p):
    v,z=g;return tuple(-a%p for a in v),(-z)%p

def RB(T,mu,ell,p):
    inv2=pow(2,-1,p)
    def b(g):
        v,z=g
        tv=mv(T,v,p)
        return tv,(mu*z+mu*inv2*omega(v,tv,p)+dot(ell,v,p))%p
    return b

def direct_check(T,mu,ell,p,samples=None):
    dim=len(T);b=RB(T,mu,ell,p)
    G=[(v,z) for v in product(range(p),repeat=dim) for z in range(p)]
    if samples is None: pairs=product(G,G)
    else:
        rng=Random(913)
        pairs=((rng.choice(G),rng.choice(G)) for _ in range(samples))
    for g,h in pairs:
        bg=b(g)
        lhs=gp(bg,b(h),p)
        rhs=b(gp(g,gp(gp(bg,h,p),neg(bg,p),p),p))
        if lhs!=rhs: return False
    return True

def condition(T,mu,p):
    d=len(T)
    S=[[ (T[i][j]-(mu if i==j else 0))%p for j in range(d)] for i in range(d)]
    cols=[tuple(S[i][j] for i in range(d)) for j in range(d)]
    for i in range(d):
        for j in range(d):
            e_i=tuple(int(t==i) for t in range(d))
            e_j=tuple(int(t==j) for t in range(d))
            if omega(cols[i],cols[j],p)!=(mu*(mu+1)*omega(e_i,e_j,p))%p:
                return False
    return True

def mat(t,d): return [list(t[i*d:(i+1)*d]) for i in range(d)]

def check_all_small(p):
    counted={k:0 for k in range(p)}
    for tup in product(range(p),repeat=4):
        T=mat(tup,2)
        for mu in range(p):
            should=condition(T,mu,p)
            if should:counted[mu]+=1
            if p==3:
                actual=direct_check(T,mu,(0,0),p)
                assert should==actual, (T,mu,should,actual)
    sp=p*(p*p-1)
    iso=1+(p+1)*(p*p-1)
    for mu in range(p):
        assert counted[mu]==(iso if mu in (0,p-1) else sp),(p,mu,counted)
    return counted

def check_dimension_four():
    p=3;d=4;rng=Random(735)
    for mu in range(p):
        for idx in range(18):
            if mu in (0,p-1):
                # Isotropic image in the first two coordinates.
                S=[[rng.randrange(p) for _ in range(d)] for _ in range(2)]+[[0]*d for _ in range(2)]
            else:
                # Diagonal symplectic similitude in the split basis.
                c=mu*(mu+1)%p
                S=[[int(i==j)*(1 if i<2 else c) for j in range(d)] for i in range(d)]
            T=[[(S[i][j]+(mu if i==j else 0))%p for j in range(d)] for i in range(d)]
            assert condition(T,mu,p)
            ell=tuple(rng.randrange(p) for _ in range(d))
            assert direct_check(T,mu,ell,p,samples=200)
    # A map with no reason to satisfy the criterion should generally fail.
    failures=0
    for i in range(100):
        T=[[rng.randrange(p) for _ in range(d)] for _ in range(d)]
        mu=rng.randrange(p)
        if not condition(T,mu,p):
            failures+=1
            assert not direct_check(T,mu,(0,0,0,0),p,samples=800)
    assert failures>50

if __name__=='__main__':
    a=check_all_small(3)
    b=check_all_small(5)
    check_dimension_four()
    print('p=3, n=1, per-mu counts:',a,' total maps:',3**2*sum(a.values()))
    print('p=5, n=1, per-mu counts:',b,' total maps:',5**2*sum(b.values()))
    print('dimension-four independent group-law samples passed')
    print('VERIFY_OK')
