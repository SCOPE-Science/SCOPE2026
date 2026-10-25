#!/usr/bin/env python3
"""Independent arithmetic checks for weighted Dirichlet affine projection norms.
Run: python checker.py
Only finite checks; the analytic proof supplies universal statements.
"""
import math
from fractions import Fraction as Q
from itertools import product
import mpmath as mp

mp.mp.dps = 55
checks = 0

def verify(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(msg)

def beta_cdf(a, b, x):
    return mp.betainc(a, b, 0, x, regularized=True)

def amplitude(S, p):
    a = mp.mpf(S) * mp.mpf(p)
    b = mp.mpf(S) - a
    t = a / (mp.mpf(S) + 1)
    return 1 + 2*(mp.mpf(S)*beta_cdf(a,b,t) - (mp.mpf(S)+1)*beta_cdf(a+1,b,t))

def exact_beta_cdf(a,b,t):
    # integer a,b and rational 0<=t<=1
    C = sum(Q((-1)**j*math.comb(b-1,j),a+j)*t**(a+j)
            for j in range(b))
    norm = Q(math.factorial(a-1)*math.factorial(b-1),math.factorial(a+b-1))
    return C/norm

def exact_amplitude(a,b):
    S=a+b; t=Q(a,S+1)
    return 1 + 2*(S*exact_beta_cdf(a,b,t) - (S+1)*exact_beta_cdf(a+1,b,t))

# Check reproducing kernel identities against exact Dirichlet second moments.
for alphas in [(1,1,1), (1,2,3), (2,4,1,3), (1,3,2,5,2), (4,1)]:
    S=sum(alphas); n=len(alphas)
    p=[Q(a,S) for a in alphas]
    def K(x,y): return (S+1)*sum(x[i]*y[i]/p[i] for i in range(n))-S
    vertices=[[Q(int(i==j)) for i in range(n)] for j in range(n)]
    for x in vertices:
        E_K=(S+1)*sum(x)-S
        verify(E_K==1,'constant reproduction')
        for j in range(n):
            E_j = (S+1)*sum(x[i]*Q(alphas[i]*(alphas[j]+int(i==j)),S*(S+1))/p[i] for i in range(n))-S*p[j]
            verify(E_j==x[j], 'affine coordinate reproduction')
        for i in range(n):
            verify(K(x,vertices[i])==K(vertices[i],x),'kernel symmetry')

# Exact rational beta integrals for dozens of integer parameter pairs.
for S in range(2,15):
    amplitudes=[]
    for a in range(1,S):
        b=S-a
        q=exact_amplitude(a,b)
        numer=amplitude(S,mp.mpf(a)/S)
        verify(abs(mp.mpf(q.numerator)/q.denominator-numer)<mp.mpf('1e-43'),'exact beta integral')
        verify(q>1 and q<1+2*S,'strict endpoint bounds')
        amplitudes.append(q)
    verify(all(amplitudes[i]>amplitudes[i+1] for i in range(len(amplitudes)-1)),'integer-shape order')
    if S>=2:
        # symmetric a=b=1 for S=2, plus the uniform-simplex specialization at alpha=1 and n=S.
        known=Q(2*S,1)*Q(S,S+1)**(S-1)-1
        verify(exact_amplitude(1,S-1)==known,'uniform simplex specialization')

# Non-integer fixed-total monotonicity at fine grids.
for S in [mp.mpf('0.1'),mp.mpf('0.7'),mp.mpf('2.5'),mp.mpf('9'),mp.mpf('41')]:
    vals=[amplitude(S,mp.mpf(k)/53) for k in range(1,53)]
    verify(all(vals[i]>vals[i+1] for i in range(len(vals)-1)),'fractional shape order')

# Fixed-dimensional, growing-concentration Gaussian scaling.
for n in [3,5,9]:
    gauss=mp.sqrt(2*(n-1)/mp.pi)
    vals=[amplitude(S,mp.mpf(1)/n)/mp.sqrt(S) for S in [300,1000,4000]]
    verify(abs(vals[-1]-gauss)<abs(vals[0]-gauss),'concentration Gaussian regime')

# Fixed per-coordinate alpha: Gamma centering amplitude.
for a in [mp.mpf('0.5'),mp.mpf('1'),mp.mpf('2')]:
    target=2*a**a*mp.exp(-a)/mp.gamma(a)
    for n in [15,60,250]:
        observed=amplitude(n*a,mp.mpf(1)/n)/n
        verify(abs(observed-target)<mp.mpf('0.08'),'Gamma asymptotic regime')

# Fixed total concentration: bounded limit (symmetric vectors grow in length).
for S in [mp.mpf('0.5'),mp.mpf('2'),mp.mpf('8')]:
    vals=[amplitude(S,mp.mpf(1)/n) for n in [30,120,600]]
    verify(abs(vals[-1]-(1+2*S))<abs(vals[0]-(1+2*S)),'fixed total regime')
    verify(all(vals[i]<vals[i+1] for i in range(2)),'fixed total approach direction')

# Numerical convexity/strict vertex dominance in the segment case.
for a,b in [(mp.mpf('0.6'),mp.mpf('1.2')), (mp.mpf('3'),mp.mpf('2'))]:
    S=a+b; p=a/S
    def kern(x,y):
        return (S+1)*(x*y/p+(1-x)*(1-y)/(1-p))-S
    def integ(x):
        den=mp.beta(a,b)
        # split at unique sign crossing (if interior), robust piecewise quadrature
        root=mp.findroot(lambda z: kern(x,z), (mp.mpf('0.01'),mp.mpf('0.99'))) if (kern(x,0)*kern(x,1)<0) else None
        cuts=[mp.mpf('0'),mp.mpf('1')]
        if root is not None and 0<root<1: cuts=[mp.mpf('0'),root,mp.mpf('1')]
        return sum(mp.quad(lambda y: abs(kern(x,y))*y**(a-1)*(1-y)**(b-1)/den,[cuts[j],cuts[j+1]]) for j in range(len(cuts)-1))
    maximum=max(amplitude(S,p),amplitude(S,1-p))
    for x in [mp.mpf('0'),mp.mpf('0.15'),mp.mpf('0.35'),mp.mpf('0.65'),mp.mpf('0.85'),mp.mpf('1')]:
        val=integ(x)
        verify(val<=maximum+mp.mpf('1e-40'),'vertex dominance')
        if x>0 and x<1:verify(val<maximum-mp.mpf('1e-9'),'strict interior dominance')

print(f'PASS {checks} deterministic assertions; universal theorem depends on supplied analytic proof.')
