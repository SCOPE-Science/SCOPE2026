#!/usr/bin/env python3
"""Exact-rational/logarithmic checks and numerical cross-checks of a two-block logistic threshold theorem."""
from fractions import Fraction as Q
from decimal import Decimal as D, getcontext
from random import Random
import math

getcontext().prec = 78
EPS = D('1e-66')

def dec(q):
    return D(q.numerator) / D(q.denominator)

def logistic(z):
    return D(1) / (D(1) + (-z).exp())

def check_extremum(a, b, d):
    lam = 1-a-b
    assert lam > 0
    # For rational d, 4*atanh(d) equals twice the log of this rational ratio.
    odds = (1+d)/(1-d)
    beta = D(2)*dec(odds).ln() / (dec(lam)*dec(d))
    field = -beta*(D('0.5')+(dec(a)-dec(b))*dec(d)/2)
    x1, x2 = (1-dec(d))/2, (1+dec(d))/2
    Bx1 = (1-dec(a))*x1 + dec(a)*x2
    Bx2 = dec(b)*x1 + (1-dec(b))*x2
    assert abs(logistic(field+beta*Bx1)-x1)<EPS
    assert abs(logistic(field+beta*Bx2)-x2)<EPS
    # The exact eigenvalues of the Jacobian at this extremal state.
    H = (1-dec(d)**2)*dec(odds).ln()/(D(2)*dec(d))
    mu_h = -1+H/dec(lam)
    mu_t = -1+H
    assert mu_t<0
    # Reverse orientation: opposite stimulus offset and opposite activity gap.
    field2 = -beta*(D('0.5')-(dec(a)-dec(b))*dec(d)/2)
    u1, u2 = x2, x1
    assert abs(logistic(field2+beta*((1-dec(a))*u1+dec(a)*u2))-u1)<EPS
    assert abs(logistic(field2+beta*(dec(b)*u1+(1-dec(b))*u2))-u2)<EPS
    # Identifiability of directed weights from the two maximizing stimuli.
    delta = (field2-field)/(beta*dec(d))
    lam2 = D(2)*dec(odds).ln()/(beta*dec(d))
    assert abs((D(1)-lam2+delta)/2-dec(a))<EPS
    assert abs((D(1)-lam2-delta)/2-dec(b))<EPS
    return beta, mu_h, mu_t

cases = [
    (Q(1,8),Q(3,8),Q(1,2)),
    (Q(1,8),Q(3,8),Q(9,10)),
    (Q(1,10),Q(1,4),Q(1,3)),
    (Q(1,3),Q(1,9),Q(4,5)),
    (Q(1,17),Q(1,13),Q(7,11)),
    (Q(3,10),Q(1,5),Q(3,4)),
]
for a,b,d in cases:
    check_extremum(a,b,d)
first = check_extremum(Q(1,8),Q(3,8),Q(1,2))
last = check_extremum(Q(1,8),Q(3,8),Q(9,10))
assert first[1] > 0, 'the smaller-contrast maximizing state must be a saddle'
assert last[1] < 0, 'the larger-contrast maximizing state must be a stable sink'

rng=Random(518200)
checked=0
for _ in range(2000):
    x1=D(str(rng.uniform(.0001,.98)))
    d=D(str(rng.uniform(.00001,float((D(1)-x1)*D('.999')))))
    x2=x1+d
    # K = secant slope of logit, bounded from below by its centered secant.
    g=lambda z:(z/(1-z)).ln()
    K=(g(x2)-g(x1))/d
    psi=D(2)*((1+d)/(1-d)).ln()/d
    assert K+EPS>=psi
    checked+=1

# H is strictly decreasing and the threshold psi is strictly increasing.
prevH=D(1)
prevPsi=D(4)
for j in range(1,1000):
    d=D(j)/D(1000)
    atanh=((1+d)/(1-d)).ln()/2
    H=(1-d*d)*atanh/d
    psi=4*atanh/d
    assert D(0)<H<prevH and psi>prevPsi
    prevH,prevPsi=H,psi

# Difference contracts at least exp(-t) if a+b>=1, independently of beta.
# This checks signs of the exact difference vector field over a finite grid.
for a,b in [(0.6,0.6),(0.9,0.3),(0.4,0.6)]:
    for i in range(1,10):
        for j in range(i):
            x1,x2=j/10,i/10
            beta=9.0
            h=-4.0
            sig=lambda z: 1/(1+math.exp(-z))
            f1=sig(h+beta*((1-a)*x1+a*x2))
            f2=sig(h+beta*(b*x1+(1-b)*x2))
            # d/dt(x2-x1) = -(x2-x1)+(f2-f1).
            assert f2-f1<1e-13

print('PASS: 6 high-precision constructed extremal pairs, both orientations and exact inverse parameters')
print('PASS: analytic Jacobian signs checked (saddle and sink examples)')
print(f'PASS: {checked} independent logit-secant inequalities')
print('PASS: 999 monotonicity checks for the sharp contrast and stability threshold functions')
print('PASS: 135 disassortative-difference sign checks')

# For the symmetric critical representative a=b=1/4, beta=8,
# field=-4, the invariant line x1+x2=1 gives d'=-d+tanh(d).
# This checks the sharp algebraic coefficient derived analytically.
y=0.6
hstep=0.2
for _ in range(50000):
    def rhs(q): return -q+math.tanh(q)
    k1=rhs(y)
    k2=rhs(y+hstep*k1/2)
    k3=rhs(y+hstep*k2/2)
    k4=rhs(y+hstep*k3)
    y+=hstep*(k1+2*k2+2*k3+k4)/6
assert abs(math.sqrt(10000)*y-math.sqrt(1.5))<0.02, (y,math.sqrt(10000)*y)
print('PASS: critical sharp algebraic relaxation example (Runge-Kutta cross-check)')
