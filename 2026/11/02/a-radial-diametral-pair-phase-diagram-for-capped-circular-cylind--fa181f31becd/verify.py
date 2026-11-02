"""Independent numeric checks for capped-cylinder opposite-cap distance formulas.

Requires Python 3, NumPy and SciPy; all geometric formulas are scale-homogeneous.
No numerical result is used as an infinite proof.
"""
import math
import numpy as np
from scipy.optimize import differential_evolution, minimize_scalar

PI = math.pi

def contact_min(R, r, t):
    s = math.sin(t / 2)
    if r >= R*s:
        return 2*R*math.cos(t/2)
    return 2*math.sqrt(R*R+r*r-2*R*r*s)

def distance_1d(R, h, r):
    f = lambda t: contact_min(R,r,t)+math.hypot(h,R*t)
    # Discontinuous derivative only at the known continuous branch seam.
    seam=2*math.asin(min(1,r/R))
    candidates=[f(0), f(seam), f(PI)]
    for a,b in [(0,seam),(seam,PI)]:
        if b>a+1e-12:
            z=minimize_scalar(f,bounds=(a,b),method='bounded',options={'xatol':1e-12})
            candidates.append(z.fun)
    return min(candidates)

def raw_cap_sum(R,r,t,alpha):
    beta=alpha+t
    return math.hypot(R*math.cos(alpha)-r,R*math.sin(alpha))+math.hypot(R*math.cos(beta)+r,R*math.sin(beta))

def direct_2angle(R,h,r):
    def f(ab):
        a,b=ab
        t=abs((b-a+PI)%(2*PI)-PI)
        return raw_cap_sum(R,r,t,a)+math.hypot(h,R*t)
    z=differential_evolution(f,[(-PI,PI),(-PI,PI)],seed=319,polish=True,popsize=12,maxiter=150,tol=1e-9)
    # The rim-antipodal competitor lies at a thin boundary basin near the first threshold.
    # Explicit candidate angle pairs keep the check global.
    return min(z.fun, f((0., PI)), f((0.,0.)), f((PI,0.)), f((PI,PI)))

def threshold_radius(R,h):
    D=h+2*R
    def S(t): return D-math.hypot(h,R*t)
    def deficit(t): return S(t)-2*R*math.cos(t/2)
    if h<=R*(PI*PI-4)/4:
        return R
    # Certified formula is inf over open positivity set. Here a dense grid +
    # bounded local refinement are numerical diagnostics only.
    ts=np.linspace(1e-5,PI,4001)
    vals=[]
    for t in ts:
        if deficit(t)>1e-13:
            b=R*math.sin(t/2)
            d=S(t)**2/4-R*R*math.cos(t/2)**2
            vals.append(b-math.sqrt(max(0,d)))
    return min(vals) if vals else R

def run():
    # Angular focal-ellipse contact minimization against direct rim-coordinate optimization.
    max_angular=0.0
    for R in [0.7,1.0,2.2]:
        for frac in [0.0,0.13,0.49,0.82,1.0]:
            for t in [0.05,0.32,0.8,1.44,2.5,PI]:
                r=frac*R
                z=minimize_scalar(lambda a:raw_cap_sum(R,r,t,a),
                                  bounds=(-PI,PI),method='bounded', options={'xatol':1e-12})
                # Several equivalent minimizers can coexist; a coarse sweep
                # prevents selecting a non-global local minimum.
                alphas=np.linspace(-PI,PI,1801)
                sample=min(raw_cap_sum(R,r,t,float(a)) for a in alphas)
                err=abs(min(z.fun,sample)-contact_min(R,r,t))
                max_angular=max(max_angular,err)
                assert err<2e-5, (R,frac,t,err)
    max_pair=0.0
    for h in [.3,1.1,1.48,1.67,1.9,2.,2.3,3.5]:
        for r in [.04,.21,.56,.91,1.]:
            expected=distance_1d(1.,h,r)
            independent=direct_2angle(1.,h,r)
            err=abs(expected-independent)
            max_pair=max(max_pair,err)
            assert err<2e-6,(h,r,expected,independent)
    h0=(PI*PI-4)/4
    assert abs((h0+2)-math.hypot(h0,PI))<1e-12
    for h in [0.3,1.,h0-1e-4,h0]:
        for r in [0.,.2,.7,1.]:
            assert abs(distance_1d(1.,h,r)-(h+2))<2e-8
    for h in [h0+.03,1.7,1.9]:
        rc=threshold_radius(1,h)
        assert 0<rc<1, (h,rc)
        assert abs(distance_1d(1,h,rc*.8)-(h+2))<2e-6,(h,rc)
        assert distance_1d(1,h,(rc+1)/2)<h+2-1e-6,(h,rc)
    for h in [2.,2.3,4.]:
        assert abs(distance_1d(1,h,0)-(h+2))<1e-10
        assert all(distance_1d(1,h,r)<h+2-1e-10 for r in [.08,.25,.6,1.])
    print('PASS: contact, two-angle minimization, threshold and regime checks')
    print('max direct-contact discrepancy', max_angular)
    print('max direct-pair discrepancy', max_pair)
    print('first sharp height ratio',h0)
    for h in [1.5,1.7,1.9,2.0]:
        print('height',h,'numerical critical radius',threshold_radius(1.,h))

if __name__=='__main__':run()
