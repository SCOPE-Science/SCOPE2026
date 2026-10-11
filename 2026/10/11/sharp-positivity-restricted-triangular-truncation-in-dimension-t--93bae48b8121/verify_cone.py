"""Exact identities for positivity-restricted 3-by-3 triangular truncation."""
from fractions import Fraction
from math import sqrt
from random import Random

# Pair (a,b) represents a+b*sqrt(2) over Q.
def q(a=0,b=0): return (Fraction(a),Fraction(b))
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def scale(x,c): return (x[0]*c,x[1]*c)
def fmt(x): return str(x[0])+" + ("+str(x[1])+")sqrt(2)"

t=q(Fraction(2,7),Fraction(1,14))
y=sub(q(1),scale(t,2))
C=q(Fraction(1,7),Fraction(2,7))
# At the extremizer, sqrt(4t-7t^2)=7t-2.
discriminant=sub(scale(t,4),scale(mul(t,t),7))
radical=sub(scale(t,7),q(2))
assert discriminant==mul(radical,radical)
assert scale(add(t,radical),Fraction(1,2))==C
# Characteristic polynomial of B*B evaluated at lambda=C^2.
csq=mul(C,C)
trace=add(mul(y,sub(q(1),y)),mul(t,t))
det=mul(mul(t,t),mul(y,y))
assert add(sub(mul(csq,csq),mul(trace,csq)),det)==q()
assert add(scale(t,2),y)==q(1)
# Scalar critical equation and optimal root.
assert sub(add(scale(mul(t,t),14),q(1)),scale(t,8))==q()
assert C==sub(scale(t,4),q(1))

rng=Random(104)
for _ in range(20000):
    a,b,c=(rng.random(),rng.random(),rng.random())
    s=a+b+c
    x,z,y0=a/s,c/s,b/s
    tr=y0*(1-y0)+x*z
    det0=x*z*y0*y0
    top=(tr+sqrt(max(0.0,tr*tr-4*det0)))/2
    assert top <= (float(C[0])+float(C[1])*sqrt(2))**2+1e-12

print("Exact radical identities, optimal projection polynomial, and critical point: PASS")
print("20,000 diagnostic simplex samples: PASS (not a proof)")
print("Sharp coefficient:",fmt(C),"~",float(C[0])+float(C[1])*sqrt(2))
