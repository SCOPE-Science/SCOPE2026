#!/usr/bin/env python3
"""Finite numerical cross-checks of annular affine-projector norm identities.

Requires only Python's standard library. These numerical tests complement,
but do not replace, the analytical arguments given in RESULT.md.
"""
import math

N_ASSERTIONS = 0

def check(condition, message):
    global N_ASSERTIONS
    N_ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)

def H(R, b):
    if R <= b:
        return 0.0
    return ((2.0 * R * R + b * b) / 3.0) * math.sqrt(R * R - b * b) - b * R * R * math.acos(b / R)

def N(r):
    b = (1.0 + r * r) / 4.0
    return 1.0 + 2.0 * (H(1.0, b) - H(r, b)) / (math.pi * b * (1.0 - r * r))

def B(r):
    b = (1.0 + r * r) / 4.0
    return 1.0 + 2.0 * H(1.0, b) / (math.pi * b * (1.0 - r * r))

def simpson(f, a, b, n=1600):
    assert n > 0 and n % 2 == 0
    dx = (b - a) / n
    total = f(a) + f(b)
    for k in range(1,n):
        total += (4 if k % 2 else 2) * f(a + k * dx)
    return dx * total / 3

def H_quadrature(R,b):
    if R <= b: return 0.0
    return simpson(lambda t: 4*(R-b)*(1-t)*(R-(R-b)*(1-t)**2-b)*math.sqrt(max(0.0,R*R-(R-(R-b)*(1-t)**2)**2)),0,1,1000)

def direct_angle_radial(r, evalrad=1.0, nrad=350, ntheta=1200):
    """Independent two-dimensional midpoint sum for the absolute affine kernel."""
    s = r*r
    total = 0.0
    for j in range(nrad):
        u = s + (1-s)*(j+.5)/nrad
        rho = math.sqrt(u)
        k = 4*evalrad*rho/(1+s)
        h = 0.0
        for i in range(ntheta):
            angle = (i+.5)*2*math.pi/ntheta
            h += abs(1 + k*math.cos(angle))
        total += h/ntheta
    return total/nrad

rstar=2-math.sqrt(3)
D=4*3**1.25/(15*math.pi*math.sqrt(rstar)*(1-rstar*rstar))
check(abs(rstar-(1+rstar*rstar)/4)<1e-14,'tangent radius')
check(abs(N(0)-(11*math.sqrt(15)/(8*math.pi)+2*math.asin(.25)/math.pi))<1e-12,'disk endpoint')
check(abs(N(.99999)-(1/3+2*math.sqrt(3)/math.pi))<2e-5,'circle endpoint')

for j in range(1,96):
    r=(j-.5)/96
    b=(1+r*r)/4
    check(abs(H(1,b)-H_quadrature(1,b))<2e-7, 'cap outer integral '+str(j))
    if r>b:
        check(abs(H(r,b)-H_quadrature(r,b))<2e-7, 'cap inner integral '+str(j))

samples=[j/250 for j in range(250)]
for a,b in zip(samples,samples[1:]):
    check(N(a)>N(b),'strictly decreasing sample')
for r in [0.0,.08,rstar-.001,rstar+.001,.4,.7,.92]:
    val = direct_angle_radial(r)
    check(abs(val-N(r))<3e-5, 'independent 2D integral '+str(r))
    for rad in [.0,.2,.5,.8,.99]:
        check(direct_angle_radial(r,rad,nrad=70,ntheta=320)<N(r)+2e-4,'inner evaluation bound')

for eps in [1e-2,5e-3,2e-3,1e-3]:
    ratio=(B(rstar+eps)-N(rstar+eps))/(eps**2.5)
    check(abs(ratio-D)<1e-2,'5/2 tangency exponent '+str(eps))

print('PASS',N_ASSERTIONS,'finite consistency checks')
print('r_star:',format(rstar,'.15f'))
print('cusp coefficient:',format(D,'.15f'))
print('disk:',format(N(0),'.15f'))
print('circle limiting:',format(1/3+2*math.sqrt(3)/math.pi,'.15f'))
