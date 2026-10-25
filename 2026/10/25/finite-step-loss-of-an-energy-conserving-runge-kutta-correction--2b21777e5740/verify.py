"""Exact arithmetic checks for a two-stage weight-corrected RK energy map.
Run with Python 3.10 or newer; no third-party packages are needed.
"""
from fractions import Fraction as F
from math import sqrt, isclose
import random

# Two-stage explicit Heun stages for planar rotations: t = h omega.
# With correction epsilon, the multiplier is (1 - b*t*t) + i*t,
# where b = 1/2-epsilon.
def gain(r, b):
    return (1-b*r)**2 + r

def near_branch(mu):
    assert 0 < mu <= 1
    return 1/(1+sqrt(1-mu))

def invariants(r, energy):
    s2 = sum(x*y for x,y in zip(r,energy))
    s4 = sum(x*x*y for x,y in zip(r,energy))
    return s2, s4

# Exact counterexample: frequencies 1/2 and 3/2, step h=1.
r = (F(1,4), F(9,4))
e = (F(27), F(1))
s2, s4 = invariants(r,e)
assert (s2,s4) == (F(9),F(27,4))
assert s4/s2 == F(3,4)
b = F(2,3)
assert s4*b*b-2*s2*b+s2 == 0
assert (gain(r[0],b),gain(r[1],b)) == (F(17,18),F(5,2))
e_next = tuple(gain(x,b)*y for x,y in zip(r,e))
assert e_next == (F(51,2),F(5,2))
assert sum(e_next) == sum(e)
s2_next, s4_next = invariants(r,e_next)
assert (s2_next,s4_next) == (F(12),F(57,4))
assert 4*s2_next*(s2_next-s4_next) == F(-108)
assert F(1,16) == (r[0]*(1-r[0]))/(r[0]*(1-r[0])+r[1]*(r[1]-1))
assert e[1]/sum(e) < F(1,16) < e_next[1]/sum(e_next)

# Verify the per-mode identity and conservation on a rational lattice.
for denominator in range(3,32):
    for n in range(1,denominator):
        # rational b in (1/2,1), mu=(2b-1)/b^2
        b = F(1,2) + F(n,2*denominator)
        mu = (2*b-1)/(b*b)
        if mu <= 0 or mu >= 1:
            continue
        r1 = mu*F(1,2)
        r2 = mu + F(1,2)
        p = r1*(mu-r1)/(r1*(mu-r1)+r2*(r2-mu))
        w = (1-p,p)
        s2,s4=invariants((r1,r2),w)
        assert s4/s2 == mu
        assert sum(ww*gain(rr,b) for ww,rr in zip(w,(r1,r2))) == 1
        for rr in (r1,r2):
            assert gain(rr,b)-1 == b*b*rr*(rr-mu)

# Independent floating tests for many-mode data.
random.seed(50721)
for _ in range(20000):
    n=random.randint(1,8)
    rs=[random.uniform(1e-4,1.9) for _ in range(n)]
    ee=[random.uniform(.01,4) for _ in range(n)]
    s2,s4=invariants(rs,ee)
    mu=s4/s2
    if mu>1: continue
    b=near_branch(mu)
    assert isclose(sum(ee[i]*gain(rs[i],b) for i in range(n)),sum(ee),rel_tol=1e-10,abs_tol=1e-10)
    assert 0.5<=b<=1.0

print('VERIFY_OK exact second-step infeasibility, rational modal identities, 20000 trials')
