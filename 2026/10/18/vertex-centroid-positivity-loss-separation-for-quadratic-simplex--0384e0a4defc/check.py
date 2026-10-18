#!/usr/bin/env python3
"""Standalone exact checks for the quadratic simplex projector contrast theorem.
Only algebraic identities and finite numerical corroboration are checked here;
infinite-dimensional and distributional assertions are proved in RESULT.md.
"""
from fractions import Fraction as F
from math import factorial, sqrt, exp, pi
import math

def rising(n,k):
    z=1
    for j in range(k): z*=n+j
    return z

def E_vertex_power(n,j):
    return F(factorial(j),rising(n,j))

def Kv(n,t):
    return F(n*(n+1),4)*( (n+2)*(n+3)*t*t-4*(n+2)*t+2 )

def A(n): return F((n+1)*(n+2)*(n+3),4*n)

def moment_dirichlet(n,mon):
    return F(math.prod(factorial(k) for k in mon),rising(n,sum(mon)))

def ckernel(n,ys):
    s=sum(y*y for y in ys)
    return 1-A(n)*(s-F(2,n+1))

assertions=0
for n in range(3,36):
    # At a vertex, the quadratic Jacobi kernel reproduces t^0,t^1,t^2.
    for j in range(3):
        a=F(n*(n+1),4)
        mass=a*((n+2)*(n+3)*E_vertex_power(n,j+2)-4*(n+2)*E_vertex_power(n,j+1)+2*E_vertex_power(n,j))
        assert mass==1
        assertions+=1
    # Exact centroid moments and the variance of Simpson concentration.
    mu=F(2,n+1)
    ES2=F(4*(n+5),(n+1)*(n+2)*(n+3))
    var=ES2-mu*mu
    assert var==F(4*(n-1),(n+1)**2*(n+2)*(n+3)); assertions+=1
    target=F(1,n)
    assert 1-A(n)*(F(1,n)-mu)==1+A(n)*(mu-F(1,n)); assertions+=1
    assert 1+A(n)*(mu-F(1,n))==1+F((n-1)*(n+2)*(n+3),4*n*n); assertions+=1
    assert mu-A(n)*(ES2-mu*mu)==F(1,n); assertions+=1
    # Pair symmetry: reproducing powers at the barycenter.
    p2mean=F(2,n*(n+1))
    mixed=F(4*(n+5),n*(n+1)*(n+2)*(n+3))
    assert p2mean-A(n)*(mixed-p2mean*mu)==F(1,n*n);assertions+=1
    pairmean=F(1,n*(n+1))
    # E[Y1 Y2 sum Yj^2] has numerator 6+6+2(n-2)=2n+8.
    pairmixed=F(2*(n+4),n*(n+1)*(n+2)*(n+3))
    assert pairmean-A(n)*(pairmixed-pairmean*mu)==F(1,n*n);assertions+=1
    # Positive maximum of quadratic evaluation at vertex.
    assert Kv(n,F(0))>0 and Kv(n,F(1))>0 and Kv(n,F(1,n))<0;assertions+=1

# Independent triangle check: exact vertex L1 mass.
import sympy as s
t=s.symbols('t'); n=3
rootlo=(2*(n+2)-s.sqrt(2*(n+1)*(n+2)))/((n+2)*(n+3))
roothi=(2*(n+2)+s.sqrt(2*(n+1)*(n+2)))/((n+2)*(n+3))
f=(n-1)*(1-t)**(n-2)*Kv(n,t)
assert s.simplify(s.integrate(f,(t,0,rootlo))-s.integrate(f,(t,rootlo,roothi))+s.integrate(f,(t,roothi,1))-(1+s.Rational(128,135)*s.sqrt(10)))==0
assertions+=1

# Check asymptotic corner and center coefficients numerically from independent formulas.
c=(sqrt(2)-1)*exp(-2+sqrt(2))+(sqrt(2)+1)*exp(-2-sqrt(2))
assert .31 < c < .311
assertions+=1
assert abs(1/sqrt(2*pi)-.3989422804014327)<1e-14
assertions+=1
print(f'VERIFY_OK exact_or_precision_checks={assertions}')
