"""Independent finite checks for the toral-shear two-lag Fourier identity.
The proof of the identity is analytic; these checks do not replace it.
Requires Python 3 standard library only.
"""
import cmath
import math
from fractions import Fraction


def tent(y, eta):
    return y / (1.0-eta) if y <= 1.0-eta else (1.0-y) / eta


def integral_exp(t):
    if abs(t) < 1e-12:
        return 1.0 + 0.0j
    return cmath.expm1(2j*math.pi*t)/(2j*math.pi*t) if hasattr(cmath,'expm1') else (cmath.exp(2j*math.pi*t)-1)/(2j*math.pi*t)


def I(m, k, eta):
    return (1-eta)*integral_exp(k+m*(1-eta)) + eta*integral_exp(k-m*eta)


def prediction(k, l, eta):
    return I(k-l, k, eta)*I(l-k, l, eta)


def iterate_twice(x, y, eta):
    u=(x+tent(y,eta))%1.0
    v=(y+u)%1.0
    return (u+tent(v,eta))%1.0


def grid_coefficient(k,l,eta,size=400):
    re=im=0.0
    for i in range(size):
        x=(i+.5)/size
        for j in range(size):
            y=(j+.5)/size
            x2=iterate_twice(x,y,eta)
            phi=2*math.pi*(k*x2-l*x)
            re+=math.cos(phi)
            im+=math.sin(phi)
    return complex(re,im)/(size*size)


def run():
    checks=0
    for eta in (Fraction(1,4),Fraction(1,3),Fraction(2,5)):
        for m in range(-5,6):
            for k in range(-5,6):
                A=k+m*(1-eta)
                B=k-m*eta
                if A != 0 and B != 0:
                    assert (1-eta)*B+eta*A==k
                    checks+=1
        ef=float(eta)
        explicit=-2*math.sin(math.pi*ef)**2/(math.pi**2*ef*(1+ef)*(3-ef)*(2-ef))
        assert abs(prediction(1,2,ef)-explicit)<1e-12
        assert explicit<0
        checks+=2
        sum_mode=math.sin(2*math.pi*ef)**2/(math.pi**2*(3-2*ef)**2*(1-2*ef)**2)
        assert abs(prediction(1,-1,ef)-sum_mode)<1e-12
        assert sum_mode>0
        checks+=2
        for k in (-3,-2,-1,1,2,3):
            assert abs(prediction(k,k,ef))<1e-12
            checks+=1
        for k,l in ((1,2),(2,1),(1,1),(2,3),(1,-1),(-1,1)):
            estimate=grid_coefficient(k,l,ef)
            expected=prediction(k,l,ef)
            error=abs(estimate-expected)
            assert error<0.002, (eta,k,l,error,estimate,expected)
            checks+=1
    for eta in (0.001,0.0001):
        assert abs(prediction(1,2,eta)/eta+1/3)<0.004
        checks+=1
    print('PASS:',checks,'exact-rational, algebraic and independent grid comparisons')


if __name__=='__main__':
    run()
