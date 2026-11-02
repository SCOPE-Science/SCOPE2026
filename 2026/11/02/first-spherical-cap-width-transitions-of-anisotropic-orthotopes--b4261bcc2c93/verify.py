#!/usr/bin/env python3
"""Reproducible numerical checks for the first width-tail transition of orthotopes.

Requires Python 3, NumPy and SciPy. Numerical experiments complement an analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import betainc, ndtri
from scipy.stats import qmc


def cap_tail(d, lengths, t):
    radius = float(np.linalg.norm(lengths))
    q = 1 - (t / radius)**2
    if q <= 0:
        return 0.0
    return (2**(d-1))*float(betainc((d-1)/2, .5, q))


def first_threshold(lengths):
    a = np.array(lengths, dtype=float)
    m = float(a.min())
    k = int(np.count_nonzero(a == m))
    return math.sqrt(float(np.dot(a,a))-m*m),m,k


def leading_coefficient(lengths):
    d=len(lengths)
    t0,m,k=first_threshold(lengths)
    return 2**d*k/(d*math.pi*m)*(2/t0)**((d-2)/2)


def single_facet_protrusion(d, lengths, t):
    """Exact cap leakage through a particular minimum-edge coordinate facet.

    Valid while t is slightly below first_threshold; other facet intersections
    are irrelevant to this single-facet integral.
    """
    L=float(np.linalg.norm(lengths))
    t0,m,_=first_threshold(lengths)
    smax=(-t*m+t0*math.sqrt(max(0,L*L-t*t)))/(L*L)
    if smax<=0: return 0.0
    from scipy.special import gamma
    cd=float(gamma(d/2)/(math.sqrt(math.pi)*gamma((d-1)/2)))
    def integrand(s):
        z=(t+m*s)/(t0*math.sqrt(1-s*s))
        zz=max(0.0,min(1.0,1-z*z))
        return cd*(1-s*s)**((d-3)/2)*0.5*float(betainc((d-2)/2,.5,zz))
    val,err=quad(integrand,0,smax,epsabs=2e-13,epsrel=2e-11,limit=180)
    return val


def d4_protrusion_closed(lengths,t):
    L=float(np.linalg.norm(lengths)); t0,m,_=first_threshold(lengths)
    s=(-t*m+t0*math.sqrt(max(0.0,L*L-t*t)))/(L*L)
    if s<=0: return 0.0
    return ((math.asin(s)+s*math.sqrt(1-s*s))/2-(t*s+m*s*s/2)/t0)/math.pi


def asymptotic_tail(d,lengths,t):
    t0,m,k=first_threshold(lengths)
    if t>=t0: return cap_tail(d,lengths,t)
    return cap_tail(d,lengths,t) - (2**d)*k*single_facet_protrusion(d,lengths,t)


def estimate_sphere_tail(lengths, points):
    a=np.asarray(lengths,dtype=float)
    return np.sum(np.abs(points)*a,axis=1)


def main():
    n=0
    for dims in (4,5,6):
        examples={4:[(1,2,3,4),(1,1,2,4),(1,1,1,1)],
                  5:[(1,2,3,4,5),(1,1,2,3,5),(1,1,1,1,1)],
                  6:[(1,2,3,4,5,6),(1,1,1,2,3,4),(1,1,1,1,1,1)]}[dims]
        for aa in examples:
            t0,m,k=first_threshold(aa); L=float(np.linalg.norm(aa))
            assert 0<t0<L
            # Independent integration in one coordinate of the sphere.
            for eps in (0.001,0.002,0.005,0.01):
                P=single_facet_protrusion(dims,aa,t0-eps)
                C=leading_coefficient(aa)
                ratio=(2**dims*k*P)/(C*eps**(dims/2))
                assert abs(ratio-1)<0.035,(dims,aa,eps,ratio)
                n+=1
            if dims==4:
                for eps in (0.01,0.03,0.06,0.08):
                    x=single_facet_protrusion(dims,aa,t0-eps)
                    y=d4_protrusion_closed(aa,t0-eps)
                    assert abs(x-y)<4e-12,(aa,eps,x,y)
                    n+=1
            # Exact cap branch and positive correction just below transition.
            assert asymptotic_tail(dims,aa,t0)==cap_tail(dims,aa,t0)
            assert asymptotic_tail(dims,aa,t0-.025)<cap_tail(dims,aa,t0-.025)
            n+=2
    # Independent integration/Monte Carlo check for four-dimensional volumes.
    sobol=qmc.Sobol(d=4,scramble=True,seed=20261031)
    u=ndtri(sobol.random_base2(20))
    u/=np.linalg.norm(u,axis=1)[:,None]
    for a in [(1,2,3,4),(1,1,2,4),(1,1,1,1)]:
        t0,_,_=first_threshold(a)
        radii=estimate_sphere_tail(a,u)
        for eps in (0.04,0.08,0.12):
            t=t0-eps
            estimate=float(np.mean(radii>=t))
            exact=asymptotic_tail(4,a,t)
            assert abs(estimate-exact)<0.002,(a,t,estimate,exact)
            n+=1
    # Two distinct four-boxes with identical maximum, shortest edge and
    # shortest-edge multiplicity have the same exact first-crossing germ.
    a=(1,2,3,4)
    b=(1,math.sqrt(5),math.sqrt(8),4)
    qa,ma,ka=first_threshold(a)
    qb,mb,kb=first_threshold(b)
    assert math.isclose(qa,qb,rel_tol=1e-14) and (ma,ka)==(mb,kb)
    assert sorted(a)!=sorted(b)
    for eps in (0.01,0.03,0.06,0.1):
        t=qa-eps
        exact_a=asymptotic_tail(4,a,t)
        exact_b=asymptotic_tail(4,b,t)
        assert abs(exact_a-exact_b)<2e-13,(eps,exact_a,exact_b)
        # Both probabilities use independent random width functions on the
        # same fixed spherical quasi-Monte-Carlo cloud.
        empirical_a=float(np.mean(estimate_sphere_tail(a,u)>=t))
        empirical_b=float(np.mean(estimate_sphere_tail(b,u)>=t))
        assert abs(empirical_a-exact_a)<0.002
        assert abs(empirical_b-exact_b)<0.002
        n+=3
    print(f'VERIFY_OK {n} independent numeric, exact integration and sphere-distribution tests')


if __name__ == '__main__':
    main()
