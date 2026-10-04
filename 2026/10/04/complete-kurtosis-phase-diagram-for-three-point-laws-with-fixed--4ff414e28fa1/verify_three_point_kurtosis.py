#!/usr/bin/env python3
from fractions import Fraction
import random

def kurtosis(a,b,c,t):
    mu=b*t+c
    xs=(Fraction(0),t,Fraction(1))
    ps=(a,b,c)
    ys=[x-mu for x in xs]
    v=sum(p*y*y for p,y in zip(ps,ys))
    m3=sum(p*y**3 for p,y in zip(ps,ys))
    m4=sum(p*y**4 for p,y in zip(ps,ys))
    return mu,v,m3,m4,m4/(v*v)

def derivative_direct(a,b,c,t):
    mu,v,m3,m4,k=kurtosis(a,b,c,t)
    dV=2*b*(t-mu)
    dM4=4*b*((t-mu)**3-m3)
    return (dM4*v-2*m4*dV)/(v**3)

def derivative_factored(a,b,c,t):
    mu,v,m3,m4,k=kurtosis(a,b,c,t)
    return 4*a*b*c*t*(1-t)*((3*b-1)*t+(3*c-1))/(v**3)

def h(u):
    return 1/(u*(1-u))-3

def tstar(a,b,c):
    return (1-3*c)/(3*b-1)

def kstar(a,b,c):
    s2=a*b+b*c+c*a
    s3=a*b*c
    return (1-3*s2)/(s2-9*s3)

def run():
    rng=random.Random(20261002)
    derivative_checks=0
    boundary_checks=0
    uniform_checks=0
    stationary_checks=0
    phase_checks=0
    monotone_checks=0

    for _ in range(30000):
        raw=[rng.randrange(1,50) for __ in range(3)]
        s=sum(raw)
        a,b,c=[Fraction(x,s) for x in raw]
        t=Fraction(rng.randrange(1,999),1000)

        assert derivative_direct(a,b,c,t)==derivative_factored(a,b,c,t)
        derivative_checks+=1

        assert kurtosis(a,b,c,Fraction(0))[-1]==h(c)
        assert kurtosis(a,b,c,Fraction(1))[-1]==h(a)
        boundary_checks+=2

        if a==b==c:
            assert kurtosis(a,b,c,t)[-1]==Fraction(3,2)
            uniform_checks+=1
            continue

        has_stationary=(
            (a<Fraction(1,3) and c<Fraction(1,3)) or
            (a>Fraction(1,3) and c>Fraction(1,3))
        )

        if has_stationary:
            ts=tstar(a,b,c)
            assert 0<ts<1
            ks=kurtosis(a,b,c,ts)[-1]
            assert ks==kstar(a,b,c)
            stationary_checks+=2

            left=ts/2
            right=(1+ts)/2
            dl=derivative_factored(a,b,c,left)
            dr=derivative_factored(a,b,c,right)

            if a<Fraction(1,3):
                assert dl<0 and dr>0
                assert ks<h(a) and ks<h(c)
            else:
                assert dl>0 and dr<0
                assert ks>h(a) and ks>h(c)
            phase_checks+=1
        else:
            vals=[derivative_factored(a,b,c,Fraction(j,20)) for j in range(1,20)]
            nonzero=[z for z in vals if z]
            assert all(z>0 for z in nonzero) or all(z<0 for z in nonzero)
            monotone_checks+=1

    # Exhaustive small rational profiles.
    for den in range(3,45):
        for ia in range(1,den-1):
            for ib in range(1,den-ia):
                ic=den-ia-ib
                if ic<=0:
                    continue
                a=Fraction(ia,den); b=Fraction(ib,den); c=Fraction(ic,den)
                if a==b==c:
                    for t in (Fraction(1,7),Fraction(2,5),Fraction(6,7)):
                        assert kurtosis(a,b,c,t)[-1]==Fraction(3,2)
                        uniform_checks+=1
                has=(
                    (a<Fraction(1,3) and c<Fraction(1,3)) or
                    (a>Fraction(1,3) and c>Fraction(1,3))
                )
                if has:
                    ts=tstar(a,b,c)
                    assert 0<ts<1
                    assert kurtosis(a,b,c,ts)[-1]==kstar(a,b,c)
                    stationary_checks+=1

    print(
        "VERIFY_OK "
        f"derivative_checks={derivative_checks} "
        f"boundary_checks={boundary_checks} "
        f"uniform_checks={uniform_checks} "
        f"stationary_checks={stationary_checks} "
        f"phase_checks={phase_checks} "
        f"monotone_checks={monotone_checks}"
    )

if __name__=="__main__":
    run()
