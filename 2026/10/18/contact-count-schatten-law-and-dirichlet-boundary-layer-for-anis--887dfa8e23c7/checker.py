#!/usr/bin/env python3
"""Finite diagnostics for singular spectra and Dirichlet critical scaling.

Analytical statements for arbitrary dimensions and all degrees require the proof;
finite checks here are independently recomputed diagnostics only.
"""
from itertools import product
from fractions import Fraction
from math import comb, prod, exp

checks=0

def assert_eq(a,b):
    global checks
    assert a==b, (a,b)
    checks+=1

def assert_close(a,b,tol=1e-10):
    global checks
    assert abs(a-b)<=tol, (a,b,tol)
    checks+=1

def compositions(n,d):
    if d==1:
        yield (n,)
    else:
        for a in range(n+1):
            for rest in compositions(n-a,d-1):
                yield (a,)+rest

def squared_sigma(n,u):
    d=len(u)
    return sum((prodpow(u,a) for a in compositions(n,d)),Fraction(0))/comb(n+d-1,d-1)

def prodpow(u,a):
    z=Fraction(1)
    for x,k in zip(u,a):z*=x**k
    return z

# (1) Exact Gram-row and generating-function coefficient identities.
options=[Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]
for d in (2,3,4):
    for u in product(options,repeat=d):
        v=[squared_sigma(n,u) for n in range(8)]
        assert_eq(v[0],1)
        assert_eq(all(0<=v[i+1]<=v[i]<=1 for i in range(7)),True)
        # Coefficient of the rational generating function, via recurrence:
        # h_n = (1/n)sum_{k=1}^n p_k h_{n-k}.
        h=[Fraction(1)]
        for n in range(1,8):
            h.append(sum(sum(x**k for x in u)*h[n-k] for k in range(1,n+1))/n)
        for n in range(8):
            assert_eq(v[n]*comb(n+d-1,d-1),h[n])

# (2) Independent finite Gram row check for a representative anisotropic case.
for d,u in [(2,[.2,.8]),(3,[0.,.5,1.]),(4,[.12,.23,.47,.85])]:
    for n in range(12):
        row=[1.]
        # Basis input z^alpha maps to (prod_j r_j^alpha_j)z^n/sqrt(N_n),
        # so its matrix row has these entries.
        row=[float(prod(x**(a/2) for x,a in zip(u,alph)))/comb(n+d-1,d-1)**.5 for alph in compositions(n,d)]
        assert_close(sum(x*x for x in row),float(squared_sigma(n,[Fraction(str(x)) for x in u])))

# (3) Dirichlet(1,1) continuum Laplace transform and exact nonasymptotic Jensen gap.
def phi2(t1,t2):
    return exp(-t1) if t1==t2 else (exp(-t1)-exp(-t2))/(t2-t1)

def candidate_N(N,t1,t2):
    return sum(exp(-(t1*j+t2*(N-j))/N) for j in range(N+1))/(N+1)

def simpson(f,m=20000):
    assert m%2==0
    h=1/m
    return h/3*(f(0)+f(1)+4*sum(f((2*k-1)*h) for k in range(1,m//2+1))+2*sum(f(2*k*h) for k in range(1,m//2)))

for t1,t2 in [(0,0),(0,1),(0,3),(1.5,2.1),(3,8),(0,10)]:
    Phi=phi2(t1,t2)
    upper=(t1-t2)**2/12
    for N in (1,2,3,4,5,8,16,30,100,300,1000):
        v=candidate_N(N,t1,t2)
        assert_eq(v+1e-12>=Phi,True)
        assert_eq(v-Phi<=upper/N+1e-12,True)
    # First-order asymptotic coefficient 0.5 * E_{x uniform}
    # [exp(-t.x) Var_x(t)]
    coeff=.5*(t1-t2)**2*simpson(lambda x:exp(-t1*x-t2*(1-x))*x*(1-x),m=4000)
    for N in (300,1000,3000):
        v=candidate_N(N,t1,t2)
        assert_eq(abs(N*(v-Phi)-coeff)<max(.03,5*(1+t1+t2)**3/N),True)

print('PASS:',checks,'finite diagnostics (exact fractions and numerical)')
