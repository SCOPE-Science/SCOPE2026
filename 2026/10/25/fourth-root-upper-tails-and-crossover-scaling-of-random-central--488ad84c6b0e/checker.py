#!/usr/bin/env python3
"""Numerical checks for finite-cylinder central-section upper-tail scaling.
This is numerical corroboration, not an exhaustive or symbolic proof.
Standard Python library only. Run: python3 checker.py
"""
import math

SQ3=math.sqrt(3)
ALPHA=2/SQ3
BETA=12*SQ3/5

def area_from_x(k,x):
    if x==0:
        return 4*k
    return 2*math.hypot(k,x)*(math.asin(x)/x+math.sqrt(max(0,1-x*x)))

def normal_cosine(k,x):
    return x/math.hypot(k,x)

def area_from_normal(k,c):
    if c==0:
        return 4*k
    if c==1:
        return math.pi
    x=k*c/math.sqrt(1-c*c)
    return math.pi/c if x>=1 else area_from_x(k,x)

def geometric_quadrature(k,c,n=800):
    if c==0:
        return 4*k
    if c==1:
        return math.pi
    a=min(1,k*c/math.sqrt(1-c*c))
    phi=math.asin(a)
    # Independent planar slice integral: (4/c) integral cos^2(theta)dtheta.
    step=phi/n
    s=math.cos(0)**2+math.cos(phi)**2
    for j in range(1,n):
        s+=(4 if j%2 else 2)*math.cos(j*step)**2
    return 4*step*s/(3*c)

def threshold_function(x):
    if x==0:
        return 3.
    if x < .45:
        # Stable convergent binomial expansion of 2 int_0^1 t^2/sqrt(1-x^2 t^2) dt.
        z=x*x; pw=1.; acc=0.
        for j in range(24):
            acc += 2*math.comb(2*j,j)/(4**j*(2*j+3))*pw
            pw*=z
        return 2*math.sqrt(1-z)/acc
    t=math.sqrt(1-x*x)
    return 2*x**3*t/(math.asin(x)-x*t)

def optimum(k):
    if k>=SQ3:
        return 0.,4*k
    lo=0.;hi=1.
    for _ in range(80):
        mid=(lo+hi)/2
        if threshold_function(mid)>k*k:
            lo=mid
        else:
            hi=mid
    x=(lo+hi)/2
    return x,area_from_x(k,x)

def near_max_prob(k,eps):
    xm,m=optimum(k)
    target=m-eps
    # For small epsilon relevant roots remain in truncated-ellipse regime.
    assert target>area_from_x(k,1.),(k,eps,target)
    if xm==0 or area_from_x(k,0)>=target:
        left=0.
    else:
        lo=0.;hi=xm
        for _ in range(72):
            mid=(lo+hi)/2
            if area_from_x(k,mid)<target:
                lo=mid
            else:
                hi=mid
        left=normal_cosine(k,(lo+hi)/2)
    lo=xm;hi=1.
    for _ in range(72):
        mid=(lo+hi)/2
        if area_from_x(k,mid)>=target:
            lo=mid
        else:
            hi=mid
    right=normal_cosine(k,(lo+hi)/2)
    return right-left

def crossover(tau):
    a=ALPHA*tau
    if tau<=0:
        return math.sqrt((a+math.sqrt(a*a+4*BETA))/(2*BETA))
    t0=a/(2*BETA)
    s=BETA**(-.5)
    return math.sqrt(t0+s)-math.sqrt(max(0,t0-s))

# Direct area calculation using planar section coordinates, checked over both regimes.
checks=0
for k in (.55,1,1.69,SQ3,2.2,4.):
    for j in range(1,101):
        c=j/101
        lhs=area_from_normal(k,c)
        rhs=geometric_quadrature(k,c,600)
        assert math.isclose(lhs,rhs,rel_tol=2e-10,abs_tol=2e-10),(k,c,lhs,rhs)
        checks+=1
print('INDEPENDENT_CYLINDER_CENTRAL_SECTION_QUADRATURE_OK',checks)

for k in (.8,1.5,1.72,SQ3,1.75,2.5):
    x,m=optimum(k)
    vals=[area_from_x(k,j/3000) for j in range(3001)]
    assert m+1e-10>=max(vals)
    if k<SQ3:
        assert x>0 and abs(threshold_function(x)-k*k)<3e-11
    else:
        assert x==0 and m==4*k
print('GLOBAL_MAXIMUM_AND_CRITICAL_NORMALIZATION_OK')

# Critical quartic flatness, second-order emergence of optimizer and area gain.
for c in (.002,.004,.006):
    deficit=4*SQ3-area_from_normal(SQ3,c)
    assert abs(deficit/(BETA*c**4)-1)<.004,(c,deficit)
for delta in (.01,.005,.002):
    k=math.sqrt(3-delta)
    x,m=optimum(k)
    c=normal_cosine(k,x)
    assert abs((c*c/delta)/(5/36)-1)<.02
    assert abs(((m-4*k)/delta**2)/(5/(36*SQ3))-1)<.025
print('QUARTIC_DEGENERACY_AND_QUADRATIC_MAXIMUM_GAIN_OK')

for eps in (1e-4,2e-5):
    p=near_max_prob(SQ3,eps)
    theory=BETA**(-.25)*eps**.25
    assert abs(p/theory-1)<.016,(eps,p,theory)
print('SHARP_FOURTH_ROOT_CRITICAL_TAIL_OK')

for tau in (-4,-1,0,1,4):
    for eps in (1e-4,2e-5):
        k=math.sqrt(3-tau*math.sqrt(eps))
        p=near_max_prob(k,eps)
        scaled=p/eps**.25
        exact=crossover(tau)
        assert abs(scaled/exact-1)<.027,(tau,eps,scaled,exact)
print('FIVE_PARAMETER_VALUES_AND_TWO_SCALES_CROSSOVER_OK')
print('ALL_CYLINDER_SECTION_CRITICAL_TAIL_CHECKS_OK')
