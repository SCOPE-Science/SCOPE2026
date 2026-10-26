#!/usr/bin/env python3
"""Reproducible finite checks for the Brownian partial-reset stationary law.

Run with standard Python 3; all core checks use exact rational arithmetic.
The asymptotic Fourier/derivative claims require the accompanying proof.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import isclose, log

checks = 0

def check(flag, msg):
    global checks
    assert flag, msg
    checks += 1


def deterministic_product(t, q, depth):
    result = F(1)
    z = F(t)
    for _ in range(depth):
        result /= 1 + z*z
        z *= q
    return result


def path_average(t, values, weights, depth):
    """Direct independent-mark enumeration of the finite perpetuity CF."""
    assert len(values) == len(weights) and sum(weights) == 1
    answer = F(0)
    # The N Laplace summands involve N-1 independent marks.
    def descend(step, multiplier, weight, cf):
        nonlocal answer
        cf /= 1 + (t * multiplier)**2
        if step + 1 == depth:
            answer += weight * cf
            return
        for q,p in zip(values,weights):
            descend(step+1, multiplier*q, weight*p, cf)
    descend(0, F(1), F(1), F(1))
    return answer


def recursive_cf(t, values, weights, depth):
    @lru_cache(None)
    def f(s, n):
        if n == 0:
            return F(1)
        return sum((w*f(s*q,n-1) for q,w in zip(values, weights)), F(0))/(1+s*s)
    return f(F(t), depth)


def stationary_even_moments(qvalues, weights, depth=8):
    e = lambda exponent: sum((w*q**exponent for q,w in zip(qvalues,weights)), F(0))
    m=[F(1)]
    for k in range(1,depth+1):
        m.append(F((2*k)*(2*k-1))*m[-1]/(1-e(2*k)))
    return m

# Fixed-reset benchmark: characteristic product equals explicit finite sum law.
for q in [F(1,3), F(1,2), F(3,4)]:
    for t in [F(1,2), F(1), F(3), F(5,2)]:
        for depth in range(1,9):
            check(path_average(t,[q],[F(1)],depth)==deterministic_product(t,q,depth),
                "deterministic finite-product law")

# A genuinely random contraction: independent-mark enumeration and recursive CF.
values=[F(1,3),F(1,2)]
weights=[F(1,100),F(99,100)]
for t in [F(1,2), F(1), F(2), F(3)]:
    for depth in range(1,9):
        enumerated=path_average(t,values,weights,depth)
        recursive=recursive_cf(t,values,weights,depth)
        check(enumerated==recursive,"random-contraction renewal recursion")
        check(deterministic_product(t,max(values),depth)<=enumerated<=
              deterministic_product(t,min(values),depth),
              "deterministic extreme-contraction sandwich")

# Moment recurrence and expectation bounds, with dimensional normalization D=r=1.
for vals,probs in [([F(1,2)],[F(1)]),
                    ([F(1,3),F(1,2)],[F(1,100),F(99,100)]),
                    ([F(0),F(1,2)],[F(1,5),F(4,5)])]:
    moms=stationary_even_moments(vals,probs)
    for k in range(1,len(moms)):
        contraction=sum((w*q**(2*k) for q,w in zip(vals,probs)),F(0))
        check((1-contraction)*moms[k]==(2*k)*(2*k-1)*moms[k-1],
              "stationary generator identity")
        check(moms[k]>0,"positivity of stationary moments")

# Presence of a zero reset mark creates the one-sided derivative jump -p0 r/D.
# For t large, Fourier's t^2 phi(t) tends to the zero-reset probability (r/D=1).
for depth in range(2,9):
    phi=recursive_cf(F(500),[F(0),F(1,2)],[F(1,5),F(4,5)],depth)
    check(abs(F(500*500)*phi-F(1,5))<F(1,1000),
          "stationary Fourier cusp coefficient")

# The squared-product quadratic logarithmic scale has coefficient 1/(-log q).
# This is only a numerical sanity check, not an asymptotic certificate.
for q in [0.5,1/3]:
    h=-log(q)
    for y in [8.,10.,12.,14.]:
        n=int(y/h)+80
        v= -sum(__import__('math').log1p(__import__('math').exp(2*(y-j*h)))
                for j in range(n))
        check(abs(v + y*y/h)/y < 5.0,
              "finite Fourier log-product quadratic estimate")

print(f"PASS: {checks} exact rational and numerical assertions")
print("Scope: finite characteristic-function identities, moment recurrences, ")
print("and Fourier leading-constant sanity checks. The infinite limit is analytic.")
