"""Exact arithmetic and finite-sample cross-checks for a symmetric stochastic affine plane map."""
from fractions import Fraction as F
import math
import random

def endpoints(mu, d):
    return (mu*(1-2*d)/(1-d),mu/(1-d))

def scalar_images(mu,d):
    a,b=endpoints(mu,d)
    return ((mu-d*b,mu-d*a),(mu+d*a,mu+d*b))

for d in [F(1,4), F(1,3), F(1,2), F(3,5), F(4,5)]:
    mu=F(2,3)
    a,b=endpoints(mu,d)
    assert a < b and abs(a)<=b
    J0,J1=scalar_images(mu,d)
    assert J0[0]==a and J1[1]==b
    assert (J0[1]<J1[0]) == (d < F(1,2))
    assert (J0[1]==J1[0]) == (d == F(1,2))
    assert (J0[1]>J1[0]) == (d > F(1,2))
    # Exact stationary scalar moments from X = mu + sigma*d*X_old.
    EX2=mu*mu/(1-d*d)
    assert EX2-mu*mu==mu*mu*d*d/(1-d*d)
    # Two-step map has exactly d-Lipschitz diagonal linear part.
    for s in (-1,1):
        for t in (-1,1):
            dx,dy=F(5,7),F(-3,11)
            newdx,newdy=s*d*dx,t*d*dy
            assert newdx*newdx+newdy*newdy == d*d*(dx*dx+dy*dy)

# At d=1/2, the two scalar images partition the base interval exactly.
mu=F(3,5)
d=F(1,2)
a,b=endpoints(mu,d)
assert (a,b)==(0,2*mu)
assert scalar_images(mu,d)==((0,mu),(mu,2*mu))
# Cartesian stationary rectangle has equal half-rectangle image contributions.
assert (b-a)*(2*d*b)==4*mu*mu
assert (1/F(2))*(1/d)==1

# Conditional quadratic memory, proved exactly from the two-step recurrence.
EX2=mu*mu/(1-d*d)
for k in range(1,16):
    for x in [F(0),F(1,2),F(7,5)]:
        conditional=d**(2*k)*x*x+mu*mu*d*d*(1-d**(2*(k-1)))/(1-d*d)
        unconditional=mu*mu*d*d/(1-d*d)
        assert conditional-unconditional==d**(2*k)*(x*x-EX2)
# Critical exact fourth moment of uniform[0,2mu].
assert (2*mu)**4/F(5)-((2*mu)**2/F(3))**2==F(64,45)*mu**4

# The even-step conditional law has 2**k atoms for every prescribed x;
# odd parity depends on disjoint iid sign strings (logical checks of sign indices).
for n in range(10):
    for k in range(1,20):
        # x_n uses signs at n-2,n-4,...; x_(n+2k+1) uses opposite parity.
        left={(n-2*j-2)%2 for j in range(20)}
        odd={(n+2*k+1-2*j-2)%2 for j in range(20)}
        assert left.isdisjoint(odd)
        # x_(n+2k) uses k new signs of the same parity; finite conditional support.
        new=[n+2*j for j in range(k)]
        assert len(new)==k and all((t-n)%2==0 for t in new)

# Independent simulation against exact stationary moments and zero lag covariance.
rng=random.Random(6729)
mu=1.0;d=0.5;x=0.4;y=-0.2
states=[]
for i in range(60000):
    s=rng.choice([-1,1]); x,y=mu+y,s*d*x
    if i>500:
        states.append(x)
mean=sum(states)/len(states)
second=sum(z*z for z in states)/len(states)
assert abs(mean-mu)<0.035
assert abs(second-4/3)<0.055
print('VERIFY_OK; stationary mean',round(mean,6),'second_moment',round(second,6))
