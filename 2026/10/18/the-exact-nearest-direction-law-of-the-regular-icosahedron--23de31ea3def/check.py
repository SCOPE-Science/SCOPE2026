"""Independent numeric checks for the icosahedral nearest-direction law.

Uses only Python's standard library. No simulation is used as a proof.
"""
from math import acos, cos, sin, tan, sqrt, pi
import random


def clamp(x):
    return max(-1.0, min(1.0, x))


def simpson(func, lo, hi, n=6000):
    assert n % 2 == 0
    h = (hi-lo)/n
    return h/3*(func(lo)+func(hi)+4*sum(func(lo+(2*i-1)*h) for i in range(1,n//2+1))
                 +2*sum(func(lo+2*i*h) for i in range(1,n//2)))

c=1/sqrt(5)
rho=acos(c)/2
R=acos(sqrt((1+2*c)/3))
ell=acos(sqrt(5)/3)
phi=(1+sqrt(5))/2
s=sqrt(1+phi*phi)
verts=[(x/s,y/s,z/s) for x,y,z in (
    [(0,a,b*phi) for a in (-1,1) for b in (-1,1)] +
    [(a,b*phi,0) for a in (-1,1) for b in (-1,1)] +
    [(a*phi,0,b) for a in (-1,1) for b in (-1,1)])]


def alpha(t):
    if t <= rho: return 0.0
    return acos(clamp(tan(rho)/tan(t)))


def f(t):
    if t <= 0: return 0.0
    if t <= rho: return 6*(1-cos(t))
    if t >= R: return 1.0
    seg=2*(acos(clamp(sin(rho)/sin(t)))-cos(t)*alpha(t))
    return 6*(1-cos(t))-(15/pi)*seg


def sector_radius(z):
    return __import__('math').atan(tan(rho)/cos(z))


def f_by_radial_integration(t):
    t=max(t,0.0)
    return 15/pi*simpson(lambda z: 1-cos(min(t,sector_radius(z))), -pi/5, pi/5)


assert len(verts)==12
assert abs(f(R)-1)<1e-15
assert abs(alpha(R)-pi/5)<1e-12
area_one=5*simpson(lambda z:1-cos(sector_radius(z)),-pi/5,pi/5)
assert abs(area_one-pi/3)<1e-11

for j in range(21):
    t=R*j/20
    err=abs(f(t)-f_by_radial_integration(t))
    assert err < 3e-8,(j,err)
for j in range(200):
    assert f(R*(j+1)/200)>=f(R*j/200)-1e-12

onset=20/pi*sqrt(2*tan(rho))
terminal=15*tan(rho)/(pi*sin(R)*sin(pi/5))
for e in (0.003,0.001):
    on=(6*(1-cos(rho+e))-f(rho+e))/e**1.5
    te=(1-f(R-e))/e**2
    assert abs(on-onset)<.2,(e,on,onset)
    assert abs(te-terminal)<.2,(e,te,terminal)

mean_cos=(15/(2*pi))*ell*sin(rho)
mean_cos_by_angular=15/(2*pi)*simpson(
    lambda z: sin(sector_radius(z))**2,-pi/5,pi/5)
assert abs(mean_cos_by_angular-mean_cos)<2e-11
mean_sq_chord=2*(1-mean_cos)

rng=random.Random(20261016)
thresholds=[rho*.5,rho,(rho+R)/2,R-.015]
counts=[0]*len(thresholds)
summ=0.0
samples=100000
for _ in range(samples):
    x,y,z=(rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1))
    den=sqrt(x*x+y*y+z*z)
    x/=den; y/=den; z/=den
    m=max(x*a+y*b+z*c for a,b,c in verts)
    summ+=m
    for i,t in enumerate(thresholds):
        if m>=cos(t): counts[i]+=1
for i,t in enumerate(thresholds):
    assert abs(counts[i]/samples-f(t))<.009,(i,counts[i]/samples,f(t))
assert abs(summ/samples-mean_cos)<.006,(summ/samples,mean_cos)
print('ICOSAHEDRAL_NEAREST_LAW_OK radial_integrals=21 spherical_samples=100000 endpoint_asymptotics=4 exact_moment=1')
print('rho=',rho,'R=',R,'mean_squared_chord=',mean_sq_chord)
