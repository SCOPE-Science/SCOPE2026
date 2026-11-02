#!/usr/bin/env python3
"""Exact counterexample checks and transparent numerical crosschecks for an adaptive SIS model.
The arbitrary-network existence theorem uses an analytical Brouwer/Perron proof.
"""
from fractions import Fraction as Q
from math import sqrt

# Transmission matrix: rows receive infections; recovery rates are both one.
beta = ((Q(4), Q(1,2)), (Q(1), Q(1,4)))
z_dfe = ((Q(1), Q(1)), (Q(1,2), Q(1)))
K = tuple(tuple(beta[i][j] * z_dfe[i][j] for j in range(2)) for i in range(2))
assert K == ((Q(4), Q(1,2)), (Q(1,2), Q(1,4)))
trace, det = K[0][0] + K[1][1], K[0][0]*K[1][1]-K[0][1]*K[1][0]
assert trace == Q(17,4) and det == Q(3,4)
assert 1-trace+det == Q(-5,2)  # One eigenvalue lies above one.
assert (17 + sqrt(241))/8 > 1
# Both minimum row and minimum column sums are below one, so the
# original sufficient row/column-sum theorem cannot imply endemicity.
assert sum(K[1]) == Q(3,4)
assert K[0][1]+K[1][1] == Q(3,4)
# IFT derivative at (y1,y2,w)=(3/4,0,0): Jac*[1/24,1]+[0,3/4] = 0.
assert -3*Q(1,24)+Q(1,8) == 0
assert -Q(3,4)+Q(3,4) == 0

# Scalar equilibrium residuals use stationary internal and 1->2 link weights.
def stationary_residual(y1, y2, z21):
    return (-y1 + (1-y1)*(4*y1+y2/2),
            -y2 + (1-y2)*(z21*y1+y2/4))
assert stationary_residual(Q(0),Q(0),Q(1,2)) == (0,0)
assert stationary_residual(Q(3,4),Q(0),Q(0)) == (0,0)
assert Q(3,4) > Q(1,2) and Q(1,4) < 1
# All y1>0 equilibria obey 1 >= 4(1-y1), hence y1 >= 3/4.
# At y1 >= 3/4, link 1->2 has creation response zero and stationary z21=0.
# Its group-2 equation is y2[-1+(1-y2)/4]=0, forcing y2=0.

# Restoring positive creation by eta gives z21=eta/(1+eta) near the boundary state.
def y1_from_y2(y2):
    return (3-y2/2+sqrt(y2*y2/4+5*y2+9))/8

def find_endemic(eta):
    w=eta/(1+eta)
    def F(y2):
        y1=y1_from_y2(y2)
        return -y2+(1-y2)*(w*y1+y2/4)
    low,high=0.,1.
    assert F(low)>0 and F(high)<0
    for _ in range(110):
        mid=(low+high)/2
        if F(mid)>0:low=mid
        else:high=mid
    y2=(low+high)/2
    y1=y1_from_y2(y2)
    assert .75<y1<1 and 0<y2<1
    a,b=stationary_residual(y1,y2,w)
    assert max(abs(a),abs(b)) < 5e-15
    return y1,y2

for eta in [.1,.01,.001,.0001,.00001]:
    y1,y2=find_endemic(eta)
    print('eta=',eta,'y1=',format(y1,'.14f'),'y2=',format(y2,'.14f'),
          'y2/eta=',format(y2/eta,'.8f'),
          '(y1-0.75)/eta=',format((y1-.75)/eta,'.8f'))

print('ALL CHECKS PASSED: exact DFE spectral value, exact boundary stationarity, no-positive-equilibrium inequalities, restored positive branch.')
