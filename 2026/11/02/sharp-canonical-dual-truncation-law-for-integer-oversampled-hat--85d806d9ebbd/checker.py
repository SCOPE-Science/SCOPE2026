#!/usr/bin/env python3
"""Deterministic supplementary calculations for the triangular-window Gabor theorem.
Only standard-library modules are required. Finite tests are not an infinite proof.
"""
import math
import cmath

assertions = 0

def check(test, msg):
    global assertions
    if not test:
        raise AssertionError(msg)
    assertions += 1


def data(q, t):
    x = (q*t-math.floor(q*t))/q
    c = (q*q-1)/(6*q)+x-q*x*x
    delta = math.sqrt(q*(q-4*c))
    rho = (q-delta)/(q+delta)
    return c, delta, rho


def coeff(q, t, k):
    c, delta, rho = data(q, t)
    return (-rho)**abs(k)/delta


def gamma_cell(q, t, n):
    c, delta, rho = data(q, t)
    if n>=0:
        return (-rho)**n*((1-t)-t*rho)/delta
    m=-n
    return (-rho)**(m-1)*(t-(1-t)*rho)/delta


def c_star(q):
    return (2*q*q+1)/(12*q)


def delta_star(q):
    return math.sqrt((q*q-1)/3)


def rho_star(q):
    delta=delta_star(q)
    return (q-delta)/(q+delta)


def asympt_constant(q):
    rho=rho_star(q)
    delta=delta_star(q)
    peaks=sum((1-(1+rho)*(j+0.5)/q)**2 for j in range(q))
    return math.sqrt(math.pi*c_star(q)*delta/(2*q*q))*peaks/(delta*delta)


def simpson(f, a, b, n=2400):
    check(n%2==0,'Simpson even')
    h=(b-a)/n
    v=f(a)+f(b)
    for k in range(1,n):
        v+=(4 if k%2 else 2)*f(a+h*k)
    return v*h/3


def phi(q, t, theta):
    return sum(abs((1-u)+u*cmath.exp(1j*theta))**2 for u in [((t+j/q)%1.0) for j in range(q)])

for q in [2,3,4,5,6,8,10]:
    A=(q*q-1)/(3*q)
    for t in [0.0,0.107,0.399,0.778,0.999]:
        c, delta, rho=data(q,t)
        check(abs(c-sum(((t+j/q)%1)*(1-((t+j/q)%1)) for j in range(q)))<2e-12,('c_sum',q,t))
        for theta in [0.0, 0.4, 1.3, math.pi]:
            expected=q-2*c+2*c*math.cos(theta)
            check(abs(phi(q,t,theta)-expected)<5e-12,('phi',q,t,theta))
            check(A-1e-10<=expected<=q+1e-10,('frame bounds',q,t,theta))
    t0=0.5/q
    check(abs(phi(q,t0,math.pi)-A)<2e-12,('sharp lower',q))
    check(abs(phi(q,t0,0)-q)<2e-12,('sharp upper',q))
    check(abs(data(q,t0)[0]-c_star(q))<2e-12,('c star',q))
    check(asympt_constant(q)>0,('positive C',q))

for q in [2,3,5]:
    for t in [0.077,0.293,0.714]:
        for k in [-3,-2,-1,0,1,2,3]:
            ntheta=4096
            observed=sum(cmath.exp(1j*k*2*math.pi*l/ntheta)/phi(q,t,2*math.pi*l/ntheta)
                         for l in range(ntheta))/ntheta
            expected=coeff(q,t,k)
            check(abs(observed-expected)<5e-12,('inverse Fourier coefficient',q,t,k))
        for n in [-3,-2,-1,0,1,2,3]:
            vals=[(1-t)*coeff(q,t,n)+t*coeff(q,t,n+1)]
            check(abs(vals[0]-gamma_cell(q,t,n))<1e-13,('dual Fourier',q,t,n))
    for n in [1,3,5]:
        for t in [0.11,0.34,0.68]:
            check(abs(gamma_cell(q,t,-n)-gamma_cell(q,1-t,n-1))<2e-12,('evenness',q,t,n))

for q in [2,3,5,10]:
    c=asympt_constant(q)
    for n in [40,80,140]:
        mass=simpson(lambda t:gamma_cell(q,t,n)**2,0.0,1.0)
        target=c*rho_star(q)**(2*n)/math.sqrt(n)
        check(abs(mass/target-1)<(0.06 if n==40 else 0.035 if n==80 else 0.025),('sharp mass',q,n,mass/target))

for q in [2,3,4,10,50,1000]:
    check(0.2679491924<rho_star(q)<=1/3+1e-12,('rate range',q))
check(abs(rho_star(2)-1/3)<1e-12,'q2 rate')
check(abs(rho_star(100000)-(2-math.sqrt(3)))<1e-10,'q inf rate')
print(f'PASS: {assertions} assertions; q=2 mass constant={asympt_constant(2):.15f}; q=3 mass constant={asympt_constant(3):.15f}')
