#!/usr/bin/env python3
"""Numerical cross-checks for a detuned lossy two-oscillator pulse model."""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def modes(g, loss, detuning):
    z = np.sqrt(g*g + (detuning/2 - 1j*loss/4)**2)
    if z.real < 0:
        z = -z
    return z


def quantities(g, loss, detuning):
    z = modes(g, loss, detuning)
    return loss/2, 2*abs(z.imag), 2*z.real


def analytic_energy(t, g, loss, detuning, pulse=1.0):
    z = modes(g, loss, detuning)
    return pulse*pulse * (g*g/abs(z)**2) * math.exp(-loss*t/2) * abs(np.sin(z*t))**2


def matrix_energy(t, g, loss, detuning, pulse=1.0):
    # Frequencies relative to their mean; only the charger's energy is lost.
    h = np.array([[detuning/2 - 0.5j*loss, g], [g, -detuning/2]], dtype=complex)
    state = expm(-1j*h*t) @ np.array([-1j*pulse, 0], dtype=complex)
    return abs(state[1])**2


def derivative_factor(t, alpha, beta, omega):
    return (alpha*np.cos(omega*t) + omega*np.sin(omega*t)
            - alpha*np.cosh(beta*t) + beta*np.sinh(beta*t))


def cutoff(g, loss, detuning):
    alpha,beta,omega = quantities(g,loss,detuning)
    assert 0 < beta < alpha and omega > 0
    R = math.hypot(alpha, omega)
    return (math.atanh(beta/alpha)
            + math.acosh(R / math.sqrt(alpha*alpha-beta*beta)))/beta


def count_maxima(g, loss, detuning):
    alpha,beta,omega = quantities(g,loss,detuning)
    t_end = cutoff(g,loss,detuning)
    # Beyond cutoff there cannot be any further stationary maximum.
    xs = np.linspace(1e-8,t_end, int(max(4000,omega*t_end*80/math.pi)))
    vs = derivative_factor(xs,alpha,beta,omega)
    ixs = np.flatnonzero(vs[:-1]*vs[1:]<0)
    roots = [brentq(derivative_factor,xs[i],xs[i+1],args=(alpha,beta,omega),xtol=1e-11)
             for i in ixs]
    return sum(derivative_factor(t-1e-4,alpha,beta,omega)>0 and
               derivative_factor(t+1e-4,alpha,beta,omega)<0 for t in roots)


def main():
    # Compare matrix exponential with independently computed closed form.
    n = 0
    for g in (0.27,0.4,0.7,1.0,1.8):
        for loss in (0.4,1.0):
            if g <= loss/4: continue
            for detuning in (-1.2,-0.25,0,0.03,0.4,1.2):
                for t in (0.1,0.8,1.7,3.3,8.0):
                    a = analytic_energy(t,g,loss,detuning)
                    b = matrix_energy(t,g,loss,detuning)
                    assert abs(a-b) < 2e-12*(1+a+b), (g,loss,detuning,t,a,b)
                    n+=1
    print('matrix_vs_analytic:',n,'tests PASS')
    # Envelope bound and absence of post-cutoff turning points.
    n=0
    for g in (0.4,0.7,1.,2.):
        for detuning in (0.01,0.05,0.2,0.5,1.0):
            T=cutoff(g,1.0,detuning)
            al,be,om=quantities(g,1.0,detuning)
            for t in (T+1e-5,T+0.3,T+4,T+12):
                assert derivative_factor(t,al,be,om)<1e-9
                n+=1
    print('envelope_post_cutoff:',n,'tests PASS')
    # Deterministic count and weak-detuning coefficient.
    g=loss=1.
    G=math.sqrt(g*g-loss*loss/16)
    constant=4*G*G*math.acosh(4*g/loss)/(math.pi*loss)
    for delta in (0.1,0.05,0.02,0.01):
        N=count_maxima(g,loss,delta)
        rel=abs(delta*N/constant-1)
        assert rel < 0.065, (delta,N,constant,rel)
        print('detuning',delta,'maxima',N,'scaled',round(delta*N,8),
              'target',round(constant,8),'relative_error',round(rel,5))
    # No new zeros after t=0 at nonzero detuning.
    for g in (0.5,1.):
        for delta in (0.01,0.5,2.0):
            for t in (0.1,1.,2.,5.,20.):
                assert analytic_energy(t,g,1.,delta)>0
    print('all checks PASS')

if __name__=='__main__': main()
