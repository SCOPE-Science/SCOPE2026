"""Numerical cross-checks for convex-order control of resetting-Brownian forcing.

Python >=3.9, standard library only. Analytic inequalities are proved in RESULT.md;
finite numerical tests here are corroboration, not infinite-parameter certificates.
"""
import math
from fractions import Fraction


def simpson(fun, a, b, n=6000):
    assert n % 2 == 0
    h = (b-a)/n
    ans = fun(a)+fun(b)
    ans += 4*sum(fun(a+i*h) for i in range(1,n,2))
    ans += 2*sum(fun(a+i*h) for i in range(2,n,2))
    return h*ans/3


def F(mu, t):
    return t*t-2*t/mu+2*(-math.expm1(-mu*t))/(mu*mu)


def v_renewal(mu, D, law):
    m=sum(p*t for p,t in law)
    return D/(mu*mu*m)*sum(p*F(mu,t) for p,t in law)


def v_periodic(mu, D, m):
    z=mu*m
    f=z*z-2*z+2*(-math.expm1(-z))
    return D*f/(mu**3*z)


def v_poisson(mu, D, m):
    r=1/m
    return 2*D/(mu*r*(mu+r))


def v_phase(mu, D, m):
    z=mu*m
    g=lambda a: 2*a-3+4*math.exp(-a)-math.exp(-2*a)
    # Positive stable near a=0 is not needed for the non-tiny test parameters.
    epoch=D/(mu**3)*g(z)/(-math.expm1(-2*z))
    return simpson(lambda t: math.exp(-2*mu*t)*epoch+D/(mu**3)*g(mu*t),0,m)/m


def cv_twopoint(s, D, law):
    m=sum(p*t for p,t in law)
    return D/m*sum(p*max(t-s,0)**2 for p,t in law)


def cv_poisson(s, D, m):
    return 2*D*m*math.exp(-s/m)


def var_from_cv(mu, cv, cutoff):
    return simpson(lambda s: math.exp(-mu*s)*cv(s)/mu,0,cutoff)


def ratio(z):
    f=z*z-2*z+2*(-math.expm1(-z))
    return 2*z**3/((1+z)*f)


def main():
    checks=0
    for mu in (0.3,0.65,1,1.7,3):
        for m in (0.4,1,1.7,2.5):
            D=1.3
            vp=v_periodic(mu,D,m)
            vr=v_renewal(mu,D,[(1.0,m)])
            assert abs(vp-vr)<1.e-10*max(1,vp)
            checks+=1
            # Independent phase average using the source's exact reset-epoch variance.
            va=v_phase(mu,D,m)
            assert abs(vp-va)<3.e-8*max(1,vp), (mu,m,vp,va)
            checks+=1
            ve=v_poisson(mu,D,m)
            # Independent Poisson Markov-generator moment relations:
            # E[Y^2]=2D/r, E[XY]=E[Y^2]/(mu+r), E[X^2]=E[XY]/mu.
            r=1/m
            emarkov=(2*D/r)/(mu+r)/mu
            assert abs(ve-emarkov)<1.e-12*max(1,ve)
            checks+=1
            assert 2<ve/vp<6
            checks+=1

    for mu in (0.45,1,2):
        D=1; m=1
        d=v_periodic(mu,D,m)
        for a in (0.05,0.15,0.3,0.5,0.8):
            for b in (1.2,1.5,2,3,8):
                p=(b-m)/(b-a)
                law=[(p,a),(1-p,b)]
                assert abs(sum(q*t for q,t in law)-m)<1e-12
                assert v_renewal(mu,D,law)>d
                checks+=1

    law=[(0.5,0.5),(0.5,1.5)]
    for mu in (0.5,1.,2.):
        a=v_renewal(mu,1,law)
        b=var_from_cv(mu,lambda s:cv_twopoint(s,1,law),1.5)
        assert abs(a-b)<2e-9, (mu,a,b)
        checks+=1
        p=v_poisson(mu,1,1)
        p2=var_from_cv(mu,lambda s:cv_poisson(s,1,1),55)
        assert abs(p-p2)<1e-8, (mu,p,p2)
        checks+=1

    # The analytic proof supplies an everywhere-positive exponential-series
    # certificate for the derivative of the Poisson/periodic ratio.
    for n in range(4,201):
        assert n*(n-1)-6>0
        checks+=1
    zs=[0.001,0.01,0.1,0.25,0.5,1,2,4,10,20,100]
    rs=[ratio(z) for z in zs]
    assert all(rs[i]>rs[i+1] for i in range(len(rs)-1))
    assert 2<rs[-1] and rs[0]<6
    checks+=len(zs)
    print(f"PASS: {checks} checks; benchmark m=mu=D=1: periodic={v_periodic(1,1,1):.12f}, Poisson={v_poisson(1,1,1):.12f}")


if __name__=='__main__':
    main()
