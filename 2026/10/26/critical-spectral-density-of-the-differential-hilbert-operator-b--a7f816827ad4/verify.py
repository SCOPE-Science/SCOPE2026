"""Numerical consistency tests for the critical Mellin-density formulas.

Run with Python 3; uses only the standard library. These finite tests are not
proofs of any infinite-dimensional theorem.
"""
import cmath
import math


def simpson(f, a, b, n=30000):
    assert n % 2 == 0
    h = (b-a)/n
    total = f(a) + f(b)
    for j in range(1, n):
        total += (4 if j % 2 else 2) * f(a+j*h)
    return total*h/3


s = 0.25
c_squared = 3.75

def h(t):
    return math.exp(s*t)/(2*math.cosh(t/2))

def density(x):
    return math.pi**2/(math.cos(math.pi*s)**2+math.sinh(math.pi*x)**2)

for q, target in [(1, math.pi/2), (2, 2*math.pi**2)]:
    val = simpson(lambda x: density(x)**q, -8, 8, n=20000)/(2*math.pi)
    assert abs(val-target) < 2e-8, (q, val, target)
    print('Mellin moment', q, f'{val:.12f}')

for xi in [0.0, 0.3, 1.0]:
    numeric = simpson(lambda t: (h(t)*cmath.exp(-1j*xi*t)).real, -100, 100, n=40000) \
            + 1j*simpson(lambda t: (h(t)*cmath.exp(-1j*xi*t)).imag, -100, 100, n=40000)
    exact = math.pi/cmath.cos(math.pi*(s-1j*xi))
    assert abs(numeric-exact)<5e-8, (xi,numeric,exact)
    print('Fourier check', xi, f'{abs(numeric-exact):.3e}')

alpha = -0.5
delta = 0.2
beta = alpha+2+delta
cd = math.sqrt(math.gamma(beta+2)/math.gamma(alpha+2))

def exact_entry(n,k):
    logb = math.log(n+1)-math.log(n+k+1) \
        + 0.5*(math.lgamma(beta+2)+math.lgamma(n+1)
               -math.lgamma(n+beta+2)+math.lgamma(k+alpha+2)
               -math.lgamma(alpha+2)-math.lgamma(k+1))
    return math.exp(logb)

def model_entry(n,k):
    x=n+1; y=k+1
    return cd*x**(-delta/2)*(y/x)**s/(x+y)

max_scaled = 0.0
for n in range(80):
    for k in range(80):
        B=exact_entry(n,k); K=model_entry(n,k)
        scaled=abs(B/K-1)/(1/(n+1)+1/(k+1))
        max_scaled=max(max_scaled,scaled)
assert max_scaled < 5
print('finite gamma-ratio error scaling, max:', f'{max_scaled:.8f}')
print('closed-form HS coefficient 15*pi/8 =', f'{15*math.pi/8:.12f}')
print('closed-form S4 coefficient 225*pi*pi/16 =', f'{225*math.pi**2/16:.12f}')
print('ALL FINITE CHECKS PASSED')
