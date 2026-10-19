#!/usr/bin/env python3
"""Standalone numerical checks for logarithmic-time quantum reset aging.
Requires numpy and mpmath; numerical tests corroborate, do not replace, proof.
"""
import math
import numpy as np
import mpmath as mp

mp.mp.dps = 45
checks = 0

def f(b, rate, w, time):
    lam = mp.mpc(rate, w)
    a = b * (1j * w) / lam
    return mp.hyp1f1(a, b, -lam * time)

def C(b, rate, w):
    lam = mp.mpc(rate, w)
    a = b * (1j * w) / lam
    return mp.gamma(b) / mp.gamma(b-a) * mp.power(lam, -a)

def asymp_alpha(b, rate, w):
    return b * (1j * w) / mp.mpc(rate, w)

def check(value, tolerance, label):
    global checks
    assert abs(value) < tolerance, (label, value, tolerance)
    checks += 1

# Finite-time Kummer solution against independently integrated memory equation.
def direct_volterra(b, rate, w, T=1.0, steps=10000):
    dt = T/steps
    z = complex(1)
    history = 0j
    for k in range(steps):
        t=k*dt
        # Left rectangular integration for the accumulated memory.
        # At zero the normalized history tends to f(0)=1.
        avg=history*b/(t**b) if t>0 else 1.
        deriv=-(rate+1j*w)*z+rate*avg
        history+=dt*(t**(b-1) if t>0 else (1 if b==1 else 0))*z
        z+=dt*deriv
    return z

for b in (1.0,1.5,2.0,2.75):
    for rate in (0.4,1.1):
        for w in (-2.1,0.0,0.75):
            for T in (0.3,0.7):
                value=complex(f(b, rate, w, T))
                direct=direct_volterra(b,rate,w,T=T,steps=10000)
                check(value-direct,0.007,'separate Volterra time-stepping')
                if w:
                    # Differentiated Kummer ODE verified independently.
                    lam=rate+1j*w
                    g=lambda x: f(b,rate,w,x)
                    ode=T*mp.diff(g,T,2)+(b+lam*T)*mp.diff(g,T)+b*1j*w*g(T)
                    check(ode,mp.mpf('1e-12'),'Kummer equation')

# Diagonal multilevel unitary-phase channels are positive Schur multipliers.
energies=np.array([0.0, 1.0, 2.7, 4.2])
for b in (1.0,1.4,2.6):
    for time in (0.02,0.5,3.0,12.0):
        block=np.array([[complex(f(b,1.0,ej-ek,time)) for ek in energies]
                        for ej in energies],dtype=np.complex128)
        check(np.linalg.norm(block-block.conj().T),1e-11,'Hermitian matrix of phase multipliers')
        check(max(0.0,-np.min(np.linalg.eigvalsh(block))),1e-9,'CP positive Choi support')
        check(np.linalg.norm(np.diag(block)-1),1e-12,'trace preserving')

# Nonunitary finite-time propagator approaches a random-unitary CPTP
# compound-Poisson semigroup as the time origin becomes large.
for b in (1.1,1.8,3.0):
    for w in (-3.0,-0.8,1.25,2.0):
        for u in (0.3,1.1):
            a=asymp_alpha(b,1.0,w)
            target=mp.exp(-a*u)
            # Independent compound-Poisson characteristic function:
            phi=mp.exp(b*u*(1/(1+1j*w)-1))
            check(target-phi,1e-12,'Poisson characteristic function')
            for time,epsilon in ((1000,0.008),(7000,0.002)):
                ratio=f(b,1.0,w,time*mp.exp(u))/f(b,1.0,w,time)
                check(ratio-target,epsilon,'scaled memory propagator')

# Sharp first-order *diamond-norm* convergence for a nondegenerate qubit.
# For the qubit off-diagonal difference map the diamond norm is exactly
# the absolute complex multiplier, independently of an ancilla.
for b in (1.25,1.8,2.5):
    rate,w,u=1.0,2.0,0.7
    lam=complex(rate,w)
    a=complex(asymp_alpha(b,rate,w))
    c=a*(a+1-b)/lam
    k=abs(np.exp(-a*u)*c*(1-np.exp(-u)))
    for time in (1000,3000,10000):
        observed=abs(complex(f(b,rate,w,time*np.exp(u))/f(b,rate,w,time)-mp.exp(-asymp_alpha(b,rate,w)*u)))*time
        check(observed-k,0.005,'sharp qubit diamond coefficient')
        check(max(0,-observed),1e-12,'nonnegative distance')

# Sharp nonzero asymptotic amplitude of a pair of conjugate coherences.
for b in (1.0,1.25,1.5,2.5):
    w=2.0
    sigma=float(mp.re(asymp_alpha(b,1.0,w)))
    amp=abs(C(b,1.0,w))
    for t in (1000,8000):
        check(abs(f(b,1.0,w,t))*t**sigma-amp,0.01,'sharp HS norm asymptotic')
    if b == 1.25:
        check(sigma-1,1e-12,'critical marginal temporal integrability')

print('VERIFY_OK',checks,'ODE/Volterra, CPTP Schur, Poisson log-time, sharp Hilbert-Schmidt exponent')
