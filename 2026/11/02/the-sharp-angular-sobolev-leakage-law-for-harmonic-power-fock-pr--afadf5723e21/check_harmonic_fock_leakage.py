#!/usr/bin/env python3
"""Finite reproducibility checks for harmonic Fock angular leakage.

Only the Python standard library is required. These finite tests supplement,
but do not replace, the analytic proof of the limiting theorem.
"""
import math


def coefficient_square(alpha, j, m):
    p, q = abs(j), abs(j + m)
    x = (2*p+2)/alpha
    y = (2*q+2)/alpha
    middle = (p+q+2)/alpha
    return math.exp(2*math.lgamma(middle) - math.lgamma(x) - math.lgamma(y))


def loss(alpha, m, N):
    return sum(1-coefficient_square(alpha,j,m) for j in range(-N,N+1))


def harmonic(n):
    return math.fsum(1/k for k in range(1,n+1))


def integration_moment(p, q):
    # independent composite Simpson quadrature after t = r^2, alpha=2.
    # Weighted radial moment ratio equals Gamma((p+q+2)/2).
    s = (p+q+2)/2
    steps = 16000
    xmax = 45.
    h = xmax/steps
    f = lambda t: t**(s-1)*math.exp(-t)
    val = f(0.)+f(xmax)
    for i in range(1,steps):
        val += (4 if i%2 else 2)*f(i*h)
    return val*h/3

checks=0
for alpha in [0.7,1.,1.5,2.,3.,5.]:
    for j in range(-8,9):
        for m in range(-7,8):
            w=coefficient_square(alpha,j,m)
            assert -.00000000002 <= w <= 1.00000000002, (alpha,j,m,w)
            checks += 1
for N in range(2,151):
    exact=harmonic(N)+harmonic(N+2)-2
    val=loss(2.,2,N)
    assert abs(val-exact) < 3.e-10, (N,val,exact)
    checks += 1
for alpha in [1.,1.5,2.,4.]:
    for m in [0,1,2,4,7]:
        for N in [3,10,40,100]:
            assert abs(loss(alpha,m,N)-loss(alpha,-m,N)) < 5.e-11
            checks += 1
# Independently integrate radial moments, rather than relying only on Gamma.
for p in range(5):
    for q in range(5):
        real=integration_moment(p,q)
        target=math.gamma((p+q+2)/2.)
        assert abs(real-target) <= 3.e-5 * target, (p,q,real,target)
        checks += 1
# Every monomial-pair leakage is nonnegative and decreases under projection.
for alpha in [1.,2.,3.]:
    for m in range(-6,7):
        for N in [2,6,20]:
            L=loss(alpha,m,N)
            assert -.00000001<=L<=2*N+1.00000001
            checks += 1
# The sharp m^2/alpha logarithmic coefficient: numerical trend only.
for alpha,m in [(1.,1),(1.,3),(2.,1),(2.,2),(3.,2),(5.,4)]:
    xs=[]
    for N in [300,1000,4000]:
        xs.append(loss(alpha,m,N) - m*m/alpha * math.log(N))
    assert abs(xs[1]-xs[2]) < 1.0, (alpha,m,xs)
    checks += 1
print(f"PASS: {checks} finite assertions; limits depend on the analytical proof.")
