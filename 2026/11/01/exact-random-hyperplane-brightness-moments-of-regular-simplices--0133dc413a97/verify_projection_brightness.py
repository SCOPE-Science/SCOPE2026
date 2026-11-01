"""Checks for regular-simplex Haar hyperplane projection brightness moments.
Run with Python 3; requires only the standard library. Numerical diagnostics are
finite checks, not a proof of the theorem's asymptotic assertions.
"""
import math
import random


def moment_formulas(m):
    if m < 3:
        raise ValueError('m must be at least three')
    log_mu = (0.5 * math.log(m * (m - 1))
              + math.lgamma((m - 1) / 2) - math.lgamma(m / 2)
              - 0.5 * math.log(math.pi))
    mu = math.exp(log_mu)
    r = 1.0 / (m - 1)
    e2 = 1 + 2 * (m - 1) / math.pi * (math.sqrt(1-r*r) + r*math.asin(r))
    return mu, e2, e2-mu*mu


def coordinate_gaussian(m, rng):
    samples = [rng.gauss(0, 1) for _ in range(m)]
    center = sum(samples)/m
    residuals = [x-center for x in samples]
    scale = math.sqrt(sum(x*x for x in residuals))
    return sum(abs(x) for x in residuals)/scale


def test():
    count=0
    # Geometric Crofton/Cauchy independently yields the mean planar and
    # three-dimensional projection values for the equilateral triangle
    # and regular tetrahedron.
    mu3, e23, v3 = moment_formulas(3)
    assert abs(math.sqrt(3)/2*mu3 - 3*math.sqrt(2)/math.pi)<1e-12
    count+=1
    mu4, e24, v4 = moment_formulas(4)
    assert abs(mu4/2 - math.sqrt(3)/2)<1e-12
    count+=1
    assert abs(e23-(4/3+2*math.sqrt(3)/math.pi))<1e-12
    count+=1
    # Exact angular integral on the circle in the zero-sum plane for m=3.
    N=72000
    acc1=acc2=0.0
    for j in range(N):
        theta=2*math.pi*(j+0.5)/N
        a=math.cos(theta)/math.sqrt(2)
        b=math.sin(theta)/math.sqrt(6)
        u=[a+b,-a+b,-2*b]
        s=sum(abs(v) for v in u)
        acc1+=s
        acc2+=s*s
    assert abs(acc1/N-mu3)<1e-8
    count+=1
    assert abs(acc2/N-e23)<1e-8
    count+=1
    # Analytic finite-dimensional bounds and the first asymptotic correction.
    for m in range(3,101):
        mu,e2,var=moment_formulas(m)
        assert mu>0 and e2>=mu*mu and var>0
        assert var < 1-3/math.pi
        count+=2
    for m in [100, 300, 1000, 3000, 10000]:
        _,_,var=moment_formulas(m)
        corr=(1-3/math.pi)-var
        assert abs(m*corr-1/(4*math.pi))<0.015
        count+=1
    rng=random.Random(93017)
    for m in (4,8):
        N=100000
        total=total2=0.0
        for _ in range(N):
            s=coordinate_gaussian(m,rng)
            total+=s
            total2+=s*s
        mu,e2,_=moment_formulas(m)
        assert abs(total/N-mu)<0.018
        assert abs(total2/N-e2)<0.045
        count+=2
    print(f'PASS: {count} deterministic geometric, exact-identity, asymptotic diagnostic, and simulation checks')

if __name__=='__main__':
    test()
