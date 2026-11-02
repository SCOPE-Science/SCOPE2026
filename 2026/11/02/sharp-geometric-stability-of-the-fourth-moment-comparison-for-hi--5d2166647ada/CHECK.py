#!/usr/bin/env python3
"""Exact finite examples and reproducible checks for fourth-moment geometric stability."""
from fractions import Fraction as F
from itertools import product
from math import sqrt

def dot(u, v):
    return sum(x*y for x, y in zip(u, v))

def add(u, v):
    return tuple(x+y for x, y in zip(u, v))

def neg(u):
    return tuple(-x for x in u)

def expected(expressions):
    return sum(expressions, F(0)) / len(expressions)

def compute_tree(n, increment):
    outcomes=[]
    local=[]
    distances=[]
    for signs in product((-1,1),repeat=n):
        m=(F(0),F(0))
        acc=F(0)
        rg=0.0
        for k in range(n):
            x=increment(k,signs[:k+1],m)
            a2=dot(x,x)
            assert a2==1
            q=dot(m,m)
            z=dot(m,x)
            acc+=q*a2-z*z
            if q:
                rg+=q*(2*a2-2*sqrt(float(a2))*abs(float(z))/sqrt(float(q)))
            m=add(m,x)
        outcomes.append(dot(m,m)**2)
        local.append(acc)
        distances.append(rg)
    fourth=expected(outcomes)
    scalar=F(3*n*n-2*n)  # fourth moment of n independent unit Rademachers
    deficit=scalar-fourth
    assert deficit==4*expected(local), (n,deficit,expected(local))
    r=sum(distances)/len(distances)
    assert float(deficit)/4-1e-10<=r<=float(deficit)/2+1e-10
    return deficit,r

def fixed_angles(c,s):
    assert c*c+s*s==1
    def get(k,signs,m):
        eps=signs[-1]
        if k==0:return (F(eps),F(0))
        return (eps*c,eps*s)
    return compute_tree(2,get)

assert fixed_angles(F(0),F(1))==(F(4),2.0)
for a,b,h in [(3,4,5),(5,12,13),(8,15,17),(20,21,29),(99,20,101)]:
    d,r=fixed_angles(F(a,h),F(b,h))
    assert d==4*F(b*b,h*h)
    assert abs(r/float(d)-1/(2*(1+a/h)))<1e-12

# Third-step direction responds to both preceding signs, but remains conditionally fair.
def adaptive(k,signs,m):
    e=F(signs[-1])
    if k==0:return(e,F(0))
    if k==1:return(F(3,5)*e,F(4,5)*e)
    return (e,F(0)) if signs[0]*signs[1]>0 else (F(0),e)
assert compute_tree(3,adaptive)[0]>0

# Adaptive reset to a new axis at zero; all nonzero-state increments are radial.
def returning(k, signs,m):
    e=F(signs[-1])
    if k==0:return(e,F(0))
    if k==1:return(e*signs[0],F(0))
    if dot(m,m)==0:return(F(0),e)
    if m[0]!=0:return(e,F(0))
    return(F(0),e)
assert compute_tree(4,returning)[0]==0

# Both stability factors are sharp on n=2; ratio R/D tends to 1/4 as c -> 1.
assert abs((fixed_angles(F(0),F(1))[1]/4)-0.5)<1e-12
for n in (5,13,65):
    # Rational cosine close to 1 via (n^2-1,n^2+1,2n).
    c=F(n*n-1,n*n+1);s=F(2*n,n*n+1)
    d,r=fixed_angles(c,s)
    assert abs(r/float(d)-1/(2*(1+float(c))))<1e-10
print('PASS: exact martingale fourth-moment telescoping; adaptive directions; reset equality; two sharp stability constants.')
