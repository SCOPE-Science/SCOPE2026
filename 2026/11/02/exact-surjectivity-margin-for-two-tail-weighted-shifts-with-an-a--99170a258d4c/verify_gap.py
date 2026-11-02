"""Exact rational checks for the two-tail weighted-shift gap identity.

Run: python verify_gap.py
Only finite checks are implemented here. The infinite-dimensional theorem
uses the telescoping identity reproduced in the mathematical proof.
"""
from fractions import Fraction as F
from random import Random

rng = Random(90271)
ZERO = (F(0), F(0))

def minus(a,b): return (a[0]-b[0],a[1]-b[1])
def times_real(t,a): return (t*a[0],t*a[1])
def times_complex(t,a): return (t[0]*a[0]-t[1]*a[1],t[0]*a[1]+t[1]*a[0])
def sq(a): return a[0]*a[0]+a[1]*a[1]
def v(y,n): return y.get(n,ZERO)

def check(alpha,r,beta,kappa,y):
    assert 0<alpha<r<beta
    nlo=min(y)-2; nhi=max(y)+2
    left=sum((sq(minus(times_real(beta,v(y,n+1)),times_real(r,v(y,n)))) for n in range(nlo,-0)),F(0))
    right=sum((sq(minus(times_real(alpha,v(y,n+1)),times_real(r,v(y,n)))) for n in range(1,nhi+1)),F(0))
    center=sq(minus(times_complex((kappa[0],-kappa[1]),v(y,1)),times_real(r,v(y,0))))
    grad_left=sum((sq(minus(v(y,n+1),v(y,n))) for n in range(nlo,0)),F(0))
    grad_right=sum((sq(minus(v(y,n+1),v(y,n))) for n in range(1,nhi+1)),F(0))
    left_formula=(beta-r)**2*sum((sq(v(y,n)) for n in range(nlo,-0)),F(0))+beta*(beta-r)*sq(v(y,0))+r*beta*grad_left
    right_formula=(r-alpha)**2*sum((sq(v(y,n)) for n in range(2,nhi+1)),F(0))+r*(r-alpha)*sq(v(y,1))+r*alpha*grad_right
    assert left==left_formula
    assert right==right_formula
    d=min(beta-r,r-alpha)
    totalnorm=sum((sq(z) for z in y.values()),F(0))
    assert left+right+center>=d*d*totalnorm
    return 3

checks=0
for i in range(700):
    r=F(rng.randint(3,20),rng.randint(2,8))
    alpha=r*F(rng.randint(1,8),10)
    beta=r*F(rng.randint(11,25),10)
    kappa=(F(rng.randint(-10,10),7),F(rng.randint(-10,10),9))
    if kappa==ZERO:kappa=(F(1),F(0))
    width=rng.randint(2,15)
    y={n:(F(rng.randint(-5,5),rng.randint(1,9)),F(rng.randint(-5,5),rng.randint(1,8))) for n in range(-width,width+1)}
    checks+=check(alpha,r,beta,kappa,y)

# Weyl tail blocks: identity for all positive integer L.
for i in range(500):
    r=F(rng.randint(2,20),rng.randint(1,10))
    alpha=r*F(rng.randint(1,9),10)
    beta=r*F(rng.randint(11,30),10)
    L=rng.randint(1,100)
    # Constant vectors supported on long blocks in the respective constant tails.
    qleft=(F(L-1)*(beta-r)**2+beta**2+r**2)/L
    qright=(F(L-1)*(r-alpha)**2+alpha**2+r**2)/L
    assert qleft==(beta-r)**2+2*r*beta/L
    assert qright==(r-alpha)**2+2*r*alpha/L
    checks+=2

print(f"PASS: {checks} exact rational assertions; no infinite proof inferred from them")
