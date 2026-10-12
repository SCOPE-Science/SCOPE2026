#!/usr/bin/env python3
"""Standalone finite checks and formal polynomial identities for dihedral-quandle idempotents.
Only Python's standard library is required. Run: python3 verify.py
"""
from itertools import product

# GF(2) multivariate polynomials as sets of monomials (exponent tuples).
NV = 6
ZERO = frozenset()
def variable(i):
    m=[0]*NV;m[i]=1
    return frozenset({tuple(m)})
ONE=frozenset({(0,)*NV})
def add(*polys):
    out=set()
    for p in polys:out.symmetric_difference_update(p)
    return frozenset(out)
def mul(x,y):
    out=set()
    for a in x:
        for b in y:
            mon=tuple(z+w for z,w in zip(a,b))
            if mon in out:out.remove(mon)
            else:out.add(mon)
    return frozenset(out)
def square(x):return mul(x,x)

def square_in_algebra(u,n,scalar_mul=mul,scalar_add=add,zero=ZERO):
    out=[zero for _ in range(n)]
    for i,a in enumerate(u):
        for j,b in enumerate(u):
            k=(2*j-i)%n
            out[k]=scalar_add(out[k],scalar_mul(a,b))
    return out

def symbolic():
    a,b,c,d,t,h=(variable(i) for i in range(6))
    z=add(ONE,t)
    u=[a,b,c,d,add(a,t),add(b,h),add(c,z),add(d,h)]
    residual=[add(v,w) for v,w in zip(square_in_algebra(u,8),u)]
    even0=add(mul(h,t),h,square(t),t)
    even2=add(mul(h,t),square(t),t)
    odd=add(square(h),mul(h,t),b,d)
    assert residual==[even0,odd,even2,odd,even0,odd,even2,odd]
    assert add(even0,even2)==h
    assert add(even2,mul(t,h),square(t),t)==ZERO
    return 8

def gf_mul(x,y,q):
    if q==2:return x&y
    assert q==4
    out=0
    while y:
        if y&1:out ^=x
        y>>=1;x <<=1
        if x&4:x ^=7
    return out

def sq_num(u,q):
    n=len(u);out=[0]*n
    for i,a in enumerate(u):
        if a:
            for j,b in enumerate(u):
                if b:out[(2*j-i)%n] ^=gf_mul(a,b,q)
    return tuple(out)

def predicted(q):
    W0=[(0,4),(2,6),(1,3,5,7)]
    W1=[(1,5),(3,7),(0,2,4,6)]
    out={(0,)*8}
    for j in range(4):
        ws=W0 if j%2==0 else W1
        for alpha,beta,gamma in product(range(q),repeat=3):
            u=[0]*8;u[j]=1
            for val,coords in zip((alpha,beta,gamma),ws):
                for pos in coords:u[pos]^=val
            v=tuple(u)
            assert v not in out
            out.add(v)
    return out

def enumerate_exact(q):
    total=0;proj={};expected=predicted(q)
    for u in product(range(q),repeat=8):
        if sq_num(u,q)==u:
            total+=1
            assert u in expected,('unexpected',q,u)
            b=tuple(u[i]^u[i+4] for i in range(4))
            proj[b]=proj.get(b,0)+1
    assert total==len(expected)==1+4*q**3
    assert proj.get((0,)*4)==1
    for j in range(4):
        basis=tuple(int(j==i) for i in range(4))
        assert proj[basis]==q**3
    assert len(proj)==5
    # The quotient has two families of q^2 nonzero idempotents.
    count4=sum(sq_num(u,q)==u for u in product(range(q),repeat=4))
    assert count4==1+2*q*q
    print(f'GF({q}): R8 idempotents={total}, R4 idempotents={count4}, lift fibers={proj}')

if __name__=='__main__':
    print('GF(2) polynomial residual identities verified:',symbolic())
    for q in (2,4):enumerate_exact(q)
    print('VERIFY_OK')
