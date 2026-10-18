#!/usr/bin/env python3
"""Reproduction checks for a Gaussian-diagonal Hadamard regression model.

Uses only the Python standard library. Tests finite identities and limiting constants;
no finite test is a proof of the universal statements.
"""
import math
import random
from fractions import Fraction

checks = 0

def verify(ok, explanation):
    global checks
    if not ok:
        raise AssertionError(explanation)
    checks += 1


def sylvester(n):
    h = [[1]]
    while len(h) < n:
        h = [row + row for row in h] + [row + [-v for v in row] for row in h]
    return h


def weights(n, m, without_replacement):
    if without_replacement:
        return [Fraction(math.comb(n//2,j)*math.comb(n//2,m-j), math.comb(n,m))
                if 0 <= j <= n//2 and 0 <= m-j <= n//2 else Fraction(0)
                for j in range(m+1)]
    return [Fraction(math.comb(m,j),2**m) for j in range(m+1)]


def abs_cdf(t, rho):
    if t <= 0:
        return 0.0
    a2 = 1-rho*rho
    if a2 > 0 and t >= 1/math.sqrt(a2):
        return 1.0
    return (2/math.pi)*math.atan(t/math.sqrt(max(0.0, 1-a2*t*t)))


rng = random.Random(440029)
for n in (2,4,8,16):
    h = sylvester(n)
    for m in (1,2,3,4,5,7,10,16):
        for without_replacement in (False, True):
            if without_replacement and m > n:
                continue
            w = weights(n,m,without_replacement)
            verify(sum(w) == 1, ('mass',n,m,without_replacement))
            singular_expected = (Fraction(2*math.comb(n//2,m),math.comb(n,m))
                         if without_replacement and m<=n//2
                         else Fraction(0) if without_replacement else Fraction(2,2**m))
            verify(w[0]+w[-1] == singular_expected,
                   ('exceptional mass',n,m,without_replacement))
            for _ in range(35):
                rows = rng.sample(range(n),m) if without_replacement else rng.choices(range(n),k=m)
                ga,gb=rng.gauss(0,1),rng.gauss(0,1)
                sx = [(ga*h[i][0]+gb*h[i][1])/math.sqrt(2*m) for i in rows]
                sy = [(ga*h[i][0]-gb*h[i][1])/math.sqrt(2*m) for i in rows]
                eta = rng.choice((0.0,0.01,0.2,1.0))
                rho=sum(h[i][0]*h[i][1] for i in rows)/m
                lhs=sum(x*y for x,y in zip(sx,sy))/(sum(x*x for x in sx)+eta/2)
                rhs=(ga*ga-gb*gb)/(ga*ga+gb*gb+2*rho*ga*gb+eta)
                verify(abs(lhs-rhs) < 1e-8*(1+abs(rhs)),
                       ('regression reduction',n,m,without_replacement,eta,rho,lhs,rhs))

# Exact symmetric density/CDF from the Gaussian angle geometry.
for rho in (-.97,-.75,-.25,0,.35,.75,.97):
    for alpha in (.03,.07,.2,.5,.8,.93,.98):
        tan = math.tan(math.pi*alpha/2)
        quantile=tan/math.sqrt(1+(1-rho*rho)*tan*tan)
        verify(abs(abs_cdf(quantile,rho)-alpha)<1e-12,
               ('conditional quantile',rho,alpha))
    # deterministic equispaced angles provide independent geometric CDF checks
    angles = 16000
    values=[]
    for k in range(angles):
        phi=2*math.pi*(k+.5)/angles
        values.append(abs(math.cos(phi)/(1+rho*math.sin(phi))))
    for t in (.2,.5,1.,1.2):
        observed=sum(val<=t for val in values)/angles
        verify(abs(observed-abs_cdf(t,rho))<.0015,
               ('angular law',rho,t,observed,abs_cdf(t,rho)))

# The ridge singular-sector constant after the tangent substitution.
for eta in (1e-3,1e-5,1e-7):
    steps=100000
    integ=0.0
    for k in range(steps):
        theta=-math.pi/2+math.pi*(k+.5)/steps
        t=math.tan(theta)
        integ+=math.sin(theta)**2*math.exp(-eta*t*t/4)
    scaled=math.pi*integ/steps/math.sqrt(math.pi)
    verify(abs(scaled-math.sqrt(math.pi)/2)<1.2*math.sqrt(eta),
           ('singular moment asymptotic',eta,scaled))

# Finite exact mixture probabilities, with and without replacement.
for n in (4,8,16):
    for m in range(1,n+1):
        for scheme in (False,True):
            ws=weights(n,m,scheme)
            for t in (.3,.7,1.2,2.0):
                mix=sum(float(w)*(1-abs_cdf(t,(2*j-m)/m)) for j,w in enumerate(ws))
                verify(-1e-15 <= mix <= 1+1e-15, ('tail bounds',n,m,scheme,t))
                if m>=2 and t>m/(2*math.sqrt(m-1)):
                    extreme=float(ws[0]+ws[-1])*(2/math.pi)*math.atan(1/t)
                    verify(abs(mix-extreme)<1e-12, ('exact extreme tail',n,m,scheme,t,mix,extreme))

print('PASS:',checks,'deterministic identity, geometric probability, and asymptotic checks')
