#!/usr/bin/env python3
"""Standalone numerical and rational checks of the stationary-density theorem.
Run: python CHECKER.py. Requires mpmath (pip install mpmath).
The infinite assertions follow from the analytical proof, not these tests.
"""
from fractions import Fraction
from math import factorial
import mpmath as mp

COUNT = 0

def check(condition, label):
    global COUNT
    if not condition:
        raise AssertionError(label)
    COUNT += 1


def coefficient(c, j, N):
    ans = Fraction(1)
    for k in range(N+1):
        if k != j:
            ans /= 1-c**(2*(k-j))
    return ans

# Independent finite-convolution partial fractions: product of characteristic
# functions of scaled Laplace variables equals rational sum of simple poles.
for c in (Fraction(1, 2), Fraction(2, 3), Fraction(3, 5)):
    for N in range(1, 10):
        B = [coefficient(c, j, N) for j in range(N+1)]
        check(sum(B) == 1, f'finite mixture total mass: {c=} {N=}')
        for z in (Fraction(0), Fraction(1, 5), Fraction(3, 2), Fraction(11, 3)):
            prod = Fraction(1)
            for j in range(N+1):
                prod /= (1+c**(2*j)*z)
            rhs = sum(B[j]/(1+c**(2*j)*z) for j in range(N+1))
            check(prod == rhs, f'exact partial fractions: {c=} {N=} {z=}')

mp.mp.dps = 130

def qprod(q):
    return mp.fprod(1-q**j for j in range(1, 210))

def density_series(c, ell, x, N=190):
    q=c*c
    qden=mp.mpf(1)
    ans=mp.mpf(0)
    for j in range(N):
        if j: qden *= 1-q**j
        term=(-1)**j * c**(j*j)*mp.exp(-abs(x)/(ell*c**j))/qden
        ans += term
    return ans/(2*ell*qprod(q))

def signed_right_derivative_series(c, ell, m, N=190):
    q=c*c
    qden=mp.mpf(1)
    ans=mp.mpf(0)
    for j in range(N):
        if j: qden *= 1-q**j
        ans += (-1)**j*c**(j*j-m*j)/qden
    return (-1)**m*ans/(2*ell**(m+1)*qprod(q))

def closed_derivative(c, ell, n, p0):
    return (-1)**n*p0*ell**(-2*n)*c**(-n*n)*mp.fprod(
        1-c**(2*j+1) for j in range(n))

for cs,es in [('0.30','1.00'),('0.50','1.00'),('0.70','1.20')]:
    c=mp.mpf(cs);ell=mp.mpf(es)
    p0=density_series(c,ell,mp.mpf('0'))
    check(p0>0, 'positive density at origin')
    # Right-hand odd derivatives must cancel exactly in the infinite sum.
    # A fixed 190-term truncation is vastly beyond the precision tested.
    for n in range(7):
        even=signed_right_derivative_series(c,ell,2*n)
        closed=closed_derivative(c,ell,n,p0)
        check(mp.almosteq(even,closed,rel_eps=mp.mpf('1e-70'),abs_eps=mp.mpf('1e-70')),
              f'even derivative identity: {cs=} {n=}')
        odd=signed_right_derivative_series(c,ell,2*n+1)
        check(abs(odd)<mp.mpf('1e-60'),f'odd derivative cancellation: {cs=} {n=}')
    for xs in ['0.04','0.08','0.15','0.35']:
        x=mp.mpf(xs)
        t=mp.log(ell/x);L=-mp.log(c)
        if t < L: continue
        n=int(mp.floor(t/L));
        if n < 1: continue
        poly=sum(closed_derivative(c,ell,j,p0)*x**(2*j)/mp.factorial(2*j) for j in range(n))
        truth=density_series(c,ell,x)
        error=abs(poly-truth)
        bound=p0*mp.exp(L-t*t/L)
        local_next=abs(closed_derivative(c,ell,n,p0))*x**(2*n)/mp.factorial(2*n)
        check(error <= local_next*(1+mp.mpf('1e-55'))+mp.mpf('1e-70'),
              f'Fourier Taylor remainder: {cs=} {xs=}')
        check(error <= bound*(1+mp.mpf('1e-55'))+mp.mpf('1e-70'),
              f'log-squared approximation envelope: {cs=} {xs=}')

print(f'PASS {COUNT} diagnostics: exact finite convolution, all-order jet, '
      'odd cancellation, and log-squared Taylor remainder.')
