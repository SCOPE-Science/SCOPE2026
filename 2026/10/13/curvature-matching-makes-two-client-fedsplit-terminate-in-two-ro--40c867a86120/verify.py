from fractions import Fraction
import math
import random
import numpy as np

def prox(w,a,b,s):
    return (w+s*a*b)/(1+s*a)

def direct_round(z1,z2,a1,a2,b1,b2,s):
    x=(z1+z2)/2
    u1=prox(2*x-z1,a1,b1,s)
    u2=prox(2*x-z2,a2,b2,s)
    return z1+2*(u1-x), z2+2*(u2-x)

def closed_round(z1,z2,a1,a2,b1,b2,s):
    r1=(1-s*a1)/(1+s*a1)
    r2=(1-s*a2)/(1+s*a2)
    return r1*z2+(1-r1)*b1, r2*z1+(1-r2)*b2

rng=random.Random(350058)
for _ in range(500):
    a1=10**rng.uniform(-1,1)
    a2=10**rng.uniform(-1,1)
    b1=rng.uniform(-3,3)
    b2=rng.uniform(-3,3)
    s=10**rng.uniform(-1,1)
    z1=rng.uniform(-4,4)
    z2=rng.uniform(-4,4)
    d=direct_round(z1,z2,a1,a2,b1,b2,s)
    c=closed_round(z1,z2,a1,a2,b1,b2,s)
    assert max(abs(d[0]-c[0]),abs(d[1]-c[1])) < 2e-12
    r1=(1-s*a1)/(1+s*a1); r2=(1-s*a2)/(1+s*a2)
    A=np.array([[0.0,r1],[r2,0.0]])
    assert np.linalg.norm(A@A-r1*r2*np.eye(2)) < 2e-14
    rho=max(abs(np.linalg.eigvals(A)))
    assert abs(rho-math.sqrt(abs(r1*r2))) < 2e-12
    B=np.array([[(1-r1)*b1],[(1-r2)*b2]])
    Z=np.linalg.solve(np.eye(2)-A,B).reshape(2)
    xstar=(a1*b1+a2*b2)/(a1+a2)
    assert abs((Z[0]+Z[1])/2-xstar) < 2e-11

for _ in range(200):
    a1=10**rng.uniform(-1,1); a2=10**rng.uniform(-1,1)
    b1=rng.uniform(-3,3); b2=rng.uniform(-3,3); x0=rng.uniform(-4,4)
    xstar=(a1*b1+a2*b2)/(a1+a2)
    for s in (1/a1,1/a2):
        z1=z2=x0
        z1,z2=direct_round(z1,z2,a1,a2,b1,b2,s)
        z1,z2=direct_round(z1,z2,a1,a2,b1,b2,s)
        assert abs((z1+z2)/2-xstar) < 5e-11
        z1n,z2n=direct_round(z1,z2,a1,a2,b1,b2,s)
        assert abs(z1n-z1)+abs(z2n-z2) < 5e-10

a1=Fraction(1); a2=Fraction(9)
b1=Fraction(-2); b2=Fraction(1); s=Fraction(1)
r1=(1-s*a1)/(1+s*a1); r2=(1-s*a2)/(1+s*a2)
assert r1 == 0 and r2 == Fraction(-4,5)
xstar=(a1*b1+a2*b2)/(a1+a2)
assert xstar == Fraction(7,10)
for x0 in (Fraction(-5,2), Fraction(0), Fraction(13,7)):
    z1=z2=x0
    z1,z2=closed_round(z1,z2,a1,a2,b1,b2,s)
    assert z1 == b1
    z1,z2=closed_round(z1,z2,a1,a2,b1,b2,s)
    assert (z1+z2)/2 == xstar
    assert closed_round(z1,z2,a1,a2,b1,b2,s) == (z1,z2)

for a1,a2 in ((1.0,4.0),(1.0,9.0),(0.25,16.0)):
    s=1/math.sqrt(a1*a2)
    r1=(1-s*a1)/(1+s*a1); r2=(1-s*a2)/(1+s*a2)
    formula=abs(math.sqrt(a2)-math.sqrt(a1))/(math.sqrt(a2)+math.sqrt(a1))
    assert abs(math.sqrt(abs(r1*r2))-formula) < 2e-15
    assert formula > 0

print("verification passed")
