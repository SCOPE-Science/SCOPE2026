"""Reproduce the stationary cross-particle energy-memory theorem.

Requirements: Python 3.10+, numpy, scipy, sympy.
Run: python verify_covariance.py
No random seeds or simulation tolerances are required.
"""
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import solve_ivp


def formula(kappa, delta, rate, diffusion):
    k, d, r, D = kappa, delta, rate, diffusion
    b = k * (k + r) - d*d
    h = 2*(k*k-d*d) + k*r
    v = D*D*d*d * (2*(k*k-d*d) + 3*k*r+r*r) / (h*b*b)
    f = 4*d*d*D*D/b
    disc = math.hypot(r, 2*d)
    lo, hi = 2*k+r-disc, 2*k+r+disc
    q = 4*D*D*d*d*r*(2*k+r)/(h*b)
    return v, f, lo, hi, q


def covariance_independent(kappa, delta, rate, diffusion, t):
    """Independent 4-state linear moment propagation, not scalar ODE."""
    k,d,r,D=kappa,delta,rate,diffusion
    switch = np.array([[-r, r],[r, -r]],dtype=float)
    a1 = switch.T - np.diag([2*(k+d),2*(k-d)])
    a2 = switch.T - np.diag([4*(k+d),4*(k-d)])
    probs=np.array([.5,.5])
    mvec=np.linalg.solve(a1,-2*D*probs)
    nvec=np.linalg.solve(a2,-4*D*mvec)
    m=float(mvec.sum())
    w0=nvec-m*mvec
    z0=mvec-m*probs
    block=np.block([[a1,2*D*np.eye(2)], [np.zeros((2,2)),switch.T]])
    state=expm(block*t)@np.r_[w0,z0]
    return float(state[:2].sum()),float(nvec.sum()-m*m),m


def covariance_ode(kappa,delta,rate,diffusion,t):
    v,f,lo,hi,_=formula(kappa,delta,rate,diffusion)
    sol=solve_ivp(lambda u,z:[z[1],-(lo+hi)*z[1]-lo*hi*z[0]+f*math.exp(-2*rate*u)],
                  (0,t),[v,0.],rtol=8e-12,atol=3e-13,method='DOP853')
    if not sol.success: raise AssertionError(sol.message)
    return float(sol.y[0,-1]),float(sol.y[1,-1])


def source_equal_time(kappa,delta,rate,diffusion):
    mu1,mu2=kappa+delta,kappa-delta
    R1=rate/(2*mu1)
    R2=rate/(2*mu2)
    return (diffusion/rate)**2*(R1-R2)**2*(2+3*R1+3*R2+4*R1*R2)/((1+R1+R2)**2*(2+R1+R2))


def main():
    checks=0
    k,d,r,D=sp.symbols('k d r D', positive=True)
    b=k*(k+r)-d**2
    h=2*(k*k-d*d)+k*r
    v=D**2*d**2*(2*(k*k-d*d)+3*k*r+r*r)/(h*b**2)
    f=4*d**2*D**2/b
    dot2=4*D**2*d**2*r*(2*k+r)/(h*b)
    assert sp.factor(4*b*v-f-dot2)==0
    checks+=1
    # The characteristic equation at the telegraph pole changes sign
    # precisely at the harmonic mean of the two stiffnesses.
    rc=(k*k-d*d)/k
    assert sp.factor(((-2*r)**2+(4*k+2*r)*(-2*r)+4*b)-4*k*(rc-r))==0
    checks+=1
    test_pars=[(1.,.4,.2,1.),(1.,.4,.84,1.),(1.,.4,2.5,1.),
               (2.,.9,.07,.8),(2.,.9,1.595,.8),(2.,.9,5.,.8),
               (.8,.79,.3,2.),(3.,.1,.6,.5),(1.,.02,1.,.4)]
    for k,d,r,D in test_pars:
        assert k>d>0 and r>0 and D>0
        V,F,a,bb,vel2=formula(k,d,r,D)
        assert 0<a<bb and V>0 and F>0 and vel2>0
        checks+=1
        v_source=source_equal_time(k,d,r,D)
        assert math.isclose(V,v_source,rel_tol=1e-11,abs_tol=1e-13),(k,d,r,V,v_source)
        checks+=1
        for t in [0.,.03,.2,.5,1.,2.,5.,9.,15.]:
            direct,V2,m=covariance_independent(k,d,r,D,t)
            ode,slope=covariance_ode(k,d,r,D,t)
            assert math.isclose(V,V2,rel_tol=2e-11,abs_tol=1e-13)
            assert math.isclose(direct,ode,rel_tol=2e-7,abs_tol=2e-9),(k,d,r,t,direct,ode)
            checks+=1
        # Check the stationary-energy cusp is quadratic, not linear.
        assert math.isclose(F-4*(k*(k+r)-d*d)*V,-vel2,rel_tol=2e-10,abs_tol=1e-11)
        checks+=1
        # Check strictly decreasing energy covariance at sampled positive lags.
        for t in [.01,.3,1.,3.,8.]:
            c,slope=covariance_ode(k,d,r,D,t)
            assert c>0 and slope<0,(k,d,r,t,c,slope)
            checks+=1
        # Verify leading amplitude and all three regimes using an exact
        # matrix exponential, away from underflow and near-cancelled poles.
        rc=(k*k-d*d)/k
        if abs(r-rc)<1e-9:
            assert math.isclose(a,2*r,rel_tol=2e-13,abs_tol=2e-13)
            amp=F/(bb-2*r)
            t=75/max(2*r,1.)
            exact=covariance_independent(k,d,r,D,t)[0]
            predicted=amp*t*math.exp(-2*r*t)
            if exact>1e-110:
                assert math.isclose(exact,predicted,rel_tol=.1),(exact,predicted)
                checks+=1
        elif r<rc:
            assert 2*r<a
            amp=F/((a-2*r)*(bb-2*r))
            assert amp>0
            checks+=1
        else:
            assert a<2*r<bb
            amp=(bb*V+F/(2*r-a))/(bb-a)
            assert amp>0
            checks+=1
    print(f'PASS: {checks} exact-symbolic, source-equaltime, independent-moment, scalar-ODE and sign checks')

if __name__=='__main__': main()
