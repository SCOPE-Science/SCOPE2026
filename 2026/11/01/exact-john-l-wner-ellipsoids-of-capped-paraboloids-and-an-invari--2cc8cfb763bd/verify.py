"""Checks for extremal ellipsoids of capped paraboloids.

Run with python verify.py. Floating point tests corroborate; certificates in proof are exact.
"""
import math
import numpy as np
from scipy.optimize import minimize


def values(d):
    assert d >= 2
    aj = d/(d+1)
    bj = 2*d/(d+1)**2
    cj = (d*d+1)/(d+1)**2
    al = d/math.sqrt(d*d-1)
    bl = d/(d+1)
    cl = bl
    z0 = (d-1)/(d+1)
    ratio = (d+1)/2*((d+1)/(d-1))**((d-1)/2)
    return (aj,bj,cj),(al,bl,cl),z0,ratio


def min_inside_value(a,b,c):
    lo,hi = c-b,c+b
    zstar = max(lo,min(hi,c-b*b/(2*a*a)))
    return zstar-a*a*(1-(zstar-c)**2/(b*b))


def max_cover_value(a,b,c):
    def f(z): return z/(a*a)+((z-c)/b)**2
    return max(f(0.),f(1.))


def numerical_fit(d,kind,expected):
    def obj(z):
        a,b,c=z
        if min(a,b)<=0: return 1e5
        v=(d-1)*math.log(a)+math.log(b)
        return -v if kind=='inner' else v
    if kind=='inner':
        cs=[{'type':'ineq','fun':lambda z: z[2]-z[1]},
            {'type':'ineq','fun':lambda z: 1-z[2]-z[1]},
            {'type':'ineq','fun':lambda z: min_inside_value(*z)}]
    else:
        cs=[{'type':'ineq','fun':lambda z: 1-(z[2]/z[1])**2},
            {'type':'ineq','fun':lambda z: 1-1/z[0]**2-((1-z[2])/z[1])**2}]
    start=np.array(expected)*np.array([.97,.97,1.]) if kind=='inner' else np.array(expected)*np.array([1.08,1.08,1.])
    opt=minimize(obj,start,method='SLSQP',bounds=[(.00001,5),(.00001,5),(-1,2)],constraints=cs,
                 options={'ftol':1e-12,'maxiter':2000})
    assert opt.success, (d,kind,opt.message,opt.x)
    err=max(abs((opt.x[i]-expected[i])/expected[i]) for i in range(3))
    assert err < 0.00005,(d,kind,err,opt.x,expected)
    return err

max_contact=0.
max_fit=0.
for d in [2,3,4,5,8,12,30,50,100,300]:
    J,L,z0,ratio=values(d)
    aj,bj,cj=J; al,bl,cl=L
    assert abs(cj+bj-1)<2e-14
    assert abs(cj-bj-z0*z0)<2e-14
    assert abs((aj*aj)*(1-1/d**2)-z0)<2e-14
    assert abs((z0-cj)/bj+1/d)<2e-14
    assert abs((-cl)/bl+1)<2e-14
    assert abs((1-cl)/bl-1/d)<2e-14
    assert abs(1/al**2+(1-cl)**2/bl**2-1)<2e-14
    for z in np.linspace(cj-bj,cj+bj,10001):
        lhs=z-aj*aj*(1-(z-cj)**2/(bj*bj))
        exact=((d+1)**2)/4*(z-z0)**2
        max_contact=max(max_contact,abs(lhs-exact))
        assert lhs>-4e-11,(d,z,lhs)
    for z in np.linspace(0,1,10001):
        val=z/al**2+(z-cl)**2/bl**2
        assert val<1+1e-12,(d,z,val)
    assert abs(ratio - (al/aj)**(d-1)*(bl/bj))<1e-10*ratio
    if d in [2,3,5,8]:
        max_fit=max(max_fit,numerical_fit(d,'inner',J),numerical_fit(d,'outer',L))
print('PASS: 10 dimensions; 100010 containment samples per body; exact moment identities checked; 8 independent SLSQP fits')
print('max quadratic identity floating error:',max_contact)
print('max independent parameter relative discrepancy:',max_fit)
