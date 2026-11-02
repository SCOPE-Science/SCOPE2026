"""Reproducibility checks for Euclidean parallelogram boundary moments.
Uses only Python's standard library. It is not a substitute for the proof.
"""
import math
from fractions import Fraction


def moment_quad(p, a, b, cosine, n=6000):
    assert n % 2 == 0 and a > 0 and b > 0 and -1 <= cosine <= 1
    h = 2 / n
    def simpson(f):
        return h / 3 * (f(-1) + f(1) +
             4 * sum(f(-1 + h * i) for i in range(1, n, 2)) +
             2 * sum(f(-1 + h * i) for i in range(2, n, 2)))
    return (2*b*simpson(lambda t: max(0.0, a*a+b*b*t*t+2*a*b*cosine*t)**(p/2))
            + 2*a*simpson(lambda t: max(0.0, b*b+a*a*t*t+2*a*b*cosine*t)**(p/2)))


def moment_even_exact(k, a, b, c):
    # k = exponent p/2, expanded with exact polynomial multiplication.
    def integral_poly(a2, b2, q):
        poly = [Fraction(1)]
        for _ in range(k):
            new = [Fraction(0)]*(len(poly)+2)
            for i,v in enumerate(poly):
                new[i] += v*a2
                new[i+1] += v*q
                new[i+2] += v*b2
            poly = new
        return sum(v * Fraction(2, i+1) for i,v in enumerate(poly) if i%2==0)
    return 2*b*integral_poly(a*a,b*b,2*a*b*c)+2*a*integral_poly(b*b,a*a,2*a*b*c)

for a,b,c in [(Fraction(1),Fraction(1),Fraction(0)),
              (Fraction(3,2),Fraction(2,5),Fraction(3,5)),
              (Fraction(2,3),Fraction(7,5),Fraction(-4,5)),
              (Fraction(5,6),Fraction(9,7),Fraction(1,10))]:
    m2 = moment_even_exact(1,a,b,c)
    m4 = moment_even_exact(2,a,b,c)
    expected2 = Fraction(4,3)*(a+b)**3
    expected4 = Fraction(4,5)*(a+b)**5-Fraction(16,3)*a*a*b*b*(a+b)*(1-c*c)
    assert m2 == expected2, (m2,expected2)
    assert m4 == expected4, (m4,expected4)
print('EXACT_QUADRATIC_AND_QUARTIC_IDENTITIES_PASSED')

for p in (2.25, 2.75, 3., 3.5, 4., 5.25):
    for a,b,c in ((1.,0.4,0.0),(1.,0.8,0.72),(1.3,0.3,-0.61)):
        measured = moment_quad(p,a,b,c)
        envelope = 4/(p+1)*(a+b)**(p+1)
        assert measured < envelope + 3.e-10
        if 2 < p <= 4:
            gap = (2*p*(p-2)/3)*a*a*b*b*(a+b)**(p-3)*(1-c*c)
            assert measured <= envelope-gap + 6.e-9, (p,a,b,c,measured,envelope,gap)
        if p==4:
            assert abs(measured-(envelope-(16/3)*a*a*b*b*(a+b)*(1-c*c)))<1.e-9
print('INDEPENDENT_QUADRATURE_AND_STABILITY_PASSED')

lo, hi = 3.0,4.0
for _ in range(90):
    mid=(lo+hi)/2
    if (math.pi/2)**mid > mid+1: hi=mid
    else: lo=mid
pc=(lo+hi)/2
assert 3.15295 < pc < 3.15296
assert (math.pi/2)**3 < 4 and (math.pi/2)**4 > 5
assert math.log(math.pi/2)>1/3
# A nondegenerate parallelogram approaches the sharp needle envelope.
for p in (3.,3.1,pc+0.05,4.):
    a,b=1.,0.7
    disk=(4*(a+b))**(p+1)/(2*math.pi)**p
    close=moment_quad(p,a,b,0.99999)
    if p<=3.1: assert close<disk
    else: assert close>disk
print('UNIQUE_CRITICAL_EXPONENT_AND_SHARPNESS_PASSED')
print('ALL_CHECKS_PASSED')
