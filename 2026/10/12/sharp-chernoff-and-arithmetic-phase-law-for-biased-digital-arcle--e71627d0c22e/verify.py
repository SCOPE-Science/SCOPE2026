#!/usr/bin/env python3
"""Finite computational checks for digit-CDF polygonal arclength asymptotics.

Uses only the Python standard library. Tests are finite diagnostics; the
all-order proof is in RESULT.md.
"""
import cmath
import itertools
import math


def direct_length(probs, n):
    q = len(probs)
    dx = q ** (-n)
    return math.fsum(math.hypot(dx, math.prod(probs[i] for i in word))
                     for word in itertools.product(range(q), repeat=n))


def binary_grouped_length(p, n):
    r = 1.0 - p
    return math.fsum(math.comb(n,k) * math.hypot(2.0 ** (-n), p ** k * r ** (n-k))
                     for k in range(n+1))


def f_log(s):
    """Evaluate 1 + exp(s) - hypot(1,exp(s)) without cancellation."""
    if s >= 0:
        y = math.exp(-s)
        return 2.0 / (1.0 + y + math.hypot(1.0, y))
    y = math.exp(s)
    return 2.0*y/(1.0+y+math.hypot(1.0,y))


def binary_params(p):
    assert 0.5 < p < 1.0
    a,b=math.log(2*p),math.log(2*(1-p))
    h=a-b
    alpha=-b/h
    theta=math.log(alpha/(1-alpha))/h
    z=(math.exp(theta*a)+math.exp(theta*b))/2
    assert 0.0 < theta < 1.0 and 0.0 < z < 1.0
    return h,alpha,theta,z


def kernel(s, theta):
    if s >= 0:
        e = math.exp(-s)
        return 2.0*math.exp(-theta*s)/(1.0+e+math.hypot(1.0,e))
    e = math.exp(s)
    return 2.0*math.exp((1.0-theta)*s)/(1.0+e+math.hypot(1.0,e))


def phase(p, u, cutoff=100):
    h, alpha, theta, z=binary_params(p)
    return math.fsum(kernel(h*(j-u),theta) for j in range(-cutoff,cutoff+1))


def tilted_defect(p,n):
    h, alpha, theta, z=binary_params(p)
    logalpha=math.log(alpha)
    logbeta=math.log1p(-alpha)
    expect=math.fsum(math.exp(math.lgamma(n+1)-math.lgamma(k+1)-math.lgamma(n-k+1)
                              +k*logalpha+(n-k)*logbeta)*
                     kernel(h*(k-n*alpha),theta) for k in range(n+1))
    return z**n * expect


def checks():
    count=0
    for p in [0.51, 0.625, 0.75, 0.9]:
        for n in range(1,11):
            a=direct_length((p,1-p),n)
            b=binary_grouped_length(p,n)
            assert abs(a-b) < 6e-13, (p,n,a,b)
            count+=1
    print('Binary geometric versus binomial length identity:', count, 'tests PASS')
    count=0
    for probs in [(0.2,0.3,0.5),(0.6,0.25,0.15),(0.1,0.2,0.3,0.4)]:
        q=len(probs)
        for n in range(1,6):
            dx=q**(-n)
            masses=[math.prod(probs[j] for j in word)
                    for word in itertools.product(range(q),repeat=n)]
            defect=math.fsum(dx+t-math.hypot(dx,t) for t in masses)
            overlap=math.fsum(min(dx,t) for t in masses)
            assert (2-math.sqrt(2))*overlap - 1e-11 <= defect <= overlap+1e-11
            assert abs(defect-(2-direct_length(probs,n))) <= 2e-11
            count+=1
    print('Arclength defect and product-overlap comparison:',count,'tests PASS')
    p=0.9
    h,alpha,theta,z=binary_params(p)
    print('p=0.9: alpha=%.13f theta=%.13f z=%.13f' % (alpha,theta,z))
    count=0
    for n in [20,50,100,200,500,1000,2000]:
        defect=tilted_defect(p,n)
        u=(n*alpha)%1
        approximation=z**n*phase(p,u)/math.sqrt(2*math.pi*n*alpha*(1-alpha))
        relative=defect/approximation - 1
        if n>=500:
            assert abs(relative)<0.015,(n,relative)
        print('n=%d: length_defect=%.12g, asymptotic_relative_error=%+.6g' %
              (n, defect, relative))
        count+=1
    print('Tilted-length and phase asymptotic:',count,'tests PASS')
    samples=128
    values=[phase(p,j/samples,cutoff=75) for j in range(samples)]
    harmonic=sum(values[j]*cmath.exp(-2j*math.pi*j/samples)
                 for j in range(samples))/samples
    print('phase_min=%.12f phase_max=%.12f first_Fourier_magnitude=%.10g' %
          (min(values),max(values),abs(harmonic)))
    assert min(values)>0 and max(values)-min(values)>.001
    assert abs(harmonic) > .001
    print('Periodic profile nonconstancy diagnostic: PASS')


if __name__=='__main__':
    checks()
