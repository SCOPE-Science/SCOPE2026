"""Reproduce finite numerical and exact-algebra checks for the sampled-feedback theorem.

Requires Python 3.10+ standard library only. Execute: python checker.py
The finite tests corroborate, rather than replace, the analytical proof.
"""
import math
import random
from fractions import Fraction


def root_bisect(f, lo, hi, steps=110):
    a, b = lo, hi
    fa, fb = f(a), f(b)
    assert fa * fb <= 0, (fa, fb)
    for _ in range(steps):
        mid = (a+b)/2
        fm = f(mid)
        if fa*fm > 0:
            a, fa = mid, fm
        else:
            b, fb = mid, fm
    return (a+b)/2


def mesh(x, alpha, beta, r):
    z = root_bisect(lambda zz: zz+r*(1-alpha)*math.tanh(zz)-alpha*x,
                    -abs(x)-2, abs(x)+2)
    return beta*x-r*(1-beta)*math.tanh(z), z


def multiplier(alpha, beta, r, slope):
    return (beta-r*(alpha-beta)*slope)/(1+r*(1-alpha)*slope)


def run():
    rng = random.Random(2802026)
    assertions = 0
    for _ in range(200):
        # Rational exact verification of the claimed difference-quotient identity.
        b = Fraction(rng.randint(1, 8), 20)
        a = b+(1-b)*Fraction(rng.randint(1, 9), 10)
        r = Fraction(rng.randint(1, 100), 9)
        s = Fraction(rng.randint(0, 15), 16)
        u = Fraction(rng.randint(1, 15), 16)
        v = Fraction(rng.randint(1, 15), 16)
        # Let z1-z2=u and f(z1)-f(z2)=s*u; x1-x2=(u+r(1-a)*s*u)/a.
        dx = (u+r*(1-a)*s*u)/a
        dy = b*dx-r*(1-b)*s*u
        assert dy/dx == multiplier(a, b, r, s)
        assert multiplier(a, b, r, 0) == b
        assert multiplier(a, b, r, s) > multiplier(a, b, r, u) if s<u else True
        assertions += 3
    for _ in range(480):
        aa = rng.uniform(.08, 3.0)
        hh = rng.uniform(.08, 3.2)
        phase = rng.random()*.9999
        alpha = math.exp(-aa*hh*phase)
        beta = math.exp(-aa*hh)
        r = rng.uniform(.01, 17)
        x = rng.uniform(-4, 4)
        fx, z = mesh(x, alpha, beta, r)
        eps = 1e-5
        dfx = (mesh(x+eps, alpha, beta, r)[0]-mesh(x-eps, alpha, beta, r)[0])/(2*eps)
        exact = multiplier(alpha, beta, r, 1/math.cosh(z)**2)
        assert abs(dfx-exact)<3e-8, (dfx, exact)
        assert abs(z+r*(1-alpha)*math.tanh(z)-alpha*x)<1e-12
        assert abs(fx-beta*x+r*(1-beta)*math.tanh(z))<1e-12
        assertions += 3
    for _ in range(160):
        aa = rng.uniform(.2, 2.0)
        hh = rng.uniform(.3, 2.4)
        beta = math.exp(-aa*hh)
        s_star = math.log(2/(1+beta))/(aa*hh)
        phase = rng.uniform(0.0, s_star*.95)
        alpha = math.exp(-aa*hh*phase)
        d = 2*alpha-1-beta
        assert d>0
        r_c = (1+beta)/d
        ratio = rng.uniform(1.001, 4)
        r = ratio*r_c
        z = root_bisect(lambda zz: math.tanh(zz)/zz-1/ratio, 1e-8, 50)
        x = z*(1-beta)/d
        fx, zs = mesh(x, alpha, beta, r)
        assert abs(fx+x)<5e-10, (fx, x, z, zs)
        assert abs(zs-z)<5e-10
        m = multiplier(alpha, beta, r, 1/math.cosh(z)**2)
        assert -1<m<1
        # Check local multiplier of the two-step orbit.
        h0 = 1e-5
        num = (mesh(x+h0, alpha, beta, r)[0]-mesh(x-h0, alpha, beta, r)[0])/(2*h0)
        assert abs(num*num-m*m)<1e-7
        assertions += 5
    aa, hh, phase = .9, 1.2, 0.12
    alpha, beta = math.exp(-aa*hh*phase), math.exp(-aa*hh)
    d = 2*alpha-1-beta
    r_c = (1+beta)/d
    c = (1+beta)*d**3/(3*alpha*(1-beta)**3)
    x = 0.05
    for _ in range(120000):
        x, _ = mesh(x, alpha, beta, r_c)
    assert abs(120000*x*x*2*c-1)<.02, (120000*x*x*2*c)
    assertions += 1
    print(f"PASS {assertions} finite checks, including rational secant identities, numerical derivatives, supercritical cycles, and critical relaxation")

if __name__ == '__main__':
    run()
