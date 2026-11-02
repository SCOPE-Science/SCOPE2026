#!/usr/bin/env python3
"""Finite checks for the exact trace-matched isotropic inverse KL envelope.
These checks supplement, but do not replace, the analytic proof in RESULT.md.
Requires only the Python 3 standard library.
"""
import math
import random
from fractions import Fraction

SEED = 174729
RNG = random.Random(SEED)


def direct_per_dim(eigenvalues):
    k = len(eigenvalues)
    mean_t = math.fsum(eigenvalues) / k
    mean_inv = math.fsum(1.0/t for t in eigenvalues) / k
    return (mean_t*mean_inv - 1.0 - math.log(mean_inv)
            - math.fsum(math.log(t) for t in eigenvalues)/k)/2.0


def endpoint_per_dim(k, cond, j):
    p = j / k
    return (p*(1-p)*(cond-1)**2/cond
            - math.log1p(-p*(1-1/cond)) - p*math.log(cond))/2


def envelope(k, cond):
    if cond == 1:
        return 0.0, 0
    candidates = [(endpoint_per_dim(k, cond, j), j)
                  for j in range(1, k)]
    return max(candidates)


def fprime(p, cond):
    c = 1-1/cond
    aa = (cond-1)**2/cond
    return aa*(1-2*p)+c/(1-c*p)-math.log(cond)


def fraction_convexity():
    tests = 0
    for k in range(2, 15):
        for _ in range(200):
            t = Fraction(RNG.randint(1, 31), RNG.randint(1, 29))
            others = [Fraction(RNG.randint(1, 31), RNG.randint(1, 29))
                      for _ in range(k-1)]
            s = sum(others)
            r = sum((1/u for u in others), Fraction(0))
            # Exactly t^2 * second derivative of 2*KL/k in one entry.
            curvature = 2*s/(k*k*t) + (r*t)**2/(r*t+1)**2 - Fraction(k-1,k)
            assert curvature > 0, (k,t,others,curvature)
            tests += 1
    return tests


def random_envelope():
    tests = 0
    for k in range(2, 21):
        for _ in range(220):
            cond = math.exp(RNG.uniform(math.log(1.1), math.log(100.0)))
            # Fix the exact extrema to test the fixed-condition-number case.
            eigenvalues = [1.0, cond] + [cond**RNG.random()
                                           for __ in range(k-2)]
            true_kl = direct_per_dim(eigenvalues)
            sharp, j = envelope(k, cond)
            assert true_kl >= -1e-12
            assert true_kl <= sharp + 2e-11, (k, cond, true_kl, sharp)
            endpoint = [1.0]*(k-j) + [cond]*j
            assert abs(direct_per_dim(endpoint)-sharp) < 2e-11
            tests += 1
    return tests


def one_peak():
    tests = 0
    for k in range(2, 25):
        for cond in [1.01,1.1,1.5,2.0,3.0,5.0,10.0,100.0,1000.0]:
            assert fprime(0,cond)>0 and fprime(1,cond)<0
            lo,hi=0.0,1.0
            for _ in range(80):
                mid=(lo+hi)/2
                if fprime(mid,cond)>0: lo=mid
                else: hi=mid
            pp=(lo+hi)/2
            best,j=envelope(k,cond)
            admissible={max(1,min(k-1,math.floor(k*pp))),
                        max(1,min(k-1,math.ceil(k*pp)))}
            assert j in admissible, (k,cond,pp,j,admissible)
            tests+=1
    return tests


def diagnostic():
    for k,cond in [(2,2),(4,10),(10,3),(100,100)]:
        kl,j=envelope(k,cond)
        print(f'k={k}, condition={cond:g}, high-multiplicity={j}, '
              f'KL_per_dimension={kl:.12g}, previous_upper_bound={(cond-1)**2/2:.12g}')


if __name__=='__main__':
    count1=fraction_convexity()
    count2=random_envelope()
    count3=one_peak()
    diagnostic()
    print('PASS: exact-rational coordinate-curvature tests:',count1)
    print('PASS: random spectrum and attainment checks:',count2)
    print('PASS: unimodality and integer-optimum checks:',count3)
    print('PASS: total checks:',count1+count2+count3)
