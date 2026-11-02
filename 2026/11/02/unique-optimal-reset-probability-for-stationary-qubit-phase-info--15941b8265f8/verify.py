#!/usr/bin/env python3
"""Reproduce stationary reset-qubit Fisher calculations and numerical cross-checks.

Requires Python 3, NumPy, and SymPy. All symbolic equalities are exact;
finite-difference checks are corroborating rather than proof of global claims.
"""
import math
import numpy as np
import sympy as sp

x, t, p = sp.symbols('x t p', real=True)
A = x*x + 4*t*(1+x)
F_odds = x*x*(A+x*x*(1+x)*(1-t))/A**3
P = (t-1)*x**5 - 2*(4*t*t-5*t+2)*x**4 + 8*t*(2-3*t)*x**3 + 16*t*(1-t)*x**2 + 32*t*t*x + 32*t*t
assert sp.cancel(sp.diff(F_odds,x)-x*P/A**4) == 0
q=1-p
Delta=p*p+4*q*t
F_reset=p*p*q*q/Delta**2+p**4*q*(1-t)/Delta**3
assert sp.cancel(F_odds-F_reset.subs({p:x/(1+x)})) == 0
assert sp.cancel(F_odds.subs(t,1)-x*x/(x+2)**4)==0
assert F_odds.subs({x:sp.Integer(2),t:sp.Integer(1)})==sp.Rational(1,64)
k2=(1+sp.sqrt(3))/2
constant=sp.simplify(k2*(2*k2+1)/(k2+1)**3)
assert constant==2*sp.sqrt(3)/9

def rho(reset,theta):
    phase=np.exp(1j*theta)
    z=reset/(1-(1-reset)*phase)
    return np.array([[0.5,z/2],[np.conj(z)/2,0.5]],dtype=complex)

def direct_sld_qfi(reset,theta):
    h=1.0e-6
    mat=rho(reset,theta)
    deriv=(rho(reset,theta+h)-rho(reset,theta-h))/(2*h)
    eigenvalues, unitary=np.linalg.eigh(mat)
    matrix=unitary.conj().T @ deriv @ unitary
    return float(sum(2*abs(matrix[j,k])**2/(eigenvalues[j]+eigenvalues[k])
                     for j in range(2) for k in range(2)).real)

def analytical_qfi(reset,theta):
    tau=math.sin(theta/2)**2
    dd=reset**2+4*(1-reset)*tau
    return reset**2*(1-reset)**2/dd**2+reset**4*(1-reset)*(1-tau)/dd**3

def poly(xx,tt):
    return float(P.subs({x:xx,t:tt}))

def optimum(tt):
    lo,hi=0.0,1.0
    while poly(hi,tt)>0:
        hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if poly(mid,tt)>0:
            lo=mid
        else:
            hi=mid
    xx=(lo+hi)/2
    return xx/(1+xx),xx

checked=0
for reset in (0.05,0.21,0.46,0.79):
    for theta in (0.12,0.4,0.9,1.8,math.pi,4.3):
        mat=rho(reset,theta)
        gate=np.diag([np.exp(0.5j*theta),np.exp(-0.5j*theta)])
        target=np.full((2,2),0.5,dtype=complex)
        update=reset*target+(1-reset)*gate@mat@gate.conj().T
        assert np.max(np.abs(update-mat))<1e-13
        measured=direct_sld_qfi(reset,theta)
        analytic=analytical_qfi(reset,theta)
        assert abs(measured-analytic)<2e-6*max(1,analytic),(reset,theta,measured,analytic)
        checked+=1

for tau in (0.0001,0.01,0.25,0.5,0.75,1.0):
    reset,xx=optimum(tau)
    assert 0<reset<1
    assert poly(xx*.999,tau)>0 and poly(xx*1.001,tau)<0
    derivative_samples=[(v,float(F_odds.subs({x:v,t:tau}))) for v in
                       (0.01*xx,0.1*xx,0.5*xx,xx,2*xx,5*xx,10*xx)]
    assert derivative_samples[3][1]==max(z[1] for z in derivative_samples)
    print('t=',tau,'p_opt=',format(reset,'.12g'),'Fmax=',format(derivative_samples[3][1],'.12g'))

print('off-resonance checks:',checked)
for delta in (0.03,0.01,0.003,0.001):
    reset,xx=optimum(math.sin(delta/2)**2)
    scale=reset/delta
    qfi_scaled=delta*delta*analytical_qfi(reset,delta)
    print('detuning=',delta,'p_opt/detuning=',scale,'detuning^2 Fmax=',qfi_scaled)
    assert abs(scale-math.sqrt(float(k2)))<0.06
    assert abs(qfi_scaled-float(constant))<0.015
print('all exact identities and independent finite-matrix checks passed')
