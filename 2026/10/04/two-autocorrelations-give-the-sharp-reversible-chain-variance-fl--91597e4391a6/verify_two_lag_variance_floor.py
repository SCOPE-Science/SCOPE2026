#!/usr/bin/env python3
from fractions import Fraction
import random

def spectral_stats(points, weights):
    r=sum(w*x for x,w in zip(points,weights))
    s=sum(w*x*x for x,w in zip(points,weights))
    tau=sum(w*(1+x)/(1-x) for x,w in zip(points,weights))
    return r,s,tau

def matvec(P,v):
    return [sum(a*b for a,b in zip(row,v)) for row in P]

def equality_parameters(r,s):
    q=(r+s)/(1+r)
    alpha=(1+r)*(1+r)/(1+2*r+s)
    return q,alpha

def run():
    rng=random.Random(20261002)
    generic_checks=0
    equality_checks=0
    matrix_checks=0
    lazy_checks=0
    one_lag_checks=0

    # Generic exact Cauchy--Schwarz checks on rational finite spectra.
    grid=[Fraction(k,10) for k in range(-9,10)]
    for _ in range(20000):
        m=rng.randrange(2,7)
        pts=[rng.choice(grid) for __ in range(m)]
        raw=[rng.randrange(1,20) for __ in range(m)]
        total=sum(raw)
        ws=[Fraction(x,total) for x in raw]
        r,s,tau=spectral_stats(pts,ws)
        assert tau*(1-s) >= (1+r)*(1+r)
        if s<1:
            assert (1+r)*(1+r)/(1-s) >= (1+r)/(1-r)
            one_lag_checks+=1
        generic_checks+=1

    # Equality spectra and explicit four-state matrix.
    qs=[Fraction(k,20) for k in range(-17,18)]
    alphas=[Fraction(k,20) for k in range(1,20)]
    for _ in range(12000):
        q=rng.choice(qs)
        alpha=rng.choice(alphas)
        r=-(1-alpha)+alpha*q
        s=(1-alpha)+alpha*q*q
        tau=alpha*(1+q)/(1-q)
        bound=(1+r)*(1+r)/(1-s)
        assert tau==bound
        q2,a2=equality_parameters(r,s)
        assert q2==q and a2==alpha
        equality_checks+=3

        theta=(1+q)/2
        P=[
            [0,0,theta,1-theta],
            [0,0,1-theta,theta],
            [theta,1-theta,0,0],
            [1-theta,theta,0,0],
        ]
        assert all(sum(row)==1 for row in P)
        uminus=[1,1,-1,-1]
        uq=[1,-1,1,-1]
        assert matvec(P,uminus)==[-x for x in uminus]
        assert matvec(P,uq)==[q*x for x in uq]
        matrix_checks+=4

        # Exact-moment aperiodic lazy approximation.
        eta=Fraction(1,10**6)
        r0=(r-eta)/(1-eta)
        s0=(s-2*eta*r+eta*eta)/((1-eta)*(1-eta))
        assert s0-r0*r0 == (s-r*r)/((1-eta)*(1-eta))
        q0,a0=equality_parameters(r0,s0)
        assert -1 < q0 < 1 and 0 < a0 <= 1
        u=2*eta-1
        v=eta+(1-eta)*q0
        rr=(1-a0)*u+a0*v
        ss=(1-a0)*u*u+a0*v*v
        assert rr==r and ss==s
        tau_lazy=(1-a0)*(1+u)/(1-u)+a0*(1+v)/(1-v)
        if s>r*r:
            assert tau_lazy>bound
        lazy_checks+=5

    print(
        "VERIFY_OK "
        f"generic_checks={generic_checks} "
        f"equality_checks={equality_checks} "
        f"matrix_checks={matrix_checks} "
        f"lazy_checks={lazy_checks} "
        f"one_lag_checks={one_lag_checks}"
    )

if __name__=="__main__":
    run()
