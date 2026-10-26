"""Exact finite-state and large-index diagnostics for alternating-memory elephant walks.

Run with Python 3.10+; requires only the standard library. Finite tests are
checks of algebra, not proof of infinite-time assertions.
"""
from fractions import Fraction
from collections import defaultdict
import math

checks=0

def assert_eq(a,b,msg):
    global checks
    assert a==b,(msg,a,b)
    checks+=1

def assert_approx(a,b,tol,msg):
    global checks
    assert abs(a-b)<tol,(msg,a,b,tol)
    checks+=1

for delta in (Fraction(-1),Fraction(-2,3),Fraction(-1,2),
              Fraction(0),Fraction(1,2),Fraction(2,3),Fraction(1)):
    dist={-1:Fraction(1,2),1:Fraction(1,2)}
    v=Fraction(1)
    moments={1:v}
    for n in range(1,12):
        a=delta * (-1 if n%2 else 1)
        next_dist=defaultdict(Fraction)
        for s,prob in dist.items():
            pplus=(1+a*Fraction(s,n))/2
            assert Fraction(0)<=pplus<=Fraction(1)
            next_dist[s+1]+=prob*pplus
            next_dist[s-1]+=prob*(1-pplus)
        dist=dict(next_dist)
        v=(1+2*a/Fraction(n))*v+1
        actual=sum(prob*s*s for s,prob in dist.items())
        assert_eq(sum(dist.values()),Fraction(1),(delta,n,'mass'))
        assert_eq(sum(s*prob for s,prob in dist.items()),Fraction(0),(delta,n,'mean'))
        assert_eq(actual,v,(delta,n,'moment'))
        moments[n+1]=v
    for m in range(1,6):
        z=moments[2*m]-2*m
        znext=moments[2*m+2]-2*(m+1)
        F=1+delta*(1-2*delta)/Fraction(m*(2*m+1))
        assert_eq(znext,F*z-4*delta*delta/Fraction(2*m+1),
                  (delta,m,'pair-recurrence'))
        odd=(1+delta/Fraction(m))*moments[2*m]+1
        assert_eq(odd,moments[2*m+1],(delta,m,'odd-reconstruction'))

# A second numerical implementation never uses the pair recursion.
# A log-slope is more diagnostic than a ratio because the constant-order
# variance correction can be substantial even at large n.
for d in (-1.,-.7,-.25,.25,.7,1.):
    x=1.
    even={}
    for n in range(1,160001):
        a=d*(-1 if n%2 else 1)
        x=(1+2*a/n)*x+1
        if n+1 in (4000,40000,160000):even[n+1]=x
    for low,high in ((4000,40000),(40000,160000)):
        slope=((even[high]-high)-(even[low]-low))/math.log(high/low)
        assert_approx(slope,-2*d*d,0.02,
                      (d,low,high,'logarithmic-slope'))

# Brownian-scale covariance prediction: exact conditional expectation and
# exact variance recur; products cover any two observation times.
for d in (-.65,.0,.8):
    nmax=24000
    v=[0.]*(nmax+1)
    v[1]=1.
    for n in range(1,nmax):
        a=d*(-1 if n%2 else 1)
        v[n+1]=(1+2*a/n)*v[n]+1
    for N in (1000,4000,12000):
        i=N//4;j=(3*N)//4
        ratio=1.
        for k in range(i,j):
            ratio*=1+d*(-1 if k%2 else 1)/k
        cov=v[i]*ratio
        assert_approx(cov/N,.25,0.015,(d,N,'diffusive-covariance'))
print(f'PASS: {checks} exact-rational/numerical assertions')
print('Limits checked only analytically in RESULT.md; no finite run proves convergence.')
