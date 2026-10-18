#!/usr/bin/env python3
"""Stand-alone check of finite-group automorphism fixed-point distributions.
Uses relation-lattice minors rather than the proof's congruence case split.
"""
from collections import Counter
from math import gcd
from itertools import product


def formula(p,m):
    if m < 3:
        raise ValueError('the checker supports the previously known boundary m=3')
    z={0:p**(m+1)*(p-2)**2,
       1:p**m*(p-2)*(2*p-1),
       m-1:p*(p-1)**2*(2*p+1),
       m:p**3-p-1,
       m+1:1}
    for j in range(2,m-1):
        z[j]=2*(p-1)**2*p**(m-j+1)
    return {j:z.get(j,0) for j in range(m+2)}


def exact_from_relation_minors(p,m):
    order=p**m
    rows=Counter()
    for a in range(1,order):
        if a%p==0: continue
        for d in range(1,p):
            for b,c in product(range(p),repeat=2):
                s=gcd(p**(m+1),p**m*c,p**m*(d-1),p*(a-1),p**m*b,(a-1)*(d-1)-p**(m-1)*b*c)
                v=0
                while s>1 and s%p==0:
                    s//=p;v+=1
                assert s==1
                rows[v]+=1
    return {j:rows[j] for j in range(m+2)}


def exact_by_group_elements(p,m):
    order=p**m
    ctr=Counter()
    for a in range(1,order):
        if a%p==0: continue
        for d in range(1,p):
            for b,c in product(range(p),repeat=2):
                count=0
                for x in range(order):
                    for y in range(p):
                        if ((a-1)*x+p**(m-1)*b*y)%order==0 and (c*x+(d-1)*y)%p==0:
                            count+=1
                v=0;k=count
                while k>1 and k%p==0:
                    k//=p;v+=1
                assert k==1
                ctr[v]+=1
    return {j:ctr[j] for j in range(m+2)}


if __name__=='__main__':
    for p,m in [(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(5,3),(5,4)]:
        expected=formula(p,m)
        got=exact_from_relation_minors(p,m)
        assert expected==got,(p,m,expected,got)
        assert sum(got.values())==(p-1)**2*p**(m+1)
        assert sum(got[j]*p**j for j in got) % ((p-1)**2*p**(m+1)) ==0
        if m==4:
            # Published Anilkumar--Prasad ordered-pair orbit polynomial for type (4,1).
            paired=sum(got[j]*p**(2*j) for j in got)//((p-1)**2*p**(m+1))
            assert paired==p**4+5*p**3+7*p**2+6*p+4
        # Independent brute fixed-element evaluation on bounded cases
        if (p,m) in {(2,3),(2,4),(3,3),(5,3)}:
            direct=exact_by_group_elements(p,m)
            assert got==direct,(p,m,got,direct)
        print('PASS',p,m, got)
    print('VERIFY_OK')
