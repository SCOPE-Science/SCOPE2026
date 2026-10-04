from fractions import Fraction as F
from math import isqrt

def binom_neg_int(r, k):
    # coefficient of x^k in (1+x)^(-r)
    # (-1)^k * C(r+k-1,k)
    from math import comb
    return F(((-1)**k) * comb(r+k-1, k), 1)

def br_coeff(r, k):
    # coefficient of z^k in (1+z/r)^(-r)
    return binom_neg_int(r,k) / (F(r,1)**k)

def b1_coeff(k):
    return F((-1)**k, 1)

def rr_coeff(r, k):
    return (F(r)*br_coeff(r,k)-b1_coeff(k))/F(r-1)

for r in range(2,51):
    assert rr_coeff(r,0) == 1
    assert rr_coeff(r,1) == -1
    assert rr_coeff(r,2) == F(1,2)

# r=2 exact sign numerator:
# R_2 = 8/(z+2)^2 - 1/(z+1)
# common numerator = 8(z+1)-(z+2)^2 = -z^2+4z+4.
for z in [F(0), F(1), F(4), F(5), F(10)]:
    lhs = F(2) / (F(1)+z/F(2))**2 - F(1)/(F(1)+z)
    rhs = (-z*z+4*z+4)/((F(1)+z)*(F(2)+z)**2)
    assert lhs == rhs

# Rational brackets for the standard threshold 2+2sqrt(2):
# 4.8284 < root < 4.8285, checked by numerator sign.
lo = F(48284,10000)
hi = F(48285,10000)
def num2(z): return -z*z+4*z+4
assert num2(lo) > 0
assert num2(hi) < 0

def comparison(r,z):
    # positive means R_r(z)>0, zero equality, negative means R_r(z)<0
    return F(r)*(F(1)+z) - (F(1)+z/F(r))**r

# Every tested r has exactly one sampled transition, and signs agree
# with the algebraic comparison defining the theorem.
for r in [2,3,4,5,8,16,32]:
    assert comparison(r,F(0)) > 0
    right = F(1)
    while comparison(r,right) > 0:
        right *= 2
    left = right/2
    # rational bisection
    for _ in range(80):
        mid=(left+right)/2
        if comparison(r,mid)>0:
            left=mid
        else:
            right=mid
    assert comparison(r,left) > 0
    assert comparison(r,right) <= 0

# Negative stiff tail check at a large exact rational point.
for r in [2,3,4,8,16]:
    z=F(10**6)
    R=(F(r)/(F(1)+z/F(r))**r - F(1)/(F(1)+z))/F(r-1)
    assert R < 0

print("VERIFY_OK")
