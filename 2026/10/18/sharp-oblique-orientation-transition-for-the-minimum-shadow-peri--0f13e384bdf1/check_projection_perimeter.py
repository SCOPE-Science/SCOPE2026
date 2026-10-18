"""Reproduce numerical checks for the minimum shadow-perimeter law of a circular bicone.

Run: python check_projection_perimeter.py
Uses NumPy and SciPy. Finite numerical tests supplement, not replace, the proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq, minimize_scalar
from scipy.special import ellipe, ellipeinc
from scipy.spatial import ConvexHull


def transition(t):
    return math.hypot(1.0, t) - math.asinh(1.0 / t)


def formula(s, t):
    L = math.hypot(1.0, t)
    if s <= 1.0 / L:
        return 4 * ellipe(s*s)
    alpha = math.acos(1.0/(s*L))
    return 4*(t*s*math.sin(alpha) + ellipeinc(math.pi/2-alpha, s*s))


def independent_integral(s, t):
    L = math.hypot(1.0,t)
    corners = [math.acos(1/(s*L))] if s*L > 1 else []
    return 4*quad(lambda a:max(math.sqrt(max(0, 1-s*s*math.cos(a)**2)), t*s*math.cos(a)),
                  0, math.pi/2, points=corners if corners else None,
                  epsabs=2e-11, limit=200)[0]


def stationarity(x,t):
    L=math.hypot(1.0,t)
    I=quad(lambda v:(math.sin(v)**2*math.cos(v))/
           (math.sqrt(1-math.sin(v)**2/L**2)*math.sqrt(max(1e-300,x*x-math.sin(v)**2))),
           0, math.pi/2, epsabs=2e-12,limit=200)[0]
    return t*math.sqrt(x*x-1)-I/L


def unique_minimizer(t, threshold):
    L=math.hypot(1.0,t)
    if t<=threshold: return 1.0
    x=brentq(lambda x:stationarity(x,t),1.0,L,xtol=1e-13)
    return x/L


def independent_hull(s,t,points=2048):
    ang=np.arange(points)*2*math.pi/points
    cc=math.sqrt(max(0.0,1-s*s))
    ellipse=np.stack([cc*np.cos(ang),np.sin(ang)],axis=1)
    data=np.vstack([ellipse,np.array([[-t*s,0],[t*s,0]])])
    v=data[ConvexHull(data).vertices]
    return float(np.linalg.norm(v-np.roll(v,-1,axis=0),axis=1).sum())


def run():
    t0=brentq(transition,0.3,1.0,xtol=1e-15)
    assert abs(t0-0.6627434193491816)<2e-14
    print('UNIQUE_THRESHOLD_OK %.15f'%t0)

    rng=np.random.default_rng(5212026)
    max_err=0.0
    for _ in range(420):
        t=math.exp(rng.uniform(math.log(.10),math.log(8.0)))
        s=rng.uniform(.00001,.99999)
        err=abs(formula(s,t)-independent_integral(s,t))
        max_err=max(err,max_err)
        assert err<1e-7, (t,s,err)
    print('INDEPENDENT_SUPPORT_INTEGRAL_OK cases=420 max_error=%.2g'%max_err)

    err_hull=0.0
    for _ in range(75):
        t=math.exp(rng.uniform(math.log(.16),math.log(6.0)))
        s=rng.uniform(.02,.999)
        # Circle sampling is inscribed; finite-sampling error is expected.
        err=abs(formula(s,t)-independent_hull(s,t))
        err_hull=max(err,err_hull)
        assert err<6.0e-6, (t,s,err)
    print('INDEPENDENT_PROJECTED_CONVEX_HULLS_OK cases=75 max_error=%.2g'%err_hull)

    worst_min_gap=0
    for t in [.08,.3,.5,t0,t0+0.0001,.69,.75,1,1.5,2,5,20]:
        s=unique_minimizer(t,t0)
        assert (s==1) == (t<=t0)
        if t>t0:
            assert abs(stationarity(s*math.hypot(1,t),t))<5e-10
        vals=[formula(v,t) for v in np.linspace(0,1,1601)]
        minimum=formula(s,t)
        assert min(vals)>=minimum-5e-9,(t,min(vals)-minimum)
        res=minimize_scalar(lambda a: independent_integral(math.sin(a),t),bounds=(0,math.pi/2),method='bounded',options={'xatol':3e-8})
        assert abs(res.fun-minimum)<3e-6,(t,res.fun,minimum)
        worst_min_gap=max(worst_min_gap,abs(res.fun-minimum))
    print('GLOBAL_MINIMIZER_GRID_AND_INDEPENDENT_OPTIMIZER_OK maximum_deviation=%.2g'%worst_min_gap)

    c=2*math.sqrt(t0/(1+t0*t0))
    errors=[]
    for delta in [1e-3,1e-4,1e-5]:
        star=math.asin(unique_minimizer(t0+delta,t0))
        errors.append(abs((math.pi/2-star)/math.sqrt(delta)-c))
    assert errors[2]<errors[1]<errors[0]
    assert errors[-1]<.002
    for t in [30,50,100]:
        star=math.asin(unique_minimizer(t,t0))
        assert abs(star-(1/t-1/(3*t**3)))<2e-6
    print('SQUARE_ROOT_TRANSITION_AND_TALL_CONE_ASYMPTOTICS_OK')
    print('ALL_BICONE_SHADOW_PERIMETER_CHECKS_OK')

if __name__=='__main__':run()
