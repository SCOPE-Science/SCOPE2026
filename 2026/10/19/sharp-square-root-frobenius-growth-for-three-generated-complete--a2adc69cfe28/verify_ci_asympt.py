#!/usr/bin/env python3
"""Finite reproducibility checks for the Frobenius-asymptotic theorem.
Only finite examples are checked; the asymptotic proof is separate.
"""
from math import gcd,isqrt,sqrt,prod
from heapq import heappush,heappop

def omega(m):
    n=m; w=0; d=2
    while d*d<=n:
        if n%d==0:
            w+=1
            while n%d==0:n//=d
        d+=1
    return w+(n>1)

def aperture_frobenius(gens):
    m=min(gens); dist=[10**15]*m;dist[0]=0;heap=[(0,0)]
    while heap:
        x,u=heappop(heap)
        if x!=dist[u]:continue
        for v in gens:
            v2=(u+v)%m;y=x+v
            if y<dist[v2]:dist[v2]=y;heappush(heap,(y,v2))
    assert max(dist)<10**15
    return max(dist)-m

def candidate(m):
    b=isqrt(m);start=m//b+1; window=4**omega(m)+1
    a=next(a for a in range(start,start+window) if gcd(a,m)==1)
    assert a*b>m and 1<a and gcd(a,m)==1
    F=a*(b*b-b-1)+(a-1)*m
    return a,b,F

if __name__=='__main__':
    count=0
    for m in range(4,301):
        a,b,F=candidate(m)
        if m<=130:
            gens=(m,a*b,a*(b+1)); actual=aperture_frobenius(gens)
            assert actual==F,(m,gens,F,actual)
            # Minimal generators cannot be expressed by the other two.
            for g in gens:
                other=[x for x in gens if x!=g]
                assert all(g-k*other[0]<0 or (g-k*other[0])%other[1]!=0
                           for k in range(g//other[0]+1)),(m,gens,g)
        assert F>=2*m*sqrt(m-1)-2.5*m-1e-9
        count+=1
    # All small normalized gluings with d in <b,c> and d nonminimal.
    tested=0
    for a in range(2,13):
        for b in range(2,19):
            for c in range(b+1,20):
                if gcd(b,c)!=1:continue
                fu=b*c-b-c
                for d in range(max(b+c,fu+1),90):
                    if gcd(a,d)!=1:continue
                    m=min(a*b,d)
                    if m<4:continue
                    fs=a*fu+(a-1)*d
                    if fs>=2*m*sqrt(m-1)-2.5*m:
                        pass
                    else:raise AssertionError((a,b,c,d,m,fs))
                    if tested%117==0:
                        assert aperture_frobenius((a*b,a*c,d))==fs
                    tested+=1
    print('VERIFY_OK:',count,'constructed multiplicities;',min(count,127),'exact Apéry checks;',tested,'normalized gluing lower-bound checks')
    for m in [100,1000,10000,100000,1000000]:
        a,b,F=candidate(m)
        print('sample',m,'a',a,'b',b,'ratio %.6f'%(F/m**1.5))
