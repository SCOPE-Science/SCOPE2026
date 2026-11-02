"""Independent finite checks for a sharp telegraph/Gaussian coherence comparison.

Requires numpy, scipy. Finite checks supplement, not replace, the analytic proof.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad


def telegraph(a, k, t):
    discriminant = k * k - 4.0 * a * a
    if discriminant > 1.e-12:
        d = math.sqrt(discriminant)
        return math.exp(-k*t/2) * (math.cosh(d*t/2)+(k/d)*math.sinh(d*t/2))
    if discriminant < -1.e-12:
        w = math.sqrt(-discriminant)
        return math.exp(-k*t/2) * (math.cos(w*t/2)+(k/w)*math.sin(w*t/2))
    return math.exp(-k*t/2) * (1.0 + k*t/2)


def gauss(a, k, t):
    return math.exp(-(a*a/(k*k))*(k*t-1+math.exp(-k*t)))


def direct_ctmc(a, k, t):
    Q = np.array([[-k/2,k/2],[k/2,-k/2]],float)
    B = Q + 1j*np.diag([a,-a])
    return (np.ones(2)@expm(t*B)@np.ones(2)/2).real


def confirm():
    tests=0
    for a,k in [(0.4,1),(0.5,1),(0.6,1),(0.7071067811865476,1),(.78,1),(1.5,1),(1.7,3)]:
        for t in [.002,.1,.75,2.,6.,13.]:
            p=telegraph(a,k,t)
            assert abs(p-direct_ctmc(a,k,t)) < 1e-9
            var=quad(lambda h:(t-h)*a*a*math.exp(-k*h),0,t,epsabs=1e-12)[0]
            assert abs(gauss(a,k,t)-math.exp(-var)) < 2e-10
            tests+=2
    for N in [1,2,3,6,15]:
        for ratio in [.1,.25,.4,.499,.5]:
            a=math.sqrt(N*ratio)
            for t in np.linspace(.05,70,120):
                f=telegraph(a/math.sqrt(N),1,t)**N
                g=gauss(a,1,t)
                assert abs(f)<=g+1.e-12
                tests+=1
        for ratio in [.51,.8,2.]:
            s=ratio; q=math.sqrt(4*s-1); phi=math.atan(1/q)
            for m in [100,101,102]:
                t=2*(phi+m*math.pi)/q
                logratio=N*(math.log(math.sqrt(1+1/q**2))+(s-.5)*t-s*(1-math.exp(-t)))
                assert logratio >0
                tests+=1
    for q in np.linspace(.03,1,100):
        d=1-math.exp(-1.5*math.pi); c=3*math.pi/8-.5
        assert c*(1/q-q)+d*(1+q*q)/4 > .5*math.log(2)
        tests+=1
    # Infinite-dimensional proof is analytic; this is only a cross-method finite check.
    return tests

if __name__=='__main__':
    print('PASS:',confirm(),'deterministic comparisons/inequalities')
