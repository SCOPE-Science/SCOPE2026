"""Independent finite diagnostics for a one-axis cross-polytope extrusion.

Pure standard-library checks; finite checks do not certify a universal theorem.
"""
from fractions import Fraction
from math import comb, exp, expm1, factorial, log1p


def volume_primal(d, h):
    return Fraction(2**d, factorial(d)) * (1 + d*h)


def polar_integral_polynomial(d, h):
    # Integrate by expanding (1-h*t)^(d-1) on [0,(1+h)^(-1)].
    top = 1/(1+h)
    return 2**d * sum(Fraction(comb(d-1,j) * (-h)**j, j+1)*top**(j+1) for j in range(d))


def polar_closed(d, h):
    return Fraction(2**d, d*h) * (1-(1+h)**(-d))


def M(d, h):
    return (1+d*h)*(1-(1+h)**(-d))/(d*h)


def M_poly(d, h):
    t = 1/(1+h)
    return 1+(sum(t**j for j in range(1,d))-(d-1)*t**d)/d


def alpha_root():
    lo,hi=1.,3.
    for _ in range(100):
        m=(lo+hi)/2
        if exp(m) < 1+m+m*m:
            lo=m
        else:
            hi=m
    return (lo+hi)/2


def optimal_t(d):
    lo,hi=0.,1.
    def derivative(t):
        return sum(j*t**(j-1) for j in range(1,d))-d*(d-1)*t**(d-1)
    for _ in range(110):
        mid=(lo+hi)/2
        if derivative(mid)>0: lo=mid
        else: hi=mid
    return (lo+hi)/2


def main():
    checks=0
    # Independent polynomial antiderivative in rational arithmetic.
    for d in range(2,19):
        for h in [Fraction(1,17),Fraction(1,4),Fraction(1,2),Fraction(1),Fraction(7,3),Fraction(9)]:
            assert polar_integral_polynomial(d,h)==polar_closed(d,h)
            assert M(d,h)==M_poly(d,h)
            assert volume_primal(d,h)*polar_closed(d,h) == Fraction(4**d,factorial(d))*M(d,h)
            checks+=3
    r=alpha_root(); C=(1+r)**2/(1+r+r*r)
    assert abs(r-1.793282132900761)<1e-13
    assert abs(C-1.2984256075256391)<1e-13
    last=1.
    for d in range(2,201):
        t=optimal_t(d)
        h=1/t-1
        peak=float(M_poly(d,h))
        assert 1<peak<C
        assert peak>last
        assert t>0 and t<1
        if d>2:
            assert d*h > 0
        last=peak
        checks+=5
    assert abs(last-C)<0.006
    for a in [0.01,0.3,0.8,r,4.,10.,100.]:
        g=(1+1/a)*(1-exp(-a))
        prev=0.
        for d in [2,3,4,5,10,20,50,100,1000]:
            v=(1+1/a)*(-expm1(-d*log1p(a/d)))
            assert 1<v<g+1e-12
            assert v+1e-13>=prev
            prev=v
            checks+=3
    print('VERIFY_OK',checks, 'alpha',f'{r:.14f}','bound',f'{C:.15f}', 'mu200',f'{last:.15f}')

if __name__=='__main__': main()
