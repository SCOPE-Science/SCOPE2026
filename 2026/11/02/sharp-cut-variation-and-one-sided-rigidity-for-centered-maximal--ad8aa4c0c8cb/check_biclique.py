#!/usr/bin/env python3
"""Standalone finite rational checks of explicit bipartite graph formulas.
The all-dimension inequalities are established in the accompanying proof.
"""
from fractions import Fraction as F
from itertools import combinations, product

COUNT=0

def verify(ok, message):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(message)

def mass_ratio(m,n):
    N=m+n
    ra=F(m,m+1)+F((m-1)*(n-1),(m+1)*N)
    rb=F(n,n+1)+F((m-1)*(n-1),(n+1)*N)
    return ra,rb

def maximal(m,n,f):
    a=f[:m];b=f[m:];suma=sum(a);sumb=sum(b);mu=F(suma+sumb,m+n)
    return [max(x,(x+sumb)/F(n+1),mu) for x in a]+[max(y,(y+suma)/F(m+1),mu) for y in b]

def variation(m,n,f):
    return sum(abs(a-b) for a in f[:m] for b in f[m:])

def composition(k,total):
    if k==1:
        yield (total,)
    else:
        for i in range(total+1):
            for tail in composition(k-1,total-i):
                yield (i,)+tail

def run():
    for m in range(2,9):
        for n in range(2,10):
            ra,rb=mass_ratio(m,n);c=max(ra,rb)
            N=m+n
            delta=(m-2)*(n-2)-3
            verify((c>1)-(c<1)==(delta>0)-(delta<0),('threshold',m,n))
            verify((ra>rb)-(ra<rb)==(n-m>0 and delta>0 or n-m<0 and delta<0)-(n-m>0 and delta<0 or n-m<0 and delta>0),('orientation',m,n))
            for k in range(m+1):
                for ell in range(n+1):
                    if (k==0 and ell==0) or (k==m and ell==n):
                        continue
                    f=[F(1)]*k+[F(0)]*(m-k)+[F(1)]*ell+[F(0)]*(n-ell)
                    d=variation(m,n,f); out=maximal(m,n,f)
                    ratio=variation(m,n,out)/d
                    verify(ratio<=c,('cut bound',m,n,k,ell,ratio,c))
                    if k==1 and ell==0:
                        verify(ratio==ra,('left singleton',m,n))
                    if k==0 and ell==1:
                        verify(ratio==rb,('right singleton',m,n))
    for m in range(2,7):
        for n in range(2,9):
            ra,_=mass_ratio(m,n)
            a=F(1,m+n); b=F(1,m+1)
            kappa=min(1-2*b+a,2*b-a)
            verify(kappa>0,('positive rigidity coefficient',m,n))
            for total in range(1,9):
                for v in composition(m,total):
                    f=[F(t) for t in v]+[F(0)]*n
                    out=maximal(m,n,f)
                    ratio=variation(m,n,out)/variation(m,n,f)
                    p=[F(t,total) for t in v]
                    q=sum(min(x,1-x) for x in p)
                    verify(ratio<=ra,('one-sided bound',m,n,v,ratio,ra))
                    verify(ra-ratio>=kappa*q,('rigidity',m,n,v))
                    if sum(t!=0 for t in v)==1:
                        verify(ratio==ra,('one-sided sharp',m,n,v))
                    else:
                        verify(ratio<ra,('one-sided strict',m,n,v))
    for m in range(2,101):
        for n in range(2,101):
            ra,rb=mass_ratio(m,n);delta=(m-2)*(n-2)-3
            verify((ra-1)*((m+1)*(m+n))==delta,('first threshold factor',m,n))
            verify((rb-1)*((n+1)*(m+n))==delta,('second threshold factor',m,n))
            verify(ra<2 and rb<2,('two bound',m,n))
    print('PASS:',COUNT,'exact-rational assertions')

if __name__=='__main__':
    run()
