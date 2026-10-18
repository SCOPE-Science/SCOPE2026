#!/usr/bin/env python3
"""Reproduce finite-field rank-one Rota--Baxter counts without external packages.

Usage: python verify.py
Only prime fields in the finite checks; the theorem covers all finite fields.
"""
from itertools import product
from math import prod

def gauss(n,r,q):
    if r<0 or r>n:return 0
    return prod(q**(n-j)-1 for j in range(r))//prod(q**(r-j)-1 for j in range(r))

def gl(n,q): return prod(q**n-q**j for j in range(n))

def formula(n,q):
    nil=sum(gauss(n,r,q)*gauss(n-r,r,q)*gl(r,q)*(q**((n-r)**2)-1)//(q-1)
            for r in range(1,n//2+1))
    idem=2*sum(gauss(n,r,q)*q**(r*(n-r))*(q**(r*(n-r))-1) for r in range(1,n))
    return nil,idem

def mm(a,b,n,q):
    return tuple(sum(a[i*n+k]*b[k*n+j] for k in range(n))%q
                 for i in range(n) for j in range(n))

def check(n,q):
    mats=list(product(range(q),repeat=n*n))
    z=(0,)*(n*n)
    count={'nil':set(),'idem':set()}
    pairs=0
    for u in mats[1:]:
        u2=mm(u,u,n,q)
        k=next(j for j in range(n*n) if u[j])
        for v in mats[1:]:
            uv=mm(u,v,n,q);vu=mm(v,u,n,q)
            nil=(u2==z and uv==z and vu==z)
            lam=(u2[k]*pow(u[k],-1,q))%q
            is_projection=lam!=0 and all(u2[j]==lam*u[j]%q for j in range(n*n))
            idem=is_projection and ((uv==z and all(vu[j]==lam*v[j]%q for j in range(n*n)))
                                   or (vu==z and all(uv[j]==lam*v[j]%q for j in range(n*n))))
            f=tuple(v[j*n+i] for i in range(n) for j in range(n))
            alpha=tuple(vu[j*n+i] for i in range(n) for j in range(n))
            beta=tuple(uv[j*n+i] for i in range(n) for j in range(n))
            # Test the ORIGINAL polynomial on every ordered pair of matrix units.
            rb=True
            for i in range(n*n):
                for j in range(n*n):
                    c=f[i]*f[j]
                    d=f[i]*alpha[j]+f[j]*beta[i]
                    if any((c*u2[t]-d*u[t])%q for t in range(n*n)):
                        rb=False;break
                if not rb:break
            if rb!=(nil or idem):
                raise AssertionError(('RB-classification mismatch',n,q,u,v,rb,nil,idem))
            if not rb:continue
            pairs+=1
            # Matrix coefficients of R(X)=tr(vX)u on the matrix-unit basis.
            key=tuple((c*w)%q for c in f for w in u)
            count['nil' if nil else 'idem'].add(key)
            if sum(u[i*n+j]*v[j*n+i] for i in range(n) for j in range(n))%q:
                raise AssertionError('R squared nonzero')
    a,b=formula(n,q)
    assert len(count['nil'])==a,(n,q,a,len(count['nil']))
    assert len(count['idem'])==b,(n,q,b,len(count['idem']))
    assert count['nil'].isdisjoint(count['idem'])
    print(f'PASS n={n} q={q}: nilpotent-image={a}, idempotent-image={b}, total={a+b}; witnesses={pairs}')

if __name__=='__main__':
    for n,q in [(2,2),(2,3),(3,2)]:check(n,q)
