"""Independent numerical checks for the circle p-Ret diffusion-rank theorem.

Run with Python 3 standard library. Finite tests complement the analytic proof;
they cannot establish universal quantifiers or operator-norm claims.
"""
import math
from fractions import Fraction


def sphere_even_moment(r, n):
    ans = Fraction(1)
    for j in range(1, n + 1):
        ans *= Fraction(2*j-1, r+2*j-2)
    return ans


def fourier_multiplier_series(r, k, h):
    """Power series for the spherical-projection characteristic function."""
    t2 = r * h * k * k
    term = 1.0
    total = 1.0
    for n in range(1, 100):
        term *= -t2 / (2*n*(r+2*n-2))
        total += term
        if abs(term) < 1e-17:
            break
    return total


def circle_average_cos(t, steps=16000):
    return sum(math.cos(t*math.cos(2*math.pi*j/steps)) for j in range(steps))/steps


def check():
    count=0
    for r in range(1,9):
        for n in range(1,7):
            # The moment coefficient used by the characteristic-function expansion.
            assert sphere_even_moment(r,n) > 0
            count+=1
    for h in (0.01,0.04,0.1,0.25,0.5,1.0):
        for k in range(1,7):
            x = k*math.sqrt(h)
            assert abs(fourier_multiplier_series(1,k,h)-math.cos(x))<1e-10
            count+=1
            x=k*math.sqrt(3*h)
            assert abs(fourier_multiplier_series(3,k,h)-math.sin(x)/x)<1e-10
            count+=1
            x=k*math.sqrt(2*h)
            assert abs(fourier_multiplier_series(2,k,h)-circle_average_cos(x))<1e-10
            count+=1
    for h in (0.01,0.1,0.35,1.0):
        for r in range(2,8):
            for k in range(1,10):
                m=fourier_multiplier_series(r,k,h)
                assert abs(m)<1
                count+=1
    for p,q in ((1,3),(2,5),(1,9),(3,7)):
        h=(2*math.pi*p/q)**2
        assert abs(math.cos(q*math.sqrt(h))-1)<1e-12
        count+=1
    # A finite approximation to the small-divisor phenomenon for an irrational step.
    errors=[1-math.cos(k) for k in range(1,10000)]
    assert min(errors)<1e-6
    count+=1
    print(f'PASS: {count} supplementary moment, Bessel, sinc, quadrature, and resonance checks')

if __name__=='__main__':
    check()
