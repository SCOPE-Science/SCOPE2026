#!/usr/bin/env python3
"""Independent numerical checks of the half-line sink asymptotic formula.

Usage: python verify.py. Requires numpy and scipy. Finite checks only;
the uniform late-time proof is analytic and not certified by this program.
"""
import numpy as np
from scipy.special import jv
from scipy.integrate import quad

PI = np.pi

def exact_edge_amplitude(m, eta, x):
    # Riberi's exact Bessel representations; x = Omega*t.
    direct = (1j ** (m-1)) * np.exp(-1j*x) * (2*m/x) * jv(m,x)
    cutoff = int(x+120)
    if eta <= 1:
        r = np.arange(cutoff)
        series = np.sum((-eta)**r * (m+1+r)/x * jv(m+1+r,x))
        return direct - 2*eta*(1j**(m-1))*np.exp(-1j*x)*series
    r = np.arange(1,cutoff)
    series = np.sum((-1.)**(r+1)*eta**(1.-r)*(m+1-r)/x*jv(m+1-r,x))
    pole = (1+eta**(-2)) * (-1j/eta)**(m-1) * np.exp(-1j*x-x*(eta-1/eta)/2)
    return direct+2*(1j**(m+1))*np.exp(-1j*x)*series+pole

def edge_asymptotic(m,eta,x):
    d=(m-1j*eta*(m-1))/(1-1j*eta)**2
    return np.sqrt(2/PI)*x**(-1.5)*(np.exp(-.75j*PI)*d+(-1)**(m-1)*np.exp(.75j*PI)*d.conjugate()*np.exp(-2j*x))

def tail_coefficient(m,eta,omega=1):
    return 2*eta/(PI*omega**2)*(m*m+eta**2*(m-1)**2)/(1+eta**2)**2

def tail_derivative(m,eta,omega=1):
    return 2/(PI*omega**2)*(m*m-3*(2*m-1)*eta**2-(m-1)**2*eta**4)/(1+eta**2)**3

def tail_maximizer(m):
    if m==1:return 1/np.sqrt(3)
    b=(m-1)**2
    x=2*m*m/(np.sqrt(9*(2*m-1)**2+4*m*m*b)+3*(2*m-1))
    # Rationalized positive root formula, avoiding cancellation.
    return np.sqrt(x)

def absorption_probability(m,eta):
    term1=quad(lambda k: np.sin(k)/(1+eta**2+2*eta*np.sin(k)),0,PI,epsabs=1e-12)[0]
    term2=quad(lambda q: q**(2*m-2)*(1-q*q)/(1+eta*eta*q*q),0,1,epsabs=1e-12)[0]
    return 2*eta/PI*(term1+term2)

def absorption_slope_at_one(m):
    return 2/PI*quad(lambda q: q**(2*m-2)*(1-q*q)**2/(1+q*q)**2,0,1,epsabs=1e-12)[0]

checks=0
for m in (1,2,4):
    for eta in (.4,.8,1.,1.3,2.5):
        for x in (390.37,890.37):
            actual=exact_edge_amplitude(m,eta,x)
            predicted=edge_asymptotic(m,eta,x)
            # Absolute scaled error remains meaningful near oscillation zeros.
            error=x**1.5*abs(actual-predicted)
            assert error<.22,(m,eta,x,error)
            checks+=1
        c=tail_coefficient(m,eta)
        assert c>0
        eps=1e-5
        num=(tail_coefficient(m,eta+eps)-tail_coefficient(m,eta-eps))/(2*eps)
        assert np.isclose(num,tail_derivative(m,eta),atol=3e-8,rtol=2e-7)
        checks+=1
    star=tail_maximizer(m)
    assert 0<star<1
    assert np.isclose(tail_derivative(m,star),0,atol=1e-12)
    assert tail_derivative(m,max(star-.08,.001))>0
    assert tail_derivative(m,star+.08)<0
    checks+=4
    d=absorption_slope_at_one(m)
    num=(absorption_probability(m,1+1e-4)-absorption_probability(m,1-1e-4))/(2e-4)
    assert d>0 and np.isclose(num,d,atol=1e-8)
    assert tail_derivative(m,1)<0
    checks+=3
print(f'PASS: {checks} analytic-identity and finite-amplitude checks.')
