"""Reproducibility checks for symmetrically truncated cross-polytopes.

The theorem is proved analytically; finite checks here are auxiliary only.
Run with Python 3, numpy, and scipy: python verification.py
"""
from math import sqrt, log, exp, isclose
from scipy.optimize import minimize, brentq
import numpy as np


def values(d,t):
    m=d-1
    t0=1-sqrt(m/d); t1=1/sqrt(d)
    if t<=t1:
        A=t; B=sqrt((1-t*t)/m)
    else:
        A=B=1/sqrt(d)
    if t<=t0:
        U=sqrt(d)*t; V=sqrt(d/m)*(1-t)
    else:
        U=sqrt(t/(2-t)); V=1.0
    return A,B,U,V,t0,t1


def ratio(d,t):
    A,B,U,V,_,_=values(d,t)
    return (U/A)*(V/B)**(d-1)


def optimum(d):
    m=d-1
    t0=1-sqrt(m/d); t1=1/sqrt(d)
    return brentq(lambda t:m*t*t*(2-t)-(1-t)**2*(1+t),t0,t1)


def check(d,t):
    m=d-1
    A,B,U,V,t0,t1=values(d,t)
    # Containment in the coordinate slab and the cross-polytope.
    assert A<=t+1e-12
    assert A*A+m*B*B<=1+1e-12
    # Every extreme point of the clipped cross-polytope is contained.
    assert 1/V**2 <=1+1e-12
    assert t*t/(U*U)+(1-t)**2/(V*V)<=1+1e-12
    # Normalized contact measures (mean zero by sign symmetries).
    mixed_mass=1 if t<t0 else 1/(d*t*(2-t))
    if t<t0:
        assert isclose(t*t/(U*U),1/d,rel_tol=1e-9,abs_tol=1e-9)
    else:
        assert 0<mixed_mass<=1+1e-10
    outer_ax=mixed_mass*t*t/(U*U)
    outer_tr=(mixed_mass*(1-t)**2+(1-mixed_mass))/(m*V*V)
    assert abs(outer_ax-1/d)<2e-10
    assert abs(outer_tr-1/d)<2e-10
    facet_mass=min(1., m/(d*(1-t*t))) if t<1 else 1.
    if t>=t1: facet_mass=1.
    inner_ax=facet_mass*A*A+(1-facet_mass)
    inner_tr=facet_mass*B*B
    assert abs(inner_ax-1/d)<2e-10
    assert abs(inner_tr-1/d)<2e-10
    # Direct strictly-concave 2-variable optimizations; not substitutes for proof.
    xin=np.log([A,B])*1.03
    def inside_obj(logs):return -(logs[0]+m*logs[1])
    def cin(logs):
        a,b=np.exp(logs)
        return np.array([t-a,1-a*a-m*b*b])
    sol=minimize(inside_obj,np.log([A,B]),method='SLSQP',bounds=[(-30,1),(-30,1)],constraints=[{'type':'ineq','fun':cin}],options={'ftol':1e-12,'maxiter':300})
    assert sol.success or np.linalg.norm(sol.x-np.log([A,B]))<1e-7, (d,t,sol.message)
    assert np.max(np.abs(np.exp(sol.x)-[A,B]))<3e-5, (d,t,sol.x)
    def outside_obj(logs):return -(logs[0]+m*logs[1])
    def cout(logs):
        al,be=np.exp(logs)
        return np.array([1-t*t*al-(1-t)**2*be,1-be])
    # logs are logarithms of precision values, maximum determinant => min ellipsoid volume
    sol=minimize(outside_obj,np.log([1/U**2,1/V**2]),method='SLSQP',bounds=[(-30,30),(-30,30)],constraints=[{'type':'ineq','fun':cout}],options={'ftol':1e-12,'maxiter':300})
    assert sol.success or np.linalg.norm(sol.x-np.log([1/U**2,1/V**2]))<1e-7, (d,t,sol.message)
    assert np.max(np.abs(np.exp(sol.x)-[1/U**2,1/V**2]))<3e-5, (d,t,sol.x)
    return max(np.max(np.abs(np.exp(sol.x)-[1/U**2,1/V**2])),abs(inner_ax-1/d),abs(outer_ax-1/d))


if __name__=='__main__':
    max_err=0; n=0
    for d in (2,3,4,5,7,10,16,30):
        t0=1-sqrt((d-1)/d); t1=1/sqrt(d)
        for t in sorted(set([1e-3,0.02,0.1,0.4,0.7,0.99,1.,t0,t1,(t0+t1)/2,optimum(d)])):
            if t>0:
                max_err=max(max_err,check(d,t));n+=1
        tm=optimum(d)
        left=ratio(d,max(1e-5,tm-1e-4));middle=ratio(d,tm);right=ratio(d,min(1.,tm+1e-4))
        assert left>middle and right>middle
        assert ratio(d,tm)<d**(d/2)
        print(f'd={d:3d} threshold_outer={t0:.12f} optimum={tm:.12f} threshold_inner={t1:.12f} minimum_ratio={middle:.12g}')
    # Exact rational check d=3, t=2/5: R=125/42.
    assert abs(ratio(3,2/5)-125/42)<1e-12
    # Asymptotic constant: d^(1/4) * Rmin / d^(d/2) -> (2e)^(-1/4).
    for d in (100,1000,10000):
        tm=optimum(d)
        m=d-1
        A,B,U,V,_,_=values(d,tm)
        scaled=exp(.25*log(d)+log(U)+m*log(V)-log(A)-m*log(B)-d/2*log(d))
        print(f'd={d:5d} scaled minimum={scaled:.10f} target={(2*np.e)**(-.25):.10f}')
    print(f'PASS: {n} configurations; max independent-optimality/certificate residual {max_err:.3e}')
