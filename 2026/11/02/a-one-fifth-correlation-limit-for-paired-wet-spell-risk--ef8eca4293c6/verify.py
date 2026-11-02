#!/usr/bin/env python3
"""Standalone exact arithmetic checks for paired wet-spell avoidance.

These finite checks complement, but do not replace, the analytic proof.
"""
from fractions import Fraction as Q
from itertools import product

checks = 0

def ck(predicate, message):
    global checks
    checks += 1
    if not predicate:
        raise AssertionError(message)


def survival(n, q):
    """Stationary fair two-state chain with self-transition probability q."""
    a, b = Q(1, 2), Q(1, 2)
    for _ in range(n - 1):
        a, b = q*a + (1-q)*b, (1-q)*a
    return a+b


def brute(n, q):
    total = Q(0)
    for seq in product((0, 1), repeat=n):
        if any(seq[i] == seq[i+1] == 1 for i in range(n-1)):
            continue
        w = Q(1, 2)
        for a, b in zip(seq, seq[1:]):
            w *= q if a == b else (1-q)
        total += w
    return total


def poly_add(x, y):
    return [ (x[i] if i < len(x) else Q(0)) + (y[i] if i < len(y) else Q(0)) for i in range(max(len(x), len(y)))]

def poly_mult(x, y):
    z = [Q(0)] * (len(x)+len(y)-1)
    for i,a in enumerate(x):
        for j,b in enumerate(y):
            z[i+j] += a*b
    return z

def poly_trim(x):
    while len(x)>1 and x[-1]==0:
        x.pop()
    return x

# Symbolically build the avoidance polynomials using Cayley-Hamilton.
f1, f2 = [Q(1)], [Q(1), Q(-1,2)]
P = [[Q(1)], f1, f2]
for n in range(3, 19):
    f1, f2 = f2, poly_trim(poly_add(poly_mult([Q(0),Q(1)],f2),poly_mult([Q(1),Q(-2),Q(1)],f1)))
    P.append(f2)
ck(P[4]==[Q(1),Q(-3,2),Q(1)],'four-day exact polynomial')
ck(P[5]==[Q(1),Q(-2),Q(2),Q(-1),Q(1,2)],'five-day exact polynomial')
for n in range(1, 14):
    for a,b in [(0,1),(1,5),(2,5),(1,2),(3,5),(3,4),(9,10),(1,1)]:
        q=Q(a,b)
        ck(survival(n,q)==brute(n,q),f'enumeration n={n}, q={q}')
        ck(survival(n,q)==sum((c*q**i for i,c in enumerate(P[n])),Q(0)),f'polynomial n={n}, q={q}')
for n in range(1,19):
    q=Q(3,5)
    pred=Q(9,10)*Q(4,5)**(n-1)+Q(1,10)*Q(-1,5)**(n-1)
    ck(survival(n,q)==pred,f'Perron-formula n={n}')
for a in range(0,21):
    q=Q(a,20)
    # The quadratic evaluated at 4/5 factors as minus the square.
    lhs=Q(4,5)**2-q*Q(4,5)-(1-q)**2
    ck(lhs==-(q-Q(3,5))**2,'spectral quadratic identity')
ck(survival(4,Q(3,4))==Q(7,16),'four-day optimum avoidance')
ck(survival(4,Q(0))==Q(1),'alternating boundary')
ck(survival(4,Q(1))==Q(1,2),'frozen boundary')

# Analytic derivatives from the 2x2 Perron characteristic equation:
# at q=3/5: lambda+=4/5, lambda-= -1/5, lambda+'=0,
# lambda- '=1, lambda+''=2, A=9/10, A'=-3/5.
from math import sqrt
q0=0.6
r=sqrt(q0*q0+4*(1-q0)**2)
lam=(q0+r)/2; mu=(q0-r)/2
A=(1-q0/2-mu)/(lam-mu)
ck(abs(lam-0.8)<1e-14 and abs(mu+0.2)<1e-14,'eigenvalue basepoint')
ck(abs(A-0.9)<1e-14,'Perron prefactor basepoint')

def f_and_prime(n,q):
    a=b=0.5
    da=db=0.0
    for _ in range(n-1):
        na=q*a+(1-q)*b
        nb=(1-q)*a
        nda=q*da+(1-q)*db+a-b
        ndb=(1-q)*da-a
        a,b,da,db=na,nb,nda,ndb
    return a+b, da+db

def stationary_root(n):
    lo,hi=0.6,0.9
    if not (f_and_prime(n,lo)[1]<0<f_and_prime(n,hi)[1]):
        raise AssertionError('root bracket for n=%s'%n)
    for i in range(80):
        m=(lo+hi)/2
        if f_and_prime(n,m)[1]<0:lo=m
        else:hi=m
    return (lo+hi)/2

for n in (4,5,6,8,10,20,50,100,250,500):
    r=stationary_root(n)
    ck(0.6<r<0.76,f'critical point interior n={n}')
    ck(f_and_prime(n,r)[0] < f_and_prime(n,0.6)[0]+1e-12, f'beats basepoint n={n}')
    ck(f_and_prime(n,r)[0] < f_and_prime(n,0.9)[0]+1e-12, f'beats high persistence n={n}')
ck(abs(stationary_root(4)-.75)<1e-12,'finite optimality')
for n in (100,250,500):
    scaled=n*(stationary_root(n)-.6)
    ck(abs(scaled-Q(4,15)) < .007,'large-horizon coefficient n=%s'%n)
print(f'VERIFY_OK assertions={checks}')
