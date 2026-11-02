"""Reproduce rational examples and numerical checks for multi-hump linear-reservoir recession."""
from fractions import Fraction
from math import exp, log


def exact_beta_3(R, k, c):
    """At t=k log R + log c, with integer k and positive rational c."""
    x = Fraction(1, R**k) / c
    w = (x, Fraction(R**2)*x**2, Fraction(R**4)*x**4)
    m0 = sum(w)
    m1 = sum((2**j)*w[j] for j in range(3))
    m2 = sum((2**j)**2*w[j] for j in range(3))
    return m0*m2/(m1*m1)


def beta_n(n, R, t):
    E = [0]
    for j in range(1, n):
        E.append(E[-1]+(2**(j-1))*(n-j))
    logs = [e*log(R) - (2**j)*t for j,e in enumerate(E)]
    top = max(logs)
    weights = [exp(x-top) for x in logs]
    s0 = sum(weights)
    s1 = sum((2**j)*w for j,w in enumerate(weights))
    s2 = sum((4**j)*w for j,w in enumerate(weights))
    return s0*s2/(s1*s1)


def run():
    R=100
    fast = [exact_beta_3(R,1,Fraction(c)) for c in (1,Fraction(4,3),2)]
    slow = [exact_beta_3(R,2,Fraction(c)) for c in (Fraction(1,2),2,4)]
    assert fast[1]>fast[0] and fast[1]>fast[2]
    assert slow[1]>slow[0] and slow[1]>slow[2]
    assert log(R)+log(2) < 2*log(R)-log(2)
    # At least two strict local maxima follow because each open bracket
    # has an interior point exceeding both endpoints.
    checks=0
    for n in range(3,10):
        for i in range(1,n):
            Ti=(n-i)*log(10**6)
            peak=Ti+log(2)/(2**(i-1))
            assert abs(beta_n(n,10**6,peak)-Fraction(9,8))<0.001
            checks+=1
            if i>=2:
                valley=(Ti+(n-i+1)*log(10**6))/2
                assert abs(beta_n(n,10**6,valley)-1)<0.001
                checks+=1
    # Analytic two-rate identity: (1+s)(1+4s)-(1+2s)^2=s.
    for s in [Fraction(1,13), Fraction(1,2),Fraction(2,1),Fraction(7,3)]:
        assert (1+s)*(1+4*s)-(1+2*s)**2==s
        assert s/(1+2*s)**2 <= Fraction(1,8)
        checks+=1
    print('PASS: two disjoint exact rational three-reservoir peak brackets')
    print('PASS: %d multi-reservoir asymptotic-window and pair-identity checks'%checks)
    print('fast bracket:',*[str(x) for x in fast])
    print('slow bracket:',*[str(x) for x in slow])


if __name__=='__main__':
    run()
