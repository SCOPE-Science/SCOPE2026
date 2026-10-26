"""Independent consistency checks for weak fixed-dose tumbling control.
These numerical checks supplement, but do not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from verify import propagate_constant, integrate_schedule

def kernel(z,k,a,v=1.):
    if abs(k-a)<1e-10:
        return 2*v*v/(k+a)*z*math.exp(-2*k*z)
    return 2*v*v/(k+a)*(math.exp(-(k+a)*z)-math.exp(-2*k*z))/(k-a)

def critical_lag(k,a):
    if abs(k-a)<1e-10:return 1/(2*k)
    return math.log(2*k/(k+a))/(k-a)

def best_start(T,m,k,a):
    fn=lambda s:kernel(T-s,k,a)-kernel(T-s-m,k,a)
    if fn(0)>=0:return 0.0
    return brentq(fn,0,T-m,xtol=1e-13)

def variance_for_window(T,m,s,k,a,eps,v=1.):
    b0=v/(k+a);a0=v*b0/k
    ss=[(s,k,a),(m,k,a+eps),(T-s-m,k,a)]
    return integrate_schedule([(x,y,z) for x,y,z in ss if x>1e-13],(a0,b0),v=v)[0]

def check():
    n=0
    for k,a in [(1.2,.45),(.5,2.),(1.,1.),(2.,4.),(3.,.1)]:
        star=critical_lag(k,a)
        assert star>0
        zgrid=np.linspace(0,3*star,401)
        ww=[kernel(z,k,a) for z in zgrid]
        assert zgrid[np.argmax(ww)]-star <(zgrid[1]-zgrid[0])+1e-9
        n+=1
    for k,a,T,m in [(1.2,.45,2.0,.25),(1.2,.45,.31,.15),(.5,2.,1.5,.2),(1.,1.,1.3,.1),(3.,.1,3.,.35)]:
        s=best_start(T,m,k,a)
        starts=np.linspace(0,T-m,251)
        gains=[quad(lambda t:kernel(T-t,k,a),z,z+m,epsabs=1e-12)[0] for z in starts]
        best=quad(lambda t:kernel(T-t,k,a),s,s+m,epsabs=1e-12)[0]
        assert best >= max(gains)-1e-11,(k,a,T,m,s)
        for eps in (1e-2,1e-3,1e-4):
            base=1/(k*(k+a))
            observed=(base-variance_for_window(T,m,s,k,a,eps))/eps
            assert abs(observed-best) < 1.5*eps,(k,a,T,m,eps,observed,best)
            n+=1
    k,a=1.2,.45;T=2.;m=.25
    s=best_start(T,m,k,a)
    assert 0<s<T-m and s>0.25
    assert variance_for_window(T,m,s,k,a,.1) < variance_for_window(T,m,0,k,a,.1)
    assert variance_for_window(T,m,s,k,a,.1) < variance_for_window(T,m,T-m,k,a,.1)
    n+=3
    print(f'{n} kernel, optimal-window, ODE dose-response checks passed. T=2 example optimal window [{s:.10f},{s+m:.10f}]')

if __name__=='__main__':check()
