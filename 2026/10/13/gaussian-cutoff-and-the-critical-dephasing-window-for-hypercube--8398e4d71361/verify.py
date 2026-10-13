#!/usr/bin/env python3
"""Finite-case checks for sharp mixing of independently dephased hypercube quantum walks.

Standard-library-only; numerical checks are not substitutes for the analytic limit proof.
"""
import math


def bias(n, k, p, t):
    """Exact one-coordinate position bias from the damped Bloch equation."""
    assert n >= 1 and k > 0 and p >= 4*k and t >= 0
    s = t/n
    if p == 4*k:
        u = 2*k*s
        return math.exp(-u)*(1+u)
    alpha = math.sqrt(p*p-16*k*k)
    return math.exp(-p*s/2)*(math.cosh(alpha*s/2)+p/alpha*math.sinh(alpha*s/2))


def critical_root(n):
    """Positive solution of (1+u)exp(-u)=n**(-1/2)."""
    assert n > 1
    lo, hi = 0.0, max(3.0, math.log(n)+10.0)
    for _ in range(90):
        mid=(lo+hi)/2
        if (1+mid)*math.exp(-mid)>n**(-0.5): lo=mid
        else: hi=mid
    return (lo+hi)/2


def critical_center(n, k, c, theta=0.0):
    g = math.sinh(theta)/theta if theta else 1.0
    return n/(2*k)*(critical_root(n)+math.log(g)+c)


def overdamped_center(n,k,p,c):
    assert p>4*k
    alpha=math.sqrt(p*p-16*k*k)
    lam=(p-alpha)/2
    coefficient=(1+p/alpha)/2
    return n/lam*(math.log(n)/2+math.log(coefficient)+c)


def exact_tv(n, z):
    """Exact finite-n binomial-tail formula evaluated with log probabilities."""
    assert 0 < z < 1
    jmax = int(math.floor(n*math.log1p(z)/(math.log1p(z)-math.log1p(-z))))
    prob1=(1-z)/2
    total=0.0
    for j in range(jmax+1):
        lncomb=math.lgamma(n+1)-math.lgamma(j+1)-math.lgamma(n-j+1)
        b=math.exp(lncomb+j*math.log(prob1)+(n-j)*math.log1p(-prob1))
        unif=math.exp(lncomb-n*math.log(2))
        total += b-unif
    return total


def profile(c):
    return math.erf(math.exp(-c)/(2*math.sqrt(2)))


def main():
    # All checks use the *actual* finite-n exact bias and the binomial likelihood test.
    for case in ["critical", "overdamped", "near_critical"]:
        for c in [-0.6,0,0.6]:
            observations=[]
            for n in [512,2048,8192]:
                k=1.0
                if case=="critical":
                    p=4.0; t=critical_center(n,k,c)
                elif case=="overdamped":
                    p=6.0; t=overdamped_center(n,k,p,c)
                else:
                    theta=0.5; p=4.0+8*k*theta*theta/(math.log(n)**2)
                    t=critical_center(n,k,c,theta)
                z=bias(n,k,p,t)
                observations.append((n,exact_tv(n,z),math.sqrt(n)*z))
            err=abs(observations[-1][1]-profile(c))
            assert err<0.065, (case,c,observations,profile(c))
            print(case, 'c=',c, 'n8192_TV=',round(observations[-1][1],8),
                  'limit=',round(profile(c),8), 'n8192_bias_scaled=',round(observations[-1][2],8))
    # Check the asymptotic critical centering beyond sizes feasible for finite-binomial summation.
    for n in [10**6,10**12]:
        u=critical_root(n)
        reference=0.5*math.log(n)+math.log(math.log(n))-math.log(2)
        assert abs(u-reference)<1.0
        assert abs(math.sqrt(n)*bias(n,1.0,4.0,critical_center(n,1.0,0))-1)<1e-10
    # Independently check the decay order for each damped parameter.
    for n in [32,1024]:
        for p in [4.0,4.03,6.0]:
            prev=1.0
            for t in [0.01*n,0.1*n,n,10*n]:
                z=bias(n,1.0,p,t)
                assert 0<z<prev
                prev=z
    print('VERIFY_OK finite_binomial_TV=passed critical_center=passed nearcritical_crossover=passed overdamped_center=passed monotonicity=passed')


if __name__ == '__main__': main()
