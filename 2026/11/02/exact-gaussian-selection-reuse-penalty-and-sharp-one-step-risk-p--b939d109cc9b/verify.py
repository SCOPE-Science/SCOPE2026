"""Reproduce numerical checks for the two-row noisy-greedy Kaczmarz theorem.

Requires only Python 3.9+ standard library. The infinite quantified claims
are established in RESULT.md; finite tests here do not prove them.
"""
from math import erf, exp, pi, sqrt, cos, sin


def cdf(t):
    return 0.5 * (1.0 + erf(t / sqrt(2.0)))


def phi(t):
    return exp(-0.5 * t*t) / sqrt(2*pi)


def risks(a, b, sigma):
    if not sigma > 0:
        raise ValueError('sigma must be positive')
    radius2 = a*a + b*b
    qplus = erf((a+b)/(2*sigma))
    qminus = erf((a-b)/(2*sigma))
    H = 0.5*(a*a-b*b)*qplus*qminus
    C = (2*sigma*sigma/pi)*exp(-radius2/(2*sigma*sigma))
    uniform = radius2/2 + sigma*sigma
    split = uniform - H
    reused = split + C
    return uniform, split, reused, H, C


def simpson(f, left, right, n=16000):
    assert n % 2 == 0
    width = (right-left)/n
    total = f(left) + f(right)
    for j in range(1, n):
        total += (4 if j % 2 else 2)*f(left+j*width)
    return total*width/3


def probability_abs_less(threshold, mean, sigma):
    return cdf((threshold-mean)/sigma) - cdf((-threshold-mean)/sigma)


def direct_one_step_risk(a, b, sigma):
    lo, hi = -12*sigma, 12*sigma
    def density(t):
        return phi(t/sigma)/sigma
    def term1(e):
        return (b*b+e*e)*density(e)*probability_abs_less(abs(a+e), b, sigma)
    def term2(e):
        return (a*a+e*e)*density(e)*probability_abs_less(abs(b+e), a, sigma)
    return simpson(term1, lo, hi) + simpson(term2, lo, hi)


def root_threshold():
    def f(z):
        return (2/pi)*exp(-z*z/2) - (z*z/2)*erf(z/2)**2
    left, right = 0.0, 3.0
    assert f(left)>0 and f(right)<0
    for _ in range(80):
        middle=(left+right)/2
        if f(middle)>0:
            left=middle
        else:
            right=middle
    return (left+right)/2


def run():
    checks=0
    cases=[(0,0,1),(0.9,0.3,1.3),(2,0,1.3),(1,1,1.3),
           (-2,1,1.3),(5,.2,.8),(-1.5,-1.5,2)]
    for a,b,sigma in cases:
        uniform,split,reused,H,C=risks(a,b,sigma)
        # Independent conditional integration of the algorithm, not of the closed form.
        direct=direct_one_step_risk(a,b,sigma)
        assert abs(direct-reused) < 4e-6*(1+abs(reused)), (a,b,sigma,direct,reused)
        checks += 1
        assert abs(reused-split-C)<1e-12*(1+abs(C))
        checks += 1
        assert split <= uniform+1e-12
        checks += 1
        assert C>0 and H>=-1e-12
        checks += 1
        assert H <= (a*a+b*b)/2 * erf(sqrt(a*a+b*b)/(2*sigma))**2+1e-12
        checks += 1
    # Sharp bounds at fixed radius; repeat over all quadrants and multiple scales.
    for sigma in (0.4,1.0,2.0):
        for radius in (0.0,0.2,1.0,2.5,6.0):
            max_gap=(2*sigma*sigma/pi)*exp(-radius*radius/(2*sigma*sigma))
            min_gap=max_gap-radius*radius/2*erf(radius/(2*sigma))**2
            for j in range(721):
                angle=2*pi*j/720
                a,b=radius*cos(angle),radius*sin(angle)
                uniform,split,reused,H,C=risks(a,b,sigma)
                assert min_gap-1e-10 <= reused-uniform <= max_gap+1e-10
                checks += 1
            if radius>0:
                u,_,g,_,_=risks(radius,0,sigma)
                assert abs(g-u-min_gap)<1e-12*(1+abs(min_gap))
                checks += 1
                u,_,g,_,_=risks(radius/sqrt(2),radius/sqrt(2),sigma)
                assert abs(g-u-max_gap)<1e-12*(1+abs(max_gap))
                checks += 1
    z=root_threshold()
    assert abs(z-1.24012526662719099095)<1e-12
    checks+=1
    for ztest in (.1,.5,1.0):
        assert risks(ztest,0,1)[2] > risks(ztest,0,1)[0]
        checks+=1
    for ztest in (1.5,2.0,5.0):
        assert risks(ztest,0,1)[2] < risks(ztest,0,1)[0]
        checks+=1
    for sigma in (.5,1,3):
        for radius in (.1,1,3,10):
            u,s,g,_,_=risks(radius/sqrt(2),radius/sqrt(2),sigma)
            assert abs(u-s)<1e-12*(1+abs(u)) and (g>=u-1e-12*(1+abs(u)))
            checks+=1
    print('PASS: %d deterministic checks, Gaussian conditional integrals and sharp bounds'%checks)
    print('unique one-sparse crossover r/sigma = %.15f'%z)
    print('zero-signal reuse penalty (sigma=1) = %.15f'%(2/pi))

if __name__=='__main__':
    run()
