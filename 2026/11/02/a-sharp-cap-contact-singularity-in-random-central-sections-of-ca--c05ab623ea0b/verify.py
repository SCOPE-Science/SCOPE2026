#!/usr/bin/env python3
"""Numerical cross-checks for centered capsule sections; standard library only."""
import math

PI=math.pi

def profile(theta,a,r):
    s=math.sin(theta); c=math.cos(theta)
    if theta<=math.atan(a/r):
        return PI*r*r/c
    x0=a/s; q=math.sqrt(max(0.0,r*r-a*a*c*c))
    # Primitive for circular root integral, with clamp for roundoff.
    def root_primitive(x,R):
        z=max(-1.0,min(1.0,x/R))
        return 0.5*(x*math.sqrt(max(0.0,R*R-x*x))+R*R*math.asin(z))
    side=0.5*x0*math.sqrt(max(0.0,r*r-c*c*x0*x0)) +r*r*math.asin(min(1.0,c*x0/r))/(2*c) if c>1e-12 else r*x0
    cap=root_primitive(q,q)-root_primitive(x0-a*s,q)
    return 4*(side+cap)

def area_by_direct_slice(theta,a,r,n=10000):
    # Independently integrate the point-to-segment distance inequality.
    s=math.sin(theta); c=math.cos(theta)
    boundary=r/c if theta<=math.atan(a/r) else a*s+math.sqrt(r*r-a*a*c*c)
    def integrand(t):
        x=boundary*(1-t*t)
        d2=c*c*x*x + max(s*x-a,0)**2
        return 8*boundary*t*math.sqrt(max(0,r*r-d2))
    h=1/n
    v=integrand(0)+integrand(1)
    for j in range(1,n): v+=(4 if j%2 else 2)*integrand(j*h)
    return v*h/3

def run():
    errors=[]
    for a,r in [(0.2,1.0),(1.0,1.0),(3.0,0.7)]:
        critical=math.atan(a/r)
        for t in [0,critical*0.5,critical*0.99,critical*1.01,0.5*(critical+PI/2),PI/2]:
            v=profile(t,a,r); w=area_by_direct_slice(t,a,r)
            error=abs(v-w)/max(1.0,v)
            errors.append(error)
            assert error<2e-6,(a,r,t,v,w,error)
        assert abs(profile(0,a,r)-PI*r*r)<1e-12
        assert abs(profile(PI/2,a,r)-(PI*r*r+4*a*r))<1e-11
        # A(theta) strictly increases as the plane tilts towards the axis.
        sampled=[profile(i*PI/2000,a,r) for i in range(1001)]
        assert all(y>x for x,y in zip(sampled,sampled[1:]))
        # Low-area law: P(A<=z) = 1 - pi*r^2/z on its exact range.
        cut=PI*r*math.hypot(a,r)
        for q in (0.05,0.3,0.7,0.95):
            z=(1-q)*PI*r*r+q*cut
            theta=math.acos(PI*r*r/z)
            assert abs(profile(theta,a,r)-z)<1e-11
            assert theta<=critical+1e-12
        # The leading one-sided 5/2 singularity coefficient.
        L=math.hypot(a,r)
        k=(16*math.sqrt(2)/15)*L**6/(math.sqrt(a)*r**3.5)
        for h in (0.0001,0.00005):
            if critical+h >=PI/2: continue
            delta=PI*r*r/math.cos(critical+h)-profile(critical+h,a,r)
            ratio=delta/(k*h**2.5)
            assert abs(ratio-1)<0.015,(a,r,h,ratio)
        B=2*a**3/(3*r)+PI*a*a+2*a*r
        c=0.008
        deficit=PI*r*r+4*a*r-profile(math.acos(c),a,r)
        assert abs(deficit/(B*c*c)-1)<0.005,(a,r,deficit/(B*c*c))
    print('PASS: 18 independently quadrature-evaluated sections; max relative area discrepancy',format(max(errors),'.3g'))
    print('PASS: strict sampled monotonicity, reciprocal CDF branch, endpoint asymptotics, 5/2 contact law')

if __name__=='__main__':run()
