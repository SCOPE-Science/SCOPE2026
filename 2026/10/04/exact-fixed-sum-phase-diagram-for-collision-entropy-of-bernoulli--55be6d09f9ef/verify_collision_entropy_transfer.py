#!/usr/bin/env python3
from fractions import Fraction
import random

def conv(a,b):
    out=[Fraction(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def bern(p):
    return [1-p,p]

def autocorr(a,j):
    if j>=len(a):
        return Fraction(0)
    return sum(a[k]*a[k+j] for k in range(len(a)-j))

def coeffs(a):
    c0,c1,c2=(autocorr(a,j) for j in range(3))
    D=3*c0-4*c1+c2
    G=c0-2*c1+c2
    return c0,c1,c2,D,G

def second_diff_energy(a):
    def z(k):
        return a[k] if 0<=k<len(a) else Fraction(0)
    return sum((z(k)-2*z(k-1)+z(k-2))**2 for k in range(len(a)+2))

def collision_from_r(a,s,r):
    c0,c1,c2,D,G=coeffs(a)
    t0=1-s+r
    t1=s-2*r
    t2=r
    return c0*(t0*t0+t1*t1+t2*t2)+2*c1*(t0*t1+t1*t2)+2*c2*t0*t2

def direct_collision(a,p,q):
    w=conv(conv(a,bern(p)),bern(q))
    return sum(x*x for x in w)

def r_bounds(s):
    return max(Fraction(0),s-1), s*s/4

def r_center(a,s):
    c0,c1,c2,D,G=coeffs(a)
    return s/2-G/(2*D)

def clamp(x,lo,hi):
    return min(hi,max(lo,x))

def pair_from_sr(s,r):
    # Only used for perfect-square rational discriminants in direct checks.
    disc=s*s-4*r
    n=disc.numerator
    d=disc.denominator
    sn=int(n**0.5); sd=int(d**0.5)
    if sn*sn!=n or sd*sd!=d:
        return None
    root=Fraction(sn,sd)
    return (s-root)/2,(s+root)/2

def run():
    rng=random.Random(20261002)
    convolution_checks=0
    energy_checks=0
    quadratic_checks=0
    projection_checks=0
    two_coin_checks=0

    for _ in range(12000):
        a=[Fraction(1)]
        for __ in range(rng.randrange(0,8)):
            p=Fraction(rng.randrange(0,13),12)
            a=conv(a,bern(p))

        c0,c1,c2,D,G=coeffs(a)
        assert D>0
        assert second_diff_energy(a)==2*D
        energy_checks+=1

        p=Fraction(rng.randrange(0,13),12)
        q=Fraction(rng.randrange(0,13),12)
        s=p+q; r=p*q
        assert collision_from_r(a,s,r)==direct_collision(a,p,q)
        convolution_checks+=1

        r0=r_center(a,s)
        q0=collision_from_r(a,s,r0)
        assert collision_from_r(a,s,r)-q0==2*D*(r-r0)**2
        quadratic_checks+=1

        lo,hi=r_bounds(s)
        ropt=clamp(r0,lo,hi)
        qopt=collision_from_r(a,s,ropt)
        for j in range(21):
            rr=lo+(hi-lo)*Fraction(j,20)
            assert collision_from_r(a,s,rr)>=qopt
            projection_checks+=1

    # Two-coin exact phase classification over a rational grid.
    a=[Fraction(1)]
    for j in range(0,401):
        s=Fraction(j,200)   # 0 to 2
        u=min(s,2-s)
        lo,hi=r_bounds(s)
        r0=s/2-Fraction(1,6)
        ropt=clamp(r0,lo,hi)

        if u<=Fraction(1,3):
            assert ropt==lo
        elif 3*(1-u)*(1-u)>1:
            assert lo<ropt<hi
            assert ropt==r0
        else:
            assert ropt==hi

        qopt=collision_from_r(a,s,ropt)
        if u<=Fraction(1,3):
            expected=1-2*u+2*u*u
        elif 3*(1-u)*(1-u)>=1:
            expected=Fraction(1,3)+(1-u)*(1-u)/2
        else:
            t=u/2
            expected=(1-t)**4+4*t*t*(1-t)*(1-t)+t**4
        assert qopt==expected
        two_coin_checks+=1

    # Direct exact two-coin checks on rational pairs.
    for den in range(1,31):
        for i in range(den+1):
            for j in range(den+1):
                p=Fraction(i,den); q=Fraction(j,den)
                s=p+q; r=p*q
                assert collision_from_r([Fraction(1)],s,r)==direct_collision([Fraction(1)],p,q)
                convolution_checks+=1

    print(
        "VERIFY_OK "
        f"convolution_checks={convolution_checks} "
        f"energy_checks={energy_checks} "
        f"quadratic_checks={quadratic_checks} "
        f"projection_checks={projection_checks} "
        f"two_coin_phase_checks={two_coin_checks}"
    )

if __name__=="__main__":
    run()
