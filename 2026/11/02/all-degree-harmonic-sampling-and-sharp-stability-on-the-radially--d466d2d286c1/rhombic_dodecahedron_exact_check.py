#!/usr/bin/env python3
"""Exact rational verification for the radially normalized rhombic-dodecahedron Legendre sampling theorem.

Only standard Python library. Handles 0<=k<120; the analytic tail uses Bernstein's inequality.
"""
from fractions import Fraction as F
from math import isqrt

LIMIT = 120

def legendre_at(q, max_degree):
    out = [F(1)]
    if max_degree:
        out.append(q)
    for n in range(1, max_degree):
        out.append(((2*n+1)*q*out[n] - n*out[n-1]) / (n+1))
    return out

def legendre_at_sqrt3_over3(max_degree):
    # Actual P_k(1/sqrt(3))=v_k*sqrt(3) if k odd, and =v_k if k even.
    out = [F(1)]
    if max_degree:
        out.append(F(1,3))
    for n in range(1, max_degree):
        # P_n(x) = out[n] * sqrt(3)^(n modulo 2), x=sqrt(3)/3
        # x * P_n(x) = out[n]*sqrt(3)/3 when n even, out[n] when n odd.
        x_pn_coeff = out[n]/3 if n%2==0 else out[n]
        out.append(((2*n+1)*x_pn_coeff-n*out[n-1])/(n+1))
    return out

a_list = legendre_at(F(1,3), LIMIT-1)
d_list = legendre_at(F(0), LIMIT-1)
c_list = legendre_at_sqrt3_over3(LIMIT-1)


def sectors(k):
    a,d,c = a_list[k],d_list[k],c_list[k]
    c2 = c*c*(3 if k%2 else 1)
    if k%2:
        return ([(1-3*a, 1)], (1+a, F(1), 4*c2, 3))
    return ([(1-a, 3),(1-d,2)], (1+3*a,1+2*d,12*c2,1))


def spectral_rank(k):
    scalar, (A,D,B2,m) = sectors(k)
    assert all(v >= 0 for v,j in scalar)
    total = sum(j for v,j in scalar if v>0)
    determinant = A*D-B2
    trace = A+D
    assert determinant>=0 and trace>=0 and A>=0 and D>=0
    if determinant>0:
        total += 2*m
    elif trace>0:
        total += m
    return total


def positive_shift(k, q, lower):
    # Exact check of eigenvalues > q (lower=True) or eigenvalues < q (lower=False).
    scalar, (A,D,B2,_) = sectors(k)
    if lower:
        return (all(v>q for v,j in scalar)
                and A>q and D>q and (A-q)*(D-q)>B2)
    return (all(v<q for v,j in scalar)
            and A<q and D<q and (q-A)*(q-D)>B2)


def envelope(k):
    # Certified fractional interval to 1e-5, using only exact rational operations.
    grid = 100000
    lo,hi = 0,grid*5
    assert positive_shift(k,F(0),True)
    while hi-lo>1:
        mid=(lo+hi)//2
        if positive_shift(k,F(mid,grid),True):
            lo=mid
        else:
            hi=mid
    lower=F(lo,grid)
    lo,hi=0,grid*5
    assert positive_shift(k,F(5),False)
    while hi-lo>1:
        mid=(lo+hi)//2
        if positive_shift(k,F(mid,grid),False):
            hi=mid
        else:
            lo=mid
    upper=F(hi,grid)
    assert positive_shift(k,lower,True)
    assert positive_shift(k,upper,False)
    return lower,upper

expected = [1,3,5,4,6,6,6,7,6,7,6,7,7,7,6] + [7]* (LIMIT-15)
assert len(expected)==LIMIT
for k in range(LIMIT):
    assert spectral_rank(k)==expected[k], (k,spectral_rank(k),expected[k])

# The exact k=7 block has eigenvalues (1337+-sqrt(889441))/1458;
# its fourth (simple) spectral eigenvalue is 364/243.
a, d, c = a_list[7],d_list[7],c_list[7]
assert (a,c)==(F(-121,729),F(5,27))
assert (1-3*a)==F(364,243)
assert F(889441) == (1458**2) * (((a*a+16*(3*c*c))/4))
# Exact isolating integers for the quadratic eigenvalue.
assert 943**2 < 889441 < 944**2
# sqrt(889441)>943 implies kappa_7 > 11/2.
assert 13*943 > 9*1337
# The remaining simple eigenvalue 364/243 lies strictly between lambda_- and lambda_+.
assert (F(364,243) > (F(1337)-F(943))/1458
        and F(364,243) < (F(1337)+F(943))/1458)

max_competitor_num=F(0)
max_competitor_degree=None
for k in range(7,LIMIT):
    if expected[k] != 7 or k==7:
        continue
    lower,upper=envelope(k)
    assert lower>0 and 2*upper<11*lower, (k,float(lower),float(upper),float(upper/lower))
    if upper/lower>max_competitor_num:
        max_competitor_num=upper/lower
        max_competitor_degree=k

# For k>=120: the distinct nontrivial dot products among representatives have |x|<=1/sqrt(3).
# Therefore sin(theta)>=sqrt(2/3)>4/5 and, by Bernstein, |P_k(x)|
# <sqrt(2/(pi*k*sin(theta)))<sqrt(5/(6*k))<=1/12.
# Each row of the 7x7 Gram has precisely six off-diagonal entries.
# Gershgorin gives eigenvalues in (1/2,3/2), hence kappa<3 < 11/2.
assert F(2,3)>F(4,5)**2
assert F(5,6*120)==F(1,12**2)

print('RHOMBIC_DODECAHEDRON_EXACT_CERTIFICATE_OK', LIMIT,
      'finite spectral degrees;',len([k for k in range(7,LIMIT) if expected[k]==7 and k!=7]),
      'strict competitor bounds;', 'worst rational enclosure degree',max_competitor_degree,
      'upper ratio',float(max_competitor_num))
