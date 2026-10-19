"""Exact, independently repeatable algebra checks for heterogeneous adaptive SIS equilibria.

This finite verifier illustrates the theorem; the arbitrary-network existence claim
is established by the analytical fixed-point argument, not by enumeration.
"""
from fractions import Fraction as Q
from math import sqrt

checks = 0

def require(condition):
    global checks
    assert condition
    checks += 1


def witness(y1, y2, xi=Q(1), zeta=Q(1), creation=None):
    # Set the edge equilibrium response, then choose transmission rates to
    # realize the prescribed strictly positive pair as an exact equilibrium.
    if creation is None:
        creation = Q(1)
    breaking = y1 + y2
    z = xi * creation / (zeta * breaking + xi * creation)
    beta12 = (y1 / (1-y1)) / (y2*z)
    beta21 = (y2 / (1-y2)) / (y1*z)
    # At the disease-free equilibrium the breaking response is zero and
    # the creation response in these families is strictly positive.
    z0 = Q(1)
    r0_squared = beta12*beta21*z0*z0
    require(z > 0)
    require(z <= 1)
    require(beta12 > 0 and beta21 > 0)
    require(-y1+(1-y1)*beta12*y2*z == 0)
    require(-y2+(1-y2)*beta21*y1*z == 0)
    require(-z*zeta*breaking + xi*(1-z)*creation == 0)
    require(r0_squared > 1)
    require(Q(1)/(1 + y1 + y2) > 0)
    require(Q(0) < y1 < Q(1))
    require(Q(0) < y2 < Q(1))
    # In this 2x2 bipartite example the source's minimum-row criterion can
    # fail even though the reproduction number exceeds one.
    require(beta12*beta21 > 1)
    return z, beta12, beta21, r0_squared


z,b12,b21,r2 = witness(Q(7,10),Q(1,10))
require(z == Q(5,9))
require(b12 == 42)
require(b21 == Q(2,7))
require(r2 == 12)
require(min(b12,b21) < 1)
require(sqrt(float(r2)) > 1)

for i in range(1,20):
    for j in range(1,20):
        y1,y2=Q(i,20),Q(j,20)
        # Constant positive link creation.
        witness(y1,y2)
        # Nonconstant creation, positive even at the boundary.
        witness(y1,y2,xi=Q(3,2),zeta=Q(7,4),creation=Q(1)-(y1+y2)/4)

print(f"PASS: {checks} exact rational assertions")
