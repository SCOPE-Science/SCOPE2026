#!/usr/bin/env python3
from fractions import Fraction as Q
from math import factorial

def taylor_sum(x, n):
    return sum((x**j)/Q(factorial(j),1) for j in range(n+1))

def exp_upper(x, n):
    # For x>0 and x/(n+2)<1, the omitted positive Taylor tail is
    # at most t_{n+1}/(1-x/(n+2)).
    s=taylor_sum(x,n)
    nxt=(x**(n+1))/Q(factorial(n+1),1)
    r=x/Q(n+2,1)
    assert 0 < r < 1
    return s+nxt/(1-r)

# Exact rational certificates for 2.83 < ln(17) < 2.84.
xlo=Q(283,100); xhi=Q(284,100)
assert exp_upper(xlo,10) < 17            # exp(2.83) < 17
assert taylor_sum(xhi,10) > 17           # exp(2.84) > 17
# Hence L=ln 17 lies in (2.83,2.84), s=sqrt(L) obeys 1.68<s<2.
assert Q(42,25)**2 < xlo
assert xhi < 4

# Published parameters a=13/5,b=1/5,c=5,d=17,k=3.
# Base cubic: q_sigma(l)=l^3+A l^2+B_sigma l+C,
# A=14/5, B_sigma=17L+sigma*39/(5s), C=(442/5)L.
# 1/s < 25/42 follows from s>42/25.
A=Q(14,5)
inv_s_upper=Q(25,42)
Bminus_lower=17*xlo-Q(39,5)*inv_s_upper
Bplus_upper=17*xhi+Q(39,5)*inv_s_upper
C_lower=Q(442,5)*xlo
assert Bminus_lower > 0
assert Bplus_upper > Bminus_lower
assert A*Bplus_upper < C_lower
# Thus B_±>0 and A B_± - C<0. The Routh first column has signs +,+,-,+,
# so each base cubic has exactly two roots in Re(lambda)>0 and one in Re(lambda)<0.

# Fiber eigenvalue signs. s<2 gives 3/s>3/2.
b=Q(1,5); k=Q(3,1)
assert b-Q(3,2) < 0   # z_+=b-3/s < b-3/2 <0
assert b > 0          # z_-=b+3/s >0

print('VERIFY_OK')
