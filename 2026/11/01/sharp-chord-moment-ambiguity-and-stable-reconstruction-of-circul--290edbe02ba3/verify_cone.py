#!/usr/bin/env python3
"""Independent finite arithmetic and quadrature checks for cone-sidewall chord moments.

Run: python3 verify_cone.py
Uses only the Python standard library. The mathematical proof is in RESULT.md.
"""
from fractions import Fraction as F
from math import comb, cos, pi


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([v * c for v in a])


def mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x * y
    return trim(out)


def power(a, n):
    out = [F(1)]
    for _ in range(n):
        out = mul(out, a)
    return out


def diff(a):
    return trim([i * a[i] for i in range(1, len(a))] or [F(0)])


def radial(n):
    return F(2, n+2)  # density 2*t, on 0<t<1


def angular_z(j):
    # z=1-k+k*cos(phi), phi uniform; odd cosine moments vanish.
    out = [F(0)]
    for ell in range(0, j+1, 2):
        moment = F(comb(ell, ell//2), 2**ell)
        term = mul(power([F(1), F(-1)], j-ell), power([F(0), F(1)], ell))
        out = add(out, scale(term, comb(j, ell)*moment))
    return out


def chord_moment(m):
    # E[(t^2+u^2-2*t*u*z)^m] with independent density 2t, 2u.
    out = [F(0)]
    for j in range(m+1):
        radial_sum = sum((F(comb(m-j,t))*radial(2*t+j)*radial(2*(m-j-t)+j)
                          for t in range(m-j+1)), F(0))
        out = add(out, scale(angular_z(j), comb(m,j)*(-2)**j*radial_sum))
    return out


expected = {
    1: [F(1,9), F(8,9)],
    2: [F(1,30), F(4,30), F(45,30)],
    3: [F(5,350), F(16,350), F(84,350), F(1120,350)],
}
count = 0
for m in (1,2,3):
    assert chord_moment(m) == expected[m], (m, chord_moment(m))
    count += len(expected[m])

A = [F(1), F(4), F(45)]
B = [F(1), F(8)]
C = [F(40), F(1668), F(11207), F(32760)]
P = [F(354), F(-2137), F(4312)]
Q = [F(13465), F(-59912), F(68992)]
assert add(mul(diff(A), B), scale(A, -16)) == [F(-12), F(58)]
assert add(mul(diff(C), B), scale(C, -24)) == scale(P, 2)
assert add(mul(diff(P), B), scale(P, -32)) == scale(Q, -1)
assert P[1]**2-4*P[0]*P[2] == -1539023
assert Q[1]**2-4*Q[0]*Q[2] == -126461376
count += 5


def m_exact(m, k):
    return sum(v*k**i for i,v in enumerate(expected[m]))


def K(k):
    return m_exact(2,k)/m_exact(1,k)**2


def J(k):
    return m_exact(3,k)/m_exact(1,k)**3


def T(k):
    return J(k)-5*K(k)

k0=F(6,29)
assert K(k0)==F(1107,770)
assert K(F(0))==F(27,10) and K(F(1))==F(5,3)
assert T(F(0))==F(-108,35) and T(F(1))==F(-29,6)
assert F(27,175)*F(2529,9**4)==F(281,4725)
count += 5

for k in [F(1,100),F(1,10),F(1,8),F(1,4),F(1,2),F(3,4),F(99,100)]:
    y=F(19*k+12,464*k-19)
    # The involution is meaningful when both shapes are interior.
    if 0 < y < 1:
        assert K(k)==K(y)
        if k != k0:
            assert J(k)!=J(y)
        assert F(19*y+12,464*y-19)==k
        count += 3

# Algebraic identity for every pair of shape parameters, not sample-only.
# A(k)*B(y)^2-A(y)*B(k)^2=(k-y)*(464*k*y-19*k-19*y-12).
def biv_add(*terms):
    out = {}
    for term in terms:
        for exp, v in term.items():
            out[exp] = out.get(exp, F(0)) + v
    return {e:v for e,v in out.items() if v}

def biv_mul(a, b):
    out = {}
    for (i,j),v in a.items():
        for (m,n),w in b.items():
            out[(i+m,j+n)] = out.get((i+m,j+n),F(0))+v*w
    return {e:v for e,v in out.items() if v}

def biv_pow(a,n):
    r={(0,0):F(1)}
    for _ in range(n):r=biv_mul(r,a)
    return r

kvar={(1,0):F(1)}; yvar={(0,1):F(1)}; one={(0,0):F(1)}
Ak=biv_add(one,biv_mul({(0,0):F(4)},kvar),biv_mul({(0,0):F(45)},biv_pow(kvar,2)))
Ay=biv_add(one,biv_mul({(0,0):F(4)},yvar),biv_mul({(0,0):F(45)},biv_pow(yvar,2)))
Bk=biv_add(one,biv_mul({(0,0):F(8)},kvar))
By=biv_add(one,biv_mul({(0,0):F(8)},yvar))
lhs=biv_add(biv_mul(Ak,biv_pow(By,2)),biv_mul({(0,0):F(-1)},biv_mul(Ay,biv_pow(Bk,2))))
rhs=biv_mul(biv_add(kvar,biv_mul({(0,0):F(-1)},yvar)),
            biv_add(biv_mul({(0,0):F(464)},biv_mul(kvar,yvar)),
                    biv_mul({(0,0):F(-19)},kvar),biv_mul({(0,0):F(-19)},yvar),{(0,0):F(-12)}))
assert lhs==rhs
count += 1

# Directly integrate ambient Euclidean distances on a midpoint radial grid.
# This is deliberately separate from the exact moment-expansion calculation.
def numeric_moments(k, n=256, nphi=8):
    w = [2*(i+0.5)/(n*n) for i in range(n)]
    t = [(i+0.5)/n for i in range(n)]
    c = [cos(2*pi*j/nphi) for j in range(nphi)]
    moments = [0.0,0.0,0.0]
    for i, u in enumerate(t):
        for j, v in enumerate(t):
            wt=w[i]*w[j]/nphi
            for cv in c:
                d2=(u-v)**2 + 2*float(k)*u*v*(1-cv)
                d4=d2*d2
                moments[0]+=wt*d2
                moments[1]+=wt*d4
                moments[2]+=wt*d4*d2
    return moments

max_error=0.0
for k in [F(1,20),F(1,10),k0,F(1,2),F(9,10)]:
    numerical=numeric_moments(k)
    for m,observed in zip((1,2,3),numerical):
        err=abs(observed-float(m_exact(m,k)))
        max_error=max(max_error,err)
        assert err<0.00020,(k,m,err)
        count+=1
print('VERIFY_OK', 'exact_polynomial_and_rational_checks=',count-15,
      'independent_quadratures=15', 'max_absolute_quadrature_error=',format(max_error,'.9g'))
