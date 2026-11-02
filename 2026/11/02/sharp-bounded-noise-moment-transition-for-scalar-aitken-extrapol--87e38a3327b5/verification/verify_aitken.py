"""Reproducible exact-algebra and quadrature diagnostics for the bounded-noise Aitken law.

The mathematical proof, rather than finite checks, establishes all moment statements.
Run with Python 3.10+ using only the standard library.
"""
from fractions import Fraction as Q
from math import exp, log, sqrt
from random import Random

N = 0

def check(test, message):
    global N
    N += 1
    if not test:
        raise AssertionError(message)

rng = Random(20261031)
for i in range(4000):
    rho = Q(rng.randint(1, 19), 20)
    s = Q(rng.randint(1, 27), rng.randint(1, 9))
    eta = Q(rng.randint(1, 12), rng.randint(2, 35))
    e0 = Q(rng.randint(-20, 20), 20) * eta
    e1 = Q(rng.randint(-20, 20), 20) * eta
    c, a = 1-rho, 2-rho
    x0, x1 = s, rho*s + e0
    x2 = rho*x1 + e1
    d = c*c*s
    D = d-a*e0+e1
    W = (c*s-e0)**2
    check(x2-2*x1+x0 == D, 'denominator identity')
    check((x1-x0)**2 == W, 'numerator identity')
    if D:
        check(x0-(x1-x0)**2/(x2-2*x1+x0) == s-W/D, 'Aitken identity')
    ec = d/(a+1)
    check(d-(a+1)*eta == d-a*eta-eta, 'minimum denominator')
    check(ec > 0, 'strict threshold')
    b = c*s-ec
    check(b == 2*c*s/(3-rho) and b > 0, 'nonzero corner numerator')
    K = b**4/(8*a*ec**2)
    C = b**4/(4*a*ec**2)
    check(K == 2*s*s/(a*(3-rho)**2), 'critical tail constant')
    check(C == 2*K, 'critical risk coefficient')

# Evaluate the exactly derived critical corner integral, not a Monte Carlo estimate.
def critical_tail(t, rho=.5, s=1.0):
    c, a = 1-rho, 2-rho
    eta = c*c*s/(a+1)
    b = c*s-eta
    T = a*(t+s)-2*b
    u = (2*b*b)/(T+sqrt(T*T-4*b*b))
    assert 0<u<2*eta
    return ((b*b*u+b*u*u+u**3/3)/(t+s)-a*u*u/2)/(4*eta*eta)

K = 16/75
for t in [10**3, 10**4, 10**5]:
    estimate = t*t*critical_tail(t)
    check(abs(estimate/K-1) < 0.002, 'critical t^-2 tail')

# Independent conditional integration of the noncritical tail using the original
# two-dimensional uniform square, integrating one direction exactly.
def tail_above(t, eta, rho=.5, s=1.0, n=10000):
    a, c, d = 2-rho, 1-rho, (1-rho)**2*s
    step = 2*eta/n
    accum = 0.
    for j in range(n):
        x = -eta+(j+.5)*step
        root = a*x-d
        W = (c*s-x)**2
        plus = max(0., min(eta, root+W/(t+s))-max(-eta, root))
        minus = max(0., min(eta, root)-max(-eta, root-W/(t-s)))
        accum += plus+minus
    return accum/(2*eta*n)

eta = .2
T = 403/1296
for t in [200., 1000., 5000.]:
    check(abs(t*tail_above(t, eta)-T) < 5e-5, 'interior t^-1 tail')

# Integrate over the second uniform error analytically, then use a logarithmic
# change of variables near the corner to resolve the developing logarithm.
def square_risk(eta, n=1600):
    rho, s = .5, 1.
    a, c = 2-rho, 1-rho
    tau = c*c*s-(a+1)*eta
    assert tau>0
    B = 2*eta
    xmax = log(1+a*B/tau)
    def integrand(z):
        eu = exp(z)
        u = tau*(eu-1)/a
        h = tau*eu
        w = (c*s-eta+u)**2
        j = s*s*B - 2*s*w*log((h+B)/h) + w*w*(1/h-1/(h+B))
        return j*tau*eu/a
    # composite Simpson
    h=xmax/n
    sm=integrand(0)+integrand(xmax)
    for k in range(1,n):
        sm+=(4 if k%2 else 2)*integrand(k*h)
    return h*sm/(3*4*eta**2)

C=32/75
r4=square_risk(.1*(1-1e-4))
r5=square_risk(.1*(1-1e-5))
r6=square_risk(.1*(1-1e-6))
check(abs((r5-r4)-C*log(10)) < 0.014, 'critical log slope 4->5')
check(abs((r6-r5)-C*log(10)) < 0.004, 'critical log slope 5->6')

# Exact rational examples and sign of the positive-length pole intersection.
a, c, d = Q(3,2), Q(1,2), Q(1,4)
eta = Q(1,5)
L = max(-eta,(d-eta)/a)
U = min(eta,(d+eta)/a)
check((L,U)==(Q(1,30),Q(1,5)), 'exact line segment')
check(((U-c)**3-(L-c)**3)/(6*eta**2)==Q(403,1296),'exact supercritical tail coefficient')

print(f'PASS: {N} checks; critical tail K=16/75, squared-risk logarithm C=32/75, supercritical T=403/1296')
