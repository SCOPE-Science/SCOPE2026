#!/usr/bin/env python3
"""Exact coefficient tests for F_(t^2)-C_t, using integer recurrences."""
from math import gcd, comb


def sigma_array(n):
    s = [0] * (n + 1)
    for d in range(1,n+1):
        for k in range(d,n+1,d): s[k] += d
    return s


def coeffs(t,n):
    """Differentiate Euler products logarithmically; all divisions are exact."""
    sig=sigma_array(n)
    a=[1]+[0]*n
    b=[1]+[0]*n
    for m in range(1,n+1):
        sa=-t*t*sum(sig[j]*a[m-j] for j in range(1,m+1))
        sb=sum((-t*t*sig[j//t] if j%t==0 else 0)*b[m-j]
               for j in range(1,m+1))
        assert sa%m==0 and sb%m==0,(t,m,sa,sb)
        a[m]=sa//m
        b[m]=sb//m
    # a is coefficient of A(x)^(t*t) and b coefficient of A(x^t)^t.
    # The original F_(t^2)-C_t is (a-b)/A(x), a unit; its p-content equals the content of a-b.
    return a,b



def direct_product(t,n):
    """Independent finite product expansion of both numerator Euler products."""
    def power_product(step,exp):
        c=[1]+[0]*n
        for m in range(step,n+1,step):
            a=[((-1)**j)*comb(exp,j) for j in range(min(n//m,exp)+1)]
            z=c[:]
            for degree in range(n+1):
                for j in range(1,min(degree//m,len(a)-1)+1):
                    z[degree]+=c[degree-j*m]*a[j]
            c=z
        return c
    return power_product(1,t*t),power_product(t,t)


def factor(n):
    ret=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0: n//=d;e+=1
            ret.append((d,e))
        d+=1
    if n>1:ret.append((n,1))
    return ret


def main():
    primepowers=[2,3,4,5,7,8,9,11,16,25,27,32,49,64,81,125]
    mixed=[6,10,12,14,15,18,20,21,22,24,26,28,30,33,35,36,40,42,45,50,54,60,72,84,90,105]
    checked=0
    direct_checked=0
    for t in primepowers+mixed:
        fs=factor(t)
        N=max(2*t if len(fs)==1 else 0,max((p**(2*e) for p,e in fs),default=0))
        N=(min(N,250) if len(fs)==1 else N)
        a,b=coeffs(t,N)
        diff=[a[i]-b[i] for i in range(N+1)]
        g=0
        for z in diff:g=gcd(g,z)
        if len(fs)==1:
            p,e=fs[0]
            d=p**(e-1)
            assert g==p**(e+1),(t,g,p**(e+1))
            assert all(z % p**(e+1)==0 for z in diff),(t,'uniform')
            assert all(z%p**(e+2)==0 for z in diff[:d]),(t,'earlier')
            assert diff[d] % p**(e+2)==(-p**(e+1))%p**(e+2),(t,'sharp')
            checked+=len(diff)
        else:
            assert g==1,(t,g)
            for p,e in fs:
                d=p**(2*e)
                assert d<=N
                m=t//p**e
                assert all(z%p==0 for z in diff[:d]),(t,p,'early')
                assert diff[d]%p==(-m*m)%p,(t,p,'first failure')
                checked+=d+1
        if t in (2,3,4,5,6,7,8,9,10,12,15):
            nd=min(N,30)
            ad,bd=direct_product(t,nd)
            assert a[:nd+1]==ad and b[:nd+1]==bd,(t,'independent')
            direct_checked+=2*(nd+1)
        print(f't={t:3d} factors={fs} checked_deg={N:3d} gcd={g}')
    print(f'PASS: {len(primepowers)} prime powers, {len(mixed)} mixed-prime moduli; {checked} modular coefficient tests; {direct_checked} direct-product crosschecks')

if __name__=='__main__': main()
