#!/usr/bin/env python3
"""Exact characteristic-p checks for a plane-filling curve's dual-branch formula.

The universal argument is in RESULT.md; these finite specializations check its
coordinate identities and the numerical semigroup computations independently.
Requires Python 3 and SymPy for the optional symbolic Hessian computation.
"""
from math import gcd


def add(a,b,p):
    c=dict(a)
    for e,v in b.items():
        v=(c.get(e,0)+v)%p
        if v:c[e]=v
        elif e in c:del c[e]
    return c


def neg(a,p):
    return {e:(-v)%p for e,v in a.items()}


def mul(a,b,p,N):
    c={}
    for i,x in a.items():
        for j,y in b.items():
            if i+j<N:c[i+j]=(c.get(i+j,0)+x*y)%p
    return {i:v for i,v in c.items() if v}


def power(a,n,p,N):
    r={0:1}
    while n:
        if n&1:r=mul(r,a,p,N)
        n//=2
        if n:a=mul(a,a,p,N)
    return r


def monomial(e):return {e:1}


def valuation(a):
    return min(a) if a else float('inf')


def inverse_unit(a,p,N):
    assert a.get(0)==1
    h=add({0:1},neg(a,p),p)
    out={0:1}
    term={0:1}
    for i in range(N):
        term=mul(term,h,p,N)
        if not term:break
        out=add(out,term,p)
    return out


def check(p,e):
    q=p**e
    M=(q+1)**2+1
    N=2*M+6
    t=monomial(1)
    x={}
    for it in range(40):
        new=add(neg(monomial(q+1),p),
                neg(mul(t,power(x,q+1,p,N),p,N),p),p)
        if new==x:break
        x=new
    else:raise AssertionError('fixed point did not stabilize')
    assert not add(add(x,monomial(q+1),p),mul(t,power(x,q+1,p,N),p,N),p)
    assert valuation(x)==q+1
    denominator=add({0:1},mul(t,power(x,q,p,N),p,N),p)
    inv=inverse_unit(denominator,p,N)
    assert mul(denominator,inv,p,N)=={0:1}
    Fy=add(power(x,q+1,p,N),monomial(q),p)
    Fz=neg(mul(t,power(x,q+1,p,N),p,N),p)
    u=mul(Fy,inv,p,N)
    v=mul(Fz,inv,p,N)
    assert valuation(u)==q,(q,valuation(u))
    assert valuation(v)==M,(M,valuation(v))
    assert gcd(q,M)==1
    conductor=(q-1)*(M-1)
    B=conductor+M+q
    representable={a*q+b*M for a in range(B//q+2)
                     for b in range(B//M+2)}
    gaps=[n for n in range(conductor) if n not in representable]
    assert len(gaps)==conductor//2
    assert all(n in representable for n in range(conductor,conductor+M+q))
    return q,M,conductor//2,it


def check_hessian(p,q):
    try:import sympy as s
    except ImportError:return 'sympy unavailable: formal series checks completed'
    X,Y,Z=s.symbols('X Y Z')
    F=X**(q+1)*Y+Y**(q+1)*Z+Z**(q+1)*X
    H=s.hessian(F,[X,Y,Z]);det=H.det(method='domain-ge')
    diff=s.Poly(s.expand(det-2*(X*Y*Z)**q),X,Y,Z,modulus=p)
    assert diff.is_zero, f'Hessian failed at characteristic {p}, q={q}'
    return 'exact symbolic Hessian identity'


if __name__=='__main__':
    for p,e in [(3,1),(5,1),(7,1),(3,2)]:
        q,M,delta,it=check(p,e)
        assert delta == (q-1)*(q+1)**2//2
        print('q=%d, dual valuations=(%d,%d), delta=%d; %s; formal fixed-point iterations=%d' %
              (q,q,M,delta,check_hessian(p,q),it+1))
    print('VERIFY_OK')
