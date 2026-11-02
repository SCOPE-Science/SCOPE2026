"""Independent finite-sum checks for point hitting with proportional Brownian resetting.

Requires Python 3 with scipy.  All numerical checks are finite and do not
replace the proof of convergence or of the first-hitting resolvent identity.
"""
import math
import sys
from scipy.integrate import quad


def h(n, x, c):
    """Exact finite hypoexponential/Laplace convolution at x."""
    s = 0.0
    for j in range(n + 1):
        weight = 1.0
        for m in range(n + 1):
            if j != m:
                weight /= 1.0 - c ** (2 * (m - j))
        s += weight * math.exp(-abs(x) / c**j) / c**j
    return 0.5 * s


def h_fourier(n, x, c):
    """Independent cosine-weighted inverse transform of the Fourier product."""
    def product(t):
        return math.prod(1.0 / (1.0 + c**(2*j)*t*t)
                         for j in range(n+1))
    return quad(product, 0.0, float("inf"), weight="cos", wvar=x,
                epsabs=2e-11, epsrel=2e-11, limlst=1000,
                maxp1=500)[0] / math.pi


def r_times_t(a, b, y, N):
    c = abs(a)
    numerator = sum(h(n, b-a**n*b, c)-h(n, b-a**n*y, c)
                    for n in range(N+1))
    return numerator/h(N, b, c)


def certified_interval(a, b, y, N):
    c = abs(a)
    s = sum(h(n, b-a**n*b, c)-h(n, b-a**n*y, c)
            for n in range(N+1))
    denominator = h(N,b,c)
    delta = c**(N+1)/(2*(1-c))
    eps = abs(b-y)*delta
    assert denominator > delta
    return max(0,(s-eps)/(denominator+delta)), (s+eps)/(denominator-delta)


def source_f(a,z):
    even=odd=0.0
    coeff_even=coeff_odd=1.0
    for n in range(42):
        if n:
            coeff_odd*=1-a**(2*n-1)
            if n>1:
                coeff_even*=1-a**(2*n-2)
            even += coeff_even*z**(2*n)/math.factorial(2*n)
        odd += coeff_odd*z**(2*n+1)/math.factorial(2*n+1)
    return even,odd


def source_negative_tilde(a,b,kappa_tilde):
    e,o=source_f(a,b)
    ee,oo=source_f(a,b/abs(a))
    return (e*oo+o*(b*b*kappa_tilde+ee))/(b*b*(oo+o))


def source_positive_tilde(a,b):
    e,o=source_f(a,b)
    numerator=math.prod(1-a**(2*j) for j in range(1,90))
    denominator=math.prod(1-a**(2*j+1) for j in range(90))
    return (e+(numerator/denominator)*o)/b**2


def main():
    count=0
    for c in [0.2,0.4,0.5,0.7]:
        for n in range(1,5):
            for x in [0.0, 0.3, 0.9, 1.8]:
                p=h(n,x,c); q=h_fourier(n,x,c)
                assert p>0 and abs(p-q)<1e-9, (c,n,x,p,q)
                count+=1
    for a,b in [(-.2,1.),(-.5,.7),(-.5,1.),(-.5,1.3)]:
        c=abs(a)
        t0=r_times_t(a,b,0.,38)/b**2
        kappa=r_times_t(a,b,-b/c,38)/b**2
        expected=source_negative_tilde(a,b,kappa)
        assert abs(t0-expected)<1e-10,(a,b,t0,expected)
        for y in [0.0,-b/c,b/2,-2*b]:
            lo,hi=certified_interval(a,b,y,22)
            actual=r_times_t(a,b,y,38)
            assert lo-1e-11 <=actual<=hi+1e-11,(a,b,y,lo,actual,hi)
            count+=1
        print(f"negative rescale {a:g}, b={b:g}, T0*D/L^2={t0:.12f}, kappa*D/L^2={kappa:.12f}")
        count+=1
    for a,b in [(.2,1.),(.5,.7),(.5,1.)]:
        t0=r_times_t(a,b,0.,38)/b**2
        assert abs(t0-source_positive_tilde(a,b))<1e-10,(a,b,t0)
        count+=1
    print(f"PASS: {count} independent finite numerical consistency checks")

if __name__=='__main__':
    main()
