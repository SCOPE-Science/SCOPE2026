#!/usr/bin/env python3
"""Exact finite checks for partition-multiplicity cylinder probabilities."""
from collections import Counter
from itertools import product
from math import factorial,pi,sqrt
from decimal import Decimal, getcontext

def partitions(n,cap=None):
    if cap is None: cap=n
    if not n:
        yield ()
        return
    for j in range(min(n,cap),0,-1):
        for t in partitions(n-j,j):
            yield (j,)+t

def pn(N):
    p=[0]*(N+1)
    p[0]=1
    for j in range(1,N+1):
        for n in range(j,N+1):p[n]+=p[n-j]
    return p

def exact_small_count(p,n,small):
    # Inclusion/exclusion: m_j=a_j for each requested type j.
    out=0
    base=sum(j*a for j,a in small.items())
    js=list(small)
    for mask in range(1<<len(js)):
        shift=base+sum(j for i,j in enumerate(js) if mask>>i&1)
        out+=(-1)**(mask.bit_count())*(p[n-shift] if n>=shift else 0)
    return out

def brute_group_quotient(multiplicities,j,p=2):
    moduli=[p**r for r,c in sorted(multiplicities.items()) for _ in range(c)]
    if not moduli:return 0
    elements=list(product(*(range(z) for z in moduli)))
    def vec_scale(v,coef): return tuple((coef*x)%mod for x,mod in zip(v,moduli))
    pj_1={vec_scale(v,p**(j-1)) for v in elements}
    pj={vec_scale(v,p**j) for v in elements}
    ker1={v for v in pj_1 if vec_scale(v,p)==(0,)*len(moduli)}
    ker2={v for v in pj if vec_scale(v,p)==(0,)*len(moduli)}
    ratio=len(ker1)//len(ker2)
    out=0
    while ratio>1: assert ratio%p==0; ratio//=p; out+=1
    return out

def main():
    p=pn(3000)
    checks=0
    for n in range(0,20):
        rows=list(partitions(n))
        assert len(rows)==p[n]; checks+=1
        for js in [(1,),(2,),(1,2),(1,2,3)]:
            for a in product((0,1,2),repeat=len(js)):
                small=dict(zip(js,a))
                direct=sum(all(t.count(j)==v for j,v in small.items()) for t in rows)
                assert direct==exact_small_count(p,n,small),(n,small,direct)
                checks+=1
    for n in range(0,30):
        for J,M in [(1,2),(2,2),(3,1)]:
            if n>19: break
            cnt=sum(all(t.count(j)>=M for j in range(1,J+1)) for t in partitions(n))
            S=M*J*(J+1)//2
            assert cnt==(p[n-S] if n>=S else 0)
            checks+=1
    for mults in ({1:1},{1:1,2:2},{2:1,3:1},{1:2,2:1,3:1}):
        for j in (1,2,3,4):
            assert brute_group_quotient(mults,j)==mults.get(j,0)
            checks+=1
    # The limiting constants for r=1,2,3 on the event
    # m_1=...=m_r=0 are r!*(pi/sqrt(6))**r.
    getcontext().prec=60
    for n in (600,1500,3000):
        for r in (1,2,3):
            exact=exact_small_count(p,n,{j:0 for j in range(1,r+1)})
            assert exact>0
            coeff=Decimal(exact)/Decimal(p[n])*Decimal(n)**(Decimal(r)/2)
            prediction=Decimal(str(factorial(r)*(pi/sqrt(6))**r))
            # deliberately coarse convergence bound for finite n
            assert abs(coeff/prediction-1)<Decimal('0.3'),(n,r,coeff,prediction)
            checks+=1
    print('PARTITION_FO_SPEED_FINITE_OK',checks,'checks')
if __name__=='__main__':main()
