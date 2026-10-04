#!/usr/bin/env python3
from fractions import Fraction
import random
import math

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def moments(xs,ps):
    mu=sum(p*x for x,p in zip(xs,ps))
    ys=[x-mu for x in xs]
    var=sum(p*y*y for y,p in zip(ys,ps))
    mad=sum(p*abs(y) for y,p in zip(ys,ps))
    return mu,var,mad

def bounds2(ps):
    p1,pm=ps[0],ps[-1]
    L2=4*p1*pm/(p1+pm)
    P=Fraction(0)
    U2=Fraction(0)
    for p in ps[:-1]:
        P+=p
        U2=max(U2,4*P*(1-P))
    return L2,U2

def ratio_float(xs,ps):
    _,v,d=moments(xs,ps)
    return float(d)/math.sqrt(float(v))

def run():
    rng=random.Random(20261002)
    random_lower_checks=0
    random_upper_checks=0
    two_point_checks=0
    three_point_endpoint_checks=0
    equal_weight_checks=0
    lower_path_checks=0
    upper_path_checks=0

    for _ in range(30000):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,30) for __ in range(m)])
        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,30),rng.randrange(1,10)))
        _,var,mad=moments(xs,ps)
        L2,U2=bounds2(ps)
        assert mad*mad>=L2*var
        random_lower_checks+=1
        if m==2:
            assert mad*mad==L2*var==U2*var
            two_point_checks+=1
        else:
            assert mad*mad<U2*var
            random_upper_checks+=1

    for _ in range(8000):
        ps=normalize([rng.randrange(1,40) for __ in range(3)])
        p1,p2,p3=ps
        xs=[-p3,Fraction(0),p1]
        _,var,mad=moments(xs,ps)
        L2,U2=bounds2(ps)
        assert mad*mad==L2*var
        assert mad*mad<U2*var
        three_point_endpoint_checks+=1

    for m in range(2,101):
        ps=[Fraction(1,m)]*m
        L2,U2=bounds2(ps)
        assert L2==Fraction(2,m)
        if m%2==0:
            assert U2==1
        else:
            assert U2==Fraction(m*m-1,m*m)
        equal_weight_checks+=2

    for _ in range(6000):
        m=rng.randrange(4,9)
        ps=normalize([rng.randrange(1,30) for __ in range(m)])
        L2,U2=bounds2(ps)
        L=math.sqrt(float(L2))
        U=math.sqrt(float(U2))

        # Lower boundary path: endpoints fixed, interior atoms collapse to zero.
        eps=Fraction(1,10**6)
        p1,pm=ps[0],ps[-1]
        center=Fraction(m-1,2)
        xs=[-pm]
        for i in range(1,m-1):
            xs.append(eps*(Fraction(i)-center))
        xs.append(p1)
        assert all(xs[i]<xs[i+1] for i in range(m-1))
        assert abs(ratio_float(xs,ps)-L)<0.01
        lower_path_checks+=1

        # Upper boundary path across a maximizing cumulative cut.
        P=Fraction(0)
        bestj=1
        bestu=Fraction(-1)
        for j,p in enumerate(ps[:-1],start=1):
            P+=p
            val=P*(1-P)
            if val>bestu:
                bestu=val
                bestj=j
        eps=Fraction(1,10**7)
        xs=[]
        for i in range(bestj):
            xs.append(eps*Fraction(i))
        for i in range(bestj,m):
            xs.append(Fraction(1)+eps*Fraction(i-bestj))
        assert all(xs[i]<xs[i+1] for i in range(m-1))
        assert abs(ratio_float(xs,ps)-U)<0.01
        upper_path_checks+=1

    print(
        "VERIFY_OK "
        f"random_lower_checks={random_lower_checks} "
        f"random_upper_checks={random_upper_checks} "
        f"two_point_checks={two_point_checks} "
        f"three_point_endpoint_checks={three_point_endpoint_checks} "
        f"equal_weight_checks={equal_weight_checks} "
        f"lower_path_checks={lower_path_checks} "
        f"upper_path_checks={upper_path_checks}"
    )

if __name__=="__main__":
    run()
