#!/usr/bin/env python3
from fractions import Fraction
import random
import math

def normalize3(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def central(xs,ps):
    mu=sum(p*x for x,p in zip(xs,ps))
    ys=[x-mu for x in xs]
    m2=sum(p*y**2 for p,y in zip(ps,ys))
    m3=sum(p*y**3 for p,y in zip(ps,ys))
    m4=sum(p*y**4 for p,y in zip(ps,ys))
    return mu,m2,m3,m4

def gap_num(xs,ps):
    _,v,m3,m4=central(xs,ps)
    # (kappa-gamma^2-1) * v^3
    return m4*v-m3*m3-v**3, v

def V_of_r(r,a,b,c):
    return a*b*r*r+a*c*(1+r)**2+b*c

def G_of_r(r,a,b,c):
    v=V_of_r(r,a,b,c)
    return a*b*c*r*r*(1+r)**2/v**3

def P_of_r(r,a,b,c):
    return (
        a*(b+c)*r**3
        +a*(2*b+c)*r**2
        -c*(a+2*b)*r
        -c*(a+b)
    )

def bisection_root(a,b,c):
    lo=0.0
    hi=1.0
    def pf(x):
        return float(a*(b+c))*x**3+float(a*(2*b+c))*x**2-float(c*(a+2*b))*x-float(c*(a+b))
    while pf(hi)<=0:
        hi*=2.0
    for _ in range(100):
        mid=(lo+hi)/2
        if pf(mid)<=0:
            lo=mid
        else:
            hi=mid
    return (lo+hi)/2

def run():
    rng=random.Random(20261002)
    determinant_checks=0
    normalized_checks=0
    derivative_checks=0
    optimizer_checks=0
    equal_mass_checks=0

    for _ in range(24000):
        a,b,c=normalize3([rng.randrange(1,40),rng.randrange(1,40),rng.randrange(1,40)])
        x1=Fraction(rng.randrange(-20,1),rng.randrange(1,8))
        g1=Fraction(rng.randrange(1,25),rng.randrange(1,9))
        g2=Fraction(rng.randrange(1,25),rng.randrange(1,9))
        xs=[x1,x1+g1,x1+g1+g2]
        ps=[a,b,c]
        lhs_num,v=gap_num(xs,ps)
        vand=a*b*c*(xs[1]-xs[0])**2*(xs[2]-xs[0])**2*(xs[2]-xs[1])**2
        assert lhs_num==vand
        assert lhs_num>0 and v>0
        determinant_checks+=2

        r=g1/g2
        # affine-normalized support (0,r,1+r)
        _,vn,m3n,m4n=central([Fraction(0),r,1+r],ps)
        assert vn==V_of_r(r,a,b,c)
        gn=(m4n*vn-m3n*m3n-vn**3)/vn**3
        assert gn==G_of_r(r,a,b,c)
        normalized_checks+=2

        # Direct rational finite-difference sign agrees locally with -P away from root.
        eps=Fraction(1,10**6)
        if r>eps:
            gl=G_of_r(r-eps,a,b,c)
            gr=G_of_r(r+eps,a,b,c)
            p=P_of_r(r,a,b,c)
            if p<0:
                assert gr>gl
            elif p>0:
                assert gr<gl
            derivative_checks+=1

        root=bisection_root(a,b,c)
        rr=Fraction.from_float(root).limit_denominator(10**7)
        # Numerical location is used only as replay evidence.
        gv=float(G_of_r(rr,a,b,c))
        for mult in (0.7,0.85,1.15,1.4):
            s=Fraction.from_float(root*mult).limit_denominator(10**7)
            if s>0:
                assert gv >= float(G_of_r(s,a,b,c))-2e-7
                optimizer_checks+=1

    a=b=c=Fraction(1,3)
    assert P_of_r(Fraction(1),a,b,c)==0
    assert G_of_r(Fraction(1),a,b,c)==Fraction(1,2)
    equal_mass_checks+=2
    for r in [Fraction(1,10),Fraction(1,2),Fraction(2),Fraction(10)]:
        assert G_of_r(r,a,b,c)<Fraction(1,2)
        equal_mass_checks+=1

    print(
        "VERIFY_OK "
        f"determinant_checks={determinant_checks} "
        f"normalized_checks={normalized_checks} "
        f"derivative_checks={derivative_checks} "
        f"optimizer_checks={optimizer_checks} "
        f"equal_mass_checks={equal_mass_checks}"
    )

if __name__=="__main__":
    run()
