"""Reproduce checks for the stabilized ETDRK2 quadratic test problem.
Requires Python 3 standard library only. Finite tests supplement the proof.
"""
import math
import random
from fractions import Fraction

checks = 0

def test(p, msg):
    global checks
    if not p:
        raise AssertionError(msg)
    checks += 1


def gain(z, t):
    s = -math.expm1(-z)
    q = 1.0 - s / z
    return 1.0 - t * s * (1.0 + (1.0-t) * q)


def direct_gain(h, ell, a, beta):
    d = ell + beta
    s = -math.expm1(-h*d)
    v = math.exp(-h*d) + s * (beta-a) / d
    phi2 = (math.expm1(-h*d) + h*d) / ((h*d)**2)
    return v + h * phi2 * (beta-a) * (v-1.0)

rng = random.Random(720240223)
for _ in range(750):
    ell = rng.uniform(0.02, 5)
    a = rng.uniform(0.0, 9)
    beta = rng.uniform(0, 12)
    h = rng.uniform(.02, 12)
    z = h * (ell+beta)
    t = (ell+a)/(ell+beta)
    x, y = gain(z,t), direct_gain(h,ell,a,beta)
    test(abs(x-y) < 2.e-12 * (1+abs(x)), 'ETDRK2 gain mismatch')

for _ in range(1200):
    z = math.exp(rng.uniform(-8, 7))
    t = rng.uniform(.00001, 2)
    R = gain(z,t)
    test(-1.0-1e-14 < R < 1.0+1e-14, 'stable region')

for _ in range(500):
    t = rng.uniform(2.005, 8)
    R = gain(5000.0, t)
    test(R > 1., 'large-step instability beyond threshold')

# Exact integer coefficient proof: 4z e^(2z) R(z,3/2)
# coefficient n! times z^n = 2^(n-1)(n-6) + 3n + 6.
for n in range(1,401):
    coeff = (2**(n-1))*(n-6)+3*n+6
    test(coeff>0, 'positivity coefficient')

# Certified rational upper bound on exp(-6) from finite positive exponential sum.
partial = sum((Fraction(6)**k/Fraction(math.factorial(k))) for k in range(14))
test(partial > 400, 'exp(6) rational lower bound')
wbound=Fraction(1,400)
test(-5 + 616*wbound < 0, 'negative intermediate gain')

for _ in range(400):
    z = math.exp(rng.uniform(-7,9))
    test(gain(z,1.5)>0., 'reentrant positivity')

ell,a=1.0,2.0
for beta in (2.0,19/11,1.0):
    t=(ell+a)/(ell+beta)
    test(t<=2, 'energy-stable example')
test(abs(gain(6.0,1.0)-math.exp(-6.0))<1e-14, 'first gain')
test(gain(6.0,11/10)<0, 'middle gain')
test(gain(6.0,3/2)>0, 'last gain')

# Minimax long-step attenuation on two eigenvalues.
for _ in range(350):
    ell = rng.uniform(.01,9)
    low = rng.uniform(.01,6)
    high= low+rng.uniform(.02,20)
    opt=(low+high)/2
    target=((high-low)/(low+high+2*ell))**2
    f=lambda b:max((b-low)**2,(b-high)**2)/(b+ell)**2
    test(abs(f(opt)-target)<1e-12, 'minimax closed form')
    trial=opt*(.1+3*rng.random())
    test(f(trial)>=target-1e-12, 'minimax inequality')

print('PASS %d deterministic checks; mathematical universality is established by the accompanying analytic proof.' % checks)
