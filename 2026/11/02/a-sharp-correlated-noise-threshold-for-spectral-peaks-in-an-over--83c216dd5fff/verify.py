#!/usr/bin/env python3
"""Numerical cross-checks for an exactly solvable two-component Langevin spectrum.

Requires Python 3, NumPy, and SciPy. No network or external data are used.
"""
import math
import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve_continuous_lyapunov, expm


def formula(a,b,k,dx,dy,rho,w):
    t=k*math.sqrt(dy/dx)
    c=b*b+t*t+2*b*t*rho
    return 2*dx*(w*w+c)/((a*a+w*w)*(b*b+w*w))


def matrix_spectrum(a,b,k,dx,dy,rho,w):
    A=np.array([[-a,k],[0.,-b]])
    D=np.array([[dx,rho*math.sqrt(dx*dy)],[rho*math.sqrt(dx*dy),dy]])
    H=np.linalg.inv(1j*w*np.eye(2)-A)
    return float(np.real((H @ (2*D) @ H.conj().T)[0,0]))


def peak_frequency(a,b,k,dx,dy,rho):
    t=k*math.sqrt(dy/dx)
    c=b*b+t*t+2*b*t*rho
    threshold=a*a*b*b/(a*a+b*b)
    if c>=threshold:
        return 0.0
    y=-c+math.sqrt((a*a-c)*(b*b-c))
    return math.sqrt(y)


def covariance_formula(a,b,k,dx,dy,rho,tau):
    t=k*math.sqrt(dy/dx)
    c=b*b+t*t+2*b*t*rho
    if abs(a-b)<1.e-9:
        z=a
        return dx*math.exp(-z*tau)*((z*z+c)+(c-z*z)*z*tau)/(2*z**3)
    A=(c-a*a)/(b*b-a*a)
    B=(b*b-c)/(b*b-a*a)
    return dx*(A/a*math.exp(-a*tau)+B/b*math.exp(-b*tau))


def full_covariance(a,b,k,dx,dy,rho,tau):
    A=np.array([[-a,k],[0.,-b]])
    D=np.array([[dx,rho*math.sqrt(dx*dy)],[rho*math.sqrt(dx*dy),dy]])
    S=solve_continuous_lyapunov(A,-2*D)
    return float((expm(A*tau)@S)[0,0])


def run():
    rng=np.random.default_rng(925171)
    checks=0
    for i in range(500):
        a,b,k=np.exp(rng.uniform(-1,1,3))
        if i%13==0: b=a
        dx,dy=np.exp(rng.uniform(-1,1,2))
        rho=rng.uniform(-0.98,0.98)
        w=float(np.exp(rng.uniform(-2,2)))
        x=formula(a,b,k,dx,dy,rho,w)
        y=matrix_spectrum(a,b,k,dx,dy,rho,w)
        assert np.isclose(x,y,rtol=1.e-11,atol=1.e-12),(i,'spectrum',x,y)
        checks+=1
        tau=float(rng.uniform(0,3))
        u=covariance_formula(a,b,k,dx,dy,rho,tau)
        v=full_covariance(a,b,k,dx,dy,rho,tau)
        assert np.isclose(u,v,rtol=5.e-10,atol=1.e-11),(i,'covariance',u,v)
        checks+=1
        opt=peak_frequency(a,b,k,dx,dy,rho)
        if opt>0:
            assert formula(a,b,k,dx,dy,rho,opt)>formula(a,b,k,dx,dy,rho,0),i
            for f in [0.1,0.6,1.4,3.,7.]:
                assert formula(a,b,k,dx,dy,rho,opt) >= formula(a,b,k,dx,dy,rho,opt*f)-1e-12,i
                checks+=1
        else:
            for f in [0.2,1,3]:
                assert formula(a,b,k,dx,dy,rho,0)>formula(a,b,k,dx,dy,rho,f)-1e-12,i
                checks+=1
        # Correlation gate is algebraically equivalent to optimized feasibility.
        rhocmax=-b/math.sqrt(a*a+b*b)
        tstar=b*b/math.sqrt(a*a+b*b)
        rhoc=(a*a*b*b/(a*a+b*b)-b*b-tstar*tstar)/(2*b*tstar)
        assert np.isclose(rhoc,rhocmax,rtol=1e-13)
        checks+=1

    a=b=k=dx=dy=1.0
    rho=-0.8
    assert abs(peak_frequency(a,b,k,dx,dy,rho)-math.sqrt(0.2))<1e-12
    assert abs(formula(a,b,k,dx,dy,rho,math.sqrt(0.2))-5.0/6.0)<1e-12
    print(f'PASS: {checks} randomized direct-resolvent, Lyapunov, and extremum comparisons')

if __name__=='__main__':
    run()
