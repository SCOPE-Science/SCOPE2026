#!/usr/bin/env python3
"""Independent finite checks of the exact harmonic majorant for a Poisson angular law.

This script checks algebraic and numerical identities, not the infinite theorem.
No external dependencies are required.
"""
import math

PI = math.pi
LAMBDA = 1.0 / (3.0 - 4.0 * math.sin(PI / 9.0) ** 2)
J = 2.0 / PI * (2.0 * math.cos(PI / 9.0) - 1.0)

def g(x):
    return math.cos(x) + LAMBDA * math.cos(3*x)

def poisson_abs_integral(t, phi, theta):
    # Stable, truncated Poisson probabilities; missing tails < 1e-14 at tested t.
    mode = int(t)
    lo = max(0, int(t - 12*math.sqrt(t)))
    hi = int(t + 12*math.sqrt(t)) + 1
    v = []
    for n in range(lo, hi):
        p = math.exp(-t + n*math.log(t) - math.lgamma(n+1))
        v.append(p)
    return sum(w*abs(g(n*phi+theta)) for n,w in zip(range(lo,hi),v))

assert abs(g(7*PI/18)) < 1e-13
assert g(0) > 0 and g(PI/2) < 0
assert abs(LAMBDA - 0.39493084363469844) < 1e-13
assert 2*J < 2/math.sqrt(3)

# Integrate using midpoint quadrature (independent of closed-form antiderivative).
N = 120000
j_quad = sum(abs(g(2*PI*(j+0.5)/N)) for j in range(N))/N
assert abs(j_quad-J) < 1e-9, (j_quad, J)

# Uniform angular-phase convergence for a representative irrational angle.
phi=PI/(2*math.sqrt(2))
for t in (800.0, 1600.0, 3200.0):
    values = [poisson_abs_integral(t,phi,2*PI*k/17) for k in range(17)]
    err = max(abs(v-J) for v in values)
    # These t are large enough for explicit low Fourier components to decay.
    assert err < 0.01, (t,err)

# Exact transform identity for a finite real sequence.
beta = 2.37
alpha = math.sqrt(beta*beta-1)
a=[1.5,-1.2,0.25,2.0,-0.7,3.1]
for n in range(len(a)):
    b=sum(math.comb(n,k)*a[k] for k in range(n+1))
    c=sum(math.comb(n,k)*(-1)**(n-k)*a[k] for k in range(n+1))
    x=[a[k]/alpha**k for k in range(n+1)]
    q=1/beta;p=alpha/beta
    yy=sum(math.comb(n,k)*q**(n-k)*p**k*x[k] for k in range(n+1))
    zz=sum(math.comb(n,k)*q**(n-k)*(-p)**k*x[k] for k in range(n+1))
    assert abs(yy-b/beta**n)<1e-11
    assert abs(zz-((-1)**n)*c/beta**n)<1e-11
print('checks passed; lambda=%.15f J=%.15f K=%.15f' % (LAMBDA,J,2*J))
