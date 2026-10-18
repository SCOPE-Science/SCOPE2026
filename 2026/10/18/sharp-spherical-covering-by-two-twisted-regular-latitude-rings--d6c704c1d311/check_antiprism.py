"""Independent numerical checks of spherical covering radii of two staggered regular rings.
Only NumPy/SciPy required. The analytic proof is separate.
"""
import math
import numpy as np
from scipy.spatial import ConvexHull

def vertices(n,delta,h):
    r=math.sqrt(1-h*h)
    top=[(r*math.cos(2*math.pi*k/n),r*math.sin(2*math.pi*k/n),h) for k in range(n)]
    bot=[(r*math.cos(delta+2*math.pi*k/n),r*math.sin(delta+2*math.pi*k/n),-h) for k in range(n)]
    return np.array(top+bot)

def predicted(n,delta,h):
    c=math.cos(math.pi/n); t=math.cos(delta-math.pi/n);r=math.sqrt(1-h*h)
    d=h*r*(c+t)/math.sqrt(4*h*h+r*r*(t-c)**2)
    return min(h,d)

rng=np.random.default_rng(2091)
count=0
for n in (3,4,5,6,8,12,21):
    for delta in (0, 1.e-5, math.pi/(2*n), math.pi/n, 1.7*math.pi/n, 2*math.pi/n-1.e-5, 2*math.pi/n):
        for h in (.07,.22,.41,.69,.89):
            v=vertices(n,delta,h)
            hull=ConvexHull(v)
            distances=-hull.equations[:,3]/np.linalg.norm(hull.equations[:,:3],axis=1)
            actual=np.min(distances)
            expected=predicted(n,delta,h)
            assert abs(actual-expected)<2.e-11,(n,delta,h,actual,expected)
            if n in (3,4,6) and delta in (0,math.pi/n) and h in (.22,.69):
                q=rng.normal(size=(25000,3));q/=np.linalg.norm(q,axis=1,keepdims=True)
                angular_cos=np.max(q@v.T,axis=1)
                assert np.min(angular_cos)>=actual-4.e-11
            count+=1
for n in (3,4,5,8,20):
    c=math.cos(math.pi/n)
    for delta in (0,math.pi/(3*n),math.pi/n,5*math.pi/(3*n),2*math.pi/n):
        t=math.cos(delta-math.pi/n)
        x_star=c*t/(1+c*t)
        radius=math.sqrt(x_star)
        eps=1e-5
        assert predicted(n,delta,math.sqrt(x_star))>predicted(n,delta,math.sqrt(x_star)-eps)
        assert predicted(n,delta,math.sqrt(x_star))>predicted(n,delta,math.sqrt(x_star)+eps)
        assert abs(predicted(n,delta,math.sqrt(x_star))-radius)<1e-12
assert abs(predicted(3,math.pi/3,1/math.sqrt(3))-1/math.sqrt(3))<1e-12
print('ANTIPRISM_SPHERICAL_COVERING_OK facet_comparisons',count,'samplings',300000,'optimal_profiles',25)
