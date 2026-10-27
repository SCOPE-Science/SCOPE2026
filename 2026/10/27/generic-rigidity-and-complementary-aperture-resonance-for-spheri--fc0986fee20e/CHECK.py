#!/usr/bin/env python3
"""Standalone finite numerical checks of spherical-cap aperture-mixing formulae.
Not a proof of infinite-dimensional spectral positivity or originality.
"""
import math
from scipy.integrate import quad
from scipy.special import eval_gegenbauer, gammaln

def kappa(d):
    return math.exp(math.lgamma((d+1)/2)-0.5*math.log(math.pi)-math.lgamma(d/2))

def cap_vol(d,r):
    return kappa(d)*quad(lambda z:math.sin(z)**(d-1),0,r,epsabs=2e-13,epsrel=2e-13)[0]

def multiplier_exact(d,l,r):
    if l==0:return cap_vol(d,r)
    lam=(d-1)/2
    cn1=math.exp(math.lgamma(l+2*lam)-math.lgamma(l+1)-math.lgamma(2*lam))
    return kappa(d)*(2*lam)/(l*(l+2*lam))*math.sin(r)**(2*lam+1)*eval_gegenbauer(l-1,lam+1,math.cos(r))/cn1

def multiplier_integral(d,l,r):
    lam=(d-1)/2
    cn1=math.exp(math.lgamma(l+2*lam)-math.lgamma(l+1)-math.lgamma(2*lam))
    return kappa(d)*quad(lambda z:math.sin(z)**(d-1)*eval_gegenbauer(l,lam,math.cos(z))/cn1,0,r,epsabs=3e-12,epsrel=3e-12,limit=500)[0]

def amplitude(d,r):
    lam=(d-1)/2
    return kappa(d)*2**(1-lam)*math.exp(math.lgamma(2*lam)-math.lgamma(lam))*math.sin(r)**lam

def multiplier_darboux(d,l,r):
    lam=(d-1)/2
    return amplitude(d,r)*l**(-lam-1)*math.cos((l+lam)*r-(lam+1)*math.pi/2)

def check():
    comparisons=0; biggest=0.
    for d in (2,3,4,5):
        for r in (.46,.93,1.51,2.19):
            for l in (1,2,3,5,9,15,25,39):
                x=multiplier_exact(d,l,r)
                y=multiplier_integral(d,l,r)
                biggest=max(biggest,abs(x-y)); comparisons+=1
                assert abs(x-y)<2e-11,(d,l,r,x,y)
    print(f'CAP_INTEGRAL_IDENTITY {comparisons} comparisons max_absolute_error {biggest:.5g}')
    comp=0;biggest=0.
    for d in (2,3,4,5,6):
        for r in (.4,math.pi/3,1.81):
            for l in range(1,71):
                x=multiplier_exact(d,l,math.pi-r)
                y=(-1)**(l+1)*multiplier_exact(d,l,r)
                biggest=max(biggest,abs(x-y)); comp+=1
                assert abs(x-y)<5e-10,(d,l,r,x,y)
    print(f'ANTIPODAL_COMPLEMENT_IDENTITY {comp} comparisons max_absolute_error {biggest:.5g}')
    for d in (2,3,4):
        r=math.pi*math.sqrt(2)/5
        s=math.pi*math.sqrt(3)/5
        negative=[];positive=[]
        for l in range(1,150):
            u,v=multiplier_exact(d,l,r),multiplier_exact(d,l,s)
            q=u*u+3*u*v+v*v
            (negative if q<-1e-14 else positive).append(l)
        assert negative and positive
        q0=cap_vol(d,r)**2+3*cap_vol(d,r)*cap_vol(d,s)+cap_vol(d,s)**2
        assert q0>0
        print(f'INDEPENDENT_RADII d={d} Q0={q0:.9g} first_negative_degree={negative[0]} first_150_negative_count={len(negative)}')
    for d in (2,3,4,5):
        r=math.pi/3;s=math.pi-r
        v=cap_vol(d,r)
        vs=cap_vol(d,s)
        assert abs(v+vs-1)<1e-12
        # The indefinite mixing matrix diag(-1,2) is accepted on complementary caps.
        e0=-v*v+2*vs*vs
        assert e0>0
        for l in range(1,100):
            ur=multiplier_exact(d,l,r)
            us=multiplier_exact(d,l,s)
            assert abs((-ur*ur+2*us*us)-ur*ur)<5e-11
        print(f'COMPLEMENTARY_NEGATIVE_WEIGHT d={d} Q0={e0:.9g} coefficients_nonnegative=verified_first_99')
    for d in (2,3,4):
        r=.83
        errors=[]
        for l in (200,400,800):
            ex=multiplier_exact(d,l,r)
            ap=multiplier_darboux(d,l,r)
            errors.append(abs(ex-ap)*l**((d+3)/2))
        print(f'DARBOUX_ASYMPTOTIC d={d} scaled_remainders={errors}')
    print('FINITE_NUMERICAL_CHECKS_PASS; asymptotic theorem uses classical Darboux proof not these tests.')
if __name__=='__main__':check()
