"""Numerical cross-checks for the geodesic-radius law on right square prisms.

Requires NumPy and SciPy. The exact analytical proof does not depend on this script.
"""
import math
import numpy as np
from scipy.integrate import quad


def area_formula(h, r):
    """Geodesic ball surface area for a unit-base square prism (h > 0)."""
    if r <= 0.0:
        return 0.0
    q = math.sqrt(h*h + h + 0.5)
    if r <= math.sqrt(0.5):
        return math.pi*r*r
    if r <= q:
        return 4*r*r*math.asin(1/(2*r)) + math.sqrt(4*r*r - 1) - 1
    if r <= h+1:
        phi = math.pi/4 - math.acos((h+1)/(math.sqrt(2)*r))
        return 4*r*r*phi - 2*h*h + 2*(h+1)*math.sqrt(max(0.0, 2*r*r-(h+1)**2))
    return 4*h+2


def rho(h, theta):
    """Radial boundary in one octant of the unfolded source domain."""
    return min(float('inf') if theta == 0 else 0.5/math.sin(theta),
               (h+1)/(math.cos(theta)+math.sin(theta)))


def area_integral(h, r):
    theta_star = math.atan(1/(2*h+1))
    return 4 * sum(quad(lambda t: min(r*r, rho(h,t)**2), a,b,
                        epsabs=1e-11, epsrel=1e-11)[0]
                   for a,b in [(0,theta_star),(theta_star,math.pi/4)])


def sample_distance(h, n, rng):
    """Independent face-wise surface-area sampler; not a polygon-area sampler."""
    u=rng.random(n)
    v=rng.random(n)
    face=rng.random(n)*(4*h+2)
    out=np.empty(n)
    bottom=face<1
    top=(face>=1)&(face<2)
    side=~(bottom|top)
    out[bottom]=np.hypot(u[bottom]-.5,v[bottom]-.5)
    t=np.minimum.reduce([u[top],1-u[top],v[top],1-v[top]])
    k=np.argmin(np.stack([v[top],1-v[top],u[top],1-u[top]],axis=0),axis=0)
    cross=np.where(k<2,u[top]-.5,v[top]-.5)
    out[top]=np.hypot(cross,h+.5+t)
    out[side]=np.hypot(u[side]-.5,.5+h*v[side])
    return out


def moment_formula(h):
    return (4*h**3+9*h*h+8*h+2)/(6*(2*h+1))


def checks():
    rng=np.random.default_rng(20261023)
    tested=0
    for h in [0.05,0.23,0.8,1.0,2.0,7.0]:
        q=math.sqrt(h*h+h+.5)
        endpoints=[0,.001,math.sqrt(.5),q,h+1]
        endpoints.sort()
        samples=sample_distance(h,160000,rng)
        assert abs(np.mean(samples*samples)-moment_formula(h))<6*np.std(samples*samples)/math.sqrt(len(samples)), h
        for r in np.linspace(.025,h+1,37):
            a=area_formula(h,float(r))
            b=area_integral(h,float(r))
            assert abs(a-b)<1e-8,(h,r,a,b)
            emp=np.mean(samples<=r)
            assert abs(emp-a/(4*h+2))<0.012,(h,r,emp,a/(4*h+2))
            tested+=1
        for rr in [math.sqrt(.5),q,h+1]:
            aa=area_formula(h,rr)
            bb=area_integral(h,rr)
            assert abs(aa-bb)<1e-8,(h,rr,aa,bb)
            tested+=1
        assert abs(area_formula(h,h+1)-(4*h+2))<1e-8
    for h1,h2 in [(0.05,.1),(.1,.5),(.7,1.0),(1.,3.),(3.,8.)]:
        for r in np.linspace(.001,h2+1,1001):
            assert area_formula(h1,float(r))/(4*h1+2) > area_formula(h2,float(r))/(4*h2+2)-1e-10,(h1,h2,r)
            tested+=1
    print('PASS',tested,'tests: polar quadrature, face-wise Monte Carlo, second moments, height order')

if __name__ == '__main__':
    checks()
