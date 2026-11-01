"""Standalone reproducibility checks for pointwise injectivity radii of flat Klein bottles.

Dependencies: Python 3.10+ standard library only. Exact rational deck-orbit
checks are independent of the integration and optimization formulas.
"""
from fractions import Fraction
from math import sqrt, asinh, log


def analytic_shortest_squared(s, y):
    """Squared shortest nonidentity deck displacement; b=1."""
    d = min(abs(2*y-k) for k in range(-5, 6))
    return min(Fraction(1), 4*s*s, s*s+d*d)


def deck_shortest_squared(s, y):
    """Direct finite deck enumeration; the range is checked below for sufficiency."""
    distances = []
    for m in range(-6, 7):
        for k in range(-6, 7):
            if m == 0 and k == 0:
                continue
            vertical = (y if m % 2 == 0 else -y) + k - y
            distances.append((m*s)**2 + vertical**2)
    return min(distances)


def normalized_moments(s):
    if s >= 1:
        return 1.0, 1.0
    c = min(1.0, 2*s)
    v = min(.5, sqrt(c*c-s*s))
    mean = v*sqrt(s*s+v*v)+s*s*asinh(v/s)+(1-2*v)*c
    second = 2*s*s*v+2*v**3/3+(1-2*v)*c*c
    return mean, second


def sampled_integral_moments(s, n=10000):
    """Midpoint integration directly from shortest displacement formula."""
    z1=z2=0.0
    for j in range(n):
        d=(j+.5)/(2*n)
        r=min(1.0, 2*s, sqrt(s*s+d*d))
        z1 += r
        z2 += r*r
    return z1/n,z2/n


def normalized_variance(s):
    m, m2=normalized_moments(s)
    return (m2-m*m)/(4*s)


def main():
    # Exact rational check for every model deck generator, with widely differing ratios.
    count=0
    for s in (Fraction(1,20),Fraction(1,6),Fraction(1,4),
              Fraction(1,3),Fraction(2,5),Fraction(1,2),
              Fraction(3,4),Fraction(9,10),Fraction(1),Fraction(3)):
        for j in range(51):
            y=Fraction(j,50)
            assert deck_shortest_squared(s,y)==analytic_shortest_squared(s,y), (s,y)
            count += 1
    print('EXACT_RATIONAL_DECK_ORBIT_CHECKS_PASSED',count)

    # Completely independent numerical quadrature of the pointwise formula.
    count=0
    for s in (.04,.1,.24,.27,1/(2*sqrt(3)),.32,.49,.5,.65,
              sqrt(3)/2,.9,.97,1.,1.5):
        m,m2=normalized_moments(s)
        mm,mm2=sampled_integral_moments(s)
        assert abs(m-mm)<1e-7,(s,m,mm)
        assert abs(m2-mm2)<1e-7,(s,m2,mm2)
        count+=1
    print('DIRECT_INTEGRATION_MOMENT_CHECKS_PASSED',count)

    L=log(2+sqrt(3))
    C=2*sqrt(3)-L
    sstar=8*(sqrt(3)-L)/(3*C*C)
    sharp=64*(sqrt(3)-L)**3/(27*C**4)
    assert 0<sstar<1/(2*sqrt(3))
    assert abs(normalized_variance(sstar)-sharp)<1e-12
    # Exact early-regime polynomial in terms of L and s, evaluated independently.
    for s in (.03,.11,.19,sstar,.28):
        expected=(sqrt(3)-L)*s*s -C*C*s**3/4
        assert abs(expected-normalized_variance(s))<3e-14
    for s in (.005,.02,.07,.11,.19,.23,.27,.3,.35,.49,.61,.7,.85,.91,.97,1.,2.):
        assert normalized_variance(s)<=sharp+1e-12,(s,normalized_variance(s))
    print('SHARP_AREA_NORMALIZED_VARIANCE_CONSTANT_PASSED')
    print('OPTIMIZER_ASPECT',format(sstar,'.15f'))
    print('SHARP_VALUE',format(sharp,'.15f'))
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    main()
