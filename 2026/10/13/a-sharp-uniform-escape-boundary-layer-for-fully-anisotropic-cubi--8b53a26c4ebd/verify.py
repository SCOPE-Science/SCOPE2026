"""Finite exact and numerical checks for anisotropic Z^3 escape estimates.

Scientific proof is analytic and does not depend on these finite checks.
Requires Python 3, SciPy for the optional numerical integrals.
"""
from fractions import Fraction
from math import factorial, sqrt, log, pi, isclose
from collections import defaultdict


def return_coefficients(weights, max_half_steps=5):
    assert len(weights) == 3 and sum(weights) == 1
    out = []
    for m in range(max_half_steps+1):
        total = Fraction(0)
        for k in range(m+1):
            for j in range(m-k+1):
                l = m-k-j
                ks = (k,j,l)
                den = 1
                for t in ks:
                    den *= factorial(t)**2
                total += (Fraction(factorial(2*m), den) *
                          (weights[0]/2)**(2*k) * (weights[1]/2)**(2*j) * (weights[2]/2)**(2*l))
        out.append(total)
    return out


def direct_returns(weights, max_half_steps=5):
    law = {(0,0,0):Fraction(1)}
    result = [Fraction(1)]
    for step in range(1,2*max_half_steps+1):
        next_law = defaultdict(Fraction)
        for coord, mass in law.items():
            for i,w in enumerate(weights):
                for sign in (-1,1):
                    new = list(coord)
                    new[i] += sign
                    next_law[tuple(new)] += mass*w/2
        law = next_law
        if step % 2 == 0:
            result.append(law.get((0,0,0), Fraction(0)))
    return result


def check_exact():
    assertions = 0
    for w in ((Fraction(1,2),Fraction(1,3),Fraction(1,6)),
              (Fraction(1,4),Fraction(1,4),Fraction(1,2)),
              (Fraction(1,10),Fraction(7,10),Fraction(1,5))):
        a = return_coefficients(w, 5)
        b = direct_returns(w, 5)
        for x,y in zip(a,b):
            assert x == y
            assertions += 1
        f = [Fraction(0)]*len(a)
        for m in range(1,len(a)):
            f[m] = a[m] - sum(f[j]*a[m-j] for j in range(1,m))
            assert f[m] >= 0
            assert a[m] == sum(f[j]*a[m-j] for j in range(1,m+1))
            assertions += 2
    return assertions


def check_numerical():
    try:
        from scipy.integrate import quad
        from scipy.special import i0e
    except ImportError:
        print('SciPy unavailable; numerical checks skipped')
        return 0
    def K(c):
        return quad(lambda z: 2/sqrt(pi)*i0e(2*c*z*z)*i0e(2*(1-c)*z*z),
                    0, float('inf'), epsabs=1e-10,limit=600)[0]
    def G(h):
        return quad(lambda t: i0e(h[0]*t)*i0e(h[1]*t)*i0e(h[2]*t),
                    0, float('inf'),epsabs=1e-9,epsrel=1e-9,limit=600)[0]
    checks = 0
    for eps in (0.01,0.1,0.4,0.7):
        for c in (0.03,0.2,0.5,0.8,0.97):
            h=(1-eps,eps*c,eps*(1-c))
            ratio=K(c)/sqrt(eps)/G(h)
            assert sqrt(1-eps)-2e-6 <=ratio<=1+2e-6,(eps,c,ratio)
            checks+=1
    khalf=K(0.5)
    assert abs(khalf-0.9091727945469298)<2e-8
    checks+=1
    for c in (0.02,0.08,0.2,0.35):
        assert K(c)>khalf and abs(K(c)-K(1-c))<2e-8
        checks+=2
    return checks

if __name__=='__main__':
    c=check_exact()+check_numerical()
    print('PASS:', c, 'exact and numerical assertions')
