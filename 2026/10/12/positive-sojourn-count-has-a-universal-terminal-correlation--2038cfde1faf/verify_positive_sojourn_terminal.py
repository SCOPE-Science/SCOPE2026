#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from math import comb, sqrt, pi

def lattice_checks(max_n=16):
    paths=0
    cov_checks=0
    for n in range(1,max_n+1):
        vals=[]
        eabs=[Fraction(0) for _ in range(n)]
        for eps in product((-1,1), repeat=n):
            s=0
            a=0
            for k,e in enumerate(eps):
                s+=e
                if s>0:
                    a+=1
                eabs[k]+=abs(s)
            vals.append((a,s))
            paths+=1
        den=2**n
        EA=Fraction(sum(a for a,s in vals),den)
        ES=Fraction(sum(s for a,s in vals),den)
        EAS=Fraction(sum(a*s for a,s in vals),den)
        cov=EAS-EA*ES
        rhs=Fraction(1,2)*sum(x/Fraction(den) for x in eabs)
        assert cov==rhs
        cov_checks+=1
    return paths,cov_checks

def arcsine_checks(max_n=200):
    norm=mean=var=0
    for n in range(1,max_n+1):
        ps=[Fraction(comb(2*r,r)*comb(2*(n-r),n-r),4**n) for r in range(n+1)]
        assert sum(ps)==1
        norm+=1
        mu=sum(Fraction(r)*ps[r] for r in range(n+1))
        assert mu==Fraction(n,2)
        mean+=1
        vv=sum((Fraction(r)-mu)**2*ps[r] for r in range(n+1))
        assert vv==Fraction(n*(n+1),8)
        var+=1
    return norm,mean,var

def gaussian_checks():
    target=4/(3*sqrt(pi))
    checked=0
    last=None
    for n in (10,100,1000,10000,100000):
        sm=sum(sqrt(k) for k in range(1,n+1))
        corr=2/sqrt(pi)*sm/(n*sqrt(n+1))
        assert 0<corr<1
        if last is not None:
            assert abs(corr-target)<abs(last-target)
        last=corr
        checked+=1
    assert abs(last-target)<0.002
    return checked,last,target

def run():
    paths,covs=lattice_checks()
    norm,means,vars_=arcsine_checks()
    gc,last,target=gaussian_checks()
    print(
        "VERIFY_OK "
        f"lattice_paths={paths} "
        f"covariance_checks={covs} "
        f"arcsine_normalizations={norm} "
        f"arcsine_means={means} "
        f"arcsine_variances={vars_} "
        f"gaussian_checks={gc} "
        f"last_corr={last:.12f} "
        f"target={target:.12f}"
    )

if __name__=="__main__":
    run()
