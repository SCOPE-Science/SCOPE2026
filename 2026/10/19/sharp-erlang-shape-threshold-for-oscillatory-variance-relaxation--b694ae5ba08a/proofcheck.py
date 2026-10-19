#!/usr/bin/env python3
"""Independent symbolic and numerical checks for an Erlang-reset harmonic diffusion.

Requires sympy, numpy, scipy. Run: python proofcheck.py
Checks reproduce finite examples; the general pole and root arguments are analytic.
"""
from fractions import Fraction
import math
import numpy as np
import sympy as sp
from scipy.linalg import expm
from scipy.integrate import quad
from scipy.special import gammaln

checks = 0

def ok(test, what):
    global checks
    if not test:
        raise AssertionError(what)
    checks += 1


def matrices(m, a, r, sym=True):
    zero = sp.S(0) if sym else 0.0
    B = sp.zeros(2*m) if sym else np.zeros((2*m, 2*m))
    for j in range(m):
        B[j,j] = -r
        B[j,(j-1)%m] += r
        B[m+j,m+j] = -(a+r)
        if j:
            B[m+j,m+j-1] = r
    B[m,m-1] = r  # reset maps the age transform to one
    y0 = sp.zeros(2*m,1) if sym else np.zeros(2*m)
    y0[0] = y0[m] = 1
    return B,y0


def laplace_formula(m, a, r, s):
    x = s+a+r
    return sp.cancel((x**m-r**m)*(s+r)**m /
                     ((s+a)*x**m*((s+r)**m-r**m)))

s = sp.symbols('s')
for m in range(1,8):
    for a,r in [(sp.Rational(1,5),sp.S(1)),
                (sp.Rational(3,2),sp.S(1)),
                (sp.Rational(7,3),sp.S(2))]:
        B,y0=matrices(m,a,r)
        for s0 in [sp.S(2),sp.Rational(7,3)]:
            w=(s0*sp.eye(2*m)-B).inv()*y0
            empirical=sp.factor(sum(w[m:]))
            exact=laplace_formula(m,a,r,s0)
            ok(sp.simplify(empirical-exact)==0, ('resolvent',m,a,r,s0))
        pstar=sp.Matrix([sp.Rational(1,m)]*m)
        vz=(-(B[m:,m:])).inv() * (B[m:,:m]*pstar)
        ust=sp.factor(sum(vz))
        eq=r/(m*a)*(1-(r/(r+a))**m)
        ok(sp.factor(ust-eq)==0, ('stationary',m,a,r))

# The m=3 displaced pole is genuinely third order with the proposed coefficient.
for a,r in [(sp.Rational(1,5),sp.S(1)),(sp.Rational(1,2),sp.S(1)),
            (sp.S(1),sp.S(1)),(sp.S(3),sp.S(2))]:
    m=3
    F=laplace_formula(m,a,r,s)
    c=sp.limit((s+a+r)**3*F,s,-a-r)
    expected=r**2*a**3/(a**3+r**3)
    ok(sp.simplify(c-expected)==0, ('triple pole',a,r))
    ok(sp.simplify(sp.limit(s*F,s,0)-r/(m*a)*(1-(r/(r+a))**m))==0,
       ('stationary residue',a,r))

# Renewal convolution independent of the Erlang-stage matrix construction.
def survival(t,m,r):
    return math.exp(-r*t)*sum((r*t)**j/math.factorial(j) for j in range(m))

def renewal_density(t,m,r):
    if t==0:
        return 0.0
    z=0.0
    # Superposition of Gamma(m*n, r) renewal-event densities.
    for n in range(1,100):
        k=m*n
        term=math.exp(k*math.log(r)+(k-1)*math.log(t)-r*t-gammaln(k))
        z+=term
        if n>5 and term<1e-15: break
    return z

def independent_u(t,m,r,a):
    first=math.exp(-a*t)*survival(t,m,r)
    second=quad(lambda h: math.exp(-a*h)*survival(h,m,r)*renewal_density(t-h,m,r),
                0,t,epsabs=1e-11,epsrel=1e-11,limit=120)[0]
    return first+second

for m in [2,3,4,5]:
    for a,r in [(0.2,1.0),(1.0,1.0),(2.5,1.2)]:
        B,y0=matrices(m,a,r,sym=False)
        for t in [0.5,2.0,4.0]:
            u1=float(np.sum((expm(B*t)@y0)[m:]))
            u2=independent_u(t,m,r,a)
            ok(abs(u1-u2)<4e-10, ('renewal vs stage',m,a,r,t,u1,u2))

# Pole-location and exact non-cancellation checks for the least-damped modes.
for m in range(3,20):
    z=complex(math.cos(2*math.pi/m),math.sin(2*math.pi/m))
    for a,r in [(0.2,1.),(1.,1.),(2.,1.),(0.7,2.)]:
        C=(r*z/m)*(1-(r/(a+r*z))**m)/(a+r*(z-1))
        ok(abs(C)>1e-7, ('leading residue',m,a,r))
        for k in range(2,m-1):
            zk=complex(math.cos(2*math.pi*k/m),math.sin(2*math.pi*k/m))
            ok(zk.real<=z.real+1e-10,('root ordering',m,k))

# Representative finite-time crossings; all-time assertions are proved analytically.
for m,a,r,ts,sgns in [
 (3,1.,1.,[4.,8.,12.],[-1,1,-1]),
 (4,0.2,1.,[2.,4.,8.],[1,-1,1]),
 (6,0.2,1.,[2.,4.,8.,12.,16.],[1,-1,1,-1,1]),
]:
    B,y0=matrices(m,a,r,sym=False)
    ust=r/(m*a)*(1-(r/(r+a))**m)
    for t,sgn in zip(ts,sgns):
        diff=float(np.sum((expm(B*t)@y0)[m:]))-ust
        ok(diff*sgn>1e-10,('alternating witness',m,a,r,t,diff))

print(f'PASS {checks} independent symbolic, renewal-convolution, and spectral checks')
