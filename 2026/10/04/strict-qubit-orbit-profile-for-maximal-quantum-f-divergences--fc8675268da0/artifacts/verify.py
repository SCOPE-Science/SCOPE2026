#!/usr/bin/env python3
from fractions import Fraction as Q
import math

def t_of_q(r,s,q):
    same = r/s + (1-r)/(1-s)
    opp = r/(1-s) + (1-r)/s
    return q*same + (1-q)*opp

def kernel(delta,t,a):
    return (a+1)*(t-delta-1)/(delta+a*t+a*a)

def kernel_deriv(delta,t,a):
    return (a+1)*(a+1)*(delta+a)/(delta+a*t+a*a)**2

r=Q(4,5); s=Q(7,10)
delta=r*(1-r)/(s*(1-s))
Delta=(2*r-1)*(2*s-1)/(s*(1-s))
tmin=r/s+(1-r)/(1-s)
assert Delta > 0
for q in [Q(0),Q(1,5),Q(3,5),Q(1)]:
    assert t_of_q(r,s,q) == tmin + Delta*(1-q)

# Exact kernel identity after Cayley-Hamilton reduction, tested by the
# closed trace-resolvent expression Tr sigma (A+aI)^-1=(t+a-1)/D.
for q in [Q(0),Q(1,5),Q(3,5),Q(1)]:
    t=t_of_q(r,s,q)
    for a in [Q(0),Q(1,3),Q(2),Q(7,2)]:
        D=delta+a*t+a*a
        resol=(t+a-1)/D
        lhs=1-(a+2)+(a+1)*(a+1)*resol
        rhs=kernel(delta,t,a)
        assert lhs == rhs
        assert kernel_deriv(delta,t,a) > 0

# Strict q-monotonicity for a non-affine positive combination of kernels.
def F(q):
    t=t_of_q(r,s,q)
    return Q(2,5)*(t-delta-1) + Q(3,7)*kernel(delta,t,Q(1,2)) + Q(5,11)*kernel(delta,t,Q(3))
qs=[Q(0),Q(1,5),Q(2,5),Q(3,5),Q(4,5),Q(1)]
vals=[F(q) for q in qs]
assert all(vals[i] > vals[i+1] for i in range(len(vals)-1))

# Representative quadratic coefficient for one kernel generator.
a=2.0
rf=float(r); sf=float(s); de=float(delta); De=float(Delta); tm=float(tmin)
def kf(t): return (a+1)*(t-de-1)/(de+a*t+a*a)
def kd(t): return (a+1)**2*(de+a)/(de+a*t+a*a)**2
coef=De*kd(tm)
for th in [1e-2,5e-3,2e-3]:
    diff=kf(tm+De*(math.sin(th)**2))-kf(tm)
    ratio=diff/(th*th)
    assert abs(ratio-coef) < 5e-4
print('VERIFY_OK')
