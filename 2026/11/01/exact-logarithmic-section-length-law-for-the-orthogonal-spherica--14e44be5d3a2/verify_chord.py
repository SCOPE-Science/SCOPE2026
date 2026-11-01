#!/usr/bin/env python3
"""Independent reproducibility checks for the right spherical lune's random great-circle section length."""
import math
import random

PI = math.pi

def cdf(theta):
    if theta <= 0: return 0.0
    if theta >= PI: return 1.0
    if abs(theta-PI/2) < 1e-15: return 0.5
    return (theta + math.cos(theta) / math.sin(theta) * math.log(abs(math.cos(theta)))) / PI

def density(theta):
    if theta <= 0 or theta >= PI: return 1.0/(2*PI)
    if theta == PI/2: return math.inf
    return -math.log(abs(math.cos(theta))) / (PI*math.sin(theta)**2)

def chord_from_normal(a,b,c):
    if abs(c) < 1e-15: raise ValueError('measure-zero degenerate normal')
    # The two endpoints each have positive x or y and the opposite coordinate 0.
    d1=math.hypot(a,c); d2=math.hypot(b,c)
    s=1 if c>0 else -1
    p=(s*c/d1,0.0,-s*a/d1)
    q=(0.0,s*c/d2,-s*b/d2)
    assert p[0]>0 and q[1]>0
    dot=sum(x*y for x,y in zip(p,q))
    chord=math.acos(max(-1.0,min(1.0,dot)))
    return chord,p,q

def composite_simpson(f,a,b,m=10000):
    if m%2: raise ValueError('even subdivisions required')
    h=(b-a)/m
    return h/3*(f(a)+f(b)+4*sum(f(a+(2*k+1)*h) for k in range(m//2)) +2*sum(f(a+2*k*h) for k in range(1,m//2)))

def independent_circle_length(n, steps=16384):
    a,b,c=n
    # Independent basis for the plane normal to n.
    if abs(c) < .85: axis=(0.0,0.0,1.0)
    else: axis=(0.0,1.0,0.0)
    cross=(b*axis[2]-c*axis[1],c*axis[0]-a*axis[2],a*axis[1]-b*axis[0])
    norm=math.sqrt(sum(z*z for z in cross))
    u=tuple(z/norm for z in cross)
    v=(b*u[2]-c*u[1],c*u[0]-a*u[2],a*u[1]-b*u[0])
    inside=0
    for j in range(steps):
        t=2*PI*(j+.5)/steps
        x=u[0]*math.cos(t)+v[0]*math.sin(t)
        y=u[1]*math.cos(t)+v[1]*math.sin(t)
        inside += x>=0 and y>=0
    return 2*PI*inside/steps

def run():
    # Closed CDF equals the independent one-dimensional integral obtained
    # from uniform latitude and uniform azimuth of the great-circle normal.
    for theta in [.015,.1,.25,.5,.8,1.0,1.25,1.48]:
        k=math.tan(theta)
        integ=composite_simpson(lambda u: math.atan(k*u)/PI,0.,1.,20000)
        assert abs(integ-cdf(theta)) < 1e-12,(theta,integ,cdf(theta))
        eps=2e-5
        numerical=(cdf(theta+eps)-cdf(theta-eps))/(2*eps)
        assert abs(numerical-density(theta)) < 2e-7,(theta,numerical,density(theta))
    for theta in [.015,.2,.5,1.2,1.45,1.65,2.3,3.0]:
        assert abs(cdf(theta)+cdf(PI-theta)-1)<1e-13
        assert abs(density(theta)-density(PI-theta))<1e-13
    assert abs(cdf(PI/2)-.5)<1e-15
    assert density(.001)>0 and density(PI/2-.00001)>density(.01)
    rng=random.Random(20261031)
    # Circle-geometry test against a separate angular-parameter clipping algorithm.
    for j in range(120):
        n=[rng.gauss(0,1) for _ in range(3)]
        z=math.sqrt(sum(x*x for x in n));n=[x/z for x in n]
        l,p,q=chord_from_normal(*n)
        l_ind=independent_circle_length(n,steps=8192)
        assert abs(l-l_ind)<2*PI/8192+2e-12,(n,l,l_ind)
        midpoint=tuple((x+y) /math.sqrt(2+2*sum(a*b for a,b in zip(p,q))) for x,y in zip(p,q))
        assert midpoint[0]>=0 and midpoint[1]>=0
    # Sampling uniform plane normals with a separate Gaussian generator.
    nsamp=240000
    sample=[0]*nsamp
    for j in range(nsamp):
        a,b,c=(rng.gauss(0,1) for _ in range(3))
        sample[j]=chord_from_normal(a,b,c)[0]
    for theta in [.08,.25,.5,.8,1.1,1.3,1.55,1.9,2.4,2.9,3.06]:
        emp=sum(x<=theta for x in sample)/nsamp
        theo=cdf(theta)
        assert abs(emp-theo)<0.006,(theta,emp,theo)
    mean=sum(sample)/nsamp
    assert abs(mean-PI/2)<.006
    # Density has a logarithmic peak, symmetric end-tails and no point mass.
    for h in [.05,.01,.002]:
        mass=cdf(PI/2+h)-cdf(PI/2-h)
        approx=2*h*(1-math.log(h))/PI
        assert abs(mass-approx)<.002,(h,mass,approx)
    print('ALL_RIGHT_LUNE_SECTION_LAW_CHECKS_PASSED')
    print('sample_size',nsamp,'sample_mean',f'{mean:.8f}','exact_mean',f'{PI/2:.8f}')
    print('cdf_quarter',f'{cdf(PI/4):.12f}','cdf_half',cdf(PI/2))
if __name__=='__main__':run()
