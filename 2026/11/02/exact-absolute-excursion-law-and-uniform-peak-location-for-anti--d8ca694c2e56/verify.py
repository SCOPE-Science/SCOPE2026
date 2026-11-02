"""Reproducible checks for anti-periodic Brownian suprema.

Finite arithmetic/numerical diagnostics only; the infinite-dimensional
claims require the analytic heat-kernel and stationarity arguments.
Run: python3 anti_periodic_verify.py
"""
import math
from fractions import Fraction

assertions = 0

def check(statement):
    global assertions
    assert statement
    assertions += 1


def spectral_cdf(h):
    return 2.0 * math.fsum((1.0 if k % 2 else -1.0) *
                           math.exp(-k*k*math.pi**2/(8*h*h))
                           for k in range(1, 100))


def modular_cdf(h):
    if h == 0.0:
        return 0.0
    return 1.0 - 4*h*math.sqrt(2/math.pi) * math.fsum(
        math.exp(-2*(2*k+1)**2*h*h) for k in range(100))

# Check the full covariance, directly using W(t)-W(1)/2,
# and verify covariance-invariance under anti-periodic rotations.
for m in (5, 12, 31, 64):
    for i in range(m+1):
        for j in range(m+1):
            t, s = Fraction(i,m), Fraction(j,m)
            direct = min(t,s) - (t+s)/2 + Fraction(1,4)
            kernel = Fraction(1,4) - abs(t-s)/2
            check(direct == kernel)
for m in (7, 16, 37):
    for shift in range(m):
        for i in range(m):
            for j in range(m):
                si, sj = (i+shift)//m, (j+shift)//m
                ui, uj = (i+shift)%m, (j+shift)%m
                left = ((-1)**(si+sj))*(m-2*abs(ui-uj))
                right = m - 2*abs(i-j)
                check(left == right)

# Orthogonality identity for the Dirichlet heat kernel on (-h,h).
# Each integrated eigenmode contributes 2*(-1)^(k+1).
for k in range(1, 13):
    nodes = 1200
    accum = 0.0
    for j in range(nodes+1):
        v = j/nodes
        integrand = math.sin(k*math.pi*v)*math.sin(k*math.pi*(1-v))
        accum += (1 if j in (0,nodes) else (4 if j%2 else 2))*integrand
    normalized = accum / (3*nodes)
    check(abs(normalized - (-1)**(k+1)/2) < 2e-13)

# Poisson/Jacobi transformation: independently convergent spectral and
# Gaussian-image expansions of exactly the same probability.
for i in range(1, 401):
    h = 0.08 + i*0.006
    x, y = spectral_cdf(h), modular_cdf(h)
    check(abs(x-y) < 1.0e-12)
    check(-1.0e-12 <= x <= 1.0+1.0e-12)
for i in range(1, 400):
    h = 0.08 + i*0.006
    check(spectral_cdf(h) <= spectral_cdf(h+0.006)+1e-14)

# Numerical integration of the modular tail against the exact moment laws.
def simpson(f, a, b, steps=12000):
    assert steps % 2 == 0
    dx=(b-a)/steps
    s=f(a)+f(b)
    for i in range(1,steps):
        s += (4 if i%2 else 2)*f(a+i*dx)
    return dx*s/3

mean=simpson(lambda h: 1-(0.0 if h == 0.0 else spectral_cdf(h) if h < 0.5 else modular_cdf(h)), 0.0, 4.5)
second=simpson(lambda h: 2*h*(1-(0.0 if h == 0.0 else spectral_cdf(h) if h < 0.5 else modular_cdf(h))), 0.0, 4.5)
check(abs(mean-math.pi**1.5/(4*math.sqrt(2))) < 8e-10)
check(abs(second-(7.0/8)*1.2020569031595942854)<8e-10)

# Certified-leading-order consistency: the omitted terms are
# exponentially suppressed at both ends.
for h in (0.12,0.16,0.20,0.24):
    leading=2*math.exp(-math.pi**2/(8*h*h))
    check(abs(spectral_cdf(h)/leading-1)<1e-8)
for h in (2., 2.25, 2.5):
    leading=4*h*math.sqrt(2/math.pi)*math.exp(-2*h*h)
    check(abs((1-modular_cdf(h))/leading-1) < 1e-5)

print(f'PASS {assertions} deterministic assertions')
print(f'CDF P(S<1) = {spectral_cdf(1):.14f}')
print(f'E[S] = {mean:.14f}')
print(f'E[S^2] = {second:.14f}')
