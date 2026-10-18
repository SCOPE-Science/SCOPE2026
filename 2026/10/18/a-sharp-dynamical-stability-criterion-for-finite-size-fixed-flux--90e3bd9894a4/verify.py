"""Standard-library verification of a fixed-flux population example.

Proof of all-parameter spectral assertions is analytical in RESULT.md.
"""
from fractions import Fraction as Q
from math import sqrt, exp, log, isclose

def g(x): return x*x - Q(9, 5)*x + 1
def h(x): return x*g(x)
def hp(x): return 3*x*x - Q(18,5)*x + 1

def near(x,y, tol=1e-11): assert abs(float(x)-float(y))<tol, (x,y)

assert g(Q(9,10)) == Q(19,100)
assert g(Q(0)) == 1
assert h(Q(3,5)) == Q(21,125)
assert hp(Q(3,5)) == -Q(2,25)
# Polynomial identity verified coefficient by coefficient.
# (x-3/5)(x^2-6x/5+7/25) = x^3-9x^2/5+x-21/125.
poly=[Q(-3,5),Q(1)]
quad=[Q(7,25),Q(-6,5),Q(1)]
res=[sum((poly[i]*quad[j] for i in range(2) for j in range(3) if i+j==k), Q(0)) for k in range(4)]
assert res == [-Q(21,125),Q(1),-Q(9,5),Q(1)]
for sign in [-1,1]:
    x=(3+sign*sqrt(2))/5
    near(float(h(x)), float(Q(21,125)))
    near(hp(x),Q(4,25))
    assert g(x)>0
critlo=(9-sqrt(6))/15
crithi=(9+sqrt(6))/15
near(hp(critlo),0)
near(hp(crithi),0)
near(h(critlo), Q(21,125) + 4*sqrt(6)/1125)
near(h(crithi), Q(21,125) - 4*sqrt(6)/1125)
assert 0 < critlo < crithi
J=1-exp(-1)
Bminus=float(h(crithi))/J
Bplus=float(h(critlo))/J
Bmid=float(Q(21,125))/J
assert Bminus < Bmid < Bplus
for x in [(3-sqrt(2))/5, (3+sqrt(2))/5]:
    near(h(x),Bmid*J)
    R=-(Bmid*(2*x-9/5))/g(x)**2
    near(1-R*(1-exp(-1)), float(hp(x))/g(x))
for k in (0.001,0.1,1.,3.,10.):
    assert exp(k)-1>k
print("PASS: exact polynomial, folds, stationary masses, signs, and normalized spectral identities")

