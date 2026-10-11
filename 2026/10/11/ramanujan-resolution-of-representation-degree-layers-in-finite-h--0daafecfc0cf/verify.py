#!/usr/bin/env python3
from fractions import Fraction
from math import gcd

def factor(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            a=0
            while n%p==0: n//=p; a+=1
            out.append((p,a))
        p += 1 if p==2 else 2
    if n>1: out.append((n,1))
    return out

def phi(n):
    r=n
    for p,_ in factor(n): r=r//p*(p-1)
    return r

def mu(n):
    s=0
    for _,a in factor(n):
        if a>1:return 0
        s+=1
    return -1 if s%2 else 1

def omega(n): return len(factor(n))

def ram(m,t):
    if m==1:return 1
    g=gcd(m,t)
    q=m//g
    return mu(q)*phi(m)//phi(q)

def divisors(n):
    return [d for d in range(1,n+1) if n%d==0]

checks=0
for n in range(2,121):
    # Bump/Grassberger degree count exhausts the regular representation.
    assert sum(((n//m)**2)*phi(m)*(m*m) for m in divisors(n)) == n**3
    # Degree-layer kernels on the center form an exact orthogonal resolution.
    kernels={}
    for m in divisors(n):
        w=[Fraction(ram(m,t),n) for t in range(n)]
        kernels[m]=w
        # total variation formula
        tv=sum(abs(x) for x in w)
        expected=Fraction((2**omega(m))*phi(m),m)
        assert tv==expected,(n,m,tv,expected)
        # rank from central exact-order character multiplicity
        assert n*n*phi(m) == ((n//m)**2)*phi(m)*(m*m)
        # idempotence on the central cyclic subgroup
        conv=[sum(w[s]*w[(t-s)%n] for s in range(n)) for t in range(n)]
        assert conv==w,(n,m)
        # complement total variation
        comp=[-x for x in w]
        comp[0]+=1
        ctv=sum(abs(x) for x in comp)
        cexp=Fraction(1,1)+expected-Fraction(2*phi(m),n)
        assert ctv==cexp,(n,m,ctv,cexp)
        # contractivity classification
        assert (expected==1) == (m & (m-1) == 0)
        checks+=1
    ds=divisors(n)
    # pairwise orthogonality and partition of the identity.
    for i,m in enumerate(ds):
        for k in ds[i+1:]:
            a,b=kernels[m],kernels[k]
            conv=[sum(a[s]*b[(t-s)%n] for s in range(n)) for t in range(n)]
            assert all(x==0 for x in conv),(n,m,k)
    total=[sum(kernels[m][t] for m in ds) for t in range(n)]
    assert total[0]==1 and all(total[t]==0 for t in range(1,n)),n
print(f"VERIFY_OK n=2..120 degree_layers={checks} exact_fraction_checks=all")
