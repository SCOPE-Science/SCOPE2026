#!/usr/bin/env python3
"""Reproducible exact and seeded checks of hollow-ball chord-moment formulas.

All claims of global monotonicity and sharpness require the analytic argument
in RESULT.md; finite checks here are deliberately supporting diagnostics.
"""
from fractions import Fraction as F
from math import sqrt
from random import Random


def radial_moment(d, q, k):
    q = F(q)
    return F(d, d + k) * (1 - q ** (d + k)) / (1 - q ** d)


def moment_pair(d, q):
    a = radial_moment(d, q, 2)
    b = radial_moment(d, q, 4)
    return 2 * a, 2 * b + (2 + F(4, d)) * a * a


def kappa(d, q):
    m2, m4 = moment_pair(d, q)
    return m4 / m2**2


def sample(d, q, n, rng):
    # Sample in unit annular volume: P(|X| <= t)=(t^d-q^d)/(1-q^d).
    acc2 = acc4 = 0.
    for _ in range(n):
        z = [rng.gauss(0.,1.) for _ in range(d)]
        w = [rng.gauss(0.,1.) for _ in range(d)]
        z_norm = sqrt(sum(a*a for a in z))
        w_norm = sqrt(sum(a*a for a in w))
        rho = (q**d + (1 - q**d) * rng.random()) ** (1./d)
        sigma = (q**d + (1 - q**d) * rng.random()) ** (1./d)
        dist2 = sum((rho*a/z_norm - sigma*b/w_norm)**2 for a,b in zip(z,w))
        acc2 += dist2
        acc4 += dist2*dist2
    return acc2/n, acc4/n


def main():
    count = 0
    # Exact positivity/order bounds for a large rational grid.
    for d in range(2, 26):
        vals = [kappa(d, F(j, 40)) for j in range(1,40)]
        assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))
        count += len(vals) - 1
        lower = 1 + F(1,d)
        upper = lower + F(2,d*(d+4))
        assert all(lower < v < upper for v in vals)
        count += len(vals)
        # Endpoint expansions checked using rational arithmetic, at small q.
        q = F(1,100)
        coeff = (upper - kappa(d,q)) / q**d
        expected = F((d+2)**2,2*d*(d+4))
        assert abs(float(coeff / expected) - 1) < 0.001
        count += 1
        q = F(999,1000)
        coeff = (kappa(d,q) - lower) / (1-q)**2
        assert abs(float(coeff / F(1,6)) - 1) < 0.005
        count += 1
    # Adjacent-dimensional exact overlap threshold, and width formula.
    for d in range(2,60):
        a = (1 + F(1,d+1) + F(2,(d+1)*(d+5))) - (1 + F(1,d))
        assert a == F(d-5, d*(d+1)*(d+5))
        assert (a>0) == (d>=6)
        count += 2
    # A concrete rational overlap in dimensions six and seven.
    target=F(146,125)
    assert 1+F(1,6) < target < 1+F(1,6)+F(2,6*10)
    assert 1+F(1,7) < target < 1+F(1,7)+F(2,7*11)
    count+=2
    # Exact bisection-based reconstruction and scale recovery.
    for d in (2,3,4,5,6,7,12,20):
        for q in (F(1,10),F(1,3),F(2,3),F(9,10)):
            mu2, mu4 = moment_pair(d,q)
            target = mu4 / mu2**2
            lo,hi = F(0),F(1)
            for _ in range(70):
                mid = (lo+hi)/2
                if kappa(d,mid) > target:lo=mid
                else:hi=mid
            assert float(lo) <= float(q) <= float(hi)
            assert float(hi-lo) < 1e-16
            R2 = float(mu2)/(2*float(radial_moment(d,q,2)))
            assert abs(R2-1)<1e-14
            count += 3
    # Independent Euclidean sampling, including q=0 as an endpoint test.
    rng=Random(16022002)
    errors=[]
    for d,q,n in ((2,.0,45000),(3,.42,45000),(5,.8,45000),
                  (6,.2,45000),(7,.6,45000),(11,.35,45000)):
        m2,m4 = sample(d,q,n,rng)
        ex2,ex4 = moment_pair(d,F(str(q)))
        rel2=abs(m2/float(ex2)-1)
        rel4=abs(m4/float(ex4)-1)
        assert rel2<.025, (d,q,'second',rel2)
        assert rel4<.045, (d,q,'fourth',rel4)
        errors.append((d,q,round(rel2,5),round(rel4,5)))
        count += 2
    print('VERIFY_OK',count,'exact_rational_and_independent_sample_checks')
    print('SAMPLED_RELATIVE_ERRORS',errors)

if __name__ == '__main__':
    main()
