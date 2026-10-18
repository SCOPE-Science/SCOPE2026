"""Exact independent finite-instance verification of cycle spanning-tree/1-out coupling."""
from fractions import Fraction
from itertools import product
from math import comb
from collections import defaultdict

checks=0
for n in range(3,11):
    for p in (Fraction(1,2),Fraction(1,3),Fraction(2,5),Fraction(3,4)):
        q=1-p
        dist=defaultdict(Fraction)
        missing_edge_marginal=[Fraction() for _ in range(n)]
        loss_dist=defaultdict(Fraction)
        for bits in product((0,1),repeat=n):
            plus=sum(bits)
            weight=p**plus*q**(n-plus)
            missing=tuple(i for i in range(n) if bits[i]==0 and bits[(i+1)%n]==1)
            m=len(missing)
            dist[m]+=weight
            choices=missing if missing else tuple(range(n))
            for j in choices:
                w=weight/Fraction(len(choices))
                missing_edge_marginal[j]+=w
                # T is all cycle edges but edge j; S is all but 'missing'.
                sym_diff=len(set(missing).symmetric_difference({j}))
                assert sym_diff==abs(m-1), (n,p,bits,j,m,sym_diff)
                checks+=1
                loss_dist[sym_diff]+=w
        assert sum(dist.values())==1
        for marginal in missing_edge_marginal:
            assert marginal==Fraction(1,n), (n,p,marginal)
            checks+=1
        for k in range(n//2+1):
            if k==0:
                expected=p**n+q**n
            else:
                expected=sum(Fraction(n,k)*comb(a-1,k-1)*comb(n-a-1,k-1)*p**a*q**(n-a)
                             for a in range(k,n-k+1))
            assert dist[k]==expected,(n,p,k,dist[k],expected)
            checks+=1
        em=sum(k*v for k,v in dist.items())
        v=sum((k-em)**2*v for k,v in dist.items())
        mu=p*q
        assert em==n*mu,(n,p,em,n*mu)
        assert v==n*mu*(1-3*mu),(n,p,v,n*mu*(1-3*mu))
        checks+=2
        e_loss=sum(k*v for k,v in loss_dist.items())
        assert e_loss==n*mu-1+2*(p**n+q**n)
        checks+=1
        if p==Fraction(1,2):
            for k,mass in dist.items():
                assert mass==Fraction(2*comb(n,2*k),2**n)
                checks+=1
print('PASS',checks,'exact rational assertions')
