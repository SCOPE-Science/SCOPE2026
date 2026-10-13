"""Exact arithmetic checks for a quadratic-behavior SIS periodic-orbit theorem.

The global periodic-orbit inference uses the Poincare-Bendixson theorem and a
proved invariant compact set; finite arithmetic alone cannot certify it.
"""
from fractions import Fraction as F

R = F(640, 437)
tau = F(39, 10)
alpha = F(2)
chi = F(1)
q = F(1)
I = F(43, 480)
B = F(1, 4)

def f(i, b):
    return i * (R * (1-i) * (1-q*b) - 1)

def g(i, b):
    return alpha * ((tau*b*b + chi*i) * (1-b) - b)

assert f(I, B) == 0 and g(I, B) == 0
assert R > 1 and tau < 4 and alpha > 0 and chi > 0 and q == 1
assert 0 < I < 1 and 0 < B < 1

# Jacobian with state order (I, B).
j11 = R * ((1 - 2*I)*(1 - B)) - 1
j12 = -R*I*(1-I)
j21 = alpha*chi*(1-B)
j22 = alpha*(2*tau*B*(1-B) - (tau*B*B+chi*I) - 1)
assert (j11,j12,j21,j22) == (F(-43,437),F(-43,360),F(3,2),F(31,120))
tr=j11+j22
det=j11*j22-j12*j21
disc=tr*tr-4*det
assert tr == F(8387, 52440) > 0
assert det == F(1075, 6992) > 0
assert disc == F(-1620848231, 2749953600) < 0

# Disease-free equilibrium has eigenvalues R-1 and -alpha.
assert R-1 == F(203, 437) > 0
assert -alpha < 0

# Endemic equilibrium admissible B range and uniqueness: h'>0.
bmax = 1-1/R
assert bmax == F(203,640)
assert B < bmax
h_at_zero = -bmax
h_at_right = bmax/(1-bmax) - tau*bmax*bmax
assert h_at_zero < 0 and h_at_right > 0
# Lower bound on (1-B)^2*h'(B) over [0,bmax] via max B(1-B)^2=4/27.
hprime_numerator_lower = (1+1/R) - 2*tau*F(4,27)
assert hprime_numerator_lower == F(15185, 28800) > 0

# Persistence barrier L=I*exp(-30*B), L'/L >= R-1 - (R+60)*I.
assert F(3,2)-R == F(31,874) > 0
assert tau*F(1,4) == F(39,40) < 1
assert alpha*(tau*F(1,4)-1) == F(-1,20)
epsilon = (R-1) / (2*(R+60))
assert epsilon == F(203,53720) > 0
assert (R-1) - (R+60)*epsilon == (R-1)/2
# Interior square boundary checks: f(1,B)=-1, g(I,1)=-2;
# g(I,0)=2I; f(0,B)=0.
for b in (F(0),F(1,4),F(1,2),F(1)):
    assert f(0,b)==0 and f(1,b)==-1
for i in (F(0),F(1,10),F(1)):
    assert g(i,0)==2*i and g(i,1)==-2

# A simple outer upper-face condition guarantees a compact interior trap.
assert alpha*((tau+1)/10 - F(9,10)) == F(-41,50) < 0
print('VERIFY_OK')
