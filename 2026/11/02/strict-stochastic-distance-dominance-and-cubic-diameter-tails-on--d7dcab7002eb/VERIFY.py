"""Reproducible finite checks for intrinsic distances on flat Klein bottles.

All geometric statements for arbitrary positive parameters are proved analytically
in RESULT.md. This script checks representative configurations and asymptotics;
it is not an exhaustive proof.
"""
from fractions import Fraction as F
from math import sqrt, hypot


def fold(a, period):
    a = a % period
    return min(a, period - a)


def closed_squared(p, q, L, H):
    x, y = p
    xx, yy = q
    u = fold(x - xx, L)
    v = fold(x + xx, L)
    z = abs(y - yy)
    return min(u*u + z*z, v*v + (H-z)*(H-z))


def lifted_squared(p, q, L, H):
    x, y = p
    xx, yy = q
    vals = []
    for k in range(-2, 3):
        for j in range(-2, 3):
            vals.append((xx + k*L-x)**2 + (yy+2*j*H-y)**2)
            vals.append((-xx + k*L-x)**2 + (yy+(2*j+1)*H-y)**2)
    return min(vals)


def check_lifts():
    checks = 0
    for L, H in [(F(2), F(1)), (F(1), F(3)), (F(5, 3), F(7, 4))]:
        points = [(i*L/7, j*H/6) for i in range(7) for j in range(6)]
        for p in points:
            for q in points:
                assert closed_squared(p, q, L, H) == lifted_squared(p, q, L, H)
                checks += 1
    # In odd finite cyclic groups the sum-difference change of variables
    # is bijective; the continuous argument uses Fourier characters instead.
    for mod in [5, 7, 11, 13]:
        outcomes = {( (i-j) % mod, (i+j) % mod) for i in range(mod) for j in range(mod)}
        assert len(outcomes) == mod*mod
        checks += mod*mod
    return checks


def qval(t, v, s):
    if v >= t:
        return 0.0
    return min(1.0, sqrt(t*t-v*v)/s)


def simpson(f, a, b, n=16000):
    if b <= a:
        return 0.0
    if n % 2:
        n += 1
    dx = (b-a)/n
    total = f(a)+f(b)
    for i in range(1,n):
        total += (4 if i % 2 else 2)*f(a+dx*i)
    return total*dx/3


def cdf_gap(t,s,h):
    a = max(0., 2*h-t)
    return simpson(lambda w:qval(t,2*h-w,s)*(1-qval(t,w,s))/h, a,h)


def upper_tails(t,s,h):
    # Near the common diameter, the torus and Klein integrands vanish
    # outside the following exactly known interval.
    a = sqrt(max(0,t*t-s*s)) if t>s else 0.
    tor = simpson(lambda w:(1-qval(t,w,s))/h,a,h)
    klein = simpson(lambda w:(1-qval(t,w,s))*(1-qval(t,2*h-w,s))/h,a,h)
    return tor,klein


def check_cdf_and_endpoints():
    checks=0
    for s,h in [(1.,1.), (2.,0.8), (0.3,2.), (1.7,1.3)]:
        diameter=hypot(s,h)
        for t in [0.,h*.2,h*.8,h,diameter,diameter*1.25]:
            assert abs(cdf_gap(t,s,h)) < 1.e-10
            checks += 1
        for t in [h+(diameter-h)*x for x in [.12,.36,.62,.88]]:
            assert cdf_gap(t,s,h)>1.e-12
            checks += 1
    # Independent limits at the two sharp thresholds.
    for eps in [0.0001,0.0003,0.001]:
        s=h=1.
        gap = cdf_gap(h+eps,s,h)
        predicted = 2*sqrt(2)/(3*s*sqrt(h))*eps**1.5
        assert abs(gap/predicted-1) < .065
        checks += 1
    for eps in [.001,.003,.007]:
        s=h=1.;R=hypot(s,h)
        tor,klein=upper_tails(R-eps,s,h)
        pt = R**2/(2*h*h*s*s)*eps**2
        pk = 2*R**3/(3*h*h*s**4)*eps**3
        assert abs(tor/pt-1)<.02
        assert abs(klein/pk-1)<.02
        checks += 2
    return checks


def main():
    n1=check_lifts()
    n2=check_cdf_and_endpoints()
    print('PASS: %d exact lift/finite-character checks; %d deterministic CDF/asymptotic checks.'%(n1,n2))
    print('Finite tests do not replace the analytical universal proof.')


if __name__=='__main__':
    main()
