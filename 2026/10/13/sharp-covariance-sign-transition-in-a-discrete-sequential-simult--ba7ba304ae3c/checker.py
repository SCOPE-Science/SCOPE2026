"""Reproduce finite-moment and transition checks for the sequential/common-shock law.

Requires only Python >=3.9 standard library. Analytic proof is in RESULT.md.
"""
from math import sqrt


def covariance(r, v, theta):
    a, b = 1-r, 1-v
    d = 1-a*b
    return a*b/d**2-theta*(1-theta)*(r*b)**2/d**4


def direct_moments(r, v, theta, cutoff=360):
    """Independently enumerate the ordered joint PMF up to cutoff-1."""
    a, b, d = 1-r, 1-v, 1-(1-r)*(1-v)
    q = a*b
    total = m1 = m2 = cross = 0.0
    for t in range(cutoff):
        w = v*q**t
        total += w
        m1 += t*w
        m2 += t*w
        cross += t*t*w
        for u in range(t+1, cutoff):
            w = r*b*d*q**(u-1)
            total += w
            m1 += w*(theta*t+(1-theta)*u)
            m2 += w*((1-theta)*t+theta*u)
            cross += w*t*u
    return total, cross-m1*m2


def critical_tie_mass(r, theta):
    a, c = 1-r, theta*(1-theta)
    if a >= c:
        return None
    return (1+a-sqrt((1-a)**2+4*a*a/c))/(2*a)


def main():
    tests = [(.9,.1,.5),(.9,.7,.5),(.5,.1,.5),
             (.95,.05,.2),(.1,.1,.5),(.7,.15,.8)]
    for r,v,theta in tests:
        mass, cov = direct_moments(r,v,theta)
        target = covariance(r,v,theta)
        assert abs(mass-1)<1.e-10, (r,v,theta,mass)
        assert abs(cov-target)<2.e-9, (r,v,theta,cov,target)
    for theta in (.2,.5,.8):
        c=theta*(1-theta)
        for r in (1-c+.01,1-c+.1):
            if r>=1:
                continue
            pi=critical_tie_mass(r,theta)
            assert 0<pi<1
            a=1-r
            v=pi*r/(1-a*pi)
            assert 0<v<1 and abs(covariance(r,v,theta))<3.e-13
            assert covariance(r,v/2,theta)<0
            assert covariance(r,(1+v)/2,theta)>0
        assert critical_tie_mass((1-c)*.9,theta) is None
    pi=critical_tie_mass(.9,.5)
    assert abs(pi-.5755710991019481)<1.e-12
    print('PASS: six independently summed joint-PMF covariance cases; '
          'three sharp transition configurations; boundary sign checks.')
    print('r=0.9, theta=0.5: critical tie mass',pi,
          'critical common-shock probability',pi*.9/(1-.1*pi))


if __name__=='__main__':
    main()
