#!/usr/bin/env python3
"""Numerical and symbolic cross-checks for radial Hermite-window concentration.
Requires Python 3, mpmath and sympy. Finite tests are not a proof of asymptotics.
"""
from math import pi, sqrt, exp, factorial
import mpmath as mp
import sympy as sp
mp.mp.dps=45
assertions=0

def check(x,msg):
    global assertions
    assertions+=1
    if not x:raise AssertionError(msg)

def charlier(q,k,t):
    c0=mp.mpf(1)
    if q==0:return c0
    c1=k-t
    for j in range(1,q):
        c0,c1=c1,(k-t-j)*c1-j*t*c0
    return c1

def density(q,k,t):
    return mp.exp(-t)*t**k/mp.factorial(k)*charlier(q,k,t)**2/(mp.factorial(q)*t**q)

def laguerre_density(q,k,t):
    m=min(q,k); d=abs(q-k)
    return mp.exp(-t)*mp.factorial(m)/mp.factorial(max(q,k))*t**d*mp.laguerre(m,d,t)**2

k,t=sp.symbols('k t')
C0=sp.Integer(1); C1=k-t
polys=[C0,C1]
for j in range(1,6):
    C0,C1=C1,sp.expand((k-t-j)*C1-j*t*C0)
    polys.append(C1)
for q in range(7):
    direct=sp.expand(sum((-1)**j*sp.binomial(q,j)*sp.ff(k,q-j)*t**j for j in range(q+1)))
    check(sp.simplify(polys[q]-direct)==0,f'Charlier generating coefficient order {q}')
for q in range(5):
    for k0 in range(8):
        for t0 in (mp.mpf('0.25'),mp.mpf('1.5'),mp.mpf('8')):
            lhs=density(q,k0,t0);rhs=laguerre_density(q,k0,t0)
            check(abs(lhs-rhs)<mp.mpf('1e-39'),f'Laguerre density q={q}, k={k0}')
for q in range(5):
    for t0 in (mp.mpf('1'),mp.mpf('8'),mp.mpf('30')):
        top=int(t0+35*mp.sqrt(t0)+150)
        s=mp.fsum(density(q,j,t0) for j in range(top))
        check(abs(s-1)<mp.mpf('1e-35'),f'Moyal normalization q={q} t={t0} sum={s}')

# Fixed-area annulus: Gauss-Legendre integration with high precision.
def annulus(q,k,a,w):
    return mp.quadgl(lambda t:density(q,k,t),[a,a+w],degree=8)

def modes(q,a,w):
    c=a+w/2; lo=max(0,int(c-6*mp.sqrt(c))-5);hi=int(c+6*mp.sqrt(c))+6
    vals=[annulus(q,j,a,w) for j in range(lo,hi)]
    j=max(range(len(vals)),key=lambda i:vals[i])
    return lo+j,vals[j]

def he(q,u):
    h0=mp.mpf(1)
    if q==0:return h0
    h1=u
    for j in range(1,q):h0,h1=h1,u*h1-j*h0
    return h1

def M(q):
    if q==0:return mp.mpf(1)
    if q==1:return 2/mp.e
    if q==2:return 8*mp.exp(-mp.mpf(5)/2)
    # stationary points from 2q He_{q-1} = u He_q
    x=sp.Symbol('x')
    poly=sp.expand(x*sp.hermite_prob(q,x)-2*q*sp.hermite_prob(q-1,x))
    roots=sp.nroots(poly,maxsteps=300)
    vals=[mp.exp(-mp.mpf(str(sp.re(root)))**2/2)*he(q,mp.mpf(str(sp.re(root))))**2/mp.factorial(q)
          for root in roots if abs(float(sp.im(root)))<1e-10]
    return max(vals)

print('Cross-checked Laguerre and Charlier eigen-densities plus Poisson normalization.')
for q in range(4):
    for a in (100,400,1600):
        a=mp.mpf(a);w=mp.mpf(2);c=a+w/2
        kstar,norm=modes(q,a,w)
        leading=w/mp.sqrt(2*mp.pi*c)*M(q)
        rel=norm/leading-1
        check(abs(rel)<mp.mpf('0.15'),f'large-radius q={q} a={a}: {rel}')
        if q==1:
            refined=leading*(1+mp.sqrt(2)/(6*mp.sqrt(c)))
            check(abs(norm/refined-1)<mp.mpf(5)/c,f'refined q=1 a={a}')
            check(abs((kstar-c)/mp.sqrt(c)+mp.sqrt(2))<mp.mpf('0.15'),f'lower-band winner a={a}')
        print('q=%d a=%d k=%d leading_ratio=%.9f'% (q,int(a),kstar,float(norm/leading)))
print('PASS',assertions,'cross-checks')
