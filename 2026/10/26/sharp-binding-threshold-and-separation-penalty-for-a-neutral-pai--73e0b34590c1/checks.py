"""Numerical corroboration for a cubic-lattice neutral two-site potential.
Uses only the Python standard library. Numerical checks are not the proof.
"""
import math


def scaled_bessel(n, z):
    """Return exp(-z) I_n(z) for integer n>=0, z>=0."""
    if z == 0:
        return float(n == 0)
    if z <= 100:
        term = (z / 2) ** n / math.factorial(n)
        total = term
        m = 0
        while True:
            m += 1
            term *= (z / 2) ** 2 / (m * (m + n))
            total += term
            if abs(term) < 1e-16 * abs(total):
                break
            assert m < 1000
        return math.exp(-z) * total
    s = 1.0
    term = 1.0
    for m in range(1, 9):
        term *= -(4 * n * n - (2 * m - 1) ** 2) / (8 * z * m)
        s += term
    return s / math.sqrt(2 * math.pi * z)


def green(n, kappa=0.0, steps=2000):
    assert steps % 2 == 0
    # t=(u/(1-u))^2 makes the kappa=0 infinite tail integrable.
    def integrand(u):
        if u == 0:
            return 0.0
        if u == 1:
            return 2 / (4 * math.pi)**1.5 if kappa == 0 else 0.0
        s = u / (1-u)
        t = s*s
        return (2*u/(1-u)**3 * math.exp(-kappa*t)
                * scaled_bessel(n,2*t) * scaled_bessel(0,2*t)**2)
    h = 1 / steps
    total = integrand(0) + integrand(1)
    for j in range(1, steps):
        total += (4 if j%2 else 2) * integrand(j*h)
    return total*h/3


def main():
    g0=green(0)
    h1=green(1)
    critical=1/math.sqrt(g0*g0-h1*h1)
    print('g(0)=',g0,'h(e1)=',h1)
    print('g(0)-h(e1)=',g0-h1,'exact=1/6')
    print('critical lambda for nearest neighbors=',critical)
    assert abs(g0-h1-1/6) < 3e-7
    assert abs(critical-4.20830204122339)<3e-5
    for n in [1,2,3,4,8,12,16]:
        h=green(n)
        lc=1/math.sqrt(g0*g0-h*h)
        print('n=',n,'critical=',round(lc,9),'scaled penalty=',round(n*n*(lc-1/g0),9))
    print('predicted scaled penalty=',1/(32*math.pi**2*g0**3))
    for kappa in [0.01,0.0025,0.000625]:
        g=green(0,kappa)
        h=green(1,kappa)
        current=1/math.sqrt(g*g-h*h)
        ratio=kappa/(current-critical)**2
        print('kappa=',kappa,'gap/delta^2=',ratio)
    print('predicted limit=',16*math.pi**2/((g0-h1)**2*critical**6))
    print('All executable assertions passed; finite numerical checks do not prove limits.')

if __name__=='__main__':
    main()
