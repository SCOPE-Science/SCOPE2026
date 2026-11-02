#!/usr/bin/env python3
"""Reproducible checks for the long-border letter-frequency theorem (Python stdlib)."""
from decimal import Decimal, localcontext
from itertools import product
from math import sqrt

def border_data(w):
    return [(j, 2*w[:j].count('1')-j, w[:j].count('1'))
            for j in range(1,len(w)+1) if w[:j]==w[-j:]]

def eligible(w):
    ds=border_data(w)
    return (len(w)>=4 and w[:2]==w[-2:]=='11'
            and all(d<=0 for j,d,c in ds if j>=3)
            and any(d<0 for j,d,c in ds))

def density(w):
    with localcontext() as ctx:
        ctx.prec=100
        ds=border_data(w)
        one=Decimal(1);two=Decimal(2)
        def bp(z):return sum(z**j for j,d,c in ds)
        lo=one;hi=two
        for _ in range(410):
            mid=(lo+hi)/2
            if (two-mid)*bp(mid)-mid>0:lo=mid
            else:hi=mid
        z=(lo+hi)/2
        B=bp(z); S=sum(j*z**j for j,d,c in ds)
        T=sum(c*z**j for j,d,c in ds)
        E=sum(d*z**j for j,d,c in ds)
        den=-two/z+S/B**2
        rho=(-one/z+T/B**2)/den
        assert E<0 and den<0 and rho>one/2,(w,E,den,rho)
        return z,rho,E

if __name__=='__main__':
    phi=(1+sqrt(5))/2
    checked=0
    for n in range(4,17):
        for t in product('01',repeat=n-4):
            w='11'+''.join(t)+'11'
            if not eligible(w):continue
            ds=border_data(w)
            E=sum(d*phi**j for j,d,c in ds)
            assert E<0,(w,E)
            checked+=1
    print('Finite exhaustive short-word boundary check: PASS; eligible cases',checked)
    u='11'+'0'*6+'11'
    for r in range(1,9):
        w=u*r
        ds=border_data(w)
        assert eligible(w)
        assert [(j,d) for j,d,c in ds]==[(1,1),(2,2)]+[(10*t,-2*t) for t in range(1,r+1)]
        lam,rho,E=density(w)
        print('periodic family r=%s length=%s negative_borders=%s lambda=%s rho=%s' %
            (r,len(w),r,str(lam)[:27],str(rho)[:32]))
    print('VERIFIED: all checks passed; finite checks are corroboration, not the infinite proof')
