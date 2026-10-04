#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import random
import math

def normalize(raw):
    s=sum(raw)
    return [Fraction(x,s) for x in raw]

def moments(xs,ps):
    mu=sum(p*x for p,x in zip(ps,xs))
    v=sum(p*(x-mu)**2 for p,x in zip(ps,xs))
    m3=sum(p*(x-mu)**3 for p,x in zip(ps,xs))
    return mu,v,m3

def g_sign_square(p):
    num=2*p-1
    sq=num*num/(p*(1-p))
    return (0 if num==0 else (1 if num>0 else -1)), sq

def compare_gamma_to_g(m3,v,p):
    # Return sign of gamma-g(p), using exact rational arithmetic.
    sg = 0 if m3==0 else (1 if m3>0 else -1)
    sp, gp2 = g_sign_square(p)
    if sg != sp:
        return 1 if sg > sp else -1
    if sg == 0:
        return 0
    gam2=m3*m3/(v*v*v)
    if gam2==gp2:
        return 0
    if sg>0:
        return 1 if gam2>gp2 else -1
    else:
        return 1 if gam2<gp2 else -1

def skew_float(xs,ps):
    _,v,m3=moments(xs,ps)
    return float(m3)/(float(v)**1.5)

def g_float(p):
    p=float(p)
    return (2*p-1)/math.sqrt(p*(1-p))

def enumerate_cov_identity(xs,ps,n):
    outcomes=list(range(len(xs)))
    exbar=Fraction(0); es2=Fraction(0); exbars2=Fraction(0)
    for idxs in product(outcomes, repeat=n):
        w=Fraction(1)
        vals=[]
        for i in idxs:
            w*=ps[i]; vals.append(xs[i])
        bar=sum(vals,Fraction(0))/n
        s2=sum((x-bar)**2 for x in vals)/(n-1)
        exbar+=w*bar; es2+=w*s2; exbars2+=w*bar*s2
    cov=exbars2-exbar*es2
    _,_,m3=moments(xs,ps)
    assert cov==m3/n

def run():
    rng=random.Random(20261002)
    bound_checks=0
    boundary_checks=0
    two_point_checks=0
    covariance_checks=0
    sign_checks=0

    for _ in range(30000):
        m=rng.randrange(3,9)
        ps=normalize([rng.randrange(1,30) for __ in range(m)])
        xs=[]
        cur=Fraction(0)
        for i in range(m):
            if i:
                cur += Fraction(rng.randrange(1,20), rng.randrange(1,9))
            xs.append(cur)
        _,v,m3=moments(xs,ps)
        assert v>0
        assert compare_gamma_to_g(m3,v,ps[0])>0
        assert compare_gamma_to_g(m3,v,1-ps[-1])<0
        bound_checks+=2

        # Sign classification.
        gamma_sign=0 if m3==0 else (1 if m3>0 else -1)
        if ps[0]>=Fraction(1,2):
            assert gamma_sign>0
        if ps[-1]>=Fraction(1,2):
            assert gamma_sign<0
        sign_checks+=1

        # Boundary approach: strict supports with epsilon=1/M.
        M=100000
        eps=Fraction(1,M)
        lower=[Fraction(0)] + [Fraction(1)+(i-1)*eps for i in range(1,m)]
        upper=[i*eps for i in range(m-1)] + [Fraction(1)]
        gl=skew_float(lower,ps)
        gu=skew_float(upper,ps)
        assert abs(gl-g_float(ps[0])) < 0.01
        assert abs(gu-g_float(1-ps[-1])) < 0.01
        boundary_checks+=2

    # Exact two-point cases.
    for den in range(2,101):
        for a in range(1,den):
            p=Fraction(a,den)
            ps=[p,1-p]
            xs=[Fraction(-7,3),Fraction(11,5)]
            _,v,m3=moments(xs,ps)
            assert compare_gamma_to_g(m3,v,p)==0
            two_point_checks+=1

    # Exact sample covariance identity on small rational examples.
    examples=[
        ([Fraction(0),Fraction(1),Fraction(3)],[Fraction(1,5),Fraction(2,5),Fraction(2,5)]),
        ([Fraction(-2),Fraction(1),Fraction(4)],[Fraction(1,4),Fraction(1,2),Fraction(1,4)]),
        ([Fraction(0),Fraction(2),Fraction(5),Fraction(9)],[Fraction(1,10),Fraction(2,10),Fraction(3,10),Fraction(4,10)])
    ]
    for xs,ps in examples:
        for n in (2,3,4):
            enumerate_cov_identity(xs,ps,n)
            covariance_checks+=1

    print(
        "VERIFY_OK "
        f"bound_checks={bound_checks} "
        f"boundary_checks={boundary_checks} "
        f"two_point_checks={two_point_checks} "
        f"covariance_checks={covariance_checks} "
        f"sign_checks={sign_checks}"
    )

if __name__=="__main__":
    run()
