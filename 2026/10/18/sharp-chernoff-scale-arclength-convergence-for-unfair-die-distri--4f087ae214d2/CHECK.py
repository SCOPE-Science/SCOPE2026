#!/usr/bin/env python3
"""Independent finite formulas and numerical checks for biased-digit arclength."""
import itertools
import math
from collections import Counter
from math import factorial, sqrt, exp, log, pi


def phi(r):
    # Rationalized to avoid subtractive cancellation near either endpoint.
    return 2.0*r / (1.0+r+math.hypot(1.0, r))


def by_words(p, n):
    q = len(p)
    u = q**(-n)
    return sum(math.hypot(u, math.prod(p[j] for j in w))
               for w in itertools.product(range(q), repeat=n))


def by_multinomial(p, n):
    q = len(p)
    u = q**(-n)
    val = 0.0
    for indices in itertools.combinations_with_replacement(range(q), n):
        counts = Counter(indices)
        multiplicity = factorial(n)
        mass = 1.0
        for j in range(q):
            c = counts[j]
            multiplicity //= factorial(c)
            mass *= p[j]**c
        val += multiplicity*math.hypot(u, mass)
    return val


def deficit(p, n):
    q = len(p)
    u = q**(-n)
    return sum(u*phi(math.prod(q*p[j] for j in w))
               for w in itertools.product(range(q), repeat=n))


def tilt(p):
    q = len(p)
    ell = [log(q*t) for t in p]
    def deriv(s):
        return sum(exp(s*x)*x for x in ell)/q
    lo, hi = 0.0, 1.0
    assert deriv(lo) < 0 and deriv(hi) > 0
    for _ in range(100):
        mid = (lo+hi)/2
        if deriv(mid) < 0:
            lo = mid
        else:
            hi = mid
    s = (lo+hi)/2
    rho = sum(exp(s*x) for x in ell)/q
    weights = [exp(s*x)/(q*rho) for x in ell]
    sigma = sqrt(sum(w*x*x for w,x in zip(weights,ell)))
    assert abs(sum(weights)-1.0)<1e-12
    assert abs(sum(w*x for w,x in zip(weights,ell)))<1e-12
    assert 0<s<1 and 0<rho<1 and sigma>0
    return s, rho, sigma, ell


def beta_constant(s):
    a=(s+1)/2
    b=1-s
    return 2.0**(s-1)*math.exp(math.lgamma(a)+math.lgamma(b)-math.lgamma(a+b))/s


def quad_constant(s):
    # Composite Simpson quadrature of g(x); tail is exponentially small.
    lower, upper, steps = -100.0, 180.0, 56000
    dx=(upper-lower)/steps
    def g(x):
        return exp(-s*x)*phi(exp(x))
    total=g(lower)+g(upper)
    for k in range(1,steps):
        total+=(4 if k%2 else 2)*g(lower+k*dx)
    return dx*total/3


def test():
    examples=[(0.25,0.75),(1/6,1/3,1/2)]
    for p in examples:
        q=len(p)
        ns = list(range(1, 8 if q==2 else 7))
        previous=sqrt(2)
        for n in ns:
            a=by_words(p,n)
            b=by_multinomial(p,n)
            d=deficit(p,n)
            assert abs(a-b)<3e-12, (p,n,a,b)
            assert abs((2-a)-d)<3e-12, (p,n,a,d)
            assert previous<a<2, (p,n,a,previous)
            previous=a
        s,rho,sigma,ell=tilt(p)
        I=beta_constant(s)
        J=quad_constant(s)
        assert abs(I/J-1)<1e-10, (I,J)
        print(f"q={q}, n={ns[0]}..{ns[-1]}, length formulas agree")
        print(f"s*={s:.12f}, rho={rho:.12f}, sigma={sigma:.12f}, I={I:.12f}, integral={J:.12f}")
        if q==2:
            h=abs(ell[1]-ell[0])
            def g(x):
                return exp(-s*x)*phi(exp(x))
            theta=(18*ell[0])%h
            A=h/(sigma*sqrt(2*pi))*sum(g(theta+k*h) for k in range(-200,201))
            assert A>0
            print(f"lattice h={h:.12f}, A(theta_18)={A:.12f}")
        else:
            print('nonlattice: log(3)/log(2) is irrational')
    print('All finite formula, monotonicity, tilt, and beta-integral checks passed.')


if __name__=='__main__':
    test()
