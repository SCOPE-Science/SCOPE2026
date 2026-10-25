"""Reproduce the global brightness transition for round solid cones."""
import math, random
from scipy.optimize import brentq
from scipy.spatial import ConvexHull
import numpy as np
pi=math.pi

def f(a):return math.cos(a)+math.sin(a)*(pi/2+a)
def D(a):return pi/2+a
def H(a):return math.sqrt(D(a)/(math.sin(a)*math.cos(a)))
def root(a):return D(a)*(D(a)+1/math.tan(a))-pi*pi
asaddle=brentq(lambda a:math.tan(2*a)-pi-2*a,.1,pi/4-.00001)
acritical=brentq(root,.03,asaddle)
hs,hc=H(asaddle),H(acritical)
assert 2.14553<hs<2.14555
assert 2.64140<hc<2.64141
print('CRITICAL_HEIGHT_AND_SADDLE_INTERVALS_OK',hs,hc)

def area(h,z):
    if z>=h/math.hypot(h,1):return pi*z
    x=z/(h*math.sqrt(1-z*z))
    return pi*z/2+math.sqrt(h*h-(h*h+1)*z*z)+z*math.asin(x)

def oblique(h):
    aa=brentq(lambda a:H(a)-h,1e-11,asaddle-1e-11)
    x=math.sin(aa)
    return h*f(aa)/math.sqrt(1+h*h*x*x),h*x/math.sqrt(1+h*h*x*x)

for h in [0.3,1.,2.1,2.14,2.2,2.4,2.6,hc,2.7,3.,4.,6.,20.]:
    values=[area(h,j/10000) for j in range(10001)]
    mx=max(values)
    assert abs(mx-max(pi,oblique(h)[0] if h>hs else 0))<2e-4
    if h>hs:
        v,z=oblique(h)
        assert abs(area(h,z)-v)<2e-12
print('GLOBAL_MAXIMUM_COMPETITION_ALL_REGIMES_OK')

rng=random.Random(407)
max_err=0
for h in [0.25,1.0,2.4,hc,3.,6.]:
    N=128
    pts=np.array([[math.cos(i*2*pi/N),math.sin(i*2*pi/N),0.] for i in range(N)]+[[0,0,h]])
    for k in range(200):
        z=rng.uniform(-1,1);phi=rng.uniform(0,2*pi)
        normal=np.array([math.sqrt(1-z*z)*math.cos(phi),math.sqrt(1-z*z)*math.sin(phi),z])
        c=np.array([-math.sin(phi),math.cos(phi),0.]); d=np.cross(normal,c)
        xy=pts@np.stack((c,d),axis=1)
        num=ConvexHull(xy).volume
        th=area(h,abs(z))
        max_err=max(max_err,abs(num-th))
assert max_err<.003
print('INDEPENDENT_1200_PROJECTED_CONVEX_HULLS_OK',max_err)
print('ALL_CIRCULAR_CONE_GLOBAL_BRIGHTNESS_CHECKS_OK')
