"""Reproducibility checks for blocking RSA neighborhood statistics on regular trees.
The symbolic identities are exact. Finite-tree simulations are supportive, not a proof.
Run: python verification.py (requires sympy 1.14.0)."""
import math
import random
from collections import Counter
from itertools import combinations
import sympy as S


def cavity(t, degree):
    if degree == 2:
        return math.exp(-t)
    return (1+(degree-2)*t)**(-1/(degree-2))


def integral_polynomial_numeric(degree):
    """Independent midpoint quadrature of the root coordination PGF coefficients."""
    steps=24000
    a=cavity(1, degree)
    out=[0.]*(degree+1)
    for j in range(steps):
        u=cavity((j+.5)/steps,degree)
        for k in range(degree+1):
            out[k]-=math.comb(degree,k)*(a**(degree-k))*((u-a)**k)/steps
    for k in range(degree+1):
        out[k]+=math.comb(degree,k)*(a**(degree-k))*((1-a)**k)
    out[0]+=(1-a*a)/2
    return out


def theoretical_three(degree):
    a=cavity(1,degree)
    p=(1-a*a)/2
    m2=p+a*a*math.log(a)
    m3=.5+1.5*a*a-2*a*a*a+3*a*a*math.log(a)
    return p,m2-p*p,m3-3*m2*p+2*p**3


def finite_regular_tree(degree, depth):
    adj=[[]]
    cur=[0]
    for h in range(depth):
        nex=[]
        for v in cur:
            children=degree if v==0 else degree-1
            for _ in range(children):
                w=len(adj)
                adj.append([v]); adj[v].append(w)
                nex.append(w)
        cur=nex
    return adj


def simulate(degree, depth, samples, seed):
    adj=finite_regular_tree(degree,depth)
    rng=random.Random(seed)
    hist=Counter()
    n=len(adj)
    for _ in range(samples):
        clocks=[rng.random() for _ in range(n)]
        occupied=bytearray(n)
        for v in sorted(range(n),key=clocks.__getitem__):
            if all(not occupied[w] for w in adj[v]):
                occupied[v]=1
        hist[sum(occupied[v] for v in adj[0])]+=1
    return {k:hist[k]/samples for k in range(degree+1)}


def main():
    a,z=S.symbols('a z', positive=True)
    log=S.log(a)
    m1=(1-a*a)/2
    m2=m1+a*a*log
    m3=S.Rational(1,2)+S.Rational(3,2)*a*a-2*a**3+3*a*a*log
    cov=S.factor(m2-m1*m1)
    cum=S.factor(m3-3*m2*m1+2*m1**3)
    expected_cov=(1-a**4)/4+a*a*log
    F=a**4+8*a-9-6*(1+a*a)*log
    assert S.simplify(cov-expected_cov)==0
    assert S.simplify(cum+a*a*F/4)==0
    t=(1-a)/(1+a)
    lower=S.factor(a**4+8*a-9+12*(1+a*a)*(t+t**3/3))
    assert S.simplify(lower-(1-a)**4*(a**3+7*a*a+9*a+7)/(1+a)**3)==0
    assert S.simplify(cum.subs(a,S.Rational(1,2))-(S.Rational(79,256)-S.Rational(15,32)*S.log(2)))==0
    print('EXACT: moment, covariance, third cumulant and positivity-bound identities OK')
    # Polynomial coordination probabilities in degree 3, checked from closed integrals.
    x=S.symbols('x', positive=True)
    u=1/(1+x)
    poly=S.expand(((1+z)/2)**3 +S.integrate(u**3-(S.Rational(1,2)+z*(u-S.Rational(1,2)))**3,(x,0,1)))
    target=S.Rational(3,8)+(S.Rational(3,4)-S.Rational(3,4)*S.log(2))*z+(S.Rational(3,2)*S.log(2)-S.Rational(3,4))*z*z+(S.Rational(5,8)-S.Rational(3,4)*S.log(2))*z**3
    assert S.simplify(poly-target)==0
    assert S.simplify(poly.subs(z,1)-1)==0
    print('EXACT: full degree-three probability polynomial OK')
    for degree in [2,3,4,5,8,16]:
        vals=integral_polynomial_numeric(degree)
        mean=sum(k*vals[k] for k in range(degree+1))
        p,c2,c3=theoretical_three(degree)
        assert all(v>-1e-8 for v in vals)
        assert abs(sum(vals)-1)<2e-8
        assert abs(vals[0]-p)<1e-9
        assert abs(mean-degree*p)<1e-8
        if degree>=3:
            assert c2>0 and c3<0
        print('QUADRATURE:',degree,'P0=',round(vals[0],8),'mean=',round(mean,8),'cov=',round(c2,8), 'third_cum=',round(c3,8) if degree>=3 else 'not applicable')
    for degree,depth,samples,seed in [(3,6,30000,57482),(4,5,24000,57483)]:
        actual=simulate(degree,depth,samples,seed)
        expected=integral_polynomial_numeric(degree)
        largest=max(abs(actual[k]-expected[k]) for k in range(degree+1))
        print('FINITE-TREE MONTE CARLO:',degree,depth,'samples=',samples,'vertices=',len(finite_regular_tree(degree,depth)),'max_abs_difference=',round(largest,5))
        assert largest<.026
    for degree in [1000,10000,100000]:
        a=cavity(1,degree)
        p=(1-a*a)/2
        log_ratio=math.log(p)-degree*math.log1p(-p)
        assert abs(math.exp(log_ratio)/math.log(degree)-1)<.15
        print('ASYMPTOTIC CHECK:',degree,'enhancement_over_independent=',round(math.exp(log_ratio),5),'log_degree=',round(math.log(degree),5))
    print('PASS')

if __name__=='__main__':
    main()
