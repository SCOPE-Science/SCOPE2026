#!/usr/bin/env python3
from fractions import Fraction
import random
import math

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def ridits(ps):
    q=[]
    P=Fraction(0)
    for p in ps:
        q.append(P+p/2)
        P+=p
    assert P==1
    return q

def mean_var(xs,ps):
    mu=sum(p*x for x,p in zip(xs,ps))
    var=sum(p*(x-mu)**2 for x,p in zip(xs,ps))
    return mu,var

def cov(xs,ys,ps):
    mx=sum(p*x for x,p in zip(xs,ps))
    my=sum(p*y for y,p in zip(ys,ps))
    return sum(p*(x-mx)*(y-my) for x,y,p in zip(xs,ys,ps))

def lower2(ps):
    s3=sum(p**3 for p in ps)
    P=Fraction(0)
    vals=[]
    for p in ps[:-1]:
        P+=p
        vals.append(Fraction(3)*P*(1-P)/(1-s3))
    return min(vals)

def corr_float(xs,ys,ps):
    _,vx=mean_var(xs,ps)
    _,vy=mean_var(ys,ps)
    c=cov(xs,ys,ps)
    return float(c)/math.sqrt(float(vx*vy))

def run():
    rng=random.Random(20261002)
    variance_checks=0
    cut_checks=0
    lower_checks=0
    upper_equality_checks=0
    boundary_checks=0
    equal_mass_checks=0

    for _ in range(22000):
        m=rng.randrange(2,9)
        ps=normalize([rng.randrange(1,30) for __ in range(m)])
        q=ridits(ps)
        mq,vq=mean_var(q,ps)
        s3=sum(p**3 for p in ps)
        assert mq==Fraction(1,2)
        assert vq==(1-s3)/12
        variance_checks+=2

        P=Fraction(0)
        for j,p in enumerate(ps[:-1]):
            P+=p
            H=[-(1-P) if i<=j else P for i in range(m)]
            _,vh=mean_var(H,ps)
            ch=cov(H,q,ps)
            assert vh==P*(1-P)
            assert ch==P*(1-P)/2
            cut_checks+=2

        cqq=cov(q,q,ps)
        assert cqq==vq
        upper_equality_checks+=1

        if m==2:
            xs=[Fraction(-7,3),Fraction(11,5)]
            _,vx=mean_var(xs,ps)
            cx=cov(xs,q,ps)
            assert cx*cx==vx*vq
            lower_checks+=1
            continue

        xs=[Fraction(0)]
        for __ in range(1,m):
            xs.append(xs[-1]+Fraction(rng.randrange(1,25),rng.randrange(1,9)))
        _,vx=mean_var(xs,ps)
        cx=cov(xs,q,ps)
        lam2=lower2(ps)
        assert cx>0
        assert cx*cx > lam2*vx*vq
        assert cx*cx <= vx*vq
        lower_checks+=2

        P=Fraction(0)
        vals=[]
        for j,p in enumerate(ps[:-1]):
            P+=p
            vals.append((P*(1-P),j))
        _,jstar=min(vals)
        eps=Fraction(1,10**7)
        xb=[Fraction(0)]
        for j in range(m-1):
            gap=Fraction(1) if j==jstar else eps
            xb.append(xb[-1]+gap)
        rho=corr_float(xb,q,ps)
        lam=math.sqrt(float(lam2))
        assert abs(rho-lam)<0.003
        boundary_checks+=1

    for m in range(3,101):
        ps=[Fraction(1,m)]*m
        assert lower2(ps)==Fraction(3,m+1)
        equal_mass_checks+=1

    print(
        "VERIFY_OK "
        f"variance_checks={variance_checks} "
        f"cut_checks={cut_checks} "
        f"lower_checks={lower_checks} "
        f"upper_equality_checks={upper_equality_checks} "
        f"boundary_checks={boundary_checks} "
        f"equal_mass_checks={equal_mass_checks}"
    )

if __name__=="__main__":
    run()
