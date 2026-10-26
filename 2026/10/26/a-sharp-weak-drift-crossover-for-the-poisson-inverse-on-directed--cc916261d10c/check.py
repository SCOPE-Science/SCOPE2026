"""Finite exact checks for the biased cyclic Poisson inverse.

Standard library only. This verifies finite identities at sampled sizes and
parameters; asymptotic statements are proved analytically in RESULT.md.
"""
from fractions import Fraction as F
from math import exp, expm1, sqrt

checks = 0


def ck(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def exact_kernel(n, eps):
    eps = F(eps)
    if eps == 0:
        return [F(n*n-1, 6*n)-F(k*(n-k), n) for k in range(n)]
    p = (1+eps)/2
    r = (1-eps)/(1+eps)
    return [(F(k,n)-F(n-1,2*n))/eps
            + r**k/(eps*(1-r**n)) - p/(n*eps**2)
            for k in range(n)]


def solve(A, b):
    n = len(A)
    A = [row[:] for row in A]
    b = b[:]
    for k in range(n):
        t = next(i for i in range(k,n) if A[i][k] != 0)
        A[k],A[t] = A[t],A[k]
        b[k],b[t] = b[t],b[k]
        z = A[k][k]
        for j in range(k,n):
            A[k][j] /= z
        b[k] /= z
        for i in range(n):
            if i == k:
                continue
            z = A[i][k]
            for j in range(k,n):
                A[i][j] -= z*A[k][j]
            b[i] -= z*b[k]
    return b


def independent_kernel(n, eps):
    eps = F(eps)
    p,q = (1+eps)/2,(1-eps)/2
    A = [[F(i==j)+F(1,n)
          -p*F(j==(i+1)%n)-q*F(j==(i-1)%n)
          for j in range(n)] for i in range(n)]
    b = [F(i==0)-F(1,n) for i in range(n)]
    return solve(A,b)


def continuum(beta,x):
    if beta == 0:
        return x*x-x+1/6
    return ((x-.5)/beta - 1/(2*beta**2)
            + exp(-2*beta*x)/(beta*(-expm1(-2*beta))))


def approximation(n,beta):
    h = exact_kernel(n,F(beta,n))
    return sum(abs(float(z)) for z in h)/(n*n)

for n in range(3,17):
    for eps in (F(0),F(1,9),F(1,3),F(2,3),F(1)):
        h = exact_kernel(n,eps)
        ck(h==independent_kernel(n,eps), 'matrix identity')
        ck(sum(h)==0, 'zero mean')
        ck(h[0] == max(h), 'diagonal column maximum')
        ck(h[0] > 0, 'positive column maximum')
        for k in range(1,n):
            p,q=(1+eps)/2,(1-eps)/2
            ck(h[k]-p*h[(k+1)%n]-q*h[(k-1)%n] == -F(1,n), 'Poisson recurrence')
        p,q=(1+eps)/2,(1-eps)/2
        ck(h[0]-p*h[1]-q*h[n-1]==1-F(1,n), 'delta')

# Independent limiting checks via fixed-grid Riemann quadrature.
for beta in (0, F(1,2), F(2), F(5)):
    n=1024
    actual=approximation(n,beta)
    limit=sum(abs(continuum(float(beta),(i+0.5)/n)) for i in range(n))/n
    ck(abs(actual-limit)<0.002, 'weak drift convergence')

for eps in (F(1,10), F(1,3), F(4,5), F(1)):
    n=2400
    e=float(eps); p=(1+e)/2; r=(1-e)/(1+e)
    h=[(k-(n-1)/2)/(n*e)+r**k/(e*(1-r**n))-p/(n*e*e) for k in range(n)]
    actual=sum(abs(z) for z in h)
    ck(abs(actual/(n/(4*float(eps)))-1)<0.025, 'drift dominated convergence')

print('CHECKS_PASSED', checks)
