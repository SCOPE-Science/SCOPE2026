#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import factorial

def falling(n,k):
    out=1
    for j in range(k):
        out*=n-j
    return out

def cyclic_count(f):
    n=len(f)
    cyc=0
    for v in range(n):
        seen=set()
        x=v
        while x not in seen:
            seen.add(x)
            x=f[x]
        if x==v:
            cyc+=1
    return cyc

def enumerate_law(n):
    total=n**n
    lcount={}
    z_by_l={}
    zsum=0
    zl_sum=0
    for f in product(range(n), repeat=n):
        indeg=[0]*n
        for x in f:
            indeg[x]+=1
        z=sum(d==0 for d in indeg)
        l=cyclic_count(f)
        lcount[l]=lcount.get(l,0)+1
        z_by_l[l]=z_by_l.get(l,0)+z
        zsum+=z
        zl_sum+=z*l
    return total,lcount,z_by_l,zsum,zl_sum

def run():
    laws={}
    mappings_checked=0
    distribution_checks=0
    tail_checks=0
    mean_z_checks=0
    palm_checks=0
    threshold_covariance_checks=0
    covariance_checks=0

    for n in range(1,8):
        laws[n]=enumerate_law(n)
        mappings_checked+=laws[n][0]

        total,lcount,z_by_l,zsum,zl_sum=laws[n]
        for k in range(1,n+1):
            got=Fraction(lcount.get(k,0),total)
            target=Fraction(k*falling(n,k),n**(k+1))
            assert got==target
            distribution_checks+=1

            got_tail=Fraction(sum(v for l,v in lcount.items() if l>=k),total)
            target_tail=Fraction(falling(n,k),n**k)
            assert got_tail==target_tail
            tail_checks+=1

    for n in range(2,8):
        total,lcount,z_by_l,zsum,zl_sum=laws[n]
        prev_total,prev_lcount,_,_,_=laws[n-1]
        ez=Fraction(zsum,total)
        target_ez=n*Fraction(n-1,n)**n
        assert ez==target_ez
        mean_z_checks+=1

        for t in range(1,n+1):
            lhs=Fraction(z_by_l.get(t,0),total)/ez
            rhs=Fraction(prev_lcount.get(t,0),prev_total)
            assert lhs==rhs
            palm_checks+=1

        el=Fraction(sum(l*c for l,c in lcount.items()),total)
        prev_el=Fraction(sum(l*c for l,c in prev_lcount.items()),prev_total)
        cov=Fraction(zl_sum,total)-ez*el
        assert cov==ez*(prev_el-el)
        assert cov<0
        covariance_checks+=1

        for k in range(2,n+1):
            qn=Fraction(falling(n,k),n**k)
            qprev=Fraction(falling(n-1,k),(n-1)**k) if k<=n-1 else Fraction(0)
            ez_tail=Fraction(sum(z_by_l.get(l,0) for l in range(k,n+1)),total)
            got=ez_tail-ez*qn
            target=ez*(qprev-qn)
            assert got==target
            assert got<0
            threshold_covariance_checks+=1

    print(
        "VERIFY_OK "
        f"mappings_checked={mappings_checked} "
        f"distribution_checks={distribution_checks} "
        f"tail_checks={tail_checks} "
        f"mean_z_checks={mean_z_checks} "
        f"palm_checks={palm_checks} "
        f"threshold_covariance_checks={threshold_covariance_checks} "
        f"covariance_checks={covariance_checks}"
    )

if __name__=="__main__":
    run()
