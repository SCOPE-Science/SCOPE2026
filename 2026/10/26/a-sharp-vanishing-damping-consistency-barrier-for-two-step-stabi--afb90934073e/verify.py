#!/usr/bin/env python3
"""Standalone checks for the two-stage damped Chebyshev forcing theorem."""
from fractions import Fraction as F
from math import sqrt, exp, isclose

checks = 0

def check(statement, context):
    global checks
    checks += 1
    if not statement:
        raise AssertionError(context)

def exact_from_q(q):
    e = (3*q*q+1)/(6-2*q)
    w = (1-q)/2
    c0 = (q+e)/(1-e)
    c1 = (q+2*e+1)/(2*(1-e))
    E = (q-1)/3 + w*(c0*c0+c1*c1)
    return e,w,c0,c1,E

def floating(epsilon):
    eta = 1-epsilon
    e = eta*eta
    q = (sqrt(e*e+18*e-3)-e)/3
    w = (1-q)/2
    c0 = (q+e)/(1-e)
    c1 = (q+2*e+1)/(2*(1-e))
    E = (q-1)/3 + w*(c0*c0+c1*c1)
    return e,q,w,c0,c1,E

def error_exact(N,T,epsilon):
    h = T/N
    e,q,w,c0,c1,E = floating(epsilon)
    defect = h**3*E
    difference = 0.0
    error = 0.0
    for _ in range(1,N):
        difference=q*difference+defect
        error+=difference
    return error

# Rational exact identities: no floating-point tolerance here.
for denominator in [3,5,7,10,20,50,100,200,1000]:
    for numerator in [1,denominator-1]:
        q = F(numerator,denominator)
        if not (F(0)<q<F(1)):
            continue
        e,w,c0,c1,E=exact_from_q(q)
        check(F(0)<e<F(1),"admissible exact e")
        check(3*q*q+2*e*q+1-6*e==0,"order polynomial")
        check(q+2*w==1,"constant forcing order")
        check(2*w*(c0+c1)==1+q,"linear forcing order")
        check(c1-c0==(1-q)/(2*(1-e)),"stage difference")
        check(E==(q-1)/3+w*(c0*c0+c1*c1),"local defect identity")

# Reconstruct the published two-stage recurrence, independently of the reduced formula.
for epsilon in [0.05,0.025,0.0125]:
    e,q,w,c0,c1,E=floating(epsilon)
    omega=sqrt((1+q/e)/2)
    cheb=2*omega**2-1
    alpha=(1+q)/(1+cheb)
    delta=alpha-e
    beta=2*omega*(1-q)/(1-e)
    b=delta*cheb
    ta=alpha/delta
    tm1=beta/(4*omega)
    m2=2*omega**2/cheb
    tm2=beta*omega/(2*cheb)
    check(isclose(ta-1,c0,rel_tol=1e-11),"first source stage time")
    check(isclose(ta-1+tm1,c1,rel_tol=1e-11),"second source stage time")
    for h in [0.001,0.1]:
        for tn in [0.0,1.0]:
            yn=tn**3/3
            ym=(tn-h)**3/3
            g=lambda t:t*t
            v0=ta*yn+(1-ta)*ym
            v1=v0+h*tm1*g(tn+c0*h)
            v2=m2*v1+(1-m2)*v0+h*tm2*g(tn+c1*h)
            direct=alpha*yn+b*v2
            reduced=(1+q)*yn-q*ym+h*w*(g(tn+c0*h)+g(tn+c1*h))
            exact=(tn+h)**3/3
            check(isclose(direct,reduced,abs_tol=3e-10,rel_tol=3e-10),"source stage reconstruction")
            check(isclose(reduced-exact,h**3*E,abs_tol=3e-10,rel_tol=3e-10),"local defect reconstruction")

# Endpoint error is an exact discrete summation identity.
for epsilon in [0.1,0.05,0.02,0.007]:
    for N in [2,3,7,11,31,101,300]:
        T=1.0
        q=floating(epsilon)[1]
        E=floating(epsilon)[-1]
        h=T/N
        summation=h**3*E/(1-q)*((N-1)-q*(1-q**(N-1))/(1-q))
        recursive=error_exact(N,T,epsilon)
        check(isclose(summation,recursive,rel_tol=5e-9,abs_tol=5e-9),"finite horizon formula")

# Three asymptotic limits with fixed T=1; these are tests, not the infinite proofs.
for N in [2000,4000]:
    h=1/N
    critical=error_exact(N,1.0,h)
    check(abs(critical-exp(-1))<0.005,"critical nonzero bias")
for N in [2000,4000]:
    h=1/N
    epsilon=sqrt(h)
    scaled=error_exact(N,1.0,epsilon)*(epsilon/h)**2
    check(abs(scaled-1)<0.1,"above-threshold rate")
for N in [200,400]:
    h=1/N
    epsilon=h*h
    scaled=error_exact(N,1.0,epsilon)*epsilon/h
    check(abs(scaled-0.5)<0.03,"below-threshold divergence")
for epsilon in [0.005,0.002,0.001]:
    e,q,w,c0,c1,E=floating(epsilon)
    check(abs(epsilon*E-1)<0.01,"singular local constant")
    check(abs(epsilon*c0-1)<0.01,"first stage blowup")
    check(abs(epsilon*c1-1)<0.01,"second stage blowup")

print("PASS: %d standalone exact-algebra and deterministic numerical assertions"%checks)
