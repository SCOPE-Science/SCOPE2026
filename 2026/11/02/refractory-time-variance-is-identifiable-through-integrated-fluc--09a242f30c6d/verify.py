"""Independent analytic and sampled checks for a partial-reset diffusion with pauses.
Requires Python 3, numpy, sympy. No external data or network access.
"""
from __future__ import annotations
import math
import numpy as np
import sympy as sp


def predicted_variance_rate(a: float, r: float, D: float, h: float, v: float) -> float:
    assert 0 < a < 1 and r > 0 and D > 0 and h > 0 and v >= 0
    x = r*h
    q0 = (2*D/(r*r*(1+x))) * (
        (2+2*a*(1+a)*x+a*a*(1+a)*x*x)/((1-a)**2*(1+a)))
    return q0 + (2*D*a*a/((1-a*a)*(1+x))) * v


def symbolic_checks():
    a,r,D,h,v=sp.symbols('a r D h v', positive=True)
    c=1/r+a*h
    V=2*D*a*a/(r*(1-a*a))
    k=a*c/(1-a)
    moment=sp.factor(V*(1/r**2+a*a*v)+4*D/r**3+4*D/r**2*(a*h+k)+2*D/r*(a*a*v+(a*h+k)**2))
    q=sp.factor(moment/(1/r+h))
    x=r*h
    expected=sp.factor((2*D/(r*r*(1+x)))*((2+2*a*(1+a)*x+a*a*(1+a)*x*x)/((1-a)**2*(1+a)))+2*D*a*a*v/((1-a*a)*(1+x)))
    assert sp.simplify(q-expected)==0
    assert sp.simplify(sp.diff(q,v)-2*D*a*a/((1-a*a)*(1+r*h)))==0
    # Independent Poisson equation for exponential pauses of mean h, variance h².
    va=2*D/(r*(1-a*a)); pA=1/(1+r*h); pR=1-pA
    bA=(1/r+a*h)/(1-a);bR=bA+h
    poisson=2*va*(pA*bA+pR*a*a*bR)
    assert sp.simplify(poisson-q.subs(v,h*h))==0
    assert sp.simplify(q.subs(a,0)-4*D/(r*r*(1+r*h)))==0
    print('Symbolic cycle-martingale, slope, independent Markov-Poisson, and complete-reset checks passed')


def simulated_martingale_rate(seed, a,r,D,h,which,N=650_000):
    rng=np.random.default_rng(seed)
    e=rng.exponential(1/r,N)
    if which=='fixed': R=np.full(N,h);v=0.
    elif which=='exponential': R=rng.exponential(h,N);v=h*h
    elif which=='two_point':
        # equal probability of h/4 and 7h/4: fixed mean h, variance 9h²/16
        R=np.where(rng.integers(2,size=N)==0,h/4,7*h/4)
        v=9*h*h/16
    else: raise ValueError(which)
    B=np.sqrt(2*D*e)*rng.normal(size=N)
    J=e*B/2+np.sqrt(D*e**3/6)*rng.normal(size=N)
    # warm-start AR(1) using true stationary variance; independent of future events
    y=rng.normal(scale=math.sqrt(2*D*a*a/(r*(1-a*a))))
    c=1/r+a*h
    k=a*c/(1-a)
    total=0.; total_sq=0.
    # M = (E+aR-c)*Y + J + (aR+k)B
    for i in range(N):
        M=(e[i]+a*R[i]-c)*y+J[i]+(a*R[i]+k)*B[i]
        total+=M
        total_sq+=M*M
        y=a*(y+B[i])
    estimate=(total_sq/N-(total/N)**2)/(1/r+h)
    prediction=predicted_variance_rate(a,r,D,h,v)
    relative=abs(estimate/prediction-1)
    print(f'Sampled martingale {which}: estimate={estimate:.8f}, theory={prediction:.8f}, rel={relative:.4%}')
    assert relative<0.02

if __name__=='__main__':
    symbolic_checks()
    for i,(a,r,D,h) in enumerate([(0.4,1.3,1.7,0.9),(0.7,1.,0.5,2.0),(0.12,2.3,1.1,0.3)]):
        for j,w in enumerate(('fixed','exponential','two_point')):
            simulated_martingale_rate(281828+i*10+j,a,r,D,h,w)
    print('ALL CHECKS PASSED')

# A second test samples physical-time integrals directly (including incomplete final cycles),
# without using the martingale formula to calculate the sample statistic.
def physical_time_test():
    try:
        from numba import njit
    except ImportError:
        return
    @njit
    def experiment(seed, a, r, D, h, mode, horizon, nrep):
        np.random.seed(seed)
        values=np.empty(nrep)
        for k in range(nrep):
            y=0.
            area=0.
            t=0.
            # Equilibrate the embedded AR(1) recursion without contributing to the area.
            for j in range(120):
                e=np.random.exponential(1/r)
                b=np.sqrt(2*D*e)*np.random.randn()
                y=a*(y+b)
            while t<horizon:
                e=np.random.exponential(1/r)
                if mode==0:
                    pause=h
                elif mode==1:
                    pause=np.random.exponential(h)
                else:
                    pause=h/4 if np.random.random()<.5 else 7*h/4
                remaining=horizon-t
                if remaining<e:
                    # Brownian time-integral of a shorter, final exploration interval.
                    j=np.sqrt(2*D*remaining**3/3)*np.random.randn()
                    area+=y*remaining+j
                    t=horizon
                else:
                    b=np.sqrt(2*D*e)*np.random.randn()
                    j=e*b/2+np.sqrt(D*e**3/6)*np.random.randn()
                    area+=y*e+j
                    t+=e
                    yn=a*(y+b)
                    if horizon-t<pause:
                        area+=yn*(horizon-t)
                        t=horizon
                    else:
                        area+=yn*pause
                        t+=pause
                        y=yn
            values[k]=area
        return values
    for mode,name,v in [(0,'fixed',0.),(1,'exponential',1.44),(2,'two_point',0.81)]:
        a=.55;r=1.2;D=.8;h=1.2
        y=experiment(1013+mode,a,r,D,h,mode,4000.,2400)
        pred=predicted_variance_rate(a,r,D,h,v)
        observed=np.var(y,ddof=1)/4000.
        err=abs(observed/pred-1)
        print(f'Physical-time {name}: estimate={observed:.6f}, formula={pred:.6f}, rel={err:.2%}')
        assert err<.11

if __name__=='__main__':
    physical_time_test()
