#!/usr/bin/env python3
from fractions import Fraction
import random
import math

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def variance(xs,ps):
    mu=sum(p*x for x,p in zip(xs,ps))
    return sum(p*(x-mu)**2 for x,p in zip(xs,ps))

def bounds(ps):
    L=ps[0]*ps[-1]/(ps[0]+ps[-1])
    P=Fraction(0)
    U=Fraction(0)
    jstar=1
    for j,p in enumerate(ps[:-1],start=1):
        P+=p
        v=P*(1-P)
        if v>U:
            U=v
            jstar=j
    return L,U,jstar

def run():
    rng=random.Random(20261002)
    random_lower=0
    random_upper=0
    two_point=0
    three_point_lower=0
    equal_mass=0
    lower_paths=0
    upper_paths=0

    for _ in range(30000):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,30) for __ in range(m)])
        gaps=[Fraction(rng.randrange(1,30),rng.randrange(1,10)) for __ in range(m-1)]
        total=sum(gaps)
        gaps=[g/total for g in gaps]
        xs=[Fraction(0)]
        for g in gaps:
            xs.append(xs[-1]+g)
        assert xs[-1]==1
        v=variance(xs,ps)
        L,U,jstar=bounds(ps)
        assert v>=L
        random_lower+=1
        if m==2:
            assert v==L==U
            two_point+=1
        else:
            assert v<U
            random_upper+=1

    for _ in range(10000):
        ps=normalize([rng.randrange(1,40) for __ in range(3)])
        p1,p2,pm=ps
        c=pm/(p1+pm)
        xs=[Fraction(0),c,Fraction(1)]
        v=variance(xs,ps)
        L,U,jstar=bounds(ps)
        assert v==L and v<U
        three_point_lower+=1

    for m in range(2,101):
        ps=[Fraction(1,m)]*m
        L,U,jstar=bounds(ps)
        assert L==Fraction(1,2*m)
        if m%2==0:
            assert U==Fraction(1,4)
        else:
            assert U==Fraction(m*m-1,4*m*m)
        equal_mass+=2

    for _ in range(6000):
        m=rng.randrange(4,9)
        ps=normalize([rng.randrange(1,30) for __ in range(m)])
        L,U,jstar=bounds(ps)
        c=ps[-1]/(ps[0]+ps[-1])

        eps=Fraction(1,10**7)
        offsets=[Fraction(2*i-(m-3),1) for i in range(m-2)]
        xs=[Fraction(0)]+[c+eps*t for t in offsets]+[Fraction(1)]
        assert all(xs[i]<xs[i+1] for i in range(m-1))
        v=variance(xs,ps)
        assert v>L
        assert float(v-L)<1e-4
        lower_paths+=1

        eps=Fraction(1,10**8)
        xs=[]
        for i in range(jstar):
            xs.append(eps*Fraction(i))
        for i in range(jstar,m):
            xs.append(Fraction(1)-eps*Fraction(m-1-i))
        assert all(xs[i]<xs[i+1] for i in range(m-1))
        v=variance(xs,ps)
        assert v<U
        assert float(U-v)<1e-4
        upper_paths+=1

    print(
        "VERIFY_OK "
        f"random_lower_checks={random_lower} "
        f"random_upper_checks={random_upper} "
        f"two_point_checks={two_point} "
        f"three_point_lower_checks={three_point_lower} "
        f"equal_mass_checks={equal_mass} "
        f"lower_path_checks={lower_paths} "
        f"upper_path_checks={upper_paths}"
    )

if __name__=="__main__":
    run()
