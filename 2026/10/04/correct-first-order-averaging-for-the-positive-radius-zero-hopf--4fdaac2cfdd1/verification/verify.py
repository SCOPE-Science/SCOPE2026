#!/usr/bin/env python3
from fractions import Fraction as Q


def corrected(b,a,d,c,j,e):
    w2 = b-Q(1)
    assert w2 == 1, "this replay intentionally uses b=2 so omega=1 exactly"
    S = a*w2 + j
    U = S/e
    r2 = Q(2)*c*(Q(1)+w2)*S/e
    det = c*S*(a+d)  # omega=1
    # quadratic: lambda^2 + c lambda - c*S
    quad = (Q(1), c, -c*S)
    return S,U,r2,det,quad

# Stable corrected branch omitted by the printed source condition.
b,a,d,c,j,e = map(Q, [2,1,2,1,-2,-1])
S,U,r2,det,quad = corrected(b,a,d,c,j,e)
assert S == -1
assert U == 1
assert r2 == 4
assert det == -3
assert quad == (1,1,1)
assert a+d > 0 and c > 0 and S < 0
source_difference = a*(b-1)*(b-1)-j
source_existence = c*source_difference/e
assert source_difference == 3
assert source_existence == -3

# Same parameters except e=+1: printed condition accepts, corrected r^2 is negative.
e = Q(1)
S,U,r2,det,quad = corrected(b,a,d,c,j,e)
source_existence = c*(a*(b-1)*(b-1)-j)/e
assert source_existence == 3 > 0
assert r2 == -4 < 0
assert U == -1

# At the stable witness the corrected average vanishes exactly at (r,Z,U)=(2,0,1).
e = Q(-1); r=Q(2); Z=Q(0); U=Q(1); w=Q(1)
f_r = r*(e*U-j-a*w*w)/(Q(2)*w**3)
f_Z = Z*(j-e*U-d*w*w)/(w**3)
f_U = (-Q(2)*c*U + Q(2)*Z*Z/w**4 + r*r/(Q(1)+w*w))/(Q(2)*w)
assert (f_r,f_Z,f_U) == (0,0,0)

print('VERIFY_OK')
print('stable_witness: S=-1 U=1 r2=4 det=-3 quadratic=(1,1,1)')
print('printed_condition_at_stable_witness=-3')
print('printed_accepts_e_plus_1=3 corrected_r2=-4')
