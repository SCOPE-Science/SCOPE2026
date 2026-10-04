#!/usr/bin/env python3
from fractions import Fraction
from math import factorial, sqrt
import random

def beta_int(r,s):
    return Fraction(factorial(r)*factorial(s), factorial(r+s+1))

def ell_u(r,s):
    c=beta_int(r,s)
    ar=Fraction(1,r+1); ass=Fraction(1,s+1)
    br=Fraction(1,2*r+1); bs=Fraction(1,2*s+1)
    ell_num=c-ar*ass
    ell_den=(br-ar*ar)*(bs-ass*ass)
    u2=c*c/(br*bs)
    return ell_num,ell_den,u2

def moments_interarrival(xs,ps,t):
    return sum(p*(x**t) for x,p in zip(xs,ps))

def corr_parts(xs,ps,r,s):
    m1=moments_interarrival(xs,ps,1)
    c=beta_int(r,s)
    EA=moments_interarrival(xs,ps,r+1)/((r+1)*m1)
    ER=moments_interarrival(xs,ps,s+1)/((s+1)*m1)
    EAA=moments_interarrival(xs,ps,2*r+1)/((2*r+1)*m1)
    ERR=moments_interarrival(xs,ps,2*s+1)/((2*s+1)*m1)
    EAR=c*moments_interarrival(xs,ps,r+s+1)/m1
    cov=EAR-EA*ER
    va=EAA-EA*EA
    vr=ERR-ER*ER
    return cov,va,vr

def inverse_size_bias(xs,hs):
    z=sum(h/x for x,h in zip(xs,hs))
    mu=1/z
    ps=[mu*h/x for x,h in zip(xs,hs)]
    assert sum(ps,Fraction(0))==1
    return ps

def run():
    rng=random.Random(20261002)
    random_checks=0
    endpoint_checks=0
    upper_path_checks=0

    for r in range(1,8):
        for s in range(1,8):
            if r==s:
                continue
            ell_num,ell_den,u2=ell_u(r,s)
            assert ell_num < 0
            for _ in range(800):
                k=rng.randrange(2,6)
                xs=sorted(set(Fraction(rng.randrange(1,25), rng.randrange(1,9)) for __ in range(k)))
                if len(xs)<2:
                    continue
                raw=[rng.randrange(1,30) for __ in xs]
                total=sum(raw)
                ps=[Fraction(z,total) for z in raw]
                cov,va,vr=corr_parts(xs,ps,r,s)
                assert va>0 and vr>0

                # lower bound: compare signs and squares only when covariance is negative
                if cov < 0:
                    # corr >= ell < 0  iff corr^2 <= ell^2
                    assert cov*cov*ell_den <= ell_num*ell_num*va*vr
                # upper bound: if corr positive, corr^2 < u^2
                if cov > 0:
                    assert cov*cov < u2*va*vr
                random_checks += 1

            # deterministic lower equality
            xs=[Fraction(7,3)]
            ps=[Fraction(1)]
            cov,va,vr=corr_parts(xs,ps,r,s)
            assert cov<0
            assert cov*cov*ell_den == ell_num*ell_num*va*vr
            endpoint_checks += 1

            # explicit rare-large size-biased path, converted to an interarrival law
            t=min(r,s)
            vals=[]
            for M in (10,100,1000):
                p=Fraction(1,M**t)
                Lxs=[Fraction(1),Fraction(M)]
                hs=[1-p,p]
                ips=inverse_size_bias(Lxs,hs)
                cov,va,vr=corr_parts(Lxs,ips,r,s)
                vals.append(float(cov)/sqrt(float(va*vr)))
            target=sqrt(float(u2))
            assert abs(target-vals[-1]) < abs(target-vals[0])
            upper_path_checks += 1

    print(
        "VERIFY_OK "
        f"random_bound_checks={random_checks} "
        f"deterministic_endpoint_checks={endpoint_checks} "
        f"upper_path_checks={upper_path_checks}"
    )

if __name__=="__main__":
    run()
